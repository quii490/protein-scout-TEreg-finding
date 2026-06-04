---
type: protein-evaluation
gene: "POU5F2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POU5F2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | POU5F2 / SPRM-1|FLJ25680 |
| 蛋白全称 | POU domain, class 5, transcription factor 2 |
| 蛋白大小 | 328 aa |
| UniProt ID | Q8N7G0 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/POU5F2/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 328 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 3 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeobox_2, homeodomain, homeodomain-like_sf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

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

**评价**: 328 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 3 |

**关键文献**:
1. Mastroberardino et al. (1998). "Amino-acid transport by heterodimers of 4F2hc/CD98 and members of a permease family.". *Nature*. PMID: 9751058
2. Krautz-Peterson et al. (2007). "Amino acid transport in schistosomes: Characterization of the permeaseheavy chain SPRM1hc.". *J Biol Chem*. PMID: 17545149
3. Pfeiffer et al. (1998). "Functional heterodimeric amino acid transporters lacking cysteine residues involved in disulfide bond.". *FEBS Lett*. PMID: 9849898
4. Xia et al. (1993). "Chromosomal organization of mammalian POU domain factors.". *Genomics*. PMID: 8276396
5. Zini et al. (1996). "POU-domain gene expression during spermatogenesis.". *World J Urol*. PMID: 8912467
**评价**: PubMed 3 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 328 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/POU5F2/POU5F2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HD |
| InterPro | Homeodomain-like_sf |
| InterPro | Lambda_DNA-bd_dom_sf |
| InterPro | POU |
| InterPro | POU_dom |
| InterPro | POU_domain_TF |
| Pfam | Homeodomain |
| Pfam | Pou |
| SMART | HOX |
| SMART | POU |
| PROSITE | HOMEOBOX_2 |
| PROSITE | POU_1 |
| PROSITE | POU_2 |
| PROSITE | POU_3 |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeobox_2, homeodomain, homeodomain-like_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, ISA:NTNU_SB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 3 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=POU5F2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000248483-POU5F2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22POU5F2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8N7G0
- STRING: https://string-db.org/network/9606.ENSG00000248483
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7G0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[POU5F2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/POU5F2/POU5F2-PAE.png]]




