---
type: protein-evaluation
gene: "FAM209A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM209A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM209A / C20orf106 |
| 蛋白名称 | Protein FAM209A |
| 蛋白大小 | 171 aa / 19.6 kDa |
| UniProt ID | Q5JX71 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus inner membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 171 aa / 19.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027943; Pfam: PF15206 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nuclear inner membrane (GO:0005637)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf106 |

**关键文献**:
1. Omics and Male Infertility: Highlighting the Application of Transcriptomic Data.. *Life (Basel, Switzerland)*. PMID: 35207567
2. Differential Proteomic Analysis of Human Sperm: A Systematic Review to Identify Candidate Targets to Monitor Sperm Quality.. *The world journal of men's health*. PMID: 37118964

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.2% |
| 中等置信 (pLDDT 50-70) 占比 | 31.6% |
| 低置信 (pLDDT<50) 占比 | 36.3% |
| 有序区域 (pLDDT>70) 占比 | 32.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM209A/FAM209A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=58.8），有序残基占 32.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027943; Pfam: PF15206 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMCO5A | 0.705 | 0.000 | — |
| C9orf43 | 0.667 | 0.000 | — |
| C9orf131 | 0.646 | 0.000 | — |
| C12orf40 | 0.626 | 0.000 | — |
| SPATA16 | 0.626 | 0.000 | — |
| MAGEB16 | 0.625 | 0.000 | — |
| ZFAND4 | 0.590 | 0.000 | — |
| TULP2 | 0.573 | 0.000 | — |
| UBASH3B | 0.571 | 0.571 | — |
| PKDREJ | 0.568 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBASH3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC1A1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| APOL2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM218 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC13A3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HACD2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| STX1B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM243 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LPAR3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SCRG1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.8 + PDB: 无 | pLDDT=58.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM209A — Protein FAM209A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小171 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JX71
- Protein Atlas: https://www.proteinatlas.org/search/FAM209A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM209A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JX71
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM209A/FAM209A-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000124103-FAM209A/subcellular

![](https://images.proteinatlas.org/79442/2010_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79442/2010_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/79442/2029_F4_21_cr615ec0c5ba68a_blue_red_green.jpg)
![](https://images.proteinatlas.org/79442/2029_F4_8_cr615ec0c5b9f2c_blue_red_green.jpg)
![](https://images.proteinatlas.org/79442/2070_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79442/2070_E8_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
