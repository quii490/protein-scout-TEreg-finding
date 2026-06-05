---
type: protein-evaluation
gene: "LRRIQ3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRIQ3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRIQ3 / LRRC44 |
| 蛋白名称 | Leucine-rich repeat and IQ domain-containing protein 3 |
| 蛋白大小 | 624 aa / 73.7 kDa |
| UniProt ID | A6PVS8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 624 aa / 73.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001611, IPR052859, IPR032675 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
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
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LRRC44 |

**关键文献**:
1. Diagnostic Yield and Novel Candidate Genes by Exome Sequencing in 152 Consanguineous Families With Neurodevelopmental Disorders.. *JAMA psychiatry*. PMID: 28097321
2. SPHK2 Knockdown Inhibits the Proliferation and Migration of Fibroblast-Like Synoviocytes Through the IL-17 Signaling Pathway in Osteoarthritis.. *Journal of inflammation research*. PMID: 39416266
3. Identification of novel common variants associated with chronic pain using conditional false discovery rate analysis with major depressive disorder and assessment of pleiotropic effects of LRFN5.. *Translational psychiatry*. PMID: 31748543
4. Characterization of Korean Colorectal Cancer Reveals Novel Driver Gene and Clinically Relevant Mutations.. *MedComm*. PMID: 41522471
5. Transcription of a protein-coding gene on B chromosomes of the Siberian roe deer (Capreolus pygargus).. *BMC biology*. PMID: 23915065

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 35.9% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 31.7% |
| 有序区域 (pLDDT>70) 占比 | 61.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.1，有序区 61.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR052859, IPR032675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMC7 | 0.742 | 0.099 | — |
| FPGT | 0.736 | 0.100 | — |
| FAM227B | 0.734 | 0.000 | — |
| SAMD5 | 0.670 | 0.000 | — |
| TNNI3K | 0.657 | 0.100 | — |
| FPGT-TNNI3K | 0.649 | 0.100 | — |
| FRMD3 | 0.645 | 0.000 | — |
| ADGRL2 | 0.517 | 0.514 | — |
| ADGRL3 | 0.514 | 0.514 | — |
| ADGRL1 | 0.514 | 0.514 | — |

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
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 无 | pLDDT=70.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRIQ3 — Leucine-rich repeat and IQ domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小624 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6PVS8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162620-LRRIQ3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRIQ3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6PVS8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000162620-LRRIQ3/subcellular

![](https://images.proteinatlas.org/30799/1844_E9_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/30799/1844_E9_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/30799/402_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30799/402_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30799/409_D8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30799/409_D8_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6PVS8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
