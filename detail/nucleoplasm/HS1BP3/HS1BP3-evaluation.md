---
type: protein-evaluation
gene: "HS1BP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HS1BP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HS1BP3 |
| 蛋白名称 | HCLS1-binding protein 3 |
| 蛋白大小 | 392 aa / 42.8 kDa |
| UniProt ID | Q53T59 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 392 aa / 42.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039701, IPR037901, IPR001683, IPR036871; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. HS1BP3 inhibits autophagy by regulation of PLD1.. *Autophagy*. PMID: 28318354
2. Genetics of essential tremor.. *Parkinsonism & related disorders*. PMID: 22166413
3. HS1BP3, transcriptionally regulated by ESR1, promotes hepatocellular carcinoma progression.. *Biochemical and biophysical research communications*. PMID: 35921704
4. HS1BP3 provides a novel mechanism of negative autophagy regulation through membrane lipids.. *Autophagy*. PMID: 28323521
5. Isolation and characterization of a novel HS1 SH3 domain binding protein, HS1BP3.. *International immunology*. PMID: 10590261

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.6 |
| 高置信度残基 (pLDDT>90) 占比 | 30.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 35.7% |
| 有序区域 (pLDDT>70) 占比 | 41.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.6），有序残基占 41.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039701, IPR037901, IPR001683, IPR036871; Pfam: PF00787 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHP1 | 0.764 | 0.000 | — |
| CTNS | 0.763 | 0.000 | — |
| HCLS1 | 0.669 | 0.095 | — |
| LDAH | 0.622 | 0.000 | — |
| TOR2A | 0.596 | 0.000 | — |
| REEP4 | 0.531 | 0.000 | — |
| SNX21 | 0.467 | 0.000 | — |
| TMED3 | 0.466 | 0.462 | — |
| SNX10 | 0.463 | 0.000 | — |
| LINGO4 | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMED3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FLT1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| TCP10L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANTXR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABTB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDXDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAD50 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| BRD4 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-21972|pubmed:24360279 |
| JMJD6 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-21972|pubmed:24360279 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.6 + PDB: 无 | pLDDT=66.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Cytosol | 一致 |
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
1. HS1BP3 — HCLS1-binding protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小392 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53T59
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118960-HS1BP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HS1BP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53T59
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000118960-HS1BP3/subcellular

![](https://images.proteinatlas.org/35050/376_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/35050/376_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/35050/378_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/35050/378_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/35050/383_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/35050/383_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q53T59-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q53T59 |
| SMART | SM00312; |
| UniProt Domain [FT] | DOMAIN 19..142; /note="PX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00147" |
| InterPro | IPR039701;IPR037901;IPR001683;IPR036871; |
| Pfam | PF00787; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000118960-HS1BP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BPIFA1 | Bioplex | false |
| CTSG | Bioplex | false |
| CTU1 | Bioplex | false |
| FGFR3 | Intact | false |
| GSN | Intact | false |
| IREB2 | Bioplex | false |
| PDXDC1 | Bioplex | false |
| PRPS1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
