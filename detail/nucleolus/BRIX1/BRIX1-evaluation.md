---
type: protein-evaluation
gene: "BRIX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRIX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRIX1 / BRIX, BXDC2 |
| 蛋白名称 | Ribosome biogenesis protein BRX1 homolog |
| 蛋白大小 | 353 aa / 41.4 kDa |
| UniProt ID | Q8TDN6 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:44:58 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoli, Mitotic chromosome; Un... |
| 蛋白大小 | 10/10 | x1 | 10 | 353 aa / 41.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=14 篇 (<=20->10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=81.3; PDB: 8FKP, 8FKQ, ... |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR007109, IPR026532 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **149.0/180** | |
| **归一化总分 (/1.83)** | | | **81.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoli, Mitotic chromosome | Enhanced |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleolus (GO:0005730)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 353 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRIX, BXDC2 |

**关键文献**:
1. Targeting BRIX1 via Engineered Exosomes Induces Nucleolar Stress to Suppress Cancer Progression.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39475053
2. RRP9 and DDX21 as new biomarkers of colorectal cancer.. *Medicine*. PMID: 37904456
3. Analysis and Validation of Autophagy-Related Gene Biomarkers and Immune Cell Infiltration Characteristic in Bronchopulmonary Dysplasia by Integrating Bioinformatics and Machine Learning.. *Journal of inflammation research*. PMID: 39839185
4. Hepatitis B virus X protein (HBx)-mediated immune modulation and prognostic model development in hepatocellular carcinoma.. *PloS one*. PMID: 40577282
5. BRIX1 promotes ribosome synthesis and enhances glycolysis by selected translation of GLUT1 in colorectal cancer.. *The journal of gene medicine*. PMID: 38282151

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.3 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.5% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 10.2% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 8FKP, 8FKQ, 8FKR, 8FKS, 8FKT, 8FKU, 8FKV, 8FKW, 8FKX, 8FKY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=81.3），结构可信度高。三维结构评分 9/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007109, IPR026532; Pfam: PF04427 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDC42BPB | anti bait coimmunoprecipitation | pubmed:17353931 |
| LYAR | anti bait coimmunoprecipitation | pubmed:17353931 |
| CNBP | anti bait coimmunoprecipitation | pubmed:17353931 |
| HDGF | tandem affinity purification | pubmed:21907836|imex:IM-17230 |
| GABARAP | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| UBE2D1 | two hybrid | imex:IM-11696|pubmed:19549727 |
| UBE2D3 | two hybrid | imex:IM-11696|pubmed:19549727 |
| CTNNB1 | display technology | pubmed:20195357|imex:IM-20475 |
| CUL3 | tandem affinity purification | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2010.11.017 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.3 + PDB: 8FKP, 8FKQ, 8FKR | pLDDT=81.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleoli / Nucleus, nucleolus | 一致 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 81.4/100

**核心优势**:
1. BRIX1 -- Ribosome biogenesis protein BRX1 homolog，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小353 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold高质量预测（pLDDT=81.3），结构可信度高。
4. 已有PDB实验结构：8FKP, 8FKQ, 8FKR。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8TDN6
- Protein Atlas: https://www.proteinatlas.org/search/BRIX1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRIX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDN6
- STRING: https://string-db.org/network/9606.BRIX1
- Packet data timestamp: 2026-06-03 03:44:58

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000113460-BRIX1/subcellular

![](https://images.proteinatlas.org/39614/1888_G3_4_red_green.jpg)
![](https://images.proteinatlas.org/39614/1888_G3_5_red_green.jpg)
![](https://images.proteinatlas.org/39614/454_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/39614/454_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/39614/456_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/39614/456_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TDN6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
