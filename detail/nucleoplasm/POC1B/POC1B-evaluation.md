---
type: protein-evaluation
gene: "POC1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POC1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POC1B / WDR51B |
| 蛋白名称 | POC1 centriolar protein homolog B |
| 蛋白大小 | 478 aa / 53.7 kDa |
| UniProt ID | Q8TC44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol, Flagellar centriole; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 478 aa / 53.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Flagellar centriole; 额外: Nucleoplasm | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, microtu... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- spindle pole (GO:0000922)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR51B |

**关键文献**:
1. Joubert Syndrome.. **. PMID: 20301500
2. Poc1B and Sas-6 Function Together during the Atypical Centriole Formation in Drosophila melanogaster.. *Cells*. PMID: 31387336
3. Homozygous frameshift variant in POC1B causes male infertility with oligoasthenoteratozoospermia in human and mice.. *Human molecular genetics*. PMID: 37070736
4. Phenotypic and genotypic features of POC1B-associated cone dystrophy.. *Ophthalmic genetics*. PMID: 37246743
5. Poc1A and Poc1B act together in human cells to ensure centriole integrity.. *Journal of cell science*. PMID: 23015594

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 72.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.4，有序区 72.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POC5 | 0.965 | 0.124 | — |
| FAM161A | 0.952 | 0.297 | — |
| POC1A | 0.823 | 0.813 | — |
| CETN2 | 0.800 | 0.104 | — |
| WDR90 | 0.747 | 0.143 | — |
| CEP135 | 0.727 | 0.190 | — |
| CEP295 | 0.721 | 0.000 | — |
| SASS6 | 0.686 | 0.000 | — |
| CEP120 | 0.684 | 0.100 | — |
| C8orf37 | 0.668 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000020113.9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CUL4B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| HSBP1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| COG7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| SQSTM1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| COG5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| M-RIP | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| EIF4A1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| GNG12 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RAI14 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 无 | pLDDT=77.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Cytosol, Flagellar centriole; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. POC1B — POC1 centriolar protein homolog B，非常新颖，仅有少数基础研究。
2. 蛋白大小478 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TC44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139323-POC1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POC1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TC44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (uncertain)。来源: https://www.proteinatlas.org/ENSG00000139323-POC1B/subcellular

![](https://images.proteinatlas.org/38841/1216_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38841/1216_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38841/2148_B2_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/38841/2148_B2_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/38841/2209_A2_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/38841/2209_A2_8_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TC44-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TC44 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR020472;IPR019775;IPR036322;IPR001680;IPR050505; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139323-POC1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NUDC | Intact, Biogrid, Bioplex | true |
| PELO | Biogrid, Bioplex | true |
| PFDN2 | Biogrid, Bioplex | true |
| POC1A | Biogrid, Bioplex | true |
| ABRAXAS2 | Bioplex | false |
| AKIP1 | Bioplex | false |
| CCDC107 | Bioplex | false |
| CCT2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
