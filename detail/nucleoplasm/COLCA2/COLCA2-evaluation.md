---
type: protein-evaluation
gene: "COLCA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## COLCA2 (POU class 2 homeobox associating factor 3) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | A8K830 |
| **Protein Name** | POU class 2 homeobox associating factor 3 |
| **Aliases** | C11orf93; CASC13; COLCA2 |
| **Length** | 251 aa |
| **Mass** | 27.4 kDa |
| **AlphaFold mean pLDDT** | 55.5 |
| **AlphaFold pLDDT >90** | 8.8% |
| **AlphaFold pLDDT <50** | 47.4% |
| **PubMed (strict)** | 11 |
| **Function** | Transcriptional coactivator that specifically associates with POU2F3 (PubMed:35576971). This complex drives the development of tuft cells, a rare a rare chemosensory cells that coordinate immune and neural functions within mucosal epithelial tissues (PubMed:35576971) |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **cytoplasm** (IDA:UniProtKB)
- **cytosol** (IDA:HPA)
- **nucleoplasm** (IDA:HPA)
- **nucleus** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: Cytosol
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 11 |

**Key Papers:**
- PMID:37742928 -- EWSR1::POU2AF3(COLCA2) Sarcoma: An Aggressive, Polyphenotypic Sarcoma With a Head and Neck Predilection. (Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc, 2023 Dec)
- PMID:35576971 -- OCA-T1 and OCA-T2 are coactivators of POU2F3 in the tuft cell lineage. (Nature, 2022 Jul)
- PMID:35102554 -- Alcohol consumption, DNA methylation and colorectal cancer risk: Results from pooled cohort studies and Mendelian random (International journal of cancer, 2022 Jul 1)
- PMID:33633225 -- rs1944919 on chromosome 11q23.1 and its effector genes COLCA1/COLCA2 confer susceptibility to primary biliary cholangiti (Scientific reports, 2021 Feb 25)
- PMID:36580038 -- Recurrent EWSR1::COLCA2 Fusions Define a Novel Sarcoma With Spindle/Round Cell Morphology and Strong Predilection for th (The American journal of surgical pathology, 2023 Mar 1)


**Research Volume Assessment**: Low (<50 papers), ample research space

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 55.5
- pLDDT >90: 8.8%, 70-90: 6.0%, 50-70: 37.8%, <50: 47.4%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| None | -- | -- | -- |

**Structure Assessment**: AlphaFold low confidence (pLDDT 55.5), normal for novel proteins

PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR047571 |  |
| IPR043265 |  |

| Pfam | Description |
|------|-------------|
| None | None |

**Domain Assessment**: Sparse domain annotation, normal for novel proteins

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| C11orf53 | 0.914 | 0.0 | -- |
| RLF | 0.564 | 0.0 | -- |
| POU2AF1 | 0.499 | 0.0 | -- |
| WBP1L | 0.489 | 0.0 | -- |
| EIF3H | 0.474 | 0.0 | -- |
| C11orf87 | 0.468 | 0.0 | -- |
| HIGD1A | 0.455 | 0.0 | -- |
| SYCE3 | 0.415 | 0.0 | -- |
| DIP2B | 0.402 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|

#### UniProt Interactions
- No UniProt interaction annotations

**PPI Assessment**: Sparse PPI network (9 STRING partners), possibly independent function protein

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | 7/10 | x4 | 28 | Mainly nuclear localization, some cytoplasmic signal |
| Protein Size | 10/10 | x1 | 10 | Medium (251 aa), convenient for biochemical experiments |
| Research Novelty | 10/10 | x5 | 50 | Extremely novel (PubMed=11 papers), nearly unstudied, huge exploration space |
| 3D Structure | 6/10 | x3 | 18 | Moderate quality (pLDDT 55.5), 8% high confidence, 47% disordered |
| Regulatory Domains | 4/10 | x2 | 8 | Sparse domain annotation, normal for novel proteins |
| PPI Network | 3/10 | x3 | 9 | Sparse PPI network (9 STRING partners), possibly independent |
| **Weighted Total** | | | **123.5/180** | |
| **Normalized Total** | | | **67.5/100** | |

### 9. Final Decision

**SCORED: 67.5/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 11 papers, Extremely high research novelty
- Medium (251 aa), convenient for biochemical experiments
- AlphaFold structure usable

**Weaknesses:**
- Nuclear localization needs further HPA confirmation
- Limited domain annotation
- Sparse PPI network

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/A8K830
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22COLCA2%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K830
- STRING: https://string-db.org/cgi/network?identifiers=COLCA2&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/COLCA2

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000214290-POU2AF3/subcellular

![](https://images.proteinatlas.org/40625/1404_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40625/1404_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40625/502_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40625/502_H5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A8K830 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 5..27; /note="OCA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01347" |
| InterPro | IPR047571;IPR043265; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000214290-POU2AF3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
