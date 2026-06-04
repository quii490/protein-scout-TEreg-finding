---
type: protein-evaluation
gene: "SHISA6"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHISA6 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHISA6 / — |
| Protein Name | Protein shisa-6 |
| Protein Size | 500 aa / 55.8 kDa |
| UniProt ID | Q6ZSJ9 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 500 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 10 publications; extremely novel (≤20) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold low (pLDDT=55.4); largely disordered |
| Regulatory Domains | 7/10 | x2 | **14** | 3 domains; novel protein baseline, possible uncharacterized domains. |
| PPI Network | 8/10 | x3 | **24** | Physical interactions (IntAct) + 1 chromatin-regulatory partner(s); regulatory relevance |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **133/183** | |
| **Normalized Total** | | | **72.7/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Membrane | ECO:0000305 |
| UniProt | Postsynaptic density | ECO:0000250 |
| HPA | Nucleoplasm, Plasma membrane | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

500 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 10 |
| PubMed symbol-only count | 17 |
| PubMed broad count | 17 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Wu Z et al. (2023). "Epigenetic and Tumor Microenvironment for Prognosis of Patients with Gastric Cancer.". *Biomolecules*. PMID: 37238607
2. Choi MR et al. (2024). "Expression Profiling of Coding and Noncoding RNAs in the Endometrium of Patients with Endometriosis.". *International journal of molecular sciences*. PMID: 39408909
3. Peter S et al. (2020). "AMPAR Auxiliary Protein SHISA6 Facilitates Purkinje Cell Synaptic Excitability and Procedural Memory Formation.". *Cell reports*. PMID: 32294428
4. Kim HD et al. (2021). "Shisa6 mediates cell-type specific regulation of depression in the nucleus accumbens.". *Molecular psychiatry*. PMID: 34253865
5. Ramos J et al. (2023). "Genetic variants in the SHISA6 gene are associated with delayed cognitive impairment in two family datasets.". *Alzheimer's & dementia : the journal of the Alzheimer's Association*. PMID: 35490390

**Assessment**: 10 publications; extremely novel (≤20)


**Function Summary**: Involved in maintenance of high-frequency synaptic transmission at hippocampal CA3-CA1 synapses. Regulates AMPA-type glutamate receptor (AMPAR) immobilization at postsynaptic density keeping the channels in an activated state in the presence of glutamate and preventing synaptic depression. May play a role in self-renewal and differentiation of spermatogonial stem cells by inhibiting canonical Wnt signaling pathway

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 55.4 |
| pLDDT > 90 (high confidence) | 12.2% |
| pLDDT 70-90 (moderate) | 9.0% |
| pLDDT 50-70 (low) | 20.4% |
| pLDDT < 50 (disordered) | 58.4% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold low (pLDDT=55.4); largely disordered

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
| PLEKHG4 | two hybrid array | 32296183 | physical association | — |
| TSSK3 | two hybrid prey pooling approach | 32296183 | physical association | — |
| KIF9 | two hybrid prey pooling approach | 32296183 | physical association | — |
| ARMC7 | two hybrid array | 32296183 | physical association | — |
| FBLIM1 | two hybrid array | 32296183 | physical association | — |
| CCDC57 | two hybrid array | 32296183 | physical association | — |
| CARD9 | two hybrid array | 32296183 | physical association | — |
| UBASH3A | two hybrid array | 32296183 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| DLG4 | 0.801 | 0.000 | — |
| CNIH2 | 0.749 | 0.000 | — |
| CACNG8 | 0.739 | 0.000 | — |
| CACNG3 | 0.720 | 0.000 | — |
| CACNG2 | 0.700 | 0.000 | — |
| GRIN2B | 0.694 | 0.000 | — |
| GRIA2 | 0.688 | 0.087 | — |
| GRIA1 | 0.682 | 0.066 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- AMPA glutamate receptor complex (IBA:GO_Central)
- asymmetric, glutamatergic, excitatory synapse (ISS:UniProtKB)
- dendritic spine membrane (IBA:GO_Central)
- postsynaptic density (ISS:UniProtKB)
- postsynaptic density membrane (IEA:Ensembl)
- postsynaptic membrane (IBA:GO_Central)

**PPI Assessment**: Physical interactions (IntAct) + 1 chromatin-regulatory partner(s); regulatory relevance

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

**Normalized Score**: 72.7/100 (Raw: 133/183)

**Strengths**:
1. Excellent research novelty (10 publications)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 72.7/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZSJ9
- HPA: https://www.proteinatlas.org/ENSG00000188803-SHISA6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHISA6%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
