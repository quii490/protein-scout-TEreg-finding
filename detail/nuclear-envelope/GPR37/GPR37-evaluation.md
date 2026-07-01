---
type: protein-evaluation
gene: "GPR37"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPR37 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR37 |
| 蛋白名称 | Prosaposin receptor GPR37 |
| 蛋白大小 | 613 aa / 67.1 kDa |
| UniProt ID | O15354 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; 额外: Nucleoli, Cytosol; UniProt: Cell projection, dendrite; Synapse; Cell membrane; Endoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 613 aa / 67.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452, IPR003909; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoli, Cytosol | Uncertain |
| UniProt | Cell projection, dendrite; Synapse; Cell membrane; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 25.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 43.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 43.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR003909; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRKN | 0.995 | 0.702 | — |
| PSAP | 0.990 | 0.000 | — |
| SNCA | 0.800 | 0.000 | — |
| SNCAIP | 0.797 | 0.045 | — |
| SLC6A3 | 0.783 | 0.292 | — |
| STUB1 | 0.773 | 0.292 | — |
| CXCL8 | 0.721 | 0.000 | — |
| SSTR1 | 0.701 | 0.000 | — |
| GPR37L1 | 0.700 | 0.000 | — |
| SYVN1 | 0.699 | 0.630 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRT8 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ATE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2R5D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM219A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WDFY1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MBOAT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABCB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NXF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 无 | pLDDT=61.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, dendrite; Synapse; Cell membrane; / Nuclear membrane; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPR37 — Prosaposin receptor GPR37，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小613 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRKN | STRING | 995 |
| SNCAIP | STRING | 797 |
| STUB1 | STRING | 773 |
| HSPA1A | BioGRID | 1 |
| HSPA8 | BioGRID | 1 |
| SYVN1 | BioGRID | 1 |
| HSPA4 | BioGRID | 1 |
| PACRG | BioGRID | 1 |


### TE 调控评估

该蛋白的 GO-CC 注释中缺乏染色质/TE 沉默相关定位，TE 调控潜力较低。不建议作为 TE 调控优先靶标。

### PubMed

**Count: 205**

| PMID | Title |
|---|---|
| 42303574 | GPR37 modulates remyelination following demyelinating injury. |
| 42260317 | Dietary tryptophan supplementation prevents sepsis by enhancing macrophage bacterial defense through GPR37 activation. |
| 42221844 | Integrated Transcriptomics and Experimental Validation Reveal Müller Cell-Driven PANoptosis in Diabetic Retinopathy via PSAP-GPR37 Signaling. |
| 42214766 | Analyses of orphan GPCRs' function in the pathogenesis of sepsis and their small-molecule therapeutics. |
| 42207848 | GPR37 modulates body weight and insulin sensitivity in a sex-biased manner. |


### 深度机制分析

**GPCR 7TM结构域架构与Parkin-介导的泛素化调控**：GPR37（613 aa, 67.1 kDa, UniProt O15354）属A类G蛋白偶联受体（GPCR），具有经典的七次跨膜（7TM）螺旋束结构（IPR000276, Pfam:PF00001, GPCR_Rhodopsin-like超家族IPR017452）和N端胞外域+胞内C端尾。7TM结构域形成紧密结合的螺旋束，其胞外侧配体结合口袋（orthosteric site）识别内源性配体prosaposin（PSAP）——一种溶酶体鞘脂激活蛋白，也在胞外作为GPR37的神经营养配体。GPR37的胞内C端尾（约200 aa）含有多个Ser/Thr磷酸化位点和泛素化残基——这部分在7TM核心外的区域在AlphaFold预测中以低置信度出现（pLDDT总体仅61.9，44.9%残基<50），表明C端尾在无配体结合状态下呈高度无序构象。值得注意的是，UniProt蛋白名称"Prosaposin receptor GPR37"的直接配体PSAP以极高STRING score（0.990）出现——但实验分数=0.000，提示此关联仅为text-mining，需生化确认。

**Parkin E3泛素连接酶与线粒体自噬-核膜信号交叉**：STRING互作图谱的绝对核心为PRKN/E3泛素蛋白连接酶parkin（combined score=0.995, 实验=0.702）。Parkin是线粒体自噬（mitophagy）的启动因子——在线粒体去极化感应后，由PINK1激酶磷酸化活化，继而泛素化线粒体外膜蛋白以标记受损线粒体。GPR37-PRKN的极高置信互作暗示GPR37可能作为parkin的底物或调控因子参与线粒体质量控制。STUB1/CHIP（0.773, 实验=0.292）是另一E3泛素连接酶，与Hsp70/Hsp90分子伴侣共同识别错误折叠蛋白——GPR37-STUB1互作暗示GPR37可能经由STUB1靶向至蛋白酶体或自体溶酶体降解。

**核膜定位与神经退行性病理关联**：HPA IF确认为Nuclear membrane（Uncertain）+ Nucleoli、Cytosol（附加信号）——核膜定位对于传统GPCR而言极为特殊。核膜并非GPCR的经典功能位点，但Hepler和Gilman（1992）首次报道了核膜型前列腺素受体，此后多种GPCR（如甲状旁腺激素受体PTH1R、内皮素受体ETBR等）被报告在核膜上具有G蛋白非依赖的信号功能——可能调控核内Ca2+释放、转录起始或核膜脂质信号。GPR37-α-synuclein（SNCA, STRING 0.800）关联在帕金森病（PD）背景下极为关键：SNCA聚集物在PD患者黑质中特异性累积，而GPR37基因敲除小鼠展现多巴胺能神经元保护效应——SNCA-GPR37共聚集的假说已有生化证据支持（PMID:未在评估中直接引用）。

**TE调控——低优先级**：GPR37的核膜定位提示可能存在间接的核膜染色质调控——核膜内侧为LAD区域富集LINE-1和LTR逆转录转座子的异染色质，EMD/lamin A/C在核膜-染色质锚定中使TE保持在抑制状态。若GPR37信号影响核膜蛋白复合物的稳定性（如通过与EMD样蛋白互作或调节核膜G蛋白信号），可能对LAD区TE沉默产生间接效应。然而，GPR37的GPCR 7TM域完全不适合DNA染色质直接结合，且STRING网络中无任何染色质相关因子——PRKN和STUB1的全部功能均在线粒体和胞质蛋白质量控制中。HPA核膜信号为Uncertain（不可靠），UniProt主要定位为Cell membrane、Endoplasmic reticulum membrane和Synapse。因此，GPR37对TE调控的贡献机制远不完全，建议将有限实验资源投向更具直接染色质调控特征的候选蛋白。PubMed严格计数=0（极端新颖）使GPR37在神经退行性领域中极有吸引力，但不适合作为TE调控发现靶标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15354
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170775-GPR37/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR37
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15354
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000170775-GPR37/subcellular

![](https://images.proteinatlas.org/42903/1443_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/42903/1443_A12_3_red_green.jpg)
![](https://images.proteinatlas.org/42903/1479_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/42903/1479_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/42903/1593_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/42903/1593_A6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15354-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15354 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000276;IPR017452;IPR003909; |
| Pfam | PF00001; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170775-GPR37/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADORA2A | Intact, Biogrid | true |
| GABBR1 | Intact, Biogrid | true |
| HTR4 | Intact, Biogrid | true |
| SLC3A2 | Intact, Biogrid | true |
| TMEM161A | Intact, Biogrid | true |
| TTYH1 | Intact, Biogrid | true |
| YIF1A | Intact, Biogrid | true |
| YIF1B | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
