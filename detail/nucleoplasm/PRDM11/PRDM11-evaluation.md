---
type: protein-evaluation
gene: "PRDM11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRDM11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRDM11 / PFM8 |
| 蛋白名称 | PR domain-containing protein 11 |
| 蛋白大小 | 511 aa / 57.9 kDa |
| UniProt ID | Q9NQV5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 511 aa / 57.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 3RAY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR044405, IPR001214, IPR046341, IPR050331; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PFM8 |

**关键文献**:
1. NSUN2-mediated R-loop stabilization as a key driver of bladder cancer progression and cisplatin sensitivity.. *Cancer letters*. PMID: 39732321
2. Chromatin Regulator-Related Gene Signature for Predicting Prognosis and Immunotherapy Efficacy in Breast Cancer.. *Journal of oncology*. PMID: 36755810
3. Evolution of Prdm Genes in Animals: Insights from Comparative Genomics.. *Molecular biology and evolution*. PMID: 26560352
4. Cox4i2, Ifit2, and Prdm11 Mutant Mice: Effective Selection of Genes Predisposing to an Altered Airway Inflammatory Response from a Large Compendium of Mutant Mouse Lines.. *PloS one*. PMID: 26263558
5. Gene network changes after exposure to nanoliposomes containing antisense miR-21 and miR-373 in bladder cancer Cells: An in vitro model study.. *Biochemistry and biophysics reports*. PMID: 40469776

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 24.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.1% |
| 低置信 (pLDDT<50) 占比 | 46.0% |
| 有序区域 (pLDDT>70) 占比 | 40.0% |
| 可用 PDB 条目 | 3RAY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 40.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044405, IPR001214, IPR046341, IPR050331; Pfam: PF21549 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRDM16 | 0.600 | 0.041 | — |
| PRDM12 | 0.542 | 0.000 | — |
| PRDM5 | 0.538 | 0.041 | — |
| CAPNS2 | 0.518 | 0.000 | — |
| MBIP | 0.514 | 0.000 | — |
| ITPK1 | 0.505 | 0.000 | — |
| PRDM8 | 0.496 | 0.000 | — |
| ASH1L | 0.487 | 0.000 | — |
| PDE8B | 0.483 | 0.000 | — |
| PRDM13 | 0.481 | 0.041 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FHL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LONRF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACBD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEK9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KXD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 3RAY | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PRDM11 — PR domain-containing protein 11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小511 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQV5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000019485-PRDM11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRDM11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQV5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PRDM11/PRDM11-PAE.png]]
