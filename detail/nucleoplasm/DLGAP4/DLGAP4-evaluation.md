---
type: protein-evaluation
gene: "DLGAP4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DLGAP4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLGAP4 / DAP4, KIAA0964, SAPAP4 |
| 蛋白名称 | Disks large-associated protein 4 |
| 蛋白大小 | 992 aa / 108.0 kDa |
| UniProt ID | Q9Y2H0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Focal adhesion sites; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 992 aa / 108.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005026; Pfam: PF03359 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Focal adhesion sites | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cholinergic synapse (GO:0098981)
- glutamatergic synapse (GO:0098978)
- neuromuscular junction (GO:0031594)
- plasma membrane (GO:0005886)
- postsynaptic specialization (GO:0099572)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAP4, KIAA0964, SAPAP4 |

**关键文献**:
1. Novel role of the synaptic scaffold protein Dlgap4 in ventricular surface integrity and neuronal migration during cortical development.. *Nature communications*. PMID: 35585091
2. Epigenetic remodelling and dysregulation of DLGAP4 is linked with early-onset cerebellar ataxia.. *Human molecular genetics*. PMID: 24986922
3. DLGAP4 acts as an effective prognostic predictor for hepatocellular carcinoma and is closely related to tumour progression.. *Scientific reports*. PMID: 36396671
4. Circular RNA DLGAP4 is down-regulated and negatively correlates with severity, inflammatory cytokine expression and pro-inflammatory gene miR-143 expression in acute ischemic stroke patients.. *International journal of clinical and experimental pathology*. PMID: 31933904
5. Circular RNA as biomarkers for acute ischemic stroke: A systematic review and meta-analysis.. *CNS neuroscience & therapeutics*. PMID: 37186176

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.4 |
| 高置信度残基 (pLDDT>90) 占比 | 9.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 72.8% |
| 有序区域 (pLDDT>70) 占比 | 16.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.4），有序残基占 16.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005026; Pfam: PF03359 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHANK3 | 0.909 | 0.351 | — |
| DLGAP2 | 0.880 | 0.614 | — |
| DLG4 | 0.864 | 0.277 | — |
| DLG3 | 0.857 | 0.435 | — |
| SHANK2 | 0.840 | 0.304 | — |
| DLG2 | 0.785 | 0.067 | — |
| SHANK1 | 0.766 | 0.191 | — |
| DLGAP3 | 0.712 | 0.000 | — |
| HOMER1 | 0.699 | 0.067 | — |
| HOMER3 | 0.619 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Abi1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Dlg4 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlg1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlg3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| UBB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PLK2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP1R1B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.4 + PDB: 无 | pLDDT=49.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Vesicles, Focal adhesion sites | 一致 |
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
1. DLGAP4 — Disks large-associated protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小992 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2H0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000080845-DLGAP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLGAP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2H0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000080845-DLGAP4/subcellular

![](https://images.proteinatlas.org/56378/1050_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/56378/1050_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/56378/2128_G11_45_red_green.jpg)
![](https://images.proteinatlas.org/56378/2128_G11_4_red_green.jpg)
![](https://images.proteinatlas.org/56378/936_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/56378/936_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2H0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y2H0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR005026; |
| Pfam | PF03359; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000080845-DLGAP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BIN1 | Intact, Biogrid | true |
| ALDH16A1 | Biogrid | false |
| DLG4 | Biogrid | false |
| KRAS | Biogrid | false |
| MPP7 | Biogrid | false |
| SHANK3 | Biogrid | false |
| SORBS2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
