---
type: protein-evaluation
gene: "C11orf68"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C11orf68 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C11orf68 / BLES03 |
| 蛋白名称 | UPF0696 protein C11orf68 |
| 蛋白大小 | 292 aa / 31.4 kDa |
| UniProt ID | Q9H3H3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Nucleoli rim; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 31.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.2; PDB: 1ZTP, 2Q4K |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015034, IPR023398; Pfam: PF08939 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Nucleoli rim | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BLES03 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.2 |
| 高置信度残基 (pLDDT>90) 占比 | 70.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 19.9% |
| 有序区域 (pLDDT>70) 占比 | 79.5% |
| 可用 PDB 条目 | 1ZTP, 2Q4K |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1ZTP, 2Q4K）+ AlphaFold高质量预测（pLDDT=82.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015034, IPR023398; Pfam: PF08939 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4H | 0.822 | 0.786 | — |
| EVA1B | 0.470 | 0.000 | — |
| CSDE1 | 0.461 | 0.458 | — |
| NONO | 0.459 | 0.449 | — |
| DRAP1 | 0.431 | 0.000 | — |
| FICD | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF4H | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SH3GL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Bles03 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ZNF341 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PHETA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRAPPC2L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NONO | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLF15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF512B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 15
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.2 + PDB: 1ZTP, 2Q4K | pLDDT=82.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli; 额外: Nucleoli rim | 待确认 |
| PPI | STRING + IntAct | 6 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C11orf68 — UPF0696 protein C11orf68，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

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
| NONO | BioGRID | 1 |
| REL | BioGRID | 1 |
| SDCBP | BioGRID | 1 |
| STRAP | BioGRID | 1 |
| MEOX2 | BioGRID | 1 |
| ZNF341 | BioGRID | 1 |
| KLF15 | BioGRID | 1 |
| MTCL1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C11orf68

### PubMed

**Count: 3**

| PMID | Title |
|---|---|
| 26427334 | A common promoter hypomethylation signature in invasive breast, liver and prostate cancer cell lines reveals novel targets involved in cancer invasive |
| 25062915 | Genome-wide search for eliminylating domains reveals novel function for BLES03-like proteins. |
| 16511166 | The structure at 2.5 A resolution of human basophilic leukemia-expressed protein BLES03. |


