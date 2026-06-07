---
type: protein-evaluation
gene: "SPIN2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPIN2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPIN2B / SPIN2 |
| 蛋白名称 | Spindlin-2B |
| 蛋白大小 | 258 aa / 29.2 kDa |
| UniProt ID | Q9BPZ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 258 aa / 29.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.7; PDB: 5LUG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003671, IPR042567; Pfam: PF02513 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPIN2 |

**关键文献**:
1. Exploring testicular miRNA profiles during developmental stages in Dezhou donkeys: A preliminary insight.. *Reproduction in domestic animals = Zuchthygiene*. PMID: 38059393
2. Comparative analysis of testis transcriptomes associated with male infertility in cattleyak.. *Theriogenology*. PMID: 27865410
3. Insights into X-Linked Susceptibility to Parkinson's Disease in the South African Population.. *medRxiv : the preprint server for health sciences*. PMID: 41480044

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 64.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 5LUG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.7，有序区 74.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003671, IPR042567; Pfam: PF02513 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPINDOC | 0.839 | 0.730 | — |
| SPIN1 | 0.818 | 0.814 | — |
| YRDC | 0.782 | 0.782 | — |
| CGGBP1 | 0.779 | 0.779 | — |
| TOPORS | 0.616 | 0.607 | — |
| WDR76 | 0.561 | 0.421 | — |
| MCM2 | 0.480 | 0.480 | — |
| SSRP1 | 0.480 | 0.478 | — |
| MYOZ1 | 0.476 | 0.000 | — |
| ARHGAP39 | 0.465 | 0.465 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOST | psi-mi:"MI:0096"(pull down) | pubmed:22206666|imex:IM-17213 |
| WDHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SSRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM122B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YRDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBR7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPINDOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 5LUG | pLDDT=80.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPIN2B — Spindlin-2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小258 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BPZ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186787-SPIN2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPIN2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BPZ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000186787-SPIN2B/subcellular

![](https://images.proteinatlas.org/69835/1337_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/69835/1337_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/69835/1338_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/69835/1338_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/69835/1511_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/69835/1511_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BPZ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BPZ2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003671;IPR042567; |
| Pfam | PF02513; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186787-SPIN2B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GALNS | Bioplex | false |
| SH3GLB1 | Intact | false |
| SPIN1 | Bioplex | false |
| SPINDOC | Bioplex | false |
| WDR76 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
