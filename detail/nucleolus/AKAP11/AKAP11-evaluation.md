---
type: protein-evaluation
gene: "AKAP11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AKAP11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP11 / AKAP220, KIAA0629 |
| 蛋白名称 | A-kinase anchor protein 11 |
| 蛋白大小 | 1901 aa / 210.5 kDa |
| UniProt ID | Q9UKA4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Plasma membrane, Cytosol; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing c |
| 蛋白大小 | 5/10 | ×1 | 5 | 1901 aa / 210.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008382 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AKAP220, KIAA0629 |

**关键文献**:
1. Autophagosomes anchor an AKAP11-dependent regulatory checkpoint that shapes neuronal PKA signaling.. *The EMBO journal*. PMID: 40263600
2. Deep proteomics identifies shared molecular pathway alterations in synapses of patients with schizophrenia and bipolar disorder and mouse model.. *Cell reports*. PMID: 37171958
3. Mouse mutants in schizophrenia risk genes GRIN2A and AKAP11 show EEG abnormalities in common with schizophrenia patients.. *Translational psychiatry*. PMID: 36914641
4. Rare loss-of-function variants in HECTD2 and AKAP11 confer risk of bipolar disorder.. *Nature genetics*. PMID: 40133559
5. Bipolar and schizophrenia risk gene AKAP11 encodes an autophagy receptor coupling the regulation of PKA kinase network homeostasis to synaptic transmission.. *Nature communications*. PMID: 41315293

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.6 |
| 高置信度残基 (pLDDT>90) 占比 | 3.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 64.6% |
| 有序区域 (pLDDT>70) 占比 | 22.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.6），有序残基占 22.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008382 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRKACB | 0.948 | 0.813 | — |
| PRKACA | 0.939 | 0.786 | — |
| IQGAP2 | 0.890 | 0.000 | — |
| AKAP1 | 0.857 | 0.000 | — |
| GSK3B | 0.850 | 0.687 | — |
| PRKAR1A | 0.817 | 0.771 | — |
| PRKAR2B | 0.809 | 0.599 | — |
| PRKACG | 0.775 | 0.225 | — |
| PRKAR2A | 0.738 | 0.518 | — |
| IRX3 | 0.731 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=45.6 + PDB: 无 | pLDDT=45.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, microtubule or / Nucleoli, Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AKAP11 — A-kinase anchor protein 11，非常新颖，仅有少数基础研究。
2. 蛋白大小1901 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=45.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKA4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023516-AKAP11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKA4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000023516-AKAP11/subcellular

![](https://images.proteinatlas.org/39089/436_F7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39089/436_F7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/39089/442_F7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39089/442_F7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39089/521_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39089/521_F7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKA4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKA4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008382; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000023516-AKAP11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GSK3A | Intact, Biogrid | true |
| GSK3B | Biogrid, Opencell | true |
| PRKACA | Biogrid, Opencell | true |
| PRKAR1A | Biogrid, Bioplex | true |
| PRKAR2B | Biogrid, Bioplex | true |
| VAPA | Biogrid, Opencell | true |
| VAPB | Biogrid, Opencell | true |
| CUL3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
