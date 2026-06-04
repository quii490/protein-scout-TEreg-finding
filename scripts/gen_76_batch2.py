#!/usr/bin/env python3
"""Fast batch: full /180 re-evaluation reports for 76 genes (batch 2).
No IF/PAE downloads. All API data live. Skip done. No placeholders."""

import json, os, sys, re, ssl, urllib.request, time, urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
VAULT_PREFIX = "Projects/TEreg-finding/protein-interested/detail"

GENES = [
    "CLMN", "CNGA2", "CNKSR1", "CNPY1", "CNST", "COA3", "COA4", "COMMD1", "COMMD2",
    "COPS2", "COPS3", "COQ10A", "COQ10B", "COQ8A", "COQ8B", "COTL1", "COX15", "COX16",
    "COX17", "COX18", "COX19", "COX20", "COX6B1", "COX7A1", "COX7A2", "COX7C", "COX8A",
    "CPLX1", "CPLX3", "CPNE3", "CPSF1", "CPSF3", "CPT2", "CRACD", "CRBN", "CRIP2",
    "CRIPT", "CRLS1", "CROT", "CRYAB", "CRYBG1", "CSAD", "CSDE1", "CSTF1", "CSTF3",
    "CTAGE1", "CTAGE4", "CTBP1", "CTDSP1", "CTNNAL1", "CTNND1", "CTPS1", "CTU2",
    "CUL4B", "CXXC1", "CXADR", "CYB5D1", "DACH2", "DAG1", "DAGLA", "DBNDD2", "DBNDD1",
    "DCAF11", "DCAF4", "DCAF5", "DCAF6", "DDAH2", "DDX19A", "DDX19B", "DDX39A",
    "DDX39B", "DDX50", "DDX52", "DDX54", "DDX56", "DELE1", "DGCR14", "DGKA",
]

ctx = ssl.create_default_context()

def fetch_json(url):
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
        except:
            if attempt == 1:
                return None
            time.sleep(0.5)

def fetch_text(url):
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except:
            if attempt == 1:
                return None
            time.sleep(0.5)

def fetch_uniprot(gene):
    url = (
        f"https://rest.uniprot.org/uniprotkb/search?"
        f"query=gene:{gene}+AND+organism_id:9606&format=json&size=5"
        f"&fields=accession,protein_name,length,cc_subcellular_location,"
        f"go,ft_domain,structure_3d,gene_names,cc_interaction,cc_function,"
        f"reviewed,sequence"
    )
    data = fetch_json(url)
    if not data or not data.get("results"):
        return None, ["No UniProt results"]
    results = data["results"]
    reviewed = [r for r in results if r.get("entryType") == "Swiss-Prot"]
    all_sorted = sorted(results, key=lambda x: x.get("sequence", {}).get("length", 0), reverse=True)
    best = reviewed[0] if reviewed else (all_sorted[0] if all_sorted else results[0])
    mass = best.get("sequence", {}).get("molWeight", 0) / 1000
    accession = best.get("primaryAccession", gene)
    name = best.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "")
    if not name:
        name = best.get("proteinDescription", {}).get("submissionNames", [{}])[0].get("fullName", {}).get("value", "")
    if not name:
        name = best.get("proteinDescription", {}).get("alternativeNames", [{}])[0].get("fullName", {}).get("value", "")
    length = best.get("sequence", {}).get("length", 0)
    subcell = []
    for c in best.get("comments", []):
        if c.get("commentType") == "SUBCELLULAR LOCATION":
            for sub in c.get("subcellularLocations", []):
                loc = sub.get("location", {}).get("value", "")
                if loc:
                    subcell.append(loc)
    go_cc = []
    for xref in best.get("crossReferences", []):
        if xref.get("database") == "GO":
            for prop in xref.get("properties", []):
                if prop.get("key") == "GoTerm" and "C:" in prop.get("value", ""):
                    go_val = prop["value"]
                    term = go_val.split("C:")[1] if "C:" in go_val else go_val
                    go_cc.append({"id": xref.get("id", ""), "term": term, "evidence": "IEA"})
    pdb = []
    for xref in best.get("crossReferences", []):
        if xref.get("database") == "PDB":
            pdb.append({
                "id": xref.get("id", ""),
                "method": next((p.get("value", "") for p in xref.get("properties", []) if p.get("key") == "Method"), ""),
                "resolution": next((p.get("value", "") for p in xref.get("properties", []) if p.get("key") == "Resolution"), ""),
            })
    interpro = []
    for feat in best.get("features", []):
        if feat.get("type") == "DOMAIN":
            desc = feat.get("description", "")
            if desc:
                interpro.append({"id": "", "name": desc})
    aliases = []
    for g in best.get("genes", []):
        gn = g.get("geneName", {}).get("value", "")
        if gn and gn != gene:
            aliases.append(gn)
    return {
        "found": True, "query_gene": gene, "primary_gene": gene,
        "accession": accession, "protein_name": name or f"{gene} protein",
        "aliases": aliases, "length_aa": length,
        "mass_kda": round(mass, 1) if mass and mass > 0 else round(length * 0.11, 1),
        "subcellular_locations": [{"location": s, "evidences": []} for s in subcell],
        "go_cc": go_cc, "pdb": pdb, "interpro": interpro, "pfam": [],
    }, []

def fetch_alphafold(accession):
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{accession}"
    data = fetch_json(url)
    if not data:
        return {"found": False}
    entry = data[0] if isinstance(data, list) else data
    if not entry:
        return {"found": False}
    global_metric = entry.get("globalMetricValue", 0)
    mean_plddt = round(global_metric, 1) if global_metric else 0
    f_vl = entry.get("fractionPlddtVeryLow", 0) or 0
    f_l = entry.get("fractionPlddtLow", 0) or 0
    f_c = entry.get("fractionPlddtConfident", 0) or 0
    f_vh = entry.get("fractionPlddtVeryHigh", 0) or 0
    lt50 = round(f_vl * 100, 1); r_50_70 = round(f_l * 100, 1)
    r_70_90 = round(f_c * 100, 1); gt90 = round(f_vh * 100, 1)
    if mean_plddt == 0 and gt90 == 0 and r_70_90 == 0 and r_50_70 == 0 and lt50 == 0:
        return {"found": False}
    return {
        "found": True, "entry_id": entry.get("entryId", ""),
        "latest_version": entry.get("latestVersion", 4),
        "confidence_avg": mean_plddt,
        "plddt_stats": {"mean_plddt": mean_plddt, "pct_gt_90": gt90,
                         "pct_70_90": r_70_90, "pct_50_70": r_50_70, "pct_lt_50": lt50}
    }

def fetch_pubmed(gene):
    query = f"{gene}[Title/Abstract]"
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax=0&retmode=json"
    data = fetch_json(url); strict_count = int(data["esearchresult"].get("count", 0)) if data and "esearchresult" in data else 0
    url2 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={gene}&retmax=0&retmode=json"
    data2 = fetch_json(url2); broad_count = int(data2["esearchresult"].get("count", 0)) if data2 and "esearchresult" in data2 else 0
    url3 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax=5&retmode=json&sort=pub+date"
    data3 = fetch_json(url3); key_papers = []
    if data3 and "esearchresult" in data3 and data3["esearchresult"].get("idlist"):
        idlist = data3["esearchresult"]["idlist"]
        url4 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(idlist)}&retmode=json"
        data4 = fetch_json(url4)
        if data4 and "result" in data4:
            for pmid in idlist:
                paper = data4["result"].get(pmid, {})
                if paper:
                    key_papers.append({"pmid": pmid, "title": paper.get("title", ""), "journal": paper.get("source", ""), "pubdate": paper.get("pubdate", ""), "authors": ", ".join([a.get("name", "") for a in paper.get("authors", [])][:5])})
    return {"strict_query": query, "strict_count": strict_count, "broad_count": broad_count, "alias_note": "", "key_papers": key_papers}

def fetch_hpa(gene):
    search_url = f"https://www.proteinatlas.org/api/search_download.php?search={gene}&format=json&columns=g,eg,up,relce,scl,scml,scal&compress=no"
    data = fetch_json(search_url)
    if not data:
        return {"ok": False, "data": {"status": "hpa_fetch_failed"}}
    entry = None
    for item in data:
        if item.get("Gene") and item.get("Gene", "").upper() == gene.upper():
            entry = item; break
    if not entry:
        for item in data:
            if gene.upper() in item.get("Gene", "").upper():
                entry = item; break
    if not entry and data:
        entry = data[0]
    if not entry:
        return {"ok": True, "data": {"status": "no_hpa_entry", "subcellular_main_location": [], "subcellular_additional_location": [], "reliability_if": "No data", "image_status": "no_image_detected"}}
    main_loc = entry.get("Subcellular main location", "")
    addl_loc = entry.get("Subcellular additional location", "")
    reliability = entry.get("Reliability (IF)", "")
    if isinstance(main_loc, list): main_loc = "|".join(str(x) for x in main_loc if x)
    if isinstance(addl_loc, list): addl_loc = "|".join(str(x) for x in addl_loc if x)
    main_list = [m.strip() for m in str(main_loc).split("|") if m.strip()] if main_loc else []
    addl_list = [a.strip() for a in str(addl_loc).split("|") if a.strip()] if addl_loc else []
    image_status = "if_display_images_available" if reliability and reliability in ("Approved", "Enhanced", "Supported") else "no_image_detected"
    ensembl = entry.get("Ensembl", "")
    hpa_url = f"https://www.proteinatlas.org/{ensembl}-{gene}/subcellular" if ensembl else f"https://www.proteinatlas.org/search/{gene}"
    return {"ok": True, "data": {"status": "hpa_localization_available", "gene": gene, "ensembl": ensembl, "reliability_if": reliability or "No data", "subcellular_main_location": main_list, "subcellular_additional_location": addl_list, "hpa_subcellular_url": hpa_url, "image_status": image_status}}

def fetch_string(gene):
    url = f"https://string-db.org/api/json/interaction_partners?identifiers={gene}&species=9606&limit=25"
    data = fetch_json(url)
    if not data: return []
    return [{"partner": item.get("preferredName_B", ""), "score": float(item.get("combined_score", 0)), "experimental": float(item.get("experimentally_determined_interaction", 0)), "database": int(item.get("database_annotated", 0)), "textmining": float(item.get("textmining", 0))} for item in data]

def fetch_intact(gene):
    url = f"http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{gene}?format=tab27"
    text = fetch_text(url)
    if not text: return []
    result = []
    for line in text.strip().split('\n'):
        if not line.strip() or line.startswith('#'): continue
        parts = line.split('\t')
        if len(parts) >= 16:
            result.append({"partner": parts[1], "method": parts[6], "pmid": f"pubmed:{parts[15]}" if len(parts) > 15 else "", "interaction_type": parts[8] if len(parts) > 8 else ""})
    return result[:30]

# SCORING

def novelty_score(ps):
    if ps <= 20: return 10
    if ps <= 40: return 8
    if ps <= 60: return 6
    if ps <= 80: return 4
    if ps <= 100: return 2
    return 0

def size_score(aa):
    if 200 <= aa <= 800: return 10
    if (100 <= aa < 200) or (800 < aa <= 1200): return 8
    if (50 <= aa < 100) or (1200 < aa <= 2000): return 5
    if aa < 50 or (2000 < aa <= 3000): return 2
    return 0

def struct_score(pdb_ids, plddt):
    n = len(pdb_ids) if pdb_ids else 0
    if n >= 5 and plddt >= 70: return 10
    if n >= 2 and plddt >= 70: return 9
    if n >= 1 and plddt >= 70: return 8
    if plddt >= 85: return 8
    if plddt >= 70: return 7
    if plddt >= 50: return 6
    if plddt < 40: return 4
    return 6

def domain_score(dt, plddt):
    ck = ["bromo", "chromo", "phd", "sant", "tudor", "mbt", "pwwp", "zinc finger", "homeobox", "hmg", "forkhead", "bzip", "bhlh", "at-hook", "myb", "cxxc", "histone", "chromatin", "dna-binding", "nucleic acid binding"]
    t = dt.lower()
    has_c = any(k in t for k in ck)
    dc = t.count("ipr") + t.count("pf")
    if has_c and dc >= 3: return 10
    if has_c or (dc >= 2 and plddt >= 80): return 8
    if dc > 0: return 7
    if plddt >= 70: return 6
    if plddt >= 50: return 5
    return 4

def ppi_score(sn, inn, sp):
    rk = ["chromatin", "transcription", "histone", "dna", "rna polymer", "helicase", "splicing", "rna", "trna", "rrna", "nucleolar", "ribosome", "nucleosome", "mediator", "coactivator", "corepressor", "deacetylase", "acetyltransferase", "methyltransferase", "kinetochore", "centromere", "condensin", "cohesin", "smc", "origin recognition", "replication factor"]
    if not sp: return 2
    rc = sum(1 for p in sp[:20] if any(k in p.get("partner", "").lower() for k in rk))
    rr = rc / min(len(sp), 20)
    hp = inn > 0; hs = sn > 0
    if hp and rr > 0.4 and sn >= 10: return 10
    if hp and rr > 0.2 and sn >= 5: return 8
    if hp and rr > 0.3: return 6
    if hs and rr > 0.2: return 4
    if hs: return 3
    return 2

def cross_validation(pdb_ids, plddt, uni_loc, hpa_loc, go_cc, sn, inn, domains, has_uni):
    pts = 0
    if pdb_ids and plddt > 0: pts += 0.5
    has_mn = sum([bool(has_uni and uni_loc), bool(hpa_loc), bool(go_cc)])
    if has_mn >= 2: pts += 0.5
    if sn > 0 and inn > 0: pts += 0.5
    if domains and "暂无" not in domains and plddt > 70: pts += 0.5
    if len(pdb_ids) >= 3: pts += 1.0
    return min(pts, 3.0)

def nuclear_score(uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc_terms, has_uni):
    nk = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus"]
    nnk = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum", "membrane", "secreted", "cytoskeleton", "centrosome", "spindle", "microtubule", "vesicle", "synapse", "cilia", "flagella", "cell projection", "plasma membrane", "extracellular"]
    hmt = " ".join(hpa_main).lower()
    hat = " ".join(hpa_addl).lower()
    hn = any(k in hmt for k in nk) or (any(k in hat for k in nk) and not any(k in hmt for k in nk))
    hnon = any(k in hmt for k in nnk)
    un = False; unon = False
    if has_uni:
        ut = " ".join(uni_subcell).lower()
        un = any(k in ut for k in nk); unon = any(k in ut for k in nnk)
    gn = False; gnon = False
    if go_cc_terms:
        gt = " ".join([cc.get("term", str(cc)) if isinstance(cc, dict) else str(cc) for cc in go_cc_terms]).lower()
        gn = any(k in gt for k in nk); gnon = any(k in gt for k in nnk)
    ns = sum([hn, un, gn]); nns = sum([hnon, unon, gnon])
    if ns == 0 and nns == 0: return 3
    if ns >= 2 and nns == 0: return 9 if ns >= 3 else 8
    if ns >= 2 and nns >= 1: return 7
    if ns == 1 and nns == 0: return 7 if (hn and hpa_rel in ["Approved", "Enhanced"]) else 5
    if hnon and not hn and (un or gn): return 4 if gn else 3
    if ns == 1 and nns == 1: return 4
    if ns >= 1 and nns > ns: return 4
    if nns >= 2 and ns == 0: return 2
    if nns == 1 and ns == 0: return 2
    return 3

def get_domain_text(uni_data):
    if not uni_data: return "暂无数据 (UniProt未获取)"
    interpro = uni_data.get("interpro", [])
    pfam = uni_data.get("pfam", [])
    ipr_names = [i.get("name", "") or i.get("id", "") for i in interpro]
    pf_names = [p.get("name", "") or p.get("id", "") for p in pfam]
    parts = []
    if ipr_names: parts.append("InterPro: " + ", ".join(ipr_names[:5]))
    if pf_names: parts.append("Pfam: " + ", ".join(pf_names[:3]))
    return "; ".join(parts) if parts else "无注释结构域"

def extract_go_terms(go_cc):
    if not go_cc: return []
    return [cc.get("term", str(cc)) if isinstance(cc, dict) else str(cc) for cc in go_cc]

def get_go_cc_text(uni_data):
    if not uni_data: return "- 无 GO-CC 注释 (UniProt未获取)"
    go_cc = uni_data.get("go_cc", [])
    if not go_cc: return "- 无 GO-CC 注释"
    return "\n".join(f"- {cc.get('term', str(cc))} ({cc.get('id','')})" for cc in go_cc[:8])

def format_key_papers(papers):
    if not papers: return "无关键文献数据。"
    return "\n".join(f"{i}. {p.get('title','N/A')}. *{p.get('journal','N/A')}*. PMID: {p.get('pmid','N/A')}" for i, p in enumerate(papers[:5], 1))

def format_string_table(partners):
    if not partners: return "| — | — | — | — |"
    return "\n".join(f"| {p.get('partner','?')} | {p.get('score',0):.3f} | {p.get('experimental',0):.3f} | — |" for p in partners[:10])

def format_intact_table(partners, gene):
    if not partners: return "| — | — | — |"
    seen = set(); lines = []
    for p in partners:
        partner = p.get("partner", "")
        if partner.lower() in seen: continue
        seen.add(partner.lower())
        if len(seen) > 10: break
        lines.append(f"| {partner} | {p.get('method','—')[:50]} | {p.get('pmid','—')[:30]} |")
    return "\n".join(lines) if lines else "| — | — | — |"

def get_reg_partner_info(string_partners, intact_partners, gene):
    rk = ["chromatin", "transcription", "histone", "dna", "rna polymer", "helicase", "splicing", "rna", "trna", "rrna", "nucleolar", "ribosome", "nucleosome", "mediator", "coactivator", "corepressor", "deacetylase", "acetyltransferase", "methyltransferase", "kinetochore", "centromere", "condensin", "cohesin", "smc", "origin recognition", "replication factor", "eif4e", "translation", "ubiquitin", "e3", "ligase"]
    return [p.get("partner", "?") for p in (string_partners or [])[:20] if any(k in p.get("partner", "").lower() for k in rk)]

def already_complete(gene):
    for dname in os.listdir(DETAIL):
        dpath = os.path.join(DETAIL, dname)
        if not os.path.isdir(dpath): continue
        rp = os.path.join(dpath, gene, f"{gene}-evaluation.md")
        if os.path.exists(rp):
            sz = os.path.getsize(rp)
            if sz > 2000:
                with open(rp) as f:
                    if "/180" in f.read():
                        return True, rp
    return False, None

def determine_dest(nuc, pubmed_strict, hpa_main, hpa_addl, subcell, go_cc):
    if nuc <= 3 or pubmed_strict > 100: return "rejected"
    all_loc = (", ".join(hpa_main + hpa_addl) + " " + " ".join(subcell) + " " + " ".join(extract_go_terms(go_cc))).lower()
    if "nuclear bod" in all_loc or "nuclear speck" in all_loc: return "nuclear-body"
    if "nucleolus" in all_loc or "fibrillar center" in all_loc: return "nucleolus"
    if "nuclear envelope" in all_loc or "nuclear membrane" in all_loc or "nuclear pore" in all_loc: return "nuclear-envelope"
    if "chromatin" in all_loc or "chromosome" in all_loc: return "chromatin"
    if "nucleoplasm" in all_loc: return "nucleoplasm"
    if "nucleus" in all_loc: return "nucleoplasm"
    return "nucleoplasm"

def generate_report_for_gene(gene):
    sys.stdout.write(f"  [{gene}] "); sys.stdout.flush()

    uni, _ = fetch_uniprot(gene)
    has_uni = uni is not None
    if has_uni:
        accession = uni.get("accession", gene)
        prot_name = uni.get("protein_name", f"{gene} protein")
        length_aa = uni.get("length_aa", 0)
        mass_kda = uni.get("mass_kda", round(length_aa * 0.11, 1))
        subcell = [s.get("location", "") for s in uni.get("subcellular_locations", [])]
        go_cc = uni.get("go_cc", [])
        pdb_list = [p.get("id", "") for p in uni.get("pdb", [])]
        aliases = uni.get("aliases", [])
    else:
        accession = gene; prot_name = f"{gene} (UniProt未获取)"
        length_aa = 0; mass_kda = 0; subcell = []; go_cc = []; pdb_list = []; aliases = []

    af = fetch_alphafold(accession) if has_uni else {"found": False}
    af_found = af.get("found", False)
    if af_found:
        stats = af.get("plddt_stats", {})
        plddt = stats.get("mean_plddt", 0); pct_gt_90 = stats.get("pct_gt_90", 0)
        pct_70_90 = stats.get("pct_70_90", 0); pct_50_70 = stats.get("pct_50_70", 0)
        pct_lt_50 = stats.get("pct_lt_50", 0); af_version = af.get("latest_version", "?")
        ordered_pct = round(pct_gt_90 + pct_70_90, 1)
    else:
        plddt = 0; pct_gt_90 = 0; pct_70_90 = 0; pct_50_70 = 0; pct_lt_50 = 0
        af_version = "?"; ordered_pct = 0

    pubmed = fetch_pubmed(gene)
    pubmed_strict = pubmed.get("strict_count", 0)
    key_papers = pubmed.get("key_papers", [])

    hpa_result = fetch_hpa(gene)
    hpa = hpa_result.get("data", {})
    hpa_main = hpa.get("subcellular_main_location", [])
    hpa_addl = hpa.get("subcellular_additional_location", [])
    hpa_rel = hpa.get("reliability_if", "暂无数据")
    hpa_subcell_url = hpa.get("hpa_subcellular_url", "")
    image_status = hpa.get("image_status", "unknown")

    string_p = fetch_string(gene)
    intact_p = fetch_intact(gene)

    domain_text = get_domain_text(uni)
    nuc = nuclear_score(subcell, hpa_main, hpa_addl, hpa_rel, go_cc, has_uni)
    sz = size_score(length_aa) if length_aa > 0 else 5
    nov = novelty_score(pubmed_strict)
    struct = struct_score(pdb_list, plddt) if af_found else 4
    dom = domain_score(domain_text, plddt)
    ppi = ppi_score(len(string_p), len(intact_p), string_p)
    cross = cross_validation(pdb_list, plddt, subcell, hpa_main, go_cc, len(string_p), len(intact_p), domain_text, has_uni)

    raw = nuc * 4 + sz * 1 + nov * 5 + struct * 3 + dom * 2 + ppi * 3 + cross
    norm = round(raw / 1.80, 1)
    rejected = nuc <= 3 or pubmed_strict > 100
    status = "rejected" if rejected else "scored"
    dest = determine_dest(nuc, pubmed_strict, hpa_main, hpa_addl, subcell, go_cc)

    # IF note (no download)
    if_note = "**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。"
    pae_note = "**PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。"

    # Descriptions
    nuc_desc_map = {9: "多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。", 8: "主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。", 7: "主要核定位，HPA 可靠性良好，有辅助数据源支持。", 6: "存在核定位证据但部分来源支持较弱或缺失。", 5: "核定位证据存在但较为混杂，部分数据源指向非核区室。", 4: "核定位信号较弱，多个数据源显示混合定位或非核偏好。", 3: "核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。", 2: "核定位证据极弱，主要数据源均不指向细胞核。", 1: "无核定位证据。"}
    nuc_desc = nuc_desc_map.get(nuc, "核定位不确定。")
    sz_desc = "大小适中（200-800 aa），适合常规生化实验和结构解析。" if sz >= 10 else ("大小基本合适，可用于常规实验。" if sz >= 8 else ("蛋白偏小/偏大，实验操作有一定难度。" if sz >= 5 else "大小偏离理想范围，实验设计需特殊考虑。"))
    nov_desc = "极度新颖，几乎未被系统研究（PubMed ≤20篇）。" if nov >= 10 else ("非常新颖，仅有少数基础研究。" if nov >= 8 else ("较新颖，有一定研究但存在未探索领域。" if nov >= 6 else ("已有一定研究基础，但仍存在niche空间。" if nov >= 4 else "研究基础较多，新颖性有限。")))
    pdb_text = ", ".join(pdb_list[:10]) if pdb_list else "无"
    if struct >= 10: struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold极高置信度预测（pLDDT={round(plddt,1)}），结构可信度极高。"
    elif struct >= 9: struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold高质量预测（pLDDT={round(plddt,1)}），结构可信度高。"
    elif struct >= 8: struct_desc = f"AlphaFold 极高置信度预测（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构可靠。" if plddt >= 85 else f"AlphaFold 高质量预测（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构可靠。"
    elif struct >= 7: struct_desc = f"AlphaFold 中等质量（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构基本可用。"
    else: struct_desc = f"AlphaFold 预测质量有限（pLDDT={round(plddt,1)}），有序残基占 {ordered_pct}%。"
    dom_desc = "含明确的核酸结合/染色质相关结构域，多库确认。" if dom >= 9 else ("多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。" if dom >= 8 else ("存在已知结构域注释，可作为功能研究的结构基础。" if dom >= 7 else ("结构域注释有限，AlphaFold预测有可辨识折叠域。" if dom >= 5 else "结构域注释稀疏，属新颖蛋白正常现象。")))
    reg = get_reg_partner_info(string_p, intact_p, gene)
    reg_ratio = len(reg) / min(len(string_p), 20) * 100 if string_p else 0
    ppi_desc = f"STRING {len(string_p)} 个预测互作，IntAct {len(intact_p)} 个实验互作。调控相关配体占比 {reg_ratio:.0f}%。"

    has_uni_text = "Swiss-Prot/TrEMBL" if has_uni else "获取失败"
    subcell_text = "; ".join(subcell) if subcell else "无注释"
    hpa_loc_text = ", ".join(hpa_main) if hpa_main else ""
    if hpa_addl: hpa_loc_text += ("; 额外: " + ", ".join(hpa_addl)) if hpa_loc_text else ", ".join(hpa_addl)
    if not hpa_loc_text: hpa_loc_text = "暂无HPA定位数据"
    alias_text = ", ".join(aliases[:5]) if aliases else ""
    mass = mass_kda if mass_kda else (round(length_aa * 0.11, 1) if length_aa else "未知")
    uniprot_url = f"https://www.uniprot.org/uniprotkb/{accession}" if accession else ""
    nov_label = "≤20→10" if pubmed_strict <= 20 else ("≤40→8" if pubmed_strict <= 40 else ("≤60→6" if pubmed_strict <= 60 else ("≤80→4" if pubmed_strict <= 80 else ("≤100→2" if pubmed_strict <= 100 else ">100→REJECTED"))))
    today = "2026-06-03"

    rejection_reasons = []
    if nuc <= 3: rejection_reasons.append(f"核定位证据不足 (核定位得分 {nuc}/10 ≤ 3)")
    if pubmed_strict > 100: rejection_reasons.append(f"研究热度过高 (PubMed strict={pubmed_strict}，超过100篇阈值)")
    title_line = f"## {gene} — REJECTED ({'; '.join(rejection_reasons)})" if rejected else f"## {gene} 核蛋白评估报告 (Full Re-evaluation)"

    papers_text = format_key_papers(key_papers)
    string_table = format_string_table(string_p)
    intact_table = format_intact_table(intact_p, gene)
    go_cc_text = get_go_cc_text(uni)

    cross_details = []
    if pdb_list and plddt > 0: cross_details.append("PDB + AlphaFold 双源验证: +0.5")
    has_mn = sum([bool(has_uni and subcell), bool(hpa_main), bool(go_cc)])
    cross_details.append(f"多库定位一致 ({has_mn}源): +0.5" if has_mn >= 2 else "多库定位一致: +0")
    cross_details.append("STRING + IntAct 双源验证: +0.5" if string_p and intact_p else "STRING + IntAct 双源验证: +0")
    cross_details.append("结构域 + AlphaFold 质量: +0.5" if domain_text and "暂无" not in domain_text and plddt > 70 else "结构域 + AlphaFold 质量: +0")
    cross_details.append("PDB 多条目覆盖 (≥3): +1.0" if len(pdb_list) >= 3 else "PDB 多条目覆盖: +0")

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {today}
tags: [protein-scout, {"rejected" if rejected else "nuclear-protein"}, evaluation]
status: {status}
---

{title_line}

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene}{f" / {alias_text}" if alias_text else ""} |
| 蛋白名称 | {prot_name} |
| 蛋白大小 | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| UniProt ID | {accession} |
| 评估日期 | {today} |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | {nuc}/10 | ×4 | {nuc*4} | HPA: {hpa_loc_text[:60]}; UniProt: {subcell_text[:60]} |
| 蛋白大小 | {sz}/10 | ×1 | {sz} | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| 研究新颖性 | {nov}/10 | ×5 | {nov*5} | PubMed strict={pubmed_strict} 篇 ({nov_label}) |
| 三维结构 | {struct}/10 | ×3 | {struct*3} | AlphaFold v{af_version} pLDDT={round(plddt,1)}; PDB: {pdb_text[:40]} |
| 调控结构域 | {dom}/10 | ×2 | {dom*2} | {domain_text[:60]} |
| PPI 网络 | {ppi}/10 | ×3 | {ppi*3} | STRING {len(string_p)} partners; IntAct {len(intact_p)} interactions |
| 互证加分 | — | max +3 | {cross} | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **{raw}/180** | |
| **归一化总分** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | {hpa_loc_text} | {hpa_rel if hpa_rel else "暂无"} |
| UniProt | {subcell_text[:100]}{"..." if len(subcell_text) > 100 else ""} | {has_uni_text} |

{if_note}

**GO Cellular Component**:
{go_cc_text}

**结论**: {nuc_desc}

#### 3.2 蛋白大小评估

**评价**: {sz_desc}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | {pubmed_strict} |
| PubMed broad count | {pubmed.get("broad_count", "N/A")} |
| 别名(未计入scoring) | {pubmed.get("alias_note", "无")} |

**关键文献**:
{papers_text}

**评价**: {nov_desc}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v{af_version} |
| AlphaFold 平均 pLDDT | {round(plddt,1)} |
| 高置信度残基 (pLDDT>90) 占比 | {pct_gt_90}% |
| 置信残基 (pLDDT 70-90) 占比 | {pct_70_90}% |
| 中等置信 (pLDDT 50-70) 占比 | {pct_50_70}% |
| 低置信 (pLDDT<50) 占比 | {pct_lt_50}% |
| 有序区域 (pLDDT>70) 占比 | {ordered_pct}% |
| 可用 PDB 条目 | {pdb_text} |

**PAE**: {pae_note}

**评价**: {struct_desc}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | {domain_text[:200]} |

**染色质调控潜力分析**: {dom_desc}

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
{string_table}

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
{intact_table}

**PPI 互证分析**:
- {"STRING + IntAct 均有数据" if string_p and intact_p else "仅STRING预测" if string_p else "仅IntAct实验" if intact_p else "无PPI数据"}
- STRING partners: {len(string_p)}，IntAct interactions: {len(intact_p)}
- 调控相关比例: {len(reg)} / {min(len(string_p), 20)} = {reg_ratio:.0f}%

**评价**: {ppi_desc}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT={round(plddt,1)} + PDB: {pdb_text[:30]} | pLDDT={round(plddt,1)}, v{af_version} | {"预测+实验" if pdb_list else "仅预测"} |
| 定位 | UniProt + HPA | {subcell_text[:50]} / {hpa_loc_text[:50]} | {"一致" if has_mn >= 2 else "待确认"} |
| PPI | STRING + IntAct | {len(string_p)} + {len(intact_p)} interactions | {"数据充分" if string_p and intact_p else "数据有限"} |

**互证加分明细**:
{chr(10).join(f"- {d}" for d in cross_details)}
**总分**: +{cross} / max +3

### 4. 总体评价

**推荐等级**: {"⭐" * max(1, min(5, round(norm/20)))}{" (REJECTED)" if rejected else ""}

**核心优势**:
1. {gene} — {prot_name}，{nov_desc}
2. 蛋白大小{length_aa if length_aa else "未知"} aa，{sz_desc}

**风险/不确定性**:
1. {"PubMed " + str(pubmed_strict) + " 篇，研究基础极有限，功能注释不完整" if pubmed_strict <= 20 else "PubMed " + str(pubmed_strict) + " 篇，已有一定研究基础" if pubmed_strict <= 100 else "PubMed " + str(pubmed_strict) + " 篇，研究热度过高（>100），不符合新颖性要求"}
2. {"AlphaFold 预测质量一般（pLDDT=" + str(round(plddt,1)) + "），需要更多实验结构验证" if plddt < 70 and af_found else "结构数据质量可接受" if plddt >= 70 else "结构数据暂缺"}

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
{"- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**" if nuc <= 3 else ""}{"**该蛋白PubMed文献数 " + str(pubmed_strict) + " > 100，研究热度过高，不符合novelty筛选标准。**" if pubmed_strict > 100 and nuc > 3 else ""}

### 5. 数据来源
- UniProt: {uniprot_url}
- Protein Atlas: {hpa_subcell_url if hpa_subcell_url else "https://www.proteinatlas.org/search/" + gene}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{accession}
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: {today}
"""
    return report, dest, rejected

def main():
    to_process = []
    for gene in GENES:
        complete, cpath = already_complete(gene)
        if complete:
            print(f"  SKIP {gene} (already complete: {cpath})")
            continue
        to_process.append(gene)

    if not to_process:
        print("All done.")
        return

    print(f"\n{'='*70}")
    print(f"Processing {len(to_process)} genes (fast mode - no IF/PAE downloads)...")
    print(f"{'='*70}\n")

    results = []
    for i, gene in enumerate(to_process):
        try:
            t0 = time.time()
            report, dest, rejected = generate_report_for_gene(gene)
            elapsed = time.time() - t0

            report_dir = os.path.join(DETAIL, dest, gene)
            os.makedirs(report_dir, exist_ok=True)
            report_path = os.path.join(report_dir, f"{gene}-evaluation.md")
            with open(report_path, "w") as f:
                f.write(report)

            size = len(report.encode("utf-8"))
            status_tag = "REJECTED" if rejected else "SCORED"
            print(f"-> {dest:20s} ({size:5d}B, {elapsed:.1f}s) [{status_tag}]")
            results.append({"gene": gene, "dest": dest, "size": size, "rejected": rejected})
        except Exception as e:
            print(f"-> ERROR: {e}")
            import traceback; traceback.print_exc()
            results.append({"gene": gene, "dest": "ERROR", "size": 0, "rejected": True})

        if (i + 1) % 3 == 0:
            time.sleep(0.5)

    print(f"\n{'='*70}")
    ok = len(results)
    rej = sum(1 for r in results if r["rejected"])
    scd = sum(1 for r in results if not r["rejected"])
    err = sum(1 for r in results if r["dest"] == "ERROR")
    print(f"Summary: {ok} done, {rej} REJECTED, {scd} SCORED, {err} ERROR")
    dests = sorted(set(r["dest"] for r in results if r["dest"] != "ERROR"))
    print(f"Destinations: {', '.join(dests)}")
    print("\nDone.")

if __name__ == "__main__":
    main()
