---
type: protein-evaluation
gene: "SGSM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGSM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SGSM2 / KIAA0397, RUTBC1 |
| 蛋白名称 | Small G protein signaling modulator 2 |
| 蛋白大小 | 1006 aa / 113.3 kDa |
| UniProt ID | O43147 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Melanosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1006 aa / 113.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000195, IPR035969, IPR004012, IPR037213, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Melanosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- melanosome (GO:0042470)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0397, RUTBC1 |

**关键文献**:
1. SGSM2 inhibits thyroid cancer progression by activating RAP1 and enhancing competitive RAS inhibition.. *Cell death & disease*. PMID: 35264562
2. SGSM2 in Uveal Melanoma: Implications for Survival, Immune Infiltration, and Drug Sensitivity.. *Protein and peptide letters*. PMID: 39501960
3. Small G protein signalling modulator 2 (SGSM2) is involved in oestrogen receptor-positive breast cancer metastasis through enhancement of migratory cell adhesion via interaction with E-cadherin.. *Cell adhesion & migration*. PMID: 30744493
4. Clinical efficacy and gene chip expression analysis of Shenzhu Guanxin recipe granules in patients with intermediate coronary lesions.. *Journal of traditional Chinese medicine = Chung i tsa chih ying wen pan*. PMID: 38767639
5. Salivary proteomics profiling reveals potential biomarkers for chronic kidney disease: a pilot study.. *Frontiers in medicine*. PMID: 39895822

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 38.9% |
| 置信残基 (pLDDT 70-90) 占比 | 24.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 30.5% |
| 有序区域 (pLDDT>70) 占比 | 63.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 63.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000195, IPR035969, IPR004012, IPR037213, IPR047345; Pfam: PF12068, PF00566, PF02759 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SGSM3 | 0.909 | 0.000 | — |
| RAB9A | 0.836 | 0.491 | — |
| RAP1B | 0.763 | 0.000 | — |
| RAB4A | 0.758 | 0.000 | — |
| RAB3A | 0.750 | 0.230 | — |
| RAP2A | 0.716 | 0.000 | — |
| RAB11A | 0.696 | 0.000 | — |
| RAB8A | 0.675 | 0.000 | — |
| RAP1A | 0.663 | 0.000 | — |
| RAP2B | 0.652 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PNO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MPP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FNBP1L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CA12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EGFR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GDPD2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| AFP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CELSR3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Melanosome / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SGSM2 — Small G protein signaling modulator 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1006 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43147
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141258-SGSM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SGSM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43147
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000141258-SGSM2/subcellular

![](https://images.proteinatlas.org/21641/192_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21641/192_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/21641/193_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21641/193_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/21641/194_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21641/194_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43147-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43147 |
| SMART | SM00593;SM00164; |
| UniProt Domain [FT] | DOMAIN 34..191; /note="RUN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00178"; DOMAIN 566..939; /note="Rab-GAP TBC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00163" |
| InterPro | IPR000195;IPR035969;IPR004012;IPR037213;IPR047345;IPR037745;IPR021935; |
| Pfam | PF12068;PF00566;PF02759; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141258-SGSM2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RAB9A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
