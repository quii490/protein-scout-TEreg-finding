# CODEX_STEP4A0_WEB_DESIGN_EXPLORATION_REPORT

- Timestamp: 20260605_015715
- Project: `/Users/quii/Desktop/projects/protein-scout-TEreg-finding`
- Detail reports detected: 5647
- Probe status distribution: {'scored': 3152, 'rejected': 2495}
- Probe category distribution: {'chromatin': 138, 'nuclear-body': 74, 'nuclear-envelope': 147, 'nuclear-speckle': 329, 'nucleolus': 400, 'nucleoplasm': 2939, 'nucleus-cytoplasm': 150, 'rejected': 1470}

## 1. Current usable total/index files

- `protein-finding.md`: best existing human-facing total table; contains category sections, scoring columns, total score, recommendations, and detail links.
- `Proteins.md`: symbol list only; useful as coverage/candidate reference, not sufficient for web tables.
- `audit_work/*coverage*`, `audit_work/*status*`, duplicate audits: useful QA/backlog sources, not primary web index.
- `data/processed/*`: useful source-evidence caches but too granular for the atlas table.

## 2. Recommended source/index strategy

Use `protein-finding.md` as the primary summary seed and regenerate a normalized `protein_report_index` by scanning `detail/`. Do not rely on `protein-finding.md` alone because its links are Obsidian-style and it lacks normalized status/category/evidence fields.

## 3. Recommended website structure

- Home overview: `docs/index.html`
- Full protein table: `docs/protein_index.html`
- Category tables: `docs/category/{nucleoplasm,nucleus-cytoplasm,nuclear-speckle,nuclear-body,nucleolus,nuclear-envelope,chromatin,rejected}.html`
- Detail pages: `docs/reports/GENE.html`
- Search/filter data: `docs/data/protein_report_index.json`

## 4. Recommended pages

Home, all-protein index, seven scored localization category pages, rejected page, and one generated detail page per report. Add manual-review or duplicate-conflict pages later only if reliable flags are exposed in the generated index.

## 5. Recommended data schema

Generate `gene`, `status`, `category`, `score`, `nuclear_score`, `report_path`, `docs_report_path`, `category_page`, `lines`, evidence flags (`has_hpa`, `has_if_image`, `has_pae`, `has_pdb`, `has_ppi`, `has_pubmed`, `has_scoring_table`, `has_manual_review`), duplicate fields, primary-candidate flag, and known backlog flags.

## 6. Recommended interactions

Client-side gene search, status/category filters, score sorting, evidence badges, category navigation, and direct gene-to-detail jump. Keep the UI table-first and research-atlas oriented.

## 7. Recommended technical option

Option A: pure static HTML/JS under `docs/`. This is the simplest GitHub Pages-compatible approach and avoids framework dependencies while supporting search, filters, and generated detail pages.

## 8. Main risks

- Score/nuclear_score parsing varies by report template; use normalized index generation and avoid overconfident guessing.
- Obsidian wikilinks and local image paths must be rewritten for GitHub Pages.
- Thousands of report pages and images may affect repository size and link-check time.
- Duplicate/conflict/backlog flags need explicit audit sources; do not invent them from path names alone.
- Rejected reports may be thin or previously repaired unevenly; site should display them honestly and optionally flag parse/evidence gaps.

## 9. Next step readiness

The project is ready to enter Step 4B using the recommended default: generate a normalized static-site index from `protein-finding.md` plus `detail/`, then build under `docs/` without modifying `detail/`.

## User decisions needed

- Default recommended: include the `rejected` category page. User can decide whether it should be visible in top navigation or secondary navigation.
- Default recommended: copy local report images into `docs/assets/report-images/` during Step 4E for GitHub Pages reliability. User can choose linking in place if repository size becomes a concern.
- Default recommended: keep duplicate/manual-review pages out of first build unless parser flags are reliable.

## Final decision

READY_FOR_STEP4B_BUILD_STATIC_SITE
