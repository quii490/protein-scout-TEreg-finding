---
type: protein-evaluation
gene: "AATK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AATK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AATK / AATYK, KIAA0641, LMR1, LMTK1 |
| 蛋白名称 | Serine/threonine-protein kinase LMTK1 |
| 蛋白大小 | 1374 aa / 144.6 kDa |
| UniProt ID | Q6ZMQ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; UniProt: Membrane; Cytoplasm; Cytoplasm, perinuclear region |
| 蛋白大小 | 5/10 | ×1 | 5 | 1374 aa / 144.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR042817, IPR000719, IPR017441, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Membrane; Cytoplasm; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endomembrane system (GO:0012505)
- membrane (GO:0016020)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AATYK, KIAA0641, LMR1, LMTK1 |

**关键文献**:
1. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539
2. Epigenetically silenced apoptosis-associated tyrosine kinase (AATK) facilitates a decreased expression of Cyclin D1 and WEE1, phosphorylates TP53 and reduces cell proliferation in a kinase-dependent manner.. *Cancer gene therapy*. PMID: 35902728
3. Contribution of Intronic miR-338-3p and Its Hosting Gene AATK to Compensatory β-Cell Mass Expansion.. *Molecular endocrinology (Baltimore, Md.)*. PMID: 25751313
4. Downregulation of AATK mediates microRNA-558-induced resistance of A549 cells to radiotherapy.. *Molecular medicine reports*. PMID: 27485693
5. Differential Expression of Several miRNAs and the Host Genes AATK and DNM2 in Leukocytes of Sporadic ALS Patients.. *Frontiers in molecular neuroscience*. PMID: 29670510

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.4 |
| 高置信度残基 (pLDDT>90) 占比 | 13.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 73.4% |
| 有序区域 (pLDDT>70) 占比 | 21.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.4），有序残基占 21.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR042817, IPR000719, IPR017441, IPR001245; Pfam: PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK5 | 0.756 | 0.292 | — |
| CDK5R1 | 0.704 | 0.292 | — |
| CSF3 | 0.530 | 0.000 | — |
| IL3 | 0.507 | 0.000 | — |
| PVALEF | 0.451 | 0.000 | — |
| FMR1 | 0.442 | 0.088 | — |
| HTT | 0.437 | 0.000 | — |
| TBC1D9B | 0.432 | 0.000 | — |
| MYADM | 0.412 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| CDK5R1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14521924|imex:IM-20115 |
| Cdk5 | psi-mi:"MI:0096"(pull down) | pubmed:14521924|imex:IM-20115 |
| Stk39 | psi-mi:"MI:0018"(two hybrid) | pubmed:14563843|imex:IM-19534 |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| TEPSIN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC25A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| SLC25A11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| DPM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| P4HA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.4 + PDB: 无 | pLDDT=47.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Cytoplasm, perinuclear region / Mitochondria | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

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
1. AATK — Serine/threonine-protein kinase LMTK1，非常新颖，仅有少数基础研究。
2. 蛋白大小1374 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=47.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZMQ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181409-AATK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AATK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZMQ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000181409-AATK/subcellular

![](https://images.proteinatlas.org/9073/1032_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9073/1032_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9073/44_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9073/44_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9073/46_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9073/46_D7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZMQ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZMQ8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 125..395; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR042817;IPR000719;IPR017441;IPR001245;IPR008266; |
| Pfam | PF07714; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181409-AATK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP1CA | Intact, Biogrid | true |
| PPP1CB | Intact, Biogrid | true |
| PPP1CC | Intact, Biogrid | true |
| TAB1 | Intact, Biogrid | true |
| ATAD3A | Biogrid | false |
| CDK5 | Biogrid | false |
| CDK5R1 | Biogrid | false |
| FBXW11 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
