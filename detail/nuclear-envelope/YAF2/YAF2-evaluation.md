---
type: protein-evaluation
gene: "YAF2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YAF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | YAF2 / -- |
| 蛋白全称 | YY1-associated factor 2 |
| 蛋白大小 | 180 aa |
| UniProt ID | Q8IY57 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/YAF2/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/YAF2/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 180 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 35 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 9 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **125/183** |  |
| **归一化总分** |  |  | **68.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA|IMP |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 180 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 35 |

**关键文献**:
1. Liu et al. (2023). "Functional dissection of PRC1 subunits RYBP and YAF2 during neural differentiation of embryonic stem cells.". *Nat Commun*. PMID: 37935677
2. Kalenik et al. (1997). "Yeast two-hybrid cloning of a novel zinc finger protein that interacts with the multifunctional transcription factor YY1.". *Nucleic Acids Res*. PMID: 9016636
3. Park et al. (2015). "YAF2 promotes TP53-mediated genotoxic stress response via stabilization of PDCD5.". *Biochim Biophys Acta*. PMID: 25603536
4. Mädge et al. (2003). "Yaf2 inhibits Myc biological function.". *Cancer Lett*. PMID: 12706874
5. Li et al. (2016). "Cellular functions of programmed cell death 5.". *Biochim Biophys Acta*. PMID: 26775586
**评价**: PubMed 35 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 180 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/YAF2/YAF2-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | RYBP/YAF2 |
| InterPro | YAF2_RYBP |
| InterPro | Znf_RanBP2 |
| InterPro | Znf_RanBP2_sf |
| Pfam | YAF2_RYBP |
| Pfam | Zn_ribbon_RanBP |
| SMART | ZnF_RBZ |
| PROSITE | ZF_RANBP2_1 |
| PROSITE | ZF_RANBP2_2 |

**染色质调控潜力分析**: 9 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 9 个 | 多库一致 |
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
1. 新颖性: PubMed 35 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=YAF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000015153-YAF2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22YAF2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8IY57
- STRING: https://string-db.org/network/9606.ENSG00000015153
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY57


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[YAF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/YAF2/YAF2-PAE.png]]




