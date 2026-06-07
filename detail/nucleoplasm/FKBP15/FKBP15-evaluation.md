---
type: protein-evaluation
gene: "FKBP15"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FKBP15 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FKBP15 / KIAA0674 |
| 蛋白名称 | FK506-binding protein 15 |
| 蛋白大小 | 1219 aa / 133.6 kDa |
| UniProt ID | Q5T1M5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Cytosol; UniProt: Cytoplasm; Cell projection, axon; Early endosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1219 aa / 133.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056598, IPR046357, IPR001179; Pfam: PF23649, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Cell projection, axon; Early endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- early endosome (GO:0005769)
- growth cone (GO:0030426)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0674 |

**关键文献**:
1. NTRK-fused central nervous system tumours: clinicopathological and genetic insights and response to TRK inhibitors.. *Acta neuropathologica communications*. PMID: 39014476
2. Multi-omics Analysis Reveals Comprehensive Aberrant Protein and Phosphorylation Characteristics in Breast Cancer and Paired Metastatic Lymph Nodes.. *Protein & cell*. PMID: 41527309
3. The peptidyl-prolyl isomerases FKBP15-1 and FKBP15-2 negatively affect lateral root development by repressing the vacuolar invertase VIN2 in Arabidopsis.. *Planta*. PMID: 32945964
4. Molecular characterization of a FKBP-type immunophilin from higher plants.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 8692927
5. M(6)A Demethylase Inhibits Osteogenesis of Dental Follicle Stem Cells via Regulating miR-7974/FKBP15 Pathway.. *International journal of molecular sciences*. PMID: 38003310

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.5 |
| 高置信度残基 (pLDDT>90) 占比 | 28.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 47.2% |
| 有序区域 (pLDDT>70) 占比 | 47.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.5），有序残基占 47.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056598, IPR046357, IPR001179; Pfam: PF23649, PF00254 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WASHC2C | 0.886 | 0.628 | — |
| WASHC5 | 0.876 | 0.588 | — |
| WASHC4 | 0.810 | 0.292 | — |
| VPS29 | 0.799 | 0.503 | — |
| VPS35 | 0.793 | 0.623 | — |
| TBC1D5 | 0.760 | 0.000 | — |
| WASHC1 | 0.683 | 0.345 | — |
| WASHC2A | 0.673 | 0.230 | — |
| VPS26A | 0.660 | 0.421 | — |
| CAPZA1 | 0.578 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Esrrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| ZYX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCF2L | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| GAB1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| AIPL1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MIOS | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CEP43 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PDE5A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| COMMD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.5 + PDB: 无 | pLDDT=63.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell projection, axon; Early endosome / Nucleoli; 额外: Cytosol | 一致 |
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
1. FKBP15 — FK506-binding protein 15，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1219 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T1M5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119321-FKBP15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FKBP15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T1M5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000119321-FKBP15/subcellular

![](https://images.proteinatlas.org/7979/20_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/7979/20_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/7979/21_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/7979/21_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/7979/22_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/7979/22_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T1M5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5T1M5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 197..290; /note="PPIase FKBP-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00277" |
| InterPro | IPR056598;IPR046357;IPR001179; |
| Pfam | PF23649;PF00254; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119321-FKBP15/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAPZB | Biogrid, Opencell | true |
| VPS29 | Biogrid, Opencell | true |
| AIPL1 | Intact | false |
| BAG2 | Bioplex | false |
| CST5 | Bioplex | false |
| DNAJC13 | Opencell | false |
| HSPA8 | Bioplex | false |
| MDP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
