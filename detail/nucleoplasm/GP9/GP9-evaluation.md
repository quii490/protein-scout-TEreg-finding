---
type: protein-evaluation
gene: "GP9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GP9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GP9 |
| 蛋白名称 | Platelet glycoprotein IX |
| 蛋白大小 | 177 aa / 19.0 kDa |
| UniProt ID | P14770 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 177 aa / 19.0 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=97 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.7; PDB: 3REZ, 8WFS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000483, IPR052313, IPR001611, IPR032675, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- glycoprotein Ib-IX-V complex (GO:1990779)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 97 |
| PubMed broad count | 152 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mendelian randomization analysis identifies druggable genes and drugs repurposing for chronic obstructive pulmonary disease.. *Frontiers in cellular and infection microbiology*. PMID: 38660492
2. Plasma protein N-glycome composition associates with postprandial lipaemic response.. *BMC medicine*. PMID: 37400796
3. A large deletion in the GP9 gene in Cocker Spaniel dogs with Bernard-Soulier syndrome.. *PloS one*. PMID: 31484196
4. Membrane insertion and assembly of epitope-tagged gp9 at the tip of the M13 phage.. *BMC microbiology*. PMID: 21943062
5. Lentiviral gene therapy reverts GPIX expression and phenotype in Bernard-Soulier syndrome type C.. *Molecular therapy. Nucleic acids*. PMID: 37416759

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 61.0% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 18.1% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 3REZ, 8WFS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3REZ, 8WFS）+ AlphaFold高质量预测（pLDDT=84.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000483, IPR052313, IPR001611, IPR032675, IPR000372; Pfam: PF13855, PF01462 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GP1BB | 0.999 | 0.292 | — |
| GP5 | 0.999 | 0.292 | — |
| GP1BA | 0.999 | 0.783 | — |
| VWF | 0.998 | 0.100 | — |
| ITGA2B | 0.980 | 0.050 | — |
| LYN | 0.919 | 0.100 | — |
| GTPBP1 | 0.918 | 0.000 | — |
| ITGB3 | 0.888 | 0.057 | — |
| GP6 | 0.860 | 0.095 | — |
| CD36 | 0.859 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| APPBP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| SPRY2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| GP1BA | psi-mi:"MI:0227"(reverse phase chromatography) | pubmed:18674540|imex:IM-24276 |
| GP5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-24277|pubmed:1730602 |
| GP1BB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-24277|pubmed:1730602 |
| NUDT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TNFSF14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAD21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 3REZ, 8WFS | pLDDT=84.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. GP9 — Platelet glycoprotein IX，研究基础较多，新颖性有限。
2. 蛋白大小177 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 97 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P14770
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169704-GP9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GP9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P14770
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000169704-GP9/subcellular

![](https://images.proteinatlas.org/63182/1770_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63182/1770_D3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/63182/1944_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63182/1944_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/63182/1953_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/63182/1953_A2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P14770-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P14770 |
| SMART | SM00082;SM00013; |
| UniProt Domain [FT] | DOMAIN 17..51; /note="LRRNT"; DOMAIN 85..137; /note="LRRCT" |
| InterPro | IPR000483;IPR052313;IPR001611;IPR032675;IPR000372; |
| Pfam | PF13855;PF01462; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169704-GP9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABHD3 | Bioplex | false |
| ADGRF1 | Bioplex | false |
| AGPAT2 | Bioplex | false |
| ALG11 | Bioplex | false |
| APPBP2 | Intact | false |
| ATP13A3 | Bioplex | false |
| BSCL2 | Bioplex | false |
| DHRS7B | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
