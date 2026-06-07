---
type: protein-evaluation
gene: "SERTAD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SERTAD2 / KIAA0127, TRIPBR2 |
| 蛋白名称 | SERTA domain-containing protein 2 |
| 蛋白大小 | 314 aa / 33.9 kDa |
| UniProt ID | Q14140 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 33.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052262, IPR009263; Pfam: PF06031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0127, TRIPBR2 |

**关键文献**:
1. Establishing and validating an ADCP-related prognostic signature in pancreatic ductal adenocarcinoma.. *Aging*. PMID: 35963640
2. Identification of a Novel 4-gene Prognostic Model Related to Neutrophil Extracellular Traps for Colorectal Cancer.. *The Turkish journal of gastroenterology : the official journal of Turkish Society of Gastroenterology*. PMID: 39549020
3. Long Noncoding RNA SERTAD2-3 Inhibits Osteosarcoma Proliferation and Migration by Competitively Binding miR-29c.. *Genetic testing and molecular biomarkers*. PMID: 31999493
4. The diagnostic significance of the ZNF gene family in pancreatic cancer: a bioinformatics and experimental study.. *Frontiers in genetics*. PMID: 37396042
5. Genetic Foundations of Nellore Traits: A Gene Prioritization and Functional Analyses of Genome-Wide Association Study Results.. *Genes*. PMID: 39336722

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.8 |
| 高置信度残基 (pLDDT>90) 占比 | 11.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 27.1% |
| 低置信 (pLDDT<50) 占比 | 43.6% |
| 有序区域 (pLDDT>70) 占比 | 29.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.8），有序残基占 29.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052262, IPR009263; Pfam: PF06031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SERTAD3 | 0.644 | 0.000 | — |
| XPO1 | 0.613 | 0.292 | — |
| SERTAD1 | 0.582 | 0.000 | — |
| E2F1 | 0.560 | 0.068 | — |
| PPP2R2A | 0.554 | 0.535 | — |
| SERTAD4 | 0.549 | 0.000 | — |
| PPP2R2C | 0.493 | 0.493 | — |
| PPP2R1B | 0.478 | 0.478 | — |
| PPP2CB | 0.477 | 0.471 | — |
| CDK4 | 0.468 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000326933.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| IGFN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLA2G6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STRA8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF524 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HELLS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PARVG | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CTNNA3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KAT5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.8 + PDB: 无 | pLDDT=59.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. SERTAD2 — SERTA domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14140
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179833-SERTAD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERTAD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14140
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000179833-SERTAD2/subcellular

![](https://images.proteinatlas.org/20904/394_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/20904/394_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/20904/395_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/20904/395_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/20904/399_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/20904/399_E2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14140-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14140 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 33..80; /note="SERTA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00396" |
| InterPro | IPR052262;IPR009263; |
| Pfam | PF06031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179833-SERTAD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATG12 | Intact | false |
| C1orf109 | Intact | false |
| CDC7 | Intact | false |
| CKS1B | Intact | false |
| ESPNL | Intact | false |
| KAT2B | Biogrid | false |
| KAT5 | Intact | false |
| PARVG | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
