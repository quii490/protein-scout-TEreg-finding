---
type: protein-evaluation
gene: "TSSK1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSSK1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSSK1B / SPOGA1, SPOGA4, STK22A, STK22D, TSSK1 |
| 蛋白名称 | Testis-specific serine/threonine-protein kinase 1 |
| 蛋白大小 | 367 aa / 41.6 kDa |
| UniProt ID | Q9BXA7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies, Principal piece; 额外: Centrosome, Basal body,; UniProt: Cytoplasm; Cytoplasmic vesicle, secretory vesicle, acrosome; |
| 蛋白大小 | 10/10 | ×1 | 10 | 367 aa / 41.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Principal piece; 额外: Centrosome, Basal body, Perinuclear theca, End piece, Annulus | Approved |
| UniProt | Cytoplasm; Cytoplasmic vesicle, secretory vesicle, acrosome; Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- motile cilium (GO:0031514)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPOGA1, SPOGA4, STK22A, STK22D, TSSK1 |

**关键文献**:
1. Role of testis‑specific serine kinase 1B in undiagnosed male infertility.. *Molecular medicine reports*. PMID: 35485285
2. Omics and Male Infertility: Highlighting the Application of Transcriptomic Data.. *Life (Basel, Switzerland)*. PMID: 35207567
3. cDNA cloning, expression and bioinformatical analysis of Tssk genes in tree shrews.. *Computational biology and chemistry*. PMID: 33765466
4. The Biological Characteristics and Differential Expression Patterns of TSSK1B Gene in Yak and Its Infertile Hybrid Offspring.. *Animals : an open access journal from MDPI*. PMID: 36670860
5. The LKB1-TSSK1B axis controls YAP phosphorylation to regulate the Hippo-YAP pathway.. *Cell death & disease*. PMID: 38245531

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 66.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 74.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.4，有序区 74.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| FAM229B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSKS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FOXN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GAPVD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRYBG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPHN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 无 | pLDDT=80.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasmic vesicle, secretory vesicle, / Nuclear bodies, Principal piece; 额外: Centrosome, B | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSSK1B — Testis-specific serine/threonine-protein kinase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小367 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXA7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000212122-TSSK1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSSK1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXA7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000212122-TSSK1B/subcellular

![](https://images.proteinatlas.org/27827/2184_F1_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/27827/2184_F1_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/27827/2201_G1_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/27827/2201_G1_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/27827/2210_E2_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/27827/2210_E2_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXA7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
