---
type: protein-evaluation
gene: "EPC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPC1 |
| 蛋白名称 | Enhancer of polycomb homolog 1 |
| 蛋白大小 | 836 aa / 93.5 kDa |
| UniProt ID | Q9H2F5 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC1/IF_images/REH_1.jpg|REH]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Nuclear bodies; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 836 aa / 93.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=99 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 6NFX, 8QR1, 8XVG, 8XVT, 9C57, 9C62, 9C6N |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024943, IPR019542, IPR009607; Pfam: PF06752, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Nuclear bodies | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- NuA4 histone acetyltransferase complex (GO:0035267)
- nuclear body (GO:0016604)
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 99 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Expression and Biological Functions of EPC1 in Nasopharyngeal Carcinoma.. *Archives of Iranian medicine*. PMID: 34841830
2. Enhancers of Polycomb EPC1 and EPC2 sustain the oncogenic potential of MLL leukemia stem cells.. *Leukemia*. PMID: 24166297
3. Identification of a diagnostic antibody-binding region on the immunogenic protein EpC1 from Echinococcus granulosus and its application in population screening for cystic echinococcosis.. *Clinical and experimental immunology*. PMID: 17403055
4. Structural Basis for EPC1-Mediated Recruitment of MBTD1 into the NuA4/TIP60 Acetyltransferase Complex.. *Cell reports*. PMID: 32209463
5. Role for O-glycosylation of RFP in the interaction with enhancer of polycomb.. *Biochemical and biophysical research communications*. PMID: 11779184

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 11.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.6% |
| 低置信 (pLDDT<50) 占比 | 49.3% |
| 有序区域 (pLDDT>70) 占比 | 33.1% |
| 可用 PDB 条目 | 6NFX, 8QR1, 8XVG, 8XVT, 9C57, 9C62, 9C6N, 9CAC, 9CAE |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC1/EPC1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 33.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024943, IPR019542, IPR009607; Pfam: PF06752, PF10513 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DMAP1 | 0.999 | 0.963 | — |
| MEAF6 | 0.999 | 0.962 | — |
| YEATS4 | 0.998 | 0.946 | — |
| TRRAP | 0.998 | 0.951 | — |
| KAT5 | 0.997 | 0.930 | — |
| MORF4L1 | 0.997 | 0.930 | — |
| ING3 | 0.996 | 0.900 | — |
| MRGBP | 0.995 | 0.934 | — |
| ACTL6A | 0.990 | 0.868 | — |
| RUVBL1 | 0.986 | 0.801 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| MRGBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| VPS72 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15647280 |
| ACTL6A | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15647280 |
| RUVBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| Dmap1 | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| Kat5 | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| EXOC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CEP63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 6NFX, 8QR1, 8XVG, 8XVT, 9C57,  | pLDDT=56.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nucleoli, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. EPC1 — Enhancer of polycomb homolog 1，研究基础较多，新颖性有限。
2. 蛋白大小836 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 99 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2F5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120616-EPC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2F5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC1/EPC1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H2F5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024943;IPR019542;IPR009607; |
| Pfam | PF06752;PF10513; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120616-EPC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRD8 | Intact, Biogrid | true |
| MBTD1 | Intact, Biogrid | true |
| RUVBL2 | Biogrid, Opencell | true |
| DMAP1 | Biogrid | false |
| E2F6 | Biogrid | false |
| EP400 | Biogrid | false |
| EZH2 | Biogrid | false |
| FOXR1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
