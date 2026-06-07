---
type: protein-evaluation
gene: "CIAO2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CIAO2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIAO2B / CIAB, FAM96B, MIP18 |
| 蛋白名称 | Cytosolic iron-sulfur assembly component 2B |
| 蛋白大小 | 163 aa / 17.7 kDa |
| UniProt ID | Q9Y3D0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm, cytoskeleton, spindle; Midbody |
| 蛋白大小 | 8/10 | x1 | 8 | 163 aa / 17.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR034904, IPR039796, IPR002744; Pfam: PF01883 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, spindle; Midbody | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- cytosolic [4Fe-4S] assembly targeting complex (GO:0097361)
- midbody (GO:0030496)
- MMXD complex (GO:0071817)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CIAB, FAM96B, MIP18 |

**关键文献**:
1. Iron-regulated assembly of the cytosolic iron-sulfur cluster biogenesis machinery.. *The Journal of biological chemistry*. PMID: 35654137
2. Structural insights into Fe-S protein biogenesis by the CIA targeting complex.. *Nature structural & molecular biology*. PMID: 32632277
3. Crosstalk of Brucella abortus nucleomodulin BspG and host DNA replication process/mitochondrial respiratory pathway promote anti-apoptosis and infection.. *Veterinary microbiology*. PMID: 35395545
4. The critical role of the iron-sulfur cluster and CTC components in DOG-1/BRIP1 function in Caenorhabditis elegans.. *Nucleic acids research*. PMID: 39011897

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 46.6% |
| 置信残基 (pLDDT 70-90) 占比 | 44.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 90.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034904, IPR039796, IPR002744; Pfam: PF01883 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MMS19 | 0.999 | 0.984 | — |
| CIAO1 | 0.999 | 0.994 | — |
| SLC25A5 | 0.994 | 0.000 | — |
| CIAO3 | 0.994 | 0.584 | — |
| ERCC2 | 0.989 | 0.720 | — |
| CIAO2A | 0.965 | 0.359 | — |
| SLC25A6 | 0.960 | 0.292 | — |
| RTEL1 | 0.900 | 0.555 | — |
| NUBP1 | 0.894 | 0.075 | — |
| FBXL5 | 0.879 | 0.796 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CIAO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MLF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| purH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| LRRC59 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, spindle; Midbody / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CIAO2B -- Cytosolic iron-sulfur assembly component 2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小163 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3D0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166595-CIAO2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIAO2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3D0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000166595-CIAO2B/subcellular

![](https://images.proteinatlas.org/41501/485_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/41501/485_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/41501/488_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/41501/488_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3D0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3D0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034904;IPR039796;IPR002744; |
| Pfam | PF01883; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166595-CIAO2B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CIAO1 | Intact, Biogrid | true |
| DNA2 | Biogrid, Bioplex | true |
| ERCC2 | Intact, Biogrid | true |
| MMS19 | Intact, Biogrid, Bioplex | true |
| POLD1 | Intact, Biogrid | true |
| CASP6 | Intact | false |
| CCK | Intact | false |
| CDKAL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
