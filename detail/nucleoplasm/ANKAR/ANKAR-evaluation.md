---
type: protein-evaluation
gene: "ANKAR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKAR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKAR |
| 蛋白名称 | Ankyrin and armadillo repeat-containing protein |
| 蛋白大小 | 1434 aa / 162.0 kDa |
| UniProt ID | Q7Z5J8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centriolar satellite; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1434 aa / 162.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043379, IPR002110, IPR036770, IPR011989, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A large-scale proteomics resource of circulating extracellular vesicles for biomarker discovery in pancreatic cancer.. *eLife*. PMID: 39693144
2. Sequence-based GWAS meta-analyses for beef production traits.. *Genetics, selection, evolution : GSE*. PMID: 37828440
3. A Large-Scale Proteomics Resource of Circulating Extracellular Vesicles for Biomarker Discovery in Pancreatic Cancer.. *medRxiv : the preprint server for health sciences*. PMID: 36993200
4. Hemizygous deletion of COL3A1, COL5A2, and MSTN causes a complex phenotype with aortic dissection: a lesson for and from true haploinsufficiency.. *European journal of human genetics : EJHG*. PMID: 20648054

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.9% |
| 置信残基 (pLDDT 70-90) 占比 | 36.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 89.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.8，有序区 89.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043379, IPR002110, IPR036770, IPR011989, IPR016024; Pfam: PF12796, PF00514 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OSGEPL1 | 0.932 | 0.000 | — |
| TMF1 | 0.820 | 0.000 | — |
| NEMP2 | 0.675 | 0.000 | — |
| ORMDL1 | 0.614 | 0.049 | — |
| WDR75 | 0.523 | 0.000 | — |
| IGFALS | 0.510 | 0.093 | — |
| DIRC1 | 0.507 | 0.000 | — |
| PMS1 | 0.490 | 0.000 | — |
| USF3 | 0.480 | 0.079 | — |
| AK9 | 0.467 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.8 + PDB: 无 | pLDDT=84.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Centriolar satellite; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. ANKAR — Ankyrin and armadillo repeat-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1434 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z5J8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151687-ANKAR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKAR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z5J8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centriolar satellite (approved)。来源: https://www.proteinatlas.org/ENSG00000151687-ANKAR/subcellular

![](https://images.proteinatlas.org/36168/434_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36168/434_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36168/450_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36168/450_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36168/453_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36168/453_E8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z5J8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
