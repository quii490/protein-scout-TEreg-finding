---
type: protein-evaluation
gene: "FBXW11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXW11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXW11 / BTRCP2, FBW1B, FBXW1B, KIAA0696 |
| 蛋白名称 | F-box/WD repeat-containing protein 11 |
| 蛋白大小 | 542 aa / 62.1 kDa |
| UniProt ID | Q9UKB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Plasma membrane; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 542 aa / 62.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.2; PDB: 6WNX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR021977, IPR036047, IPR001810, IPR050995, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon cytoplasm (GO:1904115)
- centrosome (GO:0005813)
- cytoplasmic microtubule (GO:0005881)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- microtubule associated complex (GO:0005875)
- neuron projection (GO:0043005)
- neuronal cell body (GO:0043025)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 97 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTRCP2, FBW1B, FBXW1B, KIAA0696 |

**关键文献**:
1. A haploinsufficiency restoration strategy corrects neurobehavioral deficits in Nf1+/- mice.. *The Journal of clinical investigation*. PMID: 40590220
2. Wnt/β-catenin activation by mutually exclusive FBXW11 and CTNNB1 hotspot mutations drives salivary basal cell adenoma.. *Nature communications*. PMID: 40389436
3. E3 ubiquitin ligase FBXW11-mediated downregulation of S100A11 promotes sensitivity to PARP inhibitor in ovarian cancer.. *Journal of pharmaceutical analysis*. PMID: 40747341
4. Cullin-associated and neddylation-dissociated protein 1 (CAND1) promotes cardiomyocyte proliferation and heart regeneration by enhancing the ubiquitinated degradation of Mps one binder kinase activator 1b (Mob1b).. *Cell death and differentiation*. PMID: 40555744
5. FBXW11 inhibits tumorigenesis by ubiquitinating YB1 in hepatocarcinoma.. *Journal of cancer research and clinical oncology*. PMID: 40944757

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 70.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 82.5% |
| 可用 PDB 条目 | 6WNX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.2，有序区 82.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021977, IPR036047, IPR001810, IPR050995, IPR015943; Pfam: PF12125, PF12937, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.999 | 0.994 | — |
| CUL1 | 0.999 | 0.957 | — |
| RBX1 | 0.995 | 0.713 | — |
| BTRC | 0.993 | 0.841 | — |
| CTNNB1 | 0.993 | 0.852 | — |
| NFKBIA | 0.989 | 0.877 | — |
| SKP2 | 0.980 | 0.000 | — |
| FBXO5 | 0.965 | 0.493 | — |
| NFKBIB | 0.962 | 0.623 | — |
| GLI3 | 0.960 | 0.302 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIE | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| WEE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15070733|imex:IM-19870 |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15070733|imex:IM-19870 |
| RPRM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| vpu | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| FAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 6WNX | pLDDT=85.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Vesicles, Plasma membrane; 额外: Nucleoplasm | 一致 |
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
1. FBXW11 — F-box/WD repeat-containing protein 11，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小542 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000072803-FBXW11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXW11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
