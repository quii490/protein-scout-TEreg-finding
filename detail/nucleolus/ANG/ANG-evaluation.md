---
type: protein-evaluation
gene: "ANG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ANG — REJECTED (研究热度过高 (PubMed strict=9243，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANG / RNASE5 |
| 蛋白名称 | Angiogenin |
| 蛋白大小 | 147 aa / 16.6 kDa |
| UniProt ID | P03950 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Nucleoli rim, Mitotic chromosome; 额外: Actin filame; UniProt: Secreted; Nucleus; Nucleus, nucleolus; Cytoplasm, Stress gra |
| 蛋白大小 | 8/10 | ×1 | 8 | 147 aa / 16.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=9243 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.8; PDB: 1A4Y, 1ANG, 1AWZ, 1B1E, 1B1I, 1B1J, 1GV7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001427, IPR036816, IPR023411, IPR023412; Pfam:  |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim, Mitotic chromosome; 额外: Actin filaments | Approved |
| UniProt | Secreted; Nucleus; Nucleus, nucleolus; Cytoplasm, Stress granule | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- angiogenin-PRI complex (GO:0032311)
- basement membrane (GO:0005604)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- endocytic vesicle (GO:0030139)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9243 |
| PubMed broad count | 52465 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNASE5 |

**关键文献**:
1. Targeting GPR39 in structure-based drug discovery reduces Ang II-induced hypertension.. *Communications biology*. PMID: 39500998
2. Erythropoietin Regulation by Angiotensin II.. *Vitamins and hormones*. PMID: 28629525
3. Angiotensin-(1-7) improves skeletal muscle regeneration.. *European journal of translational myology*. PMID: 38112612
4. Soluble epoxide hydrolase: gene structure, expression and deletion.. *Gene*. PMID: 23701967
5. Angiotensin-(1-7) and its effects in the kidney.. *TheScientificWorldJournal*. PMID: 19578709

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.8 |
| 高置信度残基 (pLDDT>90) 占比 | 79.6% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.0% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 1A4Y, 1ANG, 1AWZ, 1B1E, 1B1I, 1B1J, 1GV7, 1H0D, 1H52, 1H53 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1A4Y, 1ANG, 1AWZ, 1B1E, 1B1I, 1B1J, 1GV7, 1H0D, 1H52, 1H53）+ AlphaFold极高置信度预测（pLDDT=89.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001427, IPR036816, IPR023411, IPR023412; Pfam: PF00074 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNH1 | 0.999 | 0.978 | — |
| RNASE4 | 0.988 | 0.939 | — |
| RNASE2 | 0.926 | 0.000 | — |
| RNASE8 | 0.901 | 0.000 | — |
| RNASE3 | 0.879 | 0.000 | — |
| RNASET2 | 0.829 | 0.000 | — |
| PLXNB2 | 0.806 | 0.000 | — |
| CXCL8 | 0.767 | 0.000 | — |
| RNASEL | 0.740 | 0.000 | — |
| FST | 0.711 | 0.322 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ash2l | psi-mi:"MI:0071"(molecular sieving) | pubmed:21477851|imex:IM-15810 |
| Wdr5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21477851|imex:IM-15810 |
| Pou5f1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21477851|imex:IM-15810 |
| HY5 | psi-mi:"MI:0018"(two hybrid) | pubmed:9659918|imex:IM-20012|m |
| ACTN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15737636 |
| garz | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ATP6AP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PTEN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CRIPTO | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Dmel\CG9368 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 6 / 15 = 40%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 40%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.8 + PDB: 1A4Y, 1ANG, 1AWZ, 1B1E, 1B1I,  | pLDDT=89.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted; Nucleus; Nucleus, nucleolus; Cytoplasm,  / Nucleoli, Nucleoli rim, Mitotic chromosome; 额外: Ac | 一致 |
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
1. ANG — Angiogenin，研究基础较多，新颖性有限。
2. 蛋白大小147 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9243 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 9243 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P03950
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214274-ANG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P03950
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000214274-ANG/subcellular

![](https://images.proteinatlas.org/55896/1144_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/55896/1144_B11_6_red_green.jpg)
![](https://images.proteinatlas.org/55896/893_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/55896/893_E9_3_red_green.jpg)
![](https://images.proteinatlas.org/55896/895_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/55896/895_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P03950-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
