---
type: protein-evaluation
gene: "CEP164"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CEP164 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP164 / KIAA1052, NPHP15 |
| 蛋白名称 | Centrosomal protein of 164 kDa |
| 蛋白大小 | 1460 aa / 164.3 kDa |
| UniProt ID | Q9UPV0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Primary cilium transition zone, Centrosome, Principal piece;; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 5/10 | ×1 | 5 | 1460 aa / 164.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 7NWJ, 7O06, 7O0S, 7O3B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051841, IPR001202, IPR036020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Primary cilium transition zone, Centrosome, Principal piece; 额外: Nucleoplasm, Vesicles, Equatorial segment | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary transition fiber (GO:0097539)
- ciliary transition zone (GO:0035869)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- nucleoplasm (GO:0005654)
- sperm principal piece (GO:0097228)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 106 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1052, NPHP15 |

**关键文献**:
1. Nephronophthisis-Related Ciliopathies.. **. PMID: 27336129
2. Bardet-Biedl Syndrome Overview.. **. PMID: 20301537
3. Phase separation of TTBK2 and CEP164 is necessary for ciliogenesis.. *Cell reports*. PMID: 40483689
4. Disruption of distal appendage protein CEP164 causes skeletal malformation in mice.. *Biochemical and biophysical research communications*. PMID: 39612644
5. Embryonic and foetal expression patterns of the ciliopathy gene CEP164.. *PloS one*. PMID: 31990917

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 28.1% |
| 置信残基 (pLDDT 70-90) 占比 | 18.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 47.7% |
| 有序区域 (pLDDT>70) 占比 | 46.4% |
| 可用 PDB 条目 | 7NWJ, 7O06, 7O0S, 7O3B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 46.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051841, IPR001202, IPR036020 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEP83 | 0.997 | 0.099 | — |
| SCLT1 | 0.997 | 0.060 | — |
| TTBK2 | 0.993 | 0.597 | — |
| FBF1 | 0.990 | 0.046 | — |
| CEP89 | 0.979 | 0.089 | — |
| NIN | 0.901 | 0.106 | — |
| RAB3IP | 0.894 | 0.045 | — |
| PLK1 | 0.878 | 0.048 | — |
| RAB8A | 0.871 | 0.045 | — |
| ARL13B | 0.827 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mlh1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Rab6 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| rau | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Swt1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rint1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG8851 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| slam | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| eEF2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pp1-87B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pp1alpha-96A | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 7NWJ, 7O06, 7O0S, 7O3B | pLDDT=61.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Primary cilium transition zone, Centrosome, Princi | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CEP164 — Centrosomal protein of 164 kDa，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1460 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPV0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110274-CEP164/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP164
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPV0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Primary cilium transition zone (uncertain)。来源: https://www.proteinatlas.org/ENSG00000110274-CEP164/subcellular

![](https://images.proteinatlas.org/37606/2129_C2_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/37606/2129_C2_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/37606/2152_C1_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/37606/2152_C1_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/37606/2169_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37606/2169_G5_35_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPV0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPV0 |
| SMART | SM00456; |
| UniProt Domain [FT] | DOMAIN 56..89; /note="WW"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00224" |
| InterPro | IPR051841;IPR001202;IPR036020; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110274-CEP164/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC92 | Intact, Biogrid | true |
| DVL3 | Intact, Biogrid | true |
| TTBK2 | Intact, Biogrid | true |
| ATR | Biogrid | false |
| ATRIP | Biogrid | false |
| CLP1 | Intact | false |
| GYS1 | Opencell | false |
| HSPD1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
