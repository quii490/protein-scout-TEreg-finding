---
type: protein-evaluation
gene: "CHCHD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHCHD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHCHD1 / C10orf34, MRPS37 |
| 蛋白名称 | Small ribosomal subunit protein mS37 |
| 蛋白大小 | 118 aa / 13.5 kDa |
| UniProt ID | Q96BP2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Mitochondria; 额外: Nucleoli fibrillar center, Cy; UniProt: Mitochondrion; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 118 aa / 13.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=92.4; PDB: 3J9M, 6NU2, 6NU3, 6RW4, 6RW5, 6VLZ, 6VMI |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR010625, IPR009069, IPR033620; Pfam: PF06747 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.5/180** | |
| **归一化总分** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria; 额外: Nucleoli fibrillar center, Cytosol | Supported |
| UniProt | Mitochondrion; Nucleus | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- mitochondrial inner membrane (GO:0005743)
- mitochondrial small ribosomal subunit (GO:0005763)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf34, MRPS37 |

**关键文献**:
1. Identification and characterization of CHCHD1, AURKAIP1, and CRIF1 as new members of the mammalian mitochondrial ribosome.. *Frontiers in physiology*. PMID: 23908630
2. Gene Regulation Network of Prognostic Biomarker YAP1 in Human Cancers: An Integrated Bioinformatics Study.. *Pathology oncology research : POR*. PMID: 34257617
3. Integration of summary data from GWAS and eQTL studies identified novel risk genes for coronary artery disease.. *Medicine*. PMID: 33725943
4. Identification and Validation of Reference Genes for RT-qPCR Studies of Hypoxia in Squamous Cervical Cancer Patients.. *PloS one*. PMID: 27244197
5. Coiled-coil-helix-coiled-coil-helix Domain Containing 1 Promotes Hepatocellular Carcinoma Progression by Regulating Transforming Growth Factor Beta Receptor 1 in the Tumor Immune Microenvironment.. *Genetic testing and molecular biomarkers*. PMID: 41022542

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 80.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 96.6% |
| 可用 PDB 条目 | 3J9M, 6NU2, 6NU3, 6RW4, 6RW5, 6VLZ, 6VMI, 6ZM5, 6ZM6, 6ZS9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3J9M, 6NU2, 6NU3, 6RW4, 6RW5, 6VLZ, 6VMI, 6ZM5, 6ZM6, 6ZS9）+ AlphaFold极高置信度预测（pLDDT=92.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010625, IPR009069, IPR033620; Pfam: PF06747 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| rev | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| C1QBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| FTH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| LYRM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| AURKAIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ALDH1L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| GLS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| MESD | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 3J9M, 6NU2, 6NU3, 6RW4, 6RW5,  | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Nucleus / Nucleoplasm, Mitochondria; 额外: Nucleoli fibrillar  | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CHCHD1 -- Small ribosomal subunit protein mS37，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小118 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172586-CHCHD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHCHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BP2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000172586-CHCHD1/subcellular

![](https://images.proteinatlas.org/39046/436_A10_4_red_green.jpg)
![](https://images.proteinatlas.org/39046/436_A10_6_red_green.jpg)
![](https://images.proteinatlas.org/39046/442_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/39046/442_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/39046/521_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/39046/521_A10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96BP2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
