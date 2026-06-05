---
type: protein-evaluation
gene: "TMA16"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMA16 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TMA16 / FLJ11184 |
| 蛋白全称 | Translation machinery-associated protein 16 |
| 蛋白大小 | 203 aa |
| UniProt ID | Q96EY4 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 203 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 2 篇，极度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 9 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TMA16/IF_images/A-431_HPA041571_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TMA16/IF_images/U-251MG_HPA041571_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 203 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 2 |

**评价**: PubMed 2 篇，极度新颖

**关键文献**:
1. Zhu A et al. (2025). "Characterization of methylation profile in biofluid cell-free DNA and identification of differentially methylated genes for phenotypic representations in Parkinson's disease". *Clin Neurol Neurosurg*. PMID: 40527220
2. Liang X et al. (2020). "Structural snapshots of human pre-60S ribosomal particles before and after nuclear export". *Nat Commun*. PMID: 32669547
3. Loll-Krippleber R & Brown GW (2017). "P-body proteins regulate transcriptional rewiring to promote DNA replication stress resistance". *Nat Commun*. PMID: 28916784
4. Lee M et al. (2016). "Genome-wide association study for the interaction between BMR and BMI in obese Korean women including overweight". *Nutr Res Pract*. PMID: 26865924
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 203 aa |
| PDB 条数 | 9 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TMA16/TMA16-PAE.png]]

**评价**: 9 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Tma16 |
| InterPro | Tma16_sf |
| Pfam | Tma16 |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 9 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 2 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 9 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TMA16
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198498-TMA16
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TMA16%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96EY4
- STRING: https://string-db.org/network/9606.ENSG00000198498
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EY4


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TMA16-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TMA16/TMA16-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000198498-TMA16/subcellular

![](https://images.proteinatlas.org/41571/486_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/41571/486_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/41571/490_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/41571/490_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/41571/509_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/41571/509_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
