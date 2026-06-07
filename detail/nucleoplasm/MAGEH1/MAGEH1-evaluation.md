---
type: protein-evaluation
gene: "MAGEH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGEH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGEH1 / APR1 |
| 蛋白名称 | Melanoma-associated antigen H1 |
| 蛋白大小 | 219 aa / 24.4 kDa |
| UniProt ID | Q9H213 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoli, Nucleoli rim; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 219 aa / 24.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037445, IPR041899, IPR002190; Pfam: PF01454 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APR1 |

**关键文献**:
1. MAGEH1 interacts with GADD45G and induces renal tubular cell apoptosis.. *PloS one*. PMID: 34788311
2. Neonatal detection of Turner syndrome by real-time PCR gene quantification of the ARSE and MAGEH1 genes.. *Genetics and molecular research : GMR*. PMID: 25366798
3. Mucin Expression and Splicing Determine Novel Subtypes and Patient Mortality in Pancreatic Ductal Adenocarcinoma.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 34615717
4. Constructing a 10-core genes panel for diagnosis of pediatric sepsis.. *Journal of clinical laboratory analysis*. PMID: 33274532
5. Identification of three immune subtypes characterized by distinct tumor immune microenvironment and therapeutic response in stomach adenocarcinoma.. *Gene*. PMID: 35065254

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.4 |
| 高置信度残基 (pLDDT>90) 占比 | 9.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.5% |
| 中等置信 (pLDDT 50-70) 占比 | 49.3% |
| 低置信 (pLDDT<50) 占比 | 14.6% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.4），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037445, IPR041899, IPR002190; Pfam: PF01454 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NGFR | 0.902 | 0.516 | — |
| ATRAID | 0.873 | 0.000 | — |
| PRY | 0.774 | 0.000 | — |
| TMEM37 | 0.591 | 0.000 | — |
| NSMCE4A | 0.576 | 0.479 | — |
| DDX54 | 0.555 | 0.065 | — |
| EID3 | 0.536 | 0.479 | — |
| LAYN | 0.522 | 0.000 | — |
| NGF | 0.494 | 0.000 | — |
| NTSR1 | 0.491 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TADA3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| KPNA2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| PIAS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| MOAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CDK5RAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ELN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HNRNPC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SH2B2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NAP1L5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HMBOX1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.4 + PDB: 无 | pLDDT=66.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAGEH1 — Melanoma-associated antigen H1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小219 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H213
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187601-MAGEH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H213
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000187601-MAGEH1/subcellular

![](https://images.proteinatlas.org/11971/1875_D3_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/11971/1875_D3_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/11971/1913_K15_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11971/1913_K15_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/11971/1919_G8_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/11971/1919_G8_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H213-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H213 |
| SMART | SM01373; |
| UniProt Domain [FT] | DOMAIN 1..198; /note="MAGE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00127" |
| InterPro | IPR037445;IPR041899;IPR002190; |
| Pfam | PF01454; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187601-MAGEH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HMBOX1 | Intact | false |
| KAT5 | Intact | false |
| NGFR | Biogrid | false |
| PRKCA | Intact | false |
| TNIP1 | Intact | false |
| TRIM41 | Intact | false |
| YWHAG | Intact | false |
| ZSCAN9 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
