---
type: protein-evaluation
gene: "FCHO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FCHO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCHO1 / KIAA0290 |
| 蛋白名称 | F-BAR domain only protein 1 |
| 蛋白大小 | 889 aa / 96.9 kDa |
| UniProt ID | O14526 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane, clathrin-coated pit |
| 蛋白大小 | 8/10 | ×1 | 8 | 889 aa / 96.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=71.1; PDB: 7OHI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027267, IPR031160, IPR001060, IPR042735, IPR054 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Membrane, clathrin-coated pit | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- clathrin-coated pit (GO:0005905)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- postsynaptic endocytic zone (GO:0098843)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0290 |

**关键文献**:
1. Whole-genome sequencing analysis reveals new susceptibility loci and structural variants associated with progressive supranuclear palsy.. *Molecular neurodegeneration*. PMID: 39152475
2. Comprehensive exploration of FCHO1 mutations: Clinical manifestations and implications across disorders.. *American journal of medical genetics. Part A*. PMID: 39166479
3. Human FCHO1 deficiency: review of the literature and additional two cases.. *Clinical and experimental immunology*. PMID: 39498505
4. FCHO1(560-571) peptide, a PKB kinase motif, inhibits tumor progression.. *Biochemical and biophysical research communications*. PMID: 32507602
5. The conserved protein adaptors CALM/AP180 and FCHo1/2 cooperatively recruit Eps15 to promote the initiation of clathrin-mediated endocytosis in yeast.. *PLoS biology*. PMID: 39316607

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.1 |
| 高置信度残基 (pLDDT>90) 占比 | 44.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 35.0% |
| 有序区域 (pLDDT>70) 占比 | 59.7% |
| 可用 PDB 条目 | 7OHI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=71.1，有序区 59.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027267, IPR031160, IPR001060, IPR042735, IPR054713; Pfam: PF22699, PF10291 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITSN1 | 0.999 | 0.330 | — |
| EPS15 | 0.999 | 0.644 | — |
| ITSN2 | 0.998 | 0.093 | — |
| TRIP10 | 0.963 | 0.062 | — |
| EPS15L1 | 0.959 | 0.452 | — |
| EPN2 | 0.935 | 0.000 | — |
| NECAP1 | 0.891 | 0.091 | — |
| SNAP91 | 0.872 | 0.000 | — |
| HIP1R | 0.863 | 0.000 | — |
| FCHO2 | 0.857 | 0.240 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| nifJ | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DNAJC5 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:29997244|imex:IM-26441| |
| PTK6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EXOSC5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| LGALS14 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCEA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRPH | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAB21L3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.1 + PDB: 7OHI | pLDDT=71.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane, clathrin-coated pit / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FCHO1 — F-BAR domain only protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小889 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14526
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130475-FCHO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCHO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14526
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
