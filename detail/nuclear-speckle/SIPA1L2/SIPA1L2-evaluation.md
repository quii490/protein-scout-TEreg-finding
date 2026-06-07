---
type: protein-evaluation
gene: "SIPA1L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SIPA1L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIPA1L2 / KIAA1389 |
| 蛋白名称 | Signal-induced proliferation-associated 1-like protein 2 |
| 蛋白大小 | 1722 aa / 190.4 kDa |
| UniProt ID | Q9P2F8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nuclear membrane, Nuclear bodies; 额外: Golgi app; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1722 aa / 190.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001478, IPR036034, IPR035974, IPR000331, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane, Nuclear bodies; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- glutamatergic synapse (GO:0098978)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1389 |

**关键文献**:
1. Testing SIPA1L2 as a modifier of CMT1A using mouse models.. *Journal of neuropathology and experimental neurology*. PMID: 38472136
2. Testing SIPA1L2 as a modifier of CMT1A using mouse models.. *bioRxiv : the preprint server for biology*. PMID: 38076977
3. SIPA1L2 controls trafficking and local signaling of TrkB-containing amphisomes at presynaptic terminals.. *Nature communications*. PMID: 31784514
4. RNA‑seq analysis of predictive markers associated with glutamine metabolism in thyroid cancer.. *Molecular medicine reports*. PMID: 40183409
5. Variation in SIPA1L2 is correlated with phenotype modification in Charcot- Marie- Tooth disease type 1A.. *Annals of neurology*. PMID: 30706531

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.0 |
| 高置信度残基 (pLDDT>90) 占比 | 22.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 57.4% |
| 有序区域 (pLDDT>70) 占比 | 38.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.0），有序残基占 38.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001478, IPR036034, IPR035974, IPR000331, IPR050989; Pfam: PF00595, PF21022, PF02145 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAP1B | 0.913 | 0.110 | — |
| RAP1A | 0.909 | 0.110 | — |
| SIPA1 | 0.659 | 0.607 | — |
| SIPA1L1 | 0.655 | 0.597 | — |
| LZTS2 | 0.634 | 0.575 | — |
| SNAPIN | 0.614 | 0.000 | — |
| LZTS3 | 0.610 | 0.329 | — |
| LZTS1 | 0.589 | 0.589 | — |
| PRR35 | 0.575 | 0.000 | — |
| DDRGK1 | 0.567 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORC5 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TGM2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ENSP00000502693.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| mukB2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DYRK1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.0 + PDB: 无 | pLDDT=56.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nuclear membrane, Nuclear bodies; 额外: | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SIPA1L2 — Signal-induced proliferation-associated 1-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1722 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2F8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116991-SIPA1L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIPA1L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2F8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000116991-SIPA1L2/subcellular

![](https://images.proteinatlas.org/27224/1486_F10_5_red_green.jpg)
![](https://images.proteinatlas.org/27224/1486_F10_6_red_green.jpg)
![](https://images.proteinatlas.org/27224/1496_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/27224/1496_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/27224/1595_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/27224/1595_F6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2F8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2F8 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 595..812; /note="Rap-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00165"; DOMAIN 950..1026; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR001478;IPR036034;IPR035974;IPR000331;IPR050989;IPR021818; |
| Pfam | PF00595;PF21022;PF02145;PF11881; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116991-SIPA1L2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LZTS2 | Biogrid, Bioplex | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Biogrid, Opencell | true |
| YWHAG | Biogrid, Opencell | true |
| YWHAH | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
| CCZ1B | Bioplex | false |
| CEP135 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
