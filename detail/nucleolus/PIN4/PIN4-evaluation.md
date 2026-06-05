---
type: protein-evaluation
gene: "PIN4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PIN4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PIN4 / PAR14|PAR17|EPVH |
| 蛋白全称 | Peptidyl-prolyl cis-trans isomerase NIMA-interacting 4 |
| 蛋白大小 | 131 aa |
| UniProt ID | Q9Y237 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PIN4/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PIN4/IF_images/Hep-G2_1.jpg|Hep-G2]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 8/10 | ×1 | **8** | 131 aa，尚可接受 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed 86 篇，中等研究热度 |
| 三维结构 | 10/10 | ×3 | **30** | 5 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 5 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **84.5/183** | **84.0/183** |  |  |
|  | **归一化总分** |  | **46.2/100** | **45.9/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, nucleolus, Cytoplasm, cytoskeleton, spindle, Cytoplasm, Mitochondrion, Mitochondrion matrix | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 131 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 86 |

**关键文献**:
1. Inoue et al. (2025). "Prolyl isomerase Pin4 impacts estrogen receptor transactivation by enhancing phosphorylation and consequently promotes the proliferation of breast cancer cells.". *Biochim Biophys Acta Mol Cell Res*. PMID: 40796046
2. Berdion et al. (2025). "Enhanced auxin signaling promotes root-hair growth at moderately low temperature in Arabidopsis thaliana.". *Plant Commun*. PMID: 40336200
3. Saeed et al. (2023). "PIN1 and PIN4 inhibition via parvulin impeders Juglone, PiB, ATRA, 6,7,4'-THIF, KPT6566, and EGCG thwarted hepatitis B virus replication.". *Front Microbiol*. PMID: 36760500
4. Unknown et al. (2018). "FGFR3-TACC3 Activates Mitochondrial Respiration via PIN4 Phosphorylation.". *Cancer Discov*. PMID: 29330265
5. Liang et al. (2024). "PIN4 could function as a prognostic biomarker for glioma.". *Asian J Surg*. PMID: 39645496
**评价**: PubMed 86 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 131 aa |
| PDB 条数 | 5 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/PIN4/PIN4-PAE.png]]

**评价**: 5 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PIN4 |
| InterPro | PPIase_dom_sf |
| InterPro | PPIase_PpiC |
| Pfam | Rotamase_3 |
| PROSITE | PPIC_PPIASE_2 |

**染色质调控潜力分析**: 5 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ASCC2 | two hybrid pooling approach | 16169070 | — | — |
| EZH2 | two hybrid pooling approach | 16169070 | — | — |
| DNM1 | two hybrid pooling approach | 16169070 | — | — |
| SPTAN1 | two hybrid pooling approach | 16169070 | — | — |
| MPG | anti bait coimmunoprecipitation | 17353931 | — | — |
| EPB41 | anti bait coimmunoprecipitation | 17353931 | — | — |
| EGFR | ubiquitin reconstruction | 20029029 | — | — |
| CHST15 | anti tag coimmunoprecipitation | 28514442 | — | — |
| ERBB2 | ubiquitin reconstruction | 31980649 | — | — |
| ERBB3 | ubiquitin reconstruction | 31980649 | — | — |


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
| 三维结构 | AlphaFold + PDB | 5 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 86 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 5 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PIN4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102309-PIN4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PIN4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y237
- STRING: https://string-db.org/network/9606.ENSG00000102309
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y237


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PIN4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/PIN4/PIN4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000102309-PIN4/subcellular

![](https://images.proteinatlas.org/54483/1334_B10_4_red_green.jpg)
![](https://images.proteinatlas.org/54483/1334_B10_7_red_green.jpg)
![](https://images.proteinatlas.org/54483/1887_G1_5_red_green.jpg)
![](https://images.proteinatlas.org/54483/1887_G1_9_red_green.jpg)
![](https://images.proteinatlas.org/54483/870_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/54483/870_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
