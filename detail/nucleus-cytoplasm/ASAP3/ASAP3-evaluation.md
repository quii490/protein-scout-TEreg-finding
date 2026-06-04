---
type: protein-evaluation
gene: "ASAP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASAP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASAP3 / DDEFL1, UPLC1 |
| 蛋白名称 | Arf-GAP with SH3 domain, ANK repeat and PH domain-containing protein 3 |
| 蛋白大小 | 903 aa / 99.2 kDa |
| UniProt ID | Q8TDY4 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:22:52 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Vesicles; UniProt: Cytoplasm |
| 蛋白大小 | 7/10 | x1 | 7 | 903 aa / 99.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 2B0O, 3LVQ, ... |
| 调控结构域 | 10/10 | x2 | 20 | InterPro: 13; Pfam: 4; IPR027267, IPR00211... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **144.5/180** | |
| **归一化总分 (/1.83)** | | | **79.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Vesicles | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleoplasm (GO:0005654)
- ruffle (GO:0001726)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 903 aa，蛋白偏大（> 800 aa），表达纯化有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDEFL1, UPLC1 |

**关键文献**:
1. The expression of ASAP3 and NOTCH3 and the clinicopathological characteristics of adult glioma patients.. *Open medicine (Warsaw, Poland)*. PMID: 36382054
2. RNA-Sequence Reveals the Regulatory Mechanism of miR-149 on Osteoblast Skeleton under Mechanical Tension.. *Stem cells international*. PMID: 36193254
3. ASAP3 is a focal adhesion-associated Arf GAP that functions in cell migration and invasion.. *The Journal of biological chemistry*. PMID: 18400762
4. Loss of ASAP3 destabilizes cytoskeletal protein ACTG1 to suppress cancer cell migration.. *Molecular medicine reports*. PMID: 24284654
5. Mir-421 and mir-550a-1 are potential prognostic markers in esophageal adenocarcinoma.. *Biology direct*. PMID: 36829221

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 46.7% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 2B0O, 3LVQ, 3LVR |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=73.8），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027267, IPR002110, IPR036770, IPR037278, IPR001164, IPR038508, IPR043593, IPR047006, IPR028775, IPR004148, IPR011993, IPR037844, IPR001849; Pfam: PF12796, PF01412, PF16746, PF00169 |

**染色质调控潜力分析**: 存在 17 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GIT1 | 0.425 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CRK | tandem affinity purification | pubmed:19380743|imex:IM-20432 |
| GOLGA2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| NHERF4 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| TEPSIN | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| hspa1a_hspa1b_human-1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ASAP2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ELP2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ACAD11 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ASAP1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| BACH1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15

**评价**: 互作网络中等：STRING 14 预测 + IntAct 15 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 2B0O, 3LVQ, 3LVR | pLDDT=73.8, v6 | 预测+实验 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 79.0/100

**核心优势**:
1. ASAP3 -- Arf-GAP with SH3 domain, ANK repeat and PH domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 已有PDB实验结构：2B0O, 3LVQ, 3LVR。
3. 存在 17 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 5/10），需IF实验验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8TDY4
- Protein Atlas: https://www.proteinatlas.org/search/ASAP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASAP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDY4
- STRING: https://string-db.org/network/9606.ASAP3
- Packet data timestamp: 2026-06-03 03:22:52
