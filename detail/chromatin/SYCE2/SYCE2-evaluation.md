---
type: protein-evaluation
gene: "SYCE2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYCE2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SYCE2 / CESC1 |
| 蛋白全称 | Synaptonemal complex central element protein 2 |
| 蛋白大小 | 218 aa |
| UniProt ID | Q6PIF2 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE2/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 218 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 21 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 1 domain(s), 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome | 实验证据/预测 |
| GO-CC | GO:0005634 | HDA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 218 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 21 |

**评价**: PubMed 21 篇，高度新颖

**关键文献**:
1. Liu K et al. (2025). "SOX30 Governs Synaptonemal Complex Assembly and Homologous Recombination in Male Meiosis". *Cell Prolif*. PMID: 41467312
2. Dunce JM et al. (2022). "Coiled-coil structure of meiosis protein TEX12 and conformational regulation by its C-terminal tip". *Commun Biol*. PMID: 36071143
3. Hamer G et al. (2006). "Characterization of a novel meiosis-specific protein within the central element of the synaptonemal complex". *J Cell Sci*. PMID: 16968740
4. Olaya I et al. (2025). "Distinct cellular and reproductive consequences of meiotic chromosome synapsis defects in syce2 and sycp1 mutant zebrafish". *PLoS Genet*. PMID: 40911633
5. Dunce JM et al. (2021). "Structural basis of meiotic chromosome synaptic elongation through hierarchical fibrous assembly of SYCE2-TEX12". *Nat Struct Mol Biol*. PMID: 34373646
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 218 aa |
| PDB 条数 | 2 |
| 已注释结构域 | 1 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE2/SYCE2-PAE.png]]

**评价**: 2 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Syce2 |

**染色质调控潜力分析**: 1 domain(s), 新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- P:synaptonemal complex assembly (GO:0007130, NAS:BHF-UCL)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 2 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 1 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 21 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 2 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SYCE2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161860-SYCE2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SYCE2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6PIF2
- STRING: https://string-db.org/network/9606.ENSG00000161860
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PIF2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SYCE2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE2/SYCE2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000161860-SYCE2/subcellular

![](https://images.proteinatlas.org/62919/1486_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/62919/1486_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/62919/1496_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/62919/1496_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/62919/1547_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/62919/1547_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
