# Protein-Scout TEreg-Finding

Comprehensive protein evaluation project for TE (Transposable Element) regulation candidates.

## Current Status

| Metric | Value |
|---|---|
| Excel gene coverage | 4,756/4,756 = 100% |
| Missing genes | 0 |
| Total reports | 5,647 |
| Scored | ~4,177 |
| Rejected/Eliminated | ~1,470 |
| CRITICAL false rejection | 0 |
| HPA IF true mismatch | 0 |
| PAE true mismatch | 0 |

## Directory Structure

```
├── detail/                     # Protein evaluation reports (5,647)
│   ├── nucleoplasm/
│   ├── nucleus-cytoplasm/
│   ├── nuclear-speckle/
│   ├── nuclear-body/
│   ├── nucleolus/
│   ├── nuclear-envelope/
│   ├── chromatin/
│   └── rejected/
├── audit_work/                 # Full audit trail
│   ├── claude_protocols/       # Repair protocols
│   ├── quarantine/             # Stale duplicates
│   ├── final_reports/          # Final acceptance reports
│   ├── verification/           # Verification audits
│   ├── repair_audits/          # Repair audit data
│   ├── queues/                 # Repair queues
│   └── engineering/            # Engineering step reports
├── scripts/                    # Utility scripts
├── data/                       # Summary and processed data
├── logs/                       # Operation logs
├── docs/                       # Documentation
├── protein-finding.md          # Master summary index
├── skills.md                   # Project skills reference
└── protein_gate.py             # Gate validation script
```

## Known Non-blocking Backlog

- 832 need reharvest backlog (network-limited)
- 43 duplicate conflicts (manual review pending)
- ~4,800 pre-existing gate errors (format issues)
- Obsidian vault-path links may show as broken in filesystem browsers

## Next Steps

1. Step 3B: Initialize standalone git repository
2. Step 4: Build GitHub Pages documentation site
3. Step 5: Upload to GitHub

## License

Proprietary — pending decision.
