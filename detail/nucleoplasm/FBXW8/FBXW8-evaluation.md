---
type: protein-evaluation
gene: "FBXW8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXW8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXW8 / FBW6, FBW8, FBX29, FBXO29, FBXW6 |
| 蛋白名称 | F-box/WD repeat-containing protein 8 |
| 蛋白大小 | 598 aa / 67.4 kDa |
| UniProt ID | Q8N3Y1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, perinuclear region; Golgi apparatus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 598 aa / 67.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.8; PDB: 7Z8B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR011047, IPR015943, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, perinuclear region; Golgi apparatus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- ciliary basal body (GO:0036064)
- Cul7-RING ubiquitin ligase complex (GO:0031467)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- perinuclear region of cytoplasm (GO:0048471)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBW6, FBW8, FBX29, FBXO29, FBXW6 |

**关键文献**:
1. USP5 stabilizes YTHDF1 to control cancer immune surveillance through mTORC1-mediated phosphorylation.. *Nature communications*. PMID: 39900921
2. The CRL7(FBXW8) Complex Controls the Mammary Stem Cell Compartment through Regulation of NUMB Levels.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40411418
3. FBXW8-mediated degradation of PPT1 suppresses epithelial-mesenchymal transition and metastasis in hepatocellular carcinoma.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 40659255
4. Disruption of the Fbxw8 gene results in pre- and postnatal growth retardation in mice.. *Molecular and cellular biology*. PMID: 17998335
5. Structure of CRL7(FBXW8) reveals coupling with CUL1-RBX1/ROC1 for multi-cullin-RING E3-catalyzed ubiquitin ligation.. *Nature structural & molecular biology*. PMID: 35982156

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 48.8% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 19.1% |
| 有序区域 (pLDDT>70) 占比 | 71.0% |
| 可用 PDB 条目 | 7Z8B |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=76.8，有序区 71.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR011047, IPR015943, IPR001680; Pfam: PF12937 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL7 | 0.999 | 0.895 | — |
| SKP1 | 0.999 | 0.914 | — |
| RBX1 | 0.999 | 0.854 | — |
| CUL1 | 0.992 | 0.878 | — |
| GLMN | 0.979 | 0.000 | — |
| OBSL1 | 0.909 | 0.512 | — |
| SKP2 | 0.885 | 0.292 | — |
| UBA3 | 0.867 | 0.071 | — |
| FBXO4 | 0.837 | 0.299 | — |
| IRS1 | 0.825 | 0.705 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15070733|imex:IM-19870 |
| MYC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17314511 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFC3H1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF263 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CETN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 7Z8B | pLDDT=76.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Golgi apparatus; Cy / Cytosol | 一致 |
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
1. FBXW8 — F-box/WD repeat-containing protein 8，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小598 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3Y1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174989-FBXW8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXW8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3Y1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
