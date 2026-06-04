#!/usr/bin/env python3
"""Batch query UniProt + PubMed for protein-scout genes."""
import urllib.request, json, ssl, time, sys, os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

GENES = [
    "DNPH1","OGFOD2","OGFOD3","FSAF1","NT5DC1","ABRACL","ANP32D","ACBD6",
    "ACYP1","ACYP2","AP5S1","AP5Z1","ADPRH","AARSD1","ALG1L2","NPEPL1",
    "AMMECR1","AMMECR1L","ANAPC15","ANAPC16","ANKAR","ANKDD1A","ASB10","ASB13","ANKRD16"
]

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested"
os.makedirs(f"{BASE}/audit_work/claude_runs/api_cache", exist_ok=True)

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=timeout, context=ctx).read())

def uniprot_search(gene):
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:9606&format=json&size=1"
    data = fetch(url)
    if not data.get('results'):
        return None
    r = data['results'][0]
    acc = r['primaryAccession']
    name = str(r.get('proteinDescription',{}).get('recommendedName',{}).get('fullName',{}).get('value','?'))[:80]
    seq = r.get('sequence',{}).get('length','?')
    mass = int(r.get('sequence',{}).get('molWeight',0))/1000
    locs = set()
    for c in r.get('comments',[]):
        if c.get('commentType') == 'SUBCELLULAR LOCATION':
            for sl in c.get('subcellularLocations',[]):
                locs.add(sl.get('location',{}).get('locationValue','?'))
    gocc = []
    pdbs = []
    interpro = []
    for ref in r.get('uniProtKBCrossReferences',[]):
        if ref.get('database') == 'GO':
            props = {p['key']:p['value'] for p in ref.get('properties',[])}
            gt = props.get('GoTerm','')
            if gt.startswith('C:'):
                gocc.append(gt.replace('C:',''))
        if ref.get('database') == 'PDB':
            pdbs.append(ref['id'])
        if ref.get('database') == 'InterPro':
            props = {p['key']:p['value'] for p in ref.get('properties',[])}
            interpro.append(f"{ref['id']}({props.get('entryName','?')})")
    return {
        'gene': gene, 'acc': acc, 'name': name, 'seq': seq, 'mass': mass,
        'locs': sorted(locs), 'gocc': gocc, 'pdbs': pdbs, 'interpro': interpro
    }

def pubmed_count(gene, strict=True):
    term = f"{gene}[Title/Abstract]" if strict else gene
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term)}&retmax=0&retmode=json"
    data = fetch(url)
    return int(data['esearchresult']['count'])

def alphafold_check(acc):
    url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{acc}"
    try:
        data = fetch(url, timeout=25)
        entries = data if isinstance(data, list) else [data]
        for e in entries:
            if e.get('uniprotAccession') == acc:
                return {
                    'entry': e.get('entryId'),
                    'version': e.get('latestVersion'),
                    'pdb_url': e.get('pdbUrl'),
                    'pae_url': e.get('paeImageUrl'),
                }
        return None
    except:
        return None

def string_ppi(gene):
    url = f"https://string-db.org/api/json/interaction_partners?identifiers={gene}&species=9606&limit=20"
    try:
        data = fetch(url, timeout=15)
        return [(p['preferredName_B'], p['score']) for p in data[:10]]
    except:
        return []

if __name__ == '__main__':
    import urllib.parse
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    genes = sys.argv[2:] if len(sys.argv) > 2 else GENES

    if mode in ('uniprot', 'all'):
        print("=== UNIPROT ===")
        for gene in genes:
            try:
                info = uniprot_search(gene)
                if info:
                    print(f"{info['gene']}|{info['acc']}|{info['seq']}aa|{info['mass']:.1f}kDa|locs={'/'.join(info['locs'])}|CC={'/'.join(info['gocc'][:6])}|PDB={info['pdbs'][:6]}|IP={info['interpro'][:4]}|{info['name']}")
                else:
                    print(f"{gene}|NOT_FOUND")
            except Exception as e:
                print(f"{gene}|ERROR:{e}")
            time.sleep(0.3)

    if mode in ('pubmed', 'all'):
        print("=== PUBMED ===")
        for gene in genes:
            try:
                strict = pubmed_count(gene, True)
                time.sleep(0.3)
                total = pubmed_count(gene, False)
                print(f"{gene}: strict={strict} total={total}")
            except Exception as e:
                print(f"{gene}: PubMed_ERROR:{e}")
            time.sleep(0.3)
