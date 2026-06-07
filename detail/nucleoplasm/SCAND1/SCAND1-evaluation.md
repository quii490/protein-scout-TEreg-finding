---
type: protein-evaluation
gene: "SCAND1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SCAND1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SCAND1 / SDP1|RAZ1 |
| 蛋白全称 | SCAN domain-containing protein 1 |
| 蛋白大小 | 179 aa |
| UniProt ID | P57086 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 179 aa，尚可接受 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 15 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: scan-c2h2_zinc_finger |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCAND1/IF_images/PC-3_HPA071335_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCAND1/IF_images/SH-SY5Y_HPA071335_2.jpg|SH-SY5Y]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 179 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 15 |

**评价**: PubMed 15 篇，极度新颖

**关键文献**:
1. Xu C et al. (2025). "Dynamic remodelling of epithelial plasticity in colorectal cancer from single-cell and spatially resolved perspectives". *J Transl Med*. PMID: 41286944
2. Sheta M et al. (2023). "Stress-Inducible SCAND Factors Suppress the Stress Response and Are Biomarkers for Enhanced Prognosis in Cancers". *Int J Mol Sci*. PMID: 36982267
3. Eguchi T et al. (2022). "SCAND1 Reverses Epithelial-to-Mesenchymal Transition (EMT) and Suppresses Prostate Cancer Growth and Migration". *Cells*. PMID: 36552758
4. Lyu G et al. (2025). "Integrative Analysis of Cuproptosis-Related Mitochondrial Depolarisation Genes for Prognostic Prediction in Non-Small Cell Lung Cancer". *J Cell Mol Med*. PMID: 40008552
5. Goldman A et al. (2019). "A computationally inspired in-vivo approach identifies a link between amygdalar transcriptional heterogeneity, socialization and anxiety". *Transl Psychiatry*. PMID: 31819040
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 179 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCAND1/SCAND1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SCAN-C2H2_zinc_finger |
| InterPro | SCAN_dom |
| InterPro | SCAN_sf |
| Pfam | SCAN |
| SMART | SCAN |
| PROSITE | SCAN_BOX |

**染色质调控潜力分析**: 染色质/DNA 结构域: scan-c2h2_zinc_finger

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
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 15 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SCAND1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171222-SCAND1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCAND1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P57086
- STRING: https://string-db.org/network/9606.ENSG00000171222
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57086


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SCAND1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SCAND1/SCAND1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000171222-SCAND1/subcellular

![](https://images.proteinatlas.org/71335/1378_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/71335/1378_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/71335/1696_G10_4_red_green.jpg)
![](https://images.proteinatlas.org/71335/1696_G10_5_red_green.jpg)
![](https://images.proteinatlas.org/71335/1845_C1_14_cr5ab925fe3ba02_red_green.jpg)
![](https://images.proteinatlas.org/71335/1845_C1_17_cr5ab925fe3c459_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P57086 |
| SMART | SM00431; |
| UniProt Domain [FT] | DOMAIN 108..166; /note="SCAN box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00187" |
| InterPro | IPR050916;IPR003309;IPR038269; |
| Pfam | PF02023; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171222-SCAND1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MZF1 | Biogrid, Bioplex | true |
| PGBD1 | Intact, Biogrid, Bioplex | true |
| ZKSCAN4 | Intact, Biogrid, Bioplex | true |
| ZNF213 | Intact, Biogrid, Bioplex | true |
| ZNF24 | Intact, Biogrid | true |
| ZNF263 | Intact, Biogrid | true |
| ZNF394 | Intact, Biogrid | true |
| ZNF397 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
