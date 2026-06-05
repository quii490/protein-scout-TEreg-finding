---
type: protein-evaluation
gene: "QRICH1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## QRICH1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | QRICH1 / FLJ20259|VERBRAS|AB-DIP |
| 蛋白全称 | Transcriptional regulator QRICH1 |
| 蛋白大小 | 776 aa |
| UniProt ID | Q2TAL8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/QRICH1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/QRICH1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 776 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 39 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 5 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **110.5/183** |  |
| **归一化总分** |  |  | **60.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome, Cytoplasm, Cell membrane | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 776 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 39 |

**关键文献**:
1. Kumble et al. (2022). "The clinical and molecular spectrum of QRICH1 associated neurodevelopmental disorder.". *Hum Mutat*. PMID: 34859529
2. You et al. (2021). "QRICH1 dictates the outcome of ER stress through transcriptional control of proteostasis.". *Science*. PMID: 33384352
3. Bianchi et al. (2025). "Zincore, an atypical coregulator, binds zinc finger transcription factors to control gene expression.". *Science*. PMID: 40608935
4. Akula et al. (2023). "Exome Sequencing and the Identification of New Genes and Shared Mechanisms in Polymicrogyria.". *JAMA Neurol*. PMID: 37486637
5. Pande et al. (2024). "De novo variants underlying monogenic syndromes with intellectual disability in a neurodevelopmental cohort from India.". *Eur J Hum Genet*. PMID: 38114583
**评价**: PubMed 39 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 776 aa |
| PDB 条数 | 2 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/QRICH1/QRICH1-PAE.png]]

**评价**: 2 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | QRICH1_dom |
| InterPro | ZMYM2-like_C |
| InterPro | ZnF_MYMT-QRICH1 |
| Pfam | DUF3504 |
| Pfam | QRICH1 |

**染色质调控潜力分析**: 5 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 2 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 39 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 2 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=QRICH1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198218-QRICH1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22QRICH1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q2TAL8
- STRING: https://string-db.org/network/9606.ENSG00000198218
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TAL8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[QRICH1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/QRICH1/QRICH1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198218-QRICH1/subcellular

![](https://images.proteinatlas.org/37677/2267_B11_35_red_green.jpg)
![](https://images.proteinatlas.org/37677/2267_B11_62_red_green.jpg)
![](https://images.proteinatlas.org/37677/430_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/37677/430_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/37677/432_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/37677/432_A2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
