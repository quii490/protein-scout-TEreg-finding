---
type: protein-evaluation
gene: "SGTA"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGTA 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SGTA / UBP|SGT1|Vpu|hSGT|alphaSGT |
| 蛋白全称 | Small glutamine-rich tetratricopeptide repeat-containing protein alpha |
| 蛋白大小 | 313 aa |
| UniProt ID | O43765 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SGTA/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SGTA/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 313 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 81 篇，中等研究热度 |
| 三维结构 | 10/10 | ×3 | **30** | 5 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 10 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **99/183** | **98.0/183** |  |  |
|  | **归一化总分** |  | **54.1/100** | **53.6/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA|IMP|TAS |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: 313 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 81 |

**关键文献**:
1. Müller et al. (2023). "Mechanisms of readthrough mitigation reveal principles of GCN1-mediated translational quality control.". *Cell*. PMID: 37339632
2. Leznicki et al. (2020). "SGTA associates with nascent membrane protein precursors.". *EMBO Rep*. PMID: 32216016
3. Roberts et al. (2015). "Structural and Functional Insights into Small, Glutamine-Rich, Tetratricopeptide Repeat Protein Alpha.". *Front Mol Biosci*. PMID: 26734616
4. Hill et al. (2022). "USP5 enhances SGTA mediated protein quality control.". *PLoS One*. PMID: 35895711
5. Philp et al. (2013). "SGTA: a new player in the molecular co-chaperone game.". *Horm Cancer*. PMID: 23818240
**评价**: PubMed 81 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 313 aa |
| PDB 条数 | 5 |
| 已注释结构域 | 10 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SGTA/SGTA-PAE.png]]

**评价**: 5 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SGT |
| InterPro | SGTA_dimer |
| InterPro | TPR-like_helical_dom_sf |
| InterPro | TPR_rpt |
| Pfam | SGTA_dimer |
| Pfam | TPR_1 |
| Pfam | TPR_8 |
| SMART | TPR |
| PROSITE | TPR |
| PROSITE | TPR_REGION |

**染色质调控潜力分析**: 10 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:TRC complex (GO:0072380, IBA:GO_Central)
- F:BAT3 complex binding (GO:1904288, IPI:ParkinsonsUK-UCL)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 5 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 10 个 | 多库一致 |
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
1. 新颖性: PubMed 81 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 5 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SGTA
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104969-SGTA
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SGTA%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O43765
- STRING: https://string-db.org/network/9606.ENSG00000104969
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43765


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SGTA-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SGTA/SGTA-PAE.png]]




