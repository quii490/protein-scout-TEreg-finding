---
type: protein-evaluation
gene: "C11orf58"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C11orf58 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C11orf58 / C11orf58 |
| 蛋白名称 | Small acidic protein |
| 蛋白大小 | 183 aa / 20.3 kDa |
| UniProt ID | O00193 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Endoplasmic reticulum; 额外: Nucleoplasm; UniProt: 无注释 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 183 aa / 20.3 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.4; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026714, IPR028124; Pfam: PF15477 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoplasm | Approved |
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
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf58 |

**关键文献**:
1. C11orf58 (Hero20) Gene Polymorphism: Contribution to Ischemic Stroke Risk and Interactions with Other Heat-Resistant Obscure Chaperones.. *Biomedicines*. PMID: 39595169
2. Gene-based GWAS analysis for consecutive studies of GEFOS.. *Osteoporosis international : a journal established as result of cooperation between the European Foundation for Osteoporosis and the National Osteoporosis Foundation of the USA*. PMID: 30306226
3. When Heroes Fall: Reduced Expression of Heat-Resistant Obscure Proteins in Ischemic Stroke.. *Neuromolecular medicine*. PMID: 40906246
4. Bioinformatic analysis of the regulatory potential of tagging SNPs provides evidence of the involvement of genes encoding the heat-resistant obscure (Hero) proteins in the pathogenesis of cardiovascular diseases.. *Journal of integrative bioinformatics*. PMID: 40459864

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.4 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 30.6% |
| 低置信 (pLDDT<50) 占比 | 27.3% |
| 有序区域 (pLDDT>70) 占比 | 42.1% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.4），有序残基占 42.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026714, IPR028124; Pfam: PF15477 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.866 | 0.000 | — |
| SUB1 | 0.778 | 0.000 | — |
| CDC123 | 0.612 | 0.000 | — |
| PTMA | 0.608 | 0.232 | — |
| CALM3 | 0.570 | 0.000 | — |
| SUMO2 | 0.554 | 0.000 | — |
| EMC4 | 0.524 | 0.000 | — |
| CALML4 | 0.523 | 0.000 | — |
| CALML5 | 0.523 | 0.000 | — |
| CALML6 | 0.523 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| MARK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| BMX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.4 + PDB: 无 | pLDDT=65.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Endoplasmic reticulum; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C11orf58 — Small acidic protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00193
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110696-C11orf58/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C11orf58
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00193
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:20:17

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000110696-C11orf58/subcellular

![](https://images.proteinatlas.org/76406/1692_A12_13_cr57d15aaac6360_red_green.jpg)
![](https://images.proteinatlas.org/76406/1692_A12_22_cr57d15ab1316e7_red_green.jpg)
![](https://images.proteinatlas.org/76406/1712_B10_32_red_green.jpg)
![](https://images.proteinatlas.org/76406/1712_B10_33_red_green.jpg)
![](https://images.proteinatlas.org/76406/1757_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/76406/1757_E3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00193-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
