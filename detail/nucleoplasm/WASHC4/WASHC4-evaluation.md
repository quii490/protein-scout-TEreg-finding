---
type: protein-evaluation
gene: "WASHC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WASHC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WASHC4 / KIAA1033 |
| 蛋白名称 | WASH complex subunit 4 |
| 蛋白大小 | 1173 aa / 136.4 kDa |
| UniProt ID | Q2M389 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Early endosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1173 aa / 136.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028191, IPR028283, IPR028282, IPR027307; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Early endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- early endosome membrane (GO:0031901)
- endosome (GO:0005768)
- nucleoplasm (GO:0005654)
- WASH complex (GO:0071203)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1033 |

**关键文献**:
1. Genetic disruption of WASHC4 drives endo-lysosomal dysfunction and cognitive-movement impairments in mice and humans.. *eLife*. PMID: 33749590
2. Novel KIAA1033/WASHC4 mutations in three patients with syndromic intellectual disability and a review of the literature.. *American journal of medical genetics. Part A*. PMID: 31953988
3. Loss of the novel Vcp (valosin containing protein) interactor Washc4 interferes with autophagy-mediated proteostasis in striated muscle and leads to myopathy in vivo.. *Autophagy*. PMID: 30010465
4. Proteomic profiling of ovine milk after grading up.. *The Journal of dairy research*. PMID: 33985604
5. FOLFOX treatment response prediction in metastatic or recurrent colorectal cancer patients via machine learning algorithms.. *Cancer medicine*. PMID: 31893575

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.5 |
| 高置信度残基 (pLDDT>90) 占比 | 35.0% |
| 置信残基 (pLDDT 70-90) 占比 | 52.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 87.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.5，有序区 87.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028191, IPR028283, IPR028282, IPR027307; Pfam: PF14745, PF14746, PF14744 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WASHC3 | 0.999 | 0.795 | — |
| WASHC5 | 0.999 | 0.835 | — |
| WASHC1 | 0.999 | 0.736 | — |
| WASHC2C | 0.999 | 0.753 | — |
| WASHC2A | 0.988 | 0.787 | — |
| CAPZA1 | 0.970 | 0.241 | — |
| CAPZB | 0.964 | 0.459 | — |
| FKBP15 | 0.810 | 0.292 | — |
| VPS35 | 0.802 | 0.429 | — |
| CAPZA2 | 0.770 | 0.598 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| A0A0F7R8Z5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Capza1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EBI-1257121 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |
| WASHC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SEC22B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAPZA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.5 + PDB: 无 | pLDDT=83.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Early endosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WASHC4 — WASH complex subunit 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1173 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2M389
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136051-WASHC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WASHC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2M389
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000136051-WASHC4/subcellular

![](https://images.proteinatlas.org/45666/690_H11_3_red_green.jpg)
![](https://images.proteinatlas.org/45666/690_H11_4_red_green.jpg)
![](https://images.proteinatlas.org/45666/739_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/45666/739_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/45666/753_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/45666/753_D5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2M389-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
