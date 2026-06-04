---
type: protein-evaluation
gene: "SIGLEC15"
date: 2026-06-04
tags: [protein-scout, evaluation, rejected]
status: rejected
---

## SIGLEC15 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SIGLEC15 / CD33L3 |
| Protein Name | Sialic acid-binding Ig-like lectin 15 |
| Protein Size | 328 aa / 35.7 kDa |
| UniProt ID | Q6ZMC9 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 328 aa; ideal range |
| Research Novelty | 0/10 | x5 | **0** | 110 publications; REJECTED (>100) |
| 3D Structure | 9/10 | x3 | **27** | PDB (1 entries) + AlphaFold good quality (pLDDT=78.4) |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains; some domain richness. |
| PPI Network | 4/10 | x3 | **12** | No physical interactions; STRING predicted partners present |
| Cross-Validation Bonus | — | max +3 | **+0.5** | PDB + AlphaFold structural data agreement (+0.5) |
| **Raw Total** | | | **85.5/183** | |
| **Normalized Total** | | | **46.7/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Membrane | Annotation |
| HPA | Nucleoplasm, Golgi apparatus | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


**DECISION**: REJECTED. PubMed count 110 > 100 (threshold: ≤100)

### 4. Protein Size Assessment

328 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 110 |
| PubMed symbol-only count | 208 |
| PubMed broad count | 212 |
| Novelty category | >100 → REJECTED |

**Key Publications**:
1. Udagawa N et al. (2021). "Osteoclast differentiation by RANKL and OPG signaling pathways.". *Journal of bone and mineral metabolism*. PMID: 33079279
2. Deng D et al. (2024). "Evasion of immunosurveillance by the upregulation of Siglec15 in bladder cancer.". *Journal of hematology & oncology*. PMID: 39609852
3. Zhao A et al. (2025). "Predicting ovarian cancer prognosis and immunotherapy response through siglec15 and PD-L1 expression analysis.". *Translational oncology*. PMID: 41076961
4. Wang Y et al. (2022). "Emerging strategies in targeting tumor-resident myeloid cells for cancer immunotherapy.". *Journal of hematology & oncology*. PMID: 36031601
5. Huang S et al. (2023). "Siglec15 promotes the migration of thyroid carcinoma cells by enhancing the EGFR protein stability.". *Glycobiology*. PMID: 37129515

**Assessment**: 110 publications; REJECTED (>100)


**Function Summary**: Binds sialylated glycoproteins

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 78.4 |
| pLDDT > 90 (high confidence) | 57.0% |
| pLDDT 70-90 (moderate) | 12.2% |
| pLDDT 50-70 (low) | 7.3% |
| pLDDT < 50 (disordered) | 23.5% |
| Available PDB Entries | 1 |
| PDB Details |   - 7ZOZ: X-ray, 2.10 A, chains A=20-328 |

**Assessment**: PDB (1 entries) + AlphaFold good quality (pLDDT=78.4)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR007110 |  |
| InterPro | IPR036179 |  |
| InterPro | IPR013783 |  |
| InterPro | IPR003599 |  |
| InterPro | IPR013106 |  |
| InterPro | IPR042836 |  |
| Pfam | PF07686 |  |

**Assessment**: 7 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| — | — | — | — | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| TYROBP | 0.978 | 0.000 | — |
| EEF1A2 | 0.889 | 0.000 | — |
| SIGLEC1 | 0.759 | 0.126 | — |
| CD22 | 0.750 | 0.126 | — |
| SIGLEC7 | 0.669 | 0.126 | — |
| MAG | 0.660 | 0.126 | — |
| SIGLEC11 | 0.643 | 0.126 | — |
| HCST | 0.624 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- plasma membrane (IBA:GO_Central)
- protein-containing complex (IEA:Ensembl)

**PPI Assessment**: No physical interactions; STRING predicted partners present

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 0 IntAct, 15 STRING | Single/No source |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold structural data agreement (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Normalized Score**: 46.7/100 (Raw: 85.5/183)

**Core Reasons for Rejection**:
PubMed count 110 > 100 (threshold: ≤100)

### 11. Decision

**FINAL DECISION**: REJECTED. Automatically rejected. PubMed count 110 > 100 (threshold: ≤100)

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZMC9
- HPA: https://www.proteinatlas.org/ENSG00000197046-SIGLEC15
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SIGLEC15%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
