---
type: protein-evaluation
gene: "NMRK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NMRK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NMRK1 / C9orf95, NRK1 |
| 蛋白名称 | Nicotinamide riboside kinase 1 |
| 蛋白大小 | 199 aa / 23.2 kDa |
| UniProt ID | Q9NWW6 |
| 数据采集时间 | 2026-06-03 23:49:12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Centrosome; UniProt: 无注释 |
| 蛋白大小 | 8/10 | x1 | 8 | 199 aa / 23.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=7 篇 (<= 20 -> 10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=93.7; PDB: 2P0E, 2QG6, 2QL6, 2QSY, 2QSZ, 2QT0, |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR027417; Pfam: PF13238 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | -- | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf95, NRK1 |

**关键文献**:
1. Identification of the shared gene signatures and pathways between sarcopenia and type 2 diabetes mellitus.. *PloS one*. PMID: 35271662
2. Overexpression of NRK1 ameliorates diet- and age-induced hepatic steatosis and insulin resistance.. *Biochemical and biophysical research communications*. PMID: 29678570
3. Identification of BMAL1-Regulated circadian genes in mouse liver and their potential association with hepatocellular carcinoma: Gys2 and Upp2 as promising candidates.. *Biochemical and biophysical research communications*. PMID: 38183795
4. RORB gene and 9q21.13 microdeletion: report on a patient with epilepsy and mild intellectual disability.. *European journal of medical genetics*. PMID: 24355400
5. Genome-wide Association Study of 24-Hour Urinary Excretion of Calcium, Magnesium, and Uric Acid.. *Mayo Clinic proceedings. Innovations, quality & outcomes*. PMID: 31993563

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 86.9% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 92.4% |
| 可用 PDB 条目 | 2P0E, 2QG6, 2QL6, 2QSY, 2QSZ, 2QT0, 2QT1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2P0E, 2QG6, 2QL6, 2QSY, 2QSZ, 2QT0, 2QT1）+ AlphaFold极高置信度预测（pLDDT=93.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417; Pfam: PF13238 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NMNAT1 | 0.983 | 0.000 | — |
| NAPRT | 0.978 | 0.116 | — |
| NMNAT2 | 0.974 | 0.000 | — |
| QPRT | 0.971 | 0.000 | — |
| NAMPT | 0.971 | 0.000 | — |
| PNP | 0.959 | 0.115 | — |
| NUDT12 | 0.922 | 0.053 | — |
| NMRK2 | 0.910 | 0.000 | — |
| ENPP3 | 0.906 | 0.000 | — |
| ENPP1 | 0.901 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| REL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| INCA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TAX1BP1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| KCTD21 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ECE1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-30316|pubmed:38413612| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 2P0E, 2QG6, 2QL6, 2QSY, 2QSZ,  | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NMRK1 -- Nicotinamide riboside kinase 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106733-NMRK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NMRK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWW6
- STRING: https://string-db.org/network/9606.NMRK1
- Packet data timestamp: 2026-06-03 23:49:12

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106733-NMRK1/subcellular

![](https://images.proteinatlas.org/49795/1177_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/49795/1177_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/49795/728_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/49795/728_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/49795/748_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/49795/748_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NWW6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NWW6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417; |
| Pfam | PF13238; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106733-NMRK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| INCA1 | Intact | false |
| KCTD21 | Intact | false |
| TAX1BP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
