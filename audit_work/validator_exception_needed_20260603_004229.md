# Validator Exception Needed
**Date**: 2026-06-03 00:42:29

## AAAS — PubMed Alias Collision

| Field | Value |
|---|---|
| Gene | AAAS |
| Rule | PubMed>100 auto-reject |
| Why wrong | AAA abbreviation collision inflates count from ~140 relevant → 596/4450 raw |
| Evidence | E-utils disambiguation confirms pollution |
| Recommended | Add gene-symbol-disambiguation check for AAAS/AAA before applying PubMed>100 rule |
| User approval needed | Yes |

The validator cannot distinguish between genuine publication volume and abbreviation-collision inflation. For genes where the abbreviation matches a common medical term (AAA=abdominal aortic aneurysm, affecting AAAS counts), manual override is warranted.
