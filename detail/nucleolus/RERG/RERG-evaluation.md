---
type: protein-evaluation
gene: "RERG"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RERG 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RERG |
| 蛋白名称 | Ras-related and estrogen-regulated growth inhibitor |
| 蛋白大小 | 199 aa / 22.6 kDa |
| UniProt ID | Q96A58 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli fibrillar center; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 199 aa / 22.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.8; PDB: 2ATV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR051065, IPR005225, IPR001806; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli fibrillar center | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 89 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Inflammation and cancer.. *Environmental health and preventive medicine*. PMID: 30340457
2. Construction of a novel radioresistance-related signature for prediction of prognosis, immune microenvironment and anti-tumour drug sensitivity in non-small cell lung cancer.. *Annals of medicine*. PMID: 39797413
3. Expression of the RERG gene is gender-dependent in hepatocellular carcinoma and regulated by histone deacetyltransferases.. *Journal of Korean medical science*. PMID: 17043425
4. Expression of CRABP1, GRP, and RERG mRNA in clinically non-functioning and functioning pituitary adenomas.. *Journal of endocrinological investigation*. PMID: 21270509
5. RERG is a novel ras-related, estrogen-regulated and growth-inhibitory gene in breast cancer.. *The Journal of biological chemistry*. PMID: 11533059

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 76.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 90.5% |
| 可用 PDB 条目 | 2ATV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.8，有序区 90.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR051065, IPR005225, IPR001806; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.600 | 0.073 | — |
| PHLPP2 | 0.549 | 0.138 | — |
| ITSN2 | 0.540 | 0.497 | — |
| ITSN1 | 0.535 | 0.497 | — |
| ARHGEF17 | 0.434 | 0.424 | — |
| ABHD14B | 0.428 | 0.052 | — |
| ZNF549 | 0.422 | 0.079 | — |
| INSIG1 | 0.406 | 0.052 | — |
| MED7 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000441505.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ARHGEF17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 2
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 2ATV | pLDDT=90.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol; 额外: Nucleoli fibrillar cente | 一致 |
| PPI | STRING + IntAct | 9 + 2 interactions | 数据充分 |

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
1. RERG — Ras-related and estrogen-regulated growth inhibitor，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96A58
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134533-RERG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RERG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A58
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000134533-RERG/subcellular

![](https://images.proteinatlas.org/41387/1645_H2_10_cr57bd8c3197296_red_green.jpg)
![](https://images.proteinatlas.org/41387/1645_H2_5_cr57bd8c2b7d6f8_red_green.jpg)
![](https://images.proteinatlas.org/41387/1907_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/41387/1907_G2_4_red_green.jpg)
![](https://images.proteinatlas.org/41387/493_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/41387/493_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96A58-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
