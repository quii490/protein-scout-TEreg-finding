---
type: protein-evaluation
gene: "CREBZF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CREBZF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREBZF / ZF |
| 蛋白名称 | CREB/ATF bZIP transcription factor |
| 蛋白大小 | 354 aa / 37.1 kDa |
| UniProt ID | Q9NS37 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Mitochondria; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 354 aa / 37.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=30 篇 (<=40->8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=61.5; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Approved |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- chromatin (GO:0000785)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZF |

**关键文献**:
1. Glucose regulation of adipose tissue browning by CBP/p300- and HDAC3-mediated reversible acetylation of CREBZF.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38588421
2. CREBZF, a novel Smad8-binding protein.. *Molecular and cellular biochemistry*. PMID: 22707059
3. CREBZF expression and hormonal regulation in the mouse uterus.. *Reproductive biology and endocrinology : RB&E*. PMID: 24325733
4. CREBZF regulates testosterone production in mouse Leydig cells.. *Journal of cellular physiology*. PMID: 31124138
5. The transcription factor CREBZF is a novel positive regulator of p53.. *Cell cycle (Georgetown, Tex.)*. PMID: 22983008

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.5 |
| 高置信度残基 (pLDDT>90) 占比 | 16.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 20.9% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 34.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.5），有序残基占 34.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HCFC1 | 0.995 | 0.737 | — |
| HCFC2 | 0.971 | 0.000 | — |
| CREB3 | 0.945 | 0.538 | — |
| NOL9 | 0.846 | 0.832 | — |
| CREB3L4 | 0.795 | 0.000 | — |
| ATF4 | 0.778 | 0.613 | — |
| NR0B2 | 0.668 | 0.000 | — |
| XBP1 | 0.607 | 0.513 | — |
| POU2F1 | 0.595 | 0.000 | — |
| TP53 | 0.589 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HCFC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10871379 |
| CREB3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15705566 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| VWA5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BACH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RALBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTC23 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ACYP2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| CTNNBL1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.5 + PDB: 无 | pLDDT=61.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CREBZF -- CREB/ATF bZIP transcription factor，非常新颖，仅有少数基础研究。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS37
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137504-CREBZF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREBZF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS37
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
