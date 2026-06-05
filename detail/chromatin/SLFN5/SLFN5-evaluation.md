---
type: protein-evaluation
gene: "SLFN5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SLFN5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SLFN5 / MGC19764 |
| 蛋白全称 | Schlafen family member 5 |
| 蛋白大小 | 891 aa |
| UniProt ID | Q08AF3 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SLFN5/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SLFN5/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 8/10 | ×1 | **8** | 891 aa，尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 46 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: p-loop_ntpase, slfn_gtpase-like |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 7 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **110.5/183** | **110.0/183** |  |  |
|  | **归一化总分** |  | **60.4/100** | **60.1/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 891 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 46 |

**关键文献**:
1. Ding et al. (2024). "Integrated analysis of single-cell RNA-seq, bulk RNA-seq, Mendelian randomization, and eQTL reveals T cell-related nomogram model and subtype classification in rheumatoid arthritis.". *Front Immunol*. PMID: 38962008
2. Ding et al. (2023). "Schlafen-5 inhibits LINE-1 retrotransposition.". *iScience*. PMID: 37810251
3. Li et al. (2024). "Histone H4K12 lactylation promotes malignancy progression in triple-negative breast cancer through SLFN5 downregulation.". *Cell Signal*. PMID: 39395526
4. Huang et al. (2023). "SLFN5-mediated chromatin dynamics sculpt higher-order DNA repair topology.". *Mol Cell*. PMID: 36854302
5. Fan et al. (2024). "Schlafen5, regulated by the AP-1 family transcription factor c-Fos, affects diabetic wound healing through modulating PI3K/Akt/NRF2 axis.". *Int J Biol Macromol*. PMID: 39566766
**评价**: PubMed 46 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 891 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SLFN5/SLFN5-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | P-loop_NTPase |
| InterPro | Poxin-SLFN/SLFN_N |
| InterPro | Schlafen |
| InterPro | Schlafen_AlbA_2_dom |
| InterPro | Schlafen_AlbA_2_dom_sf |
| InterPro | SLFN_GTPase-like |
| Pfam | B3R |
| Pfam | SLFN_AlbA_2 |
| Pfam | SLFN_GTPase-like |

**染色质调控潜力分析**: 染色质/DNA 结构域: p-loop_ntpase, slfn_gtpase-like

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| CLLU1OS | 0 |  | no |
| SAMD10 | 0 |  | no |
| CCDC126 | 0 |  | no |
| ZNF880 | 0 |  | no |
| BPIFA3 | 0 |  | no |
| XRRA1 | 0 |  | no |
| METTL27 | 0 |  | no |

**已知复合体成员** (GO-CC):

--


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: STRING 7 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 9 个 | 多库一致 |
| PPI 网络 | STRING | 7 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 46 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLFN5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166750-SLFN5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SLFN5%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q08AF3
- STRING: https://string-db.org/network/9606.ENSG00000166750
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08AF3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SLFN5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SLFN5/SLFN5-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166750-SLFN5/subcellular

![](https://images.proteinatlas.org/17760/140_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/17760/140_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/17760/173_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/17760/173_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
