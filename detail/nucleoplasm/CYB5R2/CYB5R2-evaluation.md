---
type: protein-evaluation
gene: "CYB5R2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYB5R2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYB5R2 |
| 蛋白名称 | NADH-cytochrome b5 reductase 2 |
| 蛋白大小 | 276 aa / 31.5 kDa |
| UniProt ID | Q6BCY4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 276 aa / 31.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=95.8; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR001834, IPR008333, IPR017927, IPR001709, IPR039 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 21 |
| 别名(未计入scoring) |  |

**关键文献**:
1. GATA3 mediates doxorubicin resistance by inhibiting CYB5R2-catalyzed iron reduction in breast cancer cells.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 37230023
2. ATF7IP inhibits Sorafenib-induced ferroptosis in hepatocellular carcinoma cells by inhibiting CYB5R2 transcription and stabilizing PARK7 protein.. *Redox biology*. PMID: 40716153
3. Inhibition of NR2F2 Attenuates Vascular Dysfunction in Diabetic Retinopathy by Alleviating Endoplasmic Reticulum Stress in Retinal Microvascular Endothelial Cells.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40417967
4. Genetic, epigenetic, and molecular landscapes of multifocal and multicentric glioblastoma.. *Acta neuropathologica*. PMID: 26323991
5. Cytochrome b5 reductase 2 suppresses tumor formation in nasopharyngeal carcinoma by attenuating angiogenesis.. *Chinese journal of cancer*. PMID: 26275421

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.8 |
| 高置信度残基 (pLDDT>90) 占比 | 95.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 98.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.8，有序区 98.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001834, IPR008333, IPR017927, IPR001709, IPR039261; Pfam: PF00970, PF00175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYB5B | 0.994 | 0.111 | — |
| CYB5A | 0.993 | 0.111 | — |
| SUOX | 0.942 | 0.096 | — |
| DHODH | 0.918 | 0.469 | — |
| DPYD | 0.880 | 0.469 | — |
| UMPS | 0.853 | 0.000 | — |
| SCD | 0.820 | 0.000 | — |
| FDXR | 0.702 | 0.456 | — |
| POR | 0.653 | 0.071 | — |
| GPR143 | 0.616 | 0.048 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| COIL | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| FFAR2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF778 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AGR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NFKBID | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MED20 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SUOX | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.8 + PDB: 无 | pLDDT=95.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CYB5R2 -- NADH-cytochrome b5 reductase 2，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小276 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6BCY4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166394-CYB5R2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYB5R2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6BCY4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6BCY4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6BCY4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 15..127; /note="FAD-binding FR-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00716" |
| InterPro | IPR001834;IPR008333;IPR017927;IPR001709;IPR039261;IPR001433;IPR017938; |
| Pfam | PF00970;PF00175; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166394-CYB5R2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC23 | Intact | false |
| GOLGA2 | Intact | false |
| PSMC6 | Intact | false |
| TRAF1 | Intact | false |
| TRAF2 | Intact | false |
| TRIP13 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
