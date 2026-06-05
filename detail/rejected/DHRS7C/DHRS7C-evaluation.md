---
type: protein-evaluation
gene: "DHRS7C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHRS7C — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHRS7C |
| 蛋白名称 | Dehydrogenase/reductase SDR family member 7C |
| 蛋白大小 | 312 aa / 34.9 kDa |
| UniProt ID | A6NNS2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Sarcoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 312 aa / 34.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=12 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 22 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Sarcoplasmic reticulum membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 14 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Bridging metabolism and immuno-inflammation: a novel framework to characterize dilated cardiomyopathy subtype.. *J Transl Med*. PMID: 41121125
2. COADREADx: A comprehensive algorithmic dissection of colorectal cancer unravels salient biomarkers and actionable insights into its discrete progression.. *PeerJ*. PMID: 39484215
3. Proteomic Identification of Seasonally Expressed Proteins Contributing to Heart Function and the Avoidance of Skeletal Muscle Disuse Atrophy in a Hibernating Mammal.. *J Proteome Res*. PMID: 38117800
4. Genome-wide gene-bisphenol A, F and triclosan interaction analyses on urinary oxidative stress markers.. *Sci Total Environ*. PMID: 34619205
5. Multiple short-chain dehydrogenases/reductases are regulated in pathological cardiac hypertrophy.. *FEBS Open Bio*. PMID: 30338214

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 5.8% |
| 有序区域 (pLDDT>70) 占比 | 87.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.6，有序区 87.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SAYSD1 | 0.000 | 0.000 | — |
| AKIP1 | 0.000 | 0.000 | — |
| MCRIP1 | 0.000 | 0.000 | — |
| HSDL1 | 0.000 | 0.000 | — |
| HSD17B3 | 0.000 | 0.000 | — |
| STAM | 0.000 | 0.000 | — |
| STAM2 | 0.000 | 0.000 | — |
| DNAH8 | 0.000 | 0.000 | — |
| PLGLB2 | 0.000 | 0.000 | — |
| TRDN | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 22，IntAct interactions: 0
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 22 个预测互作，IntAct 0 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.6 + PDB: 无 | pLDDT=87.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Sarcoplasmic reticulum membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 22 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DHRS7C -- Dehydrogenase/reductase SDR family member 7C，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小312 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NNS2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184544-DHRS7C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHRS7C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NNS2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NNS2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
