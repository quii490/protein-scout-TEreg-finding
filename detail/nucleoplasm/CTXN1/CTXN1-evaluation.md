---
type: protein-evaluation
gene: "CTXN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTXN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTXN1 / CTXN |
| 蛋白名称 | Cortexin-1 |
| 蛋白大小 | 82 aa / 9.0 kDa |
| UniProt ID | P60606 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Plasma membrane, Cell Junctions; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 82 aa / 9.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR020066; Pfam: PF11057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cell Junctions | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTXN |

**关键文献**:
1. Spatial Proteomics for Further Exploration of Missing Proteins: A Case Study of the Ovary.. *Journal of proteome research*. PMID: 36108145
2. Identification of RP11-770J1.4 as immune-related lncRNA regulating the CTXN1-cGAS-STING axis in histologically lower-grade glioma.. *MedComm*. PMID: 38116063
3. Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC: insights into immune infiltration and therapeutic implications.. *Frontiers in immunology*. PMID: 40977710
4. Identification of a glycolysis- and lactate-related gene signature for predicting prognosis, immune microenvironment, and drug candidates in colon adenocarcinoma.. *Frontiers in cell and developmental biology*. PMID: 36081904

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.4 |
| 高置信度残基 (pLDDT>90) 占比 | 22.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 61.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 37.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.4，有序区 37.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020066; Pfam: PF11057 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAGE1 | 0.620 | 0.000 | — |
| CLBA1 | 0.605 | 0.000 | — |
| SULT4A1 | 0.557 | 0.000 | — |
| SH2D5 | 0.551 | 0.000 | — |
| FRRS1L | 0.498 | 0.000 | — |
| TEKT4 | 0.461 | 0.000 | — |
| CDKL1 | 0.461 | 0.000 | — |
| MAFIP | 0.461 | 0.000 | — |
| CDKL4 | 0.461 | 0.000 | — |
| PROX2 | 0.437 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Gpr50 | psi-mi:"MI:0018"(two hybrid) | pubmed:21858214|imex:IM-26972 |
| ABCC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADCY9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TOM1L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IFNGR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACVR2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BMPR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC26A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLCN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.4 + PDB: 无 | pLDDT=70.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Plasma membrane, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CTXN1 — Cortexin-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小82 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P60606
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178531-CTXN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTXN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60606
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000178531-CTXN1/subcellular

![](https://images.proteinatlas.org/16669/131_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/16669/131_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/16669/132_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/16669/132_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/16669/164_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/16669/164_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
