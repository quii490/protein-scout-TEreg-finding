---
type: protein-evaluation
gene: "SELENOF"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (ER lumen resident protein)"
---

## SELENOF -- Re-evaluation Report (REJECTED: ER Lumen Protein, No Nuclear Localization)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SELENOF / SEP15, Selenoprotein F, 15 kDa selenoprotein |
| Protein Name | Selenoprotein F (15 kDa selenoprotein, thioredoxin-like domain protein) |
| Protein Size | 162 aa, ~17.2 kDa |
| UniProt ID | O60613 (SEP15_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | ER lumen; retained via UGGT1 interaction; no nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 162 aa, small and tractable |
| Research Novelty | 6/10 | x5 | **30** | Estimated ~40-60 PubMed articles |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold predicted; thioredoxin-like fold; no experimental PDB |
| Regulatory Domains | 2/10 | x2 | **4** | Thioredoxin-like domain; no regulatory domains |
| PPI Network | 3/10 | x3 | **9** | UGGT1/UGCGL1 complex; UFBP1; limited interactome |
| Cross-Validation Bonus | -- | -- | **+0** | Consistent ER annotation; no nuclear evidence |
| **Raw Total** | | | **72.0/180** | |
| **Normalized Total** | | | **40.0/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 1/10 (threshold: ≤3). SELENOF is an ER lumen resident protein with no nuclear localization evidence.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Endoplasmic reticulum lumen | Primary annotation |
| Wikipedia | Endoplasmic reticulum | Consensus |
| HPA Cell Atlas | Endoplasmic reticulum | Database annotation |

**Manual Review Assessment**: SELENOF is definitively localized to the endoplasmic reticulum lumen. Its ER retention depends on a tight complex with UGGT1/UGCGL1 (UDP-glucose:glycoprotein glucosyltransferase), an ER-resident protein. This interaction is essential for its retention -- without UGGT1, SELENOF would be secreted. The protein functions in ER protein quality control, regulating protein folding by enhancing UGGT1/UGGT2 catalytic activity. It contains a thioredoxin-like domain with a selenocysteine (Sec) residue at its active site, involved in redox reactions associated with disulfide bond formation -- an ER-specific process. No database annotates nuclear localization. The protein's biology is entirely ER/secretory pathway-dependent. Nuclear localization score 1/10 reflects unequivocal ER localization.

### 4. Protein Size Assessment

SELENOF is 162 amino acids (17.2 kDa), a small protein amenable to structural and biochemical studies. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~40-60 articles |
| Novelty category | 41-80 -> Score 6 |

SELENOF/SEP15 was discovered as part of the selenoproteome. Research focuses on its role in ER redox homeostasis, protein quality control, and selenium biology. Moderate research activity. Score 6/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no experimental structures) |
| Domain | Thioredoxin-like fold |

AlphaFold prediction available. The thioredoxin-like domain is a well-characterized protein fold typically predicted with high confidence. No experimental structures. Score 5/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | Thioredoxin-like domain | Redox-active selenocysteine; protein disulfide isomerase family |
| UniProt | Selenocysteine active site | Sec (U) at active site position |

SELENOF contains a thioredoxin-like domain, characteristic of protein disulfide isomerases and redox enzymes functioning in the ER. No regulatory domains (no kinase, phosphatase, DNA-binding, chromatin, or signaling domains). The selenocysteine active site is specialized for ER redox catalysis. Score 2/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Known Partners | UGGT1/UGCGL1 (ER-retention complex), UFBP1 (UFM1-binding protein) |
| STRING | ER quality control network |

PPI data is limited to ER quality control machinery. No nuclear or regulatory interactions. Score 3/10.

### 9. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED)

**Primary Rejection Reason**: SELENOF is an ER lumen resident protein dedicated to ER protein quality control. It has no nuclear localization, nuclear function, or connection to transcriptional regulation. The rejection is based on unambiguous non-nuclear localization.

### 10. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 1/10. SELENOF's ER biology excludes it from TE-regulation screening.

### 11. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O60613
- HPA Cell Atlas: https://v19.proteinatlas.org/ENSG00000183291-SELENOF/cell
- Wikipedia: https://en.wikipedia.org/wiki/SEP15
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SELENOF
- Note: Harvest packet not available; data compiled from web database queries
