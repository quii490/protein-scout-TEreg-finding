---
type: protein-evaluation
gene: "PRKAA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PRKAA2 — REJECTED (研究热度过高 (PubMed strict=192，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRKAA2 / AMPK, AMPK2 |
| 蛋白名称 | 5'-AMP-activated protein kinase catalytic subunit alpha-2 |
| 蛋白大小 | 552 aa / 62.3 kDa |
| UniProt ID | P54646 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Nucleoplasm, Golgi apparatus, Basal bo; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 552 aa / 62.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=192 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.7; PDB: 2H6D, 2LTU, 2YZA, 3AQV, 4CFE, 4CFF, 4ZHX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032270, IPR039148, IPR028375, IPR011009, IPR049 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm, Golgi apparatus, Basal body, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- Golgi apparatus (GO:0005794)
- neuronal cell body (GO:0043025)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 192 |
| PubMed broad count | 630 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AMPK, AMPK2 |

**关键文献**:
1. Dysfunction of autophagy in high-fat diet-induced non-alcoholic fatty liver disease.. *Autophagy*. PMID: 37700498
2. Dietary timing enhances exercise by modulating fat-muscle crosstalk via adipocyte AMPKα2 signaling.. *Cell metabolism*. PMID: 40088888
3. The role of STAT3 in autophagy.. *Autophagy*. PMID: 25951043
4. AlphaFold-based AI docking reveals AMPK/SIRT1-TFEB pathway modulation by traditional Chinese medicine in metabolic-associated fatty liver disease.. *Pharmacological research*. PMID: 39832686
5. PRKAA2, MTOR, and TFEB in the regulation of lysosomal damage response and autophagy.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 38183492

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 40.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 2H6D, 2LTU, 2YZA, 3AQV, 4CFE, 4CFF, 4ZHX, 5EZV, 5ISO, 6B1U |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2H6D, 2LTU, 2YZA, 3AQV, 4CFE, 4CFF, 4ZHX, 5EZV, 5ISO, 6B1U）+ AlphaFold极高置信度预测（pLDDT=76.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032270, IPR039148, IPR028375, IPR011009, IPR049020; Pfam: PF16579, PF21147, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRKAB2 | 0.999 | 0.992 | — |
| PRKAG1 | 0.999 | 0.991 | — |
| PRKAB1 | 0.999 | 0.992 | — |
| PRKAG2 | 0.998 | 0.906 | — |
| PRKAG3 | 0.997 | 0.852 | — |
| PRKAA1 | 0.984 | 0.433 | — |
| STK11 | 0.978 | 0.636 | — |
| RPTOR | 0.973 | 0.354 | — |
| MTOR | 0.973 | 0.115 | — |
| PPARGC1A | 0.964 | 0.292 | — |

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
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 2H6D, 2LTU, 2YZA, 3AQV, 4CFE,  | pLDDT=76.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles; 额外: Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. PRKAA2 — 5'-AMP-activated protein kinase catalytic subunit alpha-2，研究基础较多，新颖性有限。
2. 蛋白大小552 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 192 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 192 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54646
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162409-PRKAA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRKAA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54646
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000162409-PRKAA2/subcellular

![](https://images.proteinatlas.org/44540/1337_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/44540/1337_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/44540/1338_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/44540/1338_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/44540/1581_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/44540/1581_D4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P54646-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P54646 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 16..268; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR032270;IPR039148;IPR028375;IPR011009;IPR049020;IPR028783;IPR000719;IPR017441;IPR008271; |
| Pfam | PF16579;PF21147;PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162409-PRKAA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABI2 | Intact, Biogrid | true |
| CALCOCO2 | Intact, Biogrid | true |
| PRKAB1 | Intact, Biogrid, Bioplex | true |
| PRKAB2 | Intact, Biogrid, Bioplex | true |
| PRKAG1 | Intact, Biogrid | true |
| PRKAG3 | Biogrid, Bioplex | true |
| TRIP6 | Intact, Biogrid | true |
| ULK1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
