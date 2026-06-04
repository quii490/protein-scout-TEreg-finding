---
type: protein-evaluation
gene: "TXK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TXK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TXK / PTK4, RLK |
| 蛋白名称 | Tyrosine-protein kinase TXK |
| 蛋白大小 | 527 aa / 61.3 kDa |
| UniProt ID | P42681 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli, Plasma membrane; UniProt: Cytoplasm; Nucleus; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 527 aa / 61.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.5; PDB: 2DM0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR050198, IPR000719, IPR017441, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli, Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 103 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PTK4, RLK |

**关键文献**:
1. Biochemical and genetic analyses of the Tec kinases Itk and Rlk/Txk.. *Biochemical Society transactions*. PMID: 11709089
2. Pathogenetic Dichotomy in Angioleiomyoma.. *Cancer genomics & proteomics*. PMID: 37889065
3. Role of Txk, a member of the Tec family of tyrosine kinases, in immune-inflammatory diseases.. *International reviews of immunology*. PMID: 18027204
4. Skewed Th1 responses caused by excessive expression of Txk, a member of the Tec family of tyrosine kinases, in patients with Behcet's disease.. *Clinical medicine & research*. PMID: 16809408
5. Polymorphisms of TXK and PLCE1 Genes and Their Correlation Analysis with Growth Traits in Ashidan Yaks.. *Animals : an open access journal from MDPI*. PMID: 39682472

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 46.5% |
| 置信残基 (pLDDT 70-90) 占比 | 32.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 79.1% |
| 可用 PDB 条目 | 2DM0 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=79.5，有序区 79.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR050198, IPR000719, IPR017441, IPR001245; Pfam: PF07714, PF00017, PF00018 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAV1 | 0.960 | 0.000 | — |
| VAV3 | 0.946 | 0.000 | — |
| ITK | 0.940 | 0.000 | — |
| PIK3R1 | 0.927 | 0.232 | — |
| PIK3CD | 0.923 | 0.069 | — |
| VAV2 | 0.919 | 0.000 | — |
| PIK3CB | 0.916 | 0.069 | — |
| PIK3CA | 0.914 | 0.069 | — |
| PIK3R3 | 0.911 | 0.093 | — |
| PIK3R2 | 0.909 | 0.093 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2296405 | psi-mi:"MI:0400"(affinity technology) | imex:IM-11692|pubmed:19946567 |
| EBI-1263288 | psi-mi:"MI:0400"(affinity technology) | imex:IM-11692|pubmed:19946567 |
| NCK2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| IKZF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CRK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GRB10 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZNF587 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SOCS3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DOK2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DUSP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 2DM0 | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane / Nucleoplasm, Cytosol; 额外: Nucleoli, Plasma membran | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TXK — Tyrosine-protein kinase TXK，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小527 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P42681
- Protein Atlas: https://www.proteinatlas.org/ENSG00000074966-TXK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TXK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P42681
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
