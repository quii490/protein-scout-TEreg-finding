---
type: protein-evaluation
gene: "SGF29"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGF29 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SGF29 / FLJ32446|TDRD29 |
| 蛋白全称 | SAGA-associated factor 29 |
| 蛋白大小 | 293 aa |
| UniProt ID | Q96ES7 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SGF29/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SGF29/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 293 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 26 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 8 个 PDB 结构 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: sgf29_tudor, sgf29_tudor-like_dom, tudor_sgf29_rpt1, tudo |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **139/183** |  |
| **归一化总分** |  |  | **76.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IC|IDA|IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 293 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 26 |

**关键文献**:
1. Yan et al. (2023). "SGF29 nuclear condensates reinforce cellular aging.". *Cell Discov*. PMID: 37935676
2. Espinola-Lopez et al. (2021). "The Ada2/Ada3/Gcn5/Sgf29 histone acetyltransferase module.". *Biochim Biophys Acta Gene Regul Mech*. PMID: 32890768
3. Chan et al. (2024). "Therapeutic targeting Tudor domains in leukemia via CRISPR-Scan Assisted Drug Discovery.". *Sci Adv*. PMID: 38394203
4. Kurabe et al. (2015). "SGF29 and Sry pathway in hepatocarcinogenesis.". *World J Biol Chem*. PMID: 26322172
5. Murakami et al. (2014). "The male-specific factor Sry harbors an oncogenic function.". *Oncogene*. PMID: 23893245
**评价**: PubMed 26 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 293 aa |
| PDB 条数 | 8 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SGF29/SGF29-PAE.png]]

**评价**: 8 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SGF29 |
| InterPro | SGF29_tudor-like_dom |
| InterPro | Tudor_SGF29_rpt1 |
| InterPro | Tudor_SGF29_rpt2 |
| Pfam | SGF29_Tudor |
| PROSITE | SGF29_C |

**染色质调控潜力分析**: 染色质/DNA 结构域: sgf29_tudor, sgf29_tudor-like_dom, tudor_sgf29_rpt1, tudor_sgf29_rpt2

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:ATAC complex (GO:0140672, IDA:BHF-UCL)
- C:SAGA complex (GO:0000124, IBA:GO_Central)
- C:SAGA-type complex (GO:0070461, IDA:UniProtKB)
- P:establishment of protein localization to chromatin (GO:0071169, TAS:UniProtKB)
- P:transcription initiation-coupled chromatin remodeling (GO:0045815, IMP:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 8 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 26 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 8 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SGF29
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176476-SGF29
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SGF29%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96ES7
- STRING: https://string-db.org/network/9606.ENSG00000176476
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96ES7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SGF29-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SGF29/SGF29-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000176476-SGF29/subcellular

![](https://images.proteinatlas.org/52590/767_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/52590/767_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/52590/779_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/52590/779_C6_7_red_green.jpg)
![](https://images.proteinatlas.org/52590/865_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/52590/865_G4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
