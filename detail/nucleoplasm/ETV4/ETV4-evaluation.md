---
type: protein-evaluation
gene: "ETV4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETV4 — REJECTED (研究热度过高 (PubMed strict=327，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETV4 / E1AF, PEA3 |
| 蛋白名称 | ETS translocation variant 4 |
| 蛋白大小 | 484 aa / 53.9 kDa |
| UniProt ID | P43268 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli rim; 额外: Mitotic chromosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 484 aa / 53.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=327 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 4CO8, 4UUV, 5ILU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR006715, IPR036388, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Mitotic chromosome | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 327 |
| PubMed broad count | 531 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: E1AF, PEA3 |

**关键文献**:
1. α-Ketoglutarate alleviates osteoarthritis by inhibiting ferroptosis via the ETV4/SLC7A11/GPX4 signaling pathway.. *Cellular & molecular biology letters*. PMID: 38877424
2. Transcription factor ETV4 promotes the development of hepatocellular carcinoma by driving hepatic TNF-α signaling.. *Cancer communications (London, England)*. PMID: 37670477
3. CIC-Rearranged Sarcoma.. *Surgical pathology clinics*. PMID: 38278603
4. Profiling the heterogeneity of colorectal cancer consensus molecular subtypes using spatial transcriptomics.. *NPJ precision oncology*. PMID: 38200223
5. Robust gene expression programs underlie recurrent cell states and phenotype switching in melanoma.. *Nature cell biology*. PMID: 32753671

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 16.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 18.0% |
| 低置信 (pLDDT<50) 占比 | 58.9% |
| 有序区域 (pLDDT>70) 占比 | 23.1% |
| 可用 PDB 条目 | 4CO8, 4UUV, 5ILU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 23.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR006715, IPR036388, IPR036390; Pfam: PF00178, PF04621 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCOA3 | 0.963 | 0.071 | — |
| COP1 | 0.852 | 0.777 | — |
| EWSR1 | 0.821 | 0.000 | — |
| TMPRSS2 | 0.782 | 0.000 | — |
| SLC45A3 | 0.756 | 0.000 | — |
| CD99 | 0.734 | 0.000 | — |
| GDNF | 0.719 | 0.000 | — |
| EPPIN | 0.714 | 0.000 | — |
| LPP | 0.696 | 0.000 | — |
| SCGB2A2 | 0.691 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-17394|pubmed:23275563 |
| HTT | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-17394|pubmed:23275563 |
| CARM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMAD4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| COP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:25117710|imex:IM-23043 |
| HOXD4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |
| ERF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EP300 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 4CO8, 4UUV, 5ILU | pLDDT=56.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli rim; 额外: Mitotic chromosome | 一致 |
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
1. ETV4 — ETS translocation variant 4，研究基础较多，新颖性有限。
2. 蛋白大小484 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 327 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 327 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43268
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175832-ETV4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETV4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43268
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (supported)。来源: https://www.proteinatlas.org/ENSG00000175832-ETV4/subcellular

![](https://images.proteinatlas.org/5768/1888_E1_5_red_green.jpg)
![](https://images.proteinatlas.org/5768/1888_E1_6_red_green.jpg)
![](https://images.proteinatlas.org/5768/63_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/5768/63_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/5768/93_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/5768/93_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P43268-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P43268 |
| SMART | SM00413; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000418;IPR046328;IPR006715;IPR036388;IPR036390; |
| Pfam | PF00178;PF04621; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175832-ETV4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFE2L2 | Intact, Biogrid | true |
| COP1 | Biogrid | false |
| HIF1A | Biogrid | false |
| SMAD2 | Biogrid | false |
| STK11 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
