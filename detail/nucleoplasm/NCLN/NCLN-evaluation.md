---
type: protein-evaluation
gene: "NCLN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCLN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCLN |
| 蛋白名称 | BOS complex subunit NCLN |
| 蛋白大小 | 563 aa / 63.0 kDa |
| UniProt ID | Q969V3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Lipid droplets; 额外: Nucleoplasm; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 563 aa / 63.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.4; PDB: 6W6L, 9C7U, 9C7V |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016574, IPR007484; Pfam: PF04389 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Lipid droplets; 额外: Nucleoplasm | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- multi-pass translocon complex (GO:0160064)
- protein-containing complex (GO:0032991)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Ophthalmological manifestations and plasma markers of inflammation in Ebola survivors in post-treatment era.. *Scientific reports*. PMID: 40301432
2. Comprehensive Genomic Analysis of Cemento-Ossifying Fibroma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 37995913
3. Sperm RNA landscape during sexual maturation in Duroc boars.. *BMC genomics*. PMID: 41566433
4. Identification of New ATG8s-Binding Proteins with Canonical LC3-Interacting Region in Autophagosomes of Barley Callus.. *Plant & cell physiology*. PMID: 35134996
5. Interaction of human oral cancer and the expression of virulence genes of dental pathogenic bacteria.. *Microbial pathogenesis*. PMID: 32858118

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 55.8% |
| 置信残基 (pLDDT 70-90) 占比 | 30.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 86.0% |
| 可用 PDB 条目 | 6W6L, 9C7U, 9C7V |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6W6L, 9C7U, 9C7V）+ AlphaFold高质量预测（pLDDT=85.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016574, IPR007484; Pfam: PF04389 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM147 | 0.998 | 0.845 | — |
| NOMO2 | 0.996 | 0.461 | — |
| NOMO1 | 0.966 | 0.782 | — |
| CCDC47 | 0.943 | 0.888 | — |
| TMCO1 | 0.934 | 0.896 | — |
| SEC61A1 | 0.902 | 0.819 | — |
| NOMO3 | 0.892 | 0.221 | — |
| RPL17 | 0.864 | 0.861 | — |
| RPL4 | 0.847 | 0.845 | — |
| RPL19 | 0.847 | 0.843 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SAP18 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNFRSF14 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| FBXO6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| RAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| KRTAP5-9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 6W6L, 9C7U, 9C7V | pLDDT=85.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Lipid droplets; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NCLN — BOS complex subunit NCLN，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小563 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969V3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125912-NCLN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCLN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969V3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Lipid droplets (approved)。来源: https://www.proteinatlas.org/ENSG00000125912-NCLN/subcellular

![](https://images.proteinatlas.org/6625/41_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6625/41_D12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6625/42_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6625/42_D12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6625/43_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6625/43_D12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q969V3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
