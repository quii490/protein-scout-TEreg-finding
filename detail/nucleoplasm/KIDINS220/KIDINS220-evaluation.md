---
type: protein-evaluation
gene: "KIDINS220"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIDINS220 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIDINS220 / ARMS, KIAA1250 |
| 蛋白名称 | Kinase D-interacting substrate of 220 kDa |
| 蛋白大小 | 1771 aa / 196.5 kDa |
| UniProt ID | Q9ULH0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Membrane; Late endosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1771 aa / 196.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=97 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 9JXQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR011646, IPR052771, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Uncertain |
| UniProt | Membrane; Late endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- late endosome (GO:0005770)
- membrane (GO:0016020)
- protein-containing complex (GO:0032991)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 97 |
| PubMed broad count | 134 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARMS, KIAA1250 |

**关键文献**:
1. Phosphate dysregulation via the XPR1-KIDINS220 protein complex is a therapeutic vulnerability in ovarian cancer.. *Nature cancer*. PMID: 35437317
2. Matrix stiffness regulates nucleus pulposus cell glycolysis by MRTF-A-dependent mechanotransduction.. *Bone research*. PMID: 39952914
3. KIDINS220 and InsP8 safeguard the stepwise regulation of phosphate exporter XPR1.. *Molecular cell*. PMID: 40858110
4. Functions of the multi-interacting protein KIDINS220/ARMS in cancer and other pathologies.. *Genes, chromosomes & cancer*. PMID: 29181864
5. Kidins220/ARMS modulates brain morphology and anxiety-like traits in adult mice.. *Cell death discovery*. PMID: 35140204

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 34.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 39.8% |
| 有序区域 (pLDDT>70) 占比 | 50.6% |
| 可用 PDB 条目 | 9JXQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 50.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR011646, IPR052771, IPR013761; Pfam: PF00023, PF12796, PF07693 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NTRK1 | 0.987 | 0.396 | — |
| CRKL | 0.955 | 0.303 | — |
| CRK | 0.917 | 0.050 | — |
| XPR1 | 0.814 | 0.766 | — |
| MAGI2 | 0.808 | 0.797 | — |
| SNX27 | 0.732 | 0.510 | — |
| PRKD3 | 0.715 | 0.062 | — |
| PRKD1 | 0.685 | 0.062 | — |
| NGF | 0.683 | 0.000 | — |
| NTRK2 | 0.675 | 0.212 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MOB4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CDC73 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Ntrk1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14422|pubmed:16284401| |
| CRKL | psi-mi:"MI:0096"(pull down) | imex:IM-14422|pubmed:16284401| |
| RAPGEF1 | psi-mi:"MI:0096"(pull down) | imex:IM-14422|pubmed:16284401| |
| Q9ERD4 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-14422|pubmed:16284401| |
| fer | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| glgB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| MYC | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 9JXQ | pLDDT=61.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane; Late endosome / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. KIDINS220 — Kinase D-interacting substrate of 220 kDa，研究基础较多，新颖性有限。
2. 蛋白大小1771 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 97 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134313-KIDINS220/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIDINS220
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULH0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000134313-KIDINS220/subcellular

![](https://images.proteinatlas.org/14790/2147_E11_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/14790/2147_E11_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/14790/2150_E4_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/14790/2150_E4_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/14790/1124_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/14790/1124_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULH0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9ULH0 |
| SMART | SM00248; |
| UniProt Domain [FT] | DOMAIN 440..953; /note="KAP NTPase" |
| InterPro | IPR002110;IPR036770;IPR011646;IPR052771;IPR013761;IPR057092; |
| Pfam | PF00023;PF12796;PF07693;PF23307; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134313-KIDINS220/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLTA | Opencell | false |
| EPHA2 | Biogrid | false |
| FGFR2 | Biogrid | false |
| GSK3B | Biogrid | false |
| KRAS | Biogrid | false |
| LAMP1 | Biogrid | false |
| NRAS | Biogrid | false |
| NTRK1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
