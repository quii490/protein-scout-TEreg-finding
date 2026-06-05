---
type: protein-evaluation
gene: "FAM13B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM13B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM13B / C5orf5, FAM13B1 |
| 蛋白名称 | Protein FAM13B |
| 蛋白大小 | 915 aa / 104.5 kDa |
| UniProt ID | Q9NYF5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 915 aa / 104.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039102, IPR059029, IPR008936, IPR000198; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C5orf5, FAM13B1 |

**关键文献**:
1. Biomarkers of Arginine Methylation in Diabetic Nephropathy: Novel Insights from Bioinformatics Analysis.. *Diabetes, metabolic syndrome and obesity : targets and therapy*. PMID: 39290792
2. Identification and Functional Characterization of Essential Genes Related to Gefitinib Sensitivity in Lung Adenocarcinoma.. *Current medicinal chemistry*. PMID: 38584557
3. Decreased FAM13B Expression Increases Atrial Fibrillation Susceptibility by Regulating Sodium Current and Calcium Handling.. *JACC. Basic to translational science*. PMID: 38094680
4. Genetic Control of Left Atrial Gene Expression Yields Insights into the Genetic Susceptibility for Atrial Fibrillation.. *Circulation. Genomic and precision medicine*. PMID: 29545482
5. Differential gene expression in peripheral vascular smooth muscle cells of patients with peripheral artery disease.. *Clinical and experimental nephrology*. PMID: 41123810

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 22.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 48.3% |
| 有序区域 (pLDDT>70) 占比 | 45.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 45.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039102, IPR059029, IPR008936, IPR000198; Pfam: PF26116, PF00620 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAC1 | 0.609 | 0.340 | — |
| CDC42 | 0.603 | 0.340 | — |
| NME5 | 0.602 | 0.000 | — |
| RASA1 | 0.602 | 0.000 | — |
| PKD2L2 | 0.551 | 0.000 | — |
| RETREG1 | 0.518 | 0.000 | — |
| SPATA24 | 0.513 | 0.000 | — |
| C11orf45 | 0.506 | 0.000 | — |
| SH3PXD2A | 0.503 | 0.000 | — |
| SMIM33 | 0.499 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| AHCYL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ATP5ME | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| CHCHD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| HIGD1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PAM16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PPP2CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 无 | pLDDT=61.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM13B — Protein FAM13B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小915 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYF5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000031003-FAM13B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM13B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYF5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000031003-FAM13B/subcellular

![](https://images.proteinatlas.org/41819/682_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/41819/682_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/41819/738_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/41819/738_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/41819/750_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/41819/750_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYF5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
