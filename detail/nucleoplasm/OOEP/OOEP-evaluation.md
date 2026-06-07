---
type: protein-evaluation
gene: "OOEP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OOEP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OOEP / C6orf156, KHDC2, OEP19 |
| 蛋白名称 | Oocyte-expressed protein homolog |
| 蛋白大小 | 149 aa / 17.2 kDa |
| UniProt ID | A6NGQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 149 aa / 17.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.1; PDB: 8X7V, 8X7W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036612, IPR051778, IPR031952; Pfam: PF16005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.0/180** | |
| **归一化总分** | | | **77.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytoplasmic lattice (GO:0140095)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- subcortical maternal complex (GO:0106333)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf156, KHDC2, OEP19 |

**关键文献**:
1. Mutations in OOEP and NLRP5 identified in infertile patients with early embryonic arrest.. *Human mutation*. PMID: 35946397
2. Gene birth, death, and divergence: the different scenarios of reproduction-related gene evolution.. *Biology of reproduction*. PMID: 19129511
3. Atypical structure and phylogenomic evolution of the new eutherian oocyte- and embryo-expressed KHDC1/DPPA5/ECAT1/OOEP gene family.. *Genomics*. PMID: 17913455
4. Revealing the expression profile of genes that encode the Subcortical Maternal Complex in human reproductive failures.. *Genetics and molecular biology*. PMID: 38091268
5. Maternal-effect gene Ces5/Ooep/Moep19/Floped is essential for oocyte cytoplasmic lattice formation and embryonic development at the maternal-zygotic stage transition.. *Genes to cells : devoted to molecular & cellular mechanisms*. PMID: 20590823

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 59.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 22.8% |
| 低置信 (pLDDT<50) 占比 | 6.7% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 8X7V, 8X7W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8X7V, 8X7W）+ AlphaFold高质量预测（pLDDT=82.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036612, IPR051778, IPR031952; Pfam: PF16005 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLE6 | 0.999 | 0.300 | — |
| NLRP5 | 0.996 | 0.301 | — |
| KHDC3L | 0.987 | 0.292 | — |
| KHDC1 | 0.974 | 0.000 | — |
| PADI6 | 0.965 | 0.000 | — |
| NLRP2 | 0.779 | 0.000 | — |
| ZBED3 | 0.734 | 0.000 | — |
| NLRP7 | 0.635 | 0.000 | — |
| ZAR1 | 0.611 | 0.000 | — |
| DDX43 | 0.547 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AIRIM | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ALOX5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KIF9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCEANC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNRPB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENKD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LONRF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ABI2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 8X7V, 8X7W | pLDDT=82.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. OOEP — Oocyte-expressed protein homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小149 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NGQ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203907-OOEP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OOEP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NGQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NGQ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NGQ2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 49..110; /note="KH; atypical" |
| InterPro | IPR036612;IPR051778;IPR031952; |
| Pfam | PF16005; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203907-OOEP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOX5 | Intact | false |
| C1orf109 | Intact | false |
| ENKD1 | Intact | false |
| KHDC3L | Intact | false |
| KIF9 | Intact | false |
| LONRF1 | Intact | false |
| NTAQ1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
