---
type: protein-evaluation
gene: "BTF3L4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BTF3L4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTF3L4 |
| 蛋白名称 | Transcription factor BTF3 homolog 4 |
| 蛋白大小 | 158 aa / 17.3 kDa |
| UniProt ID | Q96K17 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 158 aa / 17.3 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.1; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039370, IPR038187, IPR002715; Pfam: PF01849 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) |  |

**关键文献**:
1. MIR194-2HG, a miRNA host gene activated by HNF4A, inhibits gastric cancer by regulating microRNA biogenesis.. *Biology direct*. PMID: 39425187
2. Basic Transcription Factor 3 Like 4 Enhances Malignant Phenotypes through Modulating Tumor Cell Function and Immune Microenvironment in Glioma.. *The American journal of pathology*. PMID: 38320629
3. Dephosphorylation of the transcriptional cofactor NACA by the PP1A phosphatase enhances cJUN transcriptional activity and osteoblast differentiation.. *The Journal of biological chemistry*. PMID: 30948508
4. Quantitative proteomics analysis of chondrogenic differentiation of C3H10T1/2 mesenchymal stem cells by iTRAQ labeling coupled with on-line two-dimensional LC/MS/MS.. *Molecular & cellular proteomics : MCP*. PMID: 20008835
5. Genome-wide association studies identify miRNA-194 as a prognostic biomarker for gastrointestinal cancer by targeting ATP6V1F, PPP1R14B, BTF3L4 and SLC7A5.. *Frontiers in oncology*. PMID: 36620589

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.1 |
| 高置信度残基 (pLDDT>90) 占比 | 39.9% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 24.1% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 67.1% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.1，有序区 67.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039370, IPR038187, IPR002715; Pfam: PF01849 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NACA | 0.970 | 0.904 | — |
| NACA2 | 0.915 | 0.734 | — |
| NACAD | 0.879 | 0.621 | — |
| RPL31 | 0.843 | 0.548 | — |
| NUP93 | 0.836 | 0.809 | — |
| NUP205 | 0.795 | 0.771 | — |
| NUP155 | 0.774 | 0.771 | — |
| RPL23A | 0.748 | 0.545 | — |
| BTF3 | 0.747 | 0.709 | — |
| RPS19 | 0.740 | 0.185 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-6095589 | psi-mi:"MI:0096"(pull down) | pubmed:21712045|imex:IM-17900 |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| PB2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| SMYD2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| TXLNA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Rpl35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TXLNB | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| DCTN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.1 + PDB: 无 | pLDDT=78.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BTF3L4 — Transcription factor BTF3 homolog 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96K17
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134717-BTF3L4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTF3L4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96K17
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:18:38

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000134717-BTF3L4/subcellular

![](https://images.proteinatlas.org/67026/1213_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/67026/1213_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/67026/1235_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/67026/1235_A12_6_red_green.jpg)
![](https://images.proteinatlas.org/67026/1238_D12_7_red_green.jpg)
![](https://images.proteinatlas.org/67026/1238_D12_8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96K17-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
