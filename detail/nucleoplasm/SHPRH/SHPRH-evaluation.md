---
type: protein-evaluation
gene: "SHPRH"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHPRH 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SHPRH / FLJ90837|KIAA2023|bA545I5.2 |
| 蛋白全称 | E3 ubiquitin-protein ligase SHPRH |
| 蛋白大小 | 1683 aa |
| UniProt ID | Q149N8 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 5/10 | ×1 | **5** | 1683 aa, small/large |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 53 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: histone_h1/h5_h15, linker_histone, p-loop_ntpase, phd, zf |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **101.5/183** |  |
| **归一化总分** |  |  | **55.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SHPRH/IF_images/HEK293_HPA044852_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SHPRH/IF_images/Rh30_HPA044852_2.jpg|Rh30]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 1683 aa， small/large

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 53 |

**评价**: PubMed 53 篇，中等研究热度

**关键文献**:
1. Chang S et al. (2024). "Therapeutic SHPRH-146aa encoded by circ-SHPRH dynamically upregulates P21 to inhibit CDKs in neuroblastoma". *Cancer Lett*. PMID: 39002691
2. Ju X et al. (2021). "The Emerging Role of Circ-SHPRH in Cancer". *Onco Targets Ther*. PMID: 34285509
3. Xiong H et al. (2023). "Circ-SHPRH in human cancers: a systematic review and meta-analysis". *Front Cell Dev Biol*. PMID: 37305675
4. Lu Y et al. (2021). "Translation role of circRNAs in cancers". *J Clin Lab Anal*. PMID: 34097315
5. Wang J et al. (2019). "ncRNA-Encoded Peptides or Proteins and Cancer". *Mol Ther*. PMID: 31526596
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1683 aa |
| PDB 条数 | 2 |
| 已注释结构域 | 36 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SHPRH/SHPRH-PAE.png]]

**评价**: 2 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ATP-helicase/E3_Ub-Ligase |
| InterPro | Helicase_ATP-bd |
| InterPro | Helicase_C-like |
| InterPro | Histone_H1/H5_H15 |
| InterPro | P-loop_NTPase |
| InterPro | SHPRH_helical_1st |
| InterPro | SHPRH_helical_2nd |
| InterPro | SNF2-like_sf |
| InterPro | SNF2/RAD54-like_C |
| InterPro | SNF2_N |
| InterPro | WH-like_DNA-bd_sf |
| InterPro | WH_DNA-bd_sf |
| InterPro | Zinc_finger_PHD-type_CS |
| InterPro | Znf-RING_euk |
| InterPro | Znf_FYVE_PHD |

**染色质调控潜力分析**: 染色质/DNA 结构域: histone_h1/h5_h15, linker_histone, p-loop_ntpase, phd, zf_phd_1

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:nucleosome (GO:0000786, IEA:InterPro)
- P:nucleosome assembly (GO:0006334, IEA:InterPro)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 2 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 36 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 53 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 2 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SHPRH
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146414-SHPRH
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHPRH%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q149N8
- STRING: https://string-db.org/network/9606.ENSG00000146414
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q149N8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SHPRH-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SHPRH/SHPRH-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000146414-SHPRH/subcellular

![](https://images.proteinatlas.org/44852/1466_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/44852/1466_A5_5_red_green.jpg)
![](https://images.proteinatlas.org/44852/1494_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/44852/1494_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/44852/1521_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/44852/1521_A5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q149N8 |
| SMART | SM00487;SM00526;SM00490;SM00249;SM00184; |
| UniProt Domain [FT] | DOMAIN 307..389; /note="Helicase ATP-binding; first part"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 438..512; /note="H15"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00837"; DOMAIN 710..868; /note="Helicase ATP-binding; second part"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 1514..1672; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR052583;IPR014001;IPR001650;IPR005818;IPR027417;IPR048686;IPR048695;IPR038718;IPR049730;IPR000330;IPR036388;IPR036390;IPR019786;IPR027370;IPR011011;IPR001965;IPR001841;IPR013083;IPR017907; |
| Pfam | PF00271;PF00538;PF21325;PF21324;PF00176;PF13445; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146414-SHPRH/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RBBP4 | Biogrid, Opencell | true |
| BORCS6 | Intact | false |
| DTL | Biogrid | false |
| EDARADD | Intact | false |
| FKBP5 | Opencell | false |
| H3C1 | Biogrid | false |
| H4C1 | Biogrid | false |
| HSPA9 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
