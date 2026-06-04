---
type: protein-evaluation
gene: "SHROOM4"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHROOM4 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHROOM4 / KIAA1202, SHAP |
| Protein Name | Protein Shroom4 |
| Protein Size | 1493 aa / 164.9 kDa |
| UniProt ID | Q9ULL8 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | HPA Approved nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus |
| Protein Size | 5/10 | x1 | **5** | 1493 aa; suboptimal range |
| Research Novelty | 10/10 | x5 | **50** | 10 publications; extremely novel (≤20) |
| 3D Structure | 7/10 | x3 | **21** | PDB (1 entries); AlphaFold low confidence (pLDDT=47.1) |
| Regulatory Domains | 8/10 | x2 | **16** | 6 annotated domains; some domain richness. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (14 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0.5** | PDB + AlphaFold structural data agreement (+0.5) |
| **Raw Total** | | | **134.5/183** | |
| **Normalized Total** | | | **73.5/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm, cytoskeleton | ECO:0000269, ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm, Vesicles, Focal adhesion sites | Approved |

**Assessment**: HPA Approved nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus


### 4. Protein Size Assessment

1493 aa; suboptimal range. The protein size is outside the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 10 |
| PubMed symbol-only count | 20 |
| PubMed broad count | 20 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Yoder M et al. (2007). "Shroom4 (Kiaa1202) is an actin-associated protein implicated in cytoskeletal organization.". *Cell motility and the cytoskeleton*. PMID: 17009331
2. Kolvenbach CM et al. (2023). "X-linked variations in SHROOM4 are implicated in congenital anomalies of the urinary tract and the anorectal, cardiovascular and central nervous systems.". *Journal of medical genetics*. PMID: 36379543
3. Bian WJ et al. (2022). "SHROOM4 Variants Are Associated With X-Linked Epilepsy With Features of Generalized Seizures or Generalized Discharges.". *Frontiers in molecular neuroscience*. PMID: 35663265
4. Danyel M et al. (2019). "Familial Xp11.22 microdeletion including SHROOM4 and CLCN5 is associated with intellectual disability, short stature, microcephaly and Dent disease: a case report.". *BMC medical genomics*. PMID: 30630535
5. Wang Y et al. (2024). "Comprehensive Long-Read Sequencing Analysis Discloses the Transcriptome Features of Papillary Thyroid Microcarcinoma.". *The Journal of clinical endocrinology and metabolism*. PMID: 38038628

**Assessment**: 10 publications; extremely novel (≤20)


**Function Summary**: Probable regulator of cytoskeletal architecture that plays an important role in development. May regulate cellular and cytoskeletal architecture by modulating the spatial distribution of myosin II (By similarity)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 47.1 |
| pLDDT > 90 (high confidence) | 14.1% |
| pLDDT 70-90 (moderate) | 7.9% |
| pLDDT 50-70 (low) | 4.5% |
| pLDDT < 50 (disordered) | 73.5% |
| Available PDB Entries | 1 |
| PDB Details |   - 2EDP: NMR, -, chains A=6-92 |

**Assessment**: PDB (1 entries); AlphaFold low confidence (pLDDT=47.1)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR014799 |  |
| InterPro | IPR001478 |  |
| InterPro | IPR036034 |  |
| InterPro | IPR027685 |  |
| Pfam | PF08687 |  |
| Pfam | PF00595 |  |

**Assessment**: 6 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| ABCC4 | holdup assay | 36115835 | direct interaction | — |
| ASIC3 | holdup assay | 36115835 | direct interaction | — |
| APBA1 | holdup assay | 36115835 | direct interaction | — |
| APBA2 | holdup assay | 36115835 | direct interaction | — |
| AHNAK | holdup assay | 36115835 | direct interaction | — |
| CARD11 | holdup assay | 36115835 | direct interaction | — |
| CASK | holdup assay | 36115835 | direct interaction | — |
| ARHGAP21 | holdup assay | 36115835 | direct interaction | — |
| ... (6 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| APEX1 | 0.657 | 0.000 | — |
| PROM2 | 0.545 | 0.000 | — |
| CENPVL1 | 0.507 | 0.000 | — |
| LYG1 | 0.507 | 0.000 | — |
| ZNF106 | 0.488 | 0.088 | — |
| ALMS1 | 0.486 | 0.070 | — |
| EPM2AIP1 | 0.475 | 0.088 | — |
| IQSEC2 | 0.472 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- actin filament (IDA:UniProtKB)
- adherens junction (IBA:GO_Central)
- apical junction complex (IBA:GO_Central)
- apical plasma membrane (ISS:UniProtKB)
- basal plasma membrane (ISS:UniProtKB)
- cortical actin cytoskeleton (IBA:GO_Central)
- cytoplasm (ISS:UniProtKB)
- cytoplasmic side of plasma membrane (IDA:UniProtKB)

**PPI Assessment**: Physical interactions present (14 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold structural data agreement (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 73.5/100 (Raw: 134.5/183)

**Strengths**:
1. Excellent research novelty (10 publications)
1. Good 3D structural quality (mean pLDDT 47.1)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 6/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 73.5/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULL8
- HPA: https://www.proteinatlas.org/ENSG00000158352-SHROOM4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHROOM4%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
