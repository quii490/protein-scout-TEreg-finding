---
type: protein-evaluation
gene: "DHX38"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DHX38 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX38 |
| 蛋白名称 | Pre-mRNA-splicing factor ATP-dependent RNA helicase PRP16 |
| 蛋白大小 | 1227 aa / 140.5 kDa |
| UniProt ID | Q92620 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | x1 | 5 | 1227 aa / 140.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=28 篇 (<=40->8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 34 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Exome Sequencing in a Large Cohort with Ciliopathy-Related Kidney Disease.. *Clin J Am Soc Nephrol*. PMID: 41343253
2. DEAH-Box RNA Helicases in the Spliceosome: Advances in Structure and Function.. *FASEB J*. PMID: 41689426
3. Identification of RNA binding proteins that mediate a quality control mechanism of splicing.. *bioRxiv*. PMID: 40777298
4. Single-cell sequencing analysis reveals the essential role of the m (6)A reader YTHDF1 in retinal visual function by regulating TULP1 and DHX38 translation.. *Zool Res*. PMID: 40116022
5. Knockout of dhx38 Causes Inner Ear Developmental Defects in Zebrafish.. *Biomedicines*. PMID: 39857604

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 17.0% |
| 置信残基 (pLDDT 70-90) 占比 | 41.6% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 29.0% |
| 有序区域 (pLDDT>70) 占比 | 58.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 58.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC40 | 0.000 | 0.000 | — |
| SNRNP200 | 0.000 | 0.000 | — |
| CWC25 | 0.000 | 0.000 | — |
| SLU7 | 0.000 | 0.000 | — |
| GPKOW | 0.000 | 0.000 | — |
| CWC22 | 0.000 | 0.000 | — |
| PRPF8 | 0.000 | 0.000 | — |
| YJU2 | 0.000 | 0.000 | — |
| SYF2 | 0.000 | 0.000 | — |
| DHX16 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q92620 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P68400 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:- |
| uniprotkb:P13667 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 无 | pLDDT=68.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DHX38 -- Pre-mRNA-splicing factor ATP-dependent RNA helicase PRP16，非常新颖，仅有少数基础研究。
2. 蛋白大小1227 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92620
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140829-DHX38/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX38
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92620
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
