---
type: protein-evaluation
gene: "SPRTN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPRTN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPRTN / C1orf124, DVC1 |
| 蛋白名称 | DNA-dependent metalloprotease SPRTN |
| 蛋白大小 | 489 aa / 55.1 kDa |
| UniProt ID | Q9H040 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 489 aa / 55.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.0; PDB: 5IY4, 6MDW, 6MDX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006642, IPR044245, IPR006640, IPR055220; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 94 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf124, DVC1 |

**关键文献**:
1. DNA-protein cross-links promote cGAS-STING-driven premature aging and embryonic lethality.. *Science (New York, N.Y.)*. PMID: 41610251
2. Transcription-coupled DNA-protein crosslink repair by CSB and CRL4(CSA)-mediated degradation.. *Nature cell biology*. PMID: 38600236
3. TEX264 coordinates p97- and SPRTN-mediated resolution of topoisomerase 1-DNA adducts.. *Nature communications*. PMID: 32152270
4. Mechanisms and Regulation of DNA-Protein Crosslink Repair During DNA Replication by SPRTN Protease.. *Frontiers in molecular biosciences*. PMID: 35782873
5. Allosteric activation of the SPRTN protease by ubiquitin maintains genome stability.. *Nature communications*. PMID: 40691134

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.0 |
| 高置信度残基 (pLDDT>90) 占比 | 31.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 45.0% |
| 有序区域 (pLDDT>70) 占比 | 48.1% |
| 可用 PDB 条目 | 5IY4, 6MDW, 6MDX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.0），有序残基占 48.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006642, IPR044245, IPR006640, IPR055220; Pfam: PF10263, PF22934 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCNA | 0.992 | 0.983 | — |
| VCP | 0.976 | 0.842 | — |
| UBC | 0.864 | 0.735 | — |
| PPP2R3A | 0.827 | 0.000 | — |
| PPP2R3B | 0.827 | 0.000 | — |
| TPTE2 | 0.812 | 0.000 | — |
| TPTE | 0.809 | 0.000 | — |
| PTEN | 0.809 | 0.000 | — |
| RAD18 | 0.807 | 0.510 | — |
| UFD1 | 0.807 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RANBP3L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC102B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XKRX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EIF4E2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GTF2F1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAPG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GSTT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EMC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BRAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RALGAPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.0 + PDB: 5IY4, 6MDW, 6MDX | pLDDT=65.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SPRTN — DNA-dependent metalloprotease SPRTN，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小489 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H040
- Protein Atlas: https://www.proteinatlas.org/ENSG00000010072-SPRTN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPRTN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H040
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
