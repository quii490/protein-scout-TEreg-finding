---
type: protein-evaluation
gene: "CNOT7"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## CNOT7 (CCR4-NOT transcription complex subunit 7) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9UIV1 |
| **Protein Name** | CCR4-NOT transcription complex subunit 7 |
| **Aliases** | CAF1 |
| **Length** | 285 aa |
| **Mass** | 32.7 kDa |
| **AlphaFold mean pLDDT** | 90.7 |
| **AlphaFold pLDDT >90** | 85.3% |
| **AlphaFold pLDDT <50** | 9.1% |
| **PubMed (strict)** | 74 |
| **Function** | Has 3'-5' poly(A) exoribonuclease activity for synthetic poly(A) RNA substrate (PubMed:19276069, PubMed:20634287, PubMed:31439799). Its function seems to be partially redundant with that of CNOT8 (PubMed:19605561). Catalytic component of the CCR4-NOT complex which is one of the major cellular mRNA d |

### 2. 核定位证据

#### UniProt Subcellular Location
Nucleus; Cytoplasm, P-body; Cytoplasm, Cytoplasmic ribonucleoprotein granule

#### GO Cellular Component
- **CCR4-NOT complex** (IDA:UniProtKB)
- **CCR4-NOT core complex** (IBA:GO_Central)
- **cytoplasm** (IDA:UniProt)
- **cytosol** (TAS:Reactome)
- **membrane** (HDA:UniProtKB)
- **nuclear body** (IDA:HPA)
- **nuclear speck** (IMP:UniProtKB)
- **nucleus** (IDA:UniProtKB)

#### HPA Subcellular Localization
- **Main location**: Nuclear bodies
- **Additional locations**: Nucleoplasm
- **Reliability (IF)**: Supported
- **IF Display Images Available**: NO

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 74 |

**Key Papers:**
- PMID:40792674 -- Functional Proximity across an mRNA. (Biochemistry, 2025 Sep 16)
- PMID:36112698 -- MEX3C-Mediated Decay of SOCS3 mRNA Promotes JAK2/STAT3 Signaling to Facilitate Metastasis in Hepatocellular Carcinoma. (Cancer research, 2022 Nov 15)
- PMID:35248544 -- CNOT7 Outcompetes Its Paralog CNOT8 for Integration into The CCR4-NOT Complex. (Journal of molecular biology, 2022 May 15)
- PMID:39699231 -- The Legionella pneumophila effector PieF modulates mRNA stability through association with eukaryotic CCR4-NOT. (mSphere, 2025 Jan 28)
- PMID:38985240 -- Oncogenic Gene CNOT7 Promotes Progression and Induces Poor Prognosis of Glioma. (Molecular biotechnology, 2025 Jul)


**Research Volume Assessment**: 中等（<100篇），已有一定研究基础但仍存在未探索的niche

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 90.7
- pLDDT >90: 85.3%, 70-90: 3.5%, 50-70: 2.1%, <50: 9.1%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 2D5R | X-ray | 2.50 A | A=11-262 |
| 4GMJ | X-ray | 2.70 A | B/D/F=1-285 |
| 7AX1 | X-ray | 3.30 A | B=2-285 |
| 7VOI | X-ray | 4.38 A | B=1-285 |
| 9E7T | EM | 2.80 A | C=1-285 |

**Structure Assessment**: PDB实验结构（5个条目）+ AlphaFold高质量预测，结构可信度极高

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR039637 |  |
| IPR006941 |  |
| IPR012337 |  |
| IPR036397 |  |

| Pfam | Description |
|------|-------------|
| PF04857 |  |

**Domain Assessment**: 结构域注释有限，但AlphaFold预测有可辨识折叠域

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CNOT6L | 0.999 | 0.994 | -- |
| CNOT9 | 0.999 | 0.981 | -- |
| TOB1 | 0.999 | 0.989 | -- |
| CNOT3 | 0.999 | 0.978 | -- |
| CNOT6 | 0.999 | 0.994 | -- |
| CNOT2 | 0.999 | 0.967 | -- |
| CNOT1 | 0.999 | 0.998 | -- |
| CNOT10 | 0.999 | 0.837 | -- |
| CNOT4 | 0.998 | 0.902 | -- |
| PATL1 | 0.998 | 0.998 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-1 | psi-mi:"MI:0407"(direct intera | -- |
| Cnot3 | psi-mi:"MI:0676"(tandem affinity purific | imex:IM-11719|pubmed:2036 | psi-mi:"MI:0915"(physical asso | -- |
| Rc3h1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23663784|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| Rc3h2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23663784|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| TOB2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23340509|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| Pop2 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:2529 | psi-mi:"MI:0914"(association) | -- |
| ANXA2R | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:31527615|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- AGO2 (2 experiments)
- BTG1 (4 experiments)
- BTG2 (8 experiments)
- CNOT1 (8 experiments)
- CNOT11 (5 experiments)
- CNOT6 (5 experiments)
- CNOT6L (10 experiments)
- HTT (13 experiments)
- PATL1 (5 experiments)
- TCP11L1 (3 experiments)

**PPI Assessment**: PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 7/10 | x4 | 28 | 主要核定位，部分胞质信号 |
| 蛋白大小 | 10/10 | x1 | 10 | 中等大小（285 aa），生化实验操作便利 |
| 研究新颖性 | 6/10 | x5 | 30 | 有一定研究（PubMed=74篇），但核功能可能未被充分探索 |
| 三维结构 | 10/10 | x3 | 30 | 高质量预测（pLDDT 90.7），85%高置信度，9%无序 |
| 调控结构域 | 6/10 | x2 | 12 | 结构域注释有限，但AlphaFold预测有可辨识折叠域 |
| PPI 网络 | 3/10 | x3 | 9 | PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白 |
| **加权总分** | | | **122.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 9. Final Decision

**SCORED: 66.7/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 74 篇，有一定研究空间
- 中等大小（285 aa），生化实验操作便利
- 结构数据充分（PDB实验结构+AlphaFold）

**Weaknesses:**
- 核定位需HPA进一步确认
- 结构域注释有限
- PPI网络稀薄

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UIV1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CNOT7%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UIV1
- STRING: https://string-db.org/cgi/network?identifiers=CNOT7&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CNOT7

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000198791-CNOT7/subcellular

![](https://images.proteinatlas.org/69543/1304_A12_4_red_green.jpg)
![](https://images.proteinatlas.org/69543/1304_A12_6_red_green.jpg)
![](https://images.proteinatlas.org/69543/1323_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/69543/1323_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/69543/1418_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/69543/1418_C10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UIV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UIV1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039637;IPR006941;IPR012337;IPR036397; |
| Pfam | PF04857; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198791-CNOT7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGO2 | Intact, Biogrid | true |
| BTG1 | Intact, Biogrid | true |
| BTG2 | Intact, Biogrid | true |
| CAPZB | Biogrid, Opencell | true |
| CNOT1 | Intact, Biogrid | true |
| CNOT11 | Intact, Biogrid, Bioplex | true |
| CNOT2 | Intact, Biogrid | true |
| CNOT3 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
