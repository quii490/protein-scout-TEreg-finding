# WEB_ATLAS_INFORMATION_ARCHITECTURE

Primary source recommendation: `protein-finding.md` + fresh `detail/` scan.

## 1. Home / Overview

Path: `docs/index.html`

Content: project introduction, screening goal, brief scoring standard, data status, Excel coverage, scored/rejected counts, localization counts, known backlog, search box, and entry buttons to the atlas table.

Use summary cards for total genes, scored, rejected, categories, reports with images/evidence markers, and backlog warnings.

## 2. Protein Index / All Proteins

Path: `docs/protein_index.html`

Functions: all-protein table, gene search, status/category filters, score sorting, evidence badges, and detail links. Load `docs/data/protein_report_index.json` in browser-side JavaScript.

## 3. Category Pages

- `docs/category/nucleoplasm.html`
- `docs/category/nucleus-cytoplasm.html`
- `docs/category/nuclear-speckle.html`
- `docs/category/nuclear-body.html`
- `docs/category/nucleolus.html`
- `docs/category/nuclear-envelope.html`
- `docs/category/chromatin.html`
- `docs/category/rejected.html`

Each page should show the category description, count, filterable/sortable category table, and links back to home/index. Add `manual-review` or `duplicate-conflict` pages only after the normalized index exposes reliable flags.

## 4. Detail Pages

Path: `docs/reports/GENE.html`

Top metadata: gene, status, category, score, nuclear_score, original detail path, evidence badges. Body: rendered full evaluation Markdown. Navigation: home, all proteins, category page, previous/next within category if practical.

## 5. Search

Implement lightweight front-end search over `docs/data/protein_report_index.json`: gene symbol exact/prefix/fuzzy-lite matching, status/category filters, min/max score or descending sorting, and instant jump to detail page.

