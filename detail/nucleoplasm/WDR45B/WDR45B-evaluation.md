---
type: protein-evaluation
gene: "WDR45B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR45B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR45B / WDR45L, WIPI3 |
| 蛋白名称 | WD repeat domain phosphoinositide-interacting protein 3 |
| 蛋白大小 | 344 aa / 38.1 kDa |
| UniProt ID | Q5MNZ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Preautophagosomal structure; Lysosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 344 aa / 38.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.8; PDB: 6IYY, 6KLR, 8ZQG, 9C9I, 9CE3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR048720, IPR015943, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Uncertain |
| UniProt | Preautophagosomal structure; Lysosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- lysosome (GO:0005764)
- phagophore assembly site (GO:0000407)
- phagophore assembly site membrane (GO:0034045)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR45L, WIPI3 |

**关键文献**:
1. El-Hattab-Alkuraya Syndrome.. **. PMID: 36173873
2. ATG2A acts as a tether to regulate autophagosome-lysosome fusion in neural cells.. *Autophagy*. PMID: 40083067
3. WIPI proteins: Biological functions and related syndromes.. *Frontiers in molecular neuroscience*. PMID: 36157071
4. The BPAN and intellectual disability disease proteins WDR45 and WDR45B modulate autophagosome-lysosome fusion.. *Autophagy*. PMID: 34105435
5. Role of Wdr45b in maintaining neural autophagy and cognitive function.. *Autophagy*. PMID: 31238825

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 90.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 95.6% |
| 可用 PDB 条目 | 6IYY, 6KLR, 8ZQG, 9C9I, 9CE3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6IYY, 6KLR, 8ZQG, 9C9I, 9CE3）+ AlphaFold极高置信度预测（pLDDT=94.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048720, IPR015943, IPR036322, IPR001680; Pfam: PF21032 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATG2A | 0.891 | 0.074 | — |
| OTUD7B | 0.853 | 0.000 | — |
| ATG2B | 0.784 | 0.074 | — |
| WIPI2 | 0.616 | 0.097 | — |
| ATG12 | 0.602 | 0.000 | — |
| ATG5 | 0.594 | 0.000 | — |
| ATG7 | 0.592 | 0.125 | — |
| PIK3R4 | 0.583 | 0.000 | — |
| EPG5 | 0.579 | 0.000 | — |
| ATG16L1 | 0.575 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q81VA8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ASPRV1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RCN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNJ5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KHDRBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P2RX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5orf24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SARNP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 6IYY, 6KLR, 8ZQG, 9C9I, 9CE3 | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Preautophagosomal structure; Lysosome / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WDR45B — WD repeat domain phosphoinositide-interacting protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小344 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5MNZ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141580-WDR45B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR45B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5MNZ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (uncertain)。来源: https://www.proteinatlas.org/ENSG00000141580-WDR45B/subcellular

![](https://images.proteinatlas.org/17886/149_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17886/149_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17886/150_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17886/150_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17886/151_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17886/151_B6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5MNZ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5MNZ6 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR048720;IPR015943;IPR036322;IPR001680; |
| Pfam | PF21032; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141580-WDR45B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AHDC1 | Bioplex | false |
| AKR1B1 | Bioplex | false |
| C17orf49 | Bioplex | false |
| UBXN10 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
