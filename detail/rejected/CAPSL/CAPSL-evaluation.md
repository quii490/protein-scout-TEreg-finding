---
type: protein-evaluation
gene: "CAPSL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAPSL — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAPSL |
| 蛋白名称 | Calcyphosin-like protein |
| 蛋白大小 | 208 aa / 24.2 kDa |
| UniProt ID | Q8WWF8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 208 aa / 24.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051581, IPR011992, IPR018247, IPR002048; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- organelle (GO:0043226)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. WGCNA combined with GSVA to explore biomarkers of refractory neocortical epilepsy.. *IBRO neuroscience reports*. PMID: 36247523
2. Calcyphosine-like (CAPSL) is regulated in Multiple Symmetric Lipomatosis and is involved in Adipogenesis.. *Scientific reports*. PMID: 31186450
3. Morphological Observation and Transcriptome Analysis of Ciliogenesis in Urechis unicinctus (Annelida, Echiura).. *International journal of molecular sciences*. PMID: 37511295
4. The genetic basis of graves' disease.. *Current genomics*. PMID: 22654555
5. Insights from homozygous signatures of cervus nippon revealed genetic architecture for components of fitness.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 39191871

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.3 |
| 高置信度残基 (pLDDT>90) 占比 | 73.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 98.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.3，有序区 98.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051581, IPR011992, IPR018247, IPR002048; Pfam: PF13499 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNTN | 0.752 | 0.000 | — |
| CFAP126 | 0.720 | 0.000 | — |
| LMBRD2 | 0.673 | 0.000 | — |
| DLGAP5 | 0.664 | 0.608 | — |
| ARMC3 | 0.641 | 0.000 | — |
| C20orf85 | 0.633 | 0.000 | — |
| PIFO | 0.633 | 0.000 | — |
| EFHB | 0.612 | 0.166 | — |
| C11orf88 | 0.585 | 0.000 | — |
| FAM81B | 0.581 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TUBA1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DLGAP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBA1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBA1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EML4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BIRC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.3 + PDB: 无 | pLDDT=91.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CAPSL — Calcyphosin-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小208 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWF8
- Protein Atlas: https://www.proteinatlas.org/search/CAPSL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAPSL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWF8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000152611-CAPSL/subcellular

![](https://images.proteinatlas.org/58495/2123_B3_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/58495/2123_B3_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/58495/2131_E3_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/58495/2131_E3_60_blue_red_green.jpg)
![](https://images.proteinatlas.org/58495/2168_B8_27_blue_red_green.jpg)
![](https://images.proteinatlas.org/58495/2168_B8_41_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WWF8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
