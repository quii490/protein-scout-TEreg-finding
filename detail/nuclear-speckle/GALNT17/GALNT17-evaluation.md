---
type: protein-evaluation
gene: "GALNT17"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GALNT17 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GALNT17 / GALNT17 |
| 蛋白名称 | Polypeptide N-acetylgalactosaminyltransferase-like 6 |
| 蛋白大小 | 601 aa / 69.8 kDa |
| UniProt ID | Q49A17 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Nuclear bodies; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 601 aa / 69.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Nuclear bodies | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GALNT17 |

**关键文献**:
1. Galnt17 loss-of-function leads to developmental delay and abnormal coordination, activity, and social interactions with cerebellar vermis pathology.. *Developmental biology*. PMID: 36002036
2. A Mouse Mutation That Dysregulates Neighboring Galnt17 and Auts2 Genes Is Associated with Phenotypes Related to the Human AUTS2 Syndrome.. *G3 (Bethesda, Md.)*. PMID: 31554716
3. A genome-wide association study reveals specific transferases as candidate loci for bovine milk oligosaccharides synthesis.. *BMC genomics*. PMID: 31117955
4. WBSCR Locus: At the Crossroads of Human Behavioral Disorders and Domestication of Animals.. *International journal of molecular sciences*. PMID: 40943469
5. DCMS analysis revealed differential selection signatures in the transboundary Sahiwal cattle for major economic traits.. *Scientific reports*. PMID: 40325078

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.9 |
| 高置信度残基 (pLDDT>90) 占比 | 80.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 5.3% |
| 有序区域 (pLDDT>70) 占比 | 92.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.9，有序区 92.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000772; Pfam: PF00535, PF00652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| B3GNT6 | 0.922 | 0.000 | — |
| GCNT1 | 0.921 | 0.000 | — |
| ST6GALNAC1 | 0.916 | 0.000 | — |
| C1GALT1 | 0.734 | 0.000 | — |
| C1GALT1C1 | 0.705 | 0.000 | — |
| C1GALT1C1L | 0.669 | 0.000 | — |
| CALN1 | 0.556 | 0.000 | — |
| AUTS2 | 0.486 | 0.000 | — |
| DLGAP4 | 0.471 | 0.000 | — |
| KCNK12 | 0.445 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.9 + PDB: 无 | pLDDT=90.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Nuclea | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GALNT17 — Polypeptide N-acetylgalactosaminyltransferase-like 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小601 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49A17
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185274-GALNT17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GALNT17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49A17
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000185274-GALNT17/subcellular

![](https://images.proteinatlas.org/47986/1296_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47986/1296_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47986/1364_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47986/1364_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47986/1595_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47986/1595_G5_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49A17-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
