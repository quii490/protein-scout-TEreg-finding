---
type: protein-evaluation
gene: "ARL14EP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARL14EP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARL14EP / ARF7EP, C11orf46 |
| 蛋白名称 | ARL14 effector protein |
| 蛋白大小 | 260 aa / 29.3 kDa |
| UniProt ID | Q8N8R7 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 02:31:18 |

**IF 图像**:
![](https://images.proteinatlas.org/39634/2267_E8_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/39634/2267_E8_84_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Vesicles, Focal adhesion sites, ... |
| 蛋白大小 | 10/10 | x1 | 10 | 260 aa / 29.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (<=20->10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=80.7; PDB: 8HFP |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR029264 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **149.0/180** | |
| **归一化总分 (/1.83)** | | | **81.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Nucleoli, Vesicles, Plasma membrane, Focal adhesion sites | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 260 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARF7EP, C11orf46 |

**关键文献**:
1. Transcriptome-wide association analyses identify an association between ARL14EP and polycystic ovary syndrome.. *Journal of human genetics*. PMID: 36720993
2. Genome-wide gene by environment study of time spent in daylight and chronotype identifies emerging genetic architecture underlying light sensitivity.. *Sleep*. PMID: 36519390
3. Bivariate genome-wide association study of circulating fibrinogen and C-reactive protein levels.. *Journal of thrombosis and haemostasis : JTH*. PMID: 39299614
4. Unusual Presentation in WAGR Syndrome: Expanding the Phenotypic and Genotypic Spectrum of the Diseases.. *Genes*. PMID: 36011342
5. In vivo epigenetic editing of Sema6a promoter reverses transcallosal dysconnectivity caused by C11orf46/Arl14ep risk gene.. *Nature communications*. PMID: 31511512

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 53.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 73.8% |
| 可用 PDB 条目 | 8HFP |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=80.7），结构可信度高。三维结构评分 9/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029264; Pfam: PF14949 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUOX | 0.503 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYO1E | pull down | imex:IM-15739|pubmed:21458045 |
| ARL14 | two hybrid | imex:IM-15739|pubmed:21458045 |
| lepB | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| ezrA | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| SETDB2 | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| KANK2 | two hybrid prey pooling approach | pubmed:32296183|imex:IM-25472 |
| FAF2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PNKD | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| VHL | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ATF7IP | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 8HFP | pLDDT=80.7, v6 | 预测+实验 |
| 定位 | HPA | Nucleoplasm, Nucleoli | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 81.4/100

**核心优势**:
1. ARL14EP -- ARL14 effector protein，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小260 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold高质量预测（pLDDT=80.7），结构可信度高。
4. 已有PDB实验结构：8HFP。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 5/10），需IF实验验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8N8R7
- Protein Atlas: https://www.proteinatlas.org/search/ARL14EP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARL14EP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8R7
- STRING: https://string-db.org/network/9606.ARL14EP
- Packet data timestamp: 2026-06-03 02:31:18
