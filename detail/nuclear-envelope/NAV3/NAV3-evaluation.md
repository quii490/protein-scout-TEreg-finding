---
type: protein-evaluation
gene: "NAV3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAV3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAV3 / KIAA0938, POMFIL1, STEERIN3 |
| 蛋白名称 | Neuron navigator 3 |
| 蛋白大小 | 2385 aa / 255.6 kDa |
| UniProt ID | Q8IVL0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Cytosol; UniProt: Nucleus outer membrane; Cytoplasm, cytoskeleton |
| 蛋白大小 | 2/10 | ×1 | 2 | 2385 aa / 255.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR003959, IPR001715, IPR036872, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Cytosol | Approved |
| UniProt | Nucleus outer membrane; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- microtubule (GO:0005874)
- nuclear outer membrane (GO:0005640)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 99 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0938, POMFIL1, STEERIN3 |

**关键文献**:
1. Variants of NAV3, a neuronal morphogenesis protein, cause intellectual disability, developmental delay, and microcephaly.. *Communications biology*. PMID: 38977784
2. GWAS meta-analysis identifies five susceptibility loci for endometrial cancer.. *EBioMedicine*. PMID: 40633141
3. Microtubule-associated NAV3 regulates invasive phenotypes in glioblastoma cells.. *Brain pathology (Zurich, Switzerland)*. PMID: 39097525
4. NAV3 copy number changes and target genes in basal and squamous cell cancers.. *Experimental dermatology*. PMID: 21995814
5. NAV3, a Tumor Suppressor Gene, Is Decreased in Uterine Leiomyoma Tissue and Cells.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 32046415

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.2 |
| 高置信度残基 (pLDDT>90) 占比 | 10.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 69.7% |
| 有序区域 (pLDDT>70) 占比 | 26.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.2），有序残基占 26.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR003959, IPR001715, IPR036872, IPR057568; Pfam: PF00004, PF25408, PF00307 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNN1 | 0.703 | 0.000 | — |
| NAV2 | 0.648 | 0.610 | — |
| MEF2C | 0.611 | 0.000 | — |
| PDX1 | 0.610 | 0.610 | — |
| VPS9D1 | 0.610 | 0.610 | — |
| CSMD3 | 0.538 | 0.000 | — |
| ZFHX4 | 0.504 | 0.000 | — |
| SYT1 | 0.481 | 0.000 | — |
| XIRP2 | 0.476 | 0.052 | — |
| SPTA1 | 0.472 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| APC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| SERF2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Rab39b | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |
| ING5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CUX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBA3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PDX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PITRM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.2 + PDB: 无 | pLDDT=47.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus outer membrane; Cytoplasm, cytoskeleton / Nuclear membrane; 额外: Cytosol | 一致 |
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
1. NAV3 — Neuron navigator 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2385 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=47.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVL0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000067798-NAV3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAV3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVL0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000067798-NAV3/subcellular

![](https://images.proteinatlas.org/32111/1866_C4_1_cr5b6ac3c6e844c_blue_red_green.jpg)
![](https://images.proteinatlas.org/32111/1866_C4_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/32111/366_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/32111/366_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/32111/370_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/32111/370_F7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IVL0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
