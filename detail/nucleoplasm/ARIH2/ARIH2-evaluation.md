---
type: protein-evaluation
gene: "ARIH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARIH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARIH2 / ARI2, TRIAD1 |
| 蛋白名称 | E3 ubiquitin-protein ligase ARIH2 |
| 蛋白大小 | 493 aa / 57.8 kDa |
| UniProt ID | O95376 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 493 aa / 57.8 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.5; PDB: 7OD1, 7ONI |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045840, IPR047555, IPR031127, IPR002867, IPR047 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分 (÷1.83)** | | | **71.0/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARI2, TRIAD1 |

**关键文献**:
1. Genome-wide CRISPR screens identify critical targets to enhance CAR-NK cell antitumor potency.. *Cancer cell*. PMID: 40845844
2. Pyruvate dehydrogenase B regulates myogenic differentiation via the FoxP1-Arih2 axis.. *Journal of cachexia, sarcopenia and muscle*. PMID: 36564038
3. HSPA8 lactylation attenuates neuronal pyroptosis via E3 ligase-mediated NLRP3 degradation after ischemic stroke.. *Apoptosis : an international journal on programmed cell death*. PMID: 41518395
4. YTHDC1 promotes postnatal brown adipose tissue development and thermogenesis by stabilizing PPARγ.. *The EMBO journal*. PMID: 40355558
5. Arih2 gene influences immune response and tissue development in chicken.. *Bioscience reports*. PMID: 31551339

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 85.6% |
| 可用 PDB 条目 | 7OD1, 7ONI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7OD1, 7ONI）+ AlphaFold高质量预测（pLDDT=86.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045840, IPR047555, IPR031127, IPR002867, IPR047556; Pfam: PF19422, PF01485, PF22191 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.997 | 0.977 | — |
| RNF7 | 0.985 | 0.900 | — |
| UBE2L3 | 0.963 | 0.873 | — |
| NEDD8 | 0.938 | 0.901 | — |
| ELOB | 0.864 | 0.422 | — |
| UBE2L6 | 0.848 | 0.800 | — |
| BUB1 | 0.761 | 0.761 | — |
| ELOC | 0.745 | 0.422 | — |
| RING1 | 0.732 | 0.000 | — |
| MLLT10 | 0.724 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBE2L3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BUB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UGP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPL8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ARAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 7OD1, 7ONI | pLDDT=86.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ARIH2 — E3 ubiquitin-protein ligase ARIH2，非常新颖，仅有少数基础研究。
2. 蛋白大小493 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95376
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177479-ARIH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARIH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95376
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:30:28

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000177479-ARIH2/subcellular

![](https://images.proteinatlas.org/67381/1237_B2_4_red_green.jpg)
![](https://images.proteinatlas.org/67381/1237_B2_6_red_green.jpg)
![](https://images.proteinatlas.org/67381/1284_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/67381/1284_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/67381/1754_B2_13_cr57f3cd82b5ddd_red_green.jpg)
![](https://images.proteinatlas.org/67381/1754_B2_9_cr57f3cd795e754_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95376-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95376 |
| SMART | SM00647;SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045840;IPR047555;IPR031127;IPR002867;IPR047556;IPR044066;IPR018957;IPR001841;IPR013083;IPR017907; |
| Pfam | PF19422;PF01485;PF22191;PF26000;PF00097; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177479-ARIH2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASB6 | Biogrid, Bioplex | true |
| CUL5 | Intact, Biogrid, Bioplex | true |
| TP53 | Intact, Biogrid | true |
| UBE2L3 | Intact, Biogrid | true |
| UBE2L6 | Intact, Biogrid | true |
| APOBEC3G | Biogrid | false |
| BUB1 | Intact | false |
| CKB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
