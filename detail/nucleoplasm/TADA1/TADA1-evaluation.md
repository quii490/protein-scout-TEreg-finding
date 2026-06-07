---
type: protein-evaluation
gene: "TADA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TADA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TADA1 / TADA1L |
| 蛋白名称 | Transcriptional adapter 1 |
| 蛋白大小 | 335 aa / 37.4 kDa |
| UniProt ID | Q96BN2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Focal adhesion sites, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 335 aa / 37.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.0; PDB: 7KTR, 7KTS, 8H7G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024738; Pfam: PF12767 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Focal adhesion sites, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SAGA complex (GO:0000124)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TADA1L |

**关键文献**:
1. Genome-scale CRISPR-Cas9 knockout screening in human cells.. *Science (New York, N.Y.)*. PMID: 24336571
2. Bioinformatic analysis of the role of USP22 expression in hepatocellular carcinoma.. *International journal of clinical and experimental pathology*. PMID: 40814554
3. TaDA1, a conserved negative regulator of kernel size, has an additive effect with TaGW2 in common wheat (Triticum aestivum L.).. *Plant biotechnology journal*. PMID: 31733093
4. Species-specific function of microRNA-7702 in human colorectal cancer cells via targeting TADA1.. *American journal of translational research*. PMID: 30210694
5. SAGA Complex Subunit Hfi1 Is Important in the Stress Response and Pathogenesis of Cryptococcus neoformans.. *Journal of fungi (Basel, Switzerland)*. PMID: 38132798

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.0 |
| 高置信度残基 (pLDDT>90) 占比 | 37.0% |
| 置信残基 (pLDDT 70-90) 占比 | 37.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 15.5% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 7KTR, 7KTS, 8H7G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7KTR, 7KTS, 8H7G）+ AlphaFold高质量预测（pLDDT=77.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024738; Pfam: PF12767 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUPT20H | 0.999 | 0.991 | — |
| TAF6L | 0.999 | 0.990 | — |
| TAF9 | 0.999 | 0.991 | — |
| TRRAP | 0.999 | 0.996 | — |
| TAF5L | 0.999 | 0.991 | — |
| SUPT7L | 0.999 | 0.983 | — |
| TAF10 | 0.999 | 0.996 | — |
| TAF12 | 0.999 | 0.996 | — |
| SUPT3H | 0.999 | 0.995 | — |
| KAT2B | 0.998 | 0.907 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMEM98 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MUC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STOM | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GJB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLM1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SUSD3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATP1B3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| USP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Kat2a | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.0 + PDB: 7KTR, 7KTS, 8H7G | pLDDT=77.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Focal adhesion sites, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TADA1 — Transcriptional adapter 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小335 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BN2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152382-TADA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TADA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BN2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000152382-TADA1/subcellular

![](https://images.proteinatlas.org/28651/281_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/28651/281_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/28651/282_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/28651/282_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/28651/283_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/28651/283_A5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96BN2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BN2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024738; |
| Pfam | PF12767; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000152382-TADA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ENY2 | Biogrid, Opencell | true |
| SF3B5 | Biogrid, Opencell | true |
| SGF29 | Biogrid, Bioplex | true |
| SUPT20H | Biogrid, Bioplex | true |
| TADA2B | Biogrid, Bioplex | true |
| TAF10 | Biogrid, Bioplex | true |
| TAF12 | Biogrid, Opencell | true |
| TAF5L | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
