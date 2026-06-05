---
type: protein-evaluation
gene: "PRR14"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR14 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PRR14 / MGC3121 |
| 蛋白全称 | Proline-rich protein 14 |
| 蛋白大小 | 585 aa |
| UniProt ID | Q9BWN1 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRR14/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRR14/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 585 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 16 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | UniProt + GO 核定位互证 (+1) |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Chromosome, Nucleus, Nucleus lamina, Nucleus, nucleoplasm | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 585 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 16 |

**关键文献**:
1. Kiseleva et al. (2023). "The secret life of chromatin tethers.". *FEBS Lett*. PMID: 37339933
2. Jin et al. (2021). "Preliminary Findings on Proline-Rich Protein 14 as a Diagnostic Biomarker for Parkinson's Disease.". *Neuromolecular Med*. PMID: 33001354
3. Yang et al. (2025). "PRR14 mediates mechanotransduction and regulates myofiber identity via MEF2C in skeletal muscle.". *Metabolism*. PMID: 39706290
4. Poleshko et al. (2014). "Specifying peripheral heterochromatin during nuclear lamina reassembly.". *Nucleus*. PMID: 24637393
5. Liu et al. (2024). "Analysis of copy number variants detected by sequencing in spontaneous abortion.". *Mol Cytogenet*. PMID: 38764094
**评价**: PubMed 16 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 585 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRR14/PRR14-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PRR14 |
| InterPro | Tantalus-like |
| Pfam | Tantalus |

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


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 16 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PRR14
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156858-PRR14
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PRR14%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BWN1
- STRING: https://string-db.org/network/9606.ENSG00000156858
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWN1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PRR14-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PRR14/PRR14-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000156858-PRR14/subcellular

![](https://images.proteinatlas.org/52022/766_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/52022/766_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/52022/778_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/52022/778_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/52022/865_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/52022/865_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
