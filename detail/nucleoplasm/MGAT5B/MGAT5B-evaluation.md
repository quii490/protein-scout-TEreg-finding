---
type: protein-evaluation
gene: "MGAT5B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MGAT5B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MGAT5B / KIAA2008 |
| 蛋白名称 | Alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B |
| 蛋白大小 | 792 aa / 89.5 kDa |
| UniProt ID | Q3V5L5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitotic spindle; 额外: Cytokinetic bridge; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 792 aa / 89.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026116, IPR052105; Pfam: PF15024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitotic spindle; 额外: Cytokinetic bridge | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA2008 |

**关键文献**:
1. Epigenetic Regulation of Glycosylation.. *Advances in experimental medicine and biology*. PMID: 34495535
2. Genomic analysis of 116 autism families strengthens known risk genes and highlights promising candidates.. *NPJ genomic medicine*. PMID: 38519481
3. Regulation of intracellular activity of N-glycan branching enzymes in mammals.. *The Journal of biological chemistry*. PMID: 38879010
4. Pathological discrimination between luteinized thecoma associated with sclerosing peritonitis and thecoma.. *Medicine*. PMID: 37335673
5. Integrative Machine Learning Approach to Explore Glycosylation Signatures and Immune Landscape in Moyamoya Disease.. *Bioinformatics and biology insights*. PMID: 40416061

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.0 |
| 高置信度残基 (pLDDT>90) 占比 | 60.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 13.9% |
| 有序区域 (pLDDT>70) 占比 | 77.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.0，有序区 77.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026116, IPR052105; Pfam: PF15024 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MGAT4B | 0.992 | 0.000 | — |
| MGAT4A | 0.990 | 0.000 | — |
| POMGNT1 | 0.983 | 0.000 | — |
| MGAT4C | 0.950 | 0.045 | — |
| B4GALT2 | 0.942 | 0.000 | — |
| B4GALT3 | 0.941 | 0.000 | — |
| B4GALT1 | 0.940 | 0.000 | — |
| MGAT4D | 0.911 | 0.045 | — |
| MGAT5 | 0.910 | 0.000 | — |
| MGAT3 | 0.812 | 0.056 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |
| VAC14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| KRTAP26-1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ABHD18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PITX1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| PLEKHM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HUNK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| NTAN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.0 + PDB: 无 | pLDDT=82.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Mitotic spindle; 额外: Cytokinetic brid | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MGAT5B — Alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B，非常新颖，仅有少数基础研究。
2. 蛋白大小792 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PITX1 | BioGRID | 0 |
| CAMK2B | BioGRID | 0 |
| HOXA1 | BioGRID | 0 |
| MDFI | BioGRID | 0 |
| OTX1 | BioGRID | 0 |
| PLSCR1 | BioGRID | 0 |
| PTGER3 | BioGRID | 0 |
| STK16 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

MGAT5B（UniProt Q3V5L5）含有一个特征性催化结构域PF15024，属于糖基转移酶家族GT-B超家族，通过InterPro条目IPR026116和IPR052105注释。AlphaFold v6预测的整体结构pLDDT平均值为82.0，有序区域（pLDDT>70）占比77.8%，表明其N端催化核心折叠相对可信，但C端存在约14%低置信无序区（pLDDT<50），提示该区域可能具有固有无序特性，为底物识别或蛋白间互作提供构象柔性。目前尚无实验解析的PDB结构，因此关键催化残基的精确定位及底物结合口袋构象仍依赖AlphaFold预测模型。

STRING-PPI网络分析显示MGAT5B与N-糖链分支酶MGAT4B（combined score=0.992）、MGAT4A（0.990）、POMGNT1（0.983）高度共现，提示其在高尔基体N-糖基化通路中处于核心节点位置。然而，IntAct实验互作网络揭示了另一重功能面：MGAT5B与转录因子PITX1（PMID:24722188）和HOXA1（PMID:23088713）存在酵母双杂交验证的直接物理互作。这种糖基转移酶与转录因子的非经典PPI模式暗示MGAT5B可能通过糖基化修饰转录因子活性或在高尔基体-细胞核信号转导中扮演桥梁角色，类似OGT对转录因子的O-GlcNAc修饰机制。

HPA免疫荧光将MGAT5B定位于核质（nucleoplasm, approved）和有丝分裂纺锤体，与UniProt注释的高尔基体膜定位存在明显分歧。这种双重定位与糖基化酶在细胞器定位之外行使非经典功能的文献报道相符（PMID:34495535，糖基化的表观遗传调控），暗示MGAT5B可能在核质中通过糖基化修饰核蛋白或参与有丝分裂期间的细胞器重新分布。

MGAT5B功能机制的整合假说为：在Golgi膜上催化N-糖链的beta1,6-GlcNAc分支形成，而在细胞分裂或特定应激条件下，部分蛋白易位至核质和纺锤体，可能通过糖基化修饰影响染色体相关蛋白或纺锤体组装因子。考虑到其与PITX1/HOXA1的直接互作及核质定位证据，MGAT5B可能构成糖基化修饰与转录调控之间的交叉调控节点，但其在核内的具体底物谱和生物学意义尚需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3V5L5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167889-MGAT5B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MGAT5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3V5L5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000167889-MGAT5B/subcellular

![](https://images.proteinatlas.org/11082/1584_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/11082/1584_C4_6_red_green.jpg)
![](https://images.proteinatlas.org/11082/1637_E6_31_red_green.jpg)
![](https://images.proteinatlas.org/11082/1637_E6_32_red_green.jpg)
![](https://images.proteinatlas.org/11082/1784_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/11082/1784_A4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3V5L5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3V5L5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026116;IPR052105; |
| Pfam | PF15024; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167889-MGAT5B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PITX1 | Biogrid | false |
| VAC14 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
