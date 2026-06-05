---
type: protein-evaluation
gene: "PLEKHA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHA1 / TAPP1 |
| 蛋白名称 | Pleckstrin homology domain-containing family A member 1 |
| 蛋白大小 | 404 aa / 45.6 kDa |
| UniProt ID | Q9HB21 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Cell membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 404 aa / 45.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=52 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=70.4; PDB: 1EAZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR051707; Pfam: PF00169 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Cell membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- ruffle membrane (GO:0032587)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 52 |
| PubMed broad count | 99 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TAPP1 |

**关键文献**:
1. Transcriptomic, epigenomic, and spatial metabolomic cell profiling redefines regional human kidney anatomy.. *Cell metabolism*. PMID: 38513647
2. The PLEKHA1-TACC2 fusion gene drives tumorigenesis via vascular mimicry formation in esophageal squamous-cell carcinoma.. *Cell death and differentiation*. PMID: 40615663
3. Identification of JAZF1, KNOP1, and PLEKHA1 as causally associated genes and drug targets for Alzheimer's disease: a summary data-based Mendelian randomization study.. *Inflammopharmacology*. PMID: 39455528
4. Integrative Analysis of Endothelial Cell Senescence-Related Genes in Idiopathic Pulmonary Fibrosis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 41351492
5. Cumulative association between age-related macular degeneration and less studied genetic variants in PLEKHA1/ARMS2/HTRA1: a meta and gene-cluster analysis.. *Molecular biology reports*. PMID: 24013816

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.4 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 36.4% |
| 有序区域 (pLDDT>70) 占比 | 56.2% |
| 可用 PDB 条目 | 1EAZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=70.4，有序区 56.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR051707; Pfam: PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTPN13 | 0.971 | 0.421 | — |
| ARMS2 | 0.915 | 0.000 | — |
| CFH | 0.848 | 0.000 | — |
| PLEKHA2 | 0.738 | 0.230 | — |
| HTRA1 | 0.738 | 0.000 | — |
| HMCN1 | 0.666 | 0.000 | — |
| EFEMP1 | 0.625 | 0.087 | — |
| MPDZ | 0.593 | 0.510 | — |
| C2 | 0.587 | 0.000 | — |
| BTBD16 | 0.576 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| SH3BP4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| CRKL | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| queA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PBX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDR45B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.4 + PDB: 1EAZ | pLDDT=70.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLEKHA1 — Pleckstrin homology domain-containing family A member 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小404 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 52 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107679-PLEKHA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000107679-PLEKHA1/subcellular

![](https://images.proteinatlas.org/2043/35_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/2043/35_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/2043/36_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/2043/36_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/2043/37_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/2043/37_B5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HB21-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
