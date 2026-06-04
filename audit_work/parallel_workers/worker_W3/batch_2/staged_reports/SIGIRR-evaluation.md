---
type: protein-evaluation
gene: "SIGIRR"
date: 2026-06-04
tags: [protein-scout, evaluation, rejected]
status: rejected
---

## SIGIRR -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SIGIRR / — |
| Protein Name | Single Ig IL-1-related receptor |
| Protein Size | 410 aa / 45.7 kDa |
| UniProt ID | Q6IA17 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 410 aa; ideal range |
| Research Novelty | 0/10 | x5 | **0** | 116 publications; REJECTED (>100) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate quality (pLDDT=75.2); no PDB |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains; some domain richness. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (4 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **85/183** | |
| **Normalized Total** | | | **46.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Membrane | ECO:0000305 |
| HPA | Nucleoli fibrillar center, Cytosol | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


**DECISION**: REJECTED. PubMed count 116 > 100 (threshold: ≤100)

### 4. Protein Size Assessment

410 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 116 |
| PubMed symbol-only count | 229 |
| PubMed broad count | 250 |
| Novelty category | >100 → REJECTED |

**Key Publications**:
1. Yu W et al. (2022). "SIGIRR Mutation in Human Necrotizing Enterocolitis (NEC) Disrupts STAT3-Dependent microRNA Expression in Neonatal Gut.". *Cellular and molecular gastroenterology and hepatology*. PMID: 34563711
2. Bodaszewska-Lubas M et al. (2022). "Dominant-Negative Form of SIGIRR: SIGIRR(ΔE8) Promotes Tumor Growth Through Regulation of Metabolic Pathways.". *Journal of interferon & cytokine research : the official journal of the International Society for Interferon and Cytokine Research*. PMID: 35900274
3. Zaikova EK et al. (2023). "SIGIRR gene variants in term newborns with congenital heart defects and necrotizing enterocolitis.". *Annals of pediatric cardiology*. PMID: 38766461
4. Ye Y et al. (2024). "SIGIRR suppresses hepatitis B virus X protein-induced chronic inflammation in hepatocytes.". *Gene*. PMID: 39013482
5. Teng X et al. (2022). "SIGIRR deficiency contributes to CD4 T cell abnormalities by facilitating the IL1/C/EBPβ/TNF-α signaling axis in rheumatoid arthritis.". *Molecular medicine (Cambridge, Mass.)*. PMID: 36401167

**Assessment**: 116 publications; REJECTED (>100)


**Function Summary**: Acts as a negative regulator of the Toll-like and IL-1R receptor signaling pathways. Attenuates the recruitment of receptor-proximal signaling components to the TLR4 receptor, probably through an TIR-TIR domain interaction with TLR4. Through its extracellular domain interferes with the heterodimerization of Il1R1 and IL1RAP

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 75.2 |
| pLDDT > 90 (high confidence) | 27.3% |
| pLDDT 70-90 (moderate) | 39.8% |
| pLDDT 50-70 (low) | 16.3% |
| pLDDT < 50 (disordered) | 16.6% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold moderate quality (pLDDT=75.2); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR007110 |  |
| InterPro | IPR036179 |  |
| InterPro | IPR013783 |  |
| InterPro | IPR015621 |  |
| InterPro | IPR000157 |  |
| InterPro | IPR035897 |  |
| Pfam | PF01582 |  |

**Assessment**: 7 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| RPN1 | two hybrid pooling approach | 16169070 | physical association | — |
| ENO2 | two hybrid pooling approach | 16169070 | physical association | — |
| ENSP00000519686.1 | two hybrid pooling approach | 20711500 | physical association | — |
| ENST00000397632 | clash | 23622248 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| IRAK1 | 0.970 | 0.333 | — |
| IL37 | 0.943 | 0.000 | — |
| MYD88 | 0.928 | 0.126 | — |
| TLR4 | 0.923 | 0.326 | — |
| IL18R1 | 0.919 | 0.000 | — |
| TRAF6 | 0.870 | 0.292 | — |
| IRAK3 | 0.853 | 0.097 | — |
| TLR5 | 0.846 | 0.088 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cell surface (IBA:GO_Central)
- membrane (IMP:HGNC-UCL)
- plasma membrane (IBA:GO_Central)

**PPI Assessment**: Physical interactions present (4 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 7 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- No bonus criteria met across databases.
- **Total Cross-Validation Bonus**: +0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Normalized Score**: 46.4/100 (Raw: 85/183)

**Core Reasons for Rejection**:
PubMed count 116 > 100 (threshold: ≤100)

### 11. Decision

**FINAL DECISION**: REJECTED. Automatically rejected. PubMed count 116 > 100 (threshold: ≤100)

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6IA17
- HPA: https://www.proteinatlas.org/ENSG00000185187-SIGIRR
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SIGIRR%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
