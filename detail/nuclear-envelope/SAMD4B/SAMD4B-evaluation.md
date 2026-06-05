---
type: protein-evaluation
gene: "SAMD4B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SAMD4B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SAMD4B / FLJ10211|MGC99832|SMGB|hSmaug2 |
| 蛋白全称 | Protein Smaug homolog 2 |
| 蛋白大小 | 694 aa |
| UniProt ID | Q5PRF9 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMD4B/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMD4B/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 694 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 17 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 9 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **114.5/183** |  |
| **归一化总分** |  |  | **62.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 694 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |

**关键文献**:
1. Chen et al. (2025). "BAG2 releases SAMD4B upon sensing of arginine deficiency to promote tumor cell survival.". *Mol Cell*. PMID: 40555234
2. Qi et al. (2024). "Synergistic immunochemotherapy targeted SAMD4B-APOA2-PD-L1 axis potentiates antitumor immunity in hepatocellular carcinoma.". *Cell Death Dis*. PMID: 38886351
3. Fernández-Alvarez et al. (2016). "Smaug variants in neural and non-neuronal cells.". *Commun Integr Biol*. PMID: 27195061
4. Jackson et al. (2025). "Cellular metabolite sensors: Arginine? It's in the bag!". *Mol Cell*. PMID: 40614704
5. Wang et al. (2023). "RNA binding protein SAMD4: current knowledge and future perspectives.". *Cell Biosci*. PMID: 36732864
**评价**: PubMed 17 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 694 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMD4B/SAMD4B-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PHAT_dom_sf |
| InterPro | PHAT_Smg/ZCCHC2-like |
| InterPro | SAM |
| InterPro | SAM/pointed_sf |
| InterPro | SMAUG/VTS1_RNA-bind |
| InterPro | Smaug_SAM |
| Pfam | PHAT_SMAUG |
| Pfam | SAM_1 |
| SMART | SAM |

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
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 9 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 17 篇，极度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAMD4B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179134-SAMD4B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SAMD4B%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q5PRF9
- STRING: https://string-db.org/network/9606.ENSG00000179134
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5PRF9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SAMD4B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/SAMD4B/SAMD4B-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (enhanced)。来源: https://www.proteinatlas.org/ENSG00000179134-SAMD4B/subcellular

![](https://images.proteinatlas.org/16800/131_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16800/131_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16800/132_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16800/132_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/16800/164_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/16800/164_F11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
