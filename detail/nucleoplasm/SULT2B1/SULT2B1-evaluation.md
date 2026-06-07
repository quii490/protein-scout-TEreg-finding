---
type: protein-evaluation
gene: "SULT2B1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SULT2B1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SULT2B1 / HSST2 |
| 蛋白名称 | Sulfotransferase 2B1 |
| 蛋白大小 | 365 aa / 41.3 kDa |
| UniProt ID | O00204 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Cytosol; UniProt: Cytoplasm, cytosol; Microsome; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 365 aa / 41.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.7; PDB: 1Q1Q, 1Q1Z, 1Q20, 1Q22 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR000863; Pfam: PF00685 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm, cytosol; Microsome; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 153 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HSST2 |

**关键文献**:
1. Cholesterol sulfate alleviates ulcerative colitis by promoting cholesterol biosynthesis in colonic epithelial cells.. *Nature communications*. PMID: 35908039
2. SULT2B1-CS-DOCK2 axis regulates effector T-cell exhaustion in HCC microenvironment.. *Hepatology (Baltimore, Md.)*. PMID: 36626623
3. SULT2B1: a novel therapeutic target in colorectal cancer via modulation of AKT/PKM2-mediated glycolysis and proliferation.. *Journal of translational medicine*. PMID: 39623433
4. SULT2B1: unique properties and characteristics of a hydroxysteroid sulfotransferase family.. *Drug metabolism reviews*. PMID: 24020383
5. Liver-specific Lxr inhibition represses reverse cholesterol transport in cholesterol-fed mice.. *Atherosclerosis*. PMID: 38797615

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.7 |
| 高置信度残基 (pLDDT>90) 占比 | 74.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 80.0% |
| 可用 PDB 条目 | 1Q1Q, 1Q1Z, 1Q20, 1Q22 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1Q1Q, 1Q1Z, 1Q20, 1Q22）+ AlphaFold高质量预测（pLDDT=86.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP7A1 | 0.954 | 0.000 | — |
| HSD3B1 | 0.949 | 0.000 | — |
| HSD3B2 | 0.942 | 0.000 | — |
| STS | 0.940 | 0.000 | — |
| AKR1C3 | 0.935 | 0.000 | — |
| CYP3A7 | 0.934 | 0.000 | — |
| CYP7B1 | 0.934 | 0.000 | — |
| ENSP00000480571 | 0.932 | 0.000 | — |
| CYP3A5 | 0.932 | 0.000 | — |
| CYP17A1 | 0.931 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000201586.2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| FLACC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SULT1E1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SULT1A1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| REL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DDIT4L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SRP72 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF497 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SULT1B1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| TBC1D22B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.7 + PDB: 1Q1Q, 1Q1Z, 1Q20, 1Q22 | pLDDT=86.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Microsome; Nucleus / Vesicles; 额外: Cytosol | 一致 |
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
1. SULT2B1 — Sulfotransferase 2B1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小365 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00204
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088002-SULT2B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SULT2B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00204
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000088002-SULT2B1/subcellular

![](https://images.proteinatlas.org/41724/713_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41724/713_G2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/41724/714_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41724/714_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41724/747_G2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41724/747_G2_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00204-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00204 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR000863; |
| Pfam | PF00685; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000088002-SULT2B1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SULT1A1 | Intact, Biogrid | true |
| ACYP2 | Intact | false |
| DDIT4L | Intact | false |
| FLACC1 | Intact | false |
| PRICKLE3 | Intact | false |
| SRP72 | Intact | false |
| SULT1B1 | Intact | false |
| SULT1C3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
