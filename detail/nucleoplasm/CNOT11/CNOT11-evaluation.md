---
type: protein-evaluation
gene: "CNOT11"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 8
---

## CNOT11 (CCR4-NOT transcription complex subunit 11) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9UKZ1 |
| **Protein Name** | CCR4-NOT transcription complex subunit 11 |
| **Aliases** | C2orf29 |
| **Length** | 510 aa |
| **Mass** | 55.2 kDa |
| **AlphaFold mean pLDDT** | 76.8 |
| **AlphaFold pLDDT >90** | 39.6% |
| **AlphaFold pLDDT <50** | 16.1% |
| **PubMed (strict)** | 7 |
| **Function** | Component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional com |

### 2. 核定位证据

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **CCR4-NOT complex** (IDA:UniProtKB)
- **cytosol** (TAS:Reactome)
- **nucleus** (IEA:UniProtKB-SubCell)

#### HPA Subcellular Localization
- **Main location**: Nucleoplasm
- **Additional locations**: 无
- **Reliability (IF)**: Approved
- **IF Display Images Available**: NO

HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 3. HPA Immunofluorescence

暂无数据（Pending cell analysis），核定位基于 UniProt + GO + HPA 注释。

HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 7 |

**Key Papers:**
- PMID:37295431 -- Mechanism of ribosome-associated mRNA degradation during tubulin autoregulation. (Molecular cell, 2023 Jul 6)
- PMID:36586408 -- The human CNOT1-CNOT10-CNOT11 complex forms a structural platform for protein-protein interactions. (Cell reports, 2023 Jan 31)
- PMID:23232451 -- C2ORF29/CNOT11 and CNOT10 form a new module of the CCR4-NOT complex. (RNA biology, 2013 Feb)
- PMID:35882953 -- Reference gene selection in bovine caruncular epithelial cells under pregnancy-associated hormones exposure. (Scientific reports, 2022 Jul 26)
- PMID:32815612 -- Identification of reliable reference genes for expression studies in maternal reproductive tissues and foetal tissues of (Reproduction in domestic animals = Zuchthygiene, 2020 Nov)


**Research Volume Assessment**: 非常低（<10篇），几乎未被研究，是探索新型核蛋白功能的绝佳候选

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 76.8
- pLDDT >90: 39.6%, 70-90: 32.5%, 50-70: 11.8%, <50: 16.1%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 8BFH | X-ray | 2.20 A | A=323-497 |
| 8BFI | X-ray | 3.00 A | C=61-510 |
| 8BFJ | X-ray | 2.23 A | A=323-497 |
| 8FY3 | EM | 2.88 A | C=256-498 |

**Structure Assessment**: AlphaFold高质量预测（pLDDT 76.8），折叠域置信度高，PDB 4个条目验证

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR019312 |  |

| Pfam | Description |
|------|-------------|
| PF10155 |  |

**Domain Assessment**: 结构域注释有限，但AlphaFold预测有可辨识折叠域

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| CNOT9 | 0.999 | 0.807 | -- |
| CNOT3 | 0.999 | 0.779 | -- |
| CNOT2 | 0.999 | 0.837 | -- |
| CNOT10 | 0.999 | 0.991 | -- |
| CNOT1 | 0.999 | 0.993 | -- |
| CNOT6 | 0.998 | 0.792 | -- |
| CNOT6L | 0.997 | 0.83 | -- |
| CNOT7 | 0.997 | 0.848 | -- |
| CNOT8 | 0.995 | 0.78 | -- |
| TNKS1BP1 | 0.994 | 0.828 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| MYC | psi-mi:"MI:0676"(tandem affinity purific | pubmed:21150319|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| Cnot3 | psi-mi:"MI:0676"(tandem affinity purific | imex:IM-11719|pubmed:2036 | psi-mi:"MI:0915"(physical asso | -- |
| rsgA | psi-mi:"MI:0398"(two hybrid pooling appr | imex:IM-13779|pubmed:2071 | psi-mi:"MI:0915"(physical asso | -- |
| Rc3h1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23663784|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| Rc3h2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:23663784|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| NLK | psi-mi:"MI:0676"(tandem affinity purific | pubmed:23602568|imex:IM-1 | psi-mi:"MI:0914"(association) | -- |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purific | pubmed:31527615|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |

#### UniProt Interactions
- C2CD6 (3 experiments)
- CNOT1 (7 experiments)
- CNOT10 (7 experiments)
- CNOT2 (5 experiments)
- CNOT6 (4 experiments)
- CNOT6L (4 experiments)
- CNOT7 (5 experiments)
- CNOT9 (5 experiments)
- FAM193B (3 experiments)
- GPBP1L1 (7 experiments)

**PPI Assessment**: PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 8/10 | x4 | 32 | 明确核定位，多库交叉验证一致 |
| 蛋白大小 | 10/10 | x1 | 10 | 中等大小（510 aa），生化实验操作便利 |
| 研究新颖性 | 10/10 | x5 | 50 | 极度新颖（PubMed=7篇），几乎未被研究，探索空间巨大 |
| 三维结构 | 9/10 | x3 | 27 | 良好质量（pLDDT 76.8），39%高置信度，16%无序 |
| 调控结构域 | 6/10 | x2 | 12 | 结构域注释有限，但AlphaFold预测有可辨识折叠域 |
| PPI 网络 | 3/10 | x3 | 9 | PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白 |
| **加权总分** | | | **143.0/180** | |
| **归一化总分** | | | **78.1/100** | |

### 9. Final Decision

**SCORED: 78.1/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 7 篇，研究新颖性极高
- 中等大小（510 aa），生化实验操作便利
- 结构数据充分（PDB实验结构+AlphaFold）

**Weaknesses:**
- 核定位需HPA进一步确认
- 结构域注释有限
- PPI网络稀薄

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKZ1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CNOT11%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKZ1
- STRING: https://string-db.org/cgi/network?identifiers=CNOT11&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CNOT11
