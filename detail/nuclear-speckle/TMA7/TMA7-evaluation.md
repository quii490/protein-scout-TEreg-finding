---
type: protein-evaluation
gene: "TMA7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMA7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMA7 / CCDC72 |
| 蛋白名称 | Translation machinery-associated protein 7 |
| 蛋白大小 | 64 aa / 7.1 kDa |
| UniProt ID | Q9Y2S6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 64 aa / 7.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015157; Pfam: PF09072 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC72 |

**关键文献**:
1. Dissecting immune cell-specific genetics in migraine: a multi-omics framework for target discovery and therapeutic prioritization.. *The journal of headache and pain*. PMID: 41029193
2. Genetic deficiency of ribosomal rescue factor HBS1L causes retinal dystrophy associated with Pelota and EDF1 depletion.. *bioRxiv : the preprint server for biology*. PMID: 37905068
3. NUP-98 Rearrangements Led to the Identification of Candidate Biomarkers for Primary Induction Failure in Pediatric Acute Myeloid Leukemia.. *International journal of molecular sciences*. PMID: 33925480
4. Systematic identification and functional screens of uncharacterized proteins associated with eukaryotic ribosomal complexes.. *Genes & development*. PMID: 16702403

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.5 |
| 高置信度残基 (pLDDT>90) 占比 | 7.8% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 56.2% |
| 低置信 (pLDDT<50) 占比 | 3.1% |
| 有序区域 (pLDDT>70) 占比 | 40.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.5，有序区 40.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015157; Pfam: PF09072 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SERF2 | 0.803 | 0.000 | — |
| RPL36AL | 0.802 | 0.000 | — |
| COX7A2 | 0.789 | 0.000 | — |
| COX7C | 0.787 | 0.000 | — |
| UBL5 | 0.742 | 0.000 | — |
| NEDD8 | 0.717 | 0.000 | — |
| RPL34 | 0.673 | 0.000 | — |
| POMP | 0.668 | 0.000 | — |
| SUB1 | 0.654 | 0.000 | — |
| RPL31 | 0.647 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LOC100303964 | psi-mi:"MI:0018"(two hybrid) | pubmed:36581701|imex:IM-29553 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| APOOL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| SMYD3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC14 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC15 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.5 + PDB: 无 | pLDDT=70.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Nuclear b | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TMA7 — Translation machinery-associated protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小64 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2S6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000232112-TMA7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMA7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2S6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000232112-TMA7/subcellular

![](https://images.proteinatlas.org/47397/766_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/47397/766_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/47397/778_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/47397/778_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/47397/821_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/47397/821_H1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2S6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
