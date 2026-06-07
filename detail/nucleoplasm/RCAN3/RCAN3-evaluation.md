---
type: protein-evaluation
gene: "RCAN3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RCAN3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RCAN3 / -- |
| 蛋白全称 | Calcipressin-3 |
| 蛋白大小 | 241 aa |
| UniProt ID | Q9UKA8 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 241 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 41 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 4 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
|  | **原始总分** |  | **94/183** | **94.0/183** |  |  |  |
|  | **归一化总分** |  | **51.4/100** | **51.4/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RCAN3/IF_images/A-431_HPA064289_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RCAN3/IF_images/SK-MEL-30_HPA064289_2.jpg|SK-MEL-30]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 241 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 41 |

**评价**: PubMed 41 篇，高度新颖

**关键文献**:
1. Hu T et al. (2024). "RCAN family member 3 deficiency contributes to noncompaction of the ventricular myocardium". *J Genet Genomics*. PMID: 38181896
2. Liang Y et al. (2024). "Regulator of calcineurin 3 as a novel predictor of diagnosis and prognosis in pan-cancer". *Croat Med J*. PMID: 39219199
3. Park JS et al. (2017). "Regulator of Calcineurin 3 Ameliorates Autoimmune Arthritis by Suppressing Th17 Cell Differentiation". *Am J Pathol*. PMID: 28704638
4. Lui W-Y et al. (2024). "Nsp1 facilitates SARS-CoV-2 replication through calcineurin-NFAT signaling". *mBio*. PMID: 38411085
5. Batan S et al. (2023). "Inhibiting Anti-angiogenic VEGF165b Activates a Novel miR-17-20a-Calcipressin-3 Pathway that Revascularizes Ischemic Muscle in Peripheral Artery Disease". *Res Sq*. PMID: 37645966
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 241 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RCAN3/RCAN3-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Calcipressin |
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | RBD_domain_sf |
| Pfam | Calcipressin |

**染色质调控潜力分析**: 4 个已注释结构域，新颖蛋白基线水平

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
| 结构域 | UniProt/InterPro/Pfam | 4 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 41 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RCAN3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117602-RCAN3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RCAN3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9UKA8
- STRING: https://string-db.org/network/9606.ENSG00000117602
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKA8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[RCAN3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RCAN3/RCAN3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000117602-RCAN3/subcellular

![](https://images.proteinatlas.org/64289/1227_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/64289/1227_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/64289/1269_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/64289/1269_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/64289/1271_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/64289/1271_D12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKA8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006931;IPR012677;IPR035979; |
| Pfam | PF04847; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000117602-RCAN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRB10 | Intact, Biogrid | true |
| HTT | Intact | false |
| PPP3CA | Biogrid | false |
| PPP3CB | Biogrid | false |
| PPP3CC | Biogrid | false |
| PPP3R1 | Bioplex | false |
| PRDX6 | Bioplex | false |
| TNNI3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
