---
type: protein-evaluation
gene: "DENND4B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DENND4B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND4B / KIAA0476 |
| 蛋白名称 | DENN domain-containing protein 4B |
| 蛋白大小 | 1496 aa / 163.8 kDa |
| UniProt ID | O75064 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Golgi apparatus |
| 蛋白大小 | 5/10 | x1 | 5 | 1496 aa / 163.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=2 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=72.2; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR001194, IPR005112, IPR043153, IPR051696, IPR023 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 14 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Golgi apparatus | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0476 |

**关键文献**:
1. Genome-wide association study of hippocampal blood-oxygen-level-dependent-cerebral blood flow correlation in Chinese Han population.. *iScience*. PMID: 37822511
2. Genes and compounds that increase type VII collagen expression as potential treatments for dystrophic epidermolysis bullosa.. *Experimental dermatology*. PMID: 35243691

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 33.5% |
| 置信残基 (pLDDT 70-90) 占比 | 34.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 67.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.2，有序区 67.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001194, IPR005112, IPR043153, IPR051696, IPR023341; Pfam: PF03455, PF02141, PF03456 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB10 | 0.666 | 0.098 | — |
| CRTC2 | 0.633 | 0.000 | — |
| DENND1A | 0.499 | 0.099 | — |
| DENND1C | 0.474 | 0.099 | — |
| DENND5B | 0.460 | 0.117 | — |
| GDI1 | 0.452 | 0.000 | — |
| ARAP1 | 0.450 | 0.000 | — |
| GDI2 | 0.424 | 0.000 | — |
| TMEM160 | 0.413 | 0.000 | — |
| RNF123 | 0.411 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| manY | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-2851171 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| argE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ZMAT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CALM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLEKHJ1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000361217 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 8
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 无 | pLDDT=72.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 14 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. DENND4B -- DENN domain-containing protein 4B，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小1496 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75064
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198837-DENND4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75064
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000198837-DENND4B/subcellular

![](https://images.proteinatlas.org/40188/411_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/40188/411_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/40188/415_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/40188/415_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/40188/416_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/40188/416_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75064-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
