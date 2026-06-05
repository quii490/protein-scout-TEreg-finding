---
type: protein-evaluation
gene: "CERCAM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CERCAM — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERCAM / CEECAM1, GLT25D3, KIAA1502 |
| 蛋白名称 | Inactive glycosyltransferase 25 family member 3 |
| 蛋白大小 | 595 aa / 67.6 kDa |
| UniProt ID | Q5T4B2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 595 aa / 67.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050757, IPR002654, IPR029044; Pfam: PF01755 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CEECAM1, GLT25D3, KIAA1502 |

**关键文献**:
1. Spatial and single-cell transcriptomic analysis reveals fibroblasts dependent immune environment in colorectal cancer.. *BioFactors (Oxford, England)*. PMID: 40068177
2. Whole-genome sequencing reveals rare and structural variants contributing to psoriasis and identifies CERCAM as a risk gene.. *Cell genomics*. PMID: 40848718
3. Stromal PLAU mediates tumor progression and informs a novel therapeutic target in triple-negative breast cancer.. *Cancer cell international*. PMID: 40646496
4. Zika virus modulates blood-brain barrier of brain microvascular endothelial cells.. *Tropical biomedicine*. PMID: 33597462
5. Integrative single-cell and bulk RNA-seq analysis identifies glycosyltransferases-related signature in triple negative breast cancer.. *Functional & integrative genomics*. PMID: 41203941

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.8 |
| 高置信度残基 (pLDDT>90) 占比 | 76.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 89.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.8，有序区 89.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050757, IPR002654, IPR029044; Pfam: PF01755 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OS9 | 0.595 | 0.593 | — |
| LYPLA2 | 0.457 | 0.000 | — |
| LHPP | 0.445 | 0.000 | — |
| GOPC | 0.433 | 0.433 | — |
| GGH | 0.420 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q9UMW5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOPC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| INSL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLAMF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYZL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OS9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GEMIN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SFT2D1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FKBP7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZDHHC15 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 15
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.8 + PDB: 无 | pLDDT=88.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 5 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CERCAM — Inactive glycosyltransferase 25 family member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小595 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T4B2
- Protein Atlas: https://www.proteinatlas.org/search/CERCAM
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CERCAM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T4B2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000167123-CERCAM/subcellular

![](https://images.proteinatlas.org/51595/781_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/51595/781_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/51595/786_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/51595/786_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/51595/868_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/51595/868_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T4B2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
