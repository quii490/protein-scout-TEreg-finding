---
type: protein-evaluation
gene: "VRTN"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VRTN 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | VRTN / FLJ10811|vertnin |
| 蛋白全称 | Vertnin |
| 蛋白大小 | 702 aa |
| UniProt ID | Q9H8Y1 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 702 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 12 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | UniProt + GO 核定位互证 (+1) |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VRTN/IF_images/CACO-2_HPA001460_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VRTN/IF_images/U-251MG_HPA001460_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 702 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |

**评价**: PubMed 12 篇，极度新颖

**关键文献**:
1. Duan Y et al. (2018). "VRTN is Required for the Development of Thoracic Vertebrae in Mammals". *Int J Biol Sci*. PMID: 29904281
2. Yang J et al. (2016). "Possible introgression of the VRTN mutation increasing vertebral number, carcass length and teat number from Chinese pigs into European pigs". *Sci Rep*. PMID: 26781738
3. Li C et al. (2019). "Whole-Genome Resequencing Reveals Loci Associated With Thoracic Vertebrae Number in Sheep". *Front Genet*. PMID: 31379930
4. Hirose K et al. (2013). "Association of swine vertnin (VRTN) gene with production traits in Duroc pigs improved using a closed nucleus breeding system". *Anim Sci J*. PMID: 23480701
5. Mikawa S et al. (2011). "Identification of a second gene associated with variation in vertebral number in domestic pigs". *BMC Genet*. PMID: 21232157
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 702 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VRTN/VRTN-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Trp_repressor/repl_initiator |
| InterPro | Vertnin-like |
| InterPro | VRTN_OTU_dom |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 12 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=VRTN
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133980-VRTN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22VRTN%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H8Y1
- STRING: https://string-db.org/network/9606.ENSG00000133980
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H8Y1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[VRTN-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/VRTN/VRTN-PAE.png]]




