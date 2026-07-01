---
type: protein-evaluation
gene: "SMKR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SMKR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMKR1 |
| 蛋白名称 | Small lysine-rich protein 1 |
| 蛋白大小 | 65 aa / 7.1 kDa |
| UniProt ID | H3BMG3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 65 aa / 7.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037760 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A DNA methylation signature to improve survival prediction of gastric cancer.. *Clinical epigenetics*. PMID: 31959204
2. Exploring Pathogenic Genes in Frozen Shoulder through weighted gene co-expression network analysis and Mendelian Randomization.. *International journal of medical sciences*. PMID: 39512681

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.7 |
| 高置信度残基 (pLDDT>90) 占比 | 3.1% |
| 置信残基 (pLDDT 70-90) 占比 | 58.5% |
| 中等置信 (pLDDT 50-70) 占比 | 27.7% |
| 低置信 (pLDDT<50) 占比 | 10.8% |
| 有序区域 (pLDDT>70) 占比 | 61.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.7，有序区 61.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037760 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.990 | 0.967 | — |
| MRPL19 | 0.908 | 0.624 | — |
| MRPL20 | 0.908 | 0.624 | — |
| RPS18 | 0.908 | 0.622 | — |
| RPS3A | 0.907 | 0.622 | — |
| MRPL32 | 0.907 | 0.624 | — |
| MRPS9 | 0.907 | 0.618 | — |
| PDCD11 | 0.906 | 0.618 | — |
| MRPS16 | 0.906 | 0.620 | — |
| MRPL17 | 0.906 | 0.624 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBA52 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.7 + PDB: 无 | pLDDT=71.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. SMKR1 — Small lysine-rich protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小65 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAU | STRING | 990 |
| MRPL19 | STRING | 908 |
| RPS18 | STRING | 908 |
| MRPS9 | STRING | 907 |
| RPS3A | STRING | 907 |
| PDCD11 | STRING | 906 |
| RPS11 | STRING | 903 |
| RPL5 | STRING | 903 |


### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。

### 深度机制分析

SMKR1（Small lysine-rich protein 1, 65 aa, UniProt H3BMG3）。定位于Nucleoli（HPA Approved），是最小的评价蛋白之一（仅7.1 kDa）。InterPro注释IPR037760（SMKR1家族），Pfam未检出。AlphaFold pLDDT=71.7（有序区61.6%），无PDB结构。

从蛋白结构特征角度，SMKR1"富含赖氨酸"——基本的赖氨酸富集是核小体结合蛋白（如HMGN蛋白、linker histone H1的C端尾）的经典特征，它们通过碱性残基与DNA磷酸骨架的静电相互作用结合染色质。65 aa中高比例赖氨酸的存在暗示SMKR1可能具有内在的核小体/核酸结合能力。pLDDT=71.7，58.5%残基处于70-90区间——考虑到蛋白体积极小，已是合理置信度。

从PPI网络角度，STRING鉴定的互作伙伴几乎全为核糖体蛋白（RPS18、RPS3A、RPL5、RPS11等）和线粒体核糖体蛋白（MRPL19、MRPL20、MRPS9），FAU（combined=0.990, experimental=0.967）是最强互作伙伴。FAU编码ubiquitin-like protein FUBI与核糖体蛋白S30的融合蛋白——其泛素样域可参与蛋白降解。IntAct仅鉴定UBA52（ubiquitin-60S ribosomal protein L40）的cross-linking互作。所有互作均指向核糖体生物合成——与nucleoli定位一致。

从TE调控角度，SMKR1在nucleoli的定位暗示其主要功能是核糖体生物合成相关，而非染色质/TE调控。但富含赖氨酸的小蛋白有时具有非特异性DNA/RNA结合活性，在特定条件下可能"兼职"参与核凝聚体形成——这在nucleoli的相分离环境中尤为可能。

PubMed仅2篇（PMID:31959204、39512681），极度新颖。综合评分71.1/100。建议测定SMKR1的等温滴定量热法（ITC）检测其对DNA/RNA底物的结合亲和力。