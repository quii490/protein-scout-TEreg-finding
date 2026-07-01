---
type: protein-evaluation
gene: "ANXA11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANXA11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANXA11 / ANX11 |
| 蛋白名称 | Annexin A11 |
| 蛋白大小 | 505 aa / 54.4 kDa |
| UniProt ID | P50995 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Cytoplasm; Melanosome; Nucleus envelope; Nucleus, nucleoplas |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 54.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.8; PDB: 9FOF, 9FOR |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001464, IPR018502, IPR018252, IPR037104, IPR008 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.0/180** | |
| **归一化总分 (÷1.83)** | | | **75.4/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Cytoplasm; Melanosome; Nucleus envelope; Nucleus, nucleoplasm; Cytoplasm, cytosk... | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- azurophil granule (GO:0042582)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- melanosome (GO:0042470)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 143 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ANX11 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.8 |
| 高置信度残基 (pLDDT>90) 占比 | 59.8% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 33.5% |
| 有序区域 (pLDDT>70) 占比 | 62.6% |
| 可用 PDB 条目 | 9FOF, 9FOR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（9FOF, 9FOR）+ AlphaFold高质量预测（pLDDT=75.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001464, IPR018502, IPR018252, IPR037104, IPR008157; Pfam: PF00191 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| S100A6 | 0.985 | 0.295 | — |
| ANXA7 | 0.920 | 0.000 | — |
| PDCD6 | 0.889 | 0.787 | — |
| BTNL2 | 0.841 | 0.000 | — |
| TFG | 0.700 | 0.628 | — |
| PEF1 | 0.695 | 0.232 | — |
| ALG2 | 0.646 | 0.510 | — |
| HSPA1L | 0.642 | 0.000 | — |
| HLA-DRB1 | 0.637 | 0.166 | — |
| ANXA3 | 0.634 | 0.602 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HNRNPH3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| folC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PDCD6 | psi-mi:"MI:0096"(pull down) | pubmed:18256029|imex:IM-19024 |
| EBI-10981770 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| proW | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-1257121 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |
| EBI-1257123 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.8 + PDB: 9FOF, 9FOR | pLDDT=75.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Melanosome; Nucleus envelope; Nucleus,  / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ANXA11 — Annexin A11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

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
| ANXA7 | STRING | 920 |
| PLSCR1 | BioGRID | 1 |
| HNRNPH3 | BioGRID | 1 |
| SIRT7 | BioGRID | 1 |
| CUL5 | BioGRID | 1 |
| ANXA3 | BioGRID | 1 |
| RPS21 | BioGRID | 1 |
| BAG3 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ANXA11

### PubMed

**Count: 148**

| PMID | Title |
|---|---|
| 42365390 | Lysophagy protects against ANXA11 amyloid fibril toxicity and propagation in FTLD. |
| 42364743 | Annexin A11 C-terminal domain reveals calcium-dependent co-binding to RNA and lipid vesicles. |
| 42349418 | The ALS- and FTD-associated proteins annexin A11 and CHMP2B act sequentially in plasma membrane repair. |
| 42255490 | Integrative Analysis of Genetic Risk Factors for Acute Myeloid Leukemia Using Mendelian Randomization and Single-Cell RNA Sequencing Validation. |
| 42098143 | ANXA11 suppression restores muscular function in the mdx mouse model of Duchenne muscular dystrophy (DMD). |


