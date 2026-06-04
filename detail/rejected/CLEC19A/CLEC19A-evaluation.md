---
type: protein-evaluation
gene: "CLEC19A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLEC19A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLEC19A |
| 蛋白名称 | C-type lectin domain family 19 member A |
| 蛋白大小 | 186 aa / 21.4 kDa |
| UniProt ID | Q6UXS0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 8/10 | ×1 | 8 | 186 aa / 21.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001304, IPR016186, IPR050111, IPR018378, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CLEC19A overexpression inhibits tumor cell proliferation/migration and promotes apoptosis concomitant suppression of PI3K/AKT/NF-κB signaling pathway in glioblastoma multiforme.. *BMC cancer*. PMID: 38167030
2. Genome-wide association study in Finnish twins highlights the connection between nicotine addiction and neurotrophin signaling pathway.. *Addiction biology*. PMID: 29532581
3. Genome-wide association study on detailed profiles of smoking behavior and nicotine dependence in a twin sample.. *Molecular psychiatry*. PMID: 23752247
4. Replication of gene polymorphisms associated with periodontitis-related traits in an elderly cohort: the Washington Heights/Inwood Community Aging Project Ancillary Study of Oral Health.. *Journal of clinical periodontology*. PMID: 35179257

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.1 |
| 高置信度残基 (pLDDT>90) 占比 | 64.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 18.3% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 76.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.1，有序区 76.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001304, IPR016186, IPR050111, IPR018378, IPR033988; Pfam: PF00059 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYT17 | 0.845 | 0.000 | — |
| TM9SF2 | 0.623 | 0.000 | — |
| FNDC7 | 0.589 | 0.000 | — |
| ABHD12B | 0.577 | 0.000 | — |
| ZC3H10 | 0.559 | 0.000 | — |
| CBLN3 | 0.556 | 0.045 | — |
| TMEM69 | 0.549 | 0.000 | — |
| C1QTNF7 | 0.545 | 0.045 | — |
| RBMS3 | 0.544 | 0.000 | — |
| CCDC137 | 0.532 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBXN7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.1 + PDB: 无 | pLDDT=85.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLEC19A — C-type lectin domain family 19 member A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小186 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UXS0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000261210-CLEC19A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLEC19A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UXS0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
