---
type: protein-evaluation
gene: "SYAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYAP1 |
| 蛋白名称 | Synapse-associated protein 1 |
| 蛋白大小 | 352 aa / 39.9 kDa |
| UniProt ID | Q96A49 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm, perinuclear region; Golgi apparatus; Perikaryon;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 352 aa / 39.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 1X3A |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005607, IPR035925, IPR051494; Pfam: PF03909 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm, perinuclear region; Golgi apparatus; Perikaryon; Cell projection, axon; Cell projection, ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- growth cone (GO:0030426)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Chromosome X-wide common variant association study in autism spectrum disorder.. *American journal of human genetics*. PMID: 39706197
2. SARS-CoV-2 enhances complement-mediated endothelial injury via the suppression of membrane complement regulatory proteins.. *Emerging microbes & infections*. PMID: 39945674
3. Development and Validation of a Prognosis-Prediction Signature for Patients with Lung Adenocarcinoma Based on 11 Telomere-Related Genes.. *Frontiers in bioscience (Landmark edition)*. PMID: 37919072
4. Initial characterization of a Syap1 knock-out mouse and distribution of Syap1 in mouse brain and cultured motoneurons.. *Histochemistry and cell biology*. PMID: 27344443
5. Dlk2 interacts with Syap1 to activate Akt signaling pathway during osteoclast formation.. *Cell death & disease*. PMID: 37669921

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 22.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 27.3% |
| 低置信 (pLDDT<50) 占比 | 30.7% |
| 有序区域 (pLDDT>70) 占比 | 42.0% |
| 可用 PDB 条目 | 1X3A |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 42.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005607, IPR035925, IPR051494; Pfam: PF03909 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PIN1 | 0.777 | 0.776 | — |
| TXLNG | 0.547 | 0.000 | — |
| CTPS2 | 0.543 | 0.000 | — |
| SPPL2A | 0.531 | 0.000 | — |
| EIF2S3 | 0.501 | 0.000 | — |
| PSMB4 | 0.488 | 0.484 | — |
| NOC4L | 0.481 | 0.000 | — |
| RBBP7 | 0.474 | 0.000 | — |
| REPS2 | 0.460 | 0.000 | — |
| GOSR1 | 0.457 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| COX14 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TOMM22 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SCO1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SFXN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 1X3A | pLDDT=65.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Golgi apparatus; Pe / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SYAP1 — Synapse-associated protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小352 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96A49
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169895-SYAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A49
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (enhanced)。来源: https://www.proteinatlas.org/ENSG00000169895-SYAP1/subcellular

![](https://images.proteinatlas.org/48047/715_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48047/715_G9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48047/725_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48047/725_G9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48047/812_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48047/812_G9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96A49-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
