---
type: protein-evaluation
gene: "TELO2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TELO2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TELO2 / KIAA0683|hCLK2|TEL2 |
| 蛋白全称 | Telomere length regulation protein TEL2 homolog |
| 蛋白大小 | 837 aa |
| UniProt ID | Q9Y4R8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/TELO2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/TELO2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 8/10 | ×1 | **8** | 837 aa，尚可接受 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 62 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 7 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **101/183** | **100.0/183** |  |  |  |
|  | **归一化总分** |  | **55.2/100** | **54.6/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Cytoplasm, Membrane, Nucleus, Chromosome, telomere | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 837 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 62 |

**评价**: PubMed 62 篇，中等研究热度

**关键文献**:
1. Serey-Gaut M et al. (2023). "Bi-allelic TTI1 variants cause an autosomal-recessive neurodevelopmental disorder with microcephaly". *Am J Hum Genet*. PMID: 36724785
2. Kim Y et al. (2022). "Structure of the Human TELO2-TTI1-TTI2 Complex". *J Mol Biol*. PMID: 34838521
3. Cabezudo S et al. (2025). "Characterization of WAC interactions with R2TP and TTT chaperone complexes linking glucose and glutamine availability to mTORC1 activity". *FEBS Open Bio*. PMID: 40653822
4. Albokhari D et al. (2023). "TELO2-related syndrome (You-Hoover-Fong syndrome): Description of 14 new affected individuals and review of the literature". *Am J Med Genet A*. PMID: 36797513
5. Feng SW et al. (2023). "Exploring the Functional Roles of Telomere Maintenance 2 in the Tumorigenesis of Glioblastoma Multiforme and Drug Responsiveness to Temozolomide". *Int J Mol Sci*. PMID: 37298208
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 837 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/TELO2/TELO2-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ARM-type_fold |
| InterPro | TEL2_C_sf |
| InterPro | TEL2_Regulation |
| InterPro | TELO2_ARM |
| InterPro | Telomere_length_regulation_dom |
| Pfam | TELO2_ARM |
| Pfam | Telomere_reg-2 |

**染色质调控潜力分析**: 7 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:TTT Hsp90 cochaperone complex (GO:0110078, IPI:ComplexPortal)
- F:protein-containing complex binding (GO:0044877, IDA:MGI)
- F:protein-containing complex stabilizing activity (GO:0140777, IMP:MGI)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
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
1. 新颖性: PubMed 62 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TELO2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100726-TELO2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TELO2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y4R8
- STRING: https://string-db.org/network/9606.ENSG00000100726
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4R8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TELO2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/TELO2/TELO2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000100726-TELO2/subcellular

![](https://images.proteinatlas.org/41473/496_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41473/496_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41473/532_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41473/532_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41473/547_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41473/547_B11_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
