---
type: protein-evaluation
gene: "PWP2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PWP2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PWP2 / EHOC-17|UTP1 |
| 蛋白全称 | Periodic tryptophan protein 2 homolog |
| 蛋白大小 | 919 aa |
| UniProt ID | Q15269 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 8/10 | ×1 | **8** | 919 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 22 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 13 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **116.5/183** |  |
| **归一化总分** |  |  | **63.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 919 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 22 |

**关键文献**:
1. Wada et al. (2014). "Dynamics of WD-repeat containing proteins in SSU processome components.". *Biochem Cell Biol*. PMID: 24754225
2. Boissier et al. (2017). "Pwp2 mediates UTP-B assembly via two structurally independent domains.". *Sci Rep*. PMID: 28600509
3. Dosil et al. (2004). "Functional characterization of Pwp2, a WD family protein essential for the assembly of the 90 S pre-ribosomal particle.". *J Biol Chem*. PMID: 15231838
4. Nagamine et al. (1997). "Genomic organization and complete nucleotide sequence of the human PWP2 gene on chromosome 21.". *Genomics*. PMID: 9205129
5. Shafaatian et al. (1996). "PWP2, a member of the WD-repeat family of proteins, is an essential Saccharomyces cerevisiae gene involved in cell separation.". *Mol Gen Genet*. PMID: 8804409
**评价**: PubMed 22 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 919 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 13 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP2/PWP2-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PWP2 |
| InterPro | Quinoprotein_ADH-like_sf |
| InterPro | SSU_processome_Utp12 |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_rpt |
| Pfam | Utp12 |
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
| HSP82 | affinity chromatography technology | 15766533 | — | — |
| BFR2 | inferred by author | 16429126 | — | — |
| BMS1 | inferred by author | 16429126 | — | — |
| BEM2 | inferred by author | 16429126 | — | — |
| TOM1L1 | two hybrid pooling approach | 16169070 | — | — |
| yhs2_yeast | two hybrid array | 14690591 | — | — |
| CMS1 | inferred by author | 16429126 | — | — |
| UTP21 | two hybrid array | 29054886 | — | — |
| DIP2 | two hybrid array | 29054886 | — | — |
| SAS10 | two hybrid array | 29054886 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:Pwp2p-containing subcomplex of 90S preribosome (GO:0034388, IBA:GO_Central)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
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
1. 新颖性: PubMed 22 篇，高度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PWP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000241945-PWP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PWP2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q15269
- STRING: https://string-db.org/network/9606.ENSG00000241945
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15269


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PWP2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP2/PWP2-PAE.png]]




