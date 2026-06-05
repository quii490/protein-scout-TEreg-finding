---
type: protein-evaluation
gene: "TBC1D2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBC1D2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D2 / PARIS1, PP8997, TBC1D2A |
| 蛋白名称 | TBC1 domain family member 2A |
| 蛋白大小 | 928 aa / 105.4 kDa |
| UniProt ID | Q9BYX2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane, Cytosol; UniProt: Cytoplasm; Cytoplasmic vesicle; Cell junction |
| 蛋白大小 | 8/10 | ×1 | 8 | 928 aa / 105.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.8; PDB: 2DHK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR000195, IPR035969, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasmic vesicle; Cell junction | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- anchoring junction (GO:0070161)
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PARIS1, PP8997, TBC1D2A |

**关键文献**:
1. AlphaFold2 SLiM screen for LC3-LIR interactions in autophagy.. *Autophagy*. PMID: 40320752
2. Bioinformatics analysis of oxidative phosphorylation-related differentially expressed genes in osteoporosis.. *European journal of medical research*. PMID: 40241169
3. Genome-wide linkage analysis combined with genome sequencing in large families with intracranial aneurysms.. *European journal of human genetics : EJHG*. PMID: 35228681
4. A meta-validated immune infiltration-related gene model predicts prognosis and immunotherapy sensitivity in HNSCC.. *BMC cancer*. PMID: 36639648
5. Leucine-Rich Repeat Kinase 1 Regulates Autophagy through Turning On TBC1D2-Dependent Rab7 Inactivation.. *Molecular and cellular biology*. PMID: 26100023

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 36.5% |
| 置信残基 (pLDDT 70-90) 占比 | 33.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 69.7% |
| 可用 PDB 条目 | 2DHK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.8，有序区 69.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR000195, IPR035969, IPR050302; Pfam: PF00169, PF00566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB7A | 0.856 | 0.128 | — |
| TBC1D15 | 0.695 | 0.000 | — |
| TBC1D5 | 0.648 | 0.000 | — |
| TBC1D25 | 0.564 | 0.000 | — |
| GABARAPL1 | 0.563 | 0.292 | — |
| VAMP7 | 0.558 | 0.000 | — |
| LRRK1 | 0.554 | 0.113 | — |
| CDC16 | 0.526 | 0.000 | — |
| RAB5A | 0.503 | 0.098 | — |
| TBC1D20 | 0.500 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDC42 | psi-mi:"MI:0018"(two hybrid) | pubmed:21311754|imex:IM-26381 |
| KCTD6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| ZBTB43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KRT40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HMMR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SETDB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SASS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DNAAF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GEMIN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 2DHK | pLDDT=74.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasmic vesicle; Cell junction / Nucleoplasm, Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBC1D2 — TBC1 domain family member 2A，非常新颖，仅有少数基础研究。
2. 蛋白大小928 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000095383-TBC1D2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYX2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000095383-TBC1D2/subcellular

![](https://images.proteinatlas.org/30871/371_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30871/371_D10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30871/372_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30871/372_D10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30871/374_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30871/374_D10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BYX2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
