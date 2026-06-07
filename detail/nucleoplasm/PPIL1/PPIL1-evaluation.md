---
type: protein-evaluation
gene: "PPIL1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPIL1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPIL1 / CYPL1 |
| 蛋白全称 | Peptidyl-prolyl cis-trans isomerase-like 1 |
| 蛋白大小 | 166 aa |
| UniProt ID | Q9Y3C6 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 166 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 28 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL1/IF_images/SK-MEL-30_HPA062916_1.jpg|SK-MEL-30]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL1/IF_images/U2OS_HPA062916_2.jpg|U2OS]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 166 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |

**评价**: PubMed 28 篇，高度新颖

**关键文献**:
1. Rajiv C & Davis TL (2018). "Structural and Functional Insights into Human Nuclear Cyclophilins". *Biomolecules*. PMID: 30518120
2. Janneh AH et al. (2022). "Crosstalk between pro-survival sphingolipid metabolism and complement signaling induces inflammasome-mediated tumor metastasis". *Cell Rep*. PMID: 36476873
3. Obama K et al. (2006). "Overexpression of peptidyl-prolyl isomerase-like 1 is associated with the growth of colon cancer cells". *Clin Cancer Res*. PMID: 16397026
4. Paul S et al. (2021). "Splicing Control of Pontocerebellar Development". *Neuron*. PMID: 33476558
5. Wu J et al. (2025). "PPIL1 Drives Hepatocellular Carcinoma Progression and Cancer Stem Cell Self-renewal Through DAAM2-mediated Wnt/β-Catenin Activation". *Cancer Genomics Proteomics*. PMID: 40883023
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 166 aa |
| PDB 条数 | 28 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL1/PPIL1-PAE.png]]

**评价**: 28 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Cyclophilin-like_dom_sf |
| InterPro | Cyclophilin-type_PPIase |
| InterPro | Cyclophilin-type_PPIase_CS |
| InterPro | Cyclophilin-type_PPIase_dom |
| InterPro | Cyclophilin_A-like |
| Pfam | Pro_isomerase |
| PROSITE | CSA_PPIASE_1 |
| PROSITE | CSA_PPIASE_2 |

**染色质调控潜力分析**: 8 个已注释结构域，新颖蛋白基线水平

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

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 28 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
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
1. 新颖性: PubMed 28 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 28 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPIL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137168-PPIL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPIL1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y3C6
- STRING: https://string-db.org/network/9606.ENSG00000137168
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3C6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPIL1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL1/PPIL1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000137168-PPIL1/subcellular

![](https://images.proteinatlas.org/62916/1262_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62916/1262_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62916/1264_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62916/1264_G7_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3C6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 10..164; /note="PPIase cyclophilin-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00156" |
| InterPro | IPR029000;IPR024936;IPR020892;IPR002130;IPR044666; |
| Pfam | PF00160; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137168-PPIL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC5L | Biogrid, Bioplex | true |
| CPSF6 | Intact, Biogrid, Opencell | true |
| RBM39 | Biogrid, Opencell | true |
| SNW1 | Intact, Biogrid, Bioplex | true |
| WDR83 | Intact, Biogrid, Bioplex | true |
| AQR | Intact, Bioplex | false |
| BCAS2 | Bioplex | false |
| BUD31 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
