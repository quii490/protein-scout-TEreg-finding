#!/usr/bin/env python3
"""Deep harvest: PubMed key papers, AlphaFold pLDDT, UniProt domains, HPA interactions."""
import json, os, sys, time, urllib.request, re, xml.etree.ElementTree as ET

def pubmed_papers(gene):
    """Get top 3 centrosome-related PMIDs with titles."""
    query = f"{gene}+AND+(centrosome+OR+centriole+OR+cilia)"
    try:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=3&sort=relevance&term={query}"
        req = urllib.request.Request(url, headers={"User-Agent":"protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            pmids = re.findall(r'<Id>(\d+)</Id>', r.read().decode())
        if not pmids: return []
        # Get titles
        url2 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(pmids)}&retmode=json"
        req2 = urllib.request.Request(url2, headers={"User-Agent":"protein-scout/1.0"})
        with urllib.request.urlopen(req2, timeout=10) as r2:
            data = json.loads(r2.read())
        papers = []
        for pid in pmids:
            info = data.get('result', {}).get(pid, {})
            title = info.get('title', '?')
            date = info.get('pubdate', '?')
            src = info.get('source', '?')
            papers.append(f"PMID {pid}: {title} ({date}) *{src}*")
        return papers
    except Exception as e:
        return [f"*PubMed 查询失败: {e}*"]

def alphafold_plddt(uniprot_id):
    """Get AlphaFold pLDDT summary."""
    if not uniprot_id: return "*无 UniProt ID*"
    try:
        url = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"
        req = urllib.request.Request(url, headers={"User-Agent":"protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        if isinstance(data, list) and data:
            entry = data[0]
            return f"pLDDT 数据可用 (UniProt: {uniprot_id})。PDB 模型: {entry.get('pdbUrl','N/A')[:80]}"
        return "*AlphaFold 无该蛋白预测数据*"
    except:
        return "*AlphaFold 查询失败*"

def uniprot_domains(uniprot_id):
    """Get InterPro/Pfam/SMART domains."""
    if not uniprot_id: return [], []
    try:
        url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
        req = urllib.request.Request(url, headers={"User-Agent":"protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        interpro = []
        pfam = []
        smart = []
        for xref in data.get('uniProtKBCrossReferences', []):
            db = xref.get('database','')
            props = {p['key']: p['value'] for p in xref.get('properties', [])}
            name = props.get('EntryName', props.get('ProteinName', '?'))
            if db == 'InterPro': interpro.append(name)
            elif db == 'Pfam': pfam.append(name)
            elif db == 'SMART': smart.append(name)
        return interpro, pfam
    except Exception as e:
        return [], []

def hpa_interactions(ensg, gene):
    """Get HPA interaction data."""
    try:
        url = f"https://www.proteinatlas.org/{ensg}-{gene}/interaction"
        req = urllib.request.Request(url, headers={"User-Agent":"protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode()
        # Extract interaction table
        partners = []
        rows = re.findall(r'<tr[^>]*>.*?</tr>', html, re.DOTALL)
        for row in rows:
            tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
            if len(tds) >= 3:
                gene_name = re.sub(r'<[^>]+>', '', tds[0]).strip()
                datasets = re.sub(r'<[^>]+>', '', ' '.join(tds[1:])).strip()
                if gene_name and gene_name != gene:
                    partners.append(f"{gene_name} ({datasets[:60]})")
        return partners[:10]
    except:
        return []

if __name__ == "__main__":
    # Standalone test
    print("PubMed:", pubmed_papers("CEP152"))
    print("AlphaFold:", alphafold_plddt("Q8TEP8"))
    print("InterPro:", uniprot_domains("Q8TEP8")[0][:5])
