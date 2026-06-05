---
type: protein-evaluation
gene: "CHST1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHST1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHST1 |
| 蛋白名称 | Carbohydrate sulfotransferase 1 |
| 蛋白大小 | 411 aa / 46.7 kDa |
| UniProt ID | O43916 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Mitochondria; 额外: Nucleoli; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 411 aa / 46.7 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.4; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR016469, IPR051135, IPR027417, IPR000863; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 53 |
| 别名(未计入scoring) |  |

**关键文献**:
1. ACAN, MDFI, and CHST1 as Candidate Genes in Gastric Cancer: A Comprehensive Insilco Analysis.. *Asian Pacific journal of cancer prevention : APJCP*. PMID: 35225482
2. Glucocorticoids, genes and brain function.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 29180230
3. Airway glycomic and allergic inflammatory consequences resulting from keratan sulfate galactose 6-O-sulfotransferase (CHST1) deficiency.. *Glycobiology*. PMID: 29659839
4. Sulfation of O-glycans on Mucin-type Proteins From Serous Ovarian Epithelial Tumors.. *Molecular & cellular proteomics : MCP*. PMID: 34555499
5. Bioinformatics-Based Identification and Clinical Validation of CHST1 as a Potential Prognostic Gene Associated With EMT in Gastric Cancer.. *Frontiers in bioscience (Landmark edition)*. PMID: 41914286

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 69.6% |
| 置信残基 (pLDDT 70-90) 占比 | 16.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 85.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.4，有序区 85.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016469, IPR051135, IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LUM | 0.847 | 0.000 | — |
| KERA | 0.829 | 0.000 | — |
| SULT1C3 | 0.756 | 0.000 | — |
| SULT1C4 | 0.729 | 0.000 | — |
| SULT1B1 | 0.722 | 0.000 | — |
| NTAN1 | 0.636 | 0.000 | — |
| CHST9 | 0.538 | 0.000 | — |
| B3GNT7 | 0.499 | 0.000 | — |
| ACAN | 0.493 | 0.000 | — |
| GCNT1 | 0.491 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SFN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SNU13 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| STOM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GPX8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 无 | pLDDT=87.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Mitochondria; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHST1 -- Carbohydrate sulfotransferase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小411 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43916
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175264-CHST1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHST1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43916
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43916-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
