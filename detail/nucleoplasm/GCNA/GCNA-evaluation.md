---
type: protein-evaluation
gene: "GCNA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GCNA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GCNA / ACRC |
| 蛋白名称 | Germ cell nuclear acidic protein |
| 蛋白大小 | 691 aa / 76.1 kDa |
| UniProt ID | Q96QF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, PML body; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 691 aa / 76.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006640; Pfam: PF10263 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus, PML body; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACRC |

**关键文献**:
1. Autophagy regulation and protein kinase activity of PIK3C3 controls sertoli cell polarity through its negative regulation on SCIN (scinderin).. *Autophagy*. PMID: 37450577
2. GCNA Interacts with Spartan and Topoisomerase II to Regulate Genome Stability.. *Developmental cell*. PMID: 31839538
3. GCNA is a histone binding protein required for spermatogonial stem cell maintenance.. *Nucleic acids research*. PMID: 36919611
4. GCNA Preserves Genome Integrity and Fertility Across Species.. *Developmental cell*. PMID: 31839537
5. From the TOP: Formation, recognition and resolution of topoisomerase DNA protein crosslinks.. *DNA repair*. PMID: 39180935

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 15.8% |
| 低置信 (pLDDT<50) 占比 | 56.2% |
| 有序区域 (pLDDT>70) 占比 | 28.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 28.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006640; Pfam: PF10263 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPRTN | 0.757 | 0.000 | — |
| TAF1 | 0.573 | 0.000 | — |
| DAZL | 0.543 | 0.000 | — |
| STRA8 | 0.537 | 0.000 | — |
| SYCP3 | 0.523 | 0.000 | — |
| FRMPD1 | 0.509 | 0.000 | — |
| FAM111A | 0.507 | 0.000 | — |
| TDP2 | 0.454 | 0.000 | — |
| NANOS3 | 0.447 | 0.000 | — |
| SPO11 | 0.439 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sumo | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cyp1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| sph | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Lsd-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 无 | pLDDT=58.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. GCNA — Germ cell nuclear acidic protein，非常新颖，仅有少数基础研究。
2. 蛋白大小691 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96QF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147174-GCNA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GCNA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96QF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000147174-GCNA/subcellular

![](https://images.proteinatlas.org/30870/1790_A9_4_red_green.jpg)
![](https://images.proteinatlas.org/30870/1790_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/30870/1861_G5_31_red_green.jpg)
![](https://images.proteinatlas.org/30870/1861_G5_32_red_green.jpg)
![](https://images.proteinatlas.org/30870/1916_F12_30_cr5c99de91a0356_red_green.jpg)
![](https://images.proteinatlas.org/30870/1916_F12_5_cr5c99de91a0081_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96QF7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96QF7 |
| SMART | SM00731; |
| UniProt Domain [FT] | DOMAIN 522..677; /note="SprT-like" |
| InterPro | IPR006640; |
| Pfam | PF10263; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147174-GCNA/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
