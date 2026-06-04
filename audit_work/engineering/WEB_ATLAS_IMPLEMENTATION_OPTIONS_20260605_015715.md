# WEB_ATLAS_IMPLEMENTATION_OPTIONS

## Option A: Pure Static HTML/JS

Files: `docs/index.html`, `docs/protein_index.html`, `docs/category/*.html`, `docs/reports/*.html`, `docs/assets/app.js`, `docs/assets/style.css`, `docs/data/protein_report_index.json`.

Pros: GitHub Pages directly supports it, no framework dependency, stable, easy to audit, compatible with a generated JSON index, and does not require modifying `detail/`.

Cons: table interactions and Markdown conversion pipeline must be maintained locally.

## Option B: MkDocs

Pros: Markdown-friendly, navigation/search themes are attractive, good for docs-style browsing.

Cons: extra dependencies, thousands of reports/images may slow builds, GitHub Pages setup is more complex, and Obsidian link/image normalization still requires custom preprocessing.

## Option C: Quarto / Static Site Generator

Pros: polished tables, strong document rendering, good academic-document aesthetics.

Cons: heavier dependency chain, slower iteration, unnecessary for first public atlas, still needs custom index generation.

## Recommendation

Recommend Option A. It best matches the current project: lightweight, local-buildable, GitHub Pages-ready, non-invasive to `detail/`, and adequate for search/filter/detail pages.
