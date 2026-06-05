---
type: protein-evaluation
gene: "SOWAHB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SOWAHB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOWAHB / ANKRD56 |
| 蛋白名称 | Ankyrin repeat domain-containing protein SOWAHB |
| 蛋白大小 | 793 aa / 85.7 kDa |
| UniProt ID | A6NEL2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 793 aa / 85.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR058889; Pfam: PF12796, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANKRD56 |

**关键文献**:
1. Genome-Wide Association Study of the Genetic Determinants of Emphysema Distribution.. *American journal of respiratory and critical care medicine*. PMID: 27669027
2. Blocking p85β nuclear translocation by importazole enhances Alpelisib efficacy against PIK3CA-helical-domain-mutant tumors.. *Biochemical and biophysical research communications*. PMID: 39823894
3. Integrated analysis of the lncRNA-associated ceRNA network in Alzheimer's disease.. *Gene*. PMID: 37187245
4. Identification and Validation of Cytotoxicity-Related Features to Predict Prognostic and Immunotherapy Response in Patients with Clear Cell Renal Cell Carcinoma.. *Genetics research*. PMID: 39247556
5. A Custom Target Next-Generation Sequencing 70-Gene Panel and Replication Study to Identify Genetic Markers of Diabetic Kidney Disease.. *Genes*. PMID: 34946941

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.7 |
| 高置信度残基 (pLDDT>90) 占比 | 17.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 62.3% |
| 有序区域 (pLDDT>70) 占比 | 30.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.7），有序残基占 30.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR058889; Pfam: PF12796, PF25877 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DIAPH1 | 0.605 | 0.591 | — |
| LRFN1 | 0.557 | 0.091 | — |
| CDC6 | 0.465 | 0.306 | — |
| CDKL2 | 0.465 | 0.000 | — |
| CDK18 | 0.459 | 0.273 | — |
| C1orf210 | 0.454 | 0.091 | — |
| ASCL3 | 0.441 | 0.000 | — |
| CDK3 | 0.440 | 0.273 | — |
| CCNE1 | 0.440 | 0.000 | — |
| CDK6 | 0.440 | 0.273 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EMD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DIAPH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DIAPH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TJP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PDZD11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLEKHA7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAPGEF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DCAF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.7 + PDB: 无 | pLDDT=54.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center | 待确认 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SOWAHB — Ankyrin repeat domain-containing protein SOWAHB，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小793 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NEL2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186212-SOWAHB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOWAHB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NEL2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000186212-SOWAHB/subcellular

![](https://images.proteinatlas.org/36809/1393_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36809/1393_A1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/36809/422_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36809/422_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36809/423_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36809/423_E11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NEL2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
