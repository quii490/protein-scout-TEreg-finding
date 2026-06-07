---
type: protein-evaluation
gene: "PBRM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PBRM1 — REJECTED (研究热度过高 (PubMed strict=385，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PBRM1 / BAF180, PB1 |
| 蛋白名称 | Protein polybromo-1 |
| 蛋白大小 | 1689 aa / 192.9 kDa |
| UniProt ID | Q86U86 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1689 aa / 192.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=385 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.8; PDB: 2KTB, 3G0J, 3HMF, 3IU5, 3IU6, 3K2J, 3LJW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001025, IPR043151, IPR001487, IPR036427, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- kinetochore (GO:0000776)
- nuclear chromosome (GO:0000228)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RSC-type complex (GO:0016586)
- SWI/SNF complex (GO:0016514)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 385 |
| PubMed broad count | 748 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAF180, PB1 |

**关键文献**:
1. Integrated Genomic Characterization of Pancreatic Ductal Adenocarcinoma.. *Cancer cell*. PMID: 28810144
2. Genomic correlates of response to immune checkpoint therapies in clear cell renal cell carcinoma.. *Science (New York, N.Y.)*. PMID: 29301960
3. Molecular Subsets in Renal Cancer Determine Outcome to Checkpoint and Angiogenesis Blockade.. *Cancer cell*. PMID: 33157048
4. Comprehensive molecular characterization of clear cell renal cell carcinoma.. *Nature*. PMID: 23792563
5. The Cancer Genome Atlas Comprehensive Molecular Characterization of Renal Cell Carcinoma.. *Cell reports*. PMID: 29617669

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.8 |
| 高置信度残基 (pLDDT>90) 占比 | 38.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 66.6% |
| 可用 PDB 条目 | 2KTB, 3G0J, 3HMF, 3IU5, 3IU6, 3K2J, 3LJW, 3MB4, 3TLP, 4Q0N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2KTB, 3G0J, 3HMF, 3IU5, 3IU6, 3K2J, 3LJW, 3MB4, 3TLP, 4Q0N）+ AlphaFold极高置信度预测（pLDDT=72.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001025, IPR043151, IPR001487, IPR036427, IPR018359; Pfam: PF01426, PF00439, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMARCE1 | 0.999 | 0.974 | — |
| SMARCC1 | 0.999 | 0.958 | — |
| SMARCA4 | 0.999 | 0.994 | — |
| ARID1A | 0.999 | 0.556 | — |
| ACTL6A | 0.999 | 0.957 | — |
| SMARCD1 | 0.999 | 0.991 | — |
| PHF10 | 0.999 | 0.950 | — |
| SMARCB1 | 0.999 | 0.992 | — |
| BRD7 | 0.999 | 0.968 | — |
| ARID2 | 0.999 | 0.985 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMARCA4 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12368262 |
| Esrrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| TRIM33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14704|pubmed:20603019 |
| SCHIP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| PHB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| yopM | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SMARCB1 | psi-mi:"MI:0096"(pull down) | imex:IM-26463|pubmed:30108113 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.8 + PDB: 2KTB, 3G0J, 3HMF, 3IU5, 3IU6,  | pLDDT=72.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. PBRM1 — Protein polybromo-1，研究基础较多，新颖性有限。
2. 蛋白大小1689 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 385 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 385 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86U86
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163939-PBRM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PBRM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86U86
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000163939-PBRM1/subcellular

![](https://images.proteinatlas.org/15629/126_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/15629/126_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/15629/1395_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/15629/1395_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/15629/165_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/15629/165_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86U86-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86U86 |
| SMART | SM00439;SM00297;SM00398; |
| UniProt Domain [FT] | DOMAIN 41..151; /note="Bromo 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 177..287; /note="Bromo 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 381..487; /note="Bromo 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 518..625; /note="Bromo 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 653..763; /note="Bromo 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 769..879; /note="Bromo 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00035"; DOMAIN 956..1074; /note="BAH 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00370"; DOMAIN 1156..1272; /note="BAH 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00370" |
| InterPro | IPR001025;IPR043151;IPR001487;IPR036427;IPR018359;IPR009071;IPR036910;IPR037968;IPR037382; |
| Pfam | PF01426;PF00439;PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163939-PBRM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARID2 | Intact, Biogrid | true |
| SMARCA4 | Intact, Biogrid | true |
| ACTL6A | Biogrid | false |
| AR | Biogrid | false |
| ARID1A | Biogrid | false |
| BCL7A | Biogrid | false |
| BCL7C | Biogrid | false |
| BRD2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
