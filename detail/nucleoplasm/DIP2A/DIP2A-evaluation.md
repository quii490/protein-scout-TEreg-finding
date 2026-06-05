---
type: protein-evaluation
gene: "DIP2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DIP2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIP2A |
| 蛋白名称 | Disco interacting protein 2 homolog A |
| 蛋白大小 | 1581 aa / 171.5 kDa |
| UniProt ID | A0A494C143 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Plasma membrane, Actin filaments, Focal adh; UniProt: Cell projection, neuron projection |
| 蛋白大小 | 5/10 | ×1 | 5 | 1581 aa / 171.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 4/10 | ×2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.0/180** | |
| **归一化总分** | | | **39.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Actin filaments, Focal adhesion sites, Mitochondria | Uncertain |
| UniProt | Cell projection, neuron projection | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 65 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Immune profiling links autoimmune hepatitis to human herpesvirus 6 and relaxin receptor antigens.. *J Exp Med*. PMID: 41774077
2. Integration of Single-cell RNA Sequencing and Mendelian Randomization Analysis for Identifying Potential Immune Therapeutic Targets in Amyotrophic Lateral Sclerosis.. *Biomed Environ Sci*. PMID: 41944768
3. [Baicalin ameliorates obesity-related lung injury by targeting FSTL1/DIP2A signaling pathway].. *Zhongguo Zhong Yao Za Zhi*. PMID: 41814799
4. FSTL1 contribute to aggressive clinical behavior in DLBCL may by activating the DIP2A/ICAM-1-mediated adhesion mechanism.. *Biomed Pharmacother*. PMID: 41616470
5. The FSTL1-DIP2A axis is a significant biomarker for predicting anti-PD1 therapeutic efficacy in advanced gastric cancer.. *Cancer Immunol Immunother*. PMID: 41251805

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |


**PAE**: AlphaFold 数据未获取，无 PAE 可用。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FSTL1 | 0.000 | 0.000 | — |
| HSDL2 | 0.000 | 0.000 | — |
| AASDH | 0.000 | 0.000 | — |
| FST | 0.000 | 0.000 | — |
| YBEY | 0.000 | 0.000 | — |
| NDUFAB1 | 0.000 | 0.000 | — |
| PALB2 | 0.000 | 0.000 | — |
| DMAP1 | 0.000 | 0.000 | — |
| CBFA2T2 | 0.000 | 0.000 | — |
| KIAA0319L | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q62356 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q14689 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:P16401 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q14689-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8NA54 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q14689-4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q14689-6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q7L5A3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O43298 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q15645 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, neuron projection / Nucleoplasm; 额外: Plasma membrane, Actin filaments, | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. DIP2A — Disco interacting protein 2 homolog A，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1581 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A494C143
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160305-DIP2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIP2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A494C143
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000160305-DIP2A/subcellular

![](https://images.proteinatlas.org/44692/1047_D8_5_red_green.jpg)
![](https://images.proteinatlas.org/44692/1047_D8_7_red_green.jpg)
![](https://images.proteinatlas.org/44692/1048_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/44692/1048_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/44692/1592_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/44692/1592_A11_8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
