---
type: protein-evaluation
gene: "HROB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HROB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HROB / C17orf53 |
| 蛋白名称 | Homologous recombination OB-fold protein |
| 蛋白大小 | 647 aa / 69.8 kDa |
| UniProt ID | Q8N3J3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 647 aa / 69.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028045, IPR058570; Pfam: PF15072 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf53 |

**关键文献**:
1. Mechanism of DNA unwinding by MCM8-9 in complex with HROB.. *Nature communications*. PMID: 38678026
2. HROB Is Implicated in DNA Replication.. *Genes*. PMID: 39766854
3. HROB Induces Lung Adenocarcinoma Progression via ZC3HC1-CCNB1 Axis Regulation and Cell Cycle Dysregulation.. *Cancer science*. PMID: 40654113
4. Genetic analysis of novel pathogenic gene HROB in a family with primary ovarian insufficiency.. *Zhejiang da xue xue bao. Yi xue ban = Journal of Zhejiang University. Medical sciences*. PMID: 38105698
5. Mechanism of DNA unwinding by hexameric MCM8-9 in complex with HROB.. *bioRxiv : the preprint server for biology*. PMID: 37398313

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.7 |
| 高置信度残基 (pLDDT>90) 占比 | 14.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 59.2% |
| 有序区域 (pLDDT>70) 占比 | 22.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=54.7），有序残基占 22.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028045, IPR058570; Pfam: PF15072 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCM8 | 0.753 | 0.292 | — |
| MCM8-2 | 0.658 | 0.000 | — |
| MCM9 | 0.613 | 0.292 | — |
| ZBTB40 | 0.530 | 0.000 | — |
| TMEM89 | 0.507 | 0.000 | — |
| FAM199X | 0.447 | 0.000 | — |
| STARD3NL | 0.447 | 0.000 | — |
| FAM210A | 0.445 | 0.000 | — |
| DCDC1 | 0.433 | 0.000 | — |
| FAM71E1 | 0.431 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPRE3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNRD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZPR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MARS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIK3R3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| HYM1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TRIM33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TRIM63 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 12
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.7 + PDB: 无 | pLDDT=54.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HROB — Homologous recombination OB-fold protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小647 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3J3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125319-HROB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HROB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3J3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
