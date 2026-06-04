---
type: protein-evaluation
gene: "PHC1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHC1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PHC1 / HPH1|RAE28 |
| 蛋白全称 | Polyhomeotic-like protein 1 |
| 蛋白大小 | 1004 aa |
| UniProt ID | P78364 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/PHC1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/PHC1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1004 aa，尚可接受 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 67 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: pcg_chromatin_remod_factors |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **111/183** | **110.0/183** |  |  |
|  | **归一化总分** |  | **60.7/100** | **60.1/100** |  |  |

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

**评价**: 1004 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 67 |

**关键文献**:
1. Park et al. (2023). "Plastisphere and microorganisms involved in polyurethane biodegradation.". *Sci Total Environ*. PMID: 37156380
2. Ong et al. (2023). "Acquisition of neural fate by combination of BMP blockade and chromatin modification.". *iScience*. PMID: 37771660
3. Teng et al. (2025). "Integrating bioinformatics and machine learning to discover sumoylation associated signatures in sepsis.". *Sci Rep*. PMID: 40274894
4. Kornya et al. (2023). "Investigation of Platelet Function Analyzer 200 platelet function measurements in healthy cats and cats receiving clopidogrel.". *J Vet Diagn Invest*. PMID: 37646490
5. Chen et al. (2021). "PHC1 maintains pluripotency by organizing genome-wide chromatin interactions of the Nanog locus.". *Nat Commun*. PMID: 33990559
**评价**: PubMed 67 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1004 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/PHC1/PHC1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PcG_chromatin_remod_factors |
| InterPro | SAM |
| InterPro | SAM/pointed_sf |
| InterPro | Znf_FCS |
| InterPro | Znf_FCS_sf |
| Pfam | PHC2_SAM_assoc |
| Pfam | SAM_1 |
| Pfam | zf-FCS_1 |
| SMART | SAM |
| PROSITE | SAM_DOMAIN |
| PROSITE | ZF_FCS |

**染色质调控潜力分析**: 染色质/DNA 结构域: pcg_chromatin_remod_factors

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:PcG protein complex (GO:0031519, IDA:UniProtKB)
- C:PRC1 complex (GO:0035102, IDA:UniProtKB)
- C:sex chromatin (GO:0001739, IEA:Ensembl)
- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IMP:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 11 个 | 多库一致 |
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
1. 新颖性: PubMed 67 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PHC1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111752-PHC1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PHC1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P78364
- STRING: https://string-db.org/network/9606.ENSG00000111752
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78364


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PHC1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/PHC1/PHC1-PAE.png]]




