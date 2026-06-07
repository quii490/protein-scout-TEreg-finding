---
type: protein-evaluation
gene: "LTC4S"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LTC4S — REJECTED (研究热度过高 (PubMed strict=148，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LTC4S |
| 蛋白名称 | Leukotriene C4 synthase |
| 蛋白大小 | 150 aa / 16.6 kDa |
| UniProt ID | Q16873 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Endoplasmic reticulum, Cytosol; UniProt: Nucleus outer membrane; Endoplasmic reticulum membrane; Nucl |
| 蛋白大小 | 8/10 | ×1 | 8 | 150 aa / 16.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=148 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.2; PDB: 2PNO, 2UUH, 2UUI, 3B29, 3HKK, 3LEO, 3PCV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001446, IPR018295, IPR050997, IPR023352, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Endoplasmic reticulum, Cytosol | Approved |
| UniProt | Nucleus outer membrane; Endoplasmic reticulum membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- intracellular membrane-bounded organelle (GO:0043231)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nuclear membrane (GO:0031965)
- nuclear outer membrane (GO:0005640)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 148 |
| PubMed broad count | 214 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Temporal dynamics of the multi-omic response reveals the modulation of macrophage subsets post-myocardial infarction.. *Journal of translational medicine*. PMID: 40640882
2. The -444A/C polymorphism in the LTC4S gene and the risk of asthma: a meta-analysis.. *Archives of medical research*. PMID: 22884858
3. Pharmacogenetics of asthma.. *Current opinion in pulmonary medicine*. PMID: 19077707
4. Biosynthesis of resolvin D1, resolvin D2, and RCTR1 from 7,8(S,S)-epoxytetraene in human neutrophils and macrophages.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39236243
5. Association of ALOX5, LTA4H and LTC4S gene polymorphisms with ischemic stroke risk in a cohort of Chinese in east China.. *World journal of emergency medicine*. PMID: 25215090

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 95.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.6% |
| 可用 PDB 条目 | 2PNO, 2UUH, 2UUI, 3B29, 3HKK, 3LEO, 3PCV, 4BPM, 4J7T, 4J7Y |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2PNO, 2UUH, 2UUI, 3B29, 3HKK, 3LEO, 3PCV, 4BPM, 4J7T, 4J7Y）+ AlphaFold极高置信度预测（pLDDT=97.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001446, IPR018295, IPR050997, IPR023352, IPR001129; Pfam: PF01124 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LTA4H | 0.992 | 0.000 | — |
| ALOX5 | 0.986 | 0.322 | — |
| CYSLTR1 | 0.946 | 0.000 | — |
| MGST1 | 0.932 | 0.230 | — |
| CYSLTR2 | 0.930 | 0.000 | — |
| GGT5 | 0.930 | 0.000 | — |
| GGT1 | 0.921 | 0.000 | — |
| MGST3 | 0.896 | 0.000 | — |
| LTB4R2 | 0.872 | 0.000 | — |
| PTGES | 0.870 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FXYD3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM52B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EBP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CD79A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC7A14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GPR152 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GPR42 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FFAR3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CREB3L1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 2PNO, 2UUH, 2UUI, 3B29, 3HKK,  | pLDDT=97.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus outer membrane; Endoplasmic reticulum memb / Nucleoplasm; 额外: Endoplasmic reticulum, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. LTC4S — Leukotriene C4 synthase，研究基础较多，新颖性有限。
2. 蛋白大小150 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 148 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 148 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16873
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213316-LTC4S/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LTC4S
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16873
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000213316-LTC4S/subcellular

![](https://images.proteinatlas.org/44688/1693_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/44688/1693_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/44688/1877_B3_30_cr5b743c35c5e18_red_green.jpg)
![](https://images.proteinatlas.org/44688/1877_B3_5_cr5b743c35c560a_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16873-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16873 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001446;IPR018295;IPR050997;IPR023352;IPR001129; |
| Pfam | PF01124; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213316-LTC4S/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALOX5 | Biogrid | false |
| CD79A | Intact | false |
| CREB3L1 | Intact | false |
| EBP | Intact | false |
| FFAR3 | Intact | false |
| GPR152 | Intact | false |
| GPR42 | Intact | false |
| SLC7A14 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
