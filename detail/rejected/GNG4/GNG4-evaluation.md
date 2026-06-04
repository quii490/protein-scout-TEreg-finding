---
type: protein-evaluation
gene: "GNG4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNG4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNG4 / GNGT4 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-4 |
| 蛋白大小 | 75 aa / 8.4 kDa |
| UniProt ID | P50150 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 75 aa / 8.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- heterotrimeric G-protein complex (GO:0005834)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNGT4 |

**关键文献**:
1. Expression of NMU, PPBP and GNG4 in colon cancer and their influences on prognosis.. *Translational cancer research*. PMID: 36388046
2. Relationship between CXCR4 and GNG4 in the Brain and Chronic Stress-Induced Atherosclerosis.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 40694065
3. High GNG4 expression is associated with poor prognosis in patients with lung adenocarcinoma.. *Thoracic cancer*. PMID: 34951127
4. Neurotransmitter Pathway Genes in Cognitive Decline During Aging: Evidence for GNG4 and KCNQ2 Genes.. *American journal of Alzheimer's disease and other dementias*. PMID: 29338302
5. High GNG4 predicts adverse prognosis for osteosarcoma: Bioinformatics prediction and experimental verification.. *Frontiers in oncology*. PMID: 36845726

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.7% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.1，有序区 84.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB5 | 0.999 | 0.996 | — |
| GNB4 | 0.999 | 0.997 | — |
| GNB2 | 0.999 | 0.997 | — |
| GNB1 | 0.999 | 0.997 | — |
| GNB3 | 0.999 | 0.996 | — |
| GNG11 | 0.986 | 0.092 | — |
| GNAS | 0.980 | 0.772 | — |
| GNAI1 | 0.972 | 0.866 | — |
| GNAI3 | 0.965 | 0.865 | — |
| GNAI2 | 0.950 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Kcnk2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23021213|imex:IM-18125 |
| BCAP31 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FHL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GNAI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNAI3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNA11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNAS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.1 + PDB: 无 | pLDDT=88.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNG4 — Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-4，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小75 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50150
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168243-GNG4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNG4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50150
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
