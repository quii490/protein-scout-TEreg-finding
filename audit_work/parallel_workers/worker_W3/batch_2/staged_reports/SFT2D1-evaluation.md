---
type: protein-evaluation
gene: "SFT2D1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SFT2D1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SFT2D1 / C6orf83 |
| Protein Name | Vesicle transport protein SFT2A |
| Protein Size | 159 aa / 17.8 kDa |
| UniProt ID | Q8WV19 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 8/10 | x1 | **8** | 159 aa; acceptable range |
| Research Novelty | 10/10 | x5 | **50** | 5 publications; extremely novel (≤20) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate quality (pLDDT=74.3); no PDB |
| Regulatory Domains | 7/10 | x2 | **14** | 3 domains; novel protein baseline, possible uncharacterized domains. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (15 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **131/183** | |
| **Normalized Total** | | | **71.6/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Membrane | ECO:0000255 |
| HPA | Nucleoplasm, Nuclear bodies, Cytosol | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

159 aa; acceptable range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 5 |
| PubMed symbol-only count | 7 |
| PubMed broad count | 7 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Cheng F et al. (2025). "Unraveling the role of histone acetylation in sepsis biomarker discovery.". *Frontiers in molecular biosciences*. PMID: 40370519
2. Liu D et al. (2020). "A Transcriptome-Wide Association Study Identifies Candidate Susceptibility Genes for Pancreatic Cancer Risk.". *Cancer research*. PMID: 32907841
3. Li L et al. (2025). "Biomarker identification for rheumatoid arthritis with inadequate response to DMARD and TNF therapies using multidimensional analyses.". *Immunobiology*. PMID: 40288069
4. Ognibene M et al. (2020). "Identification of a minimal region of loss on chromosome 6q27 associated with poor survival of high-risk neuroblastoma patients.". *Cancer biology & therapy*. PMID: 31959052
5. Kang J et al. (2024). "Identification of a new gene signature for prognostic evaluation in cervical cancer: based on cuproptosis-associated angiogenesis and multi-omics analysis.". *Cancer cell international*. PMID: 38200479

**Assessment**: 5 publications; extremely novel (≤20)


**Function Summary**: May be involved in fusion of retrograde transport vesicles derived from an endocytic compartment with the Golgi complex

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 74.3 |
| pLDDT > 90 (high confidence) | 0.0% |
| pLDDT 70-90 (moderate) | 64.8% |
| pLDDT 50-70 (low) | 35.2% |
| pLDDT < 50 (disordered) | 0.0% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold moderate quality (pLDDT=74.3); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR007305 |  |
| InterPro | IPR011691 |  |
| Pfam | PF04178 |  |

**Assessment**: 3 domains; novel protein baseline, possible uncharacterized domains.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| glmU | two hybrid pooling approach | 20711500 | physical association | — |
| CERCAM | two hybrid prey pooling approach | 32296183 | physical association | — |
| SLC10A1 | two hybrid prey pooling approach | 32296183 | physical association | — |
| SYT16 | two hybrid array | 32296183 | physical association | — |
| TMX2 | two hybrid array | 32296183 | physical association | — |
| RETREG3 | two hybrid array | 32296183 | physical association | — |
| SNX1 | two hybrid array | 32296183 | physical association | — |
| DIABLO | two hybrid array | 32296183 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| PRR18 | 0.651 | 0.000 | — |
| C6orf118 | 0.593 | 0.000 | — |
| RPS6KA2 | 0.554 | 0.000 | — |
| GOLT1A | 0.519 | 0.298 | — |
| SFT2D3 | 0.518 | 0.000 | — |
| CTDNEP1 | 0.497 | 0.000 | — |
| FAM43A | 0.496 | 0.000 | — |
| TMEM60 | 0.452 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IEA:UniProtKB-ARBA)
- endomembrane system (IEA:UniProtKB-ARBA)
- membrane (IEA:UniProtKB-SubCell)

**PPI Assessment**: Physical interactions present (15 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- No bonus criteria met across databases.
- **Total Cross-Validation Bonus**: +0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 71.6/100 (Raw: 131/183)

**Strengths**:
1. Excellent research novelty (5 publications)
1. Good 3D structural quality (mean pLDDT 74.3)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 71.6/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8WV19
- HPA: https://www.proteinatlas.org/ENSG00000198818-SFT2D1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SFT2D1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
