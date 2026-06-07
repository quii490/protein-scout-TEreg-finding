---
type: protein-evaluation
gene: "LRRC31"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC31 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC31 |
| 蛋白名称 | Leucine-rich repeat-containing protein 31 |
| 蛋白大小 | 552 aa / 61.5 kDa |
| UniProt ID | Q6UY01 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 552 aa / 61.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR042419, IPR032675; Pfam: PF13516 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. BDH1-mediated LRRC31 regulation dependent on histone lysine β-hydroxybutyrylation to promote lung adenocarcinoma progression.. *MedComm*. PMID: 38098610
2. LRRC31 inhibits DNA repair and sensitizes breast cancer brain metastasis to radiation therapy.. *Nature cell biology*. PMID: 33005030
3. LRRC31 is induced by IL-13 and regulates kallikrein expression and barrier function in the esophageal epithelium.. *Mucosal immunology*. PMID: 26462420
4. Terc Gene Cluster Variants Predict Liver Telomere Length in Mice.. *Cells*. PMID: 34685603
5. Comprehensive Analysis of NAFLD and the Therapeutic Target Identified.. *Frontiers in cell and developmental biology*. PMID: 34616724

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.6 |
| 高置信度残基 (pLDDT>90) 占比 | 71.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 11.6% |
| 有序区域 (pLDDT>70) 占比 | 86.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.6，有序区 86.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR042419, IPR032675; Pfam: PF13516 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRIQ4 | 0.708 | 0.000 | — |
| LRRC34 | 0.652 | 0.000 | — |
| XRCC5 | 0.620 | 0.292 | — |
| XRCC6 | 0.620 | 0.292 | — |
| MYNN | 0.584 | 0.000 | — |
| CAPN14 | 0.571 | 0.000 | — |
| TMEM174 | 0.558 | 0.000 | — |
| ACTRT3 | 0.525 | 0.114 | — |
| TRIP10 | 0.514 | 0.514 | — |
| CEP295NL | 0.501 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PARP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| V9HW14 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| CFTR | psi-mi:"MI:0030"(cross-linking study) | pubmed:31324722|imex:IM-29200 |
| BMI1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.6 + PDB: 无 | pLDDT=85.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC31 — Leucine-rich repeat-containing protein 31，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小552 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UY01
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114248-LRRC31/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UY01
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LRRC31/IF_images/HAP1_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LRRC31/IF_images/OE19_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000114248-LRRC31/subcellular

![](https://images.proteinatlas.org/58013/1919_A5_10_red_green.jpg)
![](https://images.proteinatlas.org/58013/1919_A5_9_red_green.jpg)
![](https://images.proteinatlas.org/58013/1973_E7_26_red_green.jpg)
![](https://images.proteinatlas.org/58013/1973_E7_27_red_green.jpg)
![](https://images.proteinatlas.org/58013/2038_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/58013/2038_C1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UY01-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UY01 |
| SMART | SM00368; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR042419;IPR032675; |
| Pfam | PF13516; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114248-LRRC31/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
