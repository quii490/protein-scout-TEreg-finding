---
type: protein-evaluation
gene: "NANOGP8"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NANOGP8 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NANOGP8 / — |
| 蛋白名称 | Homeobox protein NANOGP8 |
| 蛋白大小 | 305 aa |
| UniProt ID | Q6NSW7 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NANOGP8/IF_images/SuSa_1.jpg|SuSa]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NANOGP8/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 305 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42篇，非常新颖 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | 明确染色质/DNA 调控结构域: distal-less_homeobox_tf, homeobox_1, homeobox_2, homeobox_cs, h |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 13 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 结构域: 多库注释一致 (+0.5) |
|  | **原始总分** |  | **123/183** | **122.0/183** |  |
|  | **归一化总分** |  | **67.2/100** | **66.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 305 aa，305 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 1.505 |

**关键文献**:
1. Vaidya et al. (2023). "Analysis of regulatory sequences in exosomal DNA of NANOGP8.". *PLoS One*. PMID: 36696426
2. Zhang et al. (2013). "NANOG modulates stemness in human colorectal cancer.". *Oncogene*. PMID: 23085761
3. Mikulenkova et al. (2020). "NANOG/NANOGP8 Localizes at the Centrosome and is Spatiotemporally Associated with Centriole Maturation.". *Cells*. PMID: 32168958
4. Fairbanks et al. (2012). "NANOGP8: evolution of a human-specific retro-oncogene.". *G3 (Bethesda)*. PMID: 23173096
5. Ma et al. (2018). "NANOGP8 is the key regulator of stemness, EMT, Wnt pathway, chemoresistance, and other malignant phenotypes in gastric cancer cells.". *PLoS One*. PMID: 29689047
**评价**: PubMed 42篇，非常新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 305 aa |
| PDB 条目数 | 0 |
| UniProt 注释结构域数 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NANOGP8/NANOGP8-PAE.png]]

**评价**: 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Distal-less_Homeobox_TF |
| InterPro | HD |
| InterPro | Homeobox_CS |
| InterPro | Homeodomain-like_sf |
| Pfam | Homeodomain |
| SMART | HOX |
| PROSITE | HOMEOBOX_1 |
| PROSITE | HOMEOBOX_2 |

**染色质调控潜力分析**: 明确染色质/DNA 调控结构域: distal-less_homeobox_tf, homeobox_1, homeobox_2, homeobox_cs, homeodomain

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NANOG | 0 |  | 否 |
| CD44 | 0 |  | 否 |
| STAT3 | 0 |  | 否 |
| DDX5 | 0 |  | 否 |
| DROSHA | 0 |  | 否 |
| POU5F1B | 0 |  | 否 |
| POU5F1 | 0 |  | 否 |
| SCN11A | 0 |  | 否 |
| SCN8A | 0 |  | 否 |
| SCN10A | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 13 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 entries | 仅预测 |
| 结构域 | UniProt / InterPro / Pfam | 8 domains | 多库一致 |
| PPI | STRING + IntAct | 13 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
结构域: 多库注释一致 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 42 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 无 PDB 实验结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: AlphaFold 预测为基础，设计突变实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NANOGP8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000255192-NANOGP8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NANOGP8%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6NSW7
- STRING: https://string-db.org/network/9606.ENSG00000255192
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NSW7


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NANOGP8-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/NANOGP8/NANOGP8-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6NSW7 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050460;IPR001356;IPR017970;IPR009057; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000255192-NANOGP8/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
