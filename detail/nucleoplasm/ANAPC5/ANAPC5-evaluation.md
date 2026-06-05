---
type: protein-evaluation
gene: "ANAPC5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANAPC5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANAPC5 / APC5 |
| 蛋白名称 | Anaphase-promoting complex subunit 5 |
| 蛋白大小 | 755 aa / 85.1 kDa |
| UniProt ID | Q9UJX4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytoskeleton, spindle |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 755 aa / 85.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.6; PDB: 4UI9, 5A31, 5G04, 5G05, 5KHR, 5KHU, 5L9T |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037679, IPR026000, IPR048968, IPR011990, IPR019 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分 (÷1.83)** | | | **78.1/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- anaphase-promoting complex (GO:0005680)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APC5 |

**关键文献**:
1. The anaphase-promoting complex protein 5 (AnapC5) associates with A20 and inhibits IL-17-mediated signal transduction.. *PloS one*. PMID: 23922952
2. The role of CAMKK2 polymorphisms in HIV-associated sensory neuropathy in South Africans.. *Journal of the neurological sciences*. PMID: 32585444
3. Expression and prognostic value of cell-cycle-associated genes in lung squamous cell carcinoma.. *The journal of gene medicine*. PMID: 39171952
4. PTTG1 as a common promising target for PCOS, Ovarian Cancer, and Major Depressive Disorder patients.. *Computational biology and chemistry*. PMID: 40925190
5. Unraveling the molecular pathogenesis of Type 2 Diabetes and its impact on female infertility: A bioinformatics and systems biology approach.. *Computers in biology and medicine*. PMID: 39116715

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.6 |
| 高置信度残基 (pLDDT>90) 占比 | 40.1% |
| 置信残基 (pLDDT 70-90) 占比 | 42.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 82.6% |
| 可用 PDB 条目 | 4UI9, 5A31, 5G04, 5G05, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW, 6Q6G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4UI9, 5A31, 5G04, 5G05, 5KHR, 5KHU, 5L9T, 5L9U, 5LCW, 6Q6G）+ AlphaFold预测（pLDDT=81.6），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037679, IPR026000, IPR048968, IPR011990, IPR019734; Pfam: PF12862, PF21371 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANAPC15 | 0.999 | 0.965 | — |
| FZR1 | 0.999 | 0.999 | — |
| ANAPC10 | 0.999 | 0.999 | — |
| ANAPC7 | 0.999 | 0.998 | — |
| ANAPC1 | 0.999 | 0.999 | — |
| CDC27 | 0.999 | 0.998 | — |
| ANAPC4 | 0.999 | 0.999 | — |
| CDC20 | 0.999 | 0.999 | — |
| ANAPC11 | 0.999 | 0.966 | — |
| ANAPC13 | 0.999 | 0.987 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BACH1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| anapc5.L | psi-mi:"MI:0030"(cross-linking study) | pubmed:20951947|imex:IM-15161 |
| MGC80529 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:20951947|imex:IM-15161 |
| PTEN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15335|pubmed:21241890 |
| CDC27 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15335|pubmed:21241890 |
| Anapc16 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cdc26 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.6 + PDB: 4UI9, 5A31, 5G04, 5G05, 5KHR,  | pLDDT=81.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, spindle / Nucleoplasm | 一致 |
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
1. ANAPC5 — Anaphase-promoting complex subunit 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小755 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJX4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089053-ANAPC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANAPC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJX4
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:50:20

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000089053-ANAPC5/subcellular

![](https://images.proteinatlas.org/39801/1038_D6_4_red_green.jpg)
![](https://images.proteinatlas.org/39801/1038_D6_5_red_green.jpg)
![](https://images.proteinatlas.org/39801/1040_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/39801/1040_D6_4_red_green.jpg)
![](https://images.proteinatlas.org/39801/1137_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/39801/1137_E12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJX4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
