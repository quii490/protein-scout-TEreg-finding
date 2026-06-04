---
type: protein-evaluation
gene: "YEATS2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YEATS2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | YEATS2 / FLJ10201|FLJ12841|FLJ13308|KIAA1197 |
| 蛋白全称 | YEATS domain-containing protein 2 |
| 蛋白大小 | 1422 aa |
| UniProt ID | Q9ULM3 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 5/10 | ×1 | **5** | 1422 aa, small/large |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 54 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 7 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **112/183** |  |
| **归一化总分** |  |  | **61.2/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS2/IF_images/GAMG_HPA036741_1.jpg|GAMG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS2/IF_images/PODO_TERT256_HPA036741_2.jpg|PODO/TERT256]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1422 aa， small/large

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 54 |

**评价**: PubMed 54 篇，中等研究热度

**关键文献**:
1. Ji K et al. (2025). "YEATS2: a novel cancer epigenetic reader and potential therapeutic target". *Cancer Cell Int*. PMID: 40287757
2. Yan S et al. (2025). "SUMOylation targets O-GlcNAcase to chaperone-mediated autophagy". *J Biol Chem*. PMID: 40449592
3. Zhao J et al. (2025). "YEATS2 O-GlcNAcylation promotes chromatin association of the ATAC complex and lung cancer tumorigenesis". *J Biol Chem*. PMID: 40541806
4. Erb MA (2023). "Small-molecule tools for YEATS domain proteins". *Curr Opin Chem Biol*. PMID: 37924571
5. Corbett MA et al. (2023). "Genetics of familial adult myoclonus epilepsy: From linkage studies to noncoding repeat expansions". *Epilepsia*. PMID: 37021642
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1422 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS2/YEATS2-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | YEAST_sf |
| InterPro | YEATS |
| InterPro | YEATS2_3HBD |
| InterPro | YEATS_dom |
| Pfam | 3HBD |
| Pfam | YEATS |
| PROSITE | YEATS |

**染色质调控潜力分析**: 7 个已注释结构域，新颖蛋白基线水平

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
- C:NuA4 histone acetyltransferase complex (GO:0035267, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
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
1. 新颖性: PubMed 54 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=YEATS2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163872-YEATS2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22YEATS2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9ULM3
- STRING: https://string-db.org/network/9606.ENSG00000163872
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULM3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[YEATS2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/YEATS2/YEATS2-PAE.png]]




