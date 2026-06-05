---
type: protein-evaluation
gene: "SUB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUB1 / PC4, RPO2TC1 |
| 蛋白名称 | Activated RNA polymerase II transcriptional coactivator p15 |
| 蛋白大小 | 127 aa / 14.4 kDa |
| UniProt ID | P53999 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 127 aa / 14.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.9; PDB: 1PCF, 2C62, 2PHE, 4USG, 6YCS, 7E4W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003173, IPR009044, IPR045125; Pfam: PF02229 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PC4, RPO2TC1 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.6% |
| 中等置信 (pLDDT 50-70) 占比 | 29.1% |
| 低置信 (pLDDT<50) 占比 | 17.3% |
| 有序区域 (pLDDT>70) 占比 | 53.6% |
| 可用 PDB 条目 | 1PCF, 2C62, 2PHE, 4USG, 6YCS, 7E4W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1PCF, 2C62, 2PHE, 4USG, 6YCS, 7E4W）+ AlphaFold极高置信度预测（pLDDT=75.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003173, IPR009044, IPR045125; Pfam: PF02229 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYMPK | 0.961 | 0.954 | — |
| GTF2B | 0.845 | 0.274 | — |
| CSTF2 | 0.809 | 0.334 | — |
| C11orf58 | 0.778 | 0.000 | — |
| TBP | 0.770 | 0.079 | — |
| TOP1 | 0.714 | 0.185 | — |
| SUPT5H | 0.703 | 0.274 | — |
| EP300 | 0.697 | 0.510 | — |
| CSNK2A1 | 0.696 | 0.362 | — |
| TP53 | 0.660 | 0.306 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000427100.1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PINX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| HDGF | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21907836|imex:IM-17230 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| SOST | psi-mi:"MI:0096"(pull down) | pubmed:22206666|imex:IM-17213 |
| EBI-1568896 | psi-mi:"MI:0435"(protease assay) | imex:IM-11976|pubmed:18083098 |
| Kif1c | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Shoc2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 1PCF, 2C62, 2PHE, 4USG, 6YCS,  | pLDDT=75.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SUB1 — Activated RNA polymerase II transcriptional coactivator p15，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小127 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53999
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113387-SUB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53999
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000113387-SUB1/subcellular

![](https://images.proteinatlas.org/1311/26_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/1311/26_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/1311/27_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/1311/27_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/1311/28_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/1311/28_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53999-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
