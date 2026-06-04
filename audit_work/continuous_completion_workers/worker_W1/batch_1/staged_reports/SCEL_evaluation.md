---
type: protein-evaluation
gene: "SCEL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SCEL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SCEL |
| 蛋白名称 | Sciellin |
| 蛋白大小 | 688 aa / 77.6 kDa |
| UniProt ID | O95171 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 688 aa / 77.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052621, IPR001781 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A Single-Cell Atlas of the Human Healthy Airways.. *American journal of respiratory and critical care medicine*. PMID: 32726565
2. Sciellin inhibits senescence and promotes pancreatic cancer progress by activating the notch signaling pathway.. *Scientific reports*. PMID: 40341648
3. CBX8 promotes lung adenocarcinoma growth and metastasis through transcriptional repression of CDKN2C and SCEL.. *Journal of cellular physiology*. PMID: 37733753
4. Clinical significance and diagnostic value of QPCT, SCEL and TNFRSF12A in papillary thyroid cancer.. *Pathology, research and practice*. PMID: 37060824
5. Silencing of SCEL promotes progression of oral squamous cell carcinoma via activating TGF-β/Smad pathway.. *Discover oncology*. PMID: 40372539

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.2 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 78.8% |
| 有序区域 (pLDDT>70) 占比 | 10.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=45.2），有序残基占 10.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052621, IPR001781 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SULF1 | 0.752 | 0.000 | — |
| SYNPO | 0.720 | 0.091 | — |
| YIPF3 | 0.711 | 0.000 | — |
| CYP26A1 | 0.700 | 0.046 | — |
| ACTN4 | 0.636 | 0.000 | — |
| NPHS1 | 0.601 | 0.000 | — |
| SPRR2B | 0.573 | 0.000 | — |
| LCE3D | 0.563 | 0.000 | — |
| POU4F2 | 0.547 | 0.000 | — |
| CRNN | 0.539 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAB11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCT8 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FXR2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| NMI | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| MTUS2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| KIFC3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| TSGA10 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| LRRK1 | psi-mi:"MI:0089"(protein array) | pubmed:24947832|imex:IM-22653 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.2 + PDB: 无 | pLDDT=45.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane / Plasma membrane; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SCEL — Sciellin，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小688 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=45.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95171
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136155-SCEL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCEL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95171
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
