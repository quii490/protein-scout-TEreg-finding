---
type: protein-evaluation
gene: "SIRPB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SIRPB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIRPB2 / SIRPB2 |
| 蛋白名称 | Signal-regulatory protein gamma |
| 蛋白大小 | 387 aa / 42.5 kDa |
| UniProt ID | Q9P1W8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 387 aa / 42.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.5; PDB: 2JJW, 4I2X |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051755, IPR007110, IPR036179, IPR013783, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SIRPB2 |

**关键文献**:
1. Identification of a ferroptosis-related lncRNA signature with prognosis for Wilms tumor.. *Translational pediatrics*. PMID: 34765465
2. Molecular Mechanisms Underlying Differences in Athletic Ability in Racehorses Based on Whole Transcriptome Sequencing.. *Biology*. PMID: 41154767
3. Computational Analysis of the Immune Infiltration Pattern and Candidate Diagnostic Biomarkers in Lumbar Disc Herniation.. *Frontiers in molecular neuroscience*. PMID: 35531067
4. Molecular cloning of a novel human gene (SIRP-B2) which encodes a new member of the SIRP/SHPS-1 protein family.. *Journal of human genetics*. PMID: 11185750

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 69.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 11.9% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 2JJW, 4I2X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2JJW, 4I2X）+ AlphaFold高质量预测（pLDDT=85.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051755, IPR007110, IPR036179, IPR013783, IPR003597; Pfam: PF07654, PF07686 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD79A | 0.520 | 0.478 | — |
| CD79B | 0.517 | 0.478 | — |
| FCGR3B | 0.481 | 0.410 | — |
| FCGR3A | 0.480 | 0.410 | — |
| PRNP | 0.469 | 0.469 | — |
| CD47 | 0.433 | 0.210 | — |
| C1QC | 0.415 | 0.299 | — |
| MAPT | 0.404 | 0.404 | — |
| MAP2 | 0.404 | 0.404 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIRPG | psi-mi:"MI:0054"(fluorescence-activated cell sorti | pubmed:15383453 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 2JJW, 4I2X | pLDDT=85.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SIRPB2 — Signal-regulatory protein gamma，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小387 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P1W8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196209-SIRPB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIRPB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P1W8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000196209-SIRPB2/subcellular

![](https://images.proteinatlas.org/48032/1300_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48032/1300_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48032/1365_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48032/1365_C9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/48032/1790_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48032/1790_F4_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P1W8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
