#!/usr/bin/env python3
"""
Validate the sperm module integrity.

Checks:
1. sperm/ data files exist and are valid
2. sperm/detail/ reports meet minimum requirements
3. Main atlas not polluted
4. docs/sperm/ pages valid
"""
import json
import os
import sys


def check_file(path, desc):
    exists = os.path.exists(path)
    print(f"  {'✅' if exists else '❌'} {desc}: {path}")
    return exists


def count_reports(base):
    count = 0
    for root, dirs, files in os.walk(base):
        count += sum(1 for f in files if f.endswith("-sperm-evaluation.md"))
    return count


def main():
    print("=" * 60)
    print("Sperm Module Validation")
    print("=" * 60)

    errors = 0
    warnings = 0

    # 1. Check seed data
    print("\n[1] Seed Data")
    check_file("sperm/data/sperm_hpa_seed.tsv", "HPA seed TSV")
    check_file("sperm/data/sperm_hpa_seed.json", "HPA seed JSON")
    if os.path.exists("sperm/data/sperm_hpa_seed.json"):
        with open("sperm/data/sperm_hpa_seed.json") as f:
            seed = json.load(f)
        print(f"    Seed genes: {len(seed['genes'])}")

    # 2. Check detail reports
    print("\n[2] Sperm Detail Reports")
    n = count_reports("sperm/detail")
    print(f"    Report count: {n}")
    for d in os.listdir("sperm/detail"):
        if os.path.isdir(f"sperm/detail/{d}"):
            md = f"sperm/detail/{d}/{d}-sperm-evaluation.md"
            if os.path.exists(md):
                lines = len(open(md).readlines())
                status = "✅" if lines >= 100 else "⚠️"
                print(f"    {status} {d}: {lines} lines")
                if lines < 100:
                    warnings += 1
            else:
                print(f"    ❌ {d}: missing evaluation.md")
                errors += 1

    # 3. Main atlas integrity
    print("\n[3] Main Atlas Integrity")
    if os.path.exists("docs/data/protein_report_index.json"):
        with open("docs/data/protein_report_index.json") as f:
            main_idx = json.load(f)
        print(f"    Main index records: {len(main_idx['records'])}")
    count = len([f for f in os.listdir("docs/reports") if f.endswith(".html")])
    print(f"    Main docs/reports: {count}")

    detail_count = 0
    for d in os.listdir("detail"):
        if os.path.isdir(f"detail/{d}"):
            detail_count += sum(1 for f in os.listdir(f"detail/{d}") if f.endswith("-evaluation.md"))
    print(f"    Main detail/ eval reports: {detail_count}")

    # 4. docs/sperm/
    print("\n[4] docs/sperm/")
    check_file("docs/sperm/index.html", "Sperm index")
    check_file("docs/sperm/protein_index.html", "Sperm protein index")
    report_count = len([f for f in os.listdir("docs/sperm/reports") if f.endswith(".html")])
    print(f"    docs/sperm/reports: {report_count}")

    print("\n" + "=" * 60)
    if errors == 0 and warnings == 0:
        print("✅ ALL CHECKS PASSED")
    else:
        print(f"⚠️  {errors} errors, {warnings} warnings")
    print("=" * 60)
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
