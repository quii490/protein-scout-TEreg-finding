---
type: protein-evaluation
gene: "DLX6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLX6 — REJECTED (研究热度过高 (PubMed strict=169，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLX6 |
| 蛋白名称 | Homeobox protein DLX-6 |
| 蛋白大小 | 175 aa / 19.7 kDa |
| UniProt ID | P56179 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 175 aa / 19.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=169 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050460, IPR001356, IPR020479, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 169 |
| PubMed broad count | 341 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Research progress of DLX6-AS1 in human cancers.. *Human cell*. PMID: 34508305
2. Subtype-selective electroporation of cortical interneurons.. *Journal of visualized experiments : JoVE*. PMID: 25177832
3. Multiple functions of Dlx genes.. *The International journal of developmental biology*. PMID: 11061425
4. DLX5 and DLX6 expression is biallelic and not modulated by MeCP2 deficiency.. *American journal of human genetics*. PMID: 17701895
5. DANCR promotes glioma cell autophagy and proliferation via the miR‑33b/DLX6/ATG7 axis.. *Oncology reports*. PMID: 36601767

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 32.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 33.1% |
| 低置信 (pLDDT<50) 占比 | 28.0% |
| 有序区域 (pLDDT>70) 占比 | 38.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 38.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050460, IPR001356, IPR020479, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLX5 | 0.939 | 0.000 | — |
| RUNX2 | 0.828 | 0.000 | — |
| SEM1 | 0.822 | 0.000 | — |
| BMP2 | 0.787 | 0.000 | — |
| MECP2 | 0.741 | 0.000 | — |
| TP63 | 0.725 | 0.000 | — |
| HAND2 | 0.673 | 0.000 | — |
| DYNC1I1 | 0.664 | 0.000 | — |
| BMP7 | 0.663 | 0.000 | — |
| PEG10 | 0.635 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| SCGB2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATG7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CALCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEMG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| XRCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CBX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEMG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CSTF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EEF1A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 无 | pLDDT=68.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLX6 — Homeobox protein DLX-6，研究基础较多，新颖性有限。
2. 蛋白大小175 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 169 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 169 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56179
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006377-DLX6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLX6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56179
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
