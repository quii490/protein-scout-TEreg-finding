---
type: protein-evaluation
gene: "SERTAD4"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD4 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERTAD4 / — |
| Protein Name | SERTA domain-containing protein 4 |
| Protein Size | 356 aa / 39.3 kDa |
| UniProt ID | Q9NUC0 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Supported nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 356 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 13 publications; extremely novel (≤20) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold low (pLDDT=51.6); largely disordered |
| Regulatory Domains | 7/10 | x2 | **14** | 3 domains; novel protein baseline, possible uncharacterized domains. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (4 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0.5** | IntAct + STRING overlap (8 shared partners) (+0.5) |
| **Raw Total** | | | **127.5/183** | |
| **Normalized Total** | | | **69.7/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| GO-CC | nucleus | IEA:InterPro |
| HPA | Nucleoplasm | Supported |

**Assessment**: HPA Supported nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

356 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 13 |
| PubMed symbol-only count | 19 |
| PubMed broad count | 19 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Stratton MS et al. (2019). "Dynamic Chromatin Targeting of BRD4 Stimulates Cardiac Fibroblast Activation.". *Circulation research*. PMID: 31409188
2. Chang Y et al. (2025). "Exploring SERTAD4 as a prognostic biomarker and therapeutic target in breast cancer: insights from multidatabase analyses and in vitro studies.". *Clinical and experimental medicine*. PMID: 40658117
3. Francois A et al. (2026). "Sertad4 Regulates Pathological Cardiac Remodeling.". *bioRxiv : the preprint server for biology*. PMID: 41889836
4. Hao HJ et al. (2024). "Neuroprotective effects of acteoside in a glaucoma mouse model by targeting Serta domain-containing protein 4.". *International journal of ophthalmology*. PMID: 38638260
5. Chen Y et al. (2024). "KRAS mutation promotes the colonization of Fusobacterium nucleatum in colorectal cancer by down-regulating SERTAD4.". *Journal of cellular and molecular medicine*. PMID: 39462261

**Assessment**: 13 publications; extremely novel (≤20)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 51.6 |
| pLDDT > 90 (high confidence) | 9.3% |
| pLDDT 70-90 (moderate) | 5.1% |
| pLDDT 50-70 (low) | 17.7% |
| pLDDT < 50 (disordered) | 68.0% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold low (pLDDT=51.6); largely disordered

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR009263 |  |
| InterPro | IPR029708 |  |
| Pfam | PF06031 |  |

**Assessment**: 3 domains; novel protein baseline, possible uncharacterized domains.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| AKT1 | pull down | 20368287 | physical association | — |
| BCAP31 | cross-linking study | 30021884 | physical association | — |
| SARS1 | two hybrid array | 32814053 | physical association | — |
| FKBP1A | two hybrid array | 32814053 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| PPP2R2C | 0.843 | 0.838 | — |
| PPP2R1A | 0.826 | 0.826 | — |
| PPP2R2A | 0.826 | 0.824 | — |
| PPP2R2D | 0.795 | 0.792 | — |
| CBLL2 | 0.789 | 0.789 | — |
| PPP2R1B | 0.773 | 0.773 | — |
| SERTAD1 | 0.700 | 0.000 | — |
| PPP2CB | 0.690 | 0.687 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- nucleus (IEA:InterPro)

**PPI Assessment**: Physical interactions present (4 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- IntAct + STRING overlap (8 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 69.7/100 (Raw: 127.5/183)

**Strengths**:
1. Excellent research novelty (13 publications)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 69.7/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUC0
- HPA: https://www.proteinatlas.org/ENSG00000082497-SERTAD4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERTAD4%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
