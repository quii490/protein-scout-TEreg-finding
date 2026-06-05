---
type: protein-evaluation
gene: "RHEBL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RHEBL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RHEBL1 |
| 蛋白名称 | GTPase RhebL1 |
| 蛋白大小 | 183 aa / 20.7 kDa |
| UniProt ID | Q8TAI7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centrosome; 额外: Nucleoplasm, Nucleoli; UniProt: Endomembrane system; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 183 aa / 20.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.9; PDB: 3OES |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR005225, IPR001806, IPR020849; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Nucleoplasm, Nucleoli | Approved |
| UniProt | Endomembrane system; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endomembrane system (GO:0012505)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Prognostic and immunological role of RHEBL1 in pan-cancer: a target for survival and immunotherapy.. *Discover oncology*. PMID: 40369227
2. Machine learning and bioinformatics-based insights into the potential targets of saponins in Paris polyphylla smith against non-small cell lung cancer.. *Frontiers in genetics*. PMID: 36386821
3. Analysis of mTOR signaling by the small G-proteins, Rheb and RhebL1.. *FEBS letters*. PMID: 16098514
4. Novel involvement of RhebL1 in sphingosylphosphorylcholine-induced keratin phosphorylation and reorganization: Binding to and activation of AKT1.. *Oncotarget*. PMID: 28209923
5. Coordination of Rheb lysosomal membrane interactions with mTORC1 activation.. *F1000Research*. PMID: 32518628

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 83.1% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 3OES |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.9，有序区 94.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR005225, IPR001806, IPR020849; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSC2 | 0.825 | 0.624 | — |
| TSC1 | 0.802 | 0.620 | — |
| MTOR | 0.712 | 0.489 | — |
| RRAGB | 0.674 | 0.045 | — |
| SARS1 | 0.651 | 0.000 | — |
| TXNL4A | 0.599 | 0.599 | — |
| ITSN2 | 0.540 | 0.497 | — |
| ITSN1 | 0.535 | 0.497 | — |
| TBC1D7 | 0.505 | 0.000 | — |
| PDE6D | 0.502 | 0.115 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TXNL4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0096"(pull down) | imex:IM-11703|pubmed:20368287 |
| Appl1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| Blzf1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| PRKAB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FHL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ATXN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| UCHL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 3OES | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endomembrane system; Cytoplasm / Centrosome; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. RHEBL1 — GTPase RhebL1，非常新颖，仅有少数基础研究。
2. 蛋白大小183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAI7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167550-RHEBL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RHEBL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAI7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000167550-RHEBL1/subcellular

![](https://images.proteinatlas.org/61001/1186_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/61001/1186_F1_4_red_green.jpg)
![](https://images.proteinatlas.org/61001/1200_F1_6_red_green.jpg)
![](https://images.proteinatlas.org/61001/1200_F1_8_red_green.jpg)
![](https://images.proteinatlas.org/61001/1269_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/61001/1269_E3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TAI7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
