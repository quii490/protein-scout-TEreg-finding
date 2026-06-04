---
type: protein-evaluation
gene: "SERTAD2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD2 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERTAD2 / KIAA0127, TRIPBR2 |
| Protein Name | SERTA domain-containing protein 2 |
| Protein Size | 314 aa / 33.9 kDa |
| UniProt ID | Q14140 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Supported + UniProt Nucleus; primarily nuclear |
| Protein Size | 10/10 | x1 | **10** | 314 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 10 publications; extremely novel (≤20) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold low (pLDDT=59.8); largely disordered |
| Regulatory Domains | 10/10 | x2 | **20** | 3 domains; chromatin/DNA-related function. Direct regulatory potential. |
| PPI Network | 8/10 | x3 | **24** | Physical interactions (IntAct) + 2 chromatin-regulatory partner(s); regulatory relevance |
| Cross-Validation Bonus | — | max +3 | **+0.5** | HPA + UniProt nuclear localization agreement (+0.5) |
| **Raw Total** | | | **155.5/183** | |
| **Normalized Total** | | | **85.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Nucleus | ECO:0000269 |
| UniProt | Cytoplasm | ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:MGI |
| HPA | Nucleoplasm, Cytosol | Supported |

**Assessment**: HPA Supported + UniProt Nucleus; primarily nuclear


### 4. Protein Size Assessment

314 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 10 |
| PubMed symbol-only count | 17 |
| PubMed broad count | 23 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Zhang D et al. (2022). "Establishing and validating an ADCP-related prognostic signature in pancreatic ductal adenocarcinoma.". *Aging*. PMID: 35963640
2. Qian J et al. (2024). "Identification of a Novel 4-gene Prognostic Model Related to Neutrophil Extracellular Traps for Colorectal Cancer.". *The Turkish journal of gastroenterology : the official journal of Turkish Society of Gastroenterology*. PMID: 39549020
3. Zhang Z et al. (2020). "Long Noncoding RNA SERTAD2-3 Inhibits Osteosarcoma Proliferation and Migration by Competitively Binding miR-29c.". *Genetic testing and molecular biomarkers*. PMID: 31999493
4. Zhu L et al. (2023). "The diagnostic significance of the ZNF gene family in pancreatic cancer: a bioinformatics and experimental study.". *Frontiers in genetics*. PMID: 37396042
5. Ogunbawo AR et al. (2024). "Genetic Foundations of Nellore Traits: A Gene Prioritization and Functional Analyses of Genome-Wide Association Study Results.". *Genes*. PMID: 39336722

**Assessment**: 10 publications; extremely novel (≤20)


**Function Summary**: Acts at E2F-responsive promoters as coregulator to integrate signals provided by PHD- and/or bromodomain-containing transcription factors. May act as coactivator as well as corepressor of E2F1-TFDP1 and E2F4-TFDP1 complexes on E2F consensus binding sites, which would activate or inhibit E2F-target genes expression. Modulates fat storage by down-regulating the expression of key genes involved in adipocyte lipolysis, thermogenesis and oxidative metabolism

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 59.8 |
| pLDDT > 90 (high confidence) | 11.5% |
| pLDDT 70-90 (moderate) | 17.8% |
| pLDDT 50-70 (low) | 27.1% |
| pLDDT < 50 (disordered) | 43.6% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold low (pLDDT=59.8); largely disordered

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR052262 |  |
| InterPro | IPR009263 |  |
| Pfam | PF06031 |  |

**Assessment**: 3 domains; chromatin/DNA-related function. Direct regulatory potential.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| ENSP00000326933.3 | two hybrid pooling approach | 20711500 | physical association | — |
| IGFN1 | two hybrid array | 32296183 | physical association | — |
| PLA2G6 | two hybrid array | 32296183 | physical association | — |
| STRA8 | two hybrid array | 32296183 | physical association | — |
| TNS2 | two hybrid array | 32296183 | physical association | — |
| ZNF524 | two hybrid array | 32296183 | physical association | — |
| HELLS | validated two hybrid | 32296183 | physical association | Yes |
| PARVG | validated two hybrid | 32296183 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| SERTAD3 | 0.644 | 0.000 | — |
| XPO1 | 0.613 | 0.292 | — |
| SERTAD1 | 0.582 | 0.000 | — |
| E2F1 | 0.560 | 0.068 | — |
| PPP2R2A | 0.554 | 0.535 | — |
| SERTAD4 | 0.549 | 0.000 | — |
| PPP2R2C | 0.493 | 0.493 | — |
| PPP2R1B | 0.478 | 0.478 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IDA:MGI)
- cytosol (IDA:HPA)
- nucleoplasm (IDA:HPA)
- nucleus (IDA:MGI)

**PPI Assessment**: Physical interactions (IntAct) + 2 chromatin-regulatory partner(s); regulatory relevance

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 85.0/100 (Raw: 155.5/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Excellent research novelty (10 publications)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 85.0/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q14140
- HPA: https://www.proteinatlas.org/ENSG00000179833-SERTAD2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERTAD2%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
