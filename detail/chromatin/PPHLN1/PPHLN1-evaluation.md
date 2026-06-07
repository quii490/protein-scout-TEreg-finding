---
type: protein-evaluation
gene: "PPHLN1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPHLN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPHLN1 / -- |
| 蛋白全称 | Periphilin-1 |
| 蛋白大小 | 458 aa |
| UniProt ID | Q8NEY8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PPHLN1/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PPHLN1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 458 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 20 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Cytoplasm, Chromosome | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 458 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 20 |

**关键文献**:
1. Saulnier et al. (2024). "A group 3 medulloblastoma stem cell program is maintained by OTX2-mediated alternative splicing.". *Nat Cell Biol*. PMID: 39025928
2. Zhu et al. (2018). "NP220 mediates silencing of unintegrated retroviral DNA.". *Nature*. PMID: 30487602
3. Katoh et al. (2016). "FGFR inhibitors: Effects on cancer cells, tumor microenvironment and whole-body homeostasis (Review).". *Int J Mol Med*. PMID: 27245147
4. Huang et al. (2024). "Small-cohort GWAS discovery with AI over massive functional genomics knowledge graph.". *medRxiv*. PMID: 39677475
5. Jayatissa et al. (2025). "The ERVK3-1 Microprotein Interacts with the HUSH Complex.". *Biochemistry*. PMID: 40699144
**评价**: PubMed 20 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 458 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PPHLN1/PPHLN1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Periphilin-1_C |
| InterPro | Pphln1 |
| Pfam | Periphilin_C |

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

- C:chromatin (GO:0000785, IDA:UniProtKB)
- C:HUSH complex (GO:0140283, IDA:UniProtKB)
- C:HUSH2 complex (GO:0140286, IDA:UniProtKB)
- P:constitutive heterochromatin formation (GO:0140719, IDA:UniProtKB)
- P:protein localization to heterochromatin (GO:0097355, IDA:UniProtKB)
- P:transposable element silencing by heterochromatin formation (GO:0141005, IDA:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
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
1. 新颖性: PubMed 20 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPHLN1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134283-PPHLN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPHLN1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8NEY8
- STRING: https://string-db.org/network/9606.ENSG00000134283
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEY8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPHLN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PPHLN1/PPHLN1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000134283-PPHLN1/subcellular

![](https://images.proteinatlas.org/38902/412_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38902/412_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38902/419_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38902/419_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38902/471_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38902/471_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NEY8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR057603;IPR028851; |
| Pfam | PF25234; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134283-PPHLN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANLN | Biogrid | false |
| BRCA1 | Biogrid | false |
| BRD4 | Biogrid | false |
| CCDC57 | Intact | false |
| CLK2 | Biogrid | false |
| CPSF6 | Opencell | false |
| ELAVL1 | Biogrid | false |
| HMGN5 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
