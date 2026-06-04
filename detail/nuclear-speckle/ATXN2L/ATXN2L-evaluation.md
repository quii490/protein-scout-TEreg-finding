---
type: protein-evaluation
gene: "ATXN2L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATXN2L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATXN2L / A2D, A2LG, A2LP, A2RP |
| 蛋白名称 | Ataxin-2-like protein |
| 蛋白大小 | 1075 aa / 113.4 kDa |
| UniProt ID | Q8WWM7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Membrane; Cytoplasm; Nucleus speckle; Cytoplasmic granule |
| 蛋白大小 | 8/10 | ×1 | 8 | 1075 aa / 113.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045117, IPR009604, IPR009818, IPR047575, IPR025 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane; Cytoplasm; Nucleus speckle; Cytoplasmic granule | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: A2D, A2LG, A2LP, A2RP |

**关键文献**:
1. Circadian clocks are modulated by compartmentalized oscillating translation.. *Cell*. PMID: 37369203
2. Apoptosis-associated genetic mechanisms in the transition from rheumatoid arthritis to osteoporosis: A bioinformatics and functional analysis approach.. *APL bioengineering*. PMID: 39507523
3. ATXN2L primarily interacts with NUFIP2, the absence of ATXN2L results in NUFIP2 depletion, and the ATXN2-polyQ expansion triggers NUFIP2 accumulation.. *Neurobiology of disease*. PMID: 40220918
4. Ataxin-2-like promotes translation of nonpolyadenylated reovirus mRNA.. *Nature communications*. PMID: 41408047
5. Novel genetic regulators of fibrinogen synthesis identified by an in vitro experimental platform.. *Journal of thrombosis and haemostasis : JTH*. PMID: 36696182

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.5 |
| 高置信度残基 (pLDDT>90) 占比 | 7.6% |
| 置信残基 (pLDDT 70-90) 占比 | 9.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 72.8% |
| 有序区域 (pLDDT>70) 占比 | 17.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.5），有序残基占 17.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045117, IPR009604, IPR009818, IPR047575, IPR025852; Pfam: PF06741, PF07145, PF14438 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LSM12 | 0.986 | 0.972 | — |
| ATXN2 | 0.953 | 0.442 | — |
| DDX6 | 0.952 | 0.877 | — |
| ATXN3 | 0.917 | 0.150 | — |
| PABPC1 | 0.917 | 0.746 | — |
| ITPR3 | 0.908 | 0.000 | — |
| NUFIP2 | 0.906 | 0.844 | — |
| ATXN3L | 0.903 | 0.000 | — |
| ITPR1 | 0.900 | 0.000 | — |
| ITPR2 | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| CCNA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| HADHA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SMAD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| ORF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16317|pubmed:22522808 |
| US11 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| G3BP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.5 + PDB: 无 | pLDDT=48.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Nucleus speckle; Cytoplasmic  / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ATXN2L — Ataxin-2-like protein，非常新颖，仅有少数基础研究。
2. 蛋白大小1075 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWM7
- Protein Atlas: https://www.proteinatlas.org/search/ATXN2L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATXN2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWM7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
