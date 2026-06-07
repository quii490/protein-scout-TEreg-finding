---
type: protein-evaluation
gene: "MAGEC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGEC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGEC1 |
| 蛋白名称 | Melanoma-associated antigen C1 |
| 蛋白大小 | 1142 aa / 123.6 kDa |
| UniProt ID | O60732 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1142 aa / 123.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037445, IPR041898, IPR041899, IPR002190; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 112 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of novel epithelial ovarian cancer loci in women of African ancestry.. *International journal of cancer*. PMID: 31469419
2. Identification of Novel Characteristics in TP53-Mutant Hepatocellular Carcinoma Using Bioinformatics.. *Frontiers in genetics*. PMID: 35651938
3. NMD and microRNA expression profiling of the HPCX1 locus reveal MAGEC1 as a candidate prostate cancer predisposition gene.. *BMC cancer*. PMID: 21810217
4. Evaluation of a Novel MAGEC1 Variant and Susceptibility to Ovarian Cancer in the North Indian Population.. *Genetic testing and molecular biomarkers*. PMID: 40626660
5. Gender- and Grade-Dependent Activation of Androgen Receptor Signaling in Adult-Type Diffuse Gliomas: Epigenetic Insights from a Retrospective Cohort Study.. *Biomedicines*. PMID: 41153666

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.5 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 21.7% |
| 低置信 (pLDDT<50) 占比 | 60.8% |
| 有序区域 (pLDDT>70) 占比 | 17.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.5），有序残基占 17.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037445, IPR041898, IPR041899, IPR002190; Pfam: PF01454 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTAG1B | 0.842 | 0.292 | — |
| DSE | 0.828 | 0.000 | — |
| SART1 | 0.810 | 0.000 | — |
| MAGEC2 | 0.795 | 0.000 | — |
| XAGE1A | 0.744 | 0.000 | — |
| CTAG2 | 0.723 | 0.000 | — |
| SSX2 | 0.703 | 0.000 | — |
| SAGE1 | 0.692 | 0.000 | — |
| SSX2B | 0.692 | 0.000 | — |
| SSX1 | 0.682 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTAG1A | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| RUSC2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| GTF2F1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| ECHDC2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| ATP5MG | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| MRPL19 | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| H2AZ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17137291 |
| SUV39H1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AGGF1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.5 + PDB: 无 | pLDDT=48.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAGEC1 — Melanoma-associated antigen C1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1142 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60732
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155495-MAGEC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60732
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000155495-MAGEC1/subcellular

![](https://images.proteinatlas.org/15452/944_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15452/944_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15452/947_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15452/947_C4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/15452/952_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15452/952_C4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60732-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60732 |
| SMART | SM01373; |
| UniProt Domain [FT] | DOMAIN 908..1106; /note="MAGE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00127" |
| InterPro | IPR037445;IPR041898;IPR041899;IPR002190; |
| Pfam | PF01454; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000155495-MAGEC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CTAG1B | Intact, Biogrid | true |
| CTAG1A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
