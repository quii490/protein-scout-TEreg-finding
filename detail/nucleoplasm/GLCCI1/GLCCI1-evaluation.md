---
type: protein-evaluation
gene: "GLCCI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLCCI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLCCI1 |
| 蛋白名称 | Glucocorticoid-induced transcript 1 protein |
| 蛋白大小 | 547 aa / 58.0 kDa |
| UniProt ID | Q86VQ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 547 aa / 58.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026642; Pfam: PF15388 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 85 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Involvement of GLCCI1 in mouse spermatogenesis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 36468710
2. Role of GLCCI1 in inhibiting PI3K-induced NLRP3 inflammasome activation in asthma.. *Chinese medical journal pulmonary and critical care medicine*. PMID: 39834584
3. Novel GLCCI1-BRAF fusion drives kinase signaling in a case of pheochromocytomatosis.. *European journal of endocrinology*. PMID: 35861986
4. GLCCI1 gene body methylation in peripheral blood is associated with asthma and asthma severity.. *Clinica chimica acta; international journal of clinical chemistry*. PMID: 34529984
5. The GLCCI1 rs37973 variant and the efficacy of inhaled corticosteroids in the treatment of asthma: A meta-analysis.. *The clinical respiratory journal*. PMID: 37157161

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.7% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 35.6% |
| 低置信 (pLDDT<50) 占比 | 51.6% |
| 有序区域 (pLDDT>70) 占比 | 12.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.2），有序残基占 12.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026642; Pfam: PF15388 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYRK1A | 0.772 | 0.733 | — |
| FCER2 | 0.539 | 0.000 | — |
| CRHR1 | 0.522 | 0.000 | — |
| ICA1 | 0.483 | 0.000 | — |
| UMAD1 | 0.479 | 0.000 | — |
| FAM53C | 0.473 | 0.000 | — |
| FBXL7 | 0.451 | 0.000 | — |
| CRHR1-2 | 0.448 | 0.000 | — |
| OR6X1 | 0.447 | 0.000 | — |
| DYNLL1 | 0.446 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DYRK1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| DYRK1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERICH6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCAF7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TRIM41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.2 + PDB: 无 | pLDDT=53.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GLCCI1 — Glucocorticoid-induced transcript 1 protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小547 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VQ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106415-GLCCI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLCCI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VQ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000106415-GLCCI1/subcellular

![](https://images.proteinatlas.org/1674/1884_E2_44_cr5b98d36a1c103_blue_red_green.jpg)
![](https://images.proteinatlas.org/1674/1884_E2_49_cr5b98d36a1c52e_blue_red_green.jpg)
![](https://images.proteinatlas.org/1674/63_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1674/63_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1674/93_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1674/93_F4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86VQ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86VQ1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026642; |
| Pfam | PF15388; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106415-GLCCI1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DCAF7 | Intact | false |
| DYNLL1 | Biogrid | false |
| DYNLL2 | Biogrid | false |
| DYRK1A | Biogrid | false |
| DYRK1B | Biogrid | false |
| TRIM41 | Intact | false |
| YWHAB | Biogrid | false |
| YWHAG | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
