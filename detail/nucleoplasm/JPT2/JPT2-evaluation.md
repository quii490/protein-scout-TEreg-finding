---
type: protein-evaluation
gene: "JPT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## JPT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JPT2 / C16orf34, HN1L |
| 蛋白名称 | Jupiter microtubule associated homolog 2 |
| 蛋白大小 | 190 aa / 20.1 kDa |
| UniProt ID | Q9H910 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033335; Pfam: PF17054 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf34, HN1L |

**关键文献**:
1. JPT2 Affects Trophoblast Functions and Macrophage Polarization and Metabolism, and Acts as a Potential Therapeutic Target for Recurrent Spontaneous Abortion.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38417123
2. MASTER-NAADP: a membrane permeable precursor of the Ca(2+) mobilizing second messenger NAADP.. *Nature communications*. PMID: 39271671
3. TPCs: FROM PLANT TO HUMAN.. *Physiological reviews*. PMID: 40197126
4. NAADP-binding proteins find their identity.. *Trends in biochemical sciences*. PMID: 34810081
5. NAADP: From Discovery to Mechanism.. *Frontiers in immunology*. PMID: 34557192

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 58.4% |
| 低置信 (pLDDT<50) 占比 | 23.2% |
| 有序区域 (pLDDT>70) 占比 | 18.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.0），有序残基占 18.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033335; Pfam: PF17054 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JPT1 | 0.724 | 0.000 | — |
| LSM12 | 0.650 | 0.000 | — |
| TPCN2 | 0.586 | 0.000 | — |
| CRAMP1 | 0.567 | 0.000 | — |
| TPCN1 | 0.517 | 0.000 | — |
| YARS1 | 0.484 | 0.000 | — |
| ASPDH | 0.475 | 0.000 | — |
| ARSG | 0.462 | 0.000 | — |
| EEF1AKNMT | 0.461 | 0.000 | — |
| STMN1 | 0.455 | 0.443 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RASA4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SLC25A20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| XRCC6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EGR2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FIGNL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CARM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL30 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TFAP2C | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| OTUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23897|pubmed:26752685 |
| UBA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 14
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.0 + PDB: 无 | pLDDT=60.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. JPT2 — Jupiter microtubule associated homolog 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H910
- Protein Atlas: https://www.proteinatlas.org/ENSG00000206053-JPT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JPT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H910
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000206053-JPT2/subcellular

![](https://images.proteinatlas.org/41888/484_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41888/484_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41888/489_A7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/41888/489_A7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/41888/492_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41888/492_A7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H910-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H910 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033335; |
| Pfam | PF17054; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000206053-JPT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SAR1B | Opencell | false |
| STK4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
