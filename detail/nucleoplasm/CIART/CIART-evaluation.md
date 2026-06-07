---
type: protein-evaluation
gene: "CIART"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CIART 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIART / C1orf51 |
| 蛋白名称 | Circadian-associated transcriptional repressor |
| 蛋白大小 | 385 aa / 41.4 kDa |
| UniProt ID | Q8N365 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 385 aa / 41.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031373; Pfam: PF15673 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf51 |

**关键文献**:
1. A multi-organoid platform identifies CIART as a key factor for SARS-CoV-2 infection.. *Nature cell biology*. PMID: 36918693
2. Gene expression of circadian genes and CIART in bipolar disorder: A preliminary case-control study.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 36481223
3. Paclitaxel Chemotherapy Disrupts Circadian Gene Transcription and Function of the Suprachiasmatic Nuclei in Female Mice.. *eNeuro*. PMID: 40921688
4. Intestinal microbiota by angiotensin receptor blocker therapy exerts protective effects against hypertensive damages.. *iMeta*. PMID: 39135690
5. Unbiased multitissue transcriptomic analysis reveals complex neuroendocrine regulatory networks mediated by spinal cord injury-induced immunodeficiency.. *Journal of neuroinflammation*. PMID: 37775760

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.5 |
| 高置信度残基 (pLDDT>90) 占比 | 8.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 60.0% |
| 有序区域 (pLDDT>70) 占比 | 22.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.5），有序残基占 22.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031373; Pfam: PF15673 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARNTL | 0.782 | 0.095 | — |
| PER3 | 0.767 | 0.091 | — |
| CRY2 | 0.755 | 0.095 | — |
| BHLHE41 | 0.735 | 0.095 | — |
| PER2 | 0.719 | 0.095 | — |
| NR1D2 | 0.651 | 0.064 | — |
| CLOCK | 0.644 | 0.294 | — |
| NR1D1 | 0.620 | 0.000 | — |
| TEF | 0.611 | 0.000 | — |
| NPAS2 | 0.587 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NFYC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OGT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IGHA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TPM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DAB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| LAMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CASP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ZG16B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| UQCRQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BLVRA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.5 + PDB: 无 | pLDDT=54.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CIART — Circadian-associated transcriptional repressor，非常新颖，仅有少数基础研究。
2. 蛋白大小385 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N365
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159208-CIART/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIART
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N365
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000159208-CIART/subcellular

![](https://images.proteinatlas.org/54349/834_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/54349/834_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/54349/867_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/54349/867_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/54349/877_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/54349/877_B7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N365-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N365 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031373; |
| Pfam | PF15673; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159208-CIART/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BLVRA | Bioplex | false |
| CASP6 | Intact | false |
| DAB1 | Intact | false |
| HIBCH | Bioplex | false |
| PNPT1 | Bioplex | false |
| SPRYD4 | Bioplex | false |
| UQCRQ | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
