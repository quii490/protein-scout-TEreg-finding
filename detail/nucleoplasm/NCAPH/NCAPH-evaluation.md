---
type: protein-evaluation
gene: "NCAPH"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCAPH 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCAPH / BRRN, BRRN1, CAPH, KIAA0074 |
| 蛋白名称 | Condensin complex subunit 2 |
| 蛋白大小 | 741 aa / 82.6 kDa |
| UniProt ID | Q15003 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: Nucleus; Cytoplasm; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 741 aa / 82.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.8; PDB: 6IGX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022816; Pfam: PF05786 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.5/180** | |
| **归一化总分** | | | **55.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- condensed nuclear chromosome (GO:0000794)
- condensin complex (GO:0000796)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 104 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRRN, BRRN1, CAPH, KIAA0074 |

**关键文献**:
1. The role of NCAPH in cancer treatment.. *Cellular signalling*. PMID: 38901722
2. Integrated bioinformatics combined with machine learning to analyze shared biomarkers and pathways in psoriasis and cervical squamous cell carcinoma.. *Frontiers in immunology*. PMID: 38863714
3. NCAPH-YAP1 interaction promotes breast cancer stemness and tumor progression.. *Stem cell research & therapy*. PMID: 40999529
4. NCAPH promotes immune evasion via inhibiting PD-L1 protein degradation in head and neck squamous cell carcinoma.. *Cancer letters*. PMID: 41386505
5. NCAPH drives breast cancer progression and identifies a gene signature that predicts luminal a tumour recurrence.. *Clinical and translational medicine*. PMID: 38344872

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.8 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 30.1% |
| 低置信 (pLDDT<50) 占比 | 36.3% |
| 有序区域 (pLDDT>70) 占比 | 33.6% |
| 可用 PDB 条目 | 6IGX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.8），有序残基占 33.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022816; Pfam: PF05786 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCAPG | 0.999 | 0.999 | — |
| SMC2 | 0.999 | 0.993 | — |
| SMC4 | 0.999 | 0.993 | — |
| NCAPD2 | 0.999 | 0.992 | — |
| NCAPD3 | 0.994 | 0.143 | — |
| NCAPG2 | 0.979 | 0.098 | — |
| KIF4A | 0.945 | 0.190 | — |
| BUB1 | 0.933 | 0.000 | — |
| NCAPH2 | 0.916 | 0.000 | — |
| BUB1B | 0.915 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KLKB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CD74 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| DPEP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FZD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARPC1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.8 + PDB: 6IGX | pLDDT=59.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome / Cytosol; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NCAPH — Condensin complex subunit 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小741 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15003
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121152-NCAPH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCAPH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15003
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000121152-NCAPH/subcellular

![](https://images.proteinatlas.org/3008/2175_H8_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/3008/2175_H8_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/3008/2178_A5_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/3008/2178_A5_45_blue_red_green.jpg)
![](https://images.proteinatlas.org/3008/2201_B4_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/3008/2201_B4_98_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15003-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
