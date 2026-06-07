---
type: protein-evaluation
gene: "ARL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ARL3 — REJECTED (研究热度过高 (PubMed strict=117，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARL3 / ARFL3 |
| 蛋白名称 | ADP-ribosylation factor-like protein 3 |
| 蛋白大小 | 182 aa / 20.5 kDa |
| UniProt ID | P36405 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centrosome, Basal body; 额外: Primary cilium; UniProt: Golgi apparatus membrane; Cytoplasm, cytoskeleton, spindle;  |
| 蛋白大小 | 8/10 | ×1 | 8 | 182 aa / 20.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=117 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR044612, IPR027417, IPR005225, IPR006689; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome, Basal body; 额外: Primary cilium | Supported |
| UniProt | Golgi apparatus membrane; Cytoplasm, cytoskeleton, spindle; Nucleus; Cytoplasm, cytoskeleton, microt... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary transition zone (GO:0035869)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytoplasmic microtubule (GO:0005881)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 117 |
| PubMed broad count | 170 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARFL3 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. A conserved mechanism for the retrieval of polyubiquitinated proteins from cilia.. *Cell*. PMID: 40840444
3. Arl3 and RP2 mediated assembly and traffic of membrane associated cilia proteins.. *Vision research*. PMID: 22884633
4. Dominant ARL3-related retinitis pigmentosa.. *Ophthalmic genetics*. PMID: 30932721
5. Binary Function of ARL3-GTP Revealed by Gene Knockouts.. *Advances in experimental medicine and biology*. PMID: 29721959

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 84.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.7，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044612, IPR027417, IPR005225, IPR006689; Pfam: PF00025 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UNC119 | 0.998 | 0.986 | — |
| UNC119B | 0.996 | 0.959 | — |
| RP2 | 0.994 | 0.961 | — |
| CFAP36 | 0.974 | 0.884 | — |
| PDE6D | 0.967 | 0.875 | — |
| RASA1 | 0.879 | 0.092 | — |
| SYS1 | 0.867 | 0.000 | — |
| TBCC | 0.866 | 0.000 | — |
| NPHP3 | 0.844 | 0.212 | — |
| ARL2BP | 0.829 | 0.692 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| dnd | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:unassigned1513|imex:IM- |
| PDE6D | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TLE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 无 | pLDDT=92.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Cytoplasm, cytoskeleton, / Nucleoplasm, Centrosome, Basal body; 额外: Primary c | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ARL3 — ADP-ribosylation factor-like protein 3，研究基础较多，新颖性有限。
2. 蛋白大小182 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 117 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 117 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P36405
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138175-ARL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P36405
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03





<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000138175-ARL3/subcellular

![](https://images.proteinatlas.org/63596/2133_C3_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/63596/2133_C3_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/63596/2161_E4_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/63596/2161_E4_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/63596/2169_H4_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/63596/2169_H4_63_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P36405-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P36405 |
| SMART | SM00177;SM00178; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR044612;IPR027417;IPR005225;IPR006689; |
| Pfam | PF00025; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138175-ARL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARL2BP | Intact, Biogrid | true |
| PDE6D | Intact, Biogrid, Opencell, Bioplex | true |
| RP2 | Intact, Biogrid | true |
| UNC119 | Intact, Biogrid | true |
| UNC119B | Intact, Biogrid | true |
| ACTR2 | Opencell | false |
| ACTR3 | Opencell | false |
| ALKBH2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
