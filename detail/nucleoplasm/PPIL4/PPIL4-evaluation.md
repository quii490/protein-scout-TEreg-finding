---
type: protein-evaluation
gene: "PPIL4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPIL4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPIL4 / -- |
| 蛋白全称 | Peptidyl-prolyl cis-trans isomerase-like 4 |
| 蛋白大小 | 492 aa |
| UniProt ID | Q8WUA2 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 492 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 6 篇，极度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 7 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 12 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA|ISS |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL4/IF_images/SiHa_HPA031599_1.jpg|SiHa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL4/IF_images/U-251MG_HPA031599_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 492 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 6 |

**评价**: PubMed 6 篇，极度新颖

**关键文献**:
1. Baek K et al. (2024). "Unveiling the hidden interactome of CRBN molecular glues with chemoproteomics". *bioRxiv*. PMID: 39314457
2. Schmitzová J et al. (2023). "Structural basis of catalytic activation in human splicing". *Nature*. PMID: 37165190
3. Baek K et al. (2025). "Unveiling the hidden interactome of CRBN molecular glues". *Nat Commun*. PMID: 40707481
4. Barak T et al. (2021). "PPIL4 is essential for brain angiogenesis and implicated in intracranial aneurysms in humans". *Nat Med*. PMID: 34887573
5. Chen H et al. (2025). "The Hao-Fountain syndrome protein USP7 regulates neuronal connectivity in the brain via a novel p53-independent ubiquitin signaling pathway". *Cell Rep*. PMID: 39862434
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 492 aa |
| PDB 条数 | 7 |
| 已注释结构域 | 12 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL4/PPIL4-PAE.png]]

**评价**: 7 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | CRIP |
| InterPro | Cyclophilin-like_dom_sf |
| InterPro | Cyclophilin-type_PPIase_dom |
| InterPro | Cyclophilin_PPIL4 |
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | RBD_domain_sf |
| InterPro | RRM_dom |
| Pfam | Pro_isomerase |
| Pfam | RRM_1 |
| SMART | RRM |
| PROSITE | CSA_PPIASE_2 |
| PROSITE | RRM |

**染色质调控潜力分析**: 12 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 7 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 12 个 | 多库一致 |
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
1. 新颖性: PubMed 6 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 7 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPIL4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131013-PPIL4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPIL4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8WUA2
- STRING: https://string-db.org/network/9606.ENSG00000131013
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUA2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPIL4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIL4/PPIL4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000131013-PPIL4/subcellular

![](https://images.proteinatlas.org/31599/1000_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/31599/1000_D8_3_red_green.jpg)
![](https://images.proteinatlas.org/31599/1003_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/31599/1003_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/31599/1509_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/31599/1509_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
