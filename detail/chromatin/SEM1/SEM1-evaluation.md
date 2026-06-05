---
type: protein-evaluation
gene: "SEM1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SEM1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SEM1 / DSS1|Shfdg1|ECD|SHSF1|FLJ42280|PSMD15 |
| 蛋白全称 | 26S proteasome complex subunit SEM1 |
| 蛋白大小 | 70 aa |
| UniProt ID | P60896 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SEM1/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SEM1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 5/10 | ×1 | **5** | 70 aa, small/large |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 47 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 72 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | PDB + AlphaFold 结构互证 (+0.5) |
|  | **原始总分** |  | **101.5/183** | **101.0/183** |  |  |
|  | **归一化总分** |  | **55.5/100** | **55.2/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA|TAS |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 70 aa， small/large

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 47 |

**关键文献**:
1. Osetrina et al. (2023). "Extent of N-Terminus Folding of Semenogelin 1 Cleavage Product Determines Tendency to Amyloid Formation.". *Int J Mol Sci*. PMID: 37240295
2. Li et al. (2023). "SEM1 promotes tumor progression of glioblastoma via activating the akt signaling pathway.". *Cancer Lett*. PMID: 37652287
3. Nicoletti et al. (2024). "Regulatory elements in SEM1-DLX5-DLX6 (7q21.3) locus contribute to genetic control of coronal nonsyndromic craniosynostosis and bone density-related traits.". *Genet Med Open*. PMID: 39345948
4. Kragelund et al. (2016). "DSS1/Sem1, a Multifunctional and Intrinsically Disordered Protein.". *Trends Biochem Sci*. PMID: 26944332
5. Faza et al. (2010). "Sem1: a versatile "molecular glue"?". *Nucleus*. PMID: 21327099
**评价**: PubMed 47 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 70 aa |
| PDB 条数 | 72 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SEM1/SEM1-PAE.png]]

**评价**: 72 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | DSS1_SEM1 |
| Pfam | DSS1_SEM1 |
| SMART | DSS1_SEM1 |

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

- C:integrator complex (GO:0032039, IDA:HGNC-UCL)
- C:proteasome complex (GO:0000502, IDA:UniProtKB)
- C:proteasome regulatory particle, lid subcomplex (GO:0008541, IEA:InterPro)
- C:protein-containing complex (GO:0032991, IDA:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 72 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 47 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 72 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SEM1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127922-SEM1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEM1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P60896
- STRING: https://string-db.org/network/9606.ENSG00000127922
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60896


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SEM1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SEM1/SEM1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000127922-SEM1/subcellular

![](https://images.proteinatlas.org/72648/1409_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/72648/1409_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/72648/1412_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/72648/1412_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/72648/1495_E2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/72648/1495_E2_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
