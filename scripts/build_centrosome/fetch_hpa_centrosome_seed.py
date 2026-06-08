#!/usr/bin/env python3
"""
Fetch HPA centrosome and centriolar satellite seed gene lists.

Usage:
    python fetch_hpa_centrosome_seed.py [--output-dir OUTPUT_DIR]
"""
import json
import sys
import os
import urllib.request
from datetime import datetime

CENTROSOME_URL = "https://www.proteinatlas.org/search/subcell_location%3ACentrosome?format=json&size=500"
SATELLITE_URL = "https://www.proteinatlas.org/search/subcell_location%3ACentriolar+satellite?format=json"


def fetch_json(url: str) -> list:
    """Fetch JSON from HPA API."""
    req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def main():
    output_dir = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--output-dir" else "centrosome/data"
    os.makedirs(output_dir, exist_ok=True)

    print("Fetching Centrosome gene list...")
    centro = fetch_json(CENTROSOME_URL)
    centro_genes = set(item["Gene"] for item in centro if "Gene" in item)
    print(f"  Centrosome: {len(centro_genes)} genes")

    print("Fetching Centriolar satellite gene list...")
    satellite = fetch_json(SATELLITE_URL)
    sat_genes = set(item["Gene"] for item in satellite if "Gene" in item)
    print(f"  Centriolar satellite: {len(sat_genes)} genes")

    both = centro_genes & sat_genes
    centro_only = centro_genes - sat_genes
    sat_only = sat_genes - centro_genes
    all_genes = centro_genes | sat_genes

    print(f"  Both sources: {len(both)}")
    print(f"  Centro only: {len(centro_only)}")
    print(f"  Satellite only: {len(sat_only)}")
    print(f"  Total unique: {len(all_genes)}")

    # Write TSV
    tsv_path = os.path.join(output_dir, "centrosome_hpa_seed.tsv")
    with open(tsv_path, "w") as f:
        f.write("gene\thpa_url\tsource_centrosome\tsource_centriolar_satellite\tsource_both\t"
                "hpa_location_text\thpa_reliability\thpa_evidence_text\tseed_source_urls\t"
                "fetched_at\tfetch_method\tnotes\n")
        for gene in sorted(all_genes):
            in_centro = gene in centro_genes
            in_sat = gene in sat_genes
            both_flag = "TRUE" if (in_centro and in_sat) else "FALSE"
            centro_flag = "TRUE" if in_centro else "FALSE"
            sat_flag = "TRUE" if in_sat else "FALSE"
            urls = []
            if in_centro:
                urls.append(CENTROSOME_URL.split("?")[0])
            if in_sat:
                urls.append(SATELLITE_URL.split("?")[0])
            f.write(f"{gene}\t\t{centro_flag}\t{sat_flag}\t{both_flag}\t"
                    f"Centrosome/Centriolar satellite\t\t\t{'|'.join(urls)}\t"
                    f"{datetime.now().isoformat()}\tHPA JSON API\t\n")
    print(f"  TSV written: {tsv_path} ({len(all_genes)} genes)")

    # Write JSON
    json_path = os.path.join(output_dir, "centrosome_hpa_seed.json")
    seed = {
        "metadata": {
            "fetched_at": datetime.now().isoformat(),
            "fetch_method": "HPA JSON API",
            "sources": {"centrosome": CENTROSOME_URL, "centriolar_satellite": SATELLITE_URL},
            "counts": {
                "centrosome": len(centro_genes),
                "centriolar_satellite": len(sat_genes),
                "both_sources": len(both),
                "centrosome_only": len(centro_only),
                "satellite_only": len(sat_only),
                "total_unique": len(all_genes),
            },
        },
        "genes": sorted(all_genes),
        "gene_details": {
            g: {
                "source_centrosome": g in centro_genes,
                "source_centriolar_satellite": g in sat_genes,
                "source_both": g in centro_genes and g in sat_genes,
            }
            for g in sorted(all_genes)
        },
    }
    with open(json_path, "w") as f:
        json.dump(seed, f, indent=2, ensure_ascii=False)
    print(f"  JSON written: {json_path}")

    print("Done.")


if __name__ == "__main__":
    main()
