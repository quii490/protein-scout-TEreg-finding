---
type: protein-evaluation
gene: "OAZ2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OAZ2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OAZ2 |
| 蛋白名称 | Ornithine decarboxylase antizyme 2 |
| 蛋白大小 | 189 aa / 21.0 kDa |
| UniProt ID | O95190 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 189 aa / 21.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016181, IPR002993, IPR038581; Pfam: PF02100 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular cloning and mRNA expression analysis of ornithine decarboxylase antizyme 2 in ovarian follicles of the Sichuan white goose (Anser cygnoides).. *Gene*. PMID: 24831833
2. Ornithine decarboxylase antizyme Oaz3 modulates protein phosphatase activity.. *The Journal of biological chemistry*. PMID: 21712390
3. Gene polymorphisms in the ornithine decarboxylase-polyamine pathway modify gastric cancer risk by interaction with isoflavone concentrations.. *Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association*. PMID: 25079701
4. Identifying transcript-level differential expression in primary human immune cells.. *Molecular immunology*. PMID: 36527757
5. Effects of promoter methylation on increased expression of polyamine biosynthetic genes in suicide.. *Journal of psychiatric research*. PMID: 23260169

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 50.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 16.4% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 65.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.2，有序区 65.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR002993, IPR038581; Pfam: PF02100 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AZIN1 | 0.992 | 0.757 | — |
| ODC1 | 0.980 | 0.554 | — |
| AZIN2 | 0.960 | 0.532 | — |
| SMOX | 0.613 | 0.000 | — |
| SMS | 0.609 | 0.000 | — |
| PAOX | 0.569 | 0.000 | — |
| OAZ3 | 0.545 | 0.000 | — |
| PSMD12 | 0.527 | 0.000 | — |
| PSMD3 | 0.501 | 0.000 | — |
| PSMC5 | 0.493 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ODC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| AZIN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SYTL3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AZIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDR2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENST00000326005 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 无 | pLDDT=77.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. OAZ2 — Ornithine decarboxylase antizyme 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小189 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95190
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180304-OAZ2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OAZ2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95190
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
