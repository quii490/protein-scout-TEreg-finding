---
type: protein-evaluation
gene: "FBXL17"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXL17 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL17 / FBL17, FBX13, FBXO13 |
| 蛋白名称 | F-box/LRR-repeat protein 17 |
| 蛋白大小 | 701 aa / 75.7 kDa |
| UniProt ID | Q9UF56 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 701 aa / 75.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.4; PDB: 6W66, 6WCQ, 8UAH, 8UBT, 8UBU, 8UBV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR050648, IPR057207, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL17, FBX13, FBXO13 |

**关键文献**:
1. Recognition of BACH1 quaternary structure degrons by two F-box proteins under oxidative stress.. *Cell*. PMID: 39504958
2. SCF (Fbxl17) ubiquitylation of Sufu regulates Hedgehog signaling and medulloblastoma development.. *The EMBO journal*. PMID: 27234298
3. FBXL17/spastin axis as a novel therapeutic target of hereditary spastic paraplegia.. *Cell & bioscience*. PMID: 35869491
4. Lipopolysaccharide modulates p300 and Sirt1 to promote PRMT1 stability via an SCF(Fbxl17)-recognized acetyldegron.. *Journal of cell science*. PMID: 28883095
5. Host genetics influences the relationship between the gut microbiome and psychiatric disorders.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 33130294

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.4 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 43.1% |
| 有序区域 (pLDDT>70) 占比 | 53.7% |
| 可用 PDB 条目 | 6W66, 6WCQ, 8UAH, 8UBT, 8UBU, 8UBV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.4），有序残基占 53.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR050648, IPR057207, IPR001611; Pfam: PF25372, PF12937, PF13516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.999 | 0.987 | — |
| SKP1 | 0.998 | 0.988 | — |
| BACH1 | 0.980 | 0.782 | — |
| KEAP1 | 0.955 | 0.949 | — |
| RBX1 | 0.897 | 0.685 | — |
| KLHL12 | 0.859 | 0.790 | — |
| SUFU | 0.783 | 0.625 | — |
| ZBTB18 | 0.658 | 0.615 | — |
| SKP2 | 0.640 | 0.000 | — |
| KLHL28 | 0.633 | 0.633 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| KLHL14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KBTBD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB46 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BACH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB42 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.4 + PDB: 6W66, 6WCQ, 8UAH, 8UBT, 8UBU,  | pLDDT=68.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXL17 — F-box/LRR-repeat protein 17，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小701 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UF56
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145743-FBXL17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UF56
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000145743-FBXL17/subcellular

![](https://images.proteinatlas.org/36410/605_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/36410/605_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/36410/606_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/36410/606_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/36410/608_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/36410/608_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UF56-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
