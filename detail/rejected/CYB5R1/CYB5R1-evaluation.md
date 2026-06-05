---
type: protein-evaluation
gene: "CYB5R1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYB5R1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYB5R1 / NQO3A2 |
| 蛋白名称 | NADH-cytochrome b5 reductase 1 |
| 蛋白大小 | 305 aa / 34.1 kDa |
| UniProt ID | Q9UHQ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 305 aa / 34.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001834, IPR008333, IPR017927, IPR001709, IPR039 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)
- plasma membrane (GO:0005886)
- platelet alpha granule membrane (GO:0031092)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NQO3A2 |

**关键文献**:
1. Identification of Myelin Basic Protein Proximity Interactome Using TurboID Labeling Proteomics.. *Cells*. PMID: 36980286
2. TRAP1 Improves Diabetic Retinopathy by Preserving Mitochondrial Function.. *Clinical ophthalmology (Auckland, N.Z.)*. PMID: 40689237
3. CYB5R1 is a potential biomarker that correlates with stemness and drug resistance in gastric cancer.. *Translational oncology*. PMID: 37844477
4. Identification of cuproptosis-related genes related to the progression of ankylosing spondylitis by integrated bioinformatics analysis.. *Medicine*. PMID: 39213249
5. Identification and validation of feature genes of acute myocardial infarction based on ferroptosis-related genes.. *European journal of medical research*. PMID: 41068967

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.4 |
| 高置信度残基 (pLDDT>90) 占比 | 87.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 95.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.4，有序区 95.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001834, IPR008333, IPR017927, IPR001709, IPR039261; Pfam: PF00970, PF00175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYB5B | 0.995 | 0.286 | — |
| CYB5A | 0.993 | 0.111 | — |
| SUOX | 0.948 | 0.000 | — |
| DHODH | 0.923 | 0.469 | — |
| DPYD | 0.877 | 0.469 | — |
| UMPS | 0.854 | 0.000 | — |
| SCD | 0.820 | 0.000 | — |
| FDXR | 0.726 | 0.456 | — |
| POR | 0.709 | 0.071 | — |
| CPS1 | 0.614 | 0.048 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| vpu | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| MFSD8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:0096"(pull down) | pubmed:31964889|imex:IM-27520 |
| SH2D3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| SGTA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HIGD1C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TTC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| KCNA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.4 + PDB: 无 | pLDDT=94.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Mitochondria; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CYB5R1 — NADH-cytochrome b5 reductase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小305 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHQ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159348-CYB5R1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYB5R1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHQ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000159348-CYB5R1/subcellular

![](https://images.proteinatlas.org/10531/1853_D9_57_cr5afd739a20508_blue_red_green.jpg)
![](https://images.proteinatlas.org/10531/1853_D9_62_cr5afd739a1fb0b_blue_red_green.jpg)
![](https://images.proteinatlas.org/10531/1901_K13_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10531/1901_K13_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/10531/2087_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10531/2087_G12_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHQ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
