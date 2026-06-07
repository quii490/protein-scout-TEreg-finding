---
type: protein-evaluation
gene: "HABP4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HABP4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HABP4 |
| 蛋白名称 | Intracellular hyaluronan-binding protein 4 |
| 蛋白大小 | 413 aa / 45.8 kDa |
| UniProt ID | Q5JVS0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, Stress granule; Cytoplasm, sa |
| 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 45.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039764, IPR006861, IPR032381; Pfam: PF04774, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, Stress granule; Cytoplasm, sarcoplasm; Nucleus, nuclear body; Nucleus... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- Gemini of Cajal bodies (GO:0097504)
- nuclear membrane (GO:0031965)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A molecular network of conserved factors keeps ribosomes dormant in the egg.. *Nature*. PMID: 36653451
2. Complex interactomes and post-translational modifications of the regulatory proteins HABP4 and SERBP1 suggest pleiotropic cellular functions.. *World journal of biological chemistry*. PMID: 31768228
3. HABP4 overexpression promotes apoptosis in goat turbinate bone cells.. *Animal biotechnology*. PMID: 35522841
4. Intracellular hyaluronic acid-binding protein 4 (HABP4): a candidate tumor suppressor in colorectal cancer.. *Oncotarget*. PMID: 33245729
5. Microneedle fractional radiofrequency increases epidermal hyaluronan and reverses age-related epidermal dysfunction.. *Lasers in surgery and medicine*. PMID: 26415023

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 2.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 35.4% |
| 低置信 (pLDDT<50) 占比 | 45.5% |
| 有序区域 (pLDDT>70) 占比 | 19.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 19.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039764, IPR006861, IPR032381; Pfam: PF04774, PF16174 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.970 | 0.967 | — |
| RACK1 | 0.965 | 0.862 | — |
| RPS20 | 0.914 | 0.844 | — |
| RPS3 | 0.914 | 0.841 | — |
| RPL38 | 0.901 | 0.869 | — |
| RPL5 | 0.900 | 0.840 | — |
| RPS2 | 0.900 | 0.841 | — |
| RPL24 | 0.892 | 0.835 | — |
| RPL31 | 0.891 | 0.838 | — |
| RPL15 | 0.890 | 0.835 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHD3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12505151 |
| ENO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PRMT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FRA10AC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CRK | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| EZH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EHHADH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PSENEN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 无 | pLDDT=55.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, Stress granule; Cyt / Nuclear membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HABP4 — Intracellular hyaluronan-binding protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JVS0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130956-HABP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HABP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JVS0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000130956-HABP4/subcellular

![](https://images.proteinatlas.org/62366/1251_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62366/1251_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62366/1256_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62366/1256_E11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/62366/1762_E9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/62366/1762_E9_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JVS0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5JVS0 |
| SMART | SM01233; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039764;IPR006861;IPR032381; |
| Pfam | PF04774;PF16174; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130956-HABP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHD3 | Intact, Biogrid | true |
| PRMT1 | Intact, Biogrid | true |
| SRSF9 | Intact, Biogrid | true |
| SYNCRIP | Intact, Biogrid | true |
| C1QBP | Biogrid | false |
| GNL2 | Biogrid | false |
| RACK1 | Biogrid | false |
| TP53 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
