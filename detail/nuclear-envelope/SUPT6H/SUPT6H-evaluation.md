---
type: protein-evaluation
gene: "SUPT6H"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT6H 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SUPT6H / KIAA0162|SPT6H |
| 蛋白全称 | Transcription elongation factor SPT6 |
| 蛋白大小 | 1726 aa |
| UniProt ID | Q7KZ85 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SUPT6H/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SUPT6H/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 5/10 | ×1 | **5** | 1726 aa, small/large |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 18 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 34 个已注释结构域 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **134/183** |  |
| **归一化总分** |  |  | **73.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1726 aa， small/large

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 22 |

**关键文献**:
1. Xu et al. (2023). "MiR-423-5p Inhibition Exerts Protective Effects on Angiotensin II-Induced Cardiomyocyte Hypertrophy.". *Tohoku J Exp Med*. PMID: 36517015
2. Lin et al. (2026). "A Novel Platinum-Resistance-related Gene Signature in Ovarian Cancer: Identification and Patient-derived Organoids Verification.". *Curr Cancer Drug Targets*. PMID: 39901543
3. Thavarajah et al. (2020). "The plasma peptides of sepsis.". *Clin Proteomics*. PMID: 32636717
4. Chen et al. (2022). "S100A10 and its binding partners in depression and antidepressant actions.". *Front Mol Neurosci*. PMID: 36046712
5. Chiang et al. (1996). "Isolation, sequencing, and mapping of the human homologue of the yeast transcription factor, SPT5.". *Genomics*. PMID: 8975720
**评价**: PubMed 22 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1726 aa |
| PDB 条数 | 18 |
| 已注释结构域 | 34 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SUPT6H/SUPT6H-PAE.png]]

**评价**: 18 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HHH_9 |
| InterPro | NA-bd_OB-fold |
| InterPro | RNaseH-like_sf |
| InterPro | RuvA_2-like |
| InterPro | S1_domain |
| InterPro | SH2 |
| InterPro | SH2_dom_sf |
| InterPro | Spt6_acidic_N_dom |
| InterPro | Spt6_death-like |
| InterPro | Spt6_HHH |
| InterPro | Spt6_HTH_DNA-bd_dom |
| InterPro | Spt6_SH2 |
| InterPro | Spt6_SH2_C |
| InterPro | Spt6_SH2_N |
| InterPro | Spt6_YqgF |

**染色质调控潜力分析**: 34 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| SUPT4H1 | 0 |  | no |
| IWS1 | 0 |  | no |
| POLR2A | 0 |  | no |
| SUPT5H | 0 |  | no |
| SUPT16H | 0 |  | no |
| TCEA1 | 0 |  | no |
| CTR9 | 0 |  | no |
| SSRP1 | 0 |  | no |
| POLR2C | 0 |  | no |
| RTF1 | 0 |  | yes |

**已知复合体成员** (GO-CC):

- C:transcription elongation factor complex (GO:0008023, IBA:GO_Central)
- F:nucleosome binding (GO:0031491, IBA:GO_Central)
- P:nucleosome organization (GO:0034728, IBA:GO_Central)
- P:transcription elongation-coupled chromatin remodeling (GO:0140673, IMP:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 18 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 34 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 22 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 18 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SUPT6H
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109111-SUPT6H
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SUPT6H%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q7KZ85
- STRING: https://string-db.org/network/9606.ENSG00000109111
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7KZ85


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SUPT6H-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SUPT6H/SUPT6H-PAE.png]]




