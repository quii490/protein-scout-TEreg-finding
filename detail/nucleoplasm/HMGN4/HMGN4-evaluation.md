---
type: protein-evaluation
gene: "HMGN4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HMGN4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMGN4 / HMG17L3, NHC |
| 蛋白名称 | High mobility group nucleosome-binding domain-containing protein 4 |
| 蛋白大小 | 90 aa / 9.5 kDa |
| UniProt ID | O00479 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 90 aa / 9.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000079; Pfam: PF01101 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HMG17L3, NHC |

**关键文献**:
1. Lactylation signature identifies liver fibrosis phenotypes and traces fibrotic progression to hepatocellular carcinoma.. *Frontiers in immunology*. PMID: 39257588
2. Elevated HMGN4 expression potentiates thyroid tumorigenesis.. *Carcinogenesis*. PMID: 28186538
3. Integrative transcriptome analysis identifies a crotonylation gene signature for predicting prognosis and drug sensitivity in hepatocellular carcinoma.. *Journal of cellular and molecular medicine*. PMID: 39428564
4. HMGN4 plays a key role in STAT3-mediated oncogenesis of triple-negative breast cancer.. *Carcinogenesis*. PMID: 35792800
5. HMGN4, a newly discovered nucleosome-binding protein encoded by an intronless gene.. *DNA and cell biology*. PMID: 11410162

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.7% |
| 中等置信 (pLDDT 50-70) 占比 | 83.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 16.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 16.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000079; Pfam: PF01101 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.987 | 0.967 | — |
| RPL11 | 0.949 | 0.743 | — |
| RPS15 | 0.945 | 0.761 | — |
| RPL8 | 0.943 | 0.788 | — |
| RPS18 | 0.939 | 0.744 | — |
| RPL35 | 0.939 | 0.745 | — |
| RPL23 | 0.939 | 0.743 | — |
| RPS11 | 0.938 | 0.743 | — |
| RPS3 | 0.938 | 0.743 | — |
| RPL5 | 0.938 | 0.741 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2843763 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SMARCB1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| NPM1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ARHGAP39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| EWSR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| MACROH2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| H2AC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PARP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 无 | pLDDT=65.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. HMGN4 — High mobility group nucleosome-binding domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小90 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00479
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182952-HMGN4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMGN4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00479
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000182952-HMGN4/subcellular

![](https://images.proteinatlas.org/77364/1609_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/77364/1609_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/77364/1611_H10_5_red_green.jpg)
![](https://images.proteinatlas.org/77364/1611_H10_6_red_green.jpg)
![](https://images.proteinatlas.org/77364/1634_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/77364/1634_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00479-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00479 |
| SMART | SM00527; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000079; |
| Pfam | PF01101; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182952-HMGN4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| H2AC21 | Biogrid, Bioplex | true |
| H2BC11 | Biogrid, Bioplex | true |
| H2BC12 | Biogrid, Bioplex | true |
| BMS1 | Bioplex | false |
| BOP1 | Bioplex | false |
| CCDC137 | Bioplex | false |
| DDX24 | Bioplex | false |
| DDX31 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
