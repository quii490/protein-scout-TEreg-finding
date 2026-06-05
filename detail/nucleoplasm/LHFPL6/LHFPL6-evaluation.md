---
type: protein-evaluation
gene: "LHFPL6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LHFPL6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LHFPL6 / LHFP |
| 蛋白名称 | LHFPL tetraspan subfamily member 6 protein |
| 蛋白大小 | 200 aa / 21.6 kDa |
| UniProt ID | Q9Y693 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 200 aa / 21.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019372; Pfam: PF10242 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LHFP |

**关键文献**:
1. The causal association between COVID-19 and ischemic stroke: a mendelian randomization study.. *Virology journal*. PMID: 39506873
2. Prognostic Value of LHFPL Tetraspan Subfamily Member 6 (LHFPL6) in Gastric Cancer: A Study Based on Bioinformatics Analysis and Experimental Validation.. *Pharmacogenomics and personalized medicine*. PMID: 34848995
3. Increased IGFBP7 Expression Correlates with Poor Prognosis and Immune Infiltration in Gastric Cancer.. *Journal of Cancer*. PMID: 33531979
4. Probe-based association analysis identifies several deletions associated with average daily gain in beef cattle.. *BMC genomics*. PMID: 30630414
5. Elucidating the roles of TM7SF3 and LHFPL6 in the putative H(+)/OC antiporter function in the human brain capillary endothelial cell line, hCMEC/D3.. *European journal of pharmaceutical sciences : official journal of the European Federation for Pharmaceutical Sciences*. PMID: 41386334

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 78.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 95.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.1，有序区 95.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019372; Pfam: PF10242 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNFRSF10C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ANKRD13D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP13A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTRH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IFITM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BSCL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 6
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 无 | pLDDT=92.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 6 interactions | 数据有限 |

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
1. LHFPL6 — LHFPL tetraspan subfamily member 6 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小200 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y693
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183722-LHFPL6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LHFPL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y693
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000183722-LHFPL6/subcellular

![](https://images.proteinatlas.org/58975/1010_D4_3_red_green.jpg)
![](https://images.proteinatlas.org/58975/1010_D4_4_red_green.jpg)
![](https://images.proteinatlas.org/58975/1014_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/58975/1014_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/58975/1171_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/58975/1171_C5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y693-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
