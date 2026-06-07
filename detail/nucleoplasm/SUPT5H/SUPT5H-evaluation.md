---
type: protein-evaluation
gene: "SUPT5H"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT5H 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SUPT5H / SPT5H|SPT5|FLJ34157 |
| 蛋白全称 | Transcription elongation factor SPT5 |
| 蛋白大小 | 1087 aa |
| UniProt ID | O00267 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1087 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 28 篇，高度新颖 |
| 三维结构 | 10/10 | ×3 | **30** | 43 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 32 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
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
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUPT5H/IF_images/A-431_HPA029273_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUPT5H/IF_images/U-251MG_HPA029273_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 1087 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 28 |

**评价**: PubMed 28 篇，高度新颖

**关键文献**:
1. Harteveld CL et al. (2022). "The hemoglobinopathies, molecular disease mechanisms and diagnostics". *Int J Lab Hematol*. PMID: 36074711
2. Harteveld CL et al. (2024). "Loss-of-Function Variants in SUPT5H as Modifying Factors in Beta-Thalassemia". *Int J Mol Sci*. PMID: 39201615
3. Lin Z et al. (2024). "SUPT5H mutations associated with elevation of Hb A(2) level: Identification of two novel variants and literature review". *Gene*. PMID: 38373659
4. Martell DJ et al. (2023). "RNA polymerase II pausing temporally coordinates cell cycle progression and erythroid differentiation". *Dev Cell*. PMID: 37586368
5. Chiang PW et al. (1996). "Isolation, sequencing, and mapping of the human homologue of the yeast transcription factor, SPT5". *Genomics*. PMID: 8975720
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1087 aa |
| PDB 条数 | 43 |
| 已注释结构域 | 32 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUPT5H/SUPT5H-PAE.png]]

**评价**: 43 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | KOW |
| InterPro | KOW_Spt5_1 |
| InterPro | KOW_Spt5_2 |
| InterPro | KOW_Spt5_3 |
| InterPro | KOW_Spt5_4 |
| InterPro | KOW_Spt5_5 |
| InterPro | KOW_Spt5_6_metazoa |
| InterPro | KOW_Spt5_7 |
| InterPro | KOWx_Spt5 |
| InterPro | NGN-domain |
| InterPro | NGN-like_dom |
| InterPro | NGN_dom_sf |
| InterPro | NGN_Euk |
| InterPro | Rib_uL2_dom2 |
| InterPro | SPT5 |

**染色质调控潜力分析**: 32 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:DSIF complex (GO:0032044, IDA:UniProtKB)
- F:chromatin binding (GO:0003682, IEA:Ensembl)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 43 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 32 个 | 多库一致 |
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
1. 新颖性: PubMed 28 篇，高度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 43 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SUPT5H
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196235-SUPT5H
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SUPT5H%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O00267
- STRING: https://string-db.org/network/9606.ENSG00000196235
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00267


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SUPT5H-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SUPT5H/SUPT5H-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000196235-SUPT5H/subcellular

![](https://images.proteinatlas.org/29273/295_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/29273/295_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/29273/296_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/29273/296_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/29273/297_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/29273/297_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00267 |
| SMART | SM01104;SM00739;SM00738; |
| UniProt Domain [FT] | DOMAIN 273..306; /note="KOW 1"; DOMAIN 420..451; /note="KOW 2"; DOMAIN 472..503; /note="KOW 3"; DOMAIN 594..627; /note="KOW 4"; DOMAIN 704..737; /note="KOW 5" |
| InterPro | IPR005824;IPR041973;IPR041975;IPR041976;IPR041977;IPR041978;IPR041980;IPR057934;IPR057936;IPR005100;IPR006645;IPR036735;IPR039385;IPR014722;IPR039659;IPR024945;IPR022581;IPR017071;IPR008991; |
| Pfam | PF00467;PF23042;PF23284;PF23291;PF23290;PF23288;PF23287;PF23037;PF03439;PF11942; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196235-SUPT5H/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC73 | Biogrid, Opencell | true |
| CPSF6 | Biogrid, Opencell | true |
| CRNKL1 | Biogrid, Opencell | true |
| CSNK2A1 | Biogrid, Opencell | true |
| CSNK2A2 | Biogrid, Opencell | true |
| CT45A5 | Biogrid, Opencell | true |
| CTR9 | Biogrid, Opencell | true |
| GOLGA2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
