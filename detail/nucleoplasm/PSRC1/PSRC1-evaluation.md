---
type: protein-evaluation
gene: "PSRC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PSRC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PSRC1 / DDA3 |
| 蛋白名称 | Proline/serine-rich coiled-coil protein 1 |
| 蛋白大小 | 363 aa / 38.8 kDa |
| UniProt ID | Q6PGN9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cyto |
| 蛋白大小 | 10/10 | ×1 | 10 | 363 aa / 38.8 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026657, IPR032768; Pfam: PF15259 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)
- spindle (GO:0005819)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 147 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDA3 |

**关键文献**:
1. Psrc1 Ensures Proper Spindle Assembly and Chromosome Segregation During Mouse Oocyte Maturation.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40810374
2. (Apo)Lipoprotein Profiling with Multi-Omics Analysis Identified Medium-HDL-Targeting PSRC1 with Therapeutic Potential for Coronary Artery Disease.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39985383
3. Proline/serine-rich coiled-coil protein 1 alleviates pyroptosis in murine bone marrow-derived macrophages.. *Acta biochimica et biophysica Sinica*. PMID: 39935324
4. PSRC1 May Affect Coronary Artery Disease Risk by Altering CELSR2, PSRC1, and SORT1 Gene Expression and Circulating Granulin and Apolipoprotein B Protein Levels.. *Frontiers in cardiovascular medicine*. PMID: 35252377
5. Phosphocreatine alleviates monocrotaline-induced liver injury dependent on PSRC1-regulated endoplasmic reticulum stress.. *Biochemical pharmacology*. PMID: 40194605

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.4 |
| 高置信度残基 (pLDDT>90) 占比 | 5.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.4% |
| 中等置信 (pLDDT 50-70) 占比 | 50.7% |
| 低置信 (pLDDT<50) 占比 | 34.4% |
| 有序区域 (pLDDT>70) 占比 | 14.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.4），有序残基占 14.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026657, IPR032768; Pfam: PF15259 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CELSR2 | 0.986 | 0.000 | — |
| SORT1 | 0.954 | 0.000 | — |
| PCSK9 | 0.812 | 0.000 | — |
| MYBPHL | 0.799 | 0.000 | — |
| SORCS2 | 0.670 | 0.000 | — |
| SORCS3 | 0.669 | 0.000 | — |
| SORCS1 | 0.669 | 0.000 | — |
| KIF2A | 0.657 | 0.000 | — |
| MAPRE1 | 0.650 | 0.599 | — |
| PIMREG | 0.642 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nck1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| SF3A2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MAPRE3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FUS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Homer1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ttll12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Spred2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| KIF22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.4 + PDB: 无 | pLDDT=57.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, spindle; Cytop / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. PSRC1 — Proline/serine-rich coiled-coil protein 1，研究基础较多，新颖性有限。
2. 蛋白大小363 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PGN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134222-PSRC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PSRC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PGN9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
