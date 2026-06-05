---
type: protein-evaluation
gene: "GNL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNL1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNL1 |
| 蛋白名称 | GNL1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | GNL1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Interplay between human nucleolar GNL1 and RPS20 is critical to modulate cell proliferation.. *Scientific reports*. PMID: 30061673
2. Guanine nucleotide binding protein like-1 (GNL1) promotes cancer cell proliferation and survival through AKT/p21 (CIP1) signaling cascade.. *Molecular biology of the cell*. PMID: 33147101
3. Distinct ADP-ribosylation factor-GTP exchange factors govern the opposite polarity of 2 receptor kinases.. *Plant physiology*. PMID: 37787604
4. Are Traditional mutant controls sufficient to identify true RNA G-quadruplex binding proteins?. *Biochimie*. PMID: 41183740
5. N-terminal domain of ARF-GEF GNOM prevents heterodimerization with functionally divergent GNL1 in Arabidopsis.. *The Plant journal : for cell and molecular biology*. PMID: 36106415

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF1A1 | 0.969 | 0.000 | — |
| NMD3 | 0.947 | 0.819 | — |
| PA2G4 | 0.894 | 0.799 | — |
| GTPBP4 | 0.886 | 0.502 | — |
| BOP1 | 0.880 | 0.482 | — |
| EIF6 | 0.875 | 0.806 | — |
| RPL5 | 0.852 | 0.805 | — |
| PES1 | 0.850 | 0.557 | — |
| NOC2L | 0.848 | 0.482 | — |
| HSF1 | 0.840 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNF212 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| GDI1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| PTP4A1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| Mical3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| FAU | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| KLHL40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TULP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC2A12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DYNC1I2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Vesicles | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNL1 — GNL1 (UniProt未获取)，非常新颖，仅有少数基础研究。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/GNL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204590-GNL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/GNL1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000204590-GNL1/subcellular

![](https://images.proteinatlas.org/50455/711_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50455/711_C4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/50455/723_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50455/723_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50455/866_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50455/866_C4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
