---
type: protein-evaluation
gene: "BMS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BMS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BMS1 / BMS1L, KIAA0187 |
| 蛋白名称 | Ribosome biogenesis protein BMS1 homolog |
| 蛋白大小 | 1282 aa / 145.8 kDa |
| UniProt ID | Q14692 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:40:52 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm, Nucleoli, Mitotic c... |
| 蛋白大小 | 4/10 | x1 | 4 | 1282 aa / 145.8 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=41 篇 (41-60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=71.5; PDB: 7MQ8, 7MQ9, ... |
| 调控结构域 | 10/10 | x2 | 20 | InterPro: 6; Pfam: 2; IPR012948, IPR039761... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **139.5/180** | |
| **归一化总分 (/1.83)** | | | **76.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Nucleoli, Mitotic chromosome | Enhanced |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 1282 aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 103 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BMS1L, KIAA0187 |

**关键文献**:
1. Prevotellaceae produces butyrate to alleviate PD-1/PD-L1 inhibitor-related cardiotoxicity via PPARα-CYP4X1 axis in colonic macrophages.. *Journal of experimental & clinical cancer research : CR*. PMID: 34980222
2. Stability and function of RCL1 are dependent on the interaction with BMS1.. *Journal of molecular cell biology*. PMID: 37451810
3. An essential GTPase promotes assembly of preribosomal RNA processing complexes.. *Molecular cell*. PMID: 16307926
4. Comprehensive Genomic Analysis of Cemento-Ossifying Fibroma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 37995913
5. Identification of Important Modules and Hub Gene in Chronic Kidney Disease Based on WGCNA.. *Journal of immunology research*. PMID: 35571562

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.5 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 24.3% |
| 有序区域 (pLDDT>70) 占比 | 61.0% |
| 可用 PDB 条目 | 7MQ8, 7MQ9, 7MQA |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=71.5），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012948, IPR039761, IPR037875, IPR007034, IPR030387, IPR027417; Pfam: PF08142, PF04950 |

**染色质调控潜力分析**: 存在 8 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP15 | 0.999 | 0.991 | -- |
| WDR75 | 0.999 | 0.991 | -- |
| HEATR1 | 0.999 | 0.991 | -- |
| UTP4 | 0.999 | 0.991 | -- |
| NOP56 | 0.999 | 0.991 | -- |
| UTP6 | 0.999 | 0.991 | -- |
| KRR1 | 0.999 | 0.991 | -- |
| WDR46 | 0.999 | 0.991 | -- |
| BYSL | 0.999 | 0.991 | -- |
| NOP58 | 0.999 | 0.991 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | pull down | pubmed:23902751|imex:IM-21740 |
| HDGF | tandem affinity purification | pubmed:21907836|imex:IM-17230 |
| pheS | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| purL | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| CSNK2A1 | protein kinase assay | pubmed:22113938|imex:IM-16640 |
| FBL | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| RPS6 | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| RRP1B | anti tag coimmunoprecipitation | imex:IM-26310|pubmed:20926688 |
| H9A910 | anti tag coimmunoprecipitation | pubmed:30177828|imex:IM-26452 |
| H2BC14 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.5 + PDB: 7MQ8, 7MQ9, 7MQA | pLDDT=71.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleoplasm, Nucleoli / Nucleus, nucleolus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 76.2/100

**核心优势**:
1. 已有PDB实验结构：7MQ8, 7MQ9, 7MQA。
2. 存在 8 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 蛋白偏大（1282 aa），表达纯化难度大

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q14692
- Protein Atlas: https://www.proteinatlas.org/search/BMS1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BMS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14692
- STRING: https://string-db.org/network/9606.BMS1
- Packet data timestamp: 2026-06-03 03:40:52
