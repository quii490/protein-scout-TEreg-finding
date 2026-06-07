---
type: protein-evaluation
gene: "LFNG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LFNG — REJECTED (研究热度过高 (PubMed strict=136，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LFNG |
| 蛋白名称 | Beta-1,3-N-acetylglucosaminyltransferase lunatic fringe |
| 蛋白大小 | 379 aa / 41.8 kDa |
| UniProt ID | Q8NES3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane, Golgi apparatus; UniProt: Golgi apparatus; Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 379 aa / 41.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=136 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017374, IPR003378; Pfam: PF02434 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Golgi apparatus | Approved |
| UniProt | Golgi apparatus; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- extracellular vesicle (GO:1903561)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 136 |
| PubMed broad count | 304 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Spondylocostal Dysostosis, Autosomal Recessive.. **. PMID: 20301771
2. Lfng and Dll3 cooperate to modulate protein interactions in cis and coordinate oscillatory Notch pathway activation in the segmentation clock.. *Developmental biology*. PMID: 35429490
3. Rational design of a Lfng-enhancer AAV construct drives specific and efficient gene expression in inner ear supporting cells.. *Hearing research*. PMID: 39889630
4. Bmp9 regulates Notch signaling and the temporal dynamics of angiogenesis via Lunatic Fringe.. *Developmental cell*. PMID: 41650956
5. Exploring the role of LFNG in hepatoblastoma using multiomics and raise a query in proof link.. *Gene*. PMID: 40499700

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 14.8% |
| 有序区域 (pLDDT>70) 占比 | 77.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.2，有序区 77.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017374, IPR003378; Pfam: PF02434 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH2 | 0.979 | 0.125 | — |
| NOTCH1 | 0.973 | 0.073 | — |
| NOTCH3 | 0.969 | 0.125 | — |
| NOTCH4 | 0.938 | 0.073 | — |
| MESP2 | 0.925 | 0.000 | — |
| MFNG | 0.909 | 0.000 | — |
| RFNG | 0.906 | 0.000 | — |
| DLL1 | 0.903 | 0.125 | — |
| DLL3 | 0.848 | 0.073 | — |
| JAG1 | 0.786 | 0.125 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WRAP73 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.2 + PDB: 无 | pLDDT=82.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus; Golgi apparatus membrane / Nuclear membrane, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. LFNG — Beta-1,3-N-acetylglucosaminyltransferase lunatic fringe，研究基础较多，新颖性有限。
2. 蛋白大小379 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 136 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 136 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NES3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106003-LFNG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LFNG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NES3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000106003-LFNG/subcellular

![](https://images.proteinatlas.org/69130/1592_H4_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/69130/1592_H4_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/69130/1616_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/69130/1616_D11_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/69130/2072_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/69130/2072_E10_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NES3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NES3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR017374;IPR003378; |
| Pfam | PF02434; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106003-LFNG/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
