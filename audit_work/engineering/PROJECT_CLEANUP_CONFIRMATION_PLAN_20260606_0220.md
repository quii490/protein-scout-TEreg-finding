# Project Cleanup Confirmation Plan

No deletion has been performed.

## Old Obsidian project proposed for deletion

Path:

```text
/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested
```

Observed size:

```text
1.1G
```

Delete only after explicit user confirmation.

## Desktop project to keep

Path:

```text
/Users/quii/Desktop/projects/protein-scout-TEreg-finding
```

Observed size:

```text
3.0G
```

## Keep core

- `.git`
- `.gitignore`
- `.nojekyll`
- `README.md`
- `index.html`
- `protein-finding.md`
- `rebuild_summary.py`
- `protein_gate.py`
- `data/`
- `detail/`
- `docs/`
- `scripts/build/`

## Review before archiving or pruning

- `audit_work/`: keep `audit_work/claude_protocols/`, latest engineering summaries, and current repair audit TSVs; archive old worker logs if space matters.
- `scripts/`: keep active build/repair scripts; archive historical one-off batch scripts only after confirming they are not referenced by current protocols.

## Delete-or-archive candidates

These are candidates only; do not delete without explicit confirmation:

- `fetch_if_log.txt`
- `log/`
- `logs/`
- `skills.md`
- `validate.py`
- `validate_strict.py`
- `Proteins.md`

## Recommended safe cleanup order

1. Commit or otherwise back up the current working tree.
2. Confirm GitHub Pages can be rebuilt locally with current `docs/`.
3. Archive old audit/log files into a dated archive directory, or delete only after confirmation.
4. Delete the old Obsidian project only after explicit confirmation of the exact path.

