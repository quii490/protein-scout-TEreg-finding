---
type: protein-evaluation
gene: "DENND4A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DENND4A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND4A / IRLB, MYCPBP |
| 蛋白名称 | C-myc promoter-binding protein |
| 蛋白大小 | 1863 aa / 209.2 kDa |
| UniProt ID | Q7Z401 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1863 aa / 209.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001194, IPR005112, IPR043153, IPR051696, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IRLB, MYCPBP |

**关键文献**:
1. Epigenetic Insights into Vascular Cognitive Impairment: DNA Methylation in the Human Brain Tissue.. *Molecular neurobiology*. PMID: 40551051
2. TDP-43 enhances translation of specific mRNAs linked to neurodegenerative disease.. *Nucleic acids research*. PMID: 30357366

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 27.1% |
| 置信残基 (pLDDT 70-90) 占比 | 27.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 38.1% |
| 有序区域 (pLDDT>70) 占比 | 54.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 54.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001194, IPR005112, IPR043153, IPR051696, IPR023341; Pfam: PF03455, PF02141, PF03456 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB10 | 0.721 | 0.098 | — |
| MYC | 0.541 | 0.166 | — |
| METTL6 | 0.526 | 0.526 | — |
| TAF1D | 0.503 | 0.000 | — |
| CAMTA1 | 0.488 | 0.000 | — |
| ANKRD55 | 0.486 | 0.000 | — |
| SYNGR4 | 0.466 | 0.000 | — |
| PDILT | 0.465 | 0.000 | — |
| FBXL4 | 0.461 | 0.000 | — |
| DENND1A | 0.448 | 0.150 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAQ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| A0A0F7RG55 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| C1QTNF9 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| YWHAH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11897|pubmed:17979178 |
| Calm1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEURL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| INTS13 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 无 | pLDDT=64.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DENND4A — C-myc promoter-binding protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1863 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z401
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174485-DENND4A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND4A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z401
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (approved)。来源: https://www.proteinatlas.org/ENSG00000174485-DENND4A/subcellular

![](https://images.proteinatlas.org/65343/1241_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65343/1241_G12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/65343/1320_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65343/1320_H3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/65343/1887_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/65343/1887_B1_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z401-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
