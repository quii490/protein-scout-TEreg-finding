---
type: protein-evaluation
gene: "DNTTIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNTTIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNTTIP2 / ERBP, TDIF2 |
| 蛋白名称 | Deoxynucleotidyltransferase terminal-interacting protein 2 |
| 蛋白大小 | 756 aa / 84.5 kDa |
| UniProt ID | Q5QJE6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 756 aa / 84.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.7; PDB: 7MQ8, 7MQ9, 7MQA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039883, IPR014810; Pfam: PF08698 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome | Supported |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERBP, TDIF2 |

**关键文献**:
1. Comprehensive analysis of cuproptosis-related genes involved in immune infiltration and their use in the diagnosis of hepatic ischemia-reperfusion injury: an experimental study.. *International journal of surgery (London, England)*. PMID: 38935114
2. Hepatitis B virus X protein (HBx)-mediated immune modulation and prognostic model development in hepatocellular carcinoma.. *PloS one*. PMID: 40577282
3. Exploration of differentially expressed mRNAs and miRNAs for pediatric acute myeloid leukemia.. *Frontiers in genetics*. PMID: 36160019
4. m6A regulators-based gene expression pattern is associated with immune microenvironment characteristics in hepatocellular carcinoma.. *Scientific reports*. PMID: 41310383
5. DNTTIP2 Expression is Associated with Macrophage Infiltration and Malignant Characteristics in Low-Grade Glioma.. *Pharmacogenomics and personalized medicine*. PMID: 35370417

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.7 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.3% |
| 低置信 (pLDDT<50) 占比 | 64.3% |
| 有序区域 (pLDDT>70) 占比 | 21.4% |
| 可用 PDB 条目 | 7MQ8, 7MQ9, 7MQA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.7），有序残基占 21.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039883, IPR014810; Pfam: PF08698 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FCF1 | 0.999 | 0.985 | — |
| UTP11 | 0.998 | 0.976 | — |
| UTP3 | 0.998 | 0.976 | — |
| UTP6 | 0.997 | 0.982 | — |
| NGDN | 0.997 | 0.976 | — |
| WDR46 | 0.997 | 0.976 | — |
| WDR36 | 0.997 | 0.987 | — |
| AATF | 0.997 | 0.991 | — |
| MPHOSPH10 | 0.997 | 0.976 | — |
| WDR43 | 0.997 | 0.980 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TULP3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| IFIT2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RBM6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RPF2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FAM50A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| RNF8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.7 + PDB: 7MQ8, 7MQ9, 7MQA | pLDDT=53.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic c | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNTTIP2 — Deoxynucleotidyltransferase terminal-interacting protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小756 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=53.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5QJE6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000067334-DNTTIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNTTIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5QJE6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000067334-DNTTIP2/subcellular

![](https://images.proteinatlas.org/44502/1888_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44502/1888_B4_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/44502/522_B8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44502/522_B8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/44502/527_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44502/527_B8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5QJE6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
