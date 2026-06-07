---
type: protein-evaluation
gene: "STYK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STYK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STYK1 / NOK |
| 蛋白名称 | Tyrosine-protein kinase STYK1 |
| 蛋白大小 | 422 aa / 47.6 kDa |
| UniProt ID | Q6J9G0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 422 aa / 47.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR050122, IPR001245, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NOK |

**关键文献**:
1. Overexpression of the potential kinase serine/ threonine/tyrosine kinase 1 (STYK 1) in castration-resistant prostate cancer.. *Cancer science*. PMID: 19664042
2. STYK1 mediates NK cell anti-tumor response through regulating CCR2 and trafficking.. *Journal of translational medicine*. PMID: 39415235
3. Isolation and characterization of a human putative receptor protein kinase cDNA STYK1.. *Molecular biology reports*. PMID: 12841579
4. STYK1 promotes cancer cell proliferation and malignant transformation by activating PI3K-AKT pathway in gallbladder carcinoma.. *The international journal of biochemistry & cell biology*. PMID: 29413947
5. STYK1/NOK affects cell cycle late mitosis and directly interacts with anaphase-promoting complex activator CDH1.. *Heliyon*. PMID: 36506394

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 59.0% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 10.9% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.7，有序区 80.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR050122, IPR001245, IPR008266; Pfam: PF07714 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MPP6 | 0.766 | 0.059 | — |
| MPP5 | 0.698 | 0.059 | — |
| LIN7A | 0.650 | 0.000 | — |
| ERBB2 | 0.648 | 0.621 | — |
| PATJ | 0.642 | 0.000 | — |
| MPP1 | 0.436 | 0.059 | — |
| NSMCE1 | 0.430 | 0.000 | — |
| ITPKA | 0.407 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| HSP90AB4P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSP90AA5P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HIF1AN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| XPO1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| ATP1A1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| HSP90AA1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| CANX | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| BSG | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| ALDH3A2 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 1 / 8 = 12%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 12%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 无 | pLDDT=83.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STYK1 — Tyrosine-protein kinase STYK1，非常新颖，仅有少数基础研究。
2. 蛋白大小422 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6J9G0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000060140-STYK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STYK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6J9G0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000060140-STYK1/subcellular

![](https://images.proteinatlas.org/40468/1541_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/40468/1541_A4_3_red_green.jpg)
![](https://images.proteinatlas.org/40468/1542_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/40468/1542_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/40468/1599_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/40468/1599_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6J9G0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6J9G0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 114..384; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR000719;IPR050122;IPR001245;IPR008266; |
| Pfam | PF07714; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000060140-STYK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSP90AB1 | Intact, Biogrid | true |
| ALDH3A2 | Biogrid | false |
| ATG14 | Biogrid | false |
| BECN1 | Biogrid | false |
| CACNG4 | Bioplex | false |
| CDC37 | Biogrid | false |
| DSG2 | Biogrid | false |
| EMD | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
