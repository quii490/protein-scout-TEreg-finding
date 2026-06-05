---
type: protein-evaluation
gene: "AARS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AARS2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AARS2 / AARSL, KIAA1270 |
| 蛋白名称 | Alanine--tRNA ligase, mitochondrial |
| 蛋白大小 | 985 aa / 107.3 kDa |
| UniProt ID | Q5JTZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion |
| 蛋白大小 | 8/10 | ×1 | 8 | 985 aa / 107.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.9; PDB: 6NLQ, 6NLY, 6NOW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045864, IPR002318, IPR018162, IPR018165, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Enhanced |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 99 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AARSL, KIAA1270 |

**关键文献**:
1. Hypoxia induces mitochondrial protein lactylation to limit oxidative phosphorylation.. *Cell research*. PMID: 38163844
2. Emerging roles of lysine lactyltransferases and lactylation.. *Nature cell biology*. PMID: 40185947
3. AARS2-catalyzed lactylation induces follicle development and premature ovarian insufficiency.. *Cell death discovery*. PMID: 40301335
4. AARS2 ameliorates myocardial ischemia via fine-tuning PKM2-mediated metabolism.. *eLife*. PMID: 40371904
5. Srsf3-Dependent APA Drives Macrophage Maturation and Limits Atherosclerosis.. *Circulation research*. PMID: 40160097

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.9 |
| 高置信度残基 (pLDDT>90) 占比 | 61.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 4.5% |
| 有序区域 (pLDDT>70) 占比 | 92.5% |
| 可用 PDB 条目 | 6NLQ, 6NLY, 6NOW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6NLQ, 6NLY, 6NOW）+ AlphaFold高质量预测（pLDDT=87.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045864, IPR002318, IPR018162, IPR018165, IPR018164; Pfam: PF01411, PF07973 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DARS2 | 0.955 | 0.125 | — |
| VARS2 | 0.937 | 0.125 | — |
| YARS1 | 0.927 | 0.067 | — |
| EARS2 | 0.927 | 0.128 | — |
| LARS2 | 0.924 | 0.162 | — |
| IARS2 | 0.918 | 0.166 | — |
| VARS1 | 0.915 | 0.000 | — |
| TARS2 | 0.910 | 0.095 | — |
| AARS1 | 0.910 | 0.000 | — |
| RARS2 | 0.905 | 0.217 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEGF10 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| SUCLG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SDHA | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| BCL2L14 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| IRF2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.9 + PDB: 6NLQ, 6NLY, 6NOW | pLDDT=87.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion / Mitochondria | 一致 |
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
1. AARS2 — Alanine--tRNA ligase, mitochondrial，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小985 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124608-AARS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AARS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (enhanced)。来源: https://www.proteinatlas.org/ENSG00000124608-AARS2/subcellular

![](https://images.proteinatlas.org/35636/2275_F2_114_blue_red_green.jpg)
![](https://images.proteinatlas.org/35636/2275_F2_208_blue_red_green.jpg)
![](https://images.proteinatlas.org/35636/380_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35636/380_A8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35636/382_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35636/382_A8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JTZ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
