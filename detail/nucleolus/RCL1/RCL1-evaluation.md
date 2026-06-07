---
type: protein-evaluation
gene: "RCL1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RCL1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RCL1 / RPCL1|RNAC |
| 蛋白全称 | RNA 3'-terminal phosphate cyclase-like protein |
| 蛋白大小 | 373 aa |
| UniProt ID | Q9Y2P8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RCL1/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RCL1/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 10/10 | ×1 | **10** | 373 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 11 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **118.5/183** |  |
| **归一化总分** |  |  | **64.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 373 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |

**关键文献**:
1. Wang et al. (2022). "Maize RNA 3'-terminal phosphate cyclase-like protein promotes 18S pre-rRNA cleavage and is important for kernel development.". *Plant Cell*. PMID: 35167702
2. Wang et al. (2024). "Stability and function of RCL1 are dependent on the interaction with BMS1.". *J Mol Cell Biol*. PMID: 37451810
3. Wang et al. (2025). "Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes.". *medRxiv*. PMID: 40196253
4. Mokhtarian et al. (2020). "Evaluation of Gelatinolytic and Collagenolytic Activity of Fasciola hepatica Recombinant Cathepsin-L1.". *Iran J Biotechnol*. PMID: 32884958
5. Karbstein et al. (2005). "An essential GTPase promotes assembly of preribosomal RNA processing complexes.". *Mol Cell*. PMID: 16307926
**评价**: PubMed 28 篇，高度新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 373 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/RCL1/RCL1-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | RNA3'-term_phos_cycl_insert |
| InterPro | RNA3'_phos_cyclase_dom |
| InterPro | RNA3'_phos_cyclase_dom_sf |
| InterPro | RNA3'_term_phos_cyc |
| InterPro | RNA3'_term_phos_cyc_type_2 |
| InterPro | RNA3'_term_phos_cycl-like_CS |
| InterPro | RNA3'P_cycl/enolpyr_Trfase_a/b |
| InterPro | RPTC_insert |
| Pfam | RTC |
| Pfam | RTC_insert |
| PROSITE | RTC |

**染色质调控潜力分析**: 11 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| BFR2 | inferred by author | 16429126 | — | — |
| BEM2 | inferred by author | 16429126 | — | — |
| BMS1 | inferred by author | 16429126 | — | — |
| GOLGA2 | two hybrid array | 32296183 | — | — |
| EBI-20976612 | clash | 23622248 | — | — |


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
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 11 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 28 篇，高度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RCL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120158-RCL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RCL1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y2P8
- STRING: https://string-db.org/network/9606.ENSG00000120158
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2P8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[RCL1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/RCL1/RCL1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000120158-RCL1/subcellular

![](https://images.proteinatlas.org/71308/1357_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/71308/1357_A8_3_red_green.jpg)
![](https://images.proteinatlas.org/71308/1359_A8_6_red_green.jpg)
![](https://images.proteinatlas.org/71308/1359_A8_8_red_green.jpg)
![](https://images.proteinatlas.org/71308/1510_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/71308/1510_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y2P8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013791;IPR023797;IPR037136;IPR000228;IPR016443;IPR020719;IPR013792;IPR036553; |
| Pfam | PF01137;PF05189; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120158-RCL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BMS1 | Intact, Biogrid, Opencell, Bioplex | true |
| CDK9 | Biogrid | false |
| FKBP5 | Opencell | false |
| GOLGA2 | Intact | false |
| IFI16 | Biogrid | false |
| LMNB1 | Opencell | false |
| MYC | Biogrid | false |
| NPM1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
