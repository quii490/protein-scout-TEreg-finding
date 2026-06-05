---
type: protein-evaluation
gene: "C9orf152"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C9orf152 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C9orf152 |
| 蛋白名称 | Uncharacterized protein C9orf152 |
| 蛋白大小 | 239 aa / 26.3 kDa |
| UniProt ID | Q5JTZ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 239 aa / 26.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032738; Pfam: PF15733 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Key factors mediated by PI3K signaling pathway and related genes in endometrial carcinoma.. *Journal of bioenergetics and biomembranes*. PMID: 33159265
2. Identification of Key Genes and Pathways in Triple-Negative Breast Cancer by Integrated Bioinformatics Analysis.. *BioMed research international*. PMID: 30175120
3. An 8-Gene Signature for Classifying Major Subtypes of Non-Small-Cell Lung Cancer.. *Cancer informatics*. PMID: 35722224
4. A new risk stratification system of prostate cancer to identify high-risk biochemical recurrence patients.. *Translational andrology and urology*. PMID: 33457230
5. Analysis of gene expression and regulation implicates C2H9orf152 has an important role in calcium metabolism and chicken reproduction.. *Animal reproduction science*. PMID: 27889102

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.7 |
| 高置信度残基 (pLDDT>90) 占比 | 4.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 29.3% |
| 低置信 (pLDDT<50) 占比 | 45.2% |
| 有序区域 (pLDDT>70) 占比 | 25.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.7），有序残基占 25.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032738; Pfam: PF15733 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRR15L | 0.587 | 0.000 | — |
| SMKR1 | 0.506 | 0.000 | — |
| RAB30 | 0.480 | 0.000 | — |
| SLFNL1 | 0.474 | 0.000 | — |
| KIAA1324 | 0.463 | 0.000 | — |
| IL10RA | 0.456 | 0.000 | — |
| C1orf116 | 0.429 | 0.000 | — |
| KIAA0040 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 8，IntAct interactions: 0
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.7 + PDB: 无 | pLDDT=57.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 8 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C9orf152 — Uncharacterized protein C9orf152，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小239 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTZ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188959-C9orf152/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C9orf152
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTZ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188959-C9orf152/subcellular

![](https://images.proteinatlas.org/50769/1314_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/50769/1314_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/50769/1326_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/50769/1326_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/50769/1356_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/50769/1356_B2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JTZ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
