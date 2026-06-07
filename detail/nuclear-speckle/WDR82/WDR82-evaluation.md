---
type: protein-evaluation
gene: "WDR82"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR82 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | WDR82 / PRO2730|MST107|MSTP107|PRO34047|WDR82A|SWD2 |
| 蛋白全称 | WD repeat-containing protein 82 |
| 蛋白大小 | 313 aa |
| UniProt ID | Q6UXN9 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/WDR82/IF_images/PC-3_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/WDR82/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 313 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 10 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **107/183** | **106.0/183** |  |  |
|  | **归一化总分** |  | **58.5/100** | **57.9/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome, Cytoplasm | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 313 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 42 |

**关键文献**:
1. Erickson et al. (2025). "PP1/PNUTS phosphatase binds the restrictor complex and stimulates RNA Pol II transcription termination.". *Cell Rep*. PMID: 40244850
2. Estell et al. (2023). "A restrictor complex of ZC3H4, WDR82, and ARS2 integrates with PNUTS to control unproductive transcription.". *Mol Cell*. PMID: 37329883
3. Spencley et al. (2023). "Co-transcriptional genome surveillance by HUSH is coupled to termination machinery.". *Mol Cell*. PMID: 37164018
4. Mimoso et al. (2025). "Restrictor slows RNAPII elongation to promote termination at noncoding RNA loci.". *Genes Dev*. PMID: 40393801
5. Russo et al. (2023). "Restrictor synergizes with Symplekin and PNUTS to terminate extragenic transcription.". *Genes Dev*. PMID: 38092518
**评价**: PubMed 42 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 313 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 10 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/WDR82/WDR82-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Swd2/WDR82 |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | WD40 |
| SMART | WD40 |
| PROSITE | WD_REPEATS_1 |
| PROSITE | WD_REPEATS_2 |
| PROSITE | WD_REPEATS_REGION |

**染色质调控潜力分析**: 10 个已注释结构域，新颖蛋白基线水平

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
- C:histone methyltransferase complex (GO:0035097, IDA:UniProtKB)
- C:PTW/PP1 phosphatase complex (GO:0072357, IDA:UniProtKB)
- C:Set1C/COMPASS complex (GO:0048188, IDA:UniProtKB)
- F:chromatin binding (GO:0003682, IBA:GO_Central)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 10 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 42 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=WDR82
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164091-WDR82
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22WDR82%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q6UXN9
- STRING: https://string-db.org/network/9606.ENSG00000164091
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UXN9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[WDR82-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/WDR82/WDR82-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (approved)。来源: https://www.proteinatlas.org/ENSG00000164091-WDR82/subcellular

![](https://images.proteinatlas.org/40427/1000_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/40427/1000_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/40427/1003_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/40427/1003_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/40427/1203_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/40427/1203_D5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UXN9 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037867;IPR015943;IPR020472;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164091-WDR82/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TOP1 | Biogrid, Opencell | true |
| ASH2L | Biogrid | false |
| CCT5 | Biogrid | false |
| CPSF6 | Opencell | false |
| CSNK2B | Opencell | false |
| CUL4B | Biogrid | false |
| CXXC1 | Biogrid | false |
| EP300 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
