---
type: protein-evaluation
gene: "TCF23"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCF23 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TCF23 / OUT|bHLHa24 |
| 蛋白全称 | Transcription factor 23 |
| 蛋白大小 | 214 aa |
| UniProt ID | Q7RTU1 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 214 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 5 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: bhlh, bhlh_dom, hlh, hlh_dna-bd_sf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TCF23/IF_images/THP-1_HPA044596_1.jpg|THP-1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TCF23/IF_images/U-251MG_HPA044596_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 214 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 5 |

**评价**: PubMed 5 篇，极度新颖

**关键文献**:
1. Minisy FM et al. (2024). "Transcription Factor 23 is an Essential Determinant of Murine Term Parturition". *Mol Cell Biol*. PMID: 39014976
2. Seekford ZK et al. (2026). "Induced uterine infection alters bovine endometrial function and embryonic competence". *Reproduction*. PMID: 41575562
3. Kommagani R et al. (2014). "A murine uterine transcriptome, responsive to steroid receptor coactivator-2, reveals transcription factor 23 as essential for decidualization of human endometrial stromal cells". *Biol Reprod*. PMID: 24571987
4. Tachibana M et al. (2001). "Genomic organization and chromosomal mapping of the basic helix-loop-helix factor OUT (Tcf23/TCF23)". *Cytogenet Cell Genet*. PMID: 11701948
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 214 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TCF23/TCF23-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | bHLH_dom |
| InterPro | E-box_TF_Regulators |
| InterPro | HLH_DNA-bd_sf |
| Pfam | HLH |
| SMART | HLH |
| PROSITE | BHLH |

**染色质调控潜力分析**: 染色质/DNA 结构域: bhlh, bhlh_dom, hlh, hlh_dna-bd_sf

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
- C:euchromatin (GO:0000791, ISS:ARUK-UCL)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 5 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TCF23
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163792-TCF23
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TCF23%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q7RTU1
- STRING: https://string-db.org/network/9606.ENSG00000163792
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTU1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TCF23-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TCF23/TCF23-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000163792-TCF23/subcellular

![](https://images.proteinatlas.org/44596/1855_G6_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/44596/1855_G6_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/44596/518_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44596/518_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44596/530_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44596/530_F5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7RTU1 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 76..128; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050283;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163792-TCF23/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EMD | Intact | false |
| FIGLA | Intact | false |
| TCF12 | Biogrid | false |
| TCF4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
