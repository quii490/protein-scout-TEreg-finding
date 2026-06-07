---
type: protein-evaluation
gene: "IQCE"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IQCE 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IQCE / KIAA1023 |
| 蛋白名称 | IQ domain-containing protein E |
| 蛋白大小 | 695 aa / 77.3 kDa |
| UniProt ID | Q6IPM2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; 额外: Nuclear membrane, Primary ; UniProt: Cell projection, cilium membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 695 aa / 77.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052318, IPR000048; Pfam: PF00612 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Nuclear membrane, Primary cilium | Approved |
| UniProt | Cell projection, cilium membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary membrane (GO:0060170)
- cilium (GO:0005929)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1023 |

**关键文献**:
1. Variants in EFCAB7 underlie nonsyndromic postaxial polydactyly.. *European journal of human genetics : EJHG*. PMID: 37684519
2. Identification and Validation of Prognostically Relevant Gene Signature in Melanoma.. *BioMed research international*. PMID: 32462000
3. EVC-EVC2 complex stability and ciliary targeting are regulated by modification with ubiquitin and SUMO.. *Frontiers in cell and developmental biology*. PMID: 37576597
4. Exome Sequencing in a Large Cohort with Ciliopathy-Related Kidney Disease.. *Clinical journal of the American Society of Nephrology : CJASN*. PMID: 41343253
5. Multi-omics Mendelian randomization and machine learning identify candidate therapeutic targets for Alzheimer's and Parkinson's diseases.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 41543776

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.7% |
| 低置信 (pLDDT<50) 占比 | 36.0% |
| 有序区域 (pLDDT>70) 占比 | 48.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 48.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052318, IPR000048; Pfam: PF00612 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EFCAB7 | 0.994 | 0.075 | — |
| EVC2 | 0.884 | 0.000 | — |
| FAU | 0.806 | 0.789 | — |
| TTC23L | 0.761 | 0.699 | — |
| EVC | 0.736 | 0.046 | — |
| ZNF141 | 0.711 | 0.058 | — |
| TTC23 | 0.700 | 0.406 | — |
| KIAA0825 | 0.610 | 0.000 | — |
| TTC34 | 0.594 | 0.000 | — |
| FAM92A | 0.591 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HNRNPF | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GPSM3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TTC23 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TTC23L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RFFL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM27 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 无 | pLDDT=68.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium membrane / Nucleoplasm, Plasma membrane; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. IQCE — IQ domain-containing protein E，非常新颖，仅有少数基础研究。
2. 蛋白大小695 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IPM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106012-IQCE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IQCE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IPM2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106012-IQCE/subcellular

![](https://images.proteinatlas.org/19515/2185_G5_149_blue_red_green.jpg)
![](https://images.proteinatlas.org/19515/2185_G5_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/19515/2186_A5_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/19515/2186_A5_78_blue_red_green.jpg)
![](https://images.proteinatlas.org/19515/2201_A6_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/19515/2201_A6_79_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6IPM2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6IPM2 |
| SMART | SM00015; |
| UniProt Domain [FT] | DOMAIN 542..571; /note="IQ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116"; DOMAIN 601..630; /note="IQ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116" |
| InterPro | IPR052318;IPR000048; |
| Pfam | PF00612; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106012-IQCE/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PSMA3 | Intact, Biogrid | true |
| TTC23L | Intact, Biogrid | true |
| GPSM3 | Intact | false |
| HNRNPF | Intact | false |
| TTC23 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
