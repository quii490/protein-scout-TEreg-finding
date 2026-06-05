---
type: protein-evaluation
gene: "PML"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PML — REJECTED (研究热度过高 (PubMed strict=3819，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PML |
| 蛋白名称 | PML (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | PML |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3819 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Enhanced |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3819 |
| PubMed broad count | 8997 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Function of PML-RARA in Acute Promyelocytic Leukemia.. *Advances in experimental medicine and biology*. PMID: 39017850
2. Phase separation of PML/RARα and BRD4 coassembled microspeckles governs transcriptional dysregulation in acute promyelocytic leukemia.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39136995
3. PML and PML-like exonucleases restrict retrotransposons in jawed vertebrates.. *Nucleic acids research*. PMID: 36912092
4. Promyelocytic leukemia protein (PML) and stem cells: from cancer to pluripotency.. *The International journal of developmental biology*. PMID: 34881785
5. Functional interactions between the Epstein-Barr virus BZLF1 protein and the promyelocytic leukemia protein.. *Virus research*. PMID: 16307818

**评价**: 研究基础较多，新颖性有限。

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

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUMO1 | 0.999 | 0.990 | — |
| DAXX | 0.999 | 0.925 | — |
| RARA | 0.998 | 0.837 | — |
| UBE2I | 0.981 | 0.901 | — |
| SP100 | 0.981 | 0.757 | — |
| RUNX1 | 0.974 | 0.513 | — |
| TP53 | 0.967 | 0.874 | — |
| RNF4 | 0.944 | 0.869 | — |
| SPI1 | 0.938 | 0.301 | — |
| MDM2 | 0.934 | 0.837 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000268058.3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9294197|imex:IM-19379 |
| ENSP00000315434.8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CUL3 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:21840486|imex:IM-16569 |
| KLHL20 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:21840486|imex:IM-16569 |
| CDKN2A | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:12740913 |
| NF1 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:22293200|imex:IM-18724 |
| GOLGA6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DAXX | psi-mi:"MI:0018"(two hybrid) | pubmed:10669754 |
| SUMO1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11948183 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11972|pubmed:16873060 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PML — PML (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3819 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3819 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/PML
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140464-PML/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PML
- AlphaFold: https://alphafold.ebi.ac.uk/entry/PML
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (enhanced)。来源: https://www.proteinatlas.org/ENSG00000140464-PML/subcellular

![](https://images.proteinatlas.org/10194/921_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/10194/921_B10_4_red_green.jpg)
![](https://images.proteinatlas.org/10194/923_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/10194/923_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/10194/931_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/10194/931_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
