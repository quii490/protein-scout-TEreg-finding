---
type: protein-evaluation
gene: "PTBP3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PTBP3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PTBP3 / DKFZp781I1117 |
| 蛋白全称 | Polypyrimidine tract-binding protein 3 |
| 蛋白大小 | 552 aa |
| UniProt ID | O95758 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PTBP3/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PTBP3/IF_images/CACO-2_1.jpg|CACO-2]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 552 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 71 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 13 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **84.5/183** | **84.0/183** |  |  |
|  | **归一化总分** |  | **46.2/100** | **45.9/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 552 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 71 |

**关键文献**:
1. Zhao et al. (2024). "PTBP3 Mediates IL-18 Exon Skipping to Promote Immune Escape in Gallbladder Cancer.". *Adv Sci (Weinh)*. PMID: 39116343
2. Zhou et al. (2025). "Targeting PTBP3-Mediated Alternative Splicing of COX11 Induces Cuproptosis for Inhibiting Gastric Cancer Peritoneal Metastasis.". *Adv Sci (Weinh)*. PMID: 40270362
3. Chen et al. (2025). "TERC Stimulates Fatty Acid Metabolism to Promote Bladder Cancer Progression.". *Cancer Res*. PMID: 40759031
4. Dong et al. (2022). "PTBP3 mediates TGF-β-induced EMT and metastasis of lung adenocarcinoma.". *Cell Cycle*. PMID: 35323096
5. Wang et al. (2024). "Polypyrimidine tract-binding protein 3/insulin-like growth factor 2 mRNA-binding proteins 3/high-mobility group A1 axis promotes renal cancer growth and metastasis.". *iScience*. PMID: 38405614
**评价**: PubMed 71 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 552 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 13 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PTBP3/PTBP3-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HnRNP-L/PTB |
| InterPro | HNRNPL_RRM |
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | PTBP1-like_RRM2 |
| InterPro | PTBP3_RRM4 |
| InterPro | RBD_domain_sf |
| InterPro | ROD1_RRM1 |
| InterPro | RRM_dom |
| Pfam | RRM_10 |
| Pfam | RRM_5 |
| Pfam | RRM_8 |
| SMART | RRM |
| PROSITE | RRM |

**染色质调控潜力分析**: 13 个已注释结构域，新颖蛋白基线水平

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
| 结构域 | UniProt/InterPro/Pfam | 13 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 71 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PTBP3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119314-PTBP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PTBP3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O95758
- STRING: https://string-db.org/network/9606.ENSG00000119314
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95758


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PTBP3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PTBP3/PTBP3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000119314-PTBP3/subcellular

![](https://images.proteinatlas.org/48374/699_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/48374/699_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/48374/823_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/48374/823_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/48374/850_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/48374/850_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95758 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 59..143; /note="RRM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 182..258; /note="RRM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 358..432; /note="RRM 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 475..550; /note="RRM 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR006536;IPR055204;IPR012677;IPR021790;IPR033110;IPR035979;IPR034326;IPR000504; |
| Pfam | PF22976;PF13893;PF11835; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119314-PTBP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAPZB | Opencell | false |
| COPB2 | Opencell | false |
| COPE | Opencell | false |
| ELAVL1 | Biogrid | false |
| ESR1 | Biogrid | false |
| MATR3 | Biogrid | false |
| PTBP1 | Biogrid | false |
| STAU1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
