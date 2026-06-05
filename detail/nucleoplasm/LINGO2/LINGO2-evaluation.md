---
type: protein-evaluation
gene: "LINGO2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LINGO2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LINGO2 / LERN3, LRRN6C |
| 蛋白名称 | Leucine-rich repeat and immunoglobulin-like domain-containing nogo receptor-interacting protein 2 |
| 蛋白大小 | 606 aa / 68.1 kDa |
| UniProt ID | Q7L985 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytoplasmic bodies; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 606 aa / 68.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007110, IPR036179, IPR013783, IPR013098, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytoplasmic bodies; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- glutamatergic synapse (GO:0098978)
- plasma membrane (GO:0005886)
- synaptic membrane (GO:0097060)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LERN3, LRRN6C |

**关键文献**:
1. Mettl3 regulates the pathogenesis of Alzheimer's disease via fine-tuning Lingo2.. *Molecular psychiatry*. PMID: 40169805
2. Soluble form of Lingo2, an autism spectrum disorder-associated molecule, functions as an excitatory synapse organizer in neurons.. *Translational psychiatry*. PMID: 39443477
3. LINGO1 and LINGO2 variants are associated with essential tremor and Parkinson disease.. *Neurogenetics*. PMID: 20369371
4. Variations in the LINGO2 and GLIS3 Genes and Gene-Environment Interactions Increase Gestational Diabetes Mellitus Risk in Chinese Women.. *Environmental science & technology*. PMID: 38888423
5. Analysis and meta-analysis of five polymorphisms of the LINGO1 and LINGO2 genes in Parkinson's disease and multiple system atrophy in a Chinese population.. *Journal of neurology*. PMID: 26254004

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.8 |
| 高置信度残基 (pLDDT>90) 占比 | 69.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 83.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.8，有序区 83.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR013098, IPR003599; Pfam: PF07679, PF00560, PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TFF3 | 0.741 | 0.000 | — |
| RTN4R | 0.734 | 0.000 | — |
| MOB3B | 0.614 | 0.000 | — |
| TBPL1 | 0.598 | 0.000 | — |
| MTIF3 | 0.584 | 0.000 | — |
| POC5 | 0.580 | 0.000 | — |
| SEC16B | 0.576 | 0.053 | — |
| FPGT-TNNI3K | 0.572 | 0.100 | — |
| TMEM160 | 0.570 | 0.000 | — |
| TNNI3K | 0.560 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LINGO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GAPDHS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC34A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAXD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STK11IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CNPY3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMAN2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.8 + PDB: 无 | pLDDT=84.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Cytoplasmic bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LINGO2 — Leucine-rich repeat and immunoglobulin-like domain-containing nogo receptor-interacting protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小606 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L985
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174482-LINGO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LINGO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L985
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytoplasmic bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000174482-LINGO2/subcellular

![](https://images.proteinatlas.org/16633/1835_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16633/1835_A2_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L985-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
