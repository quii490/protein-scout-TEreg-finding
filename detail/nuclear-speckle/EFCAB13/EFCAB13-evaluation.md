---
type: protein-evaluation
gene: "EFCAB13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFCAB13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFCAB13 / C17orf57 |
| 蛋白名称 | EF-hand calcium-binding domain-containing protein 13 |
| 蛋白大小 | 973 aa / 110.1 kDa |
| UniProt ID | Q8IY85 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 973 aa / 110.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear speckles | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf57 |

**关键文献**:
1. Genetic risk variants for multiple sclerosis are linked to differences in alternative pre-mRNA splicing.. *Frontiers in immunology*. PMID: 36405756
2. Genomic Analysis Using Regularized Regression in High-Grade Serous Ovarian Cancer.. *Cancer informatics*. PMID: 29434467
3. Effect of mechanical unloading on genome-wide DNA methylation profile of the failing human heart.. *JCI insight*. PMID: 36656640
4. Contribution of Rare and Low-Frequency Variants to Multiple Sclerosis Susceptibility in the Italian Continental Population.. *Frontiers in genetics*. PMID: 35047017
5. Associations between catechol-O-methyltransferase (COMT) genotypes at rs4818 and rs4680 and gene expression in human dorsolateral prefrontal cortex.. *Experimental brain research*. PMID: 31960101

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 34.0% |
| 中等置信 (pLDDT 50-70) 占比 | 19.3% |
| 低置信 (pLDDT<50) 占比 | 46.7% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.3），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LYRM4 | 0.595 | 0.595 | — |
| NFS1 | 0.584 | 0.584 | — |
| NPIPB8 | 0.530 | 0.116 | — |
| CDRT15L2 | 0.507 | 0.000 | — |
| RFPL1 | 0.498 | 0.000 | — |
| CAMK2B | 0.495 | 0.416 | — |
| CAMK2D | 0.495 | 0.416 | — |
| CAMK2A | 0.495 | 0.416 | — |
| EFCAB3 | 0.492 | 0.000 | — |
| CCDC144A | 0.491 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1R10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LYRM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZC3H4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NFS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.3 + PDB: 无 | pLDDT=53.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EFCAB13 — EF-hand calcium-binding domain-containing protein 13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小973 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=53.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IY85
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178852-EFCAB13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFCAB13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY85
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000178852-EFCAB13/subcellular

![](https://images.proteinatlas.org/21633/1749_D5_23_cr5804c0e80081f_red_green.jpg)
![](https://images.proteinatlas.org/21633/1749_D5_28_cr5804c0f209d00_red_green.jpg)
![](https://images.proteinatlas.org/21633/1788_E1_19_cr596df0e546610_red_green.jpg)
![](https://images.proteinatlas.org/21633/1788_E1_1_cr596df0e545fa0_red_green.jpg)
![](https://images.proteinatlas.org/21633/191_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/21633/191_A5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IY85-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
