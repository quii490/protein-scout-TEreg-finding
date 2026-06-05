---
type: protein-evaluation
gene: "GON7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GON7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GON7 |
| 蛋白名称 | EKC/KEOPS complex subunit GON7 |
| 蛋白大小 | 100 aa / 10.9 kDa |
| UniProt ID | Q9BXV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli rim; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 100 aa / 10.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.1; PDB: 6GWJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027893; Pfam: PF15387 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli rim | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- EKC/KEOPS complex (GO:0000408)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The structural and functional workings of KEOPS.. *Nucleic acids research*. PMID: 34614169
2. A paralog of Pcc1 is the fifth core subunit of the KEOPS tRNA-modifying complex in Archaea.. *Nature communications*. PMID: 36720870
3. Crystal structure of the human PRPK-TPRKB complex.. *Communications biology*. PMID: 33547416
4. Kae1 of Saccharomyces cerevisiae KEOPS complex possesses ADP/GDP nucleotidase activity.. *The Biochemical journal*. PMID: 36416748
5. Crystal structures of the Gon7/Pcc1 and Bud32/Cgi121 complexes provide a model for the complete yeast KEOPS complex.. *Nucleic acids research*. PMID: 25735745

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 37.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 39.0% |
| 低置信 (pLDDT<50) 占比 | 7.0% |
| 有序区域 (pLDDT>70) 占比 | 54.0% |
| 可用 PDB 条目 | 6GWJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.1，有序区 54.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027893; Pfam: PF15387 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OSGEP | 0.999 | 0.973 | — |
| TP53RK | 0.999 | 0.873 | — |
| LAGE3 | 0.999 | 0.981 | — |
| TPRKB | 0.999 | 0.361 | — |
| OSGEPL1 | 0.888 | 0.052 | — |
| YRDC | 0.763 | 0.000 | — |
| POLR1B | 0.628 | 0.000 | — |
| WDR73 | 0.471 | 0.000 | — |
| TMEM229B | 0.447 | 0.000 | — |
| TMEM131L | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6VW06 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-11969|pubmed:16564010 |
| CGI121 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BUD32 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| KAE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SET2 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| ESS1 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| RSP5 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| THG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| RPT5 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 1 / 10 = 10%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 6GWJ | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GON7 — EKC/KEOPS complex subunit GON7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小100 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170270-GON7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GON7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170270-GON7/subcellular

![](https://images.proteinatlas.org/51832/782_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/51832/782_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/51832/787_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/51832/787_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/51832/840_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/51832/840_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXV9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
