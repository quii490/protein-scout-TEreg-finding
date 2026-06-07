# Cleanup Execution Summary

Date: 2026-06-07

## Deleted

- Old Obsidian project:
  - `/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`
- Top-level obsolete files/logs in desktop project:
  - `fetch_if_log.txt`
  - `log/`
  - `logs/`
  - `Proteins.md`
  - `skills.md`
  - `validate.py`
  - `validate_strict.py`
  - `.DS_Store`
- Historical one-off scripts under `scripts/`:
  - `batch_*.py`
  - `gen_*.py`
  - `generate_*.py`
  - `write_*.py`
  - `download_*.py`
  - `fetch_if_images.py`
  - `fix_*.py`
  - `query_uniprot.py`
  - empty `scripts/maintenance/`
- Obsolete audit worker/log/cache directories:
  - `audit_work/claude_runs/`
  - `audit_work/*workers/`
  - `audit_work/*logs/`
  - `audit_work/locks/`
  - `audit_work/quarantine/`
  - `audit_work/queues/`
  - `audit_work/repair_audits/`
  - chunk/cache directories for old sheet repair runs
- Rebuildable large engineering intermediate TSVs:
  - `step4b_pages_link_validation_*.tsv`
  - `step4b_image_copy_map_*.tsv`
  - `engineering_step2a_file_tree_snapshot_*.tsv`
- Unreferenced copied web images:
  - `docs/assets/report-images/`
  - confirmed by extracting current HTML image refs before deletion

## Kept

- `detail/`
- `docs/`
- `data/`
- `.git/`
- `README.md`
- `index.html`
- `protein-finding.md`
- `rebuild_summary.py`
- `protein_gate.py`
- `scripts/build/`
- `audit_work/claude_protocols/`
- current engineering runbooks and compact audit summaries

## Size after cleanup

- Desktop project: `2.0G`
- `audit_work/`: `24M`
- `audit_work/engineering/`: `5.8M`
- `scripts/`: `128K`
- `docs/`: `89M`
- `docs/assets/`: `12K`

## Post-cleanup validation

Commands completed successfully:

```bash
python3 scripts/build/build_report_index.py
python3 scripts/build/sync_candidate_annotations.py
python3 scripts/build/build_pages.py
python3 scripts/build/audit_summary_scoring.py
python3 scripts/build/validate_pages_links.py
```

Observed validation result:

- `records=5647`
- `issues=0`
- `broken_internal=0`
- `broken_images=0`
- `reports=5647`
- `categories=8`

After deleting `docs/assets/report-images/`, `validate_pages_links.py` was rerun and still returned:

- `broken_internal=0`
- `broken_images=0`
