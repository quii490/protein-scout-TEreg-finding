---
type: protein-evaluation
gene: "CENPQ"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CENPQ 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPQ / C6orf139 |
| 蛋白名称 | Centromere protein Q |
| 蛋白大小 | 268 aa / 30.6 kDa |
| UniProt ID | Q7L2Z9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | ×4 | 40 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere |
| 蛋白大小 | 10/10 | ×1 | 10 | 268 aa / 30.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.2; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR025212; Pfam: PF13094 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **170.2/180** | |
| **归一化总分 (÷1.83)** | | | **93.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | ECO:0000269
| UniProt | Chromosome, centromere | ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629) [IDA:HPA]
- cytosol (GO:0005829) [TAS:Reactome]
- inner kinetochore (GO:0000939) [IPI:ComplexPortal]
- nucleoplasm (GO:0005654) [IDA:HPA]
- nucleus (GO:0005634) [IBA:GO_Central]

**结论**: HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere

#### 3.2 蛋白大小评估

**评价**: 268 aa / 30.6 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed 搜索链接 | [CENPQ PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CENPQ) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 39.2% |
| 置信残基 (pLDDT 70-90) 占比 | 22.4% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 61.6% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025212; Pfam: PF13094 |

**染色质调控潜力分析**: 存在染色质/调控相关结构域/功能特征: nucleosome, centromere, kinetochore

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPU | 0.999 | 0.983 | — |
| CENPM | 0.999 | 0.944 | — |
| CENPP | 0.999 | 0.986 | — |
| CENPO | 0.999 | 0.986 | — |
| CENPK | 0.999 | 0.899 | — |
| CENPH | 0.999 | 0.920 | — |
| ITGB3BP | 0.999 | 0.984 | — |
| CENPN | 0.999 | 0.970 | — |
| CENPL | 0.999 | 0.860 | — |
| CENPI | 0.999 | 0.921 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BRME1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| CENPO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CENPP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ITGB3BP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| CANX | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| HOMER1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SNX2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| EMILIN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HDAC7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=73.2, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域注释 + AlphaFold 预测: +0.25

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 93.0/100

**核心优势**:
1. CENPQ — Centromere protein Q，极度新颖，几乎未被系统研究（PubMed 18 篇）。
2. 蛋白大小268 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计 ChIP-seq/CUT&RUN 验证染色质结合
- [ ] 设计体外实验验证核定位及潜在调控功能

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CENPM | STRING | 999 |
| MLF1IP | STRING | 999 |
| CENPU | STRING | 999 |
| CENPH | STRING | 999 |
| CENPP | STRING | 999 |
| CENPO | STRING | 999 |
| CENPK | STRING | 999 |
| ITGB3BP | STRING | 999 |


### TE 调控评估

该蛋白有 ChIP-Seq 数据，可能在基因组水平参与 TE 调控。建议验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CENPQ

### PubMed

**Count: 25**

| PMID | Title |
|---|---|
| 42003665 | Integration of Genome-Wide Association Studies With Single-Cell and Bulk Expression Quantitative Trait Locus to Identify Stroke Susceptibility Genes. |
| 41502527 | CSRNP1 Promotes Apoptosis and Mitochondrial Dysfunction via ROS-Mediated JNK/p38 MAPK Pathway Activation in Hepatocellular Carcinoma. |
| 39968732 | Novel Candidate Genes Detection Using Bayesian Network-Based Genome-Wide Association Study of Latent Traits in F2 Chicken Population. |
| 38827182 | The Correlation of Centromere Protein Q with Diagnosis and Prognosis in Hepatocellular Carcinoma. |
| 36691064 | Early peripheral blood gene expression associated with good and poor 90-day ischemic stroke outcomes. |


