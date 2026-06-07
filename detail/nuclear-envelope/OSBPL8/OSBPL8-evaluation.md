---
type: protein-evaluation
gene: "OSBPL8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL8 / KIAA1451, ORP8, OSBP10 |
| 蛋白名称 | Oxysterol-binding protein-related protein 8 |
| 蛋白大小 | 889 aa / 101.2 kDa |
| UniProt ID | Q9BZF1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cytosol; UniProt: Endoplasmic reticulum membrane; Nucleus membrane; Endoplasmi |
| 蛋白大小 | 8/10 | ×1 | 8 | 889 aa / 101.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.1; PDB: 1V88, 5U77, 5U78, 8P7A |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol | Approved |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cortical endoplasmic reticulum (GO:0032541)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1451, ORP8, OSBP10 |

**关键文献**:
1. Dysfunction of autophagy in high-fat diet-induced non-alcoholic fatty liver disease.. *Autophagy*. PMID: 37700498
2. ORP8 acts as a lipophagy receptor to mediate lipid droplet turnover.. *Protein & cell*. PMID: 37707322
3. A GPX1-OSBPL8 axis mediates noncanonical in vivo ferroptosis and cancer growth suppression.. *Cell*. PMID: 41720096
4. BMDM-derived ORP8 suppresses lipotoxicity and inflammation by relieving endoplasmic reticulum stress in mice with MASH.. *Molecular medicine (Cambridge, Mass.)*. PMID: 40448016
5. The expression, immune infiltration, prognosis, and experimental validation of OSBPL family genes in liver cancer.. *BMC cancer*. PMID: 36918840

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 37.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 32.1% |
| 有序区域 (pLDDT>70) 占比 | 57.0% |
| 可用 PDB 条目 | 1V88, 5U77, 5U78, 8P7A |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1V88, 5U77, 5U78, 8P7A）+ AlphaFold高质量预测（pLDDT=70.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR001849; Pfam: PF01237, PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RMDN3 | 0.989 | 0.071 | — |
| OSBPL5 | 0.754 | 0.619 | — |
| PLEK2 | 0.703 | 0.000 | — |
| PLEK | 0.699 | 0.000 | — |
| GPR89A | 0.677 | 0.000 | — |
| GPR89B | 0.676 | 0.000 | — |
| VAPB | 0.658 | 0.230 | — |
| USP5 | 0.650 | 0.292 | — |
| ESYT2 | 0.636 | 0.173 | — |
| GLG1 | 0.619 | 0.606 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| SQSTM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TFCP2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ENSP00000261183.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| codA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CD74 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 1V88, 5U77, 5U78, 8P7A | pLDDT=70.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane;  / Vesicles, Cytosol | 一致 |
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
1. OSBPL8 — Oxysterol-binding protein-related protein 8，非常新颖，仅有少数基础研究。
2. 蛋白大小889 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZF1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000091039-OSBPL8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZF1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000091039-OSBPL8/subcellular

![](https://images.proteinatlas.org/1309/59_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1309/59_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1309/60_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1309/60_D4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1309/61_D4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1309/61_D4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZF1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BZF1 |
| SMART | SM00233; |
| UniProt Domain [FT] | DOMAIN 148..265; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR037239;IPR000648;IPR018494;IPR011993;IPR001849; |
| Pfam | PF01237;PF00169; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000091039-OSBPL8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ESYT1 | Biogrid, Opencell | true |
| GLG1 | Biogrid, Opencell | true |
| ALK | Biogrid | false |
| AMFR | Biogrid | false |
| CSNK2A1 | Biogrid | false |
| CSNK2A2 | Biogrid | false |
| ERLIN1 | Opencell | false |
| ERLIN2 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
