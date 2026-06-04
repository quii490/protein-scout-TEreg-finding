---
type: protein-evaluation
gene: "SGK2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGK2 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SGK2 / — |
| Protein Name | Serine/threonine-protein kinase Sgk2 |
| Protein Size | 367 aa / 41.2 kDa |
| UniProt ID | Q9HBY8 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Supported + UniProt Nucleus; primarily nuclear |
| Protein Size | 10/10 | x1 | **10** | 367 aa; ideal range |
| Research Novelty | 6/10 | x5 | **30** | 70 publications; moderate novelty (51-100) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold high quality (pLDDT=87.0); no PDB |
| Regulatory Domains | 8/10 | x2 | **16** | 8 annotated domains; some domain richness. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (4 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0.5** | HPA + UniProt nuclear localization agreement (+0.5) |
| **Raw Total** | | | **134.5/183** | |
| **Normalized Total** | | | **73.5/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Nucleus | ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm | Supported |

**Assessment**: HPA Supported + UniProt Nucleus; primarily nuclear


### 4. Protein Size Assessment

367 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 70 |
| PubMed symbol-only count | 94 |
| PubMed broad count | 97 |
| Novelty category | 51-100 → 6 |

**Key Publications**:
1. Tang W et al. (2023). "Targeting Kindlin-2 in adipocytes increases bone mass through inhibiting FAS/PPARγ/FABP4 signaling in mice.". *Acta pharmaceutica Sinica. B*. PMID: 37969743
2. Baldwin A et al. (2010). "Kinase requirements in human cells: V. Synthetic lethal interactions between p53 and the protein kinases SGK2 and PAK3.". *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 20616055
3. Zhou N et al. (2015). "Lethality of PAK3 and SGK2 shRNAs to human papillomavirus positive cervical cancer cells is independent of PAK3 and SGK2 knockdown.". *PloS one*. PMID: 25615606
4. Liu Y et al. (2019). "SGK2 promotes renal cancer progression via enhancing ERK 1/2 and AKT phosphorylation.". *European review for medical and pharmacological sciences*. PMID: 31002126
5. Lang F et al. (2001). "Regulation and physiological roles of serum- and glucocorticoid-induced protein kinase isoforms.". *Science's STKE : signal transduction knowledge environment*. PMID: 11707620

**Assessment**: 70 publications; moderate novelty (51-100)


**Function Summary**: Serine/threonine-protein kinase which is involved in the regulation of a wide variety of ion channels, membrane transporters, cell growth, survival and proliferation. Up-regulates Na(+) channels: SCNN1A/ENAC, K(+) channels: KCNA3/Kv1.3, KCNE1 and KCNQ1, amino acid transporter: SLC6A19, glutamate transporter: SLC1A6/EAAT4, glutamate receptors: GRIA1/GLUR1 and GRIK2/GLUR6, Na(+)/H(+) exchanger: SLC9A3/NHE3, and the Na(+)/K(+) ATPase

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 87.0 |
| pLDDT > 90 (high confidence) | 69.2% |
| pLDDT 70-90 (moderate) | 16.6% |
| pLDDT 50-70 (low) | 4.4% |
| pLDDT < 50 (disordered) | 9.8% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold high quality (pLDDT=87.0); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR000961 |  |
| InterPro | IPR011009 |  |
| InterPro | IPR017892 |  |
| InterPro | IPR000719 |  |
| InterPro | IPR017441 |  |
| InterPro | IPR008271 |  |
| Pfam | PF00069 |  |
| Pfam | PF00433 |  |

**Assessment**: 8 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| IL3RA | two hybrid array | 21988832 | physical association | — |
| HSP90AB1 | luminescence based mammalian interactome mapping | 22939624 | physical association | — |
| PMM2 | two hybrid array | 32296183 | physical association | — |
| HIRIP3 | two hybrid array | 32296183 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| PDPK1 | 0.954 | 0.454 | — |
| SGK3 | 0.934 | 0.329 | — |
| FOXO1 | 0.932 | 0.125 | — |
| FOXO3 | 0.930 | 0.125 | — |
| FOXO4 | 0.923 | 0.125 | — |
| SGK1 | 0.904 | 0.000 | — |
| NEDD4L | 0.677 | 0.092 | — |
| HSP90AB1 | 0.672 | 0.621 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytosol (TAS:Reactome)
- nucleoplasm (IDA:HPA)

**PPI Assessment**: Physical interactions present (4 partners) but no chromatin regulatory partners

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

**Normalized Score**: 73.5/100 (Raw: 134.5/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Moderate research novelty (70 publications)
1. Good 3D structural quality (mean pLDDT 87.0)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 73.5/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBY8
- HPA: https://www.proteinatlas.org/ENSG00000101049-SGK2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SGK2%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
