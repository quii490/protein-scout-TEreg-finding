---
type: protein-evaluation
gene: "RIMS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RIMS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIMS3 / KIAA0237 |
| 蛋白名称 | Regulating synaptic membrane exocytosis protein 3 |
| 蛋白大小 | 308 aa / 32.8 kDa |
| UniProt ID | Q9UJD0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Mitochondria; 额外: Nucleoplasm; UniProt: Synapse |
| 蛋白大小 | 10/10 | ×1 | 10 | 308 aa / 32.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR039032; Pfam: PF00168 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Synapse | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- presynaptic active zone (GO:0048786)
- presynaptic active zone cytoplasmic component (GO:0098831)
- presynaptic membrane (GO:0042734)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0237 |

**关键文献**:
1. Gut microbiota and host transcriptome interactions reveal diagnostic biomarkers in MASLD-associated hepatocellular carcinoma.. *Gut pathogens*. PMID: 41402920
2. Identification of a polyamine-related signature and six novel prognostic biomarkers in oral squamous cell carcinoma.. *Frontiers in molecular biosciences*. PMID: 36733434
3. A network view on Parkinson's disease.. *Computational and structural biotechnology journal*. PMID: 24688734
4. Epigenetic silencing of spermatocyte-specific and neuronal genes by SUMO modification of the transcription factor Sp3.. *PLoS genetics*. PMID: 21085687
5. Investigation of the expression of genes affecting cytomatrix active zone function in the amygdala in schizophrenia: effects of antipsychotic drugs.. *Journal of psychiatric research*. PMID: 18490030

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 25.3% |
| 低置信 (pLDDT<50) 占比 | 27.9% |
| 有序区域 (pLDDT>70) 占比 | 46.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.1，有序区 46.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR039032; Pfam: PF00168 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IL1RAPL1 | 0.585 | 0.000 | — |
| UNC13A | 0.530 | 0.280 | — |
| UNC13B | 0.529 | 0.280 | — |
| ERC2 | 0.529 | 0.259 | — |
| ERC1 | 0.513 | 0.259 | — |
| NLGN3 | 0.492 | 0.000 | — |
| PPFIA3 | 0.489 | 0.089 | — |
| UNC13C | 0.468 | 0.280 | — |
| FEZ1 | 0.444 | 0.000 | — |
| METAP1D | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GJA5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000361769.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZDHHC17 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-21827|pubmed:24705354 |
| BANP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| TRIM54 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| VIM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.1 + PDB: 无 | pLDDT=71.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Synapse / Nucleoli, Mitochondria; 额外: Nucleoplasm | 一致 |
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
1. RIMS3 — Regulating synaptic membrane exocytosis protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小308 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJD0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117016-RIMS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIMS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJD0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000117016-RIMS3/subcellular

![](https://images.proteinatlas.org/55285/1189_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55285/1189_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55285/1219_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55285/1219_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55285/1226_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55285/1226_C12_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJD0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
