---
type: protein-evaluation
gene: "TCF20"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCF20 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCF20 / KIAA0292, SPBP |
| 蛋白名称 | Transcription factor 20 |
| 蛋白大小 | 1960 aa / 211.8 kDa |
| UniProt ID | Q9UGU0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1960 aa / 211.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=38.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034732, IPR041972, IPR052440, IPR001965, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0292, SPBP |

**关键文献**:
1. De novo and inherited TCF20 pathogenic variants are associated with intellectual disability, dysmorphic features, hypotonia, and neurological impairments with similarities to Smith-Magenis syndrome.. *Genome medicine*. PMID: 30819258
2. Epigenetic Regulation and Neurodevelopmental Disorders: From MeCP2 to the TCF20/PHF14 Complex.. *Genes*. PMID: 39766920
3. Association Between CYP2D7 and TCF20 Polymorphisms and Coronary Heart Disease.. *Cardiovascular toxicology*. PMID: 39060884
4. The value of genome-wide analysis in craniosynostosis.. *Frontiers in genetics*. PMID: 38318288
5. MeCP2 Interacts with the Super Elongation Complex to Regulate Transcription.. *bioRxiv : the preprint server for biology*. PMID: 39005382

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 38.9 |
| 高置信度残基 (pLDDT>90) 占比 | 4.7% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 89.6% |
| 有序区域 (pLDDT>70) 占比 | 7.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=38.9），有序残基占 7.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034732, IPR041972, IPR052440, IPR001965, IPR013083; Pfam: PF13771 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AR | 0.752 | 0.435 | — |
| ALB | 0.713 | 0.000 | — |
| MMP3 | 0.655 | 0.292 | — |
| GATAD2B | 0.639 | 0.479 | — |
| GATAD2A | 0.614 | 0.422 | — |
| HMG20A | 0.611 | 0.440 | — |
| RAI1 | 0.608 | 0.479 | — |
| H4C6 | 0.599 | 0.565 | — |
| RNF4 | 0.590 | 0.510 | — |
| PHF14 | 0.581 | 0.422 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPK14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TRIM63 | psi-mi:"MI:0096"(pull down) | pubmed:31391242|imex:IM-25805| |
| MAPK8 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| H2BC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FKBP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COPB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TRIM27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| GATAD2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=38.9 + PDB: 无 | pLDDT=38.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
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
1. TCF20 — Transcription factor 20，非常新颖，仅有少数基础研究。
2. 蛋白大小1960 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=38.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UGU0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100207-TCF20/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCF20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UGU0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100207-TCF20/subcellular

![](https://images.proteinatlas.org/36786/2264_D8_213_red_green.jpg)
![](https://images.proteinatlas.org/36786/2264_D8_240_red_green.jpg)
![](https://images.proteinatlas.org/36786/789_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/36786/789_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/36786/899_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/36786/899_B11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UGU0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
