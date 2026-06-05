---
type: protein-evaluation
gene: "WBP4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WBP4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | WBP4 / FBP21|MGC117310 |
| 蛋白全称 | WW domain-binding protein 4 |
| 蛋白大小 | 376 aa |
| UniProt ID | O75554 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 376 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 25 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 11 个 PDB 结构 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: matrin/u1-c_znf_c2h2, matrin/u1-like-c_znf_c2h2, u1-cz_zn |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **139/183** |  |
| **归一化总分** |  |  | **76.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Nucleus speckle | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WBP4/IF_images/A-431_HPA038965_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WBP4/IF_images/U-251MG_HPA038965_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 376 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 25 |

**评价**: PubMed 25 篇，高度新颖

**关键文献**:
1. Engal E et al. (2024). "The spectrum of pre-mRNA splicing in autism". *Wiley Interdiscip Rev RNA*. PMID: 38509732
2. Du X et al. (2023). "Synthesis of Cationic Biphen[4, 5]arenes as Biofilm Disruptors". *Angew Chem Int Ed Engl*. PMID: 36929684
3. Rovito D et al. (2020). "Cytosolic sequestration of the vitamin D receptor as a therapeutic option for vitamin D-induced hypercalcemia". *Nat Commun*. PMID: 33288743
4. Xing Q et al. (2021). "A novel 13 RNA binding proteins (RBPs) signature could predict prostate cancer biochemical recurrence". *Pathol Res Pract*. PMID: 34419719
5. Engal E et al. (2023). "Bi-allelic loss-of-function variants in WBP4, encoding a spliceosome protein, result in a variable neurodevelopmental syndrome". *Am J Hum Genet*. PMID: 37963460
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 376 aa |
| PDB 条数 | 11 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WBP4/WBP4-PAE.png]]

**评价**: 11 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Matrin/U1-C_Znf_C2H2 |
| InterPro | Matrin/U1-like-C_Znf_C2H2 |
| InterPro | U1-CZ_Znf_C2H2 |
| InterPro | WBP4 |
| InterPro | WW_dom |
| InterPro | WW_dom_sf |
| InterPro | Znf_C2H2_sf |
| Pfam | WW |
| Pfam | zf-U1 |
| SMART | WW |
| SMART | ZnF_U1 |
| PROSITE | WW_DOMAIN_1 |
| PROSITE | WW_DOMAIN_2 |
| PROSITE | ZF_MATRIN |

**染色质调控潜力分析**: 染色质/DNA 结构域: matrin/u1-c_znf_c2h2, matrin/u1-like-c_znf_c2h2, u1-cz_znf_c2h2, znf_c2h2_sf

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
| 三维结构 | AlphaFold + PDB | 11 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
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
1. 新颖性: PubMed 25 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 11 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=WBP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120688-WBP4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22WBP4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O75554
- STRING: https://string-db.org/network/9606.ENSG00000120688
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75554


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[WBP4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WBP4/WBP4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000120688-WBP4/subcellular

![](https://images.proteinatlas.org/38965/435_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/38965/435_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/38965/445_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/38965/445_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/38965/448_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/38965/448_D6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
