# Centrosome Independent Scoring Policy

**Date:** 2026-06-08
**Module:** centrosome (independent of main atlas)

## Core Principle

The centrosome module is an **independent extension** to the main protein-scout TEreg-finding atlas. It does NOT use nuclear localization score as a rejection criterion. All scoring dimensions are tailored for centrosome/centriolar satellite biology.

## Rejection Rules

### Automatic rejection:
- **PubMed total > 100:** Protein is over-studied; eliminated from centrosome discovery list. Same rule as main atlas.
- **NONE based on nuclear score.** Nuclear score is irrelevant for centrosome module.

### No automatic rejection for:
- Nuclear score <= 3 (IRRELEVANT - centrosome proteins may have low nuclear scores)
- Missing nuclear localization evidence (expected for centrosome proteins)

## Scoring Dimensions (Total: 0–100)

### 1. Centrosome Evidence (0–20, weight ×4)
- HPA Centrosome / Centriolar satellite annotation (seed source)
- UniProt subcellular location: centrosome, centriole, basal body, MTOC, cilium, microtubule organizing center
- GO-CC terms: GO:0005813 (centrosome), GO:0005814 (centriole), GO:0000242 (pericentriolar material), GO:0036064 (ciliary basal body), GO:0005815 (microtubule organizing center)
- Literature centrosome/centriole support
- 0: No centrosome evidence beyond HPA seed
- 10: HPA seed + one other source
- 20: HPA seed + UniProt + GO-CC + literature consensus

### 2. TE Relevance (0–20, weight ×5)
- Chromatin / DNA damage / genome stability links
- RNA processing / transcription / splicing
- Cell cycle regulation (centrosome cycle tied to cell cycle)
- Epigenetic / chromatin remodeling
- Known TE-regulator interactions
- Indirect associations are allowed but strength must be explicitly noted
- 0: No detectable TE-relevant connection
- 10: Indirect/circumstantial links (e.g., cell cycle only)
- 20: Direct evidence (chromatin binding, transcription factor, DNA repair, known TE interaction)

### 3. PubMed / Literature (0–20, weight ×4)
- Strict query: "(GENE) AND (centrosome OR centriole OR cilia)"
- Broad query: "(GENE) AND (centrosome OR centriole OR cilia OR microtubule OR cell cycle OR DNA damage OR chromatin)"
- Key papers relevant to centrosome + TE biology
- Alias contamination check required
- 0: >100 total papers (auto-reject) or no centrosome papers
- 10: 10–100 papers, some centrosome-specific
- 20: <50 papers, rich centrosome literature, key papers identified

### 4. PPI / Network (0–20, weight ×3)
- STRING functional partners
- IntAct binary interactions
- BioGRID interactions
- HumanPPI (HPA) interaction partners
- Centrosome-related interactors (other seed genes in network)
- 0: No PPI data available
- 10: Some PPI data, few centrosome partners
- 20: Rich PPI network with multiple centrosome partners

### 5. Structure / Domain (0–10, weight ×2)
- AlphaFold pLDDT (overall confidence)
- PAE (predicted aligned error) - domain packing quality
- PDB experimental structures available
- InterPro / Pfam / SMART domains annotated
- Domain relevance to centrosome function (e.g., coiled-coil, microtubule-binding)
- 0: No structural data, low pLDDT, no domains
- 5: Partial structure/domains available
- 10: High-quality structure, informative domains, PDB available

### 6. Novelty / Specificity (0–10, weight ×2)
- Research novelty (fewer papers = more novel)
- Centrosome localization specificity (is it exclusively centrosome or ubiquitous?)
- Suitability for experimental follow-up (size, solubility, known assays)
- 0: Highly studied, non-specific localization
- 5: Moderately novel
- 10: Very novel, centrosome-specific, experimentally tractable

## Final Score Calculation

```
raw = (centrosome_evidence × 4) + (te_relevance × 5) + (pubmed × 4) + (ppi × 3) + (structure × 2) + (novelty × 2)
final_score = raw / 2.0  (range 0–100)
```

Max raw = 20×4 + 20×5 + 20×4 + 20×3 + 10×2 + 10×2 = 80 + 100 + 80 + 60 + 20 + 20 = 360
Normalized = 360/2.0 = 180 → capped at 100

## Final Status Categories

| Status | Criteria |
|--------|----------|
| **CENTROSOME_ELIMINATED** | PubMed total > 100 (over-studied) |
| **CENTROSOME_CANDIDATE** | Score ≥ 50, all dimensions have evidence, PubMed ≤ 100 |
| **CENTROSOME_LOW_PRIORITY** | Score 25–49, or missing key evidence dimensions, PubMed ≤ 100 |
| **CENTROSOME_MANUAL_REVIEW** | Score < 25, or conflicting evidence, or unusual gene, PubMed ≤ 100 |

## Prohibited Logic

- ❌ "REJECTED because nuclear_score <= 3"
- ❌ "No nuclear evidence → reject"
- ❌ Any nuclear-localization-based rejection
- ❌ Mixing centrosome scores into main atlas tables
- ❌ Modifying main atlas report status based on centrosome evaluation
