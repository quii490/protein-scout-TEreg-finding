---
type: protein-evaluation
gene: "CHST7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHST7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHST7 |
| 蛋白名称 | Carbohydrate sulfotransferase 7 |
| 蛋白大小 | 486 aa / 54.3 kDa |
| UniProt ID | Q9NS84 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 486 aa / 54.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.3; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR016469, IPR051135, IPR027417, IPR000863; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 27 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CHST7 Gene Methylation and Sex-Specific Effects on Colorectal Cancer Risk.. *Digestive diseases and sciences*. PMID: 30815821
2. CHST7 Methylation Status Related to the Proliferation and Differentiation of Pituitary Adenomas.. *Cells*. PMID: 35954244
3. Genome Sequencing Identifies 13 Novel Candidate Risk Genes for Autism Spectrum Disorder in a Qatari Cohort.. *International journal of molecular sciences*. PMID: 39519104
4. Role of the X Chromosome in Alzheimer Disease Genetics.. *JAMA neurology*. PMID: 39250132
5. Human drug metabolism genes in parathion-and estrogen-treated breast cells.. *International journal of molecular medicine*. PMID: 17982697

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.3 |
| 高置信度残基 (pLDDT>90) 占比 | 55.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 18.7% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.3，有序区 70.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016469, IPR051135, IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRBOX4 | 0.952 | 0.000 | — |
| CHST3 | 0.928 | 0.000 | — |
| SLC9A7 | 0.848 | 0.000 | — |
| ZNF674 | 0.842 | 0.000 | — |
| CHST12 | 0.811 | 0.000 | — |
| CHST13 | 0.811 | 0.000 | — |
| CHST15 | 0.772 | 0.000 | — |
| CSGALNACT2 | 0.702 | 0.000 | — |
| CHST14 | 0.699 | 0.000 | — |
| CHST11 | 0.673 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PEX19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LCN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM74 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| C1orf54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| C1QTNF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CEACAM8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HFE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLEC12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCGB2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TTMP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.3 + PDB: 无 | pLDDT=79.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHST7 -- Carbohydrate sulfotransferase 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS84
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147119-CHST7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHST7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS84
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000147119-CHST7/subcellular

![](https://images.proteinatlas.org/30503/1829_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/30503/1829_F10_3_red_green.jpg)
![](https://images.proteinatlas.org/30503/1869_F6_45_cr5b758fbf12202_red_green.jpg)
![](https://images.proteinatlas.org/30503/1869_F6_47_cr5b758fbf1266f_red_green.jpg)
![](https://images.proteinatlas.org/30503/1905_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/30503/1905_D5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NS84-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NS84 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016469;IPR051135;IPR027417;IPR000863; |
| Pfam | PF00685; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147119-CHST7/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
