---
type: protein-evaluation
gene: "SPINDOC"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPINDOC 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SPINDOC / SPIN-DOC |
| 蛋白全称 | Spindlin interactor and repressor of chromatin-binding protein |
| 蛋白大小 | 381 aa |
| UniProt ID | Q9BUA3 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SPINDOC/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SPINDOC/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度        | 得分    | 满分  | 加权后           | 关键证据摘要                                               |
| --------- | ----- | --- | ------------- | ---------------------------------------------------- |
| 核定位特异性    | 8/10  | ×4  | **32**        | UniProt 注释为细胞核，中等置信度                                 |
| 蛋白大小      | 10/10 | ×1  | **10**        | 381 aa，处于理想范围                                        |
| 研究新颖性     | 10/10 | ×5  | **50**        | PubMed 10 篇，极度新颖                                     |
| 三维结构      | 8/10  | ×3  | **24**        | 3 个 PDB 结构 + AlphaFold 预测                            |
| 调控结构域     | 10/10 | ×2  | **20**        | 染色质/DNA 结构域: spin-doc_znf-c2h2, zf-c2h2_12           |
| PPI 网络    | 2/10  | ×3  | **6**         | PPI 数据极为稀少                                           |
| 互证加分      | --    | --  | **+1.5**      | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **143/183** |  |
| **归一化总分** |  |  | **78.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 381 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 10 |

**评价**: PubMed 10 篇，极度新颖

**关键文献**:
1. Liu X et al. (2024). "An integrated structural model of the DNA damage-responsive H3K4me3 binding WDR76:SPIN1 complex with the nucleosome". *Proc Natl Acad Sci U S A*. PMID: 39116123
2. Yang F et al. (2021). "SPINDOC binds PARP1 to facilitate PARylation". *Nat Commun*. PMID: 34737271
3. Liu X et al. (2020). "Driving integrative structural modeling with serial capture affinity purification". *Proc Natl Acad Sci U S A*. PMID: 33257578
4. Zhao F et al. (2024). "Molecular Basis for SPINDOC-Spindlin1 Engagement and Its Role in Transcriptional Attenuation". *J Mol Biol*. PMID: 37977297
5. Liu X et al. (2023). "Serial Capture Affinity Purification and Integrated Structural Modeling of the H3K4me3 Binding and DNA Damage Related WDR76:SPIN1 Complex". *bioRxiv*. PMID: 36778327
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 381 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SPINDOC/SPINDOC-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SPIN-DOC_Znf-C2H2 |
| InterPro | ZnF_transloc-Spindlin_int |
| Pfam | zf-C2H2_12 |

**染色质调控潜力分析**: 染色质/DNA 结构域: spin-doc_znf-c2h2, zf-c2h2_12

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
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
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
1. 新颖性: PubMed 10 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SPINDOC
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168005-SPINDOC
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SPINDOC%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BUA3
- STRING: https://string-db.org/network/9606.ENSG00000168005
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUA3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SPINDOC-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SPINDOC/SPINDOC-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000168005-SPINDOC/subcellular

![](https://images.proteinatlas.org/50313/776_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/50313/776_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/50313/789_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/50313/789_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/50313/899_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/50313/899_F9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BUA3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040647;IPR052675; |
| Pfam | PF18658; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168005-SPINDOC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NTAQ1 | Intact | false |
| RC3H1 | Biogrid | false |
| SPIN1 | Bioplex | false |
| SPIN2B | Bioplex | false |
| SPIN3 | Intact, Bioplex | false |
| UQCRC1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
