---
type: protein-evaluation
gene: "ARFGAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARFGAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARFGAP1 |
| 蛋白名称 | ARFGAP1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | ARFGAP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nuclear membrane, Vesicles, Primary cil; UniProt: 暂无数据（UniProt获取失败） |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=94 篇 (≤100→2) |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 🧬 调控结构域 | 4/10 | ×2 | 8 | 暂无数据 (UniProt未获取) |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.5/180** | |
| **归一化总分 (÷1.83)** | | | **32.8/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nuclear membrane, Vesicles, Primary cilium, Cytosol | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 94 |
| PubMed broad count | 136 |
| 别名(未计入scoring) |  |

**关键文献**:
1. ArfGAP1 is a GTPase activating protein for LRRK2: reciprocal regulation of ArfGAP1 by LRRK2.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 22423108
2. ArfGAP1 acts as a GTPase-activating protein for human ADP-ribosylation factor-like 1 protein.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 33715220
3. ArfGAP1 inhibits mTORC1 lysosomal localization and activation.. *The EMBO journal*. PMID: 33988249
4. Golgi localization determinants in ArfGAP1 and in new tissue-specific ArfGAP1 isoforms.. *The Journal of biological chemistry*. PMID: 16316994
5. ARFGAP1 promotes AP-2-dependent endocytosis.. *Nature cell biology*. PMID: 21499258

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARF1 | 0.989 | 0.719 | — |
| MOGS | 0.960 | 0.000 | — |
| ARFGAP2 | 0.899 | 0.725 | — |
| ARF6 | 0.890 | 0.129 | — |
| ARFGAP3 | 0.889 | 0.719 | — |
| KDELR1 | 0.830 | 0.541 | — |
| GBF1 | 0.809 | 0.166 | — |
| ARF5 | 0.795 | 0.288 | — |
| AP2B1 | 0.768 | 0.613 | — |
| EDC4 | 0.767 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| stumps | psi-mi:"MI:0018"(two hybrid) | pubmed:12767830 |
| ArfGAP3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RGS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| gcm2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| vnd | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Sry-alpha | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| REEP5 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| APOB | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| APOC3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Golgi apparatus; 额外: Nuclear membrane, Vesicles, P | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0 (仅1源)
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ 

**核心优势**:
1. ARFGAP1 — ARFGAP1 (UniProt未获取)，有一定研究基础，但仍存在niche空间。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 94 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/ARFGAP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101199-ARFGAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARFGAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/ARFGAP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:28:43

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000101199-ARFGAP1/subcellular

![](https://images.proteinatlas.org/51019/742_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51019/742_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51019/807_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51019/807_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51019/846_G7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51019/846_G7_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N6T3 |
| SMART | SM00105; |
| UniProt Domain [FT] | DOMAIN 7..124; /note="Arf-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00288" |
| InterPro | IPR037278;IPR001164;IPR038508; |
| Pfam | PF01412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000101199-ARFGAP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LRRK2 | Intact, Biogrid | true |
| ARF1 | Biogrid | false |
| AURKA | Biogrid | false |
| CD2AP | Opencell | false |
| COPG2 | Opencell | false |
| GABARAPL2 | Intact | false |
| GRN | Intact | false |
| GSTM5 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
