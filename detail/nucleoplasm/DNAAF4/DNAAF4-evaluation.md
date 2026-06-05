---
type: protein-evaluation
gene: "DNAAF4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAAF4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAAF4 / DYX1C1, EKN1 |
| 蛋白名称 | Dynein axonemal assembly factor 4 |
| 蛋白大小 | 420 aa / 48.5 kDa |
| UniProt ID | Q8WXU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Mid piece; 额外: Plasma membrane, Connecting piece, P; UniProt: Nucleus; Cytoplasm; Dynein axonemal particle; Cell projectio |
| 蛋白大小 | 10/10 | ×1 | 10 | 420 aa / 48.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007052, IPR037894, IPR052004, IPR008978, IPR011 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **150.5/180** | |
| **归一化总分** | | | **83.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Mid piece; 额外: Plasma membrane, Connecting piece, Principal piece | Supported |
| UniProt | Nucleus; Cytoplasm; Dynein axonemal particle; Cell projection, neuron projection | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dynein axonemal particle (GO:0120293)
- extracellular region (GO:0005576)
- neuron projection (GO:0043005)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- sperm head-tail coupling apparatus (GO:0120212)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DYX1C1, EKN1 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. The prevalence of laterality defects in patients with congenital heart disease.. *Journal of human genetics*. PMID: 40467998
3. Whole genome sequencing enhances molecular diagnosis of primary ciliary dyskinesia.. *Pediatric pulmonology*. PMID: 39115449
4. Genetic and protein interaction studies between the ciliary dyslexia candidate genes DYX1C1 and DCDC2.. *BMC molecular and cell biology*. PMID: 37237337
5. Homozygous mutation in DNAAF4 causes primary ciliary dyskinesia in a Chinese family.. *Frontiers in genetics*. PMID: 36583018

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.6% |
| 置信残基 (pLDDT 70-90) 占比 | 33.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 86.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.9，有序区 86.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007052, IPR037894, IPR052004, IPR008978, IPR011990; Pfam: PF04969 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCDC2 | 0.978 | 0.000 | — |
| KIAA0319 | 0.972 | 0.000 | — |
| PIH1D3 | 0.961 | 0.057 | — |
| DNAAF3 | 0.901 | 0.000 | — |
| DNAAF2 | 0.883 | 0.206 | — |
| DNAAF1 | 0.861 | 0.051 | — |
| ROBO1 | 0.844 | 0.000 | — |
| LRRC6 | 0.825 | 0.065 | — |
| CFAP298 | 0.809 | 0.000 | — |
| ZMYND10 | 0.807 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3C | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| CALM1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DNAAF2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| BANF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MCC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CETN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 无 | pLDDT=83.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Dynein axonemal particle; Cell / Cytosol, Mid piece; 额外: Plasma membrane, Connectin | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAAF4 — Dynein axonemal assembly factor 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小420 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000256061-DNAAF4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAAF4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000256061-DNAAF4/subcellular

![](https://images.proteinatlas.org/51048/2147_E3_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/51048/2147_E3_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/51048/2161_H9_27_blue_red_green.jpg)
![](https://images.proteinatlas.org/51048/2161_H9_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/51048/2185_D9_27_blue_red_green.jpg)
![](https://images.proteinatlas.org/51048/2185_D9_52_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WXU2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
