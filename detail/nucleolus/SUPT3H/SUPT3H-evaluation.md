---
type: protein-evaluation
gene: "SUPT3H"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT3H 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SUPT3H / SPT3|SPT3L |
| 蛋白全称 | Transcription initiation protein SPT3 homolog |
| 蛋白大小 | 317 aa |
| UniProt ID | O75486 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT3H/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT3H/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 317 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 25 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: histone-fold |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **133/183** |  |
| **归一化总分** |  |  | **72.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 317 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 25 |

**评价**: PubMed 25 篇，高度新颖

**关键文献**:
1. Fischer V et al. (2022). "SUPT3H-less SAGA coactivator can assemble and function without significantly perturbing RNA polymerase II transcription in mammalian cells". *Nucleic Acids Res*. PMID: 35871303
2. Bonakdari H et al. (2022). "Single nucleotide polymorphism genes and mitochondrial DNA haplogroups as biomarkers for early prediction of knee osteoarthritis structural progressors: use of supervised machine learning classifiers". *BMC Med*. PMID: 36089590
3. Barutcu AR et al. (2014). "The bone-specific Runx2-P1 promoter displays conserved three-dimensional chromatin structure with the syntenic Supt3h promoter". *Nucleic Acids Res*. PMID: 25120271
4. Springer Berlin Heidelberg (2020). "Editors' Note to: EDAR, LYPLAL1, PRDM16, PAX3, DKK1, TNFSF12, CACNA2D3, and SUPT3H gene variants influence facial morphology in a Eurasian population". *Hum Genet*. PMID: 31807863
5. Zhang K et al. (2024). "Significant Prognostic Factor at Age Cut-off of 73 Years for Advanced Ovarian Serous Cystadenocarcinoma Patients: Insights from Real-World Study". *Int J Womens Health*. PMID: 38332982
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 317 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT3H/SUPT3H-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Histone-fold |
| InterPro | TFIID_TAF13 |
| Pfam | TFIID-18kDa |

**染色质调控潜力分析**: 染色质/DNA 结构域: histone-fold

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| EBI-25684183 | clash | 23622248 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:SAGA complex (GO:0000124, IDA:UniProtKB)
- C:transcription factor TFTC complex (GO:0033276, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 25 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SUPT3H
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196284-SUPT3H
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SUPT3H%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O75486
- STRING: https://string-db.org/network/9606.ENSG00000196284
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75486


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SUPT3H-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/SUPT3H/SUPT3H-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000196284-SUPT3H/subcellular

![](https://images.proteinatlas.org/24371/224_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/24371/224_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/24371/226_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/24371/226_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/24371/261_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/24371/261_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75486 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009072;IPR003195; |
| Pfam | PF02269; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196284-SUPT3H/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SF3B3 | Biogrid, Opencell | true |
| SF3B5 | Biogrid, Opencell | true |
| TAF12 | Biogrid, Opencell | true |
| TRRAP | Biogrid, Opencell | true |
| USP22 | Biogrid, Opencell | true |
| ATXN7 | Biogrid | false |
| ATXN7L3 | Biogrid | false |
| DDB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
