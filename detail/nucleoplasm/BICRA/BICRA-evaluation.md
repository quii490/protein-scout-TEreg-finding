---
type: protein-evaluation
gene: "BICRA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BICRA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BICRA / GLTSCR1 |
| 蛋白名称 | BRD4-interacting chromatin-remodeling complex-associated protein |
| 蛋白大小 | 1560 aa / 158.5 kDa |
| UniProt ID | Q9NZM4 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:37:05 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 4/10 | x1 | 4 | 1560 aa / 158.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 3/10 | x3 | 9 | AlphaFold v6 pLDDT=41.9 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR052438, IPR015671 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5 |
| **原始总分** | | | **144.0/180** | |
| **归一化总分 (/1.83)** | | | **78.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- chromatin (GO:0000785)
- GBAF complex (GO:0140288)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SWI/SNF complex (GO:0016514)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 1560 aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLTSCR1 |

**关键文献**:
1. Coffin-Siris Syndrome.. **. PMID: 23556151
2. BICRA, a SWI/SNF Complex Member, Is Associated with BAF-Disorder Related Phenotypes in Humans and Model Organisms.. *American journal of human genetics*. PMID: 33232675
3. Loss of Bicra impairs Drosophila learning and choice abilities.. *Neuroscience letters*. PMID: 34974109
4. Identifying Comprehensive Genomic Alterations and Potential Neoantigens for Cervical Cancer Immunotherapy in a Cohort of Chinese Squamous Cell Carcinoma of the Cervix.. *Biomedical and environmental sciences : BES*. PMID: 38988108
5. Loss of Bicra/Gltscr1 leads to a defect in fetal liver macrophages responsible for erythrocyte maturation in mice.. *bioRxiv : the preprint server for biology*. PMID: 39464106

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 41.9 |
| 高置信度残基 (pLDDT>90) 占比 | 3.6% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 81.6% |
| 有序区域 (pLDDT>70) 占比 | 11.8% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold低质量预测（pLDDT=41.9），大部分区域无序。三维结构评分 3/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052438, IPR015671; Pfam: PF15249 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRD9 | 0.999 | 0.691 | -- |
| SMARCD1 | 0.995 | 0.841 | -- |
| SMARCA4 | 0.990 | 0.631 | -- |
| SS18 | 0.988 | 0.839 | -- |
| BCL7A | 0.987 | 0.678 | -- |
| SMARCA2 | 0.986 | 0.612 | -- |
| BCL7C | 0.984 | 0.733 | -- |
| SMARCB1 | 0.983 | 0.445 | -- |
| SMARCC1 | 0.980 | 0.527 | -- |
| ARID1A | 0.980 | 0.303 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Syx16 | two hybrid fragment pooling approach | pubmed:15710747|imex:IM-16519|mint:MINT-5217543 |
| Mer | two hybrid fragment pooling approach | pubmed:15710747|imex:IM-16519|mint:MINT-5217543 |
| ssp6 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| MYC | tandem affinity purification | pubmed:21150319|imex:IM-16995 |
| EBI-28975771 | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| NCK1 | peptide array | imex:IM-11903|pubmed:17474147|mint:MINT-8109998 |
| CRK | peptide array | imex:IM-11903|pubmed:17474147|mint:MINT-8109998 |
| SRC | peptide array | imex:IM-11903|pubmed:17474147|mint:MINT-8109998 |
| GRB2 | peptide array | imex:IM-11903|pubmed:17474147|mint:MINT-8109998 |
| PIK3R1 | peptide array | imex:IM-11903|pubmed:17474147|mint:MINT-8109998 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=41.9 | 单一来源 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 78.7/100

**核心优势**:
1. BICRA -- BRD4-interacting chromatin-remodeling complex-associated protein，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 3 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. AlphaFold pLDDT 较低（41.9），存在显著无序区
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
3. 蛋白偏大（1560 aa），表达纯化难度大

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NZM4
- Protein Atlas: https://www.proteinatlas.org/search/BICRA
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BICRA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZM4
- STRING: https://string-db.org/network/9606.BICRA
- Packet data timestamp: 2026-06-03 03:37:05

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000063169-BICRA/subcellular

![](https://images.proteinatlas.org/56211/1168_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/56211/1168_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/56211/1252_F1_4_red_green.jpg)
![](https://images.proteinatlas.org/56211/1252_F1_8_red_green.jpg)
![](https://images.proteinatlas.org/56211/1257_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/56211/1257_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZM4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZM4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052438;IPR015671; |
| Pfam | PF15249; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000063169-BICRA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFYC | Intact, Biogrid | true |
| SMARCA4 | Biogrid, Opencell | true |
| SMARCD1 | Biogrid, Opencell | true |
| ACTL6A | Biogrid | false |
| BCL7C | Biogrid | false |
| BRD3 | Biogrid | false |
| BRD4 | Biogrid | false |
| BRD9 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
