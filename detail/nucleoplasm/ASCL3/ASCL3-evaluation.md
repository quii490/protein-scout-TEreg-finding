---
type: protein-evaluation
gene: "ASCL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASCL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASCL3 / BHLHA42, HASH3, SGN1 |
| 蛋白名称 | Achaete-scute homolog 3 |
| 蛋白大小 | 181 aa / 20.9 kDa |
| UniProt ID | Q9NQ33 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:23:42 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Nucleus |
| 蛋白大小 | 7/10 | x1 | 7 | 181 aa / 20.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=11 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=69.0 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR011598, IPR050283... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **133.0/180** | |
| **归一化总分 (/1.83)** | | | **72.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- chromatin (GO:0000785)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 181 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA42, HASH3, SGN1 |

**关键文献**:
1. An experimental study of the effects of SNPs in the TATA boxes of the GRIN1, ASCL3 and NOS1 genes on interactions with the TATA-binding protein.. *Vavilovskii zhurnal genetiki i selektsii*. PMID: 35774364
2. Integrative analysis of network pharmacology and proteomics reveal the protective effect of Xiaoqinglong Decotion on neutrophilic asthma.. *Journal of ethnopharmacology*. PMID: 38561057
3. Ionocyte-Specific Regulation of Cystic Fibrosis Transmembrane Conductance Regulator.. *American journal of respiratory cell and molecular biology*. PMID: 36952679
4. Transcription Factors as Important Regulators of Changes in Behavior through Domestication of Gray Rats: Quantitative Data from RNA Sequencing.. *International journal of molecular sciences*. PMID: 36293128
5. Deciphering transcriptomic signatures in schizophrenia, bipolar disorder, and major depressive disorder.. *Frontiers in psychiatry*. PMID: 40727846

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.0 |
| 高置信度残基 (pLDDT>90) 占比 | 29.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 50.3% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 35.4% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=69.0），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACBD6 | 0.509 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TCF3 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| ID1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| HEMK1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| VPS37C | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TCF12 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| TCF4 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| ID4 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| C2orf49 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8

**评价**: 互作网络中等：STRING 15 预测 + IntAct 8 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=69.0 | 单一来源 |
| 定位 | UniProt | Nucleus | 单一来源 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 72.7/100

**核心优势**:
1. ASCL3 -- Achaete-scute homolog 3，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ33
- Protein Atlas: https://www.proteinatlas.org/search/ASCL3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASCL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ33
- STRING: https://string-db.org/network/9606.ASCL3
- Packet data timestamp: 2026-06-03 03:23:42

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ33-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
