---
type: protein-evaluation
gene: "CRYM"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRYM 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYM / THBP |
| 蛋白名称 | Ketimine reductase mu-crystallin |
| 蛋白大小 | 314 aa / 33.8 kDa |
| UniProt ID | Q14894 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 33.8 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=90 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.0; PDB: 2I99 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036291, IPR003462, IPR023401; Pfam: PF02423 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- peroxisomal matrix (GO:0005782)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 90 |
| PubMed broad count | 106 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: THBP |

**关键文献**:
1. Emerging role of T3-binding protein μ-crystallin (CRYM) in health and disease.. *Trends in endocrinology and metabolism: TEM*. PMID: 36344381
2. Gene expression patterns of CRYM and SIGLEC10 in Alzheimer's disease: potential early diagnostic indicators.. *Molecular biology reports*. PMID: 38401023
3. µ-Crystallin: A thyroid hormone binding protein.. *Endocrine regulations*. PMID: 34020530
4. μ-Crystallin controls muscle function through thyroid hormone action.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 26718889
5. {mu}-Crystallin, new candidate protein in endotoxin-induced uveitis.. *Investigative ophthalmology & visual science*. PMID: 20570996

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.0 |
| 高置信度残基 (pLDDT>90) 占比 | 94.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.5% |
| 可用 PDB 条目 | 2I99 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.0，有序区 97.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036291, IPR003462, IPR023401; Pfam: PF02423 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| L3HYPDH | 0.940 | 0.000 | — |
| ARG2 | 0.793 | 0.000 | — |
| AGMAT | 0.786 | 0.000 | — |
| ARG1 | 0.786 | 0.000 | — |
| CRYBB1 | 0.638 | 0.051 | — |
| CBS | 0.590 | 0.000 | — |
| CBSL | 0.590 | 0.000 | — |
| LBHD1 | 0.557 | 0.000 | — |
| SLC16A2 | 0.555 | 0.000 | — |
| CRYBA1 | 0.548 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Atp6v1a | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22707207|imex:IM-17710 |
| RNF126 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTNR1B | psi-mi:"MI:0096"(pull down) | pubmed:26514267|imex:IM-24624 |
| FCGR2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OPTN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| NSF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.0 + PDB: 2I99 | pLDDT=96.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CRYM — Ketimine reductase mu-crystallin，研究基础较多，新颖性有限。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 90 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14894
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103316-CRYM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14894
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000103316-CRYM/subcellular

![](https://images.proteinatlas.org/30619/1310_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30619/1310_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30619/1312_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30619/1312_G7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/30619/1652_G3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30619/1652_G3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14894-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14894 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036291;IPR003462;IPR023401; |
| Pfam | PF02423; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103316-CRYM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NSF | Bioplex | false |
| OPTN | Intact | false |
| TERF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
