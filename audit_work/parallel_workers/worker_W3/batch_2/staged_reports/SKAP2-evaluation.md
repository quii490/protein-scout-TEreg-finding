---
type: protein-evaluation
gene: "SKAP2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKAP2 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SKAP2 / PRAP, RA70, SAPS, SCAP2, SKAP55R |
| Protein Name | Src kinase-associated phosphoprotein 2 |
| Protein Size | 359 aa / 41.2 kDa |
| UniProt ID | O75563 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Supported nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 359 aa; ideal range |
| Research Novelty | 8/10 | x5 | **40** | 45 publications; very novel (21-50) |
| 3D Structure | 9/10 | x3 | **27** | PDB (1 entries) + AlphaFold good quality (pLDDT=74.0) |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains; some domain richness. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (6 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+1.0** | PDB + AlphaFold structural data agreement (+0.5) | IntAct + STRING overlap (3 shared partners) (+0.5) |
| **Raw Total** | | | **132.0/183** | |
| **Normalized Total** | | | **72.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm, Cytosol | Supported |

**Assessment**: HPA Supported nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

359 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 45 |
| PubMed symbol-only count | 67 |
| PubMed broad count | 67 |
| Novelty category | 21-50 → 8 |

**Key Publications**:
1. Wilmink M et al. (2023). "SKAP2-A Molecule at the Crossroads for Integrin Signalling and Immune Cell Migration and Function.". *Biomedicines*. PMID: 37893161
2. Feng Y et al. (2025). "Expression and Regulatory Roles of SKAP2 and Cortactin in Mouse Ovarian Tissue and Oocyte Maturation.". *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 40629241
3. Bouti P et al. (2024). "SKAP2 acts downstream of CD11b/CD18 and regulates neutrophil effector function.". *Frontiers in immunology*. PMID: 38487529
4. Fløyel T et al. (2021). "SKAP2, a Candidate Gene for Type 1 Diabetes, Regulates β-Cell Apoptosis and Glycemic Control in Newly Diagnosed Patients.". *Diabetes*. PMID: 33203694
5. Boras M et al. (2017). "Skap2 is required for β(2) integrin-mediated neutrophil recruitment and functions.". *The Journal of experimental medicine*. PMID: 28183734

**Assessment**: 45 publications; very novel (21-50)


**Function Summary**: May be involved in B-cell and macrophage adhesion processes. In B-cells, may act by coupling the B-cell receptor (BCR) to integrin activation. May play a role in src signaling pathway

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 74.0 |
| pLDDT > 90 (high confidence) | 39.6% |
| pLDDT 70-90 (moderate) | 20.6% |
| pLDDT 50-70 (low) | 14.8% |
| pLDDT < 50 (disordered) | 25.1% |
| Available PDB Entries | 1 |
| PDB Details |   - 3OMH: X-ray, 2.90 A, chains E/F/G/H=71-79 |

**Assessment**: PDB (1 entries) + AlphaFold good quality (pLDDT=74.0)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR011993 |  |
| InterPro | IPR001849 |  |
| InterPro | IPR036028 |  |
| InterPro | IPR001452 |  |
| InterPro | IPR037781 |  |
| Pfam | PF00169 |  |
| Pfam | PF00018 |  |

**Assessment**: 7 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| Rgs1 | two hybrid | 15102471 | physical association | — |
| DNAJB6 | two hybrid fragment pooling approach | 23414517 | physical association | — |
| FASLG | phage display | 19807924 | direct interaction | — |
| FYN | two hybrid fragment pooling approach | 31413325 | physical association | — |
| PTK2B | two hybrid fragment pooling approach | 31413325 | physical association | — |
| PTPN22 | x-ray crystallography | 21719704 | direct interaction | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| FYB1 | 0.981 | 0.434 | — |
| ITGB1 | 0.914 | 0.000 | — |
| ITGA4 | 0.901 | 0.000 | — |
| ITGA5 | 0.900 | 0.000 | — |
| FYN | 0.896 | 0.690 | — |
| LCP2 | 0.851 | 0.074 | — |
| PRAM1 | 0.829 | 0.292 | — |
| LYN | 0.781 | 0.481 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IBA:GO_Central)
- cytosol (IDA:HPA)
- nucleoplasm (IDA:HPA)
- plasma membrane (IDA:MGI)

**PPI Assessment**: Physical interactions present (6 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold structural data agreement (+0.5)
- IntAct + STRING overlap (3 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 72.1/100 (Raw: 132.0/183)

**Strengths**:
1. Excellent research novelty (45 publications)
1. Good 3D structural quality (mean pLDDT 74.0)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 72.1/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75563
- HPA: https://www.proteinatlas.org/ENSG00000005020-SKAP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SKAP2%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
