---
type: protein-evaluation
gene: "YEATS4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YEATS4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | YEATS4 / NuBI-1|GAS41|YAF9 |
| 蛋白全称 | YEATS domain-containing protein 4 |
| 蛋白大小 | 227 aa |
| UniProt ID | O95619 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 227 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 45 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 16 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 5 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **123/183** | **122.0/183** |  |  |  |
|  | **归一化总分** |  | **67.2/100** | **66.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS4/IF_images/RT-4_HPA072532_1.jpg|RT-4]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS4/IF_images/U2OS_HPA072532_2.jpg|U2OS]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 227 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 45 |

**评价**: PubMed 45 篇，高度新颖

**关键文献**:
1. Xie M et al. (2024). "Targeting the KAT8/YEATS4 Axis Represses Tumor Growth and Increases Cisplatin Sensitivity in Bladder Cancer". *Adv Sci (Weinh)*. PMID: 38526153
2. Peng Z et al. (2025). "YEATS4 reads histone crotonylation to promote fatty acid metabolism and cancer cell stemness". *Cell Rep*. PMID: 41060805
3. Berta DG et al. (2021). "Deficient H2A.Z deposition is associated with genesis of uterine leiomyoma". *Nature*. PMID: 34349258
4. Xian Q et al. (2023). "Mechanistic insights into genomic structure and functions of a novel oncogene YEATS4". *Front Cell Dev Biol*. PMID: 37435030
5. Conil C et al. (2025). "A human YEATS4 variant confers resistance to TST and IGRA conversion despite Mycobacterium tuberculosis exposure". *Genome Med*. PMID: 41094526
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 227 aa |
| PDB 条数 | 16 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS4/YEATS4-PAE.png]]

**评价**: 16 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | YEAST_sf |
| InterPro | YEATS |
| InterPro | YEATS_dom |
| Pfam | YEATS |
| PROSITE | YEATS |

**染色质调控潜力分析**: 5 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:NuA4 histone acetyltransferase complex (GO:0035267, IDA:UniProtKB)
- C:nucleosome (GO:0000786, IDA:ComplexPortal)
- P:chromatin remodeling (GO:0006338, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 16 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
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
1. 新颖性: PubMed 45 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 16 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=YEATS4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127337-YEATS4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22YEATS4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O95619
- STRING: https://string-db.org/network/9606.ENSG00000127337
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95619


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[YEATS4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS4/YEATS4-PAE.png]]




