---
type: protein-evaluation
gene: "NCOR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NCOR2 — REJECTED (研究热度过高 (PubMed strict=196，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCOR2 / CTG26 |
| 蛋白名称 | Nuclear receptor corepressor 2 |
| 蛋白大小 | 2514 aa / 273.7 kDa |
| UniProt ID | Q9Y618 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2514 aa / 273.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=196 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=40.2; PDB: 1KKQ, 1R2B, 1XC5, 2GPV, 2L5G, 2LTP, 2ODD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009057, IPR017930, IPR051571, IPR031557, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- membrane (GO:0016020)
- nuclear body (GO:0016604)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 196 |
| PubMed broad count | 628 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTG26 |

**关键文献**:
1. Insights into the function of HDAC3 and NCoR1/NCoR2 co-repressor complex in metabolic diseases.. *Frontiers in molecular biosciences*. PMID: 37674539
2. Identification of astrocyte regulators by nucleic acid cytometry.. *Nature*. PMID: 36599367
3. Keratin-positive giant cell-rich tumor review.. *Seminars in diagnostic pathology*. PMID: 40555034
4. Nuclear receptor corepressors non-canonically drive glucocorticoid receptor-dependent activation of hepatic gluconeogenesis.. *Nature metabolism*. PMID: 38622413
5. HNF4A mitigates sepsis-associated lung injury by upregulating NCOR2/GR/STAB1 axis and promoting macrophage polarization towards M2 phenotype.. *Cell death & disease*. PMID: 39979267

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.2 |
| 高置信度残基 (pLDDT>90) 占比 | 2.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 83.6% |
| 有序区域 (pLDDT>70) 占比 | 11.0% |
| 可用 PDB 条目 | 1KKQ, 1R2B, 1XC5, 2GPV, 2L5G, 2LTP, 2ODD, 2RT5, 3R29, 3R2A |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=40.2），有序残基占 11.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009057, IPR017930, IPR051571, IPR031557, IPR001005; Pfam: PF15784, PF00249 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC3 | 0.999 | 0.992 | — |
| SIN3A | 0.999 | 0.712 | — |
| RARA | 0.999 | 0.856 | — |
| HDAC4 | 0.999 | 0.978 | — |
| HDAC1 | 0.999 | 0.701 | — |
| BCL6 | 0.999 | 0.989 | — |
| PPARG | 0.999 | 0.984 | — |
| TBL1X | 0.998 | 0.872 | — |
| RBPJ | 0.998 | 0.705 | — |
| NCOR1 | 0.998 | 0.622 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNW1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| RBPJ | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| HDAC10 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11739383 |
| HDAC1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11739383 |
| THRA | psi-mi:"MI:0096"(pull down) | pubmed:11259580 |
| AHR | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10395741 |
| ARNT | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10395741 |
| BCL6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16147992 |
| TNIK | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=40.2 + PDB: 1KKQ, 1R2B, 1XC5, 2GPV, 2L5G,  | pLDDT=40.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NCOR2 — Nuclear receptor corepressor 2，研究基础较多，新颖性有限。
2. 蛋白大小2514 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 196 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=40.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 196 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y618
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196498-NCOR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCOR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y618
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000196498-NCOR2/subcellular

![](https://images.proteinatlas.org/1928/62_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/1928/62_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/1928/63_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/1928/63_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/1928/93_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/1928/93_G10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y618-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y618 |
| SMART | SM00717; |
| UniProt Domain [FT] | DOMAIN 427..478; /note="SANT 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624"; DOMAIN 610..661; /note="SANT 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624" |
| InterPro | IPR009057;IPR017930;IPR051571;IPR031557;IPR001005;IPR017884; |
| Pfam | PF15784;PF00249; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196498-NCOR2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AHR | Intact, Biogrid | true |
| GPS2 | Intact, Biogrid | true |
| HDAC1 | Intact, Biogrid | true |
| HDAC3 | Intact, Biogrid, Opencell | true |
| PPARA | Intact, Biogrid | true |
| RARA | Intact, Biogrid | true |
| RBPJ | Intact, Biogrid | true |
| SNW1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
