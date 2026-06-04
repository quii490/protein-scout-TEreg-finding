---
type: protein-evaluation
gene: "BACC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BACC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BACC1 / BAP18, C17orf49 |
| 蛋白名称 | BPTF-associated chromatin complex component 1 |
| 蛋白大小 | 172 aa / 17.9 kDa |
| UniProt ID | Q8IXM2 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:30:08 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Nucleus |
| 蛋白大小 | 7/10 | x1 | 7 | 172 aa / 17.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=69.6 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 0; IPR009057, IPR001005 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 0.5 | 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **122.5/180** | |
| **归一化总分 (/1.83)** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- MLL1 complex (GO:0071339)
- nucleoplasm (GO:0005654)
- NURF complex (GO:0016589)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 172 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAP18, C17orf49 |

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.6 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 39.5% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 42.5% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=69.6），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009057, IPR001005; Pfam: 无 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000411851.2 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| Pou5f1 | anti tag coimmunoprecipitation | pubmed:20362541|imex:IM-16928 |
| H3C1 | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| ESR1 | tandem affinity purification | pubmed:31527615|imex:IM-26954 |
| MAGEA3 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TRIM44 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| BSPRY | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| RBBP4 | tandem affinity purification | pubmed:27705803|imex:IM-21659 |
| XRCC5 | anti tag coimmunoprecipitation | pubmed:26496610|imex:IM-24272 |
| Osgep | anti tag coimmunoprecipitation | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=69.6 | 单一来源 |
| 定位 | UniProt | Nucleus | 单一来源 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- 结构域 + AlphaFold 质量: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**归一化总分**: 66.9/100

**核心优势**:
1. BACC1 -- BPTF-associated chromatin complex component 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 2 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
3. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8IXM2
- Protein Atlas: https://www.proteinatlas.org/search/BACC1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BACC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXM2
- STRING: https://string-db.org/network/9606.BACC1
- Packet data timestamp: 2026-06-03 03:30:08
