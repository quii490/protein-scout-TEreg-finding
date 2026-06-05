---
type: protein-evaluation
gene: "CYGB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYGB — REJECTED (研究热度过高 (PubMed strict=144，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYGB / STAP |
| 蛋白名称 | Cytoglobin |
| 蛋白大小 | 190 aa / 21.4 kDa |
| UniProt ID | Q8WWM9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 21.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=144 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.5; PDB: 1UMO, 1URV, 1URY, 1UT0, 1UX9, 1V5H, 2DC3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000971, IPR009050, IPR012292, IPR013314; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- neuron projection (GO:0043005)
- neuronal cell body (GO:0043025)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 144 |
| PubMed broad count | 309 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STAP |

**关键文献**:
1. SOX7 inhibits the malignant progression of bladder cancer via the DNMT3B/CYGB axis.. *Molecular biomedicine*. PMID: 39227479
2. Insights into the function of cytoglobin.. *Biochemical Society transactions*. PMID: 37721133
3. Molecular analysis of the human cytoglobin mRNA isoforms.. *Journal of inorganic biochemistry*. PMID: 38016326
4. Regulation of Nitric Oxide Metabolism and Vascular Tone by Cytoglobin.. *Antioxidants & redox signaling*. PMID: 31880165
5. Cytoglobin deficiency potentiates Crb1-mediated retinal degeneration in rd8 mice.. *Developmental biology*. PMID: 31634437

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.5 |
| 高置信度残基 (pLDDT>90) 占比 | 75.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 6.3% |
| 有序区域 (pLDDT>70) 占比 | 83.2% |
| 可用 PDB 条目 | 1UMO, 1URV, 1URY, 1UT0, 1UX9, 1V5H, 2DC3, 3AG0, 4B3W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1UMO, 1URV, 1URY, 1UT0, 1UX9, 1V5H, 2DC3, 3AG0, 4B3W）+ AlphaFold极高置信度预测（pLDDT=87.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000971, IPR009050, IPR012292, IPR013314; Pfam: PF00042 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NGB | 0.975 | 0.000 | — |
| RHBDF2 | 0.851 | 0.000 | — |
| ADGB | 0.742 | 0.000 | — |
| EPO | 0.721 | 0.000 | — |
| GPT | 0.706 | 0.000 | — |
| CRP | 0.696 | 0.000 | — |
| DDI1 | 0.675 | 0.467 | — |
| ALB | 0.666 | 0.000 | — |
| GPX3 | 0.658 | 0.000 | — |
| F2 | 0.652 | 0.106 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP13A2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| ZNF747 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| LRATD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DDI1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PRR5-ARHGAP8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MZT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARHGAP8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HNRNPA1L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AKR7A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28536627|imex:IM-26700 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.5 + PDB: 1UMO, 1URV, 1URY, 1UT0, 1UX9,  | pLDDT=87.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CYGB — Cytoglobin，研究基础较多，新颖性有限。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 144 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 144 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWM9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161544-CYGB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYGB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWM9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000161544-CYGB/subcellular

![](https://images.proteinatlas.org/17757/1404_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/17757/1404_D2_3_red_green.jpg)
![](https://images.proteinatlas.org/17757/140_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/17757/140_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/17757/1834_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/17757/1834_E4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WWM9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
