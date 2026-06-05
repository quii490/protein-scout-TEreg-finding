---
type: protein-evaluation
gene: "TADA2A"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TADA2A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TADA2A / ADA2|hADA2|ADA2A |
| 蛋白全称 | Transcriptional adapter 2-alpha |
| 蛋白大小 | 443 aa |
| UniProt ID | O75478 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/TADA2A/IF_images/REH_1.jpg|REH]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/TADA2A/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 443 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 31 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeodomain-like_sf, myb_dna-binding, myb_dom, sant, sant |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 443 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 31 |

**评价**: PubMed 31 篇，高度新颖

**关键文献**:
1. Lee JY et al. (2021). "α-Synuclein A53T Binds to Transcriptional Adapter 2-Alpha and Blocks Histone H3 Acetylation". *Int J Mol Sci*. PMID: 34065515
2. Valdés-Hernández J et al. (2024). "Identification of candidate regulatory genes for intramuscular fatty acid composition in pigs by transcriptome analysis". *Genet Sel Evol*. PMID: 38347496
3. Zhang Y et al. (2017). "Investigation of fusion gene expression in HCT116 cells". *Oncol Lett*. PMID: 29181107
4. Bui APN et al. (2025). "PCR-RFLP assays to detect recessive lethal alleles in Landrace and Duroc pigs in Vietnam". *J Vet Diagn Invest*. PMID: 40772539
5. Yuan Y et al. (2025). "CircTADA2A inhibits cell proliferation and promotes ferroptosis by sponging miR-638 in acute myeloid leukemia". *Hum Cell*. PMID: 40608154
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 443 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 19 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/TADA2A/TADA2A-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ADA2-like_ZZ |
| InterPro | Ada2/TADA2 |
| InterPro | Homeodomain-like_sf |
| InterPro | Myb_dom |
| InterPro | SANT/Myb |
| InterPro | SANT_dom |
| InterPro | SWIRM |
| InterPro | TADA2A_B-like_dom |
| InterPro | WH-like_DNA-bd_sf |
| InterPro | Znf_ZZ |
| InterPro | Znf_ZZ_sf |
| Pfam | Myb_DNA-binding |
| Pfam | SWIRM |
| Pfam | TADA2A-like_3rd |
| Pfam | ZZ_ADA2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeodomain-like_sf, myb_dna-binding, myb_dom, sant, sant/myb

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:ATAC complex (GO:0140672, IDA:ComplexPortal)
- C:SAGA complex (GO:0000124, IDA:UniProtKB)
- C:SAGA-type complex (GO:0070461, IBA:GO_Central)
- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 19 个 | 多库一致 |
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
1. 新颖性: PubMed 31 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TADA2A
- Protein Atlas: https://www.proteinatlas.org/ENSG00000276234-TADA2A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TADA2A%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O75478
- STRING: https://string-db.org/network/9606.ENSG00000276234
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75478


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TADA2A-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/TADA2A/TADA2A-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000276234-TADA2A/subcellular

![](https://images.proteinatlas.org/76497/1674_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/76497/1674_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/76497/1676_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/76497/1676_F1_4_red_green.jpg)
![](https://images.proteinatlas.org/76497/1680_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/76497/1680_G1_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
