---
type: protein-evaluation
gene: "THAP4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THAP4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | THAP4 / CGI-36|Nb(III) |
| 蛋白全称 | Peroxynitrite isomerase THAP4 |
| 蛋白大小 | 577 aa |
| UniProt ID | Q8WY91 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/THAP4/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/THAP4/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 577 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 10 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 10 个已注释结构域 |
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
| UniProt | Cytoplasm, Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 577 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 10 |

**评价**: PubMed 10 篇，极度新颖

**关键文献**:
1. De Simone G et al. (2020). "Mycobacterial and Human Nitrobindins: Structure and Function". *Antioxid Redox Signal*. PMID: 32295384
2. Homann J et al. (2025). "Redefining ALS: Large-scale proteomic profiling reveals a prolonged pre-diagnostic phase with immune, muscular, metabolic, and brain involvement". *Res Sq*. PMID: 40951286
3. Homann J et al. (2025). "Redefining ALS: Large-scale proteomic profiling reveals a prolonged pre-diagnostic phase with immune, muscular, metabolic, and brain involvement". *medRxiv*. PMID: 40909834
4. Katayama K et al. (2024). "Mutation of the Thap4 gene causes dwarfism and testicular anomalies in rats and mice". *Mamm Genome*. PMID: 38658415
5. Yu Q et al. (2025). "Prenatal trio-based whole exome sequencing in fetuses with congenital pulmonary airway malformation". *Transl Pediatr*. PMID: 40949908
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 577 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 10 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/THAP4/THAP4-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Calycin |
| InterPro | Nitrobindin |
| InterPro | THAP4-like_heme-bd |
| InterPro | THAP_Znf |
| InterPro | THAP_Znf_sf |
| Pfam | THAP |
| Pfam | THAP4_heme-bd |
| SMART | DM3 |
| SMART | THAP |
| PROSITE | ZF_THAP |

**染色质调控潜力分析**: 10 个已注释结构域，新颖蛋白基线水平

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
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 10 个 | 多库一致 |
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
1. 新颖性: PubMed 10 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=THAP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176946-THAP4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22THAP4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8WY91
- STRING: https://string-db.org/network/9606.ENSG00000176946
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WY91


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[THAP4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/THAP4/THAP4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000176946-THAP4/subcellular

![](https://images.proteinatlas.org/44982/526_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/44982/526_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/44982/528_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/44982/528_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/44982/545_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/44982/545_D1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WY91 |
| SMART | SM00692;SM00980; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012674;IPR045165;IPR014878;IPR006612;IPR038441; |
| Pfam | PF05485;PF08768; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176946-THAP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CPNE2 | Intact, Biogrid, Bioplex | true |
| ALOX12B | Bioplex | false |
| AMD1 | Intact | false |
| BSND | Intact | false |
| CACNG1 | Intact | false |
| CD81 | Intact | false |
| CMTM7 | Intact | false |
| CST6 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
