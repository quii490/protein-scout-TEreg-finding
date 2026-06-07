---
type: protein-evaluation
gene: "THYN1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THYN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | THYN1 / THY28 |
| 蛋白全称 | Thymocyte nuclear protein 1 |
| 蛋白大小 | 225 aa |
| UniProt ID | Q9P016 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 225 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 9 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 5 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/THYN1/IF_images/A-431_HPA038732_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/THYN1/IF_images/U-251MG_HPA038732_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 225 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 9 |

**评价**: PubMed 9 篇，极度新颖

**关键文献**:
1. Rodríguez-López R et al. (2021). "Immune Deficiency in Jacobsen Syndrome: Molecular and Phenotypic Characterization". *Genes (Basel)*. PMID: 34440371
2. He GW et al. (2022). "Identification of novel rare copy number variants associated with sporadic tetralogy of Fallot and clinical implications". *Clin Genet*. PMID: 35882632
3. Kitaura F et al. (2019). "Normal B cell development and Pax5 expression in Thy28/ThyN1-deficient mice". *PLoS One*. PMID: 31329649
4. Guo S et al. (2024). "Whole transcriptome sequencing of testis and epididymis reveals genes associated with sperm development in roosters". *BMC Genomics*. PMID: 39497056
5. Xu W et al. (2022). "Genome-Wide Association Studies and Haplotype-Sharing Analysis Targeting the Egg Production Traits in Shaoxing Duck". *Front Genet*. PMID: 35419032
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 225 aa |
| PDB 条数 | 2 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/THYN1/THYN1-PAE.png]]

**评价**: 2 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | 5hmC_binding |
| InterPro | EVE_domain |
| InterPro | PUA-like_sf |
| InterPro | THYN1-like_EVE |
| Pfam | EVE |

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

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 2 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 9 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 2 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=THYN1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151500-THYN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22THYN1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9P016
- STRING: https://string-db.org/network/9606.ENSG00000151500
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P016


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[THYN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/THYN1/THYN1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000151500-THYN1/subcellular

![](https://images.proteinatlas.org/38732/449_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/38732/449_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/38732/452_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/38732/452_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/38732/455_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/38732/455_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P016 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052181;IPR002740;IPR015947;IPR047197; |
| Pfam | PF01878; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151500-THYN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SHPK | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
