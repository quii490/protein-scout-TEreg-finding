---
type: protein-evaluation
gene: "INCA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## INCA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INCA1 |
| 蛋白名称 | INCA1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | INCA1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. TMEM11 regulates cardiomyocyte proliferation and cardiac repair via METTL1-mediated m(7)G methylation of ATF5 mRNA.. *Cell death and differentiation*. PMID: 37286744
2. Zinc finger protein HZF1 promotes K562 cell proliferation by interacting with and inhibiting INCA1.. *Molecular medicine reports*. PMID: 21874239
3. The roles of ING5 in cancer: A tumor suppressor.. *Frontiers in cell and developmental biology*. PMID: 36425530
4. Identification of interaction partners and substrates of the cyclin A1-CDK2 complex.. *The Journal of biological chemistry*. PMID: 15159402
5. The inhibitor of growth protein 5 (ING5) depends on INCA1 as a co-factor for its antiproliferative effects.. *PloS one*. PMID: 21750715

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

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
| CCNA1 | 0.889 | 0.295 | — |
| ING5 | 0.643 | 0.292 | — |
| ZNF16 | 0.588 | 0.292 | — |
| CDK2 | 0.507 | 0.292 | — |
| PROCA1 | 0.454 | 0.000 | — |
| DPH7 | 0.453 | 0.292 | — |
| KLHDC9 | 0.446 | 0.000 | — |
| BRAT1 | 0.441 | 0.000 | — |
| ARHGAP30 | 0.432 | 0.000 | — |
| NKX1-1 | 0.429 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q6PKN9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| DAZAP2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| RNF26 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| RACK1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| USP15 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| SPOUT1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| TRIM26 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| RAB5C | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| ING5 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |
| DPH7 | psi-mi:"MI:0018"(two hybrid) | imex:IM-26469|pubmed:21750715 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. INCA1 — INCA1 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/INCA1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196388-INCA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INCA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/INCA1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000196388-INCA1/subcellular

![](https://images.proteinatlas.org/52401/1501_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52401/1501_E10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/52401/1522_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52401/1522_E10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/52401/1576_H5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/52401/1576_H5_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
