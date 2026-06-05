---
type: protein-evaluation
gene: "CIP2A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CIP2A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=326，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIP2A / KIAA1524 |
| 蛋白名称 | Protein CIP2A |
| 蛋白大小 | 905 aa / 102.2 kDa |
| UniProt ID | Q8TCG1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Plasma membrane, Centrosome, Basal body; UniProt: Cytoplasm; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 905 aa / 102.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=326 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.9; PDB: 5UFL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR042510, IPR048701; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **67.0/180** | |
| **归一化总分** | | | **37.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane, Centrosome, Basal body | Approved |
| UniProt | Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome (GO:0005694)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 326 |
| PubMed broad count | 418 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1524 |

**关键文献**:
1. Micropeptide CIP2A-BP encoded by LINC00665 inhibits triple-negative breast cancer progression.. *The EMBO journal*. PMID: 31755573
2. The CIP2A-TOPBP1 axis safeguards chromosome stability and is a synthetic lethal target for BRCA-mutated cancer.. *Nature cancer*. PMID: 35121901
3. Degradation-Based Protein Profiling: A Case Study of Celastrol.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38664976
4. CIP2A induces PKM2 tetramer formation and oxidative phosphorylation in non-small cell lung cancer.. *Cell discovery*. PMID: 38321019
5. The CIP2A-TOPBP1 complex safeguards chromosomal stability during mitosis.. *Nature communications*. PMID: 35842428

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 55.2% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 8.3% |
| 有序区域 (pLDDT>70) 占比 | 83.3% |
| 可用 PDB 条目 | 5UFL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.9，有序区 83.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR042510, IPR048701; Pfam: PF21044 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYC | 0.865 | 0.292 | — |
| PPP2R1A | 0.863 | 0.510 | — |
| PLK1 | 0.705 | 0.183 | — |
| PPME1 | 0.673 | 0.000 | — |
| MINK1 | 0.659 | 0.000 | — |
| KIF11 | 0.658 | 0.105 | — |
| SET | 0.657 | 0.000 | — |
| E2F1 | 0.654 | 0.000 | — |
| BRCA1 | 0.637 | 0.439 | — |
| SMC2 | 0.633 | 0.081 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12065|pubmed:17632056 |
| MYC | psi-mi:"MI:0096"(pull down) | imex:IM-12065|pubmed:17632056 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| FLT1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:23063127|imex:IM-18678 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| CCAR1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| IL1R2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 5UFL | pLDDT=83.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Chromosome / Cytosol; 额外: Plasma membrane, Centrosome, Basal bo | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CIP2A — Protein CIP2A，研究基础较多，新颖性有限。
2. 蛋白大小905 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 326 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163507-CIP2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIP2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCG1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000163507-CIP2A/subcellular

![](https://images.proteinatlas.org/39570/2146_F10_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/39570/2146_F10_79_blue_red_green.jpg)
![](https://images.proteinatlas.org/39570/2165_H3_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/39570/2165_H3_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/39570/2177_G3_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/39570/2177_G3_65_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TCG1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
