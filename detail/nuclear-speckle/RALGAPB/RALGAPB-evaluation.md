---
type: protein-evaluation
gene: "RALGAPB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RALGAPB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RALGAPB / KIAA1219 |
| 蛋白名称 | Ral GTPase-activating protein subunit beta |
| 蛋白大小 | 1494 aa / 166.8 kDa |
| UniProt ID | Q86X10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1494 aa / 166.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.7; PDB: 9QWP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039930, IPR035974, IPR000331, IPR046859; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1219 |

**关键文献**:
1. Inherited and multiple de novo mutations in autism/developmental delay risk genes suggest a multifactorial model.. *Molecular autism*. PMID: 30564305
2. Excess of RALGAPB de novo variants in neurodevelopmental disorders.. *European journal of medical genetics*. PMID: 32853829
3. RalA controls glucose homeostasis by regulating glucose uptake in brown fat.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 29915037
4. Rare CNVs and Known Genes Linked to Macrocephaly: Review of Genomic Loci and Promising Candidate Genes.. *Genes*. PMID: 36553552
5. The Potential of NORAD-PUMILIO-RALGAPB Regulatory Axis as a Biomarker in Breast Cancer.. *Non-coding RNA*. PMID: 36412911

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.7 |
| 高置信度残基 (pLDDT>90) 占比 | 38.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 69.5% |
| 可用 PDB 条目 | 9QWP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.7，有序区 69.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039930, IPR035974, IPR000331, IPR046859; Pfam: PF20412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RALGAPA2 | 0.964 | 0.292 | — |
| RALA | 0.892 | 0.000 | — |
| RALGAPA1 | 0.825 | 0.292 | — |
| AKT2 | 0.775 | 0.000 | — |
| RNF111 | 0.736 | 0.000 | — |
| DIP2B | 0.720 | 0.000 | — |
| TMEM131 | 0.702 | 0.000 | — |
| NKIRAS2 | 0.686 | 0.620 | — |
| SCAF8 | 0.649 | 0.000 | — |
| DIDO1 | 0.625 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| RAB11A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DPH7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| GOPC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SERPINB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.7 + PDB: 9QWP | pLDDT=74.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RALGAPB — Ral GTPase-activating protein subunit beta，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1494 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86X10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170471-RALGAPB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RALGAPB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86X10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000170471-RALGAPB/subcellular

![](https://images.proteinatlas.org/51454/1028_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/51454/1028_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/51454/802_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/51454/802_C9_3_red_green.jpg)
![](https://images.proteinatlas.org/51454/908_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/51454/908_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86X10-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
