---
type: protein-evaluation
gene: "NFIA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFIA — REJECTED (研究热度过高 (PubMed strict=264，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFIA / KIAA1439 |
| 蛋白名称 | Nuclear factor 1 A-type |
| 蛋白大小 | 509 aa / 55.9 kDa |
| UniProt ID | Q12857 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 509 aa / 55.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=264 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000647, IPR020604, IPR019739, IPR019548, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 264 |
| PubMed broad count | 421 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1439 |

**关键文献**:
1. Genes and Athletic Performance: The 2023 Update.. *Genes*. PMID: 37372415
2. NFIA regulates articular chondrocyte fatty acid metabolism and joint homeostasis.. *Science translational medicine*. PMID: 40737429
3. Astrocyte-derived extracellular vesicular NFIA mediates obesity-associated cognitive impairment.. *Journal of neuroinflammation*. PMID: 40448146
4. NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37487068
5. Single-Cell RNA-Seq Analysis of Retinal Development Identifies NFI Factors as Regulating Mitotic Exit and Late-Born Cell Specification.. *Neuron*. PMID: 31128945

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.7 |
| 高置信度残基 (pLDDT>90) 占比 | 30.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 49.5% |
| 有序区域 (pLDDT>70) 占比 | 38.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.7），有序残基占 38.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000647, IPR020604, IPR019739, IPR019548, IPR003619; Pfam: PF00859, PF03165, PF10524 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SOX9 | 0.871 | 0.292 | — |
| NFIB | 0.812 | 0.705 | — |
| SPI1 | 0.791 | 0.000 | — |
| SLC1A3 | 0.756 | 0.000 | — |
| CSF1R | 0.696 | 0.000 | — |
| NFIX | 0.660 | 0.253 | — |
| SPIB | 0.649 | 0.000 | — |
| SOX2 | 0.617 | 0.422 | — |
| PAX6 | 0.609 | 0.294 | — |
| NFIC | 0.580 | 0.253 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PLEKHF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NFIB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GABARAPL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| URS00000A07C1_10090 | psi-mi:"MI:0096"(pull down) | pubmed:29867223|imex:IM-24989 |
| EBI-26475521 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| CCL8 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.7 + PDB: 无 | pLDDT=62.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NFIA — Nuclear factor 1 A-type，研究基础较多，新颖性有限。
2. 蛋白大小509 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 264 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 264 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12857
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162599-NFIA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFIA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12857
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000162599-NFIA/subcellular

![](https://images.proteinatlas.org/6111/118_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/6111/118_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/6111/119_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/6111/119_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/6111/120_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/6111/120_F2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12857-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12857 |
| SMART | SM00523; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000647;IPR020604;IPR019739;IPR019548;IPR003619; |
| Pfam | PF00859;PF03165;PF10524; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162599-NFIA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ELK3 | Intact, Biogrid | true |
| ERG | Intact, Biogrid | true |
| ETV7 | Intact, Biogrid | true |
| FOS | Intact, Biogrid | true |
| GATA2 | Intact, Biogrid | true |
| GATA3 | Intact, Biogrid | true |
| KLF16 | Intact, Biogrid | true |
| KLF3 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
