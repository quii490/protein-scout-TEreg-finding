---
type: protein-evaluation
gene: "CMYA5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMYA5 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMYA5 |
| 蛋白名称 | Cardiomyopathy-associated protein 5 |
| 蛋白大小 | 4069 aa / 449.2 kDa |
| UniProt ID | Q8N3K9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: Endoplasmic reticulum, Plasma membrane; UniProt: Nucleus; Sarcoplasmic reticulum; Cytoplasm; Cytoplasm, perin |
| 蛋白大小 | 0/10 | x1 | 0 | 4069 aa / 449.2 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 4/10 | x2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 24 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **72.0/180** | |
| **归一化总分** | | | **40.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Plasma membrane | Uncertain |
| UniProt | Nucleus; Sarcoplasmic reticulum; Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, myofibril, sar... | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 57 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Global landscape of alternative polyadenylation during the growth and development of skeletal muscle in pigs.. *BMC Genomics*. PMID: 42129632
2. Multi-omics investigation of perineural invasion in head and neck squamous cell carcinoma: neuroimmune mechanisms and clinical implications.. *Front Immunol*. PMID: 42206060
3. Genomic Evaluation of the Genetic Structure and Analysis of Selective Evolutionary Signatures of Xupu Goose.. *Biology (Basel)*. PMID: 41892239
4. Genome-Wide Association Study and Rare Variant Association Studies of Strabismus in the All of Us Research Program.. *Ophthalmol Sci*. PMID: 40837069
5. Direct Therapeutic Modulation of RYR2 Activity by CMYA5.. *Circulation*. PMID: 41115167

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTN | 0.000 | 0.000 | — |
| DTNBP1 | 0.000 | 0.000 | — |
| PRKAR2A | 0.000 | 0.000 | — |
| CAPN3 | 0.000 | 0.000 | — |
| ACTN2 | 0.000 | 0.000 | — |
| PRKAR1B | 0.000 | 0.000 | — |
| MYOZ2 | 0.000 | 0.000 | — |
| DTNA | 0.000 | 0.000 | — |
| ALMS1 | 0.000 | 0.000 | — |
| BBOX1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N3K9 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:Q70KF4 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q14324 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:Q96CV9 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:O75923 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:- |
| uniprotkb:Q91WZ8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q02539 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| intact:EBI-25426411 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 24
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 24 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Sarcoplasmic reticulum; Cytoplasm; Cytopl / Endoplasmic reticulum, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 25 + 24 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CMYA5 -- Cardiomyopathy-associated protein 5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小4069 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3K9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164309-CMYA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMYA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3K9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (uncertain)。来源: https://www.proteinatlas.org/ENSG00000164309-CMYA5/subcellular

![](https://images.proteinatlas.org/58195/1855_D8_23_cr5ad88133c0ec2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58195/1855_D8_9_cr5ad88133c0b4b_blue_red_green.jpg)
![](https://images.proteinatlas.org/58195/1868_F5_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/58195/1868_F5_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/58195/2227_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/58195/2227_F7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
