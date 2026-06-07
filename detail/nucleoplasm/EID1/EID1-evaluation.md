---
type: protein-evaluation
gene: "EID1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EID1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EID1 / C15orf3, CRI1, RBP21 |
| 蛋白名称 | EP300-interacting inhibitor of differentiation 1 |
| 蛋白大小 | 187 aa / 20.9 kDa |
| UniProt ID | Q9Y6B2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 187 aa / 20.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.2; PDB: 7SMD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033258 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 88 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf3, CRI1, RBP21 |

**关键文献**:
1. Interaction between photoperiod and variation in circadian rhythms in tomato.. *BMC plant biology*. PMID: 35395725
2. Protein Palmitoylation Regulates Neural Stem Cell Differentiation by Modulation of EID1 Activity.. *Molecular neurobiology*. PMID: 26497028
3. Mutations in EID1 and LNK2 caused light-conditional clock deceleration during tomato domestication.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 29789384
4. Functional analysis of EID1, an F-box protein involved in phytochrome A-dependent light signal transduction.. *The Plant journal : for cell and molecular biology*. PMID: 16412087
5. Structural insights into gene repression by the orphan nuclear receptor SHP.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 24379397

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 44.9% |
| 低置信 (pLDDT<50) 占比 | 36.9% |
| 有序区域 (pLDDT>70) 占比 | 18.2% |
| 可用 PDB 条目 | 7SMD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.2），有序残基占 18.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033258 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RB1 | 0.892 | 0.868 | — |
| EP300 | 0.878 | 0.735 | — |
| NR0B2 | 0.871 | 0.625 | — |
| NDN | 0.868 | 0.688 | — |
| EID3 | 0.855 | 0.000 | — |
| RBL1 | 0.819 | 0.797 | — |
| FBXO21 | 0.786 | 0.627 | — |
| CREBBP | 0.705 | 0.510 | — |
| MDM2 | 0.701 | 0.516 | — |
| RBL2 | 0.663 | 0.602 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1A | psi-mi:"MI:0018"(two hybrid) | pubmed:12795696 |
| SKP1B | psi-mi:"MI:0018"(two hybrid) | pubmed:12795696 |
| UBAC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF4EBP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Q81YE8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ASK4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| Ndn | psi-mi:"MI:0018"(two hybrid) | pubmed:18557765|imex:IM-19307 |
| ASK11 | psi-mi:"MI:0018"(two hybrid) | pubmed:16412087 |
| ASK13 | psi-mi:"MI:0018"(two hybrid) | pubmed:16412087 |
| ASK14 | psi-mi:"MI:0018"(two hybrid) | pubmed:16412087 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.2 + PDB: 7SMD | pLDDT=56.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EID1 — EP300-interacting inhibitor of differentiation 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小187 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6B2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000255302-EID1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EID1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6B2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000255302-EID1/subcellular

![](https://images.proteinatlas.org/51122/712_D11_3_red_green.jpg)
![](https://images.proteinatlas.org/51122/712_D11_5_red_green.jpg)
![](https://images.proteinatlas.org/51122/804_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/51122/804_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/51122/964_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/51122/964_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y6B2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y6B2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033258; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000255302-EID1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXO21 | Intact, Biogrid | true |
| NDN | Intact, Biogrid | true |
| CREBBP | Biogrid | false |
| EP300 | Biogrid | false |
| MDM2 | Biogrid | false |
| NR0B2 | Biogrid | false |
| PCID2 | Biogrid | false |
| RB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
