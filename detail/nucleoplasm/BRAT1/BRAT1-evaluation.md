---
type: protein-evaluation
gene: "BRAT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRAT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRAT1 / BAAT1, C7orf27 |
| 蛋白名称 | Integrator complex assembly factor BRAT1 |
| 蛋白大小 | 821 aa / 88.1 kDa |
| UniProt ID | Q6PJG6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 821 aa / 88.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.8; PDB: 4IFI, 8R22, 8R23, 8R2D, 8UIB |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR038904, IPR000357; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAAT1, C7orf27 |

**关键文献**:
1. The Genetic Landscape of Epilepsy of Infancy with Migrating Focal Seizures.. *Annals of neurology*. PMID: 31618474
2. Assembly mechanism of Integrator's RNA cleavage module.. *Molecular cell*. PMID: 39032489
3. BRAT1 links Integrator and defective RNA processing with neurodegeneration.. *Nature communications*. PMID: 36028512
4. Genetics of neonatal-onset epilepsies.. *Handbook of clinical neurology*. PMID: 31324323
5. BRAT1 Mutation Retrospective Diagnosis: A Case Report.. *Cureus*. PMID: 37009381

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.8 |
| 高置信度残基 (pLDDT>90) 占比 | 54.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| 可用 PDB 条目 | 4IFI, 8R22, 8R23, 8R2D, 8UIB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4IFI, 8R22, 8R23, 8R2D, 8UIB）+ AlphaFold极高置信度预测（pLDDT=84.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR038904, IPR000357; Pfam: PF02985 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA1 | 0.941 | 0.624 | — |
| E4F1 | 0.782 | 0.000 | — |
| BRAP | 0.667 | 0.000 | — |
| FAAP100 | 0.641 | 0.000 | — |
| TELO2 | 0.641 | 0.000 | — |
| LRRC14 | 0.618 | 0.000 | — |
| ATM | 0.590 | 0.292 | — |
| CT47B1 | 0.514 | 0.000 | — |
| ARMC6 | 0.489 | 0.000 | — |
| TUBGCP6 | 0.448 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sala | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENKD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NMI | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MSGN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| USHBP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PSMD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P2RX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OPRM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM108 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADGRG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.8 + PDB: 4IFI, 8R22, 8R23, 8R2D, 8UIB | pLDDT=84.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. BRAT1 — Integrator complex assembly factor BRAT1，非常新颖，仅有少数基础研究。
2. 蛋白大小821 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PJG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106009-BRAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PJG6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000106009-BRAT1/subcellular

![](https://images.proteinatlas.org/76508/1692_F11_13_cr57d275597e619_red_green.jpg)
![](https://images.proteinatlas.org/76508/1692_F11_8_cr57d2755330e51_red_green.jpg)
![](https://images.proteinatlas.org/76508/1747_H2_12_cr58063054b87c7_red_green.jpg)
![](https://images.proteinatlas.org/76508/1747_H2_18_cr5806305de098f_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PJG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PJG6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR038904;IPR000357; |
| Pfam | PF02985; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106009-BRAT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRCA1 | Intact, Biogrid | true |
| APLNR | Bioplex | false |
| ATM | Intact | false |
| CIAO2A | Bioplex | false |
| COMTD1 | Bioplex | false |
| EEF1AKMT3 | Bioplex | false |
| ENKD1 | Intact | false |
| F2RL1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
