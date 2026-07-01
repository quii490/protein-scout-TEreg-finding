#!/usr/bin/env python3
"""Harvest structured protein facts for one human gene.

Reads pre-computed fields from nuclear_proteins_classified_human.xlsx, then
enriches with real-time API queries (UniProt, AlphaFold, PubMed, STRING, HPA).

Output: JSON to stdout — one object with keys:
  excel      – the Excel row dict
  uniprot    – UniProt REST API result
  alphafold  – AlphaFold API result
  pubmed     – PubMed E-utilities result
  string_ppi – STRING interaction partners
  hpa        – HPA probe result (image URLs)
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

CTX = ssl.create_default_context()

ROOT = Path(__file__).resolve().parents[2]
EXCEL = ROOT / "all_nuclear" / "nuclear_proteins_classified_human.xlsx"


def fetch_text(url: str, timeout: int = 25) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_json(url: str, timeout: int = 25) -> Any:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def safe_call(fn, *args, retries: int = 1, **kwargs):
    last = None
    for attempt in range(retries):
        try:
            return {"ok": True, "data": fn(*args, **kwargs)}
        except Exception as exc:
            last = exc
            if attempt + 1 < retries:
                time.sleep(1.0 + attempt)
    return {"ok": False, "error": f"{type(last).__name__}: {last}"}


# ── Excel lookup ──────────────────────────────────────────────────

def read_excel_row(gene: str) -> dict[str, Any] | None:
    import pandas as pd
    targets = ["unclassified_core_nuclear", "unclassified_bare",
               "families", "zinc_finger_nonfamily", "rbp_rnp_nonfamily",
               "suspicious_nonfamily", "hot_genes", "ChIP_data_summary"]
    for sheet in targets:
        df = pd.read_excel(EXCEL, sheet_name=sheet)
        match = df[df["gene_symbol"].str.upper() == gene.upper()]
        if len(match) == 0:
            continue
        row = match.iloc[0].to_dict()
        row["_sheet"] = sheet
        # Normalize types for JSON
        for k, v in row.items():
            if isinstance(v, (pd.Timestamp,)):
                row[k] = str(v)
            elif isinstance(v, (int, float, str, bool, type(None))):
                pass
            else:
                row[k] = str(v)
        return row
    return None


def primary_accession(row: dict[str, Any]) -> str | None:
    acc_str = str(row.get("uniprot_accession", "") or "")
    if not acc_str or acc_str.lower() == "nan":
        return None
    return acc_str.split(";")[0].strip()


# ── UniProt ───────────────────────────────────────────────────────

def _protein_name(entry: dict[str, Any]) -> str:
    desc = entry.get("proteinDescription", {})
    rec = desc.get("recommendedName") or {}
    full = rec.get("fullName") or {}
    return full.get("value") or desc.get("submissionNames", [{}])[0].get("fullName", {}).get("value") or ""


def uniprot_query(gene: str, known_acc: str | None) -> dict[str, Any]:
    """Fetch from UniProt REST.  Prefer known_acc; fall back to gene search."""
    entry = None
    if known_acc:
        try:
            full = fetch_json(f"https://rest.uniprot.org/uniprotkb/{known_acc}.json")
            entry = full
        except Exception:
            pass
    if entry is None:
        q = urllib.parse.quote(f"gene:{gene} AND organism_id:9606 AND reviewed:true")
        data = fetch_json(f"https://rest.uniprot.org/uniprotkb/search?query={q}&format=json&size=3")
        results = data.get("results", [])
        if not results:
            q = urllib.parse.quote(f"gene:{gene} AND organism_id:9606")
            data = fetch_json(f"https://rest.uniprot.org/uniprotkb/search?query={q}&format=json&size=3")
            results = data.get("results", [])
        if results:
            entry = results[0]

    if not entry:
        return {"found": False, "gene": gene}

    acc = entry.get("primaryAccession")
    comments = entry.get("comments", [])
    locs = []
    funcs = []
    interactions = []
    for c in comments:
        ct = c.get("commentType")
        if ct == "SUBCELLULAR LOCATION":
            for sl in c.get("subcellularLocations", []):
                loc = sl.get("location", {})
                locs.append({
                    "location": loc.get("locationValue") or loc.get("value"),
                    "evidences": [ev.get("evidenceCode") for ev in loc.get("evidences", [])],
                })
        elif ct == "FUNCTION":
            funcs.extend(t.get("value", "") for t in c.get("texts", []))
        elif ct == "INTERACTION":
            for item in c.get("interactions", []):
                interactions.append({
                    "accession": item.get("interactantOne", {}).get("uniProtKBAccession", ""),
                    "gene": item.get("interactantTwo", {}).get("geneName", ""),
                    "experiments": str(item.get("numberOfExperiments", "")),
                })

    refs = entry.get("uniProtKBCrossReferences", [])
    gocc = []
    pdb = []
    interpro = []
    pfam = []
    for ref in refs:
        db = ref.get("database")
        props = {p.get("key"): p.get("value") for p in ref.get("properties", [])}
        if db == "GO" and (props.get("GoTerm") or "").startswith("C:"):
            gocc.append({
                "id": ref.get("id", ""),
                "term": (props.get("GoTerm") or "").replace("C:", ""),
                "evidence": props.get("GoEvidenceType", ""),
            })
        elif db == "PDB":
            pdb.append({
                "id": ref.get("id", ""),
                "method": props.get("Method", ""),
                "resolution": props.get("Resolution", ""),
                "chains": props.get("Chains", ""),
            })
        elif db == "InterPro":
            name = props.get("entryName") or props.get("EntryName") or ""
            interpro.append({"id": ref.get("id", ""), "name": name})
        elif db == "Pfam":
            name = props.get("entryName") or props.get("EntryName") or ""
            pfam.append({"id": ref.get("id", ""), "name": name})

    genes_list = entry.get("genes", [])
    aliases = []
    if genes_list:
        aliases = [s.get("value") for s in genes_list[0].get("synonyms", []) if s.get("value")]

    seq = entry.get("sequence", {})
    return {
        "found": True,
        "accession": acc,
        "protein_name": _protein_name(entry),
        "aliases": aliases,
        "length_aa": seq.get("length"),
        "mass_kda": round((seq.get("molWeight") or 0) / 1000, 1) if seq.get("molWeight") else None,
        "function": funcs[:3],
        "subcellular_locations": locs,
        "go_cc": gocc,
        "pdb": pdb,
        "interpro": interpro,
        "pfam": pfam,
        "uniprot_interactions": interactions,
    }


# ── AlphaFold ─────────────────────────────────────────────────────

def alphafold_query(accession: str | None) -> dict[str, Any]:
    if not accession:
        return {"found": False}
    data = fetch_json(f"https://www.alphafold.ebi.ac.uk/api/prediction/{accession}")
    entries = data if isinstance(data, list) else [data]
    if not entries:
        return {"found": False}
    entry = entries[0]
    plddt_stats = {}
    plddt_url = entry.get("plddtDocUrl")
    if plddt_url:
        try:
            plddt_data = fetch_json(plddt_url, timeout=30)
            scores = [float(x) for x in plddt_data.get("confidenceScore", [])]
            if scores:
                plddt_stats = {
                    "mean_plddt": round(sum(scores) / len(scores), 1),
                    "pct_gt_90": round(sum(s > 90 for s in scores) * 100 / len(scores), 1),
                    "pct_70_90": round(sum(70 <= s <= 90 for s in scores) * 100 / len(scores), 1),
                    "pct_50_70": round(sum(50 <= s < 70 for s in scores) * 100 / len(scores), 1),
                    "pct_lt_50": round(sum(s < 50 for s in scores) * 100 / len(scores), 1),
                }
        except Exception as exc:
            plddt_stats = {"error": f"{type(exc).__name__}: {exc}"}
    return {
        "found": True,
        "entry_id": entry.get("entryId"),
        "pdb_url": entry.get("pdbUrl"),
        "pae_image_url": entry.get("paeImageUrl"),
        "pae_doc_url": entry.get("paeDocUrl"),
        "plddt_url": plddt_url,
        "confidence_avg": entry.get("confidenceAvgLocalScore"),
        "plddt_stats": plddt_stats,
    }


# ── PubMed ────────────────────────────────────────────────────────

def pubmed_query(gene: str) -> dict[str, Any]:
    strict_term = f'"{gene}"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract])'
    broad_term = f'"{gene}"'

    def esearch(term: str, retmax: int = 8) -> dict[str, Any]:
        q = urllib.parse.quote(term)
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={q}&retmax={retmax}&retmode=json&sort=relevance"
        return fetch_json(url, timeout=45)

    strict = esearch(strict_term, retmax=8)
    time.sleep(0.34)
    broad = esearch(broad_term, retmax=0)
    ids = strict.get("esearchresult", {}).get("idlist", [])
    papers = []
    if ids:
        joined = ",".join(ids[:5])
        summary = fetch_json(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={joined}&retmode=json",
            timeout=45,
        )
        result = summary.get("result", {})
        for pid in ids[:5]:
            item = result.get(pid, {})
            papers.append({
                "pmid": pid,
                "title": item.get("title", ""),
                "journal": item.get("fulljournalname", item.get("source", "")),
                "pubdate": item.get("pubdate", ""),
                "authors": [a.get("name") for a in item.get("authors", [])[:3]],
            })
    return {
        "strict_query": strict_term,
        "strict_count": int(strict.get("esearchresult", {}).get("count", 0)),
        "broad_query": broad_term,
        "broad_count": int(broad.get("esearchresult", {}).get("count", 0)),
        "key_papers": papers,
    }


# ── STRING PPI ────────────────────────────────────────────────────

def string_query(gene: str) -> list[dict[str, Any]]:
    url = f"https://string-db.org/api/json/interaction_partners?identifiers={urllib.parse.quote(gene)}&species=9606&limit=20"
    try:
        data = fetch_json(url, timeout=30)
    except Exception:
        return []
    partners = []
    for p in data[:15]:
        partners.append({
            "partner": p.get("preferredName_B") or p.get("stringId_B") or "",
            "score": p.get("score", p.get("combined_score")),
            "experimental": p.get("escore", p.get("experimentally_determined_interaction")),
            "database": p.get("dscore", p.get("database_annotated")),
            "textmining": p.get("tscore", p.get("textmining")),
        })
    return partners


# ── HPA probe ─────────────────────────────────────────────────────

def hpa_probe(gene: str) -> dict[str, Any]:
    """Probe HPA for subcellular IF images via search_download API."""
    api_url = (
        "https://www.proteinatlas.org/api/search_download.php?"
        + urllib.parse.urlencode({
            "search": gene,
            "format": "json",
            "columns": "g,eg,up,relce,scl,scml,scal",
            "compress": "no",
        })
    )
    out: dict[str, Any] = {
        "checked_urls": [api_url],
        "gene": gene,
        "ensembl": None,
        "reliability_if": None,
        "subcellular_location": [],
        "subcellular_main_location": [],
        "subcellular_additional_location": [],
        "hpa_subcellular_url": None,
        "if_image_urls": [],
    }

    def as_list(value: Any) -> list[str]:
        if value is None:
            return []
        if isinstance(value, list):
            return [str(v) for v in value if v]
        if isinstance(value, str):
            return [v for v in re.split(r";\s*|,\s*", value) if v]
        return [str(value)]

    try:
        rows = fetch_json(api_url, timeout=30)
        if isinstance(rows, list):
            exact = [r for r in rows if str(r.get("Gene", "")).upper() == gene.upper()]
            row = (exact or rows[:1] or [None])[0]
            if row:
                ens = row.get("Ensembl")
                out["ensembl"] = ens
                out["uniprot"] = as_list(row.get("Uniprot"))
                out["reliability_if"] = row.get("Reliability (IF)")
                out["subcellular_location"] = as_list(row.get("Subcellular location"))
                out["subcellular_main_location"] = as_list(row.get("Subcellular main location"))
                out["subcellular_additional_location"] = as_list(row.get("Subcellular additional location"))
                if ens:
                    hpa_gene = row.get("Gene") or gene
                    out["hpa_subcellular_url"] = f"https://www.proteinatlas.org/{ens}-{hpa_gene}/subcellular"
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"

    sub_url = out.get("hpa_subcellular_url")
    if sub_url:
        try:
            req = urllib.request.Request(sub_url, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            })
            with urllib.request.urlopen(req, timeout=30, context=CTX) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            seen = set()
            for m in re.finditer(r'https?://images\.proteinatlas\.org/\d+/(?:[^"\s]+\.jpg)', html):
                url = m.group(0)
                if url not in seen and ("red_green" in url or "blue_red_green" in url):
                    seen.add(url)
                    out["if_image_urls"].append(url)
        except Exception as exc:
            out.setdefault("image_errors", []).append(f"subcellular: {type(exc).__name__}: {exc}")

    return out


# ── Main ──────────────────────────────────────────────────────────

def harvest(gene: str) -> dict[str, Any]:
    result: dict[str, Any] = {"gene": gene}

    row = read_excel_row(gene)
    result["excel"] = row
    result["excel_found"] = row is not None
    if row is None:
        result["error"] = f"Gene {gene} not found in any Excel sheet"
        return result

    acc = primary_accession(row)

    # UniProt
    up = uniprot_query(gene, acc)
    result["uniprot"] = up
    if up.get("found") and up.get("accession"):
        acc = acc or up["accession"]

    # AlphaFold
    result["alphafold"] = alphafold_query(acc)

    # PubMed
    time.sleep(0.34)
    result["pubmed"] = pubmed_query(gene)

    # STRING
    result["string_ppi"] = string_query(gene)

    # HPA
    result["hpa"] = hpa_probe(gene)

    # Merge key Excel fields into a flat "meta" for report generation
    result["meta"] = {
        "gene_symbol": gene,
        "full_name": row.get("full_name", ""),
        "aliases": row.get("aliases", ""),
        "uniprot_accession": primary_accession(row) or "",
        "uniprot_entry_name": row.get("uniprot_entry_name", ""),
        "uniprot_length": row.get("uniprot_length", ""),
        "citations": row.get("citations", ""),
        "hotness": row.get("hotness", ""),
        "tier": row.get("tier", ""),
        "evidence_quality": row.get("evidence_quality", ""),
        "hpa_nuclear": row.get("hpa_nuclear", ""),
        "hpa_locations": row.get("hpa_locations", ""),
        "hpa_reliability": row.get("hpa_reliability", ""),
        "uniprot_subcellular": row.get("uniprot_subcellular", ""),
        "uniprot_go_c": row.get("uniprot_go_c", ""),
        "compartments_nuclear_score": row.get("compartments_nuclear_score", ""),
        "compartments_nuclear_evidence": row.get("compartments_nuclear_evidence", ""),
        "Combined_BS_Human_Degree": row.get("Combined_BS_Human_Degree", ""),
        "Has_Any_Human_PPI": row.get("Has_Any_Human_PPI", ""),
        "STRING_Human_Nuclear_Degree": row.get("STRING_Human_Nuclear_Degree", ""),
        "BioGRID_Human_Nuclear_Degree": row.get("BioGRID_Human_Nuclear_Degree", ""),
        "ChIP_Atlas_class": row.get("ChIP_Atlas_class", ""),
        "ChIP_Atlas_antigen": row.get("ChIP_Atlas_antigen", ""),
        "ENCODE_ChIP_WT": row.get("ENCODE_ChIP_WT", ""),
        "sheet": row.get("_sheet", ""),
    }

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Harvest protein facts for one gene")
    parser.add_argument("gene", help="Gene symbol")
    parser.add_argument("--no-cache", action="store_true", help="Skip reading harvest_packets cache")
    args = parser.parse_args()

    result = harvest(args.gene)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, default=str)


if __name__ == "__main__":
    main()
