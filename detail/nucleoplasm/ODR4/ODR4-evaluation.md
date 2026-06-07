---
type: protein-evaluation
gene: "ODR4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ODR4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ODR4 / C1orf27, TTG1, TTG1A |
| 蛋白名称 | Protein odr-4 homolog |
| 蛋白大小 | 454 aa / 51.1 kDa |
| UniProt ID | Q5SWX8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 51.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029454; Pfam: PF14778 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf27, TTG1, TTG1A |

**关键文献**:
1. Identification of potential biomarkers for lung adenocarcinoma.. *Heliyon*. PMID: 33251353
2. Trafficking prerogatives of olfactory receptors.. *Neuroreport*. PMID: 14502073
3. An ER complex of ODR-4 and ODR-8/Ufm1 specific protease 2 promotes GPCR maturation by a Ufm1-independent mechanism.. *PLoS genetics*. PMID: 24603482
4. Ubiquitously expressed GPCR membrane-trafficking orthologs.. *Genomics*. PMID: 15718105
5. Analysis of various types of single-polypeptide-chain (sc) heterodimeric A₂AR/D₂R complexes and their allosteric receptor-receptor interactions.. *Biochemical and biophysical research communications*. PMID: 25478641

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 48.5% |
| 置信残基 (pLDDT 70-90) 占比 | 27.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 12.6% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.4，有序区 75.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029454; Pfam: PF14778 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UFSP2 | 0.737 | 0.402 | — |
| UFSP1 | 0.530 | 0.149 | — |
| RTP2 | 0.528 | 0.000 | — |
| RTP1 | 0.479 | 0.000 | — |
| DDRGK1 | 0.477 | 0.196 | — |
| FAM177A1 | 0.467 | 0.467 | — |
| TXNL1 | 0.457 | 0.000 | — |
| CCDC173 | 0.454 | 0.000 | — |
| AGPS | 0.451 | 0.000 | — |
| DPM1 | 0.433 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| ENSP00000287859.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| thiD2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FGFR3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| STAP1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| FAM177A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| NAPG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NAPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 1 / 14 = 7%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 无 | pLDDT=80.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

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
1. ODR4 — Protein odr-4 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5SWX8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157181-ODR4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ODR4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5SWX8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157181-ODR4/subcellular

![](https://images.proteinatlas.org/15988/127_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15988/127_A8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15988/128_A8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/15988/128_A8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/15988/129_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15988/129_A8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5SWX8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5SWX8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029454; |
| Pfam | PF14778; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157181-ODR4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC47 | Opencell | false |
| DDRGK1 | Biogrid | false |
| SEC61B | Opencell | false |
| UFSP2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
