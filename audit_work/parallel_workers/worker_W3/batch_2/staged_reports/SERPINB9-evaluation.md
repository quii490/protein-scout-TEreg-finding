---
type: protein-evaluation
gene: "SERPINB9"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERPINB9 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERPINB9 / PI9 |
| Protein Name | Serpin B9 |
| Protein Size | 376 aa / 42.4 kDa |
| UniProt ID | P50453 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | HPA Approved nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus |
| Protein Size | 10/10 | x1 | **10** | 376 aa; ideal range |
| Research Novelty | 6/10 | x5 | **30** | 52 publications; moderate novelty (51-100) |
| 3D Structure | 10/10 | x3 | **30** | PDB (1 entries) + AlphaFold high quality (pLDDT=91.2) |
| Regulatory Domains | 8/10 | x2 | **16** | 8 annotated domains; some domain richness. |
| PPI Network | 10/10 | x3 | **30** | Physical interactions (IntAct) + 3 chromatin-regulatory partners; high regulatory relevance |
| Cross-Validation Bonus | — | max +3 | **+0.5** | PDB + AlphaFold structural data agreement (+0.5) |
| **Raw Total** | | | **140.5/183** | |
| **Normalized Total** | | | **76.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | Annotation |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm, Cytosol | Approved |

**Assessment**: HPA Approved nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus


### 4. Protein Size Assessment

376 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 52 |
| PubMed symbol-only count | 90 |
| PubMed broad count | 188 |
| Novelty category | 51-100 → 6 |

**Key Publications**:
1. Jiang P et al. (2018). "Signatures of T cell dysfunction and exclusion predict cancer immunotherapy response.". *Nature medicine*. PMID: 30127393
2. Collora JA et al. (2022). "Single-cell multiomics reveals persistence of HIV-1 in expanded cytotoxic T cell clones.". *Immunity*. PMID: 35320704
3. Hagiwara M et al. (2022). "MUC1-C integrates type II interferon and chromatin remodeling pathways in immunosuppression of prostate cancer.". *Oncoimmunology*. PMID: 35127252
4. Yan W et al. (2025). "Microbiota-reprogrammed phosphatidylcholine inactivates cytotoxic CD8 T cells through UFMylation via exosomal SerpinB9 in multiple myeloma.". *Nature communications*. PMID: 40128181
5. Harding J et al. (2024). "Immune-privileged tissues formed from immunologically cloaked mouse embryonic stem cells survive long term in allogeneic hosts.". *Nature biomedical engineering*. PMID: 37996616

**Assessment**: 52 publications; moderate novelty (51-100)


**Function Summary**: Granzyme B inhibitor

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 91.2 |
| pLDDT > 90 (high confidence) | 83.0% |
| pLDDT 70-90 (moderate) | 11.4% |
| pLDDT 50-70 (low) | 0.8% |
| pLDDT < 50 (disordered) | 4.8% |
| Available PDB Entries | 1 |
| PDB Details |   - 8ZCR: X-ray, 1.93 A, chains A=2-333, B=344-376 |

**Assessment**: PDB (1 entries) + AlphaFold high quality (pLDDT=91.2)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR000240 |  |
| InterPro | IPR023795 |  |
| InterPro | IPR023796 |  |
| InterPro | IPR000215 |  |
| InterPro | IPR036186 |  |
| InterPro | IPR042178 |  |
| InterPro | IPR042185 |  |
| Pfam | PF00079 |  |

**Assessment**: 8 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| BRD7 | two hybrid pooling approach | 16169070 | physical association | — |
| CRMP1 | two hybrid pooling approach | 16169070 | physical association | — |
| EEF1A1 | two hybrid pooling approach | 16169070 | physical association | — |
| MED31 | two hybrid pooling approach | 16169070 | physical association | Yes |
| RBM48 | two hybrid pooling approach | 16169070 | physical association | — |
| GAPDH | two hybrid pooling approach | 16169070 | physical association | — |
| RIF1 | two hybrid pooling approach | 16169070 | physical association | Yes |
| TLE1 | two hybrid pooling approach | 16169070 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| GZMB | 0.958 | 0.294 | — |
| CTSG | 0.920 | 0.045 | — |
| CASP1 | 0.792 | 0.292 | — |
| PRF1 | 0.682 | 0.051 | — |
| PIGM | 0.676 | 0.000 | — |
| CASP8 | 0.523 | 0.292 | — |
| TIMD4 | 0.499 | 0.472 | — |
| ST3GAL3 | 0.492 | 0.482 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IDA:UniProtKB)
- cytosol (IDA:UniProtKB)
- extracellular exosome (HDA:UniProtKB)
- extracellular matrix (HDA:BHF-UCL)
- extracellular space (IDA:UniProtKB)
- Golgi apparatus (IDA:HPA)
- membrane (HDA:UniProtKB)
- nucleoplasm (IDA:HPA)

**PPI Assessment**: Physical interactions (IntAct) + 3 chromatin-regulatory partners; high regulatory relevance

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

**Normalized Score**: 76.8/100 (Raw: 140.5/183)

**Strengths**:
1. Moderate research novelty (52 publications)
1. Good 3D structural quality (mean pLDDT 91.2)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 6/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 76.8/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P50453
- HPA: https://www.proteinatlas.org/ENSG00000170542-SERPINB9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERPINB9%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
