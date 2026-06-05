---
type: protein-evaluation
gene: "IRAK4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## IRAK4 — REJECTED (研究热度过高 (PubMed strict=547，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IRAK4 |
| 蛋白名称 | Interleukin-1 receptor-associated kinase 4 |
| 蛋白大小 | 460 aa / 51.5 kDa |
| UniProt ID | Q9NWZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules, Cytosol; 额外: Nucleoli, Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 460 aa / 51.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=547 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.9; PDB: 2NRU, 2NRY, 2O8Y, 2OIB, 2OIC, 2OID, 3MOP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011029, IPR017428, IPR037970, IPR011009, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Cytosol; 额外: Nucleoli, Plasma membrane | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- extracellular space (GO:0005615)
- extrinsic component of plasma membrane (GO:0019897)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 547 |
| PubMed broad count | 1091 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Flow cytometry-based diagnosis of primary immunodeficiency diseases.. *Allergology international : official journal of the Japanese Society of Allergology*. PMID: 28684198
2. An overview of PROTACs: a promising drug discovery paradigm.. *Molecular biomedicine*. PMID: 36536188
3. Oncogenically active MYD88 mutations in human lymphoma.. *Nature*. PMID: 21179087
4. The Interleukin-1 Receptor-Associated Kinase 4 Inhibitor PF-06650833 Blocks Inflammation in Preclinical Models of Rheumatic Disease and in Humans Enrolled in a Randomized Clinical Trial.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 34423919
5. Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias.. *Science translational medicine*. PMID: 40333990

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 60.9% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 12.0% |
| 有序区域 (pLDDT>70) 占比 | 83.7% |
| 可用 PDB 条目 | 2NRU, 2NRY, 2O8Y, 2OIB, 2OIC, 2OID, 3MOP, 4RMZ, 4U97, 4U9A |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2NRU, 2NRY, 2O8Y, 2OIB, 2OIC, 2OID, 3MOP, 4RMZ, 4U97, 4U9A）+ AlphaFold极高置信度预测（pLDDT=83.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011029, IPR017428, IPR037970, IPR011009, IPR051824; Pfam: PF07714 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLR4 | 0.999 | 0.540 | — |
| MYD88 | 0.999 | 0.991 | — |
| IKBKG | 0.999 | 0.994 | — |
| IRAK2 | 0.999 | 0.970 | — |
| TRAF6 | 0.999 | 0.535 | — |
| IRAK1 | 0.999 | 0.875 | — |
| IRF7 | 0.996 | 0.094 | — |
| IL1R1 | 0.996 | 0.345 | — |
| PELI1 | 0.995 | 0.838 | — |
| TIRAP | 0.995 | 0.617 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PELI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12496252 |
| MYD88 | psi-mi:"MI:0018"(two hybrid) | pubmed:12860405 |
| PELI2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12860405 |
| IRAK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12860405 |
| TBPL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ARNT | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TIRAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| IRAK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| VSIG8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF597 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 2NRU, 2NRY, 2O8Y, 2OIB, 2OIC,  | pLDDT=83.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Microtubules, Cytosol; 额外: Nucleoli, Plasma membra | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. IRAK4 — Interleukin-1 receptor-associated kinase 4，研究基础较多，新颖性有限。
2. 蛋白大小460 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 547 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 547 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198001-IRAK4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IRAK4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (approved)。来源: https://www.proteinatlas.org/ENSG00000198001-IRAK4/subcellular

![](https://images.proteinatlas.org/16685/634_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16685/634_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16685/635_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16685/635_H2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/16685/639_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16685/639_H2_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NWZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
