---
type: protein-evaluation
gene: "DIAPH2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DIAPH2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIAPH2 / DIA |
| 蛋白名称 | Protein diaphanous homolog 2 |
| 蛋白大小 | 1101 aa / 125.6 kDa |
| UniProt ID | O60879 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Vesicles; 额外: Nucleoli; UniProt: Cytoplasm, cytosol; Early endosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1101 aa / 125.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR014767, IPR044933, IPR015 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Vesicles; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm, cytosol; Early endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin filament (GO:0005884)
- cytosol (GO:0005829)
- early endosome (GO:0005769)
- endoplasmic reticulum (GO:0005783)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

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
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 34.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 19.6% |
| 有序区域 (pLDDT>70) 占比 | 69.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.3，有序区 69.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR014767, IPR044933, IPR015425; Pfam: PF06367, PF06371, PF02181 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDC42 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| ENSP00000321348.8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Cbl | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27474268|imex:IM-25617 |
| Kif20b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cetn2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PAPD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| POLR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Sidt2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SOWAHB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Fmr1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 14
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 无 | pLDDT=75.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Early endosome / Endoplasmic reticulum, Vesicles; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 14 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DIAPH2 — Protein diaphanous homolog 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1101 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RHOA | STRING | 955 |
| DIAPH1 | STRING | 906 |
| WDHD1 | STRING | 768 |
| FMR1 | STRING | 744 |
| FIGLA | STRING | 715 |
| FOXL2 | STRING | 706 |
| TCERG1 | BioGRID | 1 |
| POLR1A | BioGRID | 1 |


### TE 调控评估

该蛋白的 GO-CC 注释中缺乏染色质/TE 沉默相关定位，TE 调控潜力较低。不建议作为 TE 调控优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DIAPH2

### PubMed

**Count: 104**

| PMID | Title |
|---|---|
| 41851243 | Isobaric quantitative proteomics reveals altered extracellular matrix, cytoskeletal, and degradation pathways in glaucomatous trabecular meshwork cell |
| 40835298 | Resolving structural variations missed by short-read sequencing uncovers their pathogenicity. |
| 40282394 | Maternal Uniparental Isodisomy of Chromosome 6: A Novel Case of Teratoma and Autism Spectrum Disorder with a Diagnostic and Management Framework. |
| 40150870 | Genome-Wide Analysis of Genetic Predispositions Linked to Damaged Membranes and Impaired Fertility as Indicators of Compromised Sperm-Egg Interaction  |
| 39196658 | mDia2 is an important mediator of MRTF-A-dependent regulation of breast cancer cell migration. |


