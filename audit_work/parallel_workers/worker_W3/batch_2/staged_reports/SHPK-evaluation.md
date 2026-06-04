---
type: protein-evaluation
gene: "SHPK"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHPK -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHPK / CARKL |
| Protein Name | Sedoheptulokinase |
| Protein Size | 478 aa / 51.5 kDa |
| UniProt ID | Q9UHJ6 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 478 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 4 publications; extremely novel (≤20) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold high quality (pLDDT=94.1); no PDB |
| Regulatory Domains | 7/10 | x2 | **14** | 3 domains; novel protein baseline, possible uncharacterized domains. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (4 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **136/183** | |
| **Normalized Total** | | | **74.3/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000250 |
| HPA | Nucleoplasm, Nuclear speckles | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

478 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 4 |
| PubMed symbol-only count | 7 |
| PubMed broad count | 19 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Goodman S et al. (2021). "Deficiency of the sedoheptulose kinase (Shpk) does not alter the ability of hematopoietic stem cells to rescue cystinosis in the mouse model.". *Molecular genetics and metabolism*. PMID: 34823997
2. Freed KA et al. (2011). "The 57 kb deletion in cystinosis patients extends into TRPV1 causing dysregulation of transcription in peripheral blood mononuclear cells.". *Journal of medical genetics*. PMID: 21546516
3. Golpasand S et al. (2026). "Genomic dissection of methane emission traits in cattle: A meta-GWAS and heritability analysis across populations.". *PloS one*. PMID: 41961873
4. Wamelink MM et al. (2011). "Elevated concentrations of sedoheptulose in bloodspots of patients with cystinosis caused by the 57-kb deletion: implications for diagnostics and neonatal screening.". *Molecular genetics and metabolism*. PMID: 21195649

**Assessment**: 4 publications; extremely novel (≤20)


**Function Summary**: Acts as a modulator of macrophage activation through control of glucose metabolism

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 94.1 |
| pLDDT > 90 (high confidence) | 87.7% |
| pLDDT 70-90 (moderate) | 10.0% |
| pLDDT 50-70 (low) | 2.1% |
| pLDDT < 50 (disordered) | 0.2% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold high quality (pLDDT=94.1); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR043129 |  |
| InterPro | IPR018484 |  |
| Pfam | PF00370 |  |

**Assessment**: 3 domains; novel protein baseline, possible uncharacterized domains.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| MDM2 | two hybrid | 21988832 | physical association | — |
| TRAF3 | anti tag coimmunoprecipitation | 28514442 | physical association | — |
| THYN1 | anti tag coimmunoprecipitation | 28514442 | physical association | — |
| BTBD9 | anti tag coimmunoprecipitation | 33961781 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| CTNS | 0.978 | 0.000 | — |
| KCNA3 | 0.952 | 0.048 | — |
| FGGY | 0.879 | 0.000 | — |
| GPD2 | 0.796 | 0.097 | — |
| KCNA1 | 0.793 | 0.048 | — |
| KCNN4 | 0.731 | 0.000 | — |
| KCNA6 | 0.717 | 0.048 | — |
| LARS2 | 0.648 | 0.106 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (ISS:UniProtKB)
- cytosol (IBA:GO_Central)

**PPI Assessment**: Physical interactions present (4 partners) but no chromatin regulatory partners

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

**Normalized Score**: 74.3/100 (Raw: 136/183)

**Strengths**:
1. Excellent research novelty (4 publications)
1. Good 3D structural quality (mean pLDDT 94.1)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 74.3/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHJ6
- HPA: https://www.proteinatlas.org/ENSG00000197417-SHPK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHPK%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
