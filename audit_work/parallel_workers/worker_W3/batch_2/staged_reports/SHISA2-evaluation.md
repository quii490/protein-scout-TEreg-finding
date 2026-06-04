---
type: protein-evaluation
gene: "SHISA2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHISA2 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHISA2 / C13orf13, TMEM46 |
| Protein Name | Protein shisa-2 homolog |
| Protein Size | 295 aa / 31.4 kDa |
| UniProt ID | Q6UWI4 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 295 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 17 publications; extremely novel (≤20) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold marginal (pLDDT=63.4); novel protein baseline |
| Regulatory Domains | 7/10 | x2 | **14** | 3 domains; novel protein baseline, possible uncharacterized domains. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (2 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **130/183** | |
| **Normalized Total** | | | **71.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Endoplasmic reticulum membrane | ECO:0000250 |
| HPA | Nucleoplasm, Nuclear bodies, Vesicles | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

295 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 17 |
| PubMed symbol-only count | 24 |
| PubMed broad count | 26 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Motomura S et al. (2024). "CRL2(KLHDC3) and CRL1(Fbxw7) cooperatively mediate c-Myc degradation.". *Oncogene*. PMID: 38698266
2. Zheng Y et al. (2023). "The role of ferroptosis-related genes in airway epithelial cells of asthmatic patients based on bioinformatics.". *Medicine*. PMID: 36862916
3. Li Z et al. (2023). "Simulating neuronal development: exploring potential mechanisms for central nervous system metastasis in acute lymphoblastic leukemia.". *Frontiers in oncology*. PMID: 38239636
4. Souza LS et al. (2025). "Impaired myogenesis in limb girdle muscular dystrophy type 2B.". *Scientific reports*. PMID: 41028869
5. Liu Z et al. (2018). "Shisa2 regulates the fusion of muscle progenitors.". *Stem cell research*. PMID: 30007221

**Assessment**: 17 publications; extremely novel (≤20)


**Function Summary**: Plays an essential role in the maturation of presomitic mesoderm cells by individual attenuation of both FGF and WNT signaling

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 63.4 |
| pLDDT > 90 (high confidence) | 25.8% |
| pLDDT 70-90 (moderate) | 10.2% |
| pLDDT 50-70 (low) | 22.4% |
| pLDDT < 50 (disordered) | 41.7% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold marginal (pLDDT=63.4); novel protein baseline

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR026910 |  |
| InterPro | IPR053891 |  |
| Pfam | PF13908 |  |

**Assessment**: 3 domains; novel protein baseline, possible uncharacterized domains.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| ATXN1L | validated two hybrid | 32296183 | physical association | — |
| ENST00000319420 | clash | 23622248 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| ZNF646 | 0.504 | 0.000 | — |
| RPL36A-HNRNPH2 | 0.471 | 0.000 | — |
| PTGES2 | 0.465 | 0.466 | — |
| CDC42EP5 | 0.452 | 0.000 | — |
| ZADH2 | 0.412 | 0.000 | — |

**Known Complex Membership (GO Cellular Component)**:
- endoplasmic reticulum (IBA:GO_Central)
- endoplasmic reticulum membrane (IEA:UniProtKB-SubCell)

**PPI Assessment**: Physical interactions present (2 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 9 IntAct, 5 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- No bonus criteria met across databases.
- **Total Cross-Validation Bonus**: +0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 71.0/100 (Raw: 130/183)

**Strengths**:
1. Excellent research novelty (17 publications)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 71.0/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWI4
- HPA: https://www.proteinatlas.org/ENSG00000180730-SHISA2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHISA2%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
