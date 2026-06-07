---
type: protein-evaluation
gene: "PCP4L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCP4L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCP4L1 / IQM1 |
| 蛋白名称 | Purkinje cell protein 4-like protein 1 |
| 蛋白大小 | 68 aa / 7.5 kDa |
| UniProt ID | A6NKN8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 68 aa / 7.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052142 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IQM1 |

**关键文献**:
1. Whole-transcriptome analysis reveals a potential hsa_circ_0001955/hsa_circ_0000977-mediated miRNA-mRNA regulatory sub-network in colorectal cancer.. *Aging*. PMID: 32221048
2. Pcp4l1 contains an auto-inhibitory element that prevents its IQ motif from binding to calmodulin.. *Journal of neurochemistry*. PMID: 22458599
3. Pcp4l1, a novel gene encoding a Pcp4-like polypeptide, is expressed in specific domains of the developing brain.. *Gene expression patterns : GEP*. PMID: 15053978
4. lncRNA EDAL restricts rabies lyssavirus replication in a cell-specific and infection route-dependent manner.. *The Journal of general virology*. PMID: 35234607
5. Differences in global gene expression in muscle tissue of Nellore cattle with divergent meat tenderness.. *BMC genomics*. PMID: 29202705

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.5 |
| 高置信度残基 (pLDDT>90) 占比 | 36.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 33.8% |
| 低置信 (pLDDT<50) 占比 | 17.6% |
| 有序区域 (pLDDT>70) 占比 | 48.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.5，有序区 48.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052142 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM192 | 0.516 | 0.105 | — |
| BPIFB3 | 0.494 | 0.000 | — |
| NIM1K | 0.487 | 0.091 | — |
| GPR26 | 0.486 | 0.000 | — |
| NDUFS2 | 0.464 | 0.310 | — |
| IGFALS | 0.444 | 0.095 | — |
| VSTM2B | 0.418 | 0.000 | — |
| SLC41A3 | 0.411 | 0.000 | — |
| SLC16A7 | 0.404 | 0.000 | — |
| OR5BS1P | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 2
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.5 + PDB: 无 | pLDDT=71.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Mitochondria | 待确认 |
| PPI | STRING + IntAct | 10 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PCP4L1 — Purkinje cell protein 4-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小68 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NKN8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000248485-PCP4L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCP4L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NKN8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000248485-PCP4L1/subcellular

![](https://images.proteinatlas.org/52833/1016_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/52833/1016_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/52833/1239_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/52833/1239_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NKN8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NKN8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 45..68; /note="IQ" |
| InterPro | IPR052142; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000248485-PCP4L1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
