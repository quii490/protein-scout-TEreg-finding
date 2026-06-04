---
type: protein-evaluation
gene: "ID3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ID3 — REJECTED (研究热度过高 (PubMed strict=685，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ID3 / 1R21, BHLHB25, HEIR1 |
| 蛋白名称 | DNA-binding protein inhibitor ID-3 |
| 蛋白大小 | 119 aa / 13.0 kDa |
| UniProt ID | Q02535 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 119 aa / 13.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=685 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 2LFH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR026052, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 685 |
| PubMed broad count | 1137 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: 1R21, BHLHB25, HEIR1 |

**关键文献**:
1. An NK-like CAR T cell transition in CAR T cell dysfunction.. *Cell*. PMID: 34861191
2. Genetic subgroups inform on pathobiology in adult and pediatric Burkitt lymphoma.. *Blood*. PMID: 36201743
3. Heterogenous Populations of Tissue-Resident CD8(+) T Cells Are Generated in Response to Infection and Malignancy.. *Immunity*. PMID: 32433949
4. Single-Cell RNA-Seq Analysis of Cells from Degenerating and Non-Degenerating Intervertebral Discs from the Same Individual Reveals New Biomarkers for Intervertebral Disc Degeneration.. *International journal of molecular sciences*. PMID: 35409356
5. Tissue-infiltrating alloreactive T cells require Id3 to deflect PD-1-mediated immune suppression during GVHD.. *Blood*. PMID: 37871574

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 21.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.1% |
| 中等置信 (pLDDT 50-70) 占比 | 27.7% |
| 低置信 (pLDDT<50) 占比 | 25.2% |
| 有序区域 (pLDDT>70) 占比 | 47.1% |
| 可用 PDB 条目 | 2LFH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 47.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR026052, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCF3 | 0.951 | 0.803 | — |
| TCF4 | 0.906 | 0.774 | — |
| ID1 | 0.871 | 0.091 | — |
| PAX5 | 0.821 | 0.292 | — |
| TCF12 | 0.817 | 0.629 | — |
| NBL1 | 0.699 | 0.000 | — |
| ZBTB18 | 0.681 | 0.000 | — |
| CD79A | 0.634 | 0.000 | — |
| EP300 | 0.628 | 0.000 | — |
| CD27 | 0.606 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000489102.1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| Nphp4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| TSC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17355907|imex:IM-19197 |
| ZNF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| ZNF408 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| ZNF626 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| ATF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| CNOT3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| CSK | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| FHL2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 2LFH | pLDDT=67.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ID3 — DNA-binding protein inhibitor ID-3，研究基础较多，新颖性有限。
2. 蛋白大小119 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 685 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 685 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02535
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117318-ID3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ID3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02535
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
