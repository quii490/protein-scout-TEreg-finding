---
type: protein-evaluation
gene: "PRRG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRRG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRRG1 / PRGP1, TMG1 |
| 蛋白名称 | Transmembrane gamma-carboxyglutamic acid protein 1 |
| 蛋白大小 | 218 aa / 24.9 kDa |
| UniProt ID | O14668 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles, Plasma membrane; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 218 aa / 24.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017857, IPR035972, IPR000294, IPR050442; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular space (GO:0005615)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRGP1, TMG1 |

**关键文献**:
1. MiR-17-92 cluster promotes hepatocarcinogenesis.. *Carcinogenesis*. PMID: 26233958
2. Vitamin K-dependent gamma-carboxyglutamic acid protein 1 promotes pancreatic ductal adenocarcinoma progression through stabilizing oncoprotein KRAS and tyrosine kinase receptor EGFR.. *Clinical and translational medicine*. PMID: 39843398
3. Identification of a 6-gene signature for the survival prediction of breast cancer patients based on integrated multi-omics data analysis.. *PloS one*. PMID: 33170908
4. Apoptosis, cell cycle progression and gene expression in TP53-depleted HCT116 colon cancer cells in response to short-term 5-fluorouracil treatment.. *International journal of oncology*. PMID: 17982676
5. Screening, validation, and transcriptional regulation analysis of oxidative stress-related biomarkers in gestational diabetes mellitus: SH3BP5, ITGAM, PRRG1, and MIS12.. *European journal of medical research*. PMID: 41787525

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.2% |
| 中等置信 (pLDDT 50-70) 占比 | 18.3% |
| 低置信 (pLDDT<50) 占比 | 30.3% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017857, IPR035972, IPR000294, IPR050442; Pfam: PF00594 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GGCX | 0.940 | 0.165 | — |
| UCMA | 0.595 | 0.000 | — |
| LANCL3 | 0.583 | 0.000 | — |
| YAP1 | 0.531 | 0.165 | — |
| MGP | 0.479 | 0.000 | — |
| TMEM47 | 0.467 | 0.000 | — |
| DYNLT3 | 0.435 | 0.000 | — |
| RFFL | 0.432 | 0.000 | — |
| SLC44A1 | 0.422 | 0.000 | — |
| CMTM3 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UQCRH | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NEDD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FBXO10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DCAF10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STXBP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITCH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEDD4L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WWP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HECW2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 12
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 无 | pLDDT=67.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Vesicles, Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 12 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRRG1 — Transmembrane gamma-carboxyglutamic acid protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小218 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14668
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130962-PRRG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRRG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14668
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000130962-PRRG1/subcellular

![](https://images.proteinatlas.org/78129/1672_C5_31_red_green.jpg)
![](https://images.proteinatlas.org/78129/1672_C5_32_red_green.jpg)
![](https://images.proteinatlas.org/78129/1690_E7_3_red_green.jpg)
![](https://images.proteinatlas.org/78129/1690_E7_5_red_green.jpg)
![](https://images.proteinatlas.org/78129/1703_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/78129/1703_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14668-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
