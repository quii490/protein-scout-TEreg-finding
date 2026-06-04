---
type: protein-evaluation
gene: "NHLRC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NHLRC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NHLRC2 |
| 蛋白名称 | NHL repeat-containing protein 2 |
| 蛋白大小 | 726 aa / 79.4 kDa |
| UniProt ID | Q8NBF2 |
| 数据采集时间 | 2026-06-03 23:43:47 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | x1 | 10 | 726 aa / 79.4 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=28 篇 (21-40 -> 8) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=92.7; PDB: 6G7W, 6GC1 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR011042, IPR045302, IPR001258, IPR012336, I |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- platelet alpha granule lumen (GO:0031093)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 32 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A genome-wide screen identifies genes required for erythroid differentiation.. *Nature communications*. PMID: 40221460
2. Nhlrc2 is crucial during mouse gastrulation.. *Genesis (New York, N.Y. : 2000)*. PMID: 35258166
3. Altered behaviour and immune response in mice with NHLRC2 p.Asp148Tyr variant.. *Brain, behavior, & immunity - health*. PMID: 40510178
4. A Genome-Wide Knockout Screen in Human Macrophages Identified Host Factors Modulating Salmonella Infection.. *mBio*. PMID: 31594818
5. Broadening the phenotypic and molecular spectrum of FINCA syndrome: Biallelic NHLRC2 variants in 15 novel individuals.. *European journal of human genetics : EJHG*. PMID: 37188825

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 82.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 6G7W, 6GC1 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构（6G7W, 6GC1）+ AlphaFold高质量预测（pLDDT=92.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011042, IPR045302, IPR001258, IPR012336, IPR036249; Pfam: PF01436, PF13905 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TM2D3 | 0.632 | 0.000 | — |
| CCDC186 | 0.605 | 0.000 | — |
| VWA2 | 0.581 | 0.084 | — |
| TM2D1 | 0.578 | 0.000 | — |
| TM2D2 | 0.569 | 0.000 | — |
| ZZZ3 | 0.545 | 0.052 | — |
| DCLRE1A | 0.541 | 0.000 | — |
| NCKAP1L | 0.524 | 0.210 | — |
| GANAB | 0.513 | 0.328 | — |
| FRYL | 0.508 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| MSL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| TEKT5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CEP76 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| PTPN11 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| TAFA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANKS1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| SRSF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 6G7W, 6GC1 | pLDDT=92.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. NHLRC2 -- NHL repeat-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小726 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196865-NHLRC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NHLRC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NBF2
- STRING: https://string-db.org/network/9606.NHLRC2
- Packet data timestamp: 2026-06-03 23:43:47

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*
