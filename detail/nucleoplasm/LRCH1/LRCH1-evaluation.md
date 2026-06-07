---
type: protein-evaluation
gene: "LRCH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRCH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRCH1 / CHDC1, KIAA1016 |
| 蛋白名称 | Leucine-rich repeat and calponin homology domain-containing protein 1 |
| 蛋白大小 | 728 aa / 80.9 kDa |
| UniProt ID | Q9Y2L9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Actin filaments, Cytosol; 额外: Nucleoli; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 728 aa / 80.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001715, IPR036872, IPR001611, IPR003591, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments, Cytosol; 额外: Nucleoli | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHDC1, KIAA1016 |

**关键文献**:
1. Lack of association of single nucleotide polymorphism in LRCH1 with knee osteoarthritis susceptibility.. *Journal of human genetics*. PMID: 18049793
2. LRCH1 deficiency enhances LAT signalosome formation and CD8(+) T cell responses against tumors and pathogens.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 32727906
3. Probing the diabetes and colorectal cancer relationship using gene - environment interaction analyses.. *British journal of cancer*. PMID: 37365285
4. Leucine rich repeats and calponin homology domain containing 1 inhibits NK-92 cell cytotoxicity through attenuating Src signaling.. *Immunobiology*. PMID: 32173150
5. Inhibition of leucine-rich repeats and calponin homology domain containing 1 accelerates microglia-mediated neuroinflammation in a rat traumatic spinal cord injury model.. *Journal of neuroinflammation*. PMID: 32631435

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 13.9% |
| 置信残基 (pLDDT 70-90) 占比 | 37.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 43.3% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001715, IPR036872, IPR001611, IPR003591, IPR032675; Pfam: PF00307, PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DOCK8 | 0.935 | 0.840 | — |
| DOCK7 | 0.835 | 0.781 | — |
| LRCH3 | 0.800 | 0.776 | — |
| DOCK6 | 0.769 | 0.482 | — |
| LRCH4 | 0.757 | 0.591 | — |
| NME8 | 0.746 | 0.217 | — |
| TM2D3 | 0.648 | 0.000 | — |
| ZFAND4 | 0.645 | 0.073 | — |
| CALM1 | 0.636 | 0.104 | — |
| TNFAIP6 | 0.598 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMAD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| prfB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LRCH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| DOCK8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| DOCK6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| TMEM14A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM14B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MOB1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24255178|imex:IM-21541 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 无 | pLDDT=62.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Actin filaments, Cytosol; 额外: Nucleoli | 一致 |
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
1. LRCH1 — Leucine-rich repeat and calponin homology domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小728 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2L9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136141-LRCH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRCH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2L9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (approved)。来源: https://www.proteinatlas.org/ENSG00000136141-LRCH1/subcellular

![](https://images.proteinatlas.org/21536/187_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21536/187_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21536/188_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21536/188_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21536/246_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21536/246_B7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2L9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y2L9 |
| SMART | SM00033;SM00364;SM00369; |
| UniProt Domain [FT] | DOMAIN 576..692; /note="Calponin-homology (CH)"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044" |
| InterPro | IPR001715;IPR036872;IPR001611;IPR003591;IPR032675;IPR050216; |
| Pfam | PF00307;PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136141-LRCH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DOCK7 | Intact, Biogrid, Opencell | true |
| DOCK8 | Intact, Biogrid | true |
| MYO6 | Biogrid, Opencell | true |
| YWHAE | Biogrid, Opencell | true |
| CALD1 | Opencell | false |
| CALM3 | Opencell | false |
| DOCK6 | Biogrid | false |
| DYRK1A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
