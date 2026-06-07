---
type: protein-evaluation
gene: "STAMBP"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STAMBP 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | STAMBP / AMSH |
| 蛋白全称 | STAM-binding protein |
| 蛋白大小 | 424 aa |
| UniProt ID | O95630 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/STAMBP/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/STAMBP/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 424 aa，处于理想范围 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 82 篇，中等研究热度 |
| 三维结构 | 10/10 | ×3 | **30** | 5 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 8 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **99/183** | **98.0/183** |  |  |  |
|  | **归一化总分** |  | **54.1/100** | **53.6/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Membrane, Cytoplasm, Early endosome | 实验证据/预测 |
| GO-CC | GO:0005634 | IDA|IEA |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 424 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 82 |

**评价**: PubMed 82 篇，中等研究热度

**关键文献**:
1. Adam MP et al. (1993). "Microcephaly-Capillary Malformation Syndrome". **. PMID: 24354023
2. Zhang W et al. (2024). "Identification of STAM-binding protein as a target for the treatment of gemcitabine resistance pancreatic cancer in a nutrient-poor microenvironment". *Cell Death Dis*. PMID: 39242557
3. Hu M et al. (2024). "AAV-mediated Stambp gene replacement therapy rescues neurological defects in a mouse model of microcephaly-capillary malformation syndrome". *Mol Ther*. PMID: 39169623
4. Yu S et al. (2022). "STAM binding protein regulated by hsa_circ_0007334 exerts oncogenic potential in pancreatic cancer". *Pancreatology*. PMID: 36089485
5. Iwakami Y et al. (2018). "STAM-binding protein regulates melanoma metastasis through SLUG stabilization". *Biochem Biophys Res Commun*. PMID: 30454887
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 424 aa |
| PDB 条数 | 5 |
| 已注释结构域 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/STAMBP/STAMBP-PAE.png]]

**评价**: 5 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | JAMM/MPN+_dom |
| InterPro | MPN |
| InterPro | STAMBP/STALP-like_MPN |
| InterPro | USP8_dimer |
| Pfam | JAB |
| Pfam | USP8_dimer |
| SMART | JAB_MPN |
| PROSITE | MPN |

**染色质调控潜力分析**: 8 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| RNF11 | two hybrid | 14755250 | — | — |
| GRAP2 | two hybrid pooling approach | 16189514 | — | — |
| STAM2 | two hybrid pooling approach | 16189514 | — | — |
| RECQL5 | two hybrid pooling approach | 16169070 | — | — |
| CHMP5 | two hybrid | 21988832 | — | — |
| CHMP1B | two hybrid | 21988832 | — | — |
| CHMP1A | two hybrid | 21988832 | — | — |
| CYP2C9 | two hybrid array | 21988832 | — | — |
| SPG7 | two hybrid array | 21988832 | — | — |
| ITGA5 | two hybrid array | 21988832 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 5 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 8 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 82 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 5 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=STAMBP
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124356-STAMBP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22STAMBP%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O95630
- STRING: https://string-db.org/network/9606.ENSG00000124356
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95630


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[STAMBP-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/STAMBP/STAMBP-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000124356-STAMBP/subcellular

![](https://images.proteinatlas.org/35800/380_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/35800/380_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/35800/382_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/35800/382_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/35800/397_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/35800/397_E5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95630 |
| SMART | SM00232; |
| UniProt Domain [FT] | DOMAIN 257..388; /note="MPN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01182" |
| InterPro | IPR000555;IPR037518;IPR044098;IPR015063; |
| Pfam | PF01398;PF08969; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124356-STAMBP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHMP1A | Intact, Biogrid | true |
| CHMP1B | Intact, Biogrid | true |
| CHMP2A | Intact, Biogrid | true |
| CHMP3 | Intact, Biogrid | true |
| CHMP4A | Intact, Biogrid | true |
| CHMP4B | Intact, Biogrid | true |
| GRAP2 | Intact, Biogrid, Bioplex | true |
| GRB2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
