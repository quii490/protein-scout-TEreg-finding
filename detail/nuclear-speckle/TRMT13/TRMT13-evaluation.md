---
type: protein-evaluation
gene: "TRMT13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRMT13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRMT13 / CCDC76 |
| 蛋白名称 | tRNA:m(4)X modification enzyme TRM13 homolog |
| 蛋白大小 | 481 aa / 54.2 kDa |
| UniProt ID | Q9NUP7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; 额外: Nuclear bodies, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 481 aa / 54.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007871, IPR039044, IPR022776, IPR021721; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Nuclear bodies, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC76 |

**关键文献**:
1. TRMT13 inhibits the growth of papillary thyroid cancer by targeting ANAPC4.. *Acta biochimica et biophysica Sinica*. PMID: 38425244
2. [Whole Exome Sequencing Reveals Gene Mutation Characteristics of Primary Central Nervous System Lymphoma].. *Zhongguo shi yan xue ye xue za zhi*. PMID: 38926963
3. Identification of Mild Cognitive Impairment Subtypes using an Interpretable Neural Network based Clustering of Gene Expression Data and Neuroimaging Markers.. *Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference*. PMID: 38082666

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 53.4% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 18.7% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.2，有序区 74.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007871, IPR039044, IPR022776, IPR021721; Pfam: PF05206, PF11722, PF05253 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRMT11 | 0.657 | 0.000 | — |
| DIMT1 | 0.648 | 0.000 | — |
| LRRC39 | 0.609 | 0.000 | — |
| TRMT44 | 0.597 | 0.000 | — |
| RTCA | 0.584 | 0.000 | — |
| CMTR2 | 0.583 | 0.000 | — |
| C5orf22 | 0.579 | 0.000 | — |
| SAYSD1 | 0.577 | 0.000 | — |
| TRMT61A | 0.565 | 0.000 | — |
| DBT | 0.551 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STAG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OSER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DHRS2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Hacd3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| USF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| AGO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| MAGEA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GRIP2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PALS2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 无 | pLDDT=79.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Plasma membrane; 额外: Nuclear bodies,  | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRMT13 — tRNA:m(4)X modification enzyme TRM13 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小481 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUP7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122435-TRMT13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRMT13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUP7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000122435-TRMT13/subcellular

![](https://images.proteinatlas.org/28494/254_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/28494/254_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/28494/291_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/28494/291_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/28494/546_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/28494/546_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NUP7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NUP7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007871;IPR039044;IPR022776;IPR021721; |
| Pfam | PF05206;PF11722;PF05253; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000122435-TRMT13/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
