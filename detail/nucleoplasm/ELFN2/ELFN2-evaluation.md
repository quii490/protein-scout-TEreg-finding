---
type: protein-evaluation
gene: "ELFN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELFN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELFN2 / KIAA1904, LRRC62, PPP1R29 |
| 蛋白名称 | Protein phosphatase 1 regulatory subunit 29 |
| 蛋白大小 | 820 aa / 89.7 kDa |
| UniProt ID | Q5R3F8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 820 aa / 89.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR055106, IPR001611, IPR003591, IPR032675, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular space (GO:0005615)
- plasma membrane (GO:0005886)
- postsynaptic density membrane (GO:0098839)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1904, LRRC62, PPP1R29 |

**关键文献**:
1. Single-cell RNA-seq uncovers dynamic processes orchestrated by RNA-binding protein DDX43 in chromatin remodeling during spermiogenesis.. *Nature communications*. PMID: 37120627
2. LINC00470 Coordinates the Epigenetic Regulation of ELFN2 to Distract GBM Cell Autophagy.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 30037656
3. Profiling the Impact of mGlu(7)/Elfn1 Protein Interactions on the Pharmacology of mGlu(7) Allosteric Modulators.. *ACS chemical neuroscience*. PMID: 40689847
4. Trans-Synaptic Regulation of Metabotropic Glutamate Receptors by Elfn Proteins in Health and Disease.. *Frontiers in neural circuits*. PMID: 33790745
5. Complex N-glycosylation of mGluR6 is required for trans-synaptic interaction with ELFN adhesion proteins.. *The Journal of biological chemistry*. PMID: 38428819

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.0 |
| 高置信度残基 (pLDDT>90) 占比 | 23.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 46.0% |
| 有序区域 (pLDDT>70) 占比 | 43.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.0），有序残基占 43.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055106, IPR001611, IPR003591, IPR032675, IPR050541; Pfam: PF22986, PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CALM3 | 0.524 | 0.509 | — |
| GRM6 | 0.488 | 0.126 | — |
| KRTAP13-4 | 0.451 | 0.000 | — |
| ZFP69B | 0.425 | 0.095 | — |
| TBC1D1 | 0.424 | 0.425 | — |
| JPH3 | 0.415 | 0.093 | — |
| C3orf70 | 0.414 | 0.000 | — |
| SVOP | 0.411 | 0.000 | — |
| ZNF536 | 0.405 | 0.095 | — |
| NOM1 | 0.405 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| elfn2a | psi-mi:"MI:0892"(solid phase assay) | imex:IM-11659|pubmed:19765300 |
| boc | psi-mi:"MI:0892"(solid phase assay) | imex:IM-11659|pubmed:19765300 |
| ACAD11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TBC1D4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TBC1D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| UBR4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DPP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ELFN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CALM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCMF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 14
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.0 + PDB: 无 | pLDDT=61.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 11 + 14 interactions | 数据充分 |

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
1. ELFN2 — Protein phosphatase 1 regulatory subunit 29，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小820 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5R3F8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166897-ELFN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELFN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5R3F8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166897-ELFN2/subcellular

![](https://images.proteinatlas.org/781/50_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/781/50_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/781/51_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/781/51_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/781/52_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/781/52_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5R3F8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5R3F8 |
| SMART | SM00369; |
| UniProt Domain [FT] | DOMAIN 185..247; /note="LRRCT"; DOMAIN 292..379; /note="Fibronectin type-III" |
| InterPro | IPR055106;IPR001611;IPR003591;IPR032675;IPR050541; |
| Pfam | PF22986;PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166897-ELFN2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
