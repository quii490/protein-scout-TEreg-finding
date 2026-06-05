---
type: protein-evaluation
gene: "PLAAT5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLAAT5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLAAT5 / HRASLS5, HRLP5 |
| 蛋白名称 | Phospholipase A and acyltransferase 5 |
| 蛋白大小 | 279 aa / 30.3 kDa |
| UniProt ID | Q96KN8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 279 aa / 30.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051496, IPR007053; Pfam: PF04970 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HRASLS5, HRLP5 |

**关键文献**:
1. Comprehensive variant analysis of phospholipase A2 superfamily genes in large Chinese Parkinson' s disease cohorts.. *Mechanisms of ageing and development*. PMID: 38750970
2. Structure-Activity Relationship Studies of α-Ketoamides as Inhibitors of the Phospholipase A and Acyltransferase Enzyme Family.. *Journal of medicinal chemistry*. PMID: 32787138

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.1 |
| 高置信度残基 (pLDDT>90) 占比 | 25.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.1% |
| 低置信 (pLDDT<50) 占比 | 50.5% |
| 有序区域 (pLDDT>70) 占比 | 34.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.1），有序残基占 34.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051496, IPR007053; Pfam: PF04970 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFKBIZ | 0.790 | 0.000 | — |
| SCN8A | 0.610 | 0.000 | — |
| GGACT | 0.593 | 0.593 | — |
| SCN1A | 0.570 | 0.000 | — |
| SPATA4 | 0.543 | 0.000 | — |
| DAGLA | 0.538 | 0.000 | — |
| SCN4B | 0.537 | 0.000 | — |
| VCPIP1 | 0.524 | 0.524 | — |
| KLHDC3 | 0.467 | 0.000 | — |
| PLA2G4E | 0.463 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VCPIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HOMER3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GGACT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF783 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ENST00000301790 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.1 + PDB: 无 | pLDDT=61.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. PLAAT5 — Phospholipase A and acyltransferase 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小279 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KN8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168004-PLAAT5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLAAT5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KN8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000168004-PLAAT5/subcellular

![](https://images.proteinatlas.org/79686/2081_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79686/2081_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/79686/2101_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79686/2101_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/79686/2155_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/79686/2155_D6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96KN8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
