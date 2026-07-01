---
type: protein-evaluation
gene: "GIN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GIN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GIN1 / TGIN1, ZH2C2 |
| 蛋白名称 | Gypsy retrotransposon integrase-like protein 1 |
| 蛋白大小 | 522 aa / 59.8 kDa |
| UniProt ID | Q9NXP7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 522 aa / 59.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001584, IPR041588, IPR050951, IPR012337, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
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
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.3 |
| 高置信度残基 (pLDDT>90) 占比 | 28.5% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 29.3% |
| 有序区域 (pLDDT>70) 占比 | 61.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.3，有序区 61.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001584, IPR041588, IPR050951, IPR012337, IPR036397; Pfam: PF17921, PF00665 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PGBD5 | 0.674 | 0.070 | — |
| KRBA2 | 0.666 | 0.000 | — |
| HARBI1 | 0.603 | 0.000 | — |
| THAP9 | 0.590 | 0.050 | — |
| C5orf30 | 0.554 | 0.000 | — |
| FANCM | 0.554 | 0.528 | — |
| FAM110B | 0.549 | 0.000 | — |
| ZBED8 | 0.541 | 0.000 | — |
| EFCAB2 | 0.528 | 0.068 | — |
| BUD31 | 0.520 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NYNRIN | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ABA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| OPG200 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| FAM167A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRYAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAV1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:24255178|imex:IM-21541 |
| PTGES3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DUSP16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.3 + PDB: 无 | pLDDT=70.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GIN1 — Gypsy retrotransposon integrase-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小522 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

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
| CPSF6 | BioGRID | 0 |
| USP7 | BioGRID | 0 |
| LMNA | BioGRID | 0 |
| CUL4A | BioGRID | 0 |
| DDX39A | BioGRID | 0 |
| GSTA2 | BioGRID | 0 |
| PARK2 | BioGRID | 0 |
| RPS14 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GIN1

### PubMed

**Count: 57**

| PMID | Title |
|---|---|
| 33796126 | The Arabidopsis thaliana E3 Ubiquitin Ligase BRIZ Functions in Abscisic Acid Response. |
| 31913381 | TiO(2) exposure alters transition metal ion quota in Rhodococcus ruber GIN-1. |
| 29444316 | Glucose triggers stomatal closure mediated by basal signaling through HXK1 and PYR/RCAR receptors in Arabidopsis. |
| 23452177 | Starch metabolism and antiflorigenic signals modulate the juvenile-to-adult phase transition in Arabidopsis. |
| 22661644 | Genetic markers of rheumatoid arthritis susceptibility in anti-citrullinated peptide antibody negative patients. |


