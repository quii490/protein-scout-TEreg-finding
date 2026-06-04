---
type: protein-evaluation
gene: "EFR3A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EFR3A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFR3A |
| 蛋白名称 | Protein EFR3 homolog A |
| 蛋白大小 | 848 aa / 96.1 kDa |
| UniProt ID | A0A1B0GUZ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Cytosol; UniProt: Cell membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 848 aa / 96.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.0; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 20 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Supported |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 31 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Early blood DNA methylation patterns associated with glycemic progression in a prospective Indian cohort.. *Clin Epigenetics*. PMID: 41992370
2. Development of an inhibitory TTC7B selective nanobody that blocks EFR3 recruitment of PI4KA.. *J Biol Chem*. PMID: 41197736
3. Development of an inhibitory TTC7B selective nanobody that blocks EFR3 recruitment of PI4KA.. *bioRxiv*. PMID: 41473329
4. FAST RESENSITIZATION OF G PROTEIN-COUPLED RECEPTORS REQUIRES THEIR PI(4,5)P(2)-DEPENDENT SORTING INTO AN AP2 POSITIVE COMPARTMENT.. *bioRxiv*. PMID: 40568163
5. A Potential Role of EFR3A in Human Disease States.. *Biomolecules*. PMID: 40305161

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.7% |
| 置信残基 (pLDDT 70-90) 占比 | 43.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 19.1% |
| 有序区域 (pLDDT>70) 占比 | 69.1% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=74.0，有序区 69.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTC7A | 0.000 | 0.000 | — |
| PI4KA | 0.000 | 0.000 | — |
| TTC7B | 0.000 | 0.000 | — |
| FAM126A | 0.000 | 0.000 | — |
| FAM126B | 0.000 | 0.000 | — |
| TMEM150A | 0.000 | 0.000 | — |
| OR6X1 | 0.000 | 0.000 | — |
| SYT6 | 0.000 | 0.000 | — |
| PI4KB | 0.000 | 0.000 | — |
| PPP1R17 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q14156 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q14156-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 20，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 20 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 无 | pLDDT=74.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 20 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EFR3A — Protein EFR3 homolog A，非常新颖，仅有少数基础研究。
2. 蛋白大小848 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A1B0GUZ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132294-EFR3A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFR3A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A1B0GUZ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
