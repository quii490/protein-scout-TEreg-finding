---
type: protein-evaluation
gene: "BAG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BAG1 — REJECTED (研究热度过高 (PubMed strict=552，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BAG1 / HAP |
| 蛋白名称 | BAG family molecular chaperone regulator 1 |
| 蛋白大小 | 345 aa / 38.8 kDa |
| UniProt ID | Q99933 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 38.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=552 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.7; PDB: 1HX1, 1WXV, 3FZF, 3FZH, 3FZK, 3FZL, 3FZM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039773, IPR036533, IPR003103, IPR000626, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 552 |
| PubMed broad count | 838 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HAP |

**关键文献**:
1. Comparative analysis of BAG1 and BAG2: Insights into their structures, functions and implications in disease pathogenesis.. *International immunopharmacology*. PMID: 39405938
2. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
3. Deciphering the prognostic and therapeutic significance of BAG1 and BAG2 for predicting distinct survival outcome and effects on liposarcoma.. *Scientific reports*. PMID: 39366981
4. Bag1 protein loss sensitizes mouse embryonic fibroblasts to glutathione depletion.. *Cell stress & chaperones*. PMID: 38763404
5. Gene cloning and characterization of the protein encoded by the Neospora caninum bradyzoite-specific antigen gene BAG1.. *The Journal of parasitology*. PMID: 23245337

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.4% |
| 置信残基 (pLDDT 70-90) 占比 | 34.5% |
| 中等置信 (pLDDT 50-70) 占比 | 25.5% |
| 低置信 (pLDDT<50) 占比 | 33.6% |
| 有序区域 (pLDDT>70) 占比 | 40.9% |
| 可用 PDB 条目 | 1HX1, 1WXV, 3FZF, 3FZH, 3FZK, 3FZL, 3FZM, 3LDQ, 3M3Z, 5AQF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.7），有序残基占 40.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039773, IPR036533, IPR003103, IPR000626, IPR029071; Pfam: PF02179, PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.999 | 0.994 | — |
| HSPA4 | 0.999 | 0.882 | — |
| BAG2 | 0.997 | 0.000 | — |
| BCL2 | 0.996 | 0.477 | — |
| DNAJB1 | 0.991 | 0.366 | — |
| HSPBP1 | 0.973 | 0.000 | — |
| HSPA1B | 0.971 | 0.791 | — |
| BAG3 | 0.967 | 0.226 | — |
| STUB1 | 0.963 | 0.836 | — |
| HSPH1 | 0.954 | 0.310 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARRB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PYGL | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| A0A0G2RNT6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CAM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| purA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GTF3C2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YY1AP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CPZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYP2W1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.7 + PDB: 1HX1, 1WXV, 3FZF, 3FZH, 3FZK,  | pLDDT=62.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm; / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BAG1 — BAG family molecular chaperone regulator 1，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 552 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 552 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99933
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107262-BAG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BAG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99933
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
