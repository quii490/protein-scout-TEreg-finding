---
type: protein-evaluation
gene: "PWP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PWP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PWP1 / IEF-SSP-9502 |
| 蛋白全称 | Periodic tryptophan protein 1 homolog |
| 蛋白大小 | 501 aa |
| UniProt ID | Q13610 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 501 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 16 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 11 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Nucleus, nucleolus, Chromosome | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 501 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 16 |

**关键文献**:
1. Jiang et al. (2025). "PWP1 transcriptionally regulates p53, modulating apoptosis and cell cycle to promote gastric cancer progression.". *Apoptosis*. PMID: 39720977
2. Tian et al. (2025). "Periodic tryptophan protein 1 promotes colorectal cancer growth via ribosome biogenesis.". *Int J Clin Oncol*. PMID: 40057905
3. Yamamoto et al. (2025). "Pwp1 inhibition impairs the development and early lineage commitment of mouse preimplantation embryos.". *J Reprod Dev*. PMID: 40335308
4. Rahman et al. (2023). "The Caenorhabditis elegans cullin-RING ubiquitin ligase CRL4DCAF-1 is required for proper germline nucleolus morphology and male development.". *Genetics*. PMID: 37433110
5. Hasygar et al. (2021). "Coordinated control of adiposity and growth by anti-anabolic kinase ERK7.". *EMBO Rep*. PMID: 33369866
**评价**: PubMed 16 篇，极度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 501 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP1/PWP1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PWP1 |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | WD40 |
| SMART | WD40 |
| PROSITE | WD_REPEATS_1 |
| PROSITE | WD_REPEATS_2 |
| PROSITE | WD_REPEATS_REGION |

**染色质调控潜力分析**: 11 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ARX1 | inferred by author | 16429126 | — | — |
| MEC1 | inferred by author | 16429126 | — | — |
| ACT1 | inferred by author | 16429126 | — | — |
| LYAR | anti bait coimmunoprecipitation | 17353931 | — | — |
| AEP1 | inferred by author | 16429126 | — | — |
| ARO1 | inferred by author | 16429126 | — | — |
| a0a3n4b749_yerpe | two hybrid pooling approach | 20711500 | — | — |
| TNS2 | two hybrid array | 25814554 | — | — |
| PIK3R3 | two hybrid array | 25814554 | — | — |
| DAPK1 | protein array | 29513927 | — | — |


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
| 结构域 | UniProt/InterPro/Pfam | 11 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

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
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PWP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136045-PWP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PWP1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q13610
- STRING: https://string-db.org/network/9606.ENSG00000136045
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13610


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PWP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PWP1/PWP1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (approved)。来源: https://www.proteinatlas.org/ENSG00000136045-PWP1/subcellular

![](https://images.proteinatlas.org/38708/565_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/38708/565_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/38708/570_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/38708/570_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/38708/584_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/38708/584_B9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
