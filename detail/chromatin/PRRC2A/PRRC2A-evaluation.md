---
type: protein-evaluation
gene: "PRRC2A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRRC2A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PRRC2A / G2|D6S51E |
| 蛋白全称 | Protein PRRC2A |
| 蛋白大小 | 2157 aa |
| UniProt ID | P48634 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRRC2A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRRC2A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 2/10 | ×1 | **2** | 2157 aa, too extreme |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 45 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | UniProt + GO 核定位互证 (+1) |
|  | **原始总分** |  | **99/183** | **98.0/183** |  |  |
|  | **归一化总分** |  | **54.1/100** | **53.6/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA|NAS |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: 2157 aa， too extreme

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 45 |

**关键文献**:
1. Tan et al. (2023). "The m6A reader PRRC2A is essential for meiosis I completion during spermatogenesis.". *Nat Commun*. PMID: 36964127
2. Zhang et al. (2024). "PRRC2B modulates oligodendrocyte progenitor cell development and myelination by stabilizing Sox2 mRNA.". *Cell Rep*. PMID: 38507412
3. Wu et al. (2019). "A novel m(6)A reader Prrc2a controls oligodendroglial specification and myelination.". *Cell Res*. PMID: 30514900
4. Wu et al. (2025). "m(6)A Reader PRRC2A Promotes Colorectal Cancer Progression via CK1ε-Mediated Activation of WNT and YAP Signaling Pathways.". *Adv Sci (Weinh)*. PMID: 39582289
5. Chen et al. (2022). "Genome-Wide Identification of N6-Methyladenosine Associated SNPs as Potential Functional Variants for Type 1 Diabetes.". *Front Endocrinol (Lausanne)*. PMID: 35784577
**评价**: PubMed 45 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 2157 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PRRC2A/PRRC2A-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | BAT2_N |
| InterPro | PRRC2 |
| Pfam | BAT2_N |

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
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 45 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PRRC2A
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204469-PRRC2A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PRRC2A%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P48634
- STRING: https://string-db.org/network/9606.ENSG00000204469
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48634


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PRRC2A-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PRRC2A/PRRC2A-PAE.png]]




