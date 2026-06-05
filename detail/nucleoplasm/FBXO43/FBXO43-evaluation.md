---
type: protein-evaluation
gene: "FBXO43"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO43 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO43 / EMI2 |
| 蛋白名称 | F-box only protein 43 |
| 蛋白大小 | 708 aa / 78.4 kDa |
| UniProt ID | Q4G163 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 708 aa / 78.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001810, IPR047147, IPR002867, IPR044064; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EMI2 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. Association between F-box-only protein 43 overexpression and hepatocellular carcinoma pathogenesis and prognosis.. *Cancer medicine*. PMID: 36710413
3. A homozygous loss-of-function mutation in FBXO43 causes human non-obstructive azoospermia.. *Clinical genetics*. PMID: 34595750
4. Gene mutations impede oocyte maturation, fertilization, and early embryonic development.. *BioEssays : news and reviews in molecular, cellular and developmental biology*. PMID: 35900055
5. Bioinformatic analysis of related immune cell infiltration and key genes in the progression of osteonecrosis of the femoral head.. *Frontiers in immunology*. PMID: 38283345

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.3 |
| 高置信度残基 (pLDDT>90) 占比 | 13.6% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 65.3% |
| 有序区域 (pLDDT>70) 占比 | 23.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.3），有序残基占 23.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001810, IPR047147, IPR002867, IPR044064; Pfam: PF00646 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLK1 | 0.992 | 0.821 | — |
| CDC20 | 0.988 | 0.399 | — |
| SKP1 | 0.966 | 0.225 | — |
| BTRC | 0.956 | 0.000 | — |
| CDK1 | 0.952 | 0.095 | — |
| CUL1 | 0.948 | 0.095 | — |
| CCNB1 | 0.944 | 0.000 | — |
| PPP2R1A | 0.924 | 0.244 | — |
| RBX1 | 0.920 | 0.000 | — |
| PPP2R1B | 0.905 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC25A12 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SKP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PPP2R1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.3 + PDB: 无 | pLDDT=52.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO43 — F-box only protein 43，非常新颖，仅有少数基础研究。
2. 蛋白大小708 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4G163
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156509-FBXO43/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO43
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4G163
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000156509-FBXO43/subcellular

![](https://images.proteinatlas.org/24292/226_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24292/226_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24292/2275_E12_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/24292/2275_E12_138_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4G163-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
