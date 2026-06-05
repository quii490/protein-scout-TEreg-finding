---
type: protein-evaluation
gene: "CLSPN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLSPN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLSPN |
| 蛋白名称 | Claspin |
| 蛋白大小 | 1339 aa / 151.1 kDa |
| UniProt ID | Q9HAW4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1339 aa / 151.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.6; PDB: 7AKO, 7PFO, 7PLO, 8B9D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024146 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 169 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Interaction between CLSPN Gene Polymorphisms and Alcohol Consumption Contributes to Oral Cancer Progression.. *International journal of molecular sciences*. PMID: 38256171
2. Claspin Overexpression Promotes Tumor Progression and Predicts Poor Clinical Outcome in Prostate Cancer.. *Genetic testing and molecular biomarkers*. PMID: 33596143
3. ALKBH5-IGF2BP2 axis mediates prostate cancer progression and docetaxel resistance via m6A-stabilized CLSPN RNA.. *iScience*. PMID: 41069850
4. CLSPN actives Wnt/β-catenin signaling to facilitate glycolysis and cell proliferation in oral squamous cell carcinoma.. *Experimental cell research*. PMID: 38237848
5. Implications of CLSPN Variants in Cellular Function and Susceptibility to Cancer.. *Cancers*. PMID: 32847043

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.6 |
| 高置信度残基 (pLDDT>90) 占比 | 6.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 60.3% |
| 有序区域 (pLDDT>70) 占比 | 25.6% |
| 可用 PDB 条目 | 7AKO, 7PFO, 7PLO, 8B9D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.6），有序残基占 25.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024146 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHEK1 | 0.999 | 0.882 | — |
| TIMELESS | 0.999 | 0.898 | — |
| TIPIN | 0.999 | 0.852 | — |
| RPA2 | 0.998 | 0.994 | — |
| RPA1 | 0.998 | 0.994 | — |
| RPA3 | 0.998 | 0.994 | — |
| WDHD1 | 0.998 | 0.800 | — |
| PRIMPOL | 0.996 | 0.994 | — |
| TOPBP1 | 0.995 | 0.000 | — |
| CDC45 | 0.995 | 0.895 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FZR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11905|pubmed:18662541 |
| CHEK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:16963448|imex:IM-18894 |
| LACC1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| GINS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INPP5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MCM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RAPGEF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MCM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MCM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MMTAG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.6 + PDB: 7AKO, 7PFO, 7PLO, 8B9D | pLDDT=50.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Golgi apparatus | 一致 |
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
1. CLSPN — Claspin，非常新颖，仅有少数基础研究。
2. 蛋白大小1339 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=50.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAW4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092853-CLSPN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLSPN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAW4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000092853-CLSPN/subcellular

![](https://images.proteinatlas.org/26305/1609_D11_3_red_green.jpg)
![](https://images.proteinatlas.org/26305/1609_D11_4_red_green.jpg)
![](https://images.proteinatlas.org/26305/1632_F9_28_cr577fbd78aeef0_red_green.jpg)
![](https://images.proteinatlas.org/26305/1632_F9_33_cr577fbd7f02117_red_green.jpg)
![](https://images.proteinatlas.org/26305/1634_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/26305/1634_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HAW4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
