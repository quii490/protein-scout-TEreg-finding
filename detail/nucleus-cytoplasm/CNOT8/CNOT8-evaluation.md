---
type: protein-evaluation
gene: "CNOT8"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 5
---

## CNOT8 (CCR4-NOT transcription complex subunit 8) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9UFF9 |
| **Protein Name** | CCR4-NOT transcription complex subunit 8 |
| **Aliases** | CALIF; POP2 |
| **Length** | 292 aa |
| **Mass** | 33.5 kDa |
| **AlphaFold mean pLDDT** | 90.0 |
| **AlphaFold pLDDT >90** | 82.2% |
| **AlphaFold pLDDT <50** | 6.5% |
| **PubMed (strict)** | 24 |
| **Function** | Has 3'-5' poly(A) exoribonuclease activity for synthetic poly(A) RNA substrate. Its function seems to be partially redundant with that of CNOT7. Catalytic component of the CCR4-NOT complex which is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, trans |

### 2. 核定位证据

#### UniProt Subcellular Location
Cytoplasm; Nucleus

#### GO Cellular Component
- **CCR4-NOT complex** (IDA:UniProtKB)
- **CCR4-NOT core complex** (IBA:GO_Central)
- **cytosol** (TAS:Reactome)
- **nucleus** (IDA:GO_Central)
- **P-body** (IBA:GO_Central)

#### HPA Subcellular Localization
- **Main location**: 无
- **Additional locations**: 无
- **Reliability (IF)**: None
- **IF Display Images Available**: NO

HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 3. HPA Immunofluorescence

暂无数据（Pending cell analysis），核定位基于 UniProt + GO + HPA 注释。

HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 24 |

**Key Papers:**
- PMID:35248544 -- CNOT7 Outcompetes Its Paralog CNOT8 for Integration into The CCR4-NOT Complex. (Journal of molecular biology, 2022 May 15)
- PMID:19605561 -- The Ccr4-NOT deadenylase subunits CNOT7 and CNOT8 have overlapping roles and modulate cell proliferation. (Molecular biology of the cell, 2009 Sep)
- PMID:35390160 -- Cnot8 eliminates naïve regulation networks and is essential for naïve-to-formative pluripotency transition. (Nucleic acids research, 2022 May 6)
- PMID:25408231 -- MEK1 is associated with carboplatin resistance and is a prognostic biomarker in epithelial ovarian cancer. (BMC cancer, 2014 Nov 18)
- PMID:37767629 -- The CCR4-NOT complex suppresses untimely translational activation of maternal mRNAs. (Development (Cambridge, England), 2023 Nov 1)


**Research Volume Assessment**: 较低（<50篇），研究空间充足

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 90.0
- pLDDT >90: 82.2%, 70-90: 4.8%, 50-70: 6.5%, <50: 6.5%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 9E7U | EM | 3.50 A | C=1-292 |

**Structure Assessment**: AlphaFold高质量预测（pLDDT 90.0），折叠域置信度高，PDB 1个条目验证

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
| CNOT9 | 0.999 | 0.862 | -- |
| CNOT6L | 0.999 | 0.921 | -- |
| CNOT1 | 0.999 | 0.962 | -- |
| CNOT3 | 0.999 | 0.956 | -- |
| CNOT6 | 0.999 | 0.766 | -- |
| CNOT2 | 0.999 | 0.936 | -- |
| CNOT4 | 0.998 | 0.882 | -- |
| PATL1 | 0.998 | 0.998 | -- |
| CNOT10 | 0.996 | 0.627 | -- |
| CNOT11 | 0.995 | 0.78 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| BTG1 | psi-mi:"MI:0398"(two hybrid pooling appr | pubmed:16189514|imex:IM-1 | psi-mi:"MI:0915"(physical asso | -- |
| CNOT10 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| OTUB1 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| MARCKS | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| CAPZA1 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| CNOT1 | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |
| - | psi-mi:"MI:0006"(anti bait coimmunopreci | pubmed:17353931 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- BTG1 (6 experiments)
- BTG1 (3 experiments)
- BTG2 (5 experiments)
- CAPZA1 (2 experiments)
- CNOT1 (7 experiments)
- CNOT10 (3 experiments)
- CNOT2 (3 experiments)
- CNOT3 (5 experiments)
- CNOT6 (2 experiments)
- CNOT6L (6 experiments)

**PPI Assessment**: PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 5/10 | x4 | 20 | 核-质分布，可能为穿梭蛋白 |
| 蛋白大小 | 10/10 | x1 | 10 | 中等大小（292 aa），生化实验操作便利 |
| 研究新颖性 | 8/10 | x5 | 40 | 非常新颖（PubMed=24篇），仅有少量基础研究 |
| 三维结构 | 8/10 | x3 | 24 | 高质量预测（pLDDT 90.0），82%高置信度，6%无序 |
| 调控结构域 | 6/10 | x2 | 12 | 结构域注释有限，但AlphaFold预测有可辨识折叠域 |
| PPI 网络 | 3/10 | x3 | 9 | PPI网络稀薄（15个STRING伙伴），可能为独立功能蛋白 |
| **加权总分** | | | **117.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 9. Final Decision

**SCORED: 63.9/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 24 篇，研究新颖性极高
- 中等大小（292 aa），生化实验操作便利
- 结构数据充分（PDB实验结构+AlphaFold）

**Weaknesses:**
- 核定位证据较弱，需HPA IF验证
- 结构域注释有限
- PPI网络稀薄

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UFF9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CNOT8%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UFF9
- STRING: https://string-db.org/cgi/network?identifiers=CNOT8&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CNOT8

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UFF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
