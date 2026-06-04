---
type: protein-evaluation
gene: "LMTK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LMTK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMTK2 / AATYK2, BREK, KIAA1079, KPI2, LMR2 |
| 蛋白名称 | Serine/threonine-protein kinase LMTK2 |
| 蛋白大小 | 1503 aa / 164.9 kDa |
| UniProt ID | Q8IWU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles, Centriolar satellite; 额外: Plasma membrane,; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1503 aa / 164.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR001245, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.0/180** | |
| **归一化总分** | | | **58.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Centriolar satellite; 额外: Plasma membrane, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- early endosome (GO:0005769)
- Golgi apparatus (GO:0005794)
- growth cone (GO:0030426)
- membrane (GO:0016020)
- neuronal cell body (GO:0043025)
- perinuclear region of cytoplasm (GO:0048471)
- recycling endosome (GO:0055037)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 67 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AATYK2, BREK, KIAA1079, KPI2, LMR2 |

**关键文献**:
1. Biological function of Lemur tyrosine kinase 2 (LMTK2): implications in neurodegeneration.. *Molecular brain*. PMID: 29631601
2. Lemur tyrosine kinase 2 has a tumor-inhibition function in human glioblastoma by regulating the RUNX3/Notch pathway.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 37271222
3. Signal dependent ER export of lemur tyrosine kinase 2.. *BMC cell biology*. PMID: 26559041
4. The IRE1α/XBP1-mediated upregulation of LMTK2 attenuates endoplasmic reticulum stress by enhancing autophagic activity.. *Cancer letters*. PMID: 40834986
5. Unraveling the Function of Lemur Tyrosine Kinase 2 Network.. *Frontiers in pharmacology*. PMID: 30761001

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.8 |
| 高置信度残基 (pLDDT>90) 占比 | 14.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 73.7% |
| 有序区域 (pLDDT>70) 占比 | 22.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=46.8），有序残基占 22.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR001245, IPR008266; Pfam: PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP1CC | 0.886 | 0.728 | — |
| PPP1R2 | 0.823 | 0.324 | — |
| MYO6 | 0.751 | 0.625 | — |
| MSMB | 0.726 | 0.000 | — |
| PPP1CA | 0.692 | 0.389 | — |
| EHBP1 | 0.691 | 0.000 | — |
| TOM1 | 0.673 | 0.000 | — |
| DAB2 | 0.645 | 0.058 | — |
| JAZF1 | 0.638 | 0.000 | — |
| KLK3 | 0.555 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1R2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12393858|imex:IM-20116 |
| ENSP00000297293.5 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:12393858|imex:IM-20116 |
| PPP1CA | psi-mi:"MI:0424"(protein kinase assay) | pubmed:12393858|imex:IM-20116 |
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| SLC34A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Lyplal1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SORT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Coro1c | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.8 + PDB: 无 | pLDDT=46.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear speckles, Centriolar satellite; 额外: Plasma | 一致 |
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
1. LMTK2 — Serine/threonine-protein kinase LMTK2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1503 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=46.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164715-LMTK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMTK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
