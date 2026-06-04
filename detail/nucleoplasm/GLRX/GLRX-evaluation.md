---
type: protein-evaluation
gene: "GLRX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLRX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLRX / GRX |
| 蛋白名称 | Glutaredoxin-1 |
| 蛋白大小 | 106 aa / 11.8 kDa |
| UniProt ID | P35754 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 106 aa / 11.8 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=97 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=97.1; PDB: 1B4Q, 1JHB, 4RQR |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011767, IPR047185, IPR002109, IPR011899, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 97 |
| PubMed broad count | 275 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GRX |

**关键文献**:
1. Aortic Cellular Diversity and Quantitative Genome-Wide Association Study Trait Prioritization Through Single-Nuclear RNA Sequencing of the Aneurysmal Human Aorta.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 36172868
2. Reducing protein oxidation reverses lung fibrosis.. *Nature medicine*. PMID: 29988126
3. Pain/Stress, Mitochondrial Dysfunction, and Neurodevelopment in Preterm Infants.. *Developmental neuroscience*. PMID: 38286121
4. Glutaredoxin-1 promotes lymphangioleiomyomatosis progression through inhibiting Bim-mediated apoptosis via COX2/PGE2/ERK pathway.. *Clinical and translational medicine*. PMID: 37478294
5. Glutaredoxin 1 regulates cholesterol metabolism and gallstone formation by influencing protein S-glutathionylation.. *Metabolism: clinical and experimental*. PMID: 37277061

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.1 |
| 高置信度残基 (pLDDT>90) 占比 | 98.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 1B4Q, 1JHB, 4RQR |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1B4Q, 1JHB, 4RQR）+ AlphaFold高质量预测（pLDDT=97.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011767, IPR047185, IPR002109, IPR011899, IPR014025; Pfam: PF00462 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSR | 0.980 | 0.070 | — |
| RRM1 | 0.976 | 0.412 | — |
| TXN | 0.966 | 0.065 | — |
| TXNRD1 | 0.923 | 0.077 | — |
| GLRX5 | 0.920 | 0.000 | — |
| MSRA | 0.896 | 0.602 | — |
| GLRX3 | 0.888 | 0.100 | — |
| GPX2 | 0.869 | 0.070 | — |
| GPX3 | 0.868 | 0.070 | — |
| GPX7 | 0.863 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AQP5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CASP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MMP23B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CFAP298 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM62 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CHURC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HTRA4 | psi-mi:"MI:0096"(pull down) | imex:IM-28152|pubmed:31470122 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| OR2A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| 24334" | psi-mi:"MI:0435"(protease assay) | pubmed:34399606|imex:IM-29177 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.1 + PDB: 1B4Q, 1JHB, 4RQR | pLDDT=97.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. GLRX — Glutaredoxin-1，研究基础较多，新颖性有限。
2. 蛋白大小106 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 97 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35754
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173221-GLRX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLRX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35754
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
