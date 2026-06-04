---
type: protein-evaluation
gene: "SIVA1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SIVA1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SIVA1 / SIVA |
| Protein Name | Apoptosis regulatory protein Siva |
| Protein Size | 175 aa / 18.7 kDa |
| UniProt ID | O15304 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 10/10 | x4 | **40** | HPA Enhanced + UniProt Nucleus; primarily nuclear |
| Protein Size | 8/10 | x1 | **8** | 175 aa; acceptable range |
| Research Novelty | 6/10 | x5 | **30** | 67 publications; moderate novelty (51-100) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate quality (pLDDT=75.9); no PDB |
| Regulatory Domains | 7/10 | x2 | **14** | 2 domains; novel protein baseline, possible uncharacterized domains. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (15 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+1.0** | HPA + UniProt nuclear localization agreement (+0.5) | IntAct + STRING overlap (2 shared partners) (+0.5) |
| **Raw Total** | | | **132.0/183** | |
| **Normalized Total** | | | **72.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Nucleus | ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HGNC-UCL |
| HPA | Nucleoplasm | Enhanced |

**Assessment**: HPA Enhanced + UniProt Nucleus; primarily nuclear


### 4. Protein Size Assessment

175 aa; acceptable range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 67 |
| PubMed symbol-only count | 82 |
| PubMed broad count | 98 |
| Novelty category | 51-100 → 6 |

**Key Publications**:
1. Resch U et al. (2009). "Siva1 is a XIAP-interacting protein that balances NFkappaB and JNK signalling to promote apoptosis.". *Journal of cell science*. PMID: 19584092
2. Parducci NS et al. (2025). "Exploring the dual role of SIVA1 in cancer biology.". *Gene*. PMID: 40024298
3. Chen GH et al. (2015). "Anticancer activity of recombinant Siva1 protein in human nasopharyngeal carcinoma cell line CNE-2.". *Cancer biomarkers : section A of Disease markers*. PMID: 26406409
4. Li N et al. (2011). "Siva1 suppresses epithelial-mesenchymal transition and metastasis of tumor cells by inhibiting stathmin and stabilizing microtubules.". *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 21768358
5. Palrasu M et al. (2022). "Helicobacter pylori pathogen inhibits cellular responses to oncogenic stress and apoptosis.". *PLoS pathogens*. PMID: 35767594

**Assessment**: 67 publications; moderate novelty (51-100)


**Function Summary**: Induces CD27-mediated apoptosis. Inhibits BCL2L1 isoform Bcl-x(L) anti-apoptotic activity. Inhibits activation of NF-kappa-B and promotes T-cell receptor-mediated apoptosis

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 75.9 |
| pLDDT > 90 (high confidence) | 19.4% |
| pLDDT 70-90 (moderate) | 49.7% |
| pLDDT 50-70 (low) | 19.4% |
| pLDDT < 50 (disordered) | 11.4% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold moderate quality (pLDDT=75.9); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR022773 |  |
| Pfam | PF05458 |  |

**Assessment**: 2 domains; novel protein baseline, possible uncharacterized domains.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| CD27 | two hybrid | 9177220 | physical association | — |
| MYZAP | two hybrid pooling approach | 16169070 | physical association | — |
| BEX3 | two hybrid | 21988832 | physical association | — |
| PCNA | two hybrid | 21988832 | physical association | — |
| erpA | two hybrid pooling approach | 20711500 | physical association | — |
| pyrE | two hybrid pooling approach | 20711500 | physical association | — |
| NTAQ1 | two hybrid array | 32296183 | physical association | — |
| C2orf68 | two hybrid array | 32296183 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| BCL2L1 | 0.990 | 0.516 | — |
| CD27 | 0.972 | 0.474 | — |
| BCL2 | 0.938 | 0.294 | — |
| RAD18 | 0.783 | 0.619 | — |
| PCNA | 0.740 | 0.733 | — |
| TNFRSF18 | 0.730 | 0.301 | — |
| XIAP | 0.700 | 0.625 | — |
| STMN1 | 0.687 | 0.510 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IDA:HGNC-UCL)
- mitochondrion (IDA:HGNC-UCL)
- nucleoplasm (IDA:HGNC-UCL)

**PPI Assessment**: Physical interactions present (15 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- IntAct + STRING overlap (2 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 72.1/100 (Raw: 132.0/183)

**Strengths**:
1. Strong nuclear localization (score 10/10)
1. Moderate research novelty (67 publications)
1. Good 3D structural quality (mean pLDDT 75.9)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 72.1/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O15304
- HPA: https://www.proteinatlas.org/ENSG00000184990-SIVA1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SIVA1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
