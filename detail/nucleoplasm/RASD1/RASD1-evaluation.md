---
type: protein-evaluation
gene: "RASD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RASD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RASD1 / AGS1, DEXRAS1 |
| 蛋白名称 | Dexamethasone-induced Ras-related protein 1 |
| 蛋白大小 | 281 aa / 31.6 kDa |
| UniProt ID | Q9Y272 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Cell membrane; Cytoplasm, perinuclear region; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 281 aa / 31.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR005225, IPR001806, IPR052236; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | Cell membrane; Cytoplasm, perinuclear region; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)
- sarcoplasmic reticulum (GO:0016529)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 173 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AGS1, DEXRAS1 |

**关键文献**:
1. Pan-Cancer Analysis Identifies a Ras-Related GTPase as a Potential Modulator of Cancer.. *International journal of molecular sciences*. PMID: 40362656
2. The Roles of Rasd1 small G proteins and leptin in the activation of TRPC4 transient receptor potential channels.. *Channels (Austin, Tex.)*. PMID: 26083271
3. Integration analysis using bioinformatics and experimental validation on cellular signalling for sex differences of hypertrophic cardiomyopathy.. *Journal of cellular and molecular medicine*. PMID: 39535387
4. Rasd1 is involved in white matter injury through neuron-oligodendrocyte communication after subarachnoid hemorrhage.. *CNS neuroscience & therapeutics*. PMID: 37735980
5. Genetic Analysis of RASD1 as a Candidate Gene for Schizophrenia.. *Balkan medical journal*. PMID: 36305088

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 75.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.9，有序区 75.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR005225, IPR001806, IPR052236; Pfam: PF00071 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOS1AP | 0.996 | 0.292 | — |
| NOS1 | 0.990 | 0.292 | — |
| GNAI1 | 0.941 | 0.356 | — |
| GNAI3 | 0.927 | 0.129 | — |
| GNAI2 | 0.918 | 0.129 | — |
| CALML5 | 0.823 | 0.127 | — |
| CALML3 | 0.823 | 0.127 | — |
| CALM3 | 0.823 | 0.127 | — |
| CALML6 | 0.808 | 0.097 | — |
| CALML4 | 0.808 | 0.097 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Nr2f6 | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Cenpb | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Gnb1 | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Sh3gl2 | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Supt16h | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Tp53bp2 | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Ywhah | psi-mi:"MI:0018"(two hybrid) | pubmed:21247419|imex:IM-16862 |
| Bhlhe41 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| KRTAP1-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 无 | pLDDT=79.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasm, perinuclear region; Nucl / Nucleoplasm; 额外: Plasma membrane | 一致 |
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
1. RASD1 — Dexamethasone-induced Ras-related protein 1，研究基础较多，新颖性有限。
2. 蛋白大小281 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y272
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108551-RASD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RASD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y272
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000108551-RASD1/subcellular

![](https://images.proteinatlas.org/47896/1232_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/47896/1232_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/47896/1291_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/47896/1291_C11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y272-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y272 |
| SMART | SM00175;SM00176;SM00173;SM00174; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR005225;IPR001806;IPR052236; |
| Pfam | PF00071; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108551-RASD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APP | Intact | false |
| CDR2L | Intact | false |
| CYSRT1 | Intact | false |
| EXOSC8 | Intact | false |
| GNB1 | Biogrid | false |
| HNRNPK | Intact | false |
| KHDRBS3 | Intact | false |
| KRT34 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
