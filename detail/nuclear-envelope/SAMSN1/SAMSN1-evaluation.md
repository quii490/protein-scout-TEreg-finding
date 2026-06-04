---
type: protein-evaluation
gene: "SAMSN1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SAMSN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SAMSN1 / NASH1|SASH2|SH3D6B|HACS1|SLy2 |
| 蛋白全称 | SAM domain-containing protein SAMSN-1 |
| 蛋白大小 | 373 aa |
| UniProt ID | Q9NSI8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMSN1/IF_images/HEL_1.jpg|HEL]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMSN1/IF_images/K-562_1.jpg|K-562]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 373 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 41 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 14 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Cytoplasm, Cell projection, ruffle | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 373 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 41 |

**关键文献**:
1. Li et al. (2023). "Differentiation-related genes in tumor-associated macrophages as potential prognostic biomarkers in non-small cell lung cancer.". *Front Immunol*. PMID: 36969247
2. Wang et al. (2026). "SAMSN1 restrains NK cell mediated anti-tumor immunity in hepatocellular carcinoma.". *Nat Commun*. PMID: 41565668
3. Sierksma et al. (2020). "Novel Alzheimer risk genes determine the microglia response to amyloid-β but not to TAU pathology.". *EMBO Mol Med*. PMID: 31951107
4. An et al. (2025). "Exploration of the shared diagnostic genes and molecular mechanism between obesity and atherosclerosis via bioinformatic analysis.". *Sci Rep*. PMID: 39825072
5. Li et al. (2025). "SAMSN1 causes sepsis immunosuppression by inducing macrophages to express coinhibitory molecules that cause T-cell exhaustion via KEAP1-NRF2 signaling.". *Chin Med J (Engl)*. PMID: 40293473
**评价**: PubMed 41 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 373 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMSN1/SAMSN1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SAM |
| InterPro | SAM-SH3_domain_protein |
| InterPro | SAM/pointed_sf |
| InterPro | SAMSN1_SAM |
| InterPro | SH3-like_dom_sf |
| InterPro | SH3_domain |
| InterPro | SPIDER |
| Pfam | SAM_2 |
| Pfam | SH3_2 |
| Pfam | SPIDER |
| SMART | SAM |
| SMART | SH3 |
| PROSITE | SAM_DOMAIN |
| PROSITE | SH3 |

**染色质调控潜力分析**: 14 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 41 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAMSN1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155307-SAMSN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SAMSN1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9NSI8
- STRING: https://string-db.org/network/9606.ENSG00000155307
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSI8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SAMSN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMSN1/SAMSN1-PAE.png]]




