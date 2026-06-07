---
type: protein-evaluation
gene: "C20orf194"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C20orf194 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C20orf194 / C20orf194 |
| 蛋白名称 | Dynein axonemal assembly factor 9 |
| 蛋白大小 | 1177 aa / 132.3 kDa |
| UniProt ID | Q5TEA3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1177 aa / 132.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057478, IPR056414, IPR056498, IPR040342, IPR058 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf194 |

**关键文献**:
1. Discovery and validation of tissue-specific DNA methylation as noninvasive diagnostic markers for colorectal cancer.. *Clinical epigenetics*. PMID: 35974349
2. Weighted Gene Networks Derived from Multi-Omics Reveal Core Cancer Genes in Lung Cancer.. *Biology*. PMID: 40136480
3. Expansion of intronic GGCCTG hexanucleotide repeat in NOP56 causes SCA36, a type of spinocerebellar ataxia accompanied by motor neuron involvement.. *American journal of human genetics*. PMID: 21683323
4. The ITPA and C20orf194 Polymorphisms and Hematological Changes During Treatment With Pegylated-Interferon Plus Ribavirin in Patients With Chronic Hepatitis C.. *Hepatitis monthly*. PMID: 27148387
5. Identification of candidate genes and ceRNA networks of HPG axis in regulating sexual precocity of roosters by whole transcriptomic sequencing.. *BMC genomics*. PMID: 42185968

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 45.9% |
| 置信残基 (pLDDT 70-90) 占比 | 41.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 5.4% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.0，有序区 87.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057478, IPR056414, IPR056498, IPR040342, IPR058844; Pfam: PF23319, PF25204, PF23281 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARL3 | 0.706 | 0.556 | — |
| TBC1D19 | 0.616 | 0.000 | — |
| FEZ2 | 0.583 | 0.000 | — |
| TTBK2 | 0.565 | 0.000 | — |
| DYNLT3 | 0.525 | 0.429 | — |
| ITPA | 0.510 | 0.000 | — |
| DYNLT1 | 0.496 | 0.429 | — |
| SENP7 | 0.495 | 0.000 | — |
| WDR63 | 0.494 | 0.310 | — |
| DNAL4 | 0.489 | 0.307 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DNAAF9 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NUDCD3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| EBI-9357028 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| CDC37 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| CACYBP | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| EBI-9372282 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| PPP5C | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| ARL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HS1BP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 无 | pLDDT=84.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C20orf194 — Dynein axonemal assembly factor 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1177 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TEA3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088854-DNAAF9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C20orf194
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TEA3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000088854-DNAAF9/subcellular

![](https://images.proteinatlas.org/67418/1263_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/67418/1263_C6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/67418/1270_C6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/67418/1270_C6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/67418/1418_A2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/67418/1418_A2_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5TEA3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5TEA3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR057478;IPR056414;IPR056498;IPR040342;IPR058844;IPR058843; |
| Pfam | PF23319;PF25204;PF23281;PF25203;PF26246; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000088854-DNAAF9/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
