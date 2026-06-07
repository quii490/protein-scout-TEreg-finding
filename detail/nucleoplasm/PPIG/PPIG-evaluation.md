---
type: protein-evaluation
gene: "PPIG"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPIG 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPIG / CARS-Cyp|SRCyp|SCAF10 |
| 蛋白全称 | Peptidyl-prolyl cis-trans isomerase G |
| 蛋白大小 | 754 aa |
| UniProt ID | Q13427 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 754 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 14 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 4 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 6 个已注释结构域 |
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
| UniProt | Nucleus matrix, Nucleus speckle | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIG/IF_images/A-431_HPA021788_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIG/IF_images/U-251MG_HPA021788_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 754 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |

**评价**: PubMed 14 篇，极度新颖

**关键文献**:
1. Lu P et al. (2025). "Systematic characterization of full-length RNA isoforms in human colorectal cancer at single-cell resolution". *Protein Cell*. PMID: 40702779
2. Yang X et al. (2025). "Genome-wide Mendelian randomization study identifies therapeutic targets for diabetic microangiopathy". *Diabetes Res Clin Pract*. PMID: 40349847
3. Mercadante S et al. (2020). "Personalized Pain Goals and Responses in Advanced Cancer Patients". *Pain Med*. PMID: 31633792
4. Reynolds LJ et al. (2023). "Short-term removal of exercise impairs glycemic control in older adults: A randomized trial". *Physiol Rep*. PMID: 36695760
5. Hou XX et al. (2025). "Improving gelation properties of low concentration peanut protein isolate by phosphorylation". *Int J Biol Macromol*. PMID: 40360110
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 754 aa |
| PDB 条数 | 4 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIG/PPIG-PAE.png]]

**评价**: 4 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Cyclophilin-like_dom_sf |
| InterPro | Cyclophilin-type_PPIase_CS |
| InterPro | Cyclophilin-type_PPIase_dom |
| Pfam | Pro_isomerase |
| PROSITE | CSA_PPIASE_1 |
| PROSITE | CSA_PPIASE_2 |

**染色质调控潜力分析**: 6 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 4 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
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
1. 新颖性: PubMed 14 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 4 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPIG
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138398-PPIG
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPIG%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q13427
- STRING: https://string-db.org/network/9606.ENSG00000138398
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13427


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPIG-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPIG/PPIG-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000138398-PPIG/subcellular

![](https://images.proteinatlas.org/21788/234_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/21788/234_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/21788/235_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/21788/235_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/21788/535_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/21788/535_D10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13427 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 11..176; /note="PPIase cyclophilin-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00156" |
| InterPro | IPR029000;IPR020892;IPR002130; |
| Pfam | PF00160; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138398-PPIG/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NKAP | Intact, Biogrid | true |
| PCBP1 | Intact, Biogrid | true |
| RBM39 | Intact, Biogrid, Opencell | true |
| CEP70 | Intact | false |
| CPSF6 | Opencell | false |
| CUL3 | Biogrid | false |
| DAB1 | Intact | false |
| KCTD6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
