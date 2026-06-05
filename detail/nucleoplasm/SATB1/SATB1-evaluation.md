---
type: protein-evaluation
gene: "SATB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SATB1 — REJECTED (研究热度过高 (PubMed strict=521，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SATB1 |
| 蛋白名称 | DNA-binding protein SATB1 |
| 蛋白大小 | 763 aa / 86.0 kDa |
| UniProt ID | Q01826 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus matrix; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 763 aa / 86.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=521 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.3; PDB: 1YSE, 2L1P, 2MW8, 2O49, 2O4A, 3NZL, 3TUO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003350, IPR032355, IPR001356, IPR009057, IPR010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus matrix; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear body (GO:0016604)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 521 |
| PubMed broad count | 678 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The role of transcription factors in shaping regulatory T cell identity.. *Nature reviews. Immunology*. PMID: 37336954
2. Mutation-specific pathophysiological mechanisms define different neurodevelopmental disorders associated with SATB1 dysfunction.. *American journal of human genetics*. PMID: 33513338
3. SATB1 is a key regulator of quiescence in stem-like CD8(+) T cells.. *Nature immunology*. PMID: 40847243
4. Thymus and autoimmunity.. *Seminars in immunopathology*. PMID: 33537838
5. SATB1, senescence and senescence-related diseases.. *Journal of cellular physiology*. PMID: 38801120

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.3 |
| 高置信度残基 (pLDDT>90) 占比 | 27.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 41.9% |
| 有序区域 (pLDDT>70) 占比 | 51.0% |
| 可用 PDB 条目 | 1YSE, 2L1P, 2MW8, 2O49, 2O4A, 3NZL, 3TUO, 6LFF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.3），有序残基占 51.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003350, IPR032355, IPR001356, IPR009057, IPR010982; Pfam: PF02376, PF16557, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC1 | 0.949 | 0.636 | — |
| CASP6 | 0.867 | 0.294 | — |
| SATB2 | 0.810 | 0.693 | — |
| UBE2I | 0.738 | 0.551 | — |
| FOXP1 | 0.731 | 0.292 | — |
| PIAS1 | 0.725 | 0.490 | — |
| FOXP3 | 0.698 | 0.164 | — |
| GATA3 | 0.697 | 0.054 | — |
| EP300 | 0.690 | 0.292 | — |
| SMARCA5 | 0.686 | 0.302 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SUMO1 | psi-mi:"MI:0096"(pull down) | pubmed:18408014|imex:IM-17284 |
| CASP6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18408014|imex:IM-17284 |
| TOPORS | psi-mi:"MI:0018"(two hybrid) | pubmed:18408014|imex:IM-17284 |
| PIAS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:18408014|imex:IM-17284 |
| PIAS3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18408014|imex:IM-17284 |
| CBX4 | psi-mi:"MI:0018"(two hybrid) | pubmed:18408014|imex:IM-17284 |
| PIAS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18408014|imex:IM-17284 |
| tolC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.3 + PDB: 1YSE, 2L1P, 2MW8, 2O49, 2O4A,  | pLDDT=65.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix; Nucleus, PML body / Nucleoplasm; 额外: Nuclear bodies | 一致 |
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
1. SATB1 — DNA-binding protein SATB1，研究基础较多，新颖性有限。
2. 蛋白大小763 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 521 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 521 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01826
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182568-SATB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SATB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01826
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000182568-SATB1/subcellular

![](https://images.proteinatlas.org/51769/1042_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/51769/1042_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/51769/1423_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/51769/1423_G11_3_red_green.jpg)
![](https://images.proteinatlas.org/51769/761_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/51769/761_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01826-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
