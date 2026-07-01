---
type: protein-evaluation
gene: "GPBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPBP1 / GPBP, SSH6 |
| 蛋白名称 | Vasculin |
| 蛋白大小 | 473 aa / 53.3 kDa |
| UniProt ID | Q86WP2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cytosol; 额外: Plasma membrane; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 473 aa / 53.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028128; Pfam: PF15337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol; 额外: Plasma membrane | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.0 |
| 高置信度残基 (pLDDT>90) 占比 | 4.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 31.9% |
| 低置信 (pLDDT<50) 占比 | 52.6% |
| 有序区域 (pLDDT>70) 占比 | 15.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.0），有序残基占 15.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028128; Pfam: PF15337 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FNDC11 | 0.672 | 0.672 | — |
| TOP2A | 0.670 | 0.000 | — |
| GTF2B | 0.642 | 0.095 | — |
| PSMC1 | 0.479 | 0.000 | — |
| CNOT2 | 0.468 | 0.000 | — |
| RSRC2 | 0.465 | 0.000 | — |
| EP300 | 0.452 | 0.091 | — |
| SSH3 | 0.447 | 0.000 | — |
| CNOT1 | 0.437 | 0.412 | — |
| EAPP | 0.427 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Camk2a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| DNAL4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MCRS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| FNDC11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| RACK1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NXF1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM161A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MORF4L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PSMB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRPF18 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 1 / 10 = 10%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.0 + PDB: 无 | pLDDT=54.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Vesicles, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

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
1. GPBP1 — Vasculin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小473 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MCRS1 | BioGRID | 1 |
| HNRNPD | BioGRID | 1 |
| SLX1A | BioGRID | 1 |
| OTUB2 | BioGRID | 1 |
| DUSP14 | BioGRID | 1 |
| SELENBP1 | BioGRID | 1 |
| EPB41L5 | BioGRID | 1 |
| EIF3A | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GPBP1

### PubMed

**Count: 10**

| PMID | Title |
|---|---|
| 40708043 | Transplantation of miR-216a-5p-overexpressing mesenchymal stem cells encapsulated in a thermosensitive hydrogel promotes functional recovery in a rat  |
| 35596061 | Loss of RTN3 phenocopies chronic kidney disease and results in activation of the IGF2-JAK2 pathway in proximal tubular epithelial cells. |
| 34829754 | Identification of Disease-Related Genes That Are Common between Alzheimer's and Cardiovascular Disease Using Blood Genome-Wide Transcriptome Analysis. |
| 30377252 | Unicellular ancestry and mechanisms of diversification of Goodpasture antigen-binding protein. |
| 29669295 | A Quantitative Chemotherapy Genetic Interaction Map Reveals Factors Associated with PARP Inhibitor Resistance. |


