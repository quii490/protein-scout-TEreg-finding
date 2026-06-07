---
type: protein-evaluation
gene: "NFRKB"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NFRKB 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NFRKB / DKFZp547B2013|INO80G |
| 蛋白名称 | Nuclear factor related to kappa-B-binding protein |
| 蛋白大小 | 1299 aa |
| UniProt ID | Q6P4R8 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 5/10 | ×1 | **5** | 1299 aa，偏小或偏大 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 23篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 8 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **128/183** |  |
| **归一化总分** |  |  | **69.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | IF image available (embedded below) | See IF_images/ |
| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFRKB/IF_images/A-431_HPA007082_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFRKB/IF_images/U-251MG_HPA007082_2.jpg|U-251MG]]

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 1299 aa，1299 aa，偏小或偏大。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 23 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 3.6558 |

**评价**: PubMed 23篇，非常新颖

**关键文献**:
1. Peng Q et al. (2022). "The biological function of metazoan-specific subunit nuclear factor related to kappaB binding protein of INO80 complex". *Int J Biol Macromol*. PMID: 35093437
2. Vander Linden RT et al. (2015). "Structural basis for the activation and inhibition of the UCH37 deubiquitylase". *Mol Cell*. PMID: 25702872
3. Grygalewicz B et al. (2025). "Cytogenomic and Clinicopathologic Comparison of MYC-Positive and MYC-Negative High-Grade B-Cell Lymphoma With 11q Aberration in the Context of Other Aggressive Lymphomas With MYC Rearrangement". *Mod Pathol*. PMID: 40222649
4. Audard V et al. (2012). "Upregulation of nuclear factor-related kappa B suggests a disorder of transcriptional regulation in minimal change nephrotic syndrome". *PLoS One*. PMID: 22291976
5. Kumar A et al. (2012). "Structure of a novel winged-helix like domain from human NFRKB protein". *PLoS One*. PMID: 22984442
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1299 aa |
| PDB 条目数 | 4 |
| UniProt 注释结构域数 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFRKB/NFRKB-PAE.png]]

**评价**: 4 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | DEUBAD_dom |
| InterPro | NFRKB |
| InterPro | NFRKB_WH_1 |
| InterPro | NFRKB_WH_2 |
| InterPro | NFRKB_winged_sf |
| Pfam | WHD_1st_NFRKB |
| Pfam | WHD_2nd_NFRKB |
| PROSITE | DEUBAD |

**染色质调控潜力分析**: 8 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| INO80E | 0 |  | 否 |
| ACTR5 | 0 |  | 否 |
| UCHL5 | 0 |  | 否 |
| INO80 | 0 |  | 否 |
| ACTR8 | 0 |  | 否 |
| RUVBL1 | 0 |  | 否 |
| TFPT | 0 |  | 是 |
| YY1 | 0 |  | 否 |
| RUVBL2 | 0 |  | 否 |
| MCRS1 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- C:Ino80 complex (GO:0031011, IDA:UniProtKB)
- P:chromatin remodeling (GO:0006338, IDA:ComplexPortal)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 8 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 23 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 无 HPA IF 实验数据
2. 4 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NFRKB
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170322-NFRKB
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NFRKB%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6P4R8
- STRING: https://string-db.org/network/9606.ENSG00000170322
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P4R8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NFRKB-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NFRKB/NFRKB-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P4R8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 39..156; /note="DEUBAD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01264" |
| InterPro | IPR044867;IPR024867;IPR025220;IPR057748;IPR038106; |
| Pfam | PF14465;PF25793; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170322-NFRKB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| INO80 | Biogrid, Opencell | true |
| RUVBL1 | Biogrid, Opencell | true |
| RUVBL2 | Biogrid, Opencell | true |
| UCHL5 | Intact, Biogrid | true |
| YY1 | Biogrid, Opencell | true |
| ACTR5 | Biogrid | false |
| ACTR8 | Biogrid | false |
| BRD3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
