---
type: protein-evaluation
gene: "LETMD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LETMD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LETMD1 |
| 蛋白名称 | LETM1 domain-containing protein 1 |
| 蛋白大小 | 360 aa / 41.8 kDa |
| UniProt ID | Q6P1Q0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm, Nucleoli; UniProt: Mitochondrion outer membrane; Nucleus; Mitochondrion inner m |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 41.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR033122, IPR044202; Pfam: PF07766 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Mitochondrion outer membrane; Nucleus; Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial outer membrane (GO:0005741)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Architecture of the outbred brown fat proteome defines regulators of metabolic physiology.. *Cell*. PMID: 36334589
2. Mitochondrial matrix protein LETMD1 maintains thermogenic capacity of brown adipose tissue in male mice.. *Nature communications*. PMID: 37353518
3. LETMD1 regulates mitochondrial protein synthesis and import to guard brown fat mitochondrial integrity and function.. *iScience*. PMID: 39398236
4. LETMD1 is required for mitochondrial structure and thermogenic function of brown adipocytes.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 34669999
5. LETMD1 Regulates Phagocytosis and Inflammatory Responses to Lipopolysaccharide via Reactive Oxygen Species Generation and NF-κB Activation in Macrophages.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 31980577

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.3 |
| 高置信度残基 (pLDDT>90) 占比 | 43.3% |
| 置信残基 (pLDDT 70-90) 占比 | 41.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 84.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.3，有序区 84.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033122, IPR044202; Pfam: PF07766 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2D | 0.759 | 0.000 | — |
| SMARCC2 | 0.547 | 0.000 | — |
| TP53 | 0.528 | 0.000 | — |
| WDR59 | 0.495 | 0.000 | — |
| PCGF1 | 0.452 | 0.292 | — |
| MYC | 0.451 | 0.000 | — |
| AFP | 0.440 | 0.000 | — |
| HPS4 | 0.436 | 0.000 | — |
| ARID1B | 0.435 | 0.000 | — |
| LMBR1L | 0.430 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| REEP5 | psi-mi:"MI:0018"(two hybrid) | pubmed:16762630 |
| RTN4IP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CPVL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RHBDD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM167B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UPK1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C3AR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC39A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POMK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APOC4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.3 + PDB: 无 | pLDDT=81.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion outer membrane; Nucleus; Mitochondri / Mitochondria; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LETMD1 — LETM1 domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P1Q0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000050426-LETMD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LETMD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P1Q0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (supported)。来源: https://www.proteinatlas.org/ENSG00000050426-LETMD1/subcellular

![](https://images.proteinatlas.org/74361/1436_G2_5_red_green.jpg)
![](https://images.proteinatlas.org/74361/1436_G2_6_red_green.jpg)
![](https://images.proteinatlas.org/74361/1516_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/74361/1516_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/74361/1876_A9_21_cr5b71682d09483_red_green.jpg)
![](https://images.proteinatlas.org/74361/1876_A9_8_cr5b71682d07627_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P1Q0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
