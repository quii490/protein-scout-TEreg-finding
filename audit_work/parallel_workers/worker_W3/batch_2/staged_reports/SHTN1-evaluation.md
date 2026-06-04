---
type: protein-evaluation
gene: "SHTN1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHTN1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHTN1 / KIAA1598 |
| Protein Name | Shootin-1 |
| Protein Size | 631 aa / 71.6 kDa |
| UniProt ID | A0MZ66 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | HPA Approved nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus |
| Protein Size | 10/10 | x1 | **10** | 631 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 11 publications; extremely novel (≤20) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate quality (pLDDT=70.8); no PDB |
| Regulatory Domains | 7/10 | x2 | **14** | 1 annotated domain; novel protein baseline. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (12 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **137/183** | |
| **Normalized Total** | | | **74.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Perikaryon | ECO:0000250 |
| UniProt | Cell projection, axon | ECO:0000250 |
| UniProt | Cell projection, growth cone | ECO:0000250 |
| UniProt | Cytoplasm, cytoskeleton | ECO:0000250 |
| UniProt | Cell projection, filopodium | ECO:0000250 |
| UniProt | Cell projection, lamellipodium | ECO:0000250 |
| GO-CC | perinuclear region of cytoplasm | ISS:UniProtKB |
| HPA | Nucleoplasm, Plasma membrane, Centrosome, Basal body, Cytosol | Approved |

**Assessment**: HPA Approved nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus


### 4. Protein Size Assessment

631 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 11 |
| PubMed symbol-only count | 19 |
| PubMed broad count | 30 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Zhang K et al. (2024). "Shootin1 Regulates Retinal Ganglion Cell Neurite Development: Insights From an RGC Direct Somatic Cell Reprogramming Model.". *Investigative ophthalmology & visual science*. PMID: 38935030
2. Ergin V et al. (2025). "Exploring Shootin1's oncogenic role within FGFR2 gene fusions.". *Turkish journal of biology = Turk biyoloji dergisi*. PMID: 41496852
3. InanlooRahatloo K et al. (2019). "Whole-Transcriptome Analysis Reveals Dysregulation of Actin-Cytoskeleton Pathway in Intellectual Disability Patients.". *Neuroscience*. PMID: 30742961
4. Wang Y et al. (2024). "Data-mining-based biomarker evaluation and experimental validation of SHTN1 for bladder cancer.". *Cancer genetics*. PMID: 39260052
5. Zhang M et al. (2019). "Axonogenesis Is Coordinated by Neuron-Specific Alternative Splicing Programming and Splicing Regulator PTBP2.". *Neuron*. PMID: 30733148

**Assessment**: 11 publications; extremely novel (≤20)


**Function Summary**: Involved in the generation of internal asymmetric signals required for neuronal polarization and neurite outgrowth. Mediates netrin-1-induced F-actin-substrate coupling or 'clutch engagement' within the axon growth cone through activation of CDC42, RAC1 and PAK1-dependent signaling pathway, thereby converting the F-actin retrograde flow into traction forces, concomitantly with filopodium extension and axon outgrowth. Plays a role in cytoskeletal organization by regulating the subcellular localization of phosphoinositide 3-kinase (PI3K) activity at the axonal growth cone. Also plays a role in r

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 70.8 |
| pLDDT > 90 (high confidence) | 39.9% |
| pLDDT 70-90 (moderate) | 15.4% |
| pLDDT 50-70 (low) | 11.3% |
| pLDDT < 50 (disordered) | 33.4% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold moderate quality (pLDDT=70.8); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR024849 |  |

**Assessment**: 1 annotated domain; novel protein baseline.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| ENSP00000376636.3 | two hybrid array | 32296183 | physical association | — |
| ENSP00000347532.4 | two hybrid array | 25416956 | physical association | — |
| MEGF10 | two hybrid | unassigned5 | physical association | — |
| YWHAG | anti bait coimmunoprecipitation | 17353931 | physical association | — |
| IKBKG | protein array | 20098747 | direct interaction | — |
| ARL6IP5 | cross-linking study | 30021884 | physical association | — |
| PRAF2 | cross-linking study | 30021884 | physical association | — |
| DISC1 | two hybrid fragment pooling approach | 31413325 | physical association | — |
| ... (4 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| L1CAM | 0.980 | 0.051 | — |
| RUFY3 | 0.966 | 0.000 | — |
| LNX1 | 0.760 | 0.532 | — |
| HCLS1 | 0.649 | 0.098 | — |
| CTTN | 0.641 | 0.098 | — |
| AHCYL1 | 0.604 | 0.225 | — |
| TACC3 | 0.596 | 0.098 | — |
| BICC1 | 0.588 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- axon (ISS:UniProtKB)
- axonal growth cone (ISS:UniProtKB)
- cell leading edge (ISS:UniProtKB)
- cytoplasm (IDA:BHF-UCL)
- filopodium (ISS:UniProtKB)
- growth cone (ISS:UniProtKB)
- lamellipodium (ISS:UniProtKB)
- microtubule (IDA:MGI)

**PPI Assessment**: Physical interactions present (12 partners) but no chromatin regulatory partners

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

**Normalized Score**: 74.9/100 (Raw: 137/183)

**Strengths**:
1. Excellent research novelty (11 publications)
1. Good 3D structural quality (mean pLDDT 70.8)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 6/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 74.9/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/A0MZ66
- HPA: https://www.proteinatlas.org/ENSG00000187164-SHTN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHTN1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
