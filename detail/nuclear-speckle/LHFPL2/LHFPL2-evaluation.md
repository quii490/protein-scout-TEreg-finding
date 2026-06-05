---
type: protein-evaluation
gene: "LHFPL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LHFPL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LHFPL2 / KIAA0206 |
| 蛋白名称 | LHFPL tetraspan subfamily member 2 protein |
| 蛋白大小 | 228 aa / 24.5 kDa |
| UniProt ID | Q6ZUX7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nuclear bodies, Vesicles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 24.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019372; Pfam: PF10242 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nuclear bodies, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- platelet alpha granule membrane (GO:0031092)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0206 |

**关键文献**:
1. Identification of genetic modifiers of age-at-onset for familial Parkinson's disease.. *Human molecular genetics*. PMID: 27402877
2. A novel hepatocellular carcinoma-specific mTORC1-related signature for anticipating prognosis and immunotherapy.. *Aging*. PMID: 37589508
3. CYLD as a key regulator of myocardial infarction-to-heart failure transition revealed by multi-omics integration.. *Frontiers in genetics*. PMID: 40626177
4. Novel function of LHFPL2 in female and male distal reproductive tract development.. *Scientific reports*. PMID: 26964900
5. LHFPL2 Serves as a Potential Biomarker for M2 Polarization of Macrophages in Renal Cell Carcinoma.. *International journal of molecular sciences*. PMID: 38928412

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 44.3% |
| 置信残基 (pLDDT 70-90) 占比 | 37.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.3，有序区 81.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019372; Pfam: PF10242 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APLP2 | 0.491 | 0.000 | — |
| TMEM51 | 0.484 | 0.000 | — |
| RNF182 | 0.476 | 0.000 | — |
| TBC1D30 | 0.476 | 0.000 | — |
| TMEM86A | 0.467 | 0.000 | — |
| HMGA2 | 0.463 | 0.000 | — |
| OCIAD2 | 0.456 | 0.000 | — |
| DUSP3 | 0.450 | 0.000 | — |
| RASSF2 | 0.446 | 0.000 | — |
| PCDH7 | 0.446 | 0.116 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OLFM4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM147 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM128 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GPR152 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SNORC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FXYD6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GAST | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GJB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GJA5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SCARF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 无 | pLDDT=83.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nuclear bodies, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LHFPL2 — LHFPL tetraspan subfamily member 2 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUX7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145685-LHFPL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LHFPL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUX7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000145685-LHFPL2/subcellular

![](https://images.proteinatlas.org/76743/1871_B2_11_cr5b718036a6009_blue_red_green.jpg)
![](https://images.proteinatlas.org/76743/1871_B2_18_cr5b718036a634f_blue_red_green.jpg)
![](https://images.proteinatlas.org/76743/1931_H7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/76743/1931_H7_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/76743/1934_C5_18_cr5d9708a4ee846_blue_red_green.jpg)
![](https://images.proteinatlas.org/76743/1934_C5_33_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZUX7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
