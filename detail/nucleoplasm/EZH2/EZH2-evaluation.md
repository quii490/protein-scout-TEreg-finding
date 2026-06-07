---
type: protein-evaluation
gene: "EZH2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EZH2 — REJECTED (研究热度过高 (PubMed strict=4554，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EZH2 / KMT6 |
| 蛋白名称 | Histone-lysine N-methyltransferase EZH2 |
| 蛋白大小 | 746 aa / 85.4 kDa |
| UniProt ID | Q15910 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 746 aa / 85.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4554 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.2; PDB: 4MI0, 4MI5, 5GSA, 5H14, 5H15, 5H17, 5H19 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026489, IPR045318, IPR048358, IPR021654, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromatin silencing complex (GO:0005677)
- chromosome (GO:0005694)
- chromosome, telomeric region (GO:0000781)
- ESC/E(Z) complex (GO:0035098)
- heterochromatin (GO:0000792)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4554 |
| PubMed broad count | 7917 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KMT6 |

**关键文献**:
1. The roles of EZH2 in cancer and its inhibitors.. *Medical oncology (Northwood, London, England)*. PMID: 37148376
2. Ezh2 Shapes T Cell Plasticity to Drive Atherosclerosis.. *Circulation*. PMID: 39917842
3. PRMT5 functionally associates with EZH2 to promote colorectal cancer progression through epigenetically repressing CDKN2B expression.. *Theranostics*. PMID: 33664859
4. ROS regulates circadian rhythms by modulating Ezh2 interactions with clock proteins.. *Redox biology*. PMID: 39952198
5. EZH2 noncanonically binds cMyc and p300 through a cryptic transactivation domain to mediate gene activation and promote oncogenesis.. *Nature cell biology*. PMID: 35210568

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 42.9% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 68.8% |
| 可用 PDB 条目 | 4MI0, 4MI5, 5GSA, 5H14, 5H15, 5H17, 5H19, 5H24, 5H25, 5HYN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4MI0, 4MI5, 5GSA, 5H14, 5H15, 5H17, 5H19, 5H24, 5H25, 5HYN）+ AlphaFold极高置信度预测（pLDDT=76.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026489, IPR045318, IPR048358, IPR021654, IPR044439; Pfam: PF21358, PF11616, PF18118 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUZ12 | 0.999 | 0.999 | — |
| RBBP7 | 0.999 | 0.903 | — |
| RBBP4 | 0.999 | 0.919 | — |
| EED | 0.999 | 0.998 | — |
| DNMT1 | 0.999 | 0.826 | — |
| HDAC1 | 0.999 | 0.862 | — |
| BMI1 | 0.999 | 0.610 | — |
| DNMT3B | 0.999 | 0.790 | — |
| HDAC2 | 0.999 | 0.812 | — |
| AEBP2 | 0.999 | 0.933 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PHF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11571280 |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| POLA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GTF3C1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KLHDC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PIN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ATP1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PSMB6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SKIC8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 4MI0, 4MI5, 5GSA, 5H14, 5H15,  | pLDDT=76.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. EZH2 — Histone-lysine N-methyltransferase EZH2，研究基础较多，新颖性有限。
2. 蛋白大小746 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4554 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4554 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15910
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106462-EZH2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EZH2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15910
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000106462-EZH2/subcellular

![](https://images.proteinatlas.org/29131/2145_E8_56_blue_red_green.jpg)
![](https://images.proteinatlas.org/29131/2145_E8_70_blue_red_green.jpg)
![](https://images.proteinatlas.org/29131/2153_C1_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/29131/2153_C1_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/29131/2268_A1_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/29131/2268_A1_187_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15910-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15910 |
| SMART | SM01114;SM00717;SM00317; |
| UniProt Domain [FT] | DOMAIN 503..605; /note="CXC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00970"; DOMAIN 612..727; /note="SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00190" |
| InterPro | IPR026489;IPR045318;IPR048358;IPR021654;IPR044439;IPR041343;IPR041355;IPR001005;IPR001214;IPR046341;IPR033467; |
| Pfam | PF21358;PF11616;PF18118;PF18264;PF00856; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106462-EZH2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AEBP2 | Intact, Biogrid | true |
| AR | Intact, Biogrid | true |
| ATRX | Intact, Biogrid | true |
| CAPRIN1 | Biogrid, Opencell | true |
| CUL4B | Intact, Biogrid | true |
| DNMT1 | Intact, Biogrid | true |
| DNMT3A | Intact, Biogrid | true |
| DNMT3B | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
