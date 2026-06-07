---
type: protein-evaluation
gene: "CDA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDA — REJECTED (研究热度过高 (PubMed strict=717，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDA / CDD |
| 蛋白名称 | Cytidine deaminase |
| 蛋白大小 | 146 aa / 16.2 kDa |
| UniProt ID | P32320 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 146 aa / 16.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=717 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.1; PDB: 1MQ0 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016192, IPR002125, IPR050202, IPR006262, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- secretory granule lumen (GO:0034774)
- tertiary granule lumen (GO:1904724)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 717 |
| PubMed broad count | 8329 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDD |

**关键文献**:
1. The senescence-associated secretome of Hedgehog-deficient hepatocytes drives MASLD progression.. *The Journal of clinical investigation*. PMID: 39190624
2. Enhanced mitochondrial activity reshapes a gut microbiota profile that delays NASH progression.. *Hepatology (Baltimore, Md.)*. PMID: 35921199
3. Nucleotide metabolism in cancer cells fuels a UDP-driven macrophage cross-talk, promoting immunosuppression and immunotherapy resistance.. *Nature cancer*. PMID: 38844817
4. Fibroblast growth factor 21 is a hepatokine involved in MASLD progression.. *United European gastroenterology journal*. PMID: 38894596
5. Updates on clinical and laboratory aspects of hereditary dyserythropoietic anemias.. *International journal of laboratory hematology*. PMID: 38747503

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 91.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 94.5% |
| 可用 PDB 条目 | 1MQ0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.1，有序区 94.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016192, IPR002125, IPR050202, IPR006262, IPR016193; Pfam: PF00383 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UPP2 | 0.997 | 0.000 | — |
| TYMP | 0.997 | 0.000 | — |
| UPP1 | 0.997 | 0.000 | — |
| DCK | 0.996 | 0.000 | — |
| UCK1 | 0.977 | 0.000 | — |
| UCK2 | 0.977 | 0.000 | — |
| UCKL1 | 0.974 | 0.000 | — |
| TK2 | 0.972 | 0.000 | — |
| APOBEC1 | 0.967 | 0.000 | — |
| PNP | 0.947 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000364212.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| cdi | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15014439 |
| NTAQ1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ZBTB24 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| INCA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP8-1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DDIT4L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARRDC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 1MQ0 | pLDDT=94.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CDA — Cytidine deaminase，研究基础较多，新颖性有限。
2. 蛋白大小146 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 717 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 717 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P32320
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158825-CDA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P32320
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000158825-CDA/subcellular

![](https://images.proteinatlas.org/64202/1164_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/64202/1164_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/64202/1174_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/64202/1174_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/64202/1246_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/64202/1246_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P32320-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P32320 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 13..140; /note="CMP/dCMP-type deaminase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01083" |
| InterPro | IPR016192;IPR002125;IPR050202;IPR006262;IPR016193; |
| Pfam | PF00383; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158825-CDA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APBA3 | Bioplex | false |
| ARRDC3 | Intact | false |
| DDIT4L | Intact | false |
| FNDC11 | Intact | false |
| FOXN1 | Intact | false |
| GAPDHS | Bioplex | false |
| GORASP2 | Intact | false |
| INCA1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
