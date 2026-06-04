---
type: protein-evaluation
gene: "HARBI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HARBI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HARBI1 / C11orf77 |
| 蛋白名称 | Putative nuclease HARBI1 |
| 蛋白大小 | 349 aa / 39.1 kDa |
| UniProt ID | Q96MB7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 39.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045249, IPR026103, IPR027806; Pfam: PF13359 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf77 |

**关键文献**:
1. Harbinger transposons and an ancient HARBI1 gene derived from a transposase.. *DNA and cell biology*. PMID: 15169610
2. Molecular characterization of shrimp harbinger transposase derived 1 (HARBI1)-like and its role in white spot syndrome virus and Vibrio alginolyticus infection.. *Fish & shellfish immunology*. PMID: 29680489
3. Transposition of a reconstructed Harbinger element in human cells and functional homology with two transposon-derived cellular genes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 18339812
4. MdHARBI1, a MdATG8i-interacting protein, plays a positive role in plant thermotolerance.. *Plant science : an international journal of experimental plant biology*. PMID: 33775357
5. A living fossil in the genome of a living fossil: Harbinger transposons in the coelacanth genome.. *Molecular biology and evolution*. PMID: 22045999

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 63.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 83.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.9，有序区 83.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045249, IPR026103, IPR027806; Pfam: PF13359 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAIF1 | 0.922 | 0.574 | — |
| PGBD5 | 0.663 | 0.000 | — |
| GIN1 | 0.603 | 0.000 | — |
| THAP9 | 0.592 | 0.000 | — |
| QRICH1 | 0.547 | 0.000 | — |
| CENPBD1 | 0.531 | 0.000 | — |
| TIGD2 | 0.521 | 0.000 | — |
| PIGZ | 0.504 | 0.000 | — |
| PRORP | 0.487 | 0.000 | — |
| POGK | 0.479 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NAIF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 无 | pLDDT=84.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. HARBI1 — Putative nuclease HARBI1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MB7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180423-HARBI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HARBI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MB7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
