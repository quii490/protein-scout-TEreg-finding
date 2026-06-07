---
type: protein-evaluation
gene: "RTF2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RTF2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RTF2 / HSPC164|CDAO5 |
| 蛋白全称 | Replication termination factor 2 |
| 蛋白大小 | 306 aa |
| UniProt ID | Q9BY42 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/RTF2/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/RTF2/IF_images/NIH-3T3_1.jpg|NIH 3T3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | Nuclear + cyto, some evidence |
| 蛋白大小 | 10/10 | ×1 | **10** | 306 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 7 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
| **原始总分** |  |  | **122/183** |  |
| **归一化总分** |  |  | **66.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Chromosome | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, some evidence

#### 3.2 蛋白大小评估

**评价**: 306 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 7 |

**关键文献**:
1. Kottemann et al. (2018). "Removal of RTF2 from Stalled Replisomes Promotes Maintenance of Genome Integrity.". *Mol Cell*. PMID: 29290612
2. Budden et al. (2023). "Schizosaccharomyces pombe Rtf2 is important for replication fork barrier activity of RTS1 via splicing of Rtf1.". *Elife*. PMID: 37615341
3. Chia et al. (2020). "Loss of the Nuclear Protein RTF2 Enhances Influenza Virus Replication.". *J Virol*. PMID: 32878895
4. Inagawa et al. (2009). "Schizosaccharomyces pombe Rtf2 mediates site-specific replication termination by inhibiting replication restart.". *Proc Natl Acad Sci U S A*. PMID: 19416828
5. Conti et al. (2024). "RTF2 controls replication repriming and ribonucleotide excision at the replisome.". *Nat Commun*. PMID: 38431617
**评价**: PubMed 7 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 306 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/RTF2/RTF2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Rtf2 |
| InterPro | Rtf2_RING-finger |
| Pfam | Rtf2 |

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
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 7 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RTF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000022277-RTF2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTF2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BY42
- STRING: https://string-db.org/network/9606.ENSG00000022277
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BY42


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[RTF2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/RTF2/RTF2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BY42 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006735;IPR027799; |
| Pfam | PF04641; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000022277-RTF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BBOX1 | Bioplex | false |
| CES2 | Bioplex | false |
| DMAP1 | Bioplex | false |
| FLNC | Intact | false |
| IL1R2 | Bioplex | false |
| KDM4B | Bioplex | false |
| KIFBP | Bioplex | false |
| MILR1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
