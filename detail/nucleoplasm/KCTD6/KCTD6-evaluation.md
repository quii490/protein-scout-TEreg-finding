---
type: protein-evaluation
gene: "KCTD6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD6 |
| 蛋白名称 | BTB/POZ domain-containing protein KCTD6 |
| 蛋白大小 | 237 aa / 27.6 kDa |
| UniProt ID | Q8NC69 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Mitochondria; UniProt: Cytoplasm, myofibril, sarcomere, M line |
| 蛋白大小 | 10/10 | ×1 | 10 | 237 aa / 27.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000210, IPR011333, IPR003131; Pfam: PF02214 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Mitochondria | Approved |
| UniProt | Cytoplasm, myofibril, sarcomere, M line | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- M band (GO:0031430)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Obscurin and KCTD6 regulate cullin-dependent small ankyrin-1 (sAnk1.5) protein turnover.. *Molecular biology of the cell*. PMID: 22573887
2. An age-independent gene signature for monitoring acute rejection in kidney transplantation.. *Theranostics*. PMID: 32550916
3. GSDMD suppresses keratinocyte differentiation by inhibiting FLG expression and attenuating KCTD6-mediated HDAC1 degradation in atopic dermatitis.. *PeerJ*. PMID: 38250727
4. The centrosomal deubiquitylase USP21 regulates Gli1 transcriptional activity and stability.. *Journal of cell science*. PMID: 27621083
5. Cullin 3 Recognition Is Not a Universal Property among KCTD Proteins.. *PloS one*. PMID: 25974686

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 66.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 86.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.2，有序区 86.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR011333, IPR003131; Pfam: PF02214 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000417490.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| GLMN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FUS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| PRPF31 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EHHADH | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 无 | pLDDT=87.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, myofibril, sarcomere, M line / Nucleoli, Mitochondria | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KCTD6 — BTB/POZ domain-containing protein KCTD6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小237 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NC69
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168301-KCTD6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NC69
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000168301-KCTD6/subcellular

![](https://images.proteinatlas.org/36101/593_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36101/593_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36101/594_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36101/594_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36101/596_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36101/596_G11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NC69-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NC69 |
| SMART | SM00225; |
| UniProt Domain [FT] | DOMAIN 12..81; /note="BTB" |
| InterPro | IPR000210;IPR011333;IPR003131; |
| Pfam | PF02214; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168301-KCTD6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL3 | Intact, Biogrid | true |
| EHHADH | Intact, Biogrid, Bioplex | true |
| ACTN1 | Intact | false |
| ANK1 | Biogrid | false |
| BAG4 | Intact | false |
| C8orf33 | Intact | false |
| CDC23 | Intact | false |
| FAM124B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
