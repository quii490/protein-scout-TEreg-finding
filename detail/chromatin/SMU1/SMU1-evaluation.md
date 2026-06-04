---
type: protein-evaluation
gene: "SMU1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SMU1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SMU1 / SMU-1|FLJ10805|BWD|fSAP57 |
| 蛋白全称 | WD40 repeat-containing protein SMU1 |
| 蛋白大小 | 513 aa |
| UniProt ID | Q2TAY7 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SMU1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SMU1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 513 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 18 篇，极度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 9 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 19 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **126.5/183** |  |
| **归一化总分** |  |  | **69.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Cytoplasm, Nucleus, Nucleus speckle | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 513 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 18 |

**关键文献**:
1. Long et al. (2024). "Cotranscriptional splicing is required in the cold to produce COOLAIR isoforms that repress Arabidopsis FLC.". *Proc Natl Acad Sci U S A*. PMID: 39546565
2. Feng et al. (2020). "An SMU Splicing Factor Complex Within Nuclear Speckles Contributes to Magnesium Homeostasis in Arabidopsis.". *Plant Physiol*. PMID: 32601148
3. Zhao et al. (2023). "Dynamic changes of 3'UTR length during oocyte-to-zygote transition of in vitro pig embryos.". *Reprod Domest Anim*. PMID: 36755113
4. Ashraf et al. (2019). "Destabilization of the human RED-SMU1 splicing complex as a basis for host-directed antiinfluenza strategy.". *Proc Natl Acad Sci U S A*. PMID: 31076555
5. Lovely et al. (2011). "Role of Hsl7 in morphology and pathogenicity and its interaction with other signaling components in the plant pathogen Ustilago maydis.". *Eukaryot Cell*. PMID: 21622903
**评价**: PubMed 18 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 513 aa |
| PDB 条数 | 9 |
| 已注释结构域 | 19 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SMU1/SMU1-PAE.png]]

**评价**: 9 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | CTLH_C |
| InterPro | LisH |
| InterPro | SMU1 |
| InterPro | TPL_SMU1_LisH-like |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | LisH_TPL |
| Pfam | WD40 |
| SMART | CTLH |
| SMART | LisH |
| SMART | WD40 |
| PROSITE | CTLH |

**染色质调控潜力分析**: 19 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 9 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 19 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 18 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 9 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SMU1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122692-SMU1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SMU1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q2TAY7
- STRING: https://string-db.org/network/9606.ENSG00000122692
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TAY7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SMU1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SMU1/SMU1-PAE.png]]




