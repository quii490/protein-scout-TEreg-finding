---
type: protein-evaluation
gene: "TRIM7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM7 / GNIP, RNF90 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM7 |
| 蛋白大小 | 511 aa / 56.6 kDa |
| UniProt ID | Q9C029 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 511 aa / 56.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=85.5; PDB: 6UMA, 6UMB, 7OVX, 7OW2, 7W0Q, 7W0S, 7W0T |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm; Golgi apparatus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNIP, RNF90 |

**关键文献**:
1. Envelope protein ubiquitination drives entry and pathogenesis of Zika virus.. *Nature*. PMID: 32641828
2. TRIM7 modulates NCOA4-mediated ferritinophagy and ferroptosis in glioblastoma cells.. *Redox biology*. PMID: 36067704
3. TRIM7 inhibits enterovirus replication and promotes emergence of a viral variant with increased pathogenicity.. *Cell*. PMID: 34062120
4. TRIM7/RNF90 promotes autophagy via regulation of ATG7 ubiquitination during L. monocytogenes infection.. *Autophagy*. PMID: 36576150
5. TRIM7 ubiquitinates SARS-CoV-2 membrane protein to limit apoptosis and viral replication.. *Nature communications*. PMID: 39616206

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 61.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 8.0% |
| 有序区域 (pLDDT>70) 占比 | 87.6% |
| 可用 PDB 条目 | 6UMA, 6UMB, 7OVX, 7OW2, 7W0Q, 7W0S, 7W0T, 7X6Y, 7X6Z, 7X70 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6UMA, 6UMB, 7OVX, 7OW2, 7W0Q, 7W0S, 7W0T, 7X6Y, 7X6Z, 7X70）+ AlphaFold极高置信度预测（pLDDT=85.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006574; Pfam: PF13765, PF00622, PF00643 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GYG1 | 0.987 | 0.807 | — |
| GYG2 | 0.962 | 0.425 | — |
| TRAT1 | 0.830 | 0.000 | — |
| BBOX1 | 0.747 | 0.000 | — |
| UBE2D1 | 0.746 | 0.674 | — |
| BRMS1 | 0.625 | 0.292 | — |
| KLHL40 | 0.470 | 0.000 | — |
| ARMC12 | 0.459 | 0.000 | — |
| INIP | 0.458 | 0.000 | — |
| TRIM46 | 0.431 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000274773.7 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dnaX | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dacB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| flbD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| icmF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| sgbU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| lptD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| AQP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CFL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 6UMA, 6UMB, 7OVX, 7OW2, 7W0Q,  | pLDDT=85.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Golgi apparatus / Vesicles; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRIM7 — E3 ubiquitin-protein ligase TRIM7，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小511 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C029
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146054-TRIM7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C029
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000146054-TRIM7/subcellular

![](https://images.proteinatlas.org/39213/413_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39213/413_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39213/417_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39213/417_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39213/420_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39213/420_F8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C029-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
