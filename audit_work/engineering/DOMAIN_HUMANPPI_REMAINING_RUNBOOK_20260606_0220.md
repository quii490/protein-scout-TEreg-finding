# Domain/SMART + humanPPI Remaining Runbook

Project:

```bash
cd "/Users/quii/Desktop/projects/protein-scout-TEreg-finding"
```

## Current state after Codex repair

- Scored reports total: 4,177
- Scored reports with `DOMAIN_HUMANPPI_REPAIR` block: 1,305
- Scored reports remaining without this block: 2,872
- Last validated build:
  - `scripts/build/audit_summary_scoring.py`: `issues=0`
  - `scripts/build/validate_pages_links.py`: `broken_internal=0 broken_images=0 reports=5647 categories=8`

## Continue remaining scored reports

Run in batches. Do not edit scores or classifications during this enrichment.

```bash
python3 scripts/build/enrich_domain_humanppi.py --status scored --limit 1000 --apply --workers 10 --top-n 8
python3 scripts/build/build_report_index.py
python3 scripts/build/sync_candidate_annotations.py
python3 scripts/build/build_pages.py
python3 scripts/build/audit_summary_scoring.py
python3 scripts/build/validate_pages_links.py
```

Repeat until remaining scored reports without `DOMAIN_HUMANPPI_REPAIR_START` is 0:

```bash
python3 - <<'PY'
import json
from pathlib import Path
records = json.load(open("docs/data/protein_report_index.json"))["records"]
scored = [r for r in records if r.get("status") == "scored"]
with_block = sum(
    "<!-- DOMAIN_HUMANPPI_REPAIR_START -->" in (Path(".") / r["report_path"]).read_text(encoding="utf-8", errors="replace")
    for r in scored
)
print("scored_total", len(scored), "with_block", with_block, "remaining", len(scored) - with_block)
PY
```

## Failed or transient rows

If a batch TSV contains `URLError` or temporary network failures, rerun only those genes with refresh:

```bash
python3 scripts/build/enrich_domain_humanppi.py --genes GENE1,GENE2,GENE3 --apply --refresh-existing --workers 4 --top-n 8
```

`hpa_entry_not_found` means no HPA entry was located from the report/search page; this should be treated as manual review, not an automatic failure.

## Quality gate

Every batch is incomplete until all of these pass:

```bash
python3 scripts/build/build_report_index.py
python3 scripts/build/sync_candidate_annotations.py
python3 scripts/build/build_pages.py
python3 scripts/build/audit_summary_scoring.py
python3 scripts/build/validate_pages_links.py
```

Do not report completion unless the final two scripts return:

- `issues=0`
- `broken_internal=0 broken_images=0`

