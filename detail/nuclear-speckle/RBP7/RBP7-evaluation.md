---
type: protein-evaluation
gene: "RBP7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RBP7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RBP7 |
| 蛋白名称 | Retinoid-binding protein 7 |
| 蛋白大小 | 134 aa / 15.5 kDa |
| UniProt ID | Q96R05 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 134 aa / 15.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=52 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=96.2; PDB: 1LPJ, 6AT8, 6E6K |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012674, IPR000463, IPR031259, IPR000566; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytosol | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 52 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Genes Related to 5-Fluorouracil Based Chemotherapy for Colorectal Cancer.. *Frontiers in immunology*. PMID: 35784334
2. Adipose-specific expression of mouse Rbp7 gene and its developmental and metabolic changes.. *Gene*. PMID: 29803924
3. Retinol-binding protein 7 is an endothelium-specific PPARγ cofactor mediating an antioxidant response through adiponectin.. *JCI insight*. PMID: 28352663
4. Reduced Expression of RBP7 is Associated with Resistance to Tamoxifen In Luminal A Breast Cancer.. *Anti-cancer agents in medicinal chemistry*. PMID: 36537604
5. RBP7 Regulated by EBF1 Affects Th2 Cells and the Oocyte Meiosis Pathway in Bone Metastases of Bladder Urothelial Carcinoma.. *Frontiers in bioscience (Landmark edition)*. PMID: 37664915

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.2 |
| 高置信度残基 (pLDDT>90) 占比 | 94.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.2% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 1LPJ, 6AT8, 6E6K |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1LPJ, 6AT8, 6E6K）+ AlphaFold高质量预测（pLDDT=96.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012674, IPR000463, IPR031259, IPR000566; Pfam: PF00061 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLR2D | 0.759 | 0.000 | — |
| POLR2G | 0.513 | 0.000 | — |
| POLR2K | 0.467 | 0.000 | — |
| UBE4B | 0.457 | 0.000 | — |
| RARS1 | 0.455 | 0.000 | — |
| LRRK1 | 0.434 | 0.000 | — |
| RBP4 | 0.427 | 0.000 | — |
| SOCS4 | 0.426 | 0.421 | — |
| HSH2D | 0.420 | 0.421 | — |
| PIK3R3 | 0.420 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hrb27C | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14204 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "fs | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| tna | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| FER | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| recC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NCKIPSD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Spn | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Dmel\CG16812 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| HSH2D | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.2 + PDB: 1LPJ, 6AT8, 6E6K | pLDDT=96.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nuclear speckles, Cytosol | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RBP7 — Retinoid-binding protein 7，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小134 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 52 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96R05
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162444-RBP7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RBP7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96R05
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
