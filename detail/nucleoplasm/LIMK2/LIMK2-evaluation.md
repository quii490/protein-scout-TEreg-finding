---
type: protein-evaluation
gene: "LIMK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LIMK2 — REJECTED (研究热度过高 (PubMed strict=150，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LIMK2 |
| 蛋白名称 | LIM domain kinase 2 |
| 蛋白大小 | 638 aa / 72.2 kDa |
| UniProt ID | P53671 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, m |
| 蛋白大小 | 10/10 | ×1 | 10 | 638 aa / 72.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=150 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.2; PDB: 1X6A, 4TPT, 5NXD, 7QHG, 8GI4, 8S3X, 8WSW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050940, IPR011009, IPR001478, IPR036034, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cis-Golgi network (GO:0005801)
- cytoplasm (GO:0005737)
- mitotic spindle (GO:0072686)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 150 |
| PubMed broad count | 286 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Decoding the tumour-modulatory roles of LIMK2.. *Life sciences*. PMID: 38580197
2. Biomarker Landscape in RASopathies.. *International journal of molecular sciences*. PMID: 39201250
3. LIMK2-NKX3.1 Engagement Promotes Castration-Resistant Prostate Cancer.. *Cancers*. PMID: 34066036
4. LIM kinase 2 activates cardiac fibroblasts and exacerbates postinfarction left ventricular remodeling via crosstalk between the canonical and non-canonical Wnt pathways.. *Pharmacological research*. PMID: 39153710
5. The Role of LIM Kinase in the Male Urogenital System.. *Cells*. PMID: 35011645

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 34.0% |
| 置信残基 (pLDDT 70-90) 占比 | 37.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 15.5% |
| 有序区域 (pLDDT>70) 占比 | 71.5% |
| 可用 PDB 条目 | 1X6A, 4TPT, 5NXD, 7QHG, 8GI4, 8S3X, 8WSW |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1X6A, 4TPT, 5NXD, 7QHG, 8GI4, 8S3X, 8WSW）+ AlphaFold极高置信度预测（pLDDT=76.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050940, IPR011009, IPR001478, IPR036034, IPR000719; Pfam: PF00412, PF00595, PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CFL1 | 0.995 | 0.555 | — |
| CFL2 | 0.990 | 0.130 | — |
| ROCK1 | 0.967 | 0.555 | — |
| LIMK1 | 0.962 | 0.611 | — |
| PAK4 | 0.943 | 0.076 | — |
| ROCK2 | 0.932 | 0.131 | — |
| COLEC12 | 0.926 | 0.098 | — |
| PAK1 | 0.916 | 0.071 | — |
| PAK5 | 0.912 | 0.076 | — |
| PAK6 | 0.912 | 0.076 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0G2RMD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380984 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| HSP90AB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17906|pubmed:22939624| |
| ATP5F1E | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TRIM35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC18A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UNC119 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HNRNPLL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 1X6A, 4TPT, 5NXD, 7QHG, 8GI4,  | pLDDT=76.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytos / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. LIMK2 — LIM domain kinase 2，研究基础较多，新颖性有限。
2. 蛋白大小638 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 150 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 150 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53671
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182541-LIMK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LIMK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53671
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
