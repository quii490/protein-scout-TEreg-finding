---
type: protein-evaluation
gene: "RDM1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RDM1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RDM1 / MGC33977 |
| 蛋白全称 | RAD52 motif-containing protein 1 |
| 蛋白大小 | 284 aa |
| UniProt ID | Q8NG50 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RDM1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RDM1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 284 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 23 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 9 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Cytoplasm, Nucleus, nucleolus, Cytoplasm, Nucleus, PML body, Nucleus, Cajal body | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 284 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 23 |

**关键文献**:
1. Xie et al. (2019). "RDM1 promotes neuroblastoma growth through the RAS-Raf-MEK-ERK pathway.". *FEBS Open Bio*. PMID: 30868057
2. Jagić et al. (2022). "BPM1 regulates RdDM-mediated DNA methylation via a cullin 3 independent mechanism.". *Plant Cell Rep*. PMID: 36066603
3. Li et al. (2025). "RDM1 plays an oncogenic role in clear cell renal cell carcinoma potentially by modulating MCM2.". *Sci Rep*. PMID: 40595023
4. Sheng et al. (2021). "Association of RDM1 with osteosarcoma progression via cell cycle and MEK/ERK signalling pathway regulation.". *J Cell Mol Med*. PMID: 34264012
5. Wongpalee et al. (2019). "CryoEM structures of Arabidopsis DDR complexes involved in RNA-directed DNA methylation.". *Nat Commun*. PMID: 31477705
**评价**: PubMed 23 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 284 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RDM1/RDM1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | DSRM_RDM1 |
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | RBD_domain_sf |
| InterPro | RDM1 |
| InterPro | RDM1_RRM |
| InterPro | RRM_dom |
| Pfam | DSRM_RDM1 |
| Pfam | RRM_1 |
| PROSITE | RRM |

**染色质调控潜力分析**: 9 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| SCNM1 | two hybrid prey pooling approach | 32296183 | — | — |
| CCDC57 | two hybrid prey pooling approach | 32296183 | — | — |
| CNTF | two hybrid array | 32296183 | — | — |
| RAD52 | two hybrid array | 32296183 | — | — |
| MRFAP1L1 | two hybrid array | 25416956 | — | — |
| PI4KB | anti tag coimmunoprecipitation | 33961781 | — | — |


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
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 23 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RDM1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000278023-RDM1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RDM1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8NG50
- STRING: https://string-db.org/network/9606.ENSG00000278023
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NG50


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[RDM1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/RDM1/RDM1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000278023-RDM1/subcellular

![](https://images.proteinatlas.org/24794/196_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24794/196_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24794/197_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24794/197_F10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
