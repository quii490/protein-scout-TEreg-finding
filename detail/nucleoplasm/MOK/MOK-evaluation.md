---
type: protein-evaluation
gene: "MOK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MOK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOK / RAGE, RAGE1 |
| 蛋白名称 | MAPK/MAK/MRK overlapping kinase |
| 蛋白大小 | 419 aa / 48.0 kDa |
| UniProt ID | Q9UQ07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Mid piece, Principal piece, End p; UniProt: Cytoplasm; Cell projection, cilium; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 48.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Mid piece, Principal piece, End piece | Approved |
| UniProt | Cytoplasm; Cell projection, cilium; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary base (GO:0097546)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 7945 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAGE, RAGE1 |

**关键文献**:
1. MAPK/MAK/MRK overlapping kinase (MOK) controls microglial inflammatory/type-I IFN responses via Brd4 and is involved in ALS.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37399380
2. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
3. Molecular Mechanism of Mok I Gene Overexpression in Enhancing Monacolin K Production in Monascus pilosus.. *Journal of fungi (Basel, Switzerland)*. PMID: 39452673
4. Cdx2 homeodomain protein regulates the expression of MOK, a member of the mitogen-activated protein kinase superfamily, in the intestinal epithelial cells.. *FEBS letters*. PMID: 15327990
5. Identification of NEK3 and MOK as novel targets for lithium.. *Chemical biology & drug design*. PMID: 30667602

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 61.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 27.9% |
| 有序区域 (pLDDT>70) 占比 | 70.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.2，有序区 70.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCM2 | 0.788 | 0.782 | — |
| CDC6 | 0.788 | 0.782 | — |
| CDT1 | 0.783 | 0.782 | — |
| MCM3 | 0.783 | 0.782 | — |
| MCM7 | 0.783 | 0.782 | — |
| MCM4 | 0.783 | 0.782 | — |
| MCM6 | 0.782 | 0.782 | — |
| ORC2 | 0.782 | 0.782 | — |
| ORC4 | 0.782 | 0.782 | — |
| ORC5 | 0.782 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| S100P | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17587138 |
| SDF4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| PRP4K | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ANXA2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ECHDC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DGKD | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CLPB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| IMPDH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 无 | pLDDT=76.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell projection, cilium; Nucleus / Endoplasmic reticulum; 额外: Mid piece, Principal pi | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MOK — MAPK/MAK/MRK overlapping kinase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQ07
- Protein Atlas: https://www.proteinatlas.org/ENSG00000080823-MOK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQ07
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000080823-MOK/subcellular

![](https://images.proteinatlas.org/27292/2148_A8_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/27292/2148_A8_63_blue_red_green.jpg)
![](https://images.proteinatlas.org/27292/2150_E9_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/27292/2150_E9_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/27292/2211_B7_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/27292/2211_B7_45_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UQ07-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
