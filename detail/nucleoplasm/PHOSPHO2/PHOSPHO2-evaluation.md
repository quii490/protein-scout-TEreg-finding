---
type: protein-evaluation
gene: "PHOSPHO2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHOSPHO2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHOSPHO2 |
| 蛋白名称 | Pyridoxal phosphate phosphatase PHOSPHO2 |
| 蛋白大小 | 241 aa / 27.8 kDa |
| UniProt ID | Q8TCD6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 241 aa / 27.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036412, IPR006384, IPR023214, IPR016965; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of key genes and signaling pathways of liver cancer and model construction for prognosis and diagnosis based on bioinformatics analysis.. *PloS one*. PMID: 40465781
2. Sofosbuvir induces gene expression for promoting cell proliferation and migration of hepatocellular carcinoma cells.. *Aging*. PMID: 35833210
3. Overexpression of KLHL23 protein from read-through transcription of PHOSPHO2-KLHL23 in gastric cancer increases cell proliferation.. *FEBS open bio*. PMID: 27833855
4. Bmo-miR-6498-5p suppresses Bombyx mori nucleopolyhedrovirus infection by down-regulating BmPLPP2 to modulate pyridoxal phosphate content in B. mori.. *Insect molecular biology*. PMID: 38335442
5. Association between air pollution exposure and increased chronic kidney disease risk: the modifying effects of genetic susceptibility, transcriptomic, and proteomic signatures.. *BMC medicine*. PMID: 42106700

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.1 |
| 高置信度残基 (pLDDT>90) 占比 | 93.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.1，有序区 98.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036412, IPR006384, IPR023214, IPR016965; Pfam: PF06888 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mviM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SPARC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GKAP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATP5PF | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TSEN15 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| C1QTNF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SIGLEC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CPNE4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNTTIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FLNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.1 + PDB: 无 | pLDDT=96.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PHOSPHO2 — Pyridoxal phosphate phosphatase PHOSPHO2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小241 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCD6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144362-PHOSPHO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHOSPHO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCD6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000144362-PHOSPHO2/subcellular

![](https://images.proteinatlas.org/34726/380_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34726/380_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34726/382_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34726/382_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34726/397_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34726/397_B12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TCD6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
