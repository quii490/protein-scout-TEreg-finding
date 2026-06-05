---
type: protein-evaluation
gene: "TBL3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBL3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TBL3 / SAZD|UTP13 |
| 蛋白全称 | Transducin beta-like protein 3 |
| 蛋白大小 | 808 aa |
| UniProt ID | Q12788 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TBL3/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TBL3/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 8/10 | ×1 | **8** | 808 aa，尚可接受 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 12 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 13 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **126.5/183** |  |
| **归一化总分** |  |  | **69.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 808 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 12 |

**评价**: PubMed 12 篇，极度新颖

**关键文献**:
1. Bao J et al. (2024). "A UTP3-dependent nucleolar translocation pathway facilitates pre-rRNA 5'ETS processing". *Nucleic Acids Res*. PMID: 39036955
2. Jimbo M et al. (2007). "Purification, cloning and characterization of egg lectins from the teleost Tribolodon brandti". *Comp Biochem Physiol B Biochem Mol Biol*. PMID: 17331772
3. Wada K et al. (2014). "Dynamics of WD-repeat containing proteins in SSU processome components". *Biochem Cell Biol*. PMID: 24754225
4. Hutchinson SA et al. (2012). "Tbl3 regulates cell cycle length during zebrafish development". *Dev Biol*. PMID: 22659140
5. Yuan Y et al. (2016). "TBL3 and TBL31, Two Arabidopsis DUF231 Domain Proteins, are Required for 3-O-Monoacetylation of Xylan". *Plant Cell Physiol*. PMID: 26556650
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 808 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 13 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TBL3/TBL3-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Quino_amine_DH_bsu |
| InterPro | Utp13_C |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | Utp13 |
| Pfam | WD40 |
| SMART | WD40 |
| PROSITE | WD_REPEATS_1 |
| PROSITE | WD_REPEATS_2 |
| PROSITE | WD_REPEATS_REGION |

**染色质调控潜力分析**: 13 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| APPBP2 | two hybrid pooling approach | 16189514 | — | — |
| SFN | two hybrid pooling approach | 16189514 | — | — |
| ITSN2 | two hybrid pooling approach | 16169070 | — | — |
| CACNB4 | two hybrid pooling approach | 16169070 | — | — |
| USP11 | two hybrid pooling approach | 16169070 | — | — |
| AURKB | two hybrid pooling approach | 16169070 | — | — |
| URM1 | two hybrid pooling approach | 16169070 | — | — |
| NUDC | luminescence based mammalian interactome mapping | 25036637 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 13 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 12 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TBL3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183751-TBL3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TBL3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q12788
- STRING: https://string-db.org/network/9606.ENSG00000183751
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12788


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TBL3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TBL3/TBL3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000183751-TBL3/subcellular

![](https://images.proteinatlas.org/42562/496_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/42562/496_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/42562/532_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/42562/532_G5_4_red_green.jpg)
![](https://images.proteinatlas.org/42562/547_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/42562/547_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
