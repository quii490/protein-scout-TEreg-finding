---
type: protein-evaluation
gene: "DLX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLX1 — REJECTED (研究热度过高 (PubMed strict=196，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLX1 |
| 蛋白名称 | Homeobox protein DLX-1 |
| 蛋白大小 | 255 aa / 27.3 kDa |
| UniProt ID | P56177 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 255 aa / 27.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=196 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050460, IPR001356, IPR020479, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 196 |
| PubMed broad count | 317 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Decoding gene networks controlling hypothalamic and prethalamic neuron development.. *Cell reports*. PMID: 40512619
2. The extracellular matrix fibulin 7 maintains epidermal stem cell heterogeneity during skin aging.. *EMBO reports*. PMID: 36278510
3. The DLX1-NCS1-MYC axis drives oncogenesis and progression in lung adenocarcinoma.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 40614386
4. Dlx1 and Dlx2 Promote Interneuron GABA Synthesis, Synaptogenesis, and Dendritogenesis.. *Cerebral cortex (New York, N.Y. : 1991)*. PMID: 29028947
5. The distribution of Dlx1-2 and glutamic acid decarboxylase in the embryonic and adult hypothalamus reveals three differentiated LHA subdivisions in rodents.. *Journal of chemical neuroanatomy*. PMID: 35283254

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.3 |
| 高置信度残基 (pLDDT>90) 占比 | 22.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.9% |
| 中等置信 (pLDDT 50-70) 占比 | 48.2% |
| 低置信 (pLDDT<50) 占比 | 25.9% |
| 有序区域 (pLDDT>70) 占比 | 25.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.3），有序残基占 25.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050460, IPR001356, IPR020479, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLX2 | 0.877 | 0.072 | — |
| ASCL1 | 0.874 | 0.000 | — |
| CALB2 | 0.794 | 0.000 | — |
| MYT1L | 0.759 | 0.000 | — |
| LHX6 | 0.755 | 0.045 | — |
| BMP4 | 0.691 | 0.000 | — |
| PVALB | 0.678 | 0.000 | — |
| TDRD1 | 0.678 | 0.000 | — |
| FOXG1 | 0.648 | 0.065 | — |
| POU3F2 | 0.639 | 0.059 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IGLC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IMPDH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DHPS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Mixl1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Tbx21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Foxa1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Cdx4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Barx1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Dlx2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Cdx1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.3 + PDB: 无 | pLDDT=64.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLX1 — Homeobox protein DLX-1，研究基础较多，新颖性有限。
2. 蛋白大小255 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 196 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 196 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56177
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144355-DLX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56177
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000144355-DLX1/subcellular

![](https://images.proteinatlas.org/7175/1910_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/7175/1910_G7_5_red_green.jpg)
![](https://images.proteinatlas.org/7175/1972_B7_24_cr5e16f61403b37_red_green.jpg)
![](https://images.proteinatlas.org/7175/1972_B7_5_cr5e16f61401d59_red_green.jpg)
![](https://images.proteinatlas.org/7175/2060_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/7175/2060_B2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56177-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P56177 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050460;IPR001356;IPR020479;IPR017970;IPR009057;IPR000047; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144355-DLX1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
