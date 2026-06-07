---
type: protein-evaluation
gene: "HMGN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HMGN1 — REJECTED (研究热度过高 (PubMed strict=141，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMGN1 / HMG14 |
| 蛋白名称 | Non-histone chromosomal protein HMG-14 |
| 蛋白大小 | 100 aa / 10.7 kDa |
| UniProt ID | P05114 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 100 aa / 10.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=141 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000079; Pfam: PF01101 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- female germ cell nucleus (GO:0001674)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 141 |
| PubMed broad count | 192 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HMG14 |

**关键文献**:
1. Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21.. *Nature*. PMID: 41125893
2. Shaking up the silence: consequences of HMGN1 antagonizing PRC2 in the Down syndrome brain.. *Epigenetics & chromatin*. PMID: 36463299
3. Human HMGN1 and HMGN2 are not required for transcription-coupled DNA repair.. *Scientific reports*. PMID: 32152397
4. Alarmins and Antitumor Immunity.. *Clinical therapeutics*. PMID: 27101817
5. High-mobility group nucleosome binding domain 1 (HMGN1) functions as a Th1-polarizing alarmin.. *Seminars in immunology*. PMID: 29503123

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 90.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 10.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.3），有序残基占 10.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000079; Pfam: PF01101 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HMGN2 | 0.994 | 0.196 | — |
| FAU | 0.988 | 0.967 | — |
| TCEA1 | 0.975 | 0.000 | — |
| ERCC6 | 0.961 | 0.292 | — |
| HMGN5 | 0.956 | 0.000 | — |
| EP300 | 0.947 | 0.292 | — |
| RPS3 | 0.946 | 0.743 | — |
| RPL5 | 0.942 | 0.741 | — |
| RPS18 | 0.941 | 0.744 | — |
| RPS15 | 0.941 | 0.747 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC38A3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SMARCB1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| H2BC12L | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZNF653 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CACNG2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ANK3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PLAGL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DCDC2B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MAGEA4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.3 + PDB: 无 | pLDDT=63.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HMGN1 — Non-histone chromosomal protein HMG-14，研究基础较多，新颖性有限。
2. 蛋白大小100 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 141 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 141 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P05114
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205581-HMGN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMGN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P05114
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000205581-HMGN1/subcellular

![](https://images.proteinatlas.org/48694/712_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/48694/712_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/48694/804_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/48694/804_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P05114-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P05114 |
| SMART | SM00527; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000079; |
| Pfam | PF01101; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205581-HMGN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANKRD49 | Bioplex | false |
| APEX1 | Biogrid | false |
| H2BC5 | Biogrid | false |
| H2BC8 | Biogrid | false |
| H2BC9 | Biogrid | false |
| H4C1 | Biogrid | false |
| H4C7 | Bioplex | false |
| HMGN2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
