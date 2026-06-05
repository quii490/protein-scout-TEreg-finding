---
type: protein-evaluation
gene: "ETV1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETV1 — REJECTED (研究热度过高 (PubMed strict=332，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETV1 / ER81 |
| 蛋白名称 | ETS translocation variant 1 |
| 蛋白大小 | 477 aa / 55.1 kDa |
| UniProt ID | P50549 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 477 aa / 55.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=332 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 4AVP, 4BNC, 5ILS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR006715, IPR036388, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 332 |
| PubMed broad count | 547 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ER81 |

**关键文献**:
1. The Molecular Taxonomy of Primary Prostate Cancer.. *Cell*. PMID: 26544944
2. Recurrent fusion of TMPRSS2 and ETS transcription factor genes in prostate cancer.. *Science (New York, N.Y.)*. PMID: 16254181
3. Integrated analysis of ATAC-seq and RNA-seq reveals the transcriptional regulation network in SLE.. *International immunopharmacology*. PMID: 36738683
4. ETS factors in prostate cancer.. *Cancer letters*. PMID: 35033589
5. Copy Number Variation and Osteoporosis.. *Current osteoporosis reports*. PMID: 36795294

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 19.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 22.9% |
| 低置信 (pLDDT<50) 占比 | 52.2% |
| 有序区域 (pLDDT>70) 占比 | 25.0% |
| 可用 PDB 条目 | 4AVP, 4BNC, 5ILS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 25.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR006715, IPR036388, IPR036390; Pfam: PF00178, PF04621 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMPRSS2 | 0.942 | 0.000 | — |
| COP1 | 0.901 | 0.850 | — |
| SLC45A3 | 0.892 | 0.000 | — |
| AR | 0.884 | 0.000 | — |
| EWSR1 | 0.884 | 0.000 | — |
| DET1 | 0.863 | 0.809 | — |
| STK40 | 0.837 | 0.835 | — |
| DUX4 | 0.789 | 0.000 | — |
| KIT | 0.773 | 0.000 | — |
| FUS | 0.752 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCND3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PRKDC | psi-mi:"MI:0096"(pull down) | pubmed:21575865|imex:IM-16532 |
| XRCC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21575865|imex:IM-16532 |
| PARP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21575865|imex:IM-16532 |
| XRCC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21575865|imex:IM-16532 |
| DET1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STK40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 4AVP, 4BNC, 5ILS | pLDDT=58.5, v6 | 预测+实验 |
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
1. ETV1 — ETS translocation variant 1，研究基础较多，新颖性有限。
2. 蛋白大小477 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 332 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 332 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50549
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006468-ETV1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETV1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50549
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000006468-ETV1/subcellular

![](https://images.proteinatlas.org/77249/1609_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/77249/1609_F11_5_red_green.jpg)
![](https://images.proteinatlas.org/77249/1623_B11_4_red_green.jpg)
![](https://images.proteinatlas.org/77249/1623_B11_5_red_green.jpg)
![](https://images.proteinatlas.org/77249/1634_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/77249/1634_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50549-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
