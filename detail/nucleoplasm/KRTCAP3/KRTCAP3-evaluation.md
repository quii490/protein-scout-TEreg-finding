---
type: protein-evaluation
gene: "KRTCAP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KRTCAP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KRTCAP3 / KCP3 |
| 蛋白名称 | Keratinocyte-associated protein 3 |
| 蛋白大小 | 240 aa / 25.6 kDa |
| UniProt ID | Q53RY4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 240 aa / 25.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR020977; Pfam: PF12304 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KCP3 |

**关键文献**:
1. Genome-Wide DNA Methylation and Gene Expression in Patients with Indolent Systemic Mastocytosis.. *International journal of molecular sciences*. PMID: 37762215
2. Keratinocyte-associated protein 3 plays a role in body weight and adiposity with differential effects in males and females.. *Frontiers in genetics*. PMID: 36212147
3. Chronic stress from adolescence to adulthood increases adiposity and anxiety in rats with decreased expression of Krtcap3.. *Frontiers in genetics*. PMID: 38323241
4. Changes in environmental stress over COVID-19 pandemic likely contributed to failure to replicate adiposity phenotype associated with Krtcap3.. *Physiological genomics*. PMID: 37458463
5. Genetic Fine-Mapping and Identification of Candidate Genes and Variants for Adiposity Traits in Outbred Rats.. *Obesity (Silver Spring, Md.)*. PMID: 29193816

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 30.4% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 22.1% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=76.5，有序区 65.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020977; Pfam: PF12304 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC121 | 0.654 | 0.000 | — |
| NRBP1 | 0.626 | 0.000 | — |
| ZNF512 | 0.604 | 0.000 | — |
| TTC22 | 0.591 | 0.000 | — |
| FNDC4 | 0.564 | 0.000 | — |
| ZNF513 | 0.529 | 0.000 | — |
| ZNF888 | 0.527 | 0.000 | — |
| SPATC1L | 0.510 | 0.000 | — |
| TSPEAR | 0.504 | 0.000 | — |
| GTF3C2 | 0.473 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FNDC9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC22A23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLRG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GOSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TSPAN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GOSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TSPAN15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP12A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| REEP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 无 | pLDDT=76.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Cytosol | 一致 |
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
1. KRTCAP3 — Keratinocyte-associated protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小240 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53RY4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157992-KRTCAP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KRTCAP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53RY4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
