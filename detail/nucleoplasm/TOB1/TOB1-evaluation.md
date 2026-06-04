---
type: protein-evaluation
gene: "TOB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TOB1 — REJECTED (研究热度过高 (PubMed strict=139，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TOB1 / TOB, TROB1 |
| 蛋白名称 | Protein Tob1 |
| 蛋白大小 | 345 aa / 38.2 kDa |
| UniProt ID | P50616 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 38.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=139 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 2D5R, 2Z15, 5CI8, 5CI9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002087, IPR036054, IPR015676; Pfam: PF07742 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- CCR4-NOT complex (GO:0030014)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 139 |
| PubMed broad count | 245 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TOB, TROB1 |

**关键文献**:
1. Analyses of non-coding somatic drivers in 2,658 cancer whole genomes.. *Nature*. PMID: 32025015
2. TOB1 modulates neutrophil phenotypes to influence gastric cancer progression and immunotherapy efficacy.. *Frontiers in immunology*. PMID: 38617839
3. Decreased TOB1 expression and increased phosphorylation of nuclear TOB1 promotes gastric cancer.. *Oncotarget*. PMID: 29088861
4. Methylation Mediated Downregulation of TOB1-AS1 and TOB1 Correlates with Malignant Progression and Poor Prognosis of Esophageal Squamous Cell Carcinoma.. *Digestive diseases and sciences*. PMID: 36002674
5. TOB1 Blocks Intestinal Mucosal Inflammation Through Inducing ID2-Mediated Suppression of Th1/Th17 Cell Immune Responses in IBD.. *Cellular and molecular gastroenterology and hepatology*. PMID: 34920145

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 33.3% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.7% |
| 低置信 (pLDDT<50) 占比 | 39.4% |
| 有序区域 (pLDDT>70) 占比 | 38.8% |
| 可用 PDB 条目 | 2D5R, 2Z15, 5CI8, 5CI9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 38.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002087, IPR036054, IPR015676; Pfam: PF07742 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT7 | 0.999 | 0.989 | — |
| CNOT8 | 0.987 | 0.652 | — |
| CNOT1 | 0.984 | 0.797 | — |
| CNOT6L | 0.983 | 0.788 | — |
| CNOT10 | 0.980 | 0.786 | — |
| CNOT3 | 0.980 | 0.786 | — |
| CNOT9 | 0.979 | 0.768 | — |
| CNOT11 | 0.979 | 0.782 | — |
| CNOT2 | 0.978 | 0.754 | — |
| TNKS1BP1 | 0.977 | 0.780 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SCMH1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CNOT7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CNOT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CNOT6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAVER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CNOT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OBI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 2D5R, 2Z15, 5CI8, 5CI9 | pLDDT=66.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. TOB1 — Protein Tob1，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 139 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 139 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50616
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141232-TOB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TOB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50616
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
