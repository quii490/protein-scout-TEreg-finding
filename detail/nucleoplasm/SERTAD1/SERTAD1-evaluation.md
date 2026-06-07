---
type: protein-evaluation
gene: "SERTAD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERTAD1 / SEI1, TRIPBR1 |
| 蛋白名称 | SERTA domain-containing protein 1 |
| 蛋白大小 | 236 aa / 24.7 kDa |
| UniProt ID | Q9UHV2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 236 aa / 24.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052262, IPR009263; Pfam: PF06031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- sarcoplasm (GO:0016528)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 76 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEI1, TRIPBR1 |

**关键文献**:
1. CDCA4/SERTAD1/E2F1 Facilitates Lung Adenocarcinoma Progression by Inhibiting PINK1/Parkin-Mediated Mitophagy.. *IUBMB life*. PMID: 41137604
2. Prognostic and Clinicopathological Significance of SERTAD1 in Various Types of Cancer Risk: A Systematic Review and Retrospective Analysis.. *Cancers*. PMID: 30857225
3. SERTAD1 Sensitizes Breast Cancer Cells to Doxorubicin and Promotes Lysosomal Protein Biosynthesis.. *Biomedicines*. PMID: 35625886
4. SERTAD1 initiates NLRP3-mediated inflammasome activation through restricting NLRP3 polyubiquitination.. *Cell reports*. PMID: 38341852
5. Sertad1 promotes prostate cancer progression through binding androgen receptor ligand binding domain.. *International journal of cancer*. PMID: 30230528

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 14.4% |
| 置信残基 (pLDDT 70-90) 占比 | 24.6% |
| 中等置信 (pLDDT 50-70) 占比 | 22.0% |
| 低置信 (pLDDT<50) 占比 | 39.0% |
| 有序区域 (pLDDT>70) 占比 | 39.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 39.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052262, IPR009263; Pfam: PF06031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDCA4 | 0.890 | 0.000 | — |
| CDK4 | 0.874 | 0.519 | — |
| RPA2 | 0.763 | 0.000 | — |
| STN1 | 0.761 | 0.000 | — |
| CDKN2A | 0.758 | 0.510 | — |
| SERTAD4 | 0.700 | 0.000 | — |
| CCNA1 | 0.699 | 0.078 | — |
| XIAP | 0.686 | 0.625 | — |
| CCNA2 | 0.654 | 0.078 | — |
| E2F1 | 0.614 | 0.068 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KLHL42 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATXN7L3 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SETD7 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ASB8 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SMAD3 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| SPEN | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| POT1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| COPB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RCHY1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 无 | pLDDT=62.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SERTAD1 — SERTA domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小236 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHV2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197019-SERTAD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERTAD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHV2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000197019-SERTAD1/subcellular

![](https://images.proteinatlas.org/63323/1113_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/63323/1113_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/63323/1123_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/63323/1123_G11_6_red_green.jpg)
![](https://images.proteinatlas.org/63323/1230_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/63323/1230_C7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHV2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UHV2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 38..85; /note="SERTA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00396" |
| InterPro | IPR052262;IPR009263; |
| Pfam | PF06031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197019-SERTAD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SETD7 | Intact, Biogrid | true |
| ADCY1 | Biogrid | false |
| ATG12 | Intact | false |
| C1orf109 | Intact | false |
| CDK4 | Biogrid | false |
| CDKN2A | Biogrid | false |
| CHAF1A | Intact | false |
| CIB3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
