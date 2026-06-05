---
type: protein-evaluation
gene: "ANXA5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ANXA5 — REJECTED (研究热度过高 (PubMed strict=363，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANXA5 / ANX5, ENX2, PP4 |
| 蛋白名称 | Annexin A5 |
| 蛋白大小 | 320 aa / 35.9 kDa |
| UniProt ID | P08758 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 320 aa / 35.9 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=363 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.1; PDB: 1ANW, 1ANX, 1AVH, 1AVR, 1HAK, 1HVD, 1HVE |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001464, IPR018502, IPR018252, IPR037104, IPR002 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分 (÷1.83)** | | | **49.7/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endothelial microparticle (GO:0072563)
- external side of plasma membrane (GO:0009897)
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 363 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANX5, ENX2, PP4 |

**关键文献**:
1. Artesunate Sensitizes human hepatocellular carcinoma to sorafenib via exacerbating AFAP1L2-SRC-FUNDC1 axis-dependent mitophagy.. *Autophagy*. PMID: 37733919
2. Alternative mitochondrial quality control mediated by extracellular release.. *Autophagy*. PMID: 33218272
3. Inhibition of PINK1 senses ROS signaling to facilitate neuroblastoma cell pyroptosis.. *Autophagy*. PMID: 40160153
4. Gallium-68-dotamaleimide-Cys165-annexin A5.. **. PMID: 21850779
5. Gallium-68-dotamaleimide-Cys2-annexin A5.. **. PMID: 21850781

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.1 |
| 高置信度残基 (pLDDT>90) 占比 | 93.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 98.8% |
| 可用 PDB 条目 | 1ANW, 1ANX, 1AVH, 1AVR, 1HAK, 1HVD, 1HVE, 1HVF, 1HVG, 1SAV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1ANW, 1ANX, 1AVH, 1AVR, 1HAK, 1HVD, 1HVE, 1HVF, 1HVG, 1SAV）+ AlphaFold极高置信度预测（pLDDT=96.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001464, IPR018502, IPR018252, IPR037104, IPR002392; Pfam: PF00191 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTB | 0.950 | 0.141 | — |
| GAPDH | 0.943 | 0.000 | — |
| CASP3 | 0.921 | 0.000 | — |
| BCL2 | 0.899 | 0.000 | — |
| CCK | 0.891 | 0.000 | — |
| PXDNL | 0.888 | 0.000 | — |
| PXDN | 0.888 | 0.000 | — |
| CASP9 | 0.885 | 0.000 | — |
| PARP1 | 0.874 | 0.000 | — |
| F3 | 0.854 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FDFT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SUPT4H1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EIF4G1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| LAMC3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Col11a1 | psi-mi:"MI:0096"(pull down) | pubmed:22038862|imex:IM-16591 |
| ATF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22304920|imex:IM-17307 |
| PPP2R1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11929|pubmed:17540176| |
| KCNMA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15154|pubmed:22174833 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.1 + PDB: 1ANW, 1ANX, 1AVH, 1AVR, 1HAK,  | pLDDT=96.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ANXA5 — Annexin A5，有一定研究基础，但仍存在niche空间。
2. 蛋白大小320 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 363 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 363 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P08758
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164111-ANXA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANXA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P08758
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:54:19

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000164111-ANXA5/subcellular

![](https://images.proteinatlas.org/35330/690_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/35330/690_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/35330/728_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35330/728_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/35330/896_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35330/896_B6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P08758-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
