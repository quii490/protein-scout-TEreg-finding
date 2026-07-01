---
type: protein-evaluation
gene: "CCDC183"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC183 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC183 / KIAA1984 |
| 蛋白名称 | Coiled-coil domain-containing protein 183 |
| 蛋白大小 | 534 aa / 62.7 kDa |
| UniProt ID | Q5T5S1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Primary cilium tip, Mid piece; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 534 aa / 62.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043247 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Primary cilium tip, Mid piece | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1984 |

**关键文献**:
1. Genomic Markers for Essential Tremor.. *Pharmaceuticals (Basel, Switzerland)*. PMID: 34072005
2. CCDC183 is essential for cytoplasmic invagination around the flagellum during spermiogenesis and male fertility.. *Development (Cambridge, England)*. PMID: 37882665
3. Multimodal immunogenomic biomarker analysis of tumors from pediatric patients enrolled to a phase 1-2 study of single-agent atezolizumab.. *Nature cancer*. PMID: 37038005
4. Gene-knockout by iSTOP enables rapid reproductive disease modeling and phenotyping in germ cells of the founder generation.. *Science China. Life sciences*. PMID: 38332217
5. Exome-wide rare variant analysis in familial essential tremor.. *Parkinsonism & related disorders*. PMID: 33279834

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.0 |
| 高置信度残基 (pLDDT>90) 占比 | 48.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.0% |
| 低置信 (pLDDT<50) 占比 | 7.9% |
| 有序区域 (pLDDT>70) 占比 | 77.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.0，有序区 77.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043247 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RABL6 | 0.658 | 0.000 | — |
| TMEM141 | 0.631 | 0.000 | — |
| GPR151 | 0.599 | 0.000 | — |
| LCN12 | 0.597 | 0.000 | — |
| MAMDC4 | 0.591 | 0.000 | — |
| NPDC1 | 0.539 | 0.000 | — |
| KCNS2 | 0.539 | 0.000 | — |
| TMEM51 | 0.535 | 0.000 | — |
| HAPLN4 | 0.529 | 0.000 | — |
| STK32B | 0.518 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZMYND19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRSS45P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FTCD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FCHSD2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CTNNA3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NRDE2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMARCE1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MBD3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BFSP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.0 + PDB: 无 | pLDDT=82.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Primary cilium tip, Mid  | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCDC183 — Coiled-coil domain-containing protein 183，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小534 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BCR | BioGRID | 0 |
| NRBF2 | BioGRID | 0 |
| FOXP1 | BioGRID | 0 |
| RABEP1 | BioGRID | 0 |
| CEP131 | BioGRID | 0 |
| NDEL1 | BioGRID | 0 |
| NDE1 | BioGRID | 0 |
| RABGEF1 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

CCDC183（UniProt Q5T5S1）属于含卷曲螺旋结构域蛋白超家族，仅注释有一个InterPro条目IPR043247（CCDC183 coiled-coil domain-containing protein）。卷曲螺旋（coiled-coil）结构由两股或多股alpha螺旋以左手超螺旋方式缠绕而成，经典七肽重复序列（abcdefg）的a和d位点为疏水残基，驱动螺旋间的疏水界面形成。Pfam未检出已知结构域，SMART同样无匹配，表明CCDC183的卷曲螺旋区域可能为新型折叠或采用了偏离经典七肽重复的变体模式。AlphaFold v6预测pLDDT=82.0，有序区域77.1%，高置信残基（pLDDT>90）48.1%，提示该蛋白具有稳定的折叠结构，且其卷曲螺旋区域（预估占蛋白的40-60%）折叠可靠，具备结构生物学研究的可行性。

STRING-PPI网络规模有限且缺乏实验验证：RABL6（0.658）和TMEM141（0.631）为纯计算预测，所有互作的experimental分值均为0，提示CCDC183的PPI网络尚未在实验层面被系统鉴定。然而，IntAct实验数据提供了更为关键的视角：酵母双杂交验证捕捉到CCDC183与染色质调控蛋白SMARCE1（SWI/SNF复合体的BAF57亚基，PMID:32296183）、甲基化DNA结合蛋白MBD3（NuRD复合体亚基，PMID:32296183）以及核RNA降解因子NRDE2（PMID:32296183）的直接互作。这些互作伙伴的染色质/转录调控功能高度一致：SMARCE1是ATP依赖的染色质重塑核心组分，MBD3识别甲基化CpG并通过NuRD复合体介导转录抑制，NRDE2参与核内RNA监视和降解。

CCDC183与SMARCE1和MBD3的互作暗示该蛋白可能通过SWI/SNF和NuRD两类关键染色质重塑复合物参与基因表达调控。SWI/SNF（BAF）复合体利用ATP水解能量滑动或移除核小体以激活转录，而NuRD复合体兼具组蛋白去乙酰化酶（HDAC1/2）和ATP酶（CHD3/4）活性，执行转录抑制。CCDC183若同时与这两类功能拮抗的复合体互作，可能作为染色质状态的切换因子（switch factor），在基因激活与沉默之间提供调控灵活性。

HPA IF定位于核质和胞质溶胶（Nucleoplasm, Cytosol），额外定位于初级纤毛尖端和中段暗示CCDC183具有多亚细胞定位特征。在精子发生过程中，CCDC183被鉴定为鞭毛周围细胞质内陷的关键因子（PMID:37882665），其敲除导致雄性不育。这一动态膜重塑功能需要精确的微管-膜协调，而卷曲螺旋结构域是实现这一机械功能的理想结构模块——它可以形成延伸的刚性杆状结构来桥接细胞骨架与膜。对于TE调控假说，CCDC183在核质中与SMARCE1/MBD3的互作是最具提示性的线索，但缺乏ChIP-seq或ATAC-seq数据，其染色质结合位点和靶基因谱尚待实验确定。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T5S1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213213-CCDC183/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC183
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T5S1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000213213-CCDC183/subcellular

![](https://images.proteinatlas.org/43812/2179_G2_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/43812/2179_G2_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/43812/2212_E8_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/43812/2212_E8_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/43812/2234_G2_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/43812/2234_G2_80_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T5S1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5T5S1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043247; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213213-CCDC183/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
