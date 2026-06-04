# WEB_ATLAS_BUILD_PLAN

## Step 4B: Generate report index

Input: `protein-finding.md`, `detail/`, audit summaries. Output: `data/summary/protein_report_index.tsv/csv`, `docs/data/protein_report_index.json`. Risk: score parse inconsistency. Verification: row count matches expected report/candidate coverage; no missing report paths. Modifies detail: No.

## Step 4C: Generate docs home, index, category pages

Input: generated JSON/index. Output: `docs/index.html`, `docs/protein_index.html`, `docs/category/*.html`, `docs/assets/style.css`, `docs/assets/app.js`. Risk: category count mismatch. Verification: each category count matches index. Modifies detail: No.

## Step 4D: Generate detail page HTML

Input: `detail/*/*/*-evaluation.md`. Output: `docs/reports/*.html`. Risk: Markdown/Obsidian syntax conversion gaps. Verification: generated page count equals index records and spot-check rich reports. Modifies detail: No.

## Step 4E: Copy/rewrite image links

Input: image references in reports. Output: `docs/assets/report-images/...` plus rewritten HTML links, or validated remote/original relative links. Risk: missing local assets, large repository size. Verification: link checker and sampled rendered image checks. Modifies detail: No.

## Step 4F: Link verification

Input: generated docs. Output: link/image validation report under `audit_work/engineering/`. Risk: false positives for remote links. Verification: zero broken local links; remote failures flagged not hidden. Modifies detail: No.

## Step 4G: Commit

Input: generated docs and data after user approval. Output: git commit. Risk: committing oversized assets. Verification: `git status`, size audit. Modifies detail: No unless user separately approves.

## Step 5: Create GitHub repo / push

Input: approved commit. Output: remote repository. Risk: accidental publication of private notes. Verification: final file allowlist before push. Modifies detail: No.

## Step 6: Enable GitHub Pages

Input: GitHub repository with `docs/`. Output: public Pages site. Risk: Pages caching/build delay. Verification: public URL loads home/index/detail pages. Modifies detail: No.

