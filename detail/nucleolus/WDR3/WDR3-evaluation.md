---
type: protein-evaluation
gene: "WDR3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | WDR3 / FLJ12796|UTP12|DIP2 |
| 蛋白全称 | WD repeat-containing protein 3 |
| 蛋白大小 | 943 aa |
| UniProt ID | Q9UNX4 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/WDR3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/WDR3/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 8/10 | ×1 | **8** | 943 aa，尚可接受 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 32 篇，高度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 14 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **116.5/183** |  |
| **归一化总分** |  |  | **63.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, nucleolus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 943 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 32 |

**评价**: PubMed 32 篇，高度新颖

**关键文献**:
1. Li M et al. (2025). "WDR3 undergoes phase separation to mediate the therapeutic mechanism of Nilotinib against osteosarcoma". *J Exp Clin Cancer Res*. PMID: 40646517
2. Kobayashi-Tanabe M et al. (2023). "Characterization of a WD-repeat family protein WDR3 in the brain of WDR3 hetero knockout mice". *Brain Res*. PMID: 36463953
3. Chi X et al. (2023). "RRP9 and DDX21 as new biomarkers of colorectal cancer". *Medicine (Baltimore)*. PMID: 37904456
4. Liu W et al. (2023). "WDR3 promotes stem cell-like properties in prostate cancer by inhibiting USF2-mediated transcription of RASSF1A". *J Gene Med*. PMID: 36905106
5. Kobayashi M et al. (2018). "Association studies of WD repeat domain 3 and chitobiosyldiphosphodolichol beta-mannosyltransferase genes with schizophrenia in a Japanese population". *PLoS One*. PMID: 29309433
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 943 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 14 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/WDR3/WDR3-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SSU_processome_Utp12 |
| InterPro | TBC1_cilium_biogenesis |
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_PAC1 |
| InterPro | WD40_repeat_CS |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| Pfam | Beta-prop_WDR3_1st |
| Pfam | Beta-prop_WDR3_2nd |
| Pfam | Utp12 |
| SMART | WD40 |
| PROSITE | WD_REPEATS_1 |
| PROSITE | WD_REPEATS_2 |
| PROSITE | WD_REPEATS_REGION |

**染色质调控潜力分析**: 14 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| PDE10A | two hybrid pooling approach | 16169070 | — | — |
| ENO4 | cross-linking study | 30021884 | — | — |
| RPL4 | anti tag coimmunoprecipitation | 33961781 | — | — |
| HSPA13 | two hybrid fragment pooling approach | 35914814 | — | — |
| EBI-25591227 | clash | 23622248 | — | — |
| EBI-54261855 | clash | 23622248 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:Pwp2p-containing subcomplex of 90S preribosome (GO:0034388, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 14 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 32 篇，高度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=WDR3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065183-WDR3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22WDR3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9UNX4
- STRING: https://string-db.org/network/9606.ENSG00000065183
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNX4


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[WDR3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/WDR3/WDR3-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000065183-WDR3/subcellular

![](https://images.proteinatlas.org/27509/231_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27509/231_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27509/232_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27509/232_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/54354/834_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54354/834_D7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UNX4 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007148;IPR051570;IPR015943;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF25173;PF25172;PF04003; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000065183-WDR3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NPM1 | Biogrid, Opencell | true |
| TBL3 | Biogrid, Opencell | true |
| ANKRD26 | Opencell | false |
| CLNS1A | Opencell | false |
| COPS6 | Opencell | false |
| EIF4E | Opencell | false |
| EXOSC4 | Bioplex | false |
| FBL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
