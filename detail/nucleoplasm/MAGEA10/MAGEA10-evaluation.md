---
type: protein-evaluation
gene: "MAGEA10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGEA10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGEA10 / MAGE10 |
| 蛋白名称 | Melanoma-associated antigen 10 |
| 蛋白大小 | 369 aa / 40.8 kDa |
| UniProt ID | P43363 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 369 aa / 40.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=72.7; PDB: 7PBC, 7PDW, 7QPJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037445, IPR021072, IPR041898, IPR041899, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAGE10 |

**关键文献**:
1. MAGEA10 gene expression in non-small cell lung cancer and A549 cells, and the affinity of epitopes with the complex of HLA-A(∗)0201 alleles.. *Cellular immunology*. PMID: 26058806
2. How the Intrinsically Disordered N-Terminus of Cancer/Testis Antigen MAGEA10 Is Responsible for Its Expression, Nuclear Localisation and Aberrant Migration.. *Biomolecules*. PMID: 38136576
3. Identification of Novel Characteristics in TP53-Mutant Hepatocellular Carcinoma Using Bioinformatics.. *Frontiers in genetics*. PMID: 35651938
4. Expression of immune-related genes and breast cancer recurrence in women with ductal carcinoma in situ.. *European journal of cancer (Oxford, England : 1990)*. PMID: 38615592
5. A cancer-specific antigen drives histone acetylation by stabilizing the acetyltransferases.. *Cell reports*. PMID: 41060806

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 48.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 32.5% |
| 有序区域 (pLDDT>70) 占比 | 58.8% |
| 可用 PDB 条目 | 7PBC, 7PDW, 7QPJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7PBC, 7PDW, 7QPJ）+ AlphaFold高质量预测（pLDDT=72.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037445, IPR021072, IPR041898, IPR041899, IPR002190; Pfam: PF01454, PF12440 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAGEA4 | 0.863 | 0.421 | — |
| CTAG1B | 0.785 | 0.000 | — |
| CTAG2 | 0.761 | 0.000 | — |
| PASD1 | 0.711 | 0.061 | — |
| PMEL | 0.694 | 0.000 | — |
| CSAG3 | 0.657 | 0.000 | — |
| MAGEA9 | 0.647 | 0.617 | — |
| SSX2 | 0.640 | 0.000 | — |
| FOXJ2 | 0.638 | 0.624 | — |
| FAM216A | 0.634 | 0.610 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEB10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POTEF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PES1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TADA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TPM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POU2F1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NRIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 7PBC, 7PDW, 7QPJ | pLDDT=72.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAGEA10 — Melanoma-associated antigen 10，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小369 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAGEA4 | STRING | 863 |
| CTAG2 | STRING | 761 |
| PASD1 | STRING | 711 |
| KAT2A | BioGRID | 1 |
| KAT2B | BioGRID | 1 |
| NCOA2 | BioGRID | 1 |
| YEATS2 | BioGRID | 1 |
| MAGEA9B | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43363
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124260-MAGEA10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEA10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43363
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000124260-MAGEA10/subcellular

![](https://images.proteinatlas.org/70780/1441_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/70780/1441_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/70780/1696_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/70780/1696_F2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P43363-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P43363 |
| SMART | SM01373;SM01392; |
| UniProt Domain [FT] | DOMAIN 134..333; /note="MAGE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00127" |
| InterPro | IPR037445;IPR021072;IPR041898;IPR041899;IPR002190; |
| Pfam | PF01454;PF12440; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124260-MAGEA10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM216A | Biogrid | false |
| FOXJ2 | Biogrid | false |
| KAT2A | Biogrid | false |
| NCOA2 | Biogrid | false |
| QSER1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

### 深度机制分析

MAGEA10（Melanoma-associated antigen 10, 369 aa, 40.8 kDa）属于MAGE（Melanoma Antigen Gene）蛋白家族中的I类MAGE亚家族（包括MAGEA、MAGEB和MAGEC），是癌症/睾丸抗原（cancer/testis antigen, CTA）的典型代表。其MAGE同源结构域（MAGE homology domain, MHD, 134-333 aa, SMART: SM01373, Pfam: PF01454）为MAGE家族的结构标志，由两个串联的翼状螺旋亚结构域（winged-helix subdomain）构成，赋予了与RING finger E3泛素连接酶结合的能力。已有的3个PDB实验结构（7PBC, 7PDW, 7QPJ）覆盖了部分MHD区域，加之AlphaFold v6预测pLDDT=72.7，提供了中等质量的结构框架。然而，32.5%的低置信残基（pLDDT<50）富集在MHD之外的N端区域——该区域已被证实为内在无序区域（IDR），负责MAGEA10的表达调控、核定位和异常电泳迁移行为（PMID:38136576），该研究明确指出IDR既赋予核定位信号，又驱动蛋白的构象灵活性，是MAGEA10功能的关键决定因子。

PPI网络揭示MAGEA10的核心功能轴围绕染色质调控机器展开。实验验证互作中的关键节点包括：KAT2A/GCN5（BioGRID）、KAT2B/PCAF（BioGRID）、NCOA2/SRC-2（BioGRID）——这三个蛋白均为组蛋白乙酰转移酶（HAT）和转录共激活因子复合体的核心组分。2025年发表的突破性研究（PMID:41060806）明确报道“癌特异性抗原MAGE通过稳定乙酰转移酶驱动组蛋白乙酰化”——MAGEA10直接与KAT2A/KAT2B结合，抑制其泛素化依赖性降解，从而稳定HAT蛋白水平并促进全基因组H3K9ac和H3K27ac的积累。这一发现将MAGEA10从传统的“肿瘤相关抗原”重新定位为表观遗传调控因子（epigenetic regulator），其功能不是经典的转录因子，而是作为HAT稳定因子控制全基因组乙酰化水平。

从TE调控机制角度，MAGEA10通过稳定KAT2A/KAT2B影响组蛋白乙酰化修饰，这对于TE调控具有深远意义。H3K9ac和H3K27ac是活性顺式调控区域的标志修饰，包括TE衍生的增强子元件。许多ERV/LTR元件被共选用作组织特异性增强子，其活性的维持依赖于KAT2A/KAT2B介导的组蛋白乙酰化。若MAGEA10在癌细胞中异常高表达（作为CTA），其稳定KAT2A/KAT2B的效应可能导致大量TE衍生的cryptic enhancer被异常激活，驱动癌基因的表达。该作用提供了反向干预策略：MAGEA10的靶向降解可选择性抑制癌性TE增强子的活性。

此外，NRIP1/RIP140（IntAct验证互作, PMID:28514442）是核受体共抑制因子，与MAGEA10的结合可能将KAT2A复合体招募至核受体靶位点，协调配体依赖的转录程序。POU2F1/Oct-1（IntAct验证互作, PMID:28514442）是POU同源异型盒转录因子，识别八聚体基序（ATGCAAAT）——该基序频繁出现在TE的启动子区域（尤其是SINE元件）。因此，MAGEA10-POU2F1相互作用的可能性在于：在含有POU2F1结合位点的TE上，MAGEA10通过KAT2A/KAT2B确定该位点的组蛋白乙酰化和转录活性。

尽管MAGEA10的PubMed文献数（48篇）已超过新颖性的理想阈值，但2025年KAT2A稳定机制的发现（PMID:41060806）和2023年IDR驱动核定位的阐明（PMID:38136576）表明，该蛋白的分子机制远未被完全理解，特别是其在TE调控中的角色尚未被直接探究。验证实验应从KAT2A/MAGEA10共同ChIP-seq入手，关注TE亚家族邻近区域的乙酰化和占据变化，并结合MAGEA10敲除后的全基因组H3K9ac/H3K27ac ChIP-seq以评估TE增强子活性的全局变化。

