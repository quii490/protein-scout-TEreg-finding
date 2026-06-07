---
type: protein-evaluation
gene: "NCOA7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCOA7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCOA7 / ERAP140, ESNA1 |
| 蛋白名称 | Nuclear receptor coactivator 7 |
| 蛋白大小 | 942 aa / 106.2 kDa |
| UniProt ID | Q8NI08 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 942 aa / 106.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.6; PDB: 7OBP, 8AR6, 8AR9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018392, IPR036779, IPR006571; Pfam: PF01476, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERAP140, ESNA1 |

**关键文献**:
1. Stress granule clearance mediated by V-ATPase-interacting protein NCOA7 mitigates ovarian aging.. *Nature aging*. PMID: 40745099
2. Oxr1 and Ncoa7 regulate V-ATPase to achieve optimal pH for glycosylation within the Golgi apparatus and trans-Golgi network.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40445757
3. Human V-ATPase function is positively and negatively regulated by TLDc proteins.. *Structure (London, England : 1993)*. PMID: 38593795
4. NCOA7 inhibits renal cancer progression by inducing autophagy and lipid metabolism through V-ATPase interaction.. *Cell death discovery*. PMID: 41120258
5. Lessons in self-defence: inhibition of virus entry by intrinsic immunity.. *Nature reviews. Immunology*. PMID: 34646033

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.6 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 57.4% |
| 有序区域 (pLDDT>70) 占比 | 34.9% |
| 可用 PDB 条目 | 7OBP, 8AR6, 8AR9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.6），有序残基占 34.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018392, IPR036779, IPR006571; Pfam: PF01476, PF07534 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.842 | 0.512 | — |
| ESR2 | 0.785 | 0.045 | — |
| ATP6V1B1 | 0.783 | 0.738 | — |
| RARA | 0.688 | 0.045 | — |
| ATP6V1B2 | 0.655 | 0.616 | — |
| ATP6V1G1 | 0.627 | 0.610 | — |
| PPARG | 0.614 | 0.045 | — |
| NCOA2 | 0.610 | 0.000 | — |
| NCOA1 | 0.605 | 0.000 | — |
| NCOA3 | 0.583 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AHR | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10395741 |
| ARNT | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10395741 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3C | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| EBI-2851663 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ATP6V1B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.6 + PDB: 7OBP, 8AR6, 8AR9 | pLDDT=55.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NCOA7 — Nuclear receptor coactivator 7，非常新颖，仅有少数基础研究。
2. 蛋白大小942 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NI08
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111912-NCOA7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCOA7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NI08
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000111912-NCOA7/subcellular

![](https://images.proteinatlas.org/30292/563_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/30292/566_H8_10_red_green.jpg)
![](https://images.proteinatlas.org/30292/566_H8_7_red_green.jpg)
![](https://images.proteinatlas.org/30292/569_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/30292/569_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NI08-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NI08 |
| SMART | SM00257;SM00584; |
| UniProt Domain [FT] | DOMAIN 114..157; /note="LysM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01118"; DOMAIN 781..942; /note="TLDc"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01234" |
| InterPro | IPR018392;IPR036779;IPR006571; |
| Pfam | PF01476;PF07534; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111912-NCOA7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AHR | Intact | false |
| ARNT | Intact | false |
| ESR1 | Biogrid | false |
| GABARAP | Intact | false |
| GABARAPL1 | Intact | false |
| GABARAPL2 | Intact | false |
| MAP1LC3B | Intact | false |
| MAP1LC3C | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
