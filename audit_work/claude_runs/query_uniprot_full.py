#!/usr/bin/env python3
"""Get proper UniProt entries (canonical) with subcellular location."""
import urllib.request, json, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

GENES = [
    "DNPH1","OGFOD2","OGFOD3","FSAF1","NT5DC1","ABRACL","ANP32D","ACBD6",
    "ACYP1","ACYP2","AP5S1","AP5Z1","ADPRH","AARSD1","ALG1L2","NPEPL1",
    "AMMECR1","AMMECR1L","ANAPC15","ANAPC16","ANKAR","ANKDD1A","ASB10","ASB13","ANKRD16"
]

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=timeout, context=ctx).read())

def get_canonical(gene):
    """Search by gene and return canonical entry."""
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:9606+AND+reviewed:true&format=json&size=1"
    try:
        data = fetch(url)
        if data.get('results'):
            return data['results'][0]
    except:
        pass
    # Fallback: include unreviewed
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:9606&format=json&size=1"
    data = fetch(url)
    return data['results'][0] if data.get('results') else None

def extract_info(r):
    acc = r['primaryAccession']
    name_raw = r.get('proteinDescription',{}).get('recommendedName',{})
    if isinstance(name_raw, dict):
        name = name_raw.get('fullName',{}).get('value','?')
    else:
        name = str(name_raw)[:80] if name_raw else '?'
    seq = r.get('sequence',{}).get('length','?')
    mass = int(r.get('sequence',{}).get('molWeight',0))/1000

    # Subcellular location
    locs = []
    loc_evids = []
    for c in r.get('comments',[]):
        if c.get('commentType') == 'SUBCELLULAR LOCATION':
            for sl in c.get('subcellularLocations',[]):
                loc_val = sl.get('location',{}).get('locationValue','?')
                locs.append(loc_val)
                for ev in sl.get('location',{}).get('evidences',[]):
                    loc_evids.append(f"{loc_val}:{ev.get('evidenceCode','?')}")

    # GO-CC
    gocc = []
    for ref in r.get('uniProtKBCrossReferences',[]):
        if ref.get('database') == 'GO':
            props = {p['key']:p['value'] for p in ref.get('properties',[])}
            gt = props.get('GoTerm','')
            if gt.startswith('C:'):
                aspect = props.get('GoEvidenceType','')
                gocc.append(f"{gt.replace('C:','')}({aspect[:4] if aspect else '?'})")

    # PDB
    pdbs = []
    for ref in r.get('uniProtKBCrossReferences',[]):
        if ref.get('database') == 'PDB':
            pdbs.append(ref['id'])

    # InterPro
    interpro = []
    for ref in r.get('uniProtKBCrossReferences',[]):
        if ref.get('database') == 'InterPro':
            props = {p['key']:p['value'] for p in ref.get('properties',[])}
            interpro.append(f"{ref['id']}({props.get('entryName','?')})")

    # Function
    func = ''
    for c in r.get('comments',[]):
        if c.get('commentType') == 'FUNCTION':
            func = ' '.join(t.get('value','') for t in c.get('texts',[]))[:200]
            break

    return {
        'acc': acc, 'name': name, 'seq': seq, 'mass': mass,
        'locs': locs, 'loc_evids': loc_evids, 'gocc': gocc,
        'pdbs': pdbs, 'interpro': interpro, 'func': func
    }

for gene in GENES:
    try:
        r = get_canonical(gene)
        if r:
            info = extract_info(r)
            print(f"GENE: {gene}")
            print(f"  ACC: {info['acc']} | {info['seq']}aa | {info['mass']:.1f}kDa")
            print(f"  NAME: {info['name']}")
            print(f"  LOCS: {'; '.join(info['locs']) if info['locs'] else 'NONE'}")
            print(f"  LOC_EVID: {'; '.join(info['loc_evids'][:5]) if info['loc_evids'] else 'NONE'}")
            print(f"  GO-CC: {'; '.join(info['gocc'][:8]) if info['gocc'] else 'NONE'}")
            print(f"  PDB: {info['pdbs'][:10] if info['pdbs'] else 'NONE'}")
            print(f"  IP: {info['interpro'][:5] if info['interpro'] else 'NONE'}")
            if info['func']:
                print(f"  FUNC: {info['func'][:200]}")
        else:
            print(f"GENE: {gene} | NOT_FOUND")
    except Exception as e:
        print(f"GENE: {gene} | ERROR: {e}")
    print()
    time.sleep(0.5)
