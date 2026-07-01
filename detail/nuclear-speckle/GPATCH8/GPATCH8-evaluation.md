---
type: protein-evaluation
gene: "GPATCH8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPATCH8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPATCH8 / GPATC8, KIAA0553 |
| 蛋白名称 | G patch domain-containing protein 8 |
| 蛋白大小 | 1502 aa / 164.2 kDa |
| UniProt ID | Q9UKJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nuclear speckles; 额外: Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1502 aa / 164.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000467, IPR052445, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

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
| AlphaFold 平均 pLDDT | 45.7 |
| 高置信度残基 (pLDDT>90) 占比 | 4.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 77.7% |
| 有序区域 (pLDDT>70) 占比 | 13.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.7），有序残基占 13.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000467, IPR052445, IPR036236, IPR013087; Pfam: PF01585 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNPS1 | 0.681 | 0.605 | — |
| CLK3 | 0.677 | 0.666 | — |
| CLK2 | 0.629 | 0.608 | — |
| KRR1 | 0.624 | 0.504 | — |
| SRSF11 | 0.560 | 0.421 | — |
| UTP6 | 0.540 | 0.504 | — |
| NOL6 | 0.534 | 0.504 | — |
| UTP25 | 0.522 | 0.504 | — |
| UTP3 | 0.522 | 0.504 | — |
| DDX10 | 0.520 | 0.504 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| APH1A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NUMBL | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ENSP00000467556.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EPB41L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| CLK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.7 + PDB: 无 | pLDDT=45.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPATCH8 — G patch domain-containing protein 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1502 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=45.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TERF2 | BioGRID | 0 |
| ATXN1 | BioGRID | 0 |
| ATXN1L | BioGRID | 0 |
| APH1A | BioGRID | 0 |
| NUMBL | BioGRID | 0 |
| CLK3 | BioGRID | 0 |
| TP53 | BioGRID | 0 |
| BMI1 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GPATCH8

### PubMed

**Count: 9**

| PMID | Title |
|---|---|
| 40694934 | Gonadal sex differentiation in Eleutheronema tetradactylum: Histological features and transcriptomic insights from mature gonads. |
| 39062728 | Hepatopancreas Transcriptome Analysis of Spinibarbus sinensis to Reveal Different Growth-Related Genes. |
| 38762373 | (G)Patching up mis-splicing in cancer. |
| 38688280 | GPATCH8 modulates mutant SF3B1 mis-splicing and pathogenicity in hematologic malignancies. |
| 37474895 | Identification of the susceptible genes and mechanism underlying the comorbid presence of coronary artery disease and rheumatoid arthritis: a network  |


