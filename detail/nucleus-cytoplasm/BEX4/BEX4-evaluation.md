---
type: protein-evaluation
gene: "BEX4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEX4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEX4 / BEXL1, NADE3 |
| 蛋白名称 | Protein BEX4 |
| 蛋白大小 | 120 aa / 14.1 kDa |
| UniProt ID | Q9NWD9 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:35:49 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoplasm, Cytosol; UniProt: C... |
| 蛋白大小 | 7/10 | x1 | 7 | 120 aa / 14.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=63.3 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR007623, IPR021156 |
| PPI 网络 | 8/10 | x3 | 24 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **131.5/180** | |
| **归一化总分 (/1.83)** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton, spindle pole, Nucleus, Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle pole (GO:0000922)

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 120 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BEXL1, NADE3 |

**关键文献**:
1. Immune genes involved in synaptic plasticity during early postnatal brain development contribute to post-stroke damage in the aging male rat brain.. *Biogerontology*. PMID: 39966204
2. Oncogenic potential of BEX4 is conferred by Polo-like kinase 1-mediated phosphorylation.. *Experimental & molecular medicine*. PMID: 30367032
3. BEX4 upregulation alters Sertoli cell growth properties and protein expression profiles: An explanation for cadmium-induced testicular Sertoli cell injury.. *Journal of biochemical and molecular toxicology*. PMID: 28295929
4. Machine Learning Reveals Aneuploidy Characteristics in Cancers: The Impact of BEX4.. *Frontiers in bioscience (Landmark edition)*. PMID: 39735979
5. BEX4 inhibits the progression of clear cell renal cell carcinoma by stabilizing SH2D4A, which is achieved by blocking SIRT2 activity.. *Oncogene*. PMID: 39639172

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.3 |
| 高置信度残基 (pLDDT>90) 占比 | 7.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 54.2% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 25.0% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=63.3），存在部分低置信区域。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007623, IPR021156; Pfam: PF04538 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCEAL1 | 0.424 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MPPED2 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| KLHL41 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| LYPLA1 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| CDKN2C | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| ALDH6A1 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| PRKCD | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| FAAP100 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| MTMR1 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| MAPK14 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| PPP2R2D | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15

**评价**: 互作网络中等：STRING 7 预测 + IntAct 15 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=63.3 | 单一来源 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus | 一致 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 71.9/100

**核心优势**:
1. BEX4 -- Protein BEX4，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 3 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9NWD9
- Protein Atlas: https://www.proteinatlas.org/search/BEX4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BEX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWD9
- STRING: https://string-db.org/network/9606.BEX4
- Packet data timestamp: 2026-06-03 03:35:49
