# Detail Report Schema Probe Summary

- Timestamp: 20260605_015715
- Detail report count: 5647
- Stable gene parse ratio: 100.0%
- Stable status parse ratio: 100.0%
- Stable category parse ratio: 100.0%
- Score parse or rejected-without-score ratio: 99.6%
- Image reference count: 36
- Parse quality distribution: {'GOOD': 5544, 'PARTIAL': 103}
- Status distribution: {'scored': 3152, 'rejected': 2495}
- Category distribution: {'chromatin': 138, 'nuclear-body': 74, 'nuclear-envelope': 147, 'nuclear-speckle': 329, 'nucleolus': 400, 'nucleoplasm': 2939, 'nucleus-cytoplasm': 150, 'rejected': 1470}

## Evidence Marker Coverage

- has_hpa: 5503/5647 (97.4%)
- has_if_image: 4840/5647 (85.7%)
- has_pae: 4915/5647 (87.0%)
- has_pdb: 4883/5647 (86.5%)
- has_ppi: 5050/5647 (89.4%)
- has_pubmed: 5619/5647 (99.5%)
- has_scoring_table: 5098/5647 (90.3%)
- has_manual_review: 167/5647 (3.0%)
- has_images: 18/5647 (0.3%)

## Detail Page Generation Difficulty

- Gene and file path are reliably recoverable from `detail/<category>/<gene>/<gene>-evaluation.md`.
- Category is reliable from directory name; status can default to `rejected` for `detail/rejected` and `scored` otherwise, with report text as a secondary check.
- Scores are not uniformly formatted across all reports; site generation should prefer a normalized generated index and show blank/NA rather than guessing when parsing fails.
- Images may be Obsidian-relative, local nested assets, or remote links. Step 4E should validate and optionally copy image assets into `docs/assets/report-images/`.
- Existing reports can be converted to HTML safely if the converter writes only to `docs/reports/` and never edits `detail/`.
