---
type: protein-evaluation
gene: "SUDS3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUDS3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SUDS3 / SDS3|FLJ00052|SAP45 |
| 蛋白全称 | Sin3 histone deacetylase corepressor complex component SDS3 |
| 蛋白大小 | 328 aa |
| UniProt ID | Q9H7L9 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 328 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 10 篇，极度新颖 |
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
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUDS3/IF_images/A-431_HPA040402_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUDS3/IF_images/U-251MG_HPA040402_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 328 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 10 |

**评价**: PubMed 10 篇，极度新颖

**关键文献**:
1. Rider SD Jr et al. (2023). "Suppressors of Break-Induced Replication in Human Cells". *Genes (Basel)*. PMID: 36833325
2. Banks CAS et al. (2020). "Integrative Modeling of a Sin3/HDAC Complex Sub-structure". *Cell Rep*. PMID: 32294434
3. Zhang K et al. (2013). "Depletion of Suds3 reveals an essential role in early lineage specification". *Dev Biol*. PMID: 23123966
4. Banks CAS et al. (2018). "A Structured Workflow for Mapping Human Sin3 Histone Deacetylase Complex Interactions Using Halo-MudPIT Affinity-Purification Mass Spectrometry". *Mol Cell Proteomics*. PMID: 29599190
5. Feng Y et al. (2009). "Isolation and characterization of sexual dimorphism genes expressed in chicken embryonic gonads". *Acta Biochim Biophys Sin (Shanghai)*. PMID: 19352543
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 328 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUDS3/SUDS3-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Sds3 |
| Pfam | Sds3 |
| SMART | Sds3 |

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

- C:Sin3-type complex (GO:0070822, ISS:UniProtKB)
- P:chromatin remodeling (GO:0006338, IDA:UniProtKB)

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
1. 新颖性: PubMed 10 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SUDS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111707-SUDS3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SUDS3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H7L9
- STRING: https://string-db.org/network/9606.ENSG00000111707
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7L9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SUDS3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUDS3/SUDS3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000111707-SUDS3/subcellular

![](https://images.proteinatlas.org/40402/413_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40402/413_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40402/417_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40402/417_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40402/420_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40402/420_B11_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
