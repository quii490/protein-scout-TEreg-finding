---
type: protein-evaluation
gene: "MYF6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MYF6 — REJECTED (研究热度过高 (PubMed strict=194，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYF6 / BHLHC4, MRF4 |
| 蛋白名称 | Myogenic factor 6 |
| 蛋白大小 | 242 aa / 27.0 kDa |
| UniProt ID | P23409 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic spindle, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 27.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=194 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR002546, IPR039704; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic spindle, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- mitotic spindle (GO:0072686)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 194 |
| PubMed broad count | 268 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHC4, MRF4 |

**关键文献**:
1. Single-cell RNA-seq reveals novel interaction between muscle satellite cells and fibro-adipogenic progenitors mediated with FGF7 signalling.. *Journal of cachexia, sarcopenia and muscle*. PMID: 38751367
2. Porcine myogenesis in cloned wildtype and MYF5/MYOD/MYF6-null porcine embryo.. *Communications biology*. PMID: 39934347
3. Characterization of Myf6 and association with growth traits in swimming crab (Portunus trituberculatus).. *BMC genomics*. PMID: 39736553
4. Indoxyl sulfate inhibits muscle cell differentiation via Myf6/MRF4 and MYH2 downregulation.. *Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association*. PMID: 37349959
5. Porcine MYF6 gene: sequence, homology analysis, and variation in the promoter region.. *Animal biotechnology*. PMID: 15595701

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.2 |
| 高置信度残基 (pLDDT>90) 占比 | 26.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 37.2% |
| 有序区域 (pLDDT>70) 占比 | 41.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.2），有序残基占 41.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR002546, IPR039704; Pfam: PF01586, PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYF5 | 0.933 | 0.000 | — |
| MYOD1 | 0.927 | 0.000 | — |
| TCF3 | 0.925 | 0.655 | — |
| TCF12 | 0.912 | 0.636 | — |
| PAX3 | 0.900 | 0.000 | — |
| MYOG | 0.886 | 0.000 | — |
| MEF2A | 0.860 | 0.045 | — |
| TCF4 | 0.857 | 0.660 | — |
| PAX7 | 0.850 | 0.000 | — |
| MYH2 | 0.840 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=66.2 + PDB: 无 | pLDDT=66.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Mitotic spindle, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MYF6 — Myogenic factor 6，研究基础较多，新颖性有限。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 194 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 194 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23409
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111046-MYF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23409
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000111046-MYF6/subcellular

![](https://images.proteinatlas.org/65102/1692_G6_13_cr57d2aaa2e7748_red_green.jpg)
![](https://images.proteinatlas.org/65102/1692_G6_18_cr57d2aaaae7ad0_red_green.jpg)
![](https://images.proteinatlas.org/65102/1777_A3_33_red_green.jpg)
![](https://images.proteinatlas.org/65102/1777_A3_34_red_green.jpg)
![](https://images.proteinatlas.org/65102/1782_B6_15_cr596f4e0e126e3_red_green.jpg)
![](https://images.proteinatlas.org/65102/1782_B6_1_cr596f4e0e114b8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23409-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P23409 |
| SMART | SM00520;SM00353; |
| UniProt Domain [FT] | DOMAIN 93..144; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638;IPR002546;IPR039704; |
| Pfam | PF01586;PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111046-MYF6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TCF12 | Intact, Biogrid | true |
| TCF3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
