---
type: protein-evaluation
gene: "LRRN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRN3 |
| 蛋白名称 | Leucine-rich repeat neuronal protein 3 |
| 蛋白大小 | 708 aa / 79.4 kDa |
| UniProt ID | Q9H3W5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 708 aa / 79.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000483, IPR003961, IPR036116, IPR007110, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrative eQTL and Mendelian randomization analysis reveals key genetic markers in mesothelioma.. *Respiratory research*. PMID: 40223054
2. Analysis of LRRN3, MEF2C, SLC22A, and P2RY12 Gene Expression in the Peripheral Blood of Patients in the Early Stages of Parkinson's Disease.. *Biomedicines*. PMID: 39061965
3. Identification of PLOD3 and LRRN3 as potential biomarkers for Parkinson's disease based on integrative analysis.. *NPJ Parkinson's disease*. PMID: 37258507
4. Examination of NRCAM, LRRN3, KIAA0716, and LAMB1 as autism candidate genes.. *BMC medical genetics*. PMID: 15128462
5. A Novel Immunomodulatory Mechanism by Which Vitamin D Influences Folate Receptor 3 Expression to Reduce COVID-19 Severity.. *Anticancer research*. PMID: 36192006

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 62.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 11.6% |
| 有序区域 (pLDDT>70) 占比 | 78.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.1，有序区 78.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000483, IPR003961, IPR036116, IPR007110, IPR036179; Pfam: PF00041, PF07679, PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| F2RL3 | 0.576 | 0.091 | — |
| GPR15 | 0.571 | 0.000 | — |
| ADGRL1 | 0.553 | 0.514 | — |
| ADGRL3 | 0.546 | 0.514 | — |
| ADGRL2 | 0.532 | 0.514 | — |
| IMMP2L | 0.521 | 0.000 | — |
| NELL2 | 0.519 | 0.099 | — |
| CLDND1 | 0.507 | 0.000 | — |
| CD4 | 0.482 | 0.100 | — |
| B3GALT2 | 0.478 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 无 | pLDDT=83.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRN3 — Leucine-rich repeat neuronal protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小708 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3W5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173114-LRRN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3W5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000173114-LRRN3/subcellular

![](https://images.proteinatlas.org/46792/1189_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/46792/1189_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/46792/1219_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/46792/1219_C3_3_red_green.jpg)
![](https://images.proteinatlas.org/46792/1368_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/46792/1368_E8_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3W5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
