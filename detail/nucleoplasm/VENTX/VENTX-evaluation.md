---
type: protein-evaluation
gene: "VENTX"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VENTX 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | VENTX / HPX42B |
| 蛋白全称 | Homeobox protein VENTX |
| 蛋白大小 | 258 aa |
| UniProt ID | O95231 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 258 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeobox_1, homeobox_2, homeobox_cs, homeobox_tf, homeodo |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VENTX/IF_images/CACO-2_HPA050955_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VENTX/IF_images/SuSa_HPA050955_2.jpg|SuSa]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 258 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |

**评价**: PubMed 28 篇，高度新颖

**关键文献**:
1. Long Z et al. (2022). "Single-cell multiomics analysis reveals regulatory programs in clear cell renal cell carcinoma". *Cell Discov*. PMID: 35853872
2. Kumar S et al. (2022). "Ventx Family and Its Functional Similarities with Nanog: Involvement in Embryonic Development and Cancer Progression". *Int J Mol Sci*. PMID: 35269883
3. Ducos B et al. (2022). "Vertebrate Cell Differentiation, Evolution, and Diseases: The Vertebrate-Specific Developmental Potential Guardians VENTX/NANOG and POU5/OCT4 Enter the Stage". *Cells*. PMID: 35892595
4. Le Y et al. (2018). "The homeobox protein VentX reverts immune suppression in the tumor microenvironment". *Nat Commun*. PMID: 29872044
5. Wu X et al. (2011). "VentX trans-activates p53 and p16ink4a to regulate cellular senescence". *J Biol Chem*. PMID: 21325273
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 258 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VENTX/VENTX-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HD |
| InterPro | Homeobox_CS |
| InterPro | Homeobox_TF |
| InterPro | Homeodomain-like_sf |
| Pfam | Homeodomain |
| SMART | HOX |
| PROSITE | HOMEOBOX_1 |
| PROSITE | HOMEOBOX_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeobox_1, homeobox_2, homeobox_cs, homeobox_tf, homeodomain

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

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 28 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=VENTX
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151650-VENTX
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22VENTX%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O95231
- STRING: https://string-db.org/network/9606.ENSG00000151650
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95231


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[VENTX-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VENTX/VENTX-PAE.png]]




