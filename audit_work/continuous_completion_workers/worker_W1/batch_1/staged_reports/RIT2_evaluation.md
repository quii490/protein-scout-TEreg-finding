---
type: protein-evaluation
gene: "RIT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RIT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIT2 / RIN, ROC2 |
| 蛋白名称 | GTP-binding protein Rit2 |
| 蛋白大小 | 217 aa / 24.7 kDa |
| UniProt ID | Q99578 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Cytosol; UniProt: Nucleus; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 217 aa / 24.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR005225, IPR001806, IPR020849; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Cytosol | Supported |
| UniProt | Nucleus; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell body (GO:0044297)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic tree (GO:0097447)
- Golgi apparatus (GO:0005794)
- membrane raft (GO:0045121)
- neuron projection (GO:0043005)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 67 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RIN, ROC2 |

**关键文献**:
1. Molecular profiling of human substantia nigra identifies diverse neuron types associated with vulnerability in Parkinson's disease.. *Science advances*. PMID: 38198537
2. RIT2: responsible and susceptible gene for neurological and psychiatric disorders.. *Molecular genetics and genomics : MGG*. PMID: 29860660
3. RIT2 rs12456492 polymorphism and the risk of Parkinson's disease: A meta-analysis.. *Neuroscience letters*. PMID: 26188085
4. Prioritizing Parkinson's disease risk genes in genome-wide association loci.. *NPJ Parkinson's disease*. PMID: 40240380
5. Association of RIT2 and RAB7L1 with Parkinson's disease: a case-control study in a Taiwanese cohort and a meta-analysis in Asian populations.. *Neurobiology of aging*. PMID: 31818509

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.8 |
| 高置信度残基 (pLDDT>90) 占比 | 68.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 88.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.8，有序区 88.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR005225, IPR001806, IPR020849; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RIT1 | 0.893 | 0.788 | — |
| POU4F1 | 0.833 | 0.292 | — |
| LZTR1 | 0.802 | 0.788 | — |
| BRAF | 0.801 | 0.284 | — |
| SLC6A3 | 0.707 | 0.333 | — |
| POU4F2 | 0.702 | 0.000 | — |
| SYT4 | 0.661 | 0.000 | — |
| CALM1 | 0.628 | 0.355 | — |
| CCDC62 | 0.602 | 0.000 | — |
| GAK | 0.590 | 0.144 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RLF | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 |
| RALGDS | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 |
| AFDN | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| RIT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LZTR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RGL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC6A3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25101|pubmed:21957239 |
| VPS37C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.8 + PDB: 无 | pLDDT=87.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cell membrane / Nucleoplasm; 额外: Golgi apparatus, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RIT2 — GTP-binding protein Rit2，非常新颖，仅有少数基础研究。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99578
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152214-RIT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99578
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
