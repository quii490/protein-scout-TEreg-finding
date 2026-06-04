# Engineering Step 2A — Target Structure Plan
**Date**: 2026-06-05 00:59:59

## Current State
- Total files: 10636
- Detail reports: 5647
- Detail images: 3438
- Audit files: 609
- Root scripts: 0

## Recommended Target Structure

```
protein-interested/              # Keep as is (Obsidian vault root)
├── .obsidian/                   # Keep (Obsidian config)
├── detail/                      # P0_KEEP — all protein reports
│   ├── nucleoplasm/
│   ├── nucleus-cytoplasm/
│   ├── nuclear-speckle/
│   ├── nuclear-body/
│   ├── nucleolus/
│   ├── nuclear-envelope/
│   ├── chromatin/
│   └── rejected/
├── audit_work/                  # Keep — audit trail
│   ├── claude_protocols/        # P0_KEEP
│   ├── final_reports/           # Move acceptance/final reports here later
│   ├── repair_audits/           # Move repair audits here later
│   ├── verification/            # Move verification reports here later
│   ├── queues/                  # Move repair queues here later
│   ├── logs/                    # Move logs here later
│   └── quarantine/              # P0_KEEP
├── protein-finding.md           # P0_KEEP — summary index
├── skills.md                    # P0_KEEP
├── *.py                         # P1_SAFE_MOVE → scripts/ later
├── *.log                        # P1_SAFE_MOVE → audit_work/logs/ later
└── protein_gate.py              # P0_KEEP — essential script
```

## Safety Rules
- detail/ must NOT be moved (all report image links depend on it)
- audit_work/ must NOT be moved (audit trail)
- Root scripts (*.py) can be gathered into scripts/ after link verification
- All images inside detail/ must preserve their current paths
