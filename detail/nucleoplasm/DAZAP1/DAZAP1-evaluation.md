---
type: protein-evaluation
gene: "DAZAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DAZAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAZAP1 |
| 蛋白名称 | DAZ-associated protein 1 |
| 蛋白大小 | 407 aa / 43.4 kDa |
| UniProt ID | Q96EP5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Midbody, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 407 aa / 43.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.7; PDB: 2DGS, 2DH8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034134, IPR034131, IPR012677, IPR035979, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Midbody, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- male germ cell nucleus (GO:0001673)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genomic analyses identify recurrent MEF2D fusions in acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27824051
2. DAZAP1 Phase Separation Regulates Mitochondrial Metabolism to Facilitate Invasion and Metastasis of Oral Squamous Cell Carcinoma.. *Cancer research*. PMID: 39120588
3. Genomic and epigenomic insights into the origin, pathogenesis, and clinical behavior of mantle cell lymphoma subtypes.. *Blood*. PMID: 32584970
4. DAZAP1 maintains gastric cancer stemness by inducing mitophagy.. *JCI insight*. PMID: 40401521
5. DAZAP1 promotes cancer progression and chemotherapy resistance by stabilizing PIN1 protein in gastric cancer.. *Cell biology and toxicology*. PMID: 41331184

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.7 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 21.9% |
| 低置信 (pLDDT<50) 占比 | 38.1% |
| 有序区域 (pLDDT>70) 占比 | 40.1% |
| 可用 PDB 条目 | 2DGS, 2DH8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.7），有序残基占 40.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034134, IPR034131, IPR012677, IPR035979, IPR000504; Pfam: PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DAZ1 | 0.949 | 0.334 | — |
| DAZAP2 | 0.938 | 0.000 | — |
| MSI1 | 0.911 | 0.000 | — |
| MSI2 | 0.909 | 0.000 | — |
| KHSRP | 0.839 | 0.000 | — |
| DAZL | 0.839 | 0.456 | — |
| ZC3H14 | 0.832 | 0.782 | — |
| HNRNPA1 | 0.692 | 0.256 | — |
| HNRNPH1 | 0.675 | 0.354 | — |
| SRSF1 | 0.654 | 0.189 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| PPP2R2B | psi-mi:"MI:0096"(pull down) | imex:IM-9155|pubmed:19156129 |
| RAD52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19338310|imex:IM-17201 |
| EBI-6095751 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19119138|imex:IM-20555 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.7 + PDB: 2DGS, 2DH8 | pLDDT=64.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Midbody, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DAZAP1 — DAZ-associated protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小407 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EP5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000071626-DAZAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAZAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EP5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
