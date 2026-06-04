---
type: protein-evaluation
gene: "SKAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SKAP2 / PRAP, RA70, SAPS, SCAP2, SKAP55R |
| 蛋白名称 | Src kinase-associated phosphoprotein 2 |
| 蛋白大小 | 359 aa / 41.2 kDa |
| UniProt ID | O75563 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 41.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.0; PDB: 3OMH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR036028, IPR001452, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 67 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRAP, RA70, SAPS, SCAP2, SKAP55R |

**关键文献**:
1. SKAP2-A Molecule at the Crossroads for Integrin Signalling and Immune Cell Migration and Function.. *Biomedicines*. PMID: 37893161
2. Expression and Regulatory Roles of SKAP2 and Cortactin in Mouse Ovarian Tissue and Oocyte Maturation.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 40629241
3. SKAP2 acts downstream of CD11b/CD18 and regulates neutrophil effector function.. *Frontiers in immunology*. PMID: 38487529
4. SKAP2, a Candidate Gene for Type 1 Diabetes, Regulates β-Cell Apoptosis and Glycemic Control in Newly Diagnosed Patients.. *Diabetes*. PMID: 33203694
5. Skap2 is required for β(2) integrin-mediated neutrophil recruitment and functions.. *The Journal of experimental medicine*. PMID: 28183734

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.8% |
| 低置信 (pLDDT<50) 占比 | 25.1% |
| 有序区域 (pLDDT>70) 占比 | 60.2% |
| 可用 PDB 条目 | 3OMH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=74.0，有序区 60.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR036028, IPR001452, IPR037781; Pfam: PF00169, PF00018 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FYB1 | 0.981 | 0.434 | — |
| ITGB1 | 0.914 | 0.000 | — |
| ITGA4 | 0.901 | 0.000 | — |
| ITGA5 | 0.900 | 0.000 | — |
| FYN | 0.896 | 0.690 | — |
| LCP2 | 0.851 | 0.074 | — |
| PRAM1 | 0.829 | 0.292 | — |
| LYN | 0.781 | 0.481 | — |
| SIRPA | 0.768 | 0.000 | — |
| LCK | 0.767 | 0.238 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rgs1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| DNAJB6 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| FASLG | psi-mi:"MI:0084"(phage display) | pubmed:19807924|imex:IM-20398 |
| GRB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19380743|imex:IM-20432 |
| Lcp2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-25620|pubmed:24584089 |
| FYN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PTK2B | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| SNRPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABHD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RGS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 3OMH | pLDDT=74.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. SKAP2 — Src kinase-associated phosphoprotein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75563
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005020-SKAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75563
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
