---
type: protein-evaluation
gene: "THTPA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THTPA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THTPA |
| 蛋白名称 | Thiamine-triphosphatase |
| 蛋白大小 | 230 aa / 25.6 kDa |
| UniProt ID | Q9BU02 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 230 aa / 25.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.6; PDB: 3BHD, 3TVL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR033469, IPR023577, IPR039582, IPR012177; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Emergence of unique SARS-CoV-2 ORF10 variants and their impact on protein structure and function.. *International journal of biological macromolecules*. PMID: 34863825
2. The iron-regulated metastasis suppressor, Ndrg-1: identification of novel molecular targets.. *Biochimica et biophysica acta*. PMID: 18582504
3. High-throughput proteomics of breast cancer interstitial fluid: identification of tumor subtype-specific serologically relevant biomarkers.. *Molecular oncology*. PMID: 33176066
4. Molecular functions of the iron-regulated metastasis suppressor, NDRG1, and its potential as a molecular target for cancer therapy.. *Biochimica et biophysica acta*. PMID: 24269900
5. Cross-Species Meta-Analysis of Transcriptomic Data in Combination With Supervised Machine Learning Models Identifies the Common Gene Signature of Lactation Process.. *Frontiers in genetics*. PMID: 30050559

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 83.0% |
| 可用 PDB 条目 | 3BHD, 3TVL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3BHD, 3TVL）+ AlphaFold高质量预测（pLDDT=86.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033469, IPR023577, IPR039582, IPR012177; Pfam: PF01928 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D3DS50 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TLX3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| RTL8C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLPX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ITIH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AFG2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ORF10 | psi-mi:"MI:0096"(pull down) | imex:IM-28441|pubmed:33060197 |
| TEX13B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WDR59 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 3BHD, 3TVL | pLDDT=86.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. THTPA — Thiamine-triphosphatase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小230 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BU02
- Protein Atlas: https://www.proteinatlas.org/ENSG00000259431-THTPA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THTPA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BU02
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000259431-THTPA/subcellular

![](https://images.proteinatlas.org/28876/329_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/28876/329_G9_3_red_green.jpg)
![](https://images.proteinatlas.org/28876/332_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/28876/332_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/28876/334_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/28876/334_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BU02-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BU02 |
| SMART | SM01118; |
| UniProt Domain [FT] | DOMAIN 5..201; /note="CYTH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01044" |
| InterPro | IPR033469;IPR023577;IPR039582;IPR012177; |
| Pfam | PF01928; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000259431-THTPA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABCF2 | Bioplex | false |
| ATP1A3 | Bioplex | false |
| AURKB | Bioplex | false |
| CDC45 | Bioplex | false |
| CLPX | Bioplex | false |
| DHRS7B | Bioplex | false |
| DIMT1 | Bioplex | false |
| GTPBP6 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
