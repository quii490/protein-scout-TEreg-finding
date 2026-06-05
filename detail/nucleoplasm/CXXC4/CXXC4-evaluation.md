---
type: protein-evaluation
gene: "CXXC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 8
---

## CXXC4 (CXXC-type zinc finger protein 4) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | Q9H2H0 |
| **Protein Name** | CXXC-type zinc finger protein 4 |
| **Aliases** | IDAX |
| **Length** | 198 aa |
| **Mass** | 21.0 kDa |
| **AlphaFold mean pLDDT** | 63.5 |
| **AlphaFold pLDDT >90** | 19.7% |
| **AlphaFold pLDDT <50** | 25.8% |
| **PubMed (strict)** | 41 |
| **Function** | Acts as a negative regulator of the Wnt signaling pathway via its interaction with DVL1 (By similarity). Binds preferentially to DNA containing cytidine-phosphate-guanosine (CpG) dinucleotides over CpH (H=A, T, and C), hemimethylated-CpG and hemimethylated-hydroxymethyl-CpG (PubMed:29276034) |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm

#### GO Cellular Component
- **cytoplasm** (IDA:BHF-UCL)
- **cytoplasmic vesicle** (IDA:BHF-UCL)
- **nucleus** (IBA:GO_Central)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Golgi apparatus
- **Reliability (IF)**: Approved
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 41 |

**Key Papers:**
- PMID:32280999 -- CXXC4 mediates glucose-induced β-cell proliferation. (Acta diabetologica, 2020 Sep)
- PMID:34076982 -- SPZ1 promotes glioma aggravation via targeting CXXC4. (Journal of B.U.ON. : official journal of the Balkan Union of Oncology, 2021 Mar-Apr)
- PMID:15375572 -- Identification and characterization of human CXXC10 gene in silico. (International journal of oncology, 2004 Oct)
- PMID:25085016 -- CXXC4 mRNA levels are associated with clinicopathological parameters and survival of myelodysplastic syndrome patients. (Leukemia research, 2014 Sep)
- PMID:25064842 -- New tumor suppressor CXXC finger protein 4 inactivates mitogen activated protein kinase signaling. (FEBS letters, 2014 Sep 17)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 63.5
- pLDDT >90: 19.7%, 70-90: 9.1%, 50-70: 45.5%, <50: 25.8%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 5VC9 | X-ray | 2.10 A | C/F=133-180 |

**Structure Assessment**: AlphaFold low confidence (pLDDT 63.5), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR040388 |  |
| IPR002857 |  |

| Pfam | Description |
|------|-------------|
| PF02008 |  |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| DVL1 | 0.983 | 0.095 | -- |
| TET2 | 0.923 | 0.0 | -- |
| DVL3 | 0.921 | 0.091 | -- |
| DVL2 | 0.915 | 0.091 | -- |
| AXIN1 | 0.62 | 0.0 | -- |
| FOXL2 | 0.611 | 0.292 | -- |
| OGT | 0.588 | 0.047 | -- |
| TCF7L2 | 0.567 | 0.0 | -- |
| WT1 | 0.561 | 0.049 | -- |
| WNT3A | 0.545 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| ESR1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:31527615|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| ZNFX1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:26496610|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| TIA1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:26496610|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| RAD51 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:26496610|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| GPN3 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:26496610|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| PUS7 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:26496610|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| BRD9 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:26496610|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| RCVRN | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- No UniProt interaction annotations

**PPI Assessment**: Sparse PPI network (15 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 8/10 | x4 | 32 | Clear nuclear localization, multi-db cross-validated |
| Protein Size | 8/10 | x1 | 8 | Small (198 aa), suitable for structural studies |
| Research Novelty | 8/10 | x5 | 40 | Very novel (PubMed=41 papers), only limited foundational research |
| 3D Structure | 6/10 | x3 | 18 | Moderate quality (pLDDT 63.5), 19% high confidence, 25% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (15 STRING partners), possibly independen |
| **Weighted Total** | | | **116.5/180** | |
| **Normalized Total** | | | **63.7/100** | |

### 9. Final Decision

**SCORED: 63.7/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 41 papers, Extremely high research novelty
- Small (198 aa), suitable for structural studies
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2H0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CXXC4%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2H0
- STRING: https://string-db.org/cgi/network?identifiers=CXXC4&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CXXC4

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000168772-CXXC4/subcellular

![](https://images.proteinatlas.org/36925/1337_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/36925/1337_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/36925/1338_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/36925/1338_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/36925/1652_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/36925/1652_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
