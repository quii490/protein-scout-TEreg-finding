---
type: protein-evaluation
gene: "TARS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TARS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TARS3 / TARSL2 |
| 蛋白名称 | Threonine--tRNA ligase 2, cytoplasmic |
| 蛋白大小 | 802 aa / 92.6 kDa |
| UniProt ID | A2RTX5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 802 aa / 92.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002314, IPR006195, IPR045864, IPR004154, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TARSL2 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 71.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 87.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.4，有序区 87.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002314, IPR006195, IPR045864, IPR004154, IPR036621; Pfam: PF03129, PF02824, PF00587 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LARS1 | 0.994 | 0.755 | — |
| LARS2 | 0.980 | 0.065 | — |
| TARS1 | 0.958 | 0.596 | — |
| AARS1 | 0.955 | 0.443 | — |
| IARS1 | 0.951 | 0.596 | — |
| KARS1 | 0.951 | 0.737 | — |
| EPRS1 | 0.924 | 0.219 | — |
| TARS2 | 0.919 | 0.199 | — |
| QARS1 | 0.918 | 0.591 | — |
| RARS1 | 0.914 | 0.691 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TP53BP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| ECSIT | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TARS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARPC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TARS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LGALS14 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 无 | pLDDT=87.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
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
1. TARS3 — Threonine--tRNA ligase 2, cytoplasmic，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小802 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A2RTX5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185418-TARS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TARS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A2RTX5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000185418-TARS3/subcellular

![](https://images.proteinatlas.org/66697/1285_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66697/1285_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66697/1288_G6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/66697/1288_G6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/66697/1416_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66697/1416_G2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A2RTX5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A2RTX5 |
| SMART | SM00863; |
| UniProt Domain [FT] | DOMAIN 157..222; /note="TGS"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01228" |
| InterPro | IPR002314;IPR006195;IPR045864;IPR004154;IPR036621;IPR012675;IPR004095;IPR012676;IPR002320;IPR018163;IPR047246;IPR033728;IPR012947; |
| Pfam | PF03129;PF02824;PF00587;PF07973; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185418-TARS3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARPC3 | Intact | false |
| ATF4 | Intact | false |
| ECSIT | Intact | false |
| LGALS14 | Intact | false |
| TARS1 | Intact, Biogrid | false |
| TARS2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
