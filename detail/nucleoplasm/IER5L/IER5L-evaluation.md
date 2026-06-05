---
type: protein-evaluation
gene: "IER5L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IER5L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IER5L |
| 蛋白名称 | Immediate early response gene 5-like protein |
| 蛋白大小 | 404 aa / 42.1 kDa |
| UniProt ID | Q5T953 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 404 aa / 42.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008653; Pfam: PF05760 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
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
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The PP2A regulator IER5L supports prostate cancer progression.. *Cell death & disease*. PMID: 39025841
2. Construction of a novel radioresistance-related signature for prediction of prognosis, immune microenvironment and anti-tumour drug sensitivity in non-small cell lung cancer.. *Annals of medicine*. PMID: 39797413
3. Identification of Diagnostic Biomarkers and Their Correlation with Immune Infiltration in Age-Related Macular Degeneration.. *Diagnostics (Basel, Switzerland)*. PMID: 34204836
4. IER5L is a Prognostic Biomarker in Pan-Cancer Analysis and Correlates with Immune Infiltration and Immune Molecules in Non-Small Cell Lung Cancer.. *International journal of general medicine*. PMID: 38106972
5. ADAMTSL2 is an independent predictor for the prognosis of gastric cancer.. *Discover oncology*. PMID: 40252157

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.5 |
| 高置信度残基 (pLDDT>90) 占比 | 7.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.1% |
| 中等置信 (pLDDT 50-70) 占比 | 23.5% |
| 低置信 (pLDDT<50) 占比 | 51.5% |
| 有序区域 (pLDDT>70) 占比 | 25.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.5），有序残基占 25.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008653; Pfam: PF05760 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBM14 | 0.430 | 0.000 | — |
| SLC35F3 | 0.425 | 0.000 | — |
| THEG | 0.423 | 0.000 | — |
| PGM2L1 | 0.423 | 0.000 | — |
| TM9SF4 | 0.414 | 0.000 | — |
| NAA25 | 0.402 | 0.000 | — |
| PGBD4 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 3
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.5 + PDB: 无 | pLDDT=56.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 7 + 3 interactions | 数据充分 |

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
1. IER5L — Immediate early response gene 5-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小404 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T953
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188483-IER5L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IER5L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T953
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188483-IER5L/subcellular

![](https://images.proteinatlas.org/21327/146_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/21327/146_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/21327/147_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/21327/147_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/21327/148_C1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T953-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
