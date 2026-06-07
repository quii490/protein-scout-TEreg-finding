---
type: protein-evaluation
gene: "SYNE3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYNE3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYNE3 / C14orf139, C14orf49, LINC00341 |
| 蛋白名称 | Nesprin-3 |
| 蛋白大小 | 975 aa / 112.2 kDa |
| UniProt ID | Q6ZMZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus outer membrane; Nucleus envelope; Rough endoplasmic  |
| 蛋白大小 | 8/10 | ×1 | 8 | 975 aa / 112.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.3; PDB: 6WME |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012315, IPR052403, IPR018159, IPR002017, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Supported |
| UniProt | Nucleus outer membrane; Nucleus envelope; Rough endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nuclear membrane (GO:0031965)
- nuclear outer membrane (GO:0005640)
- rough endoplasmic reticulum (GO:0005791)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf139, C14orf49, LINC00341 |

**关键文献**:
1. Twenty-Five Novel Loci for Carotid Intima-Media Thickness: A Genome-Wide Association Study in >45 000 Individuals and Meta-Analysis of >100 000 Individuals.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 34852643
2. Laminin-binding integrin gene copy number alterations in distinct epithelial-type cancers.. *American journal of translational research*. PMID: 27158381
3. p63 Transcription Factor Regulates Nuclear Shape and Expression of Nuclear Envelope-Associated Genes in Epidermal Keratinocytes.. *The Journal of investigative dermatology*. PMID: 28595999

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 33.8% |
| 置信残基 (pLDDT 70-90) 占比 | 47.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 10.7% |
| 有序区域 (pLDDT>70) 占比 | 81.4% |
| 可用 PDB 条目 | 6WME |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.3，有序区 81.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012315, IPR052403, IPR018159, IPR002017, IPR057932; Pfam: PF10541, PF00435, PF25803 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLEC | 0.998 | 0.124 | — |
| SUN2 | 0.998 | 0.911 | — |
| SUN1 | 0.984 | 0.124 | — |
| SYNE2 | 0.945 | 0.101 | — |
| SYNE4 | 0.943 | 0.000 | — |
| SYNE1 | 0.936 | 0.070 | — |
| SUN3 | 0.912 | 0.094 | — |
| MACF1 | 0.882 | 0.101 | — |
| CCDC155 | 0.848 | 0.095 | — |
| TOR1A | 0.847 | 0.125 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Syne1 | psi-mi:"MI:0096"(pull down) | imex:IM-24041|pubmed:22518138 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |
| ENST00000334258 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 6WME | pLDDT=80.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus outer membrane; Nucleus envelope; Rough en / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. SYNE3 — Nesprin-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小975 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZMZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176438-SYNE3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYNE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZMZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000176438-SYNE3/subcellular

![](https://images.proteinatlas.org/77140/1609_C3_3_red_green.jpg)
![](https://images.proteinatlas.org/77140/1609_C3_4_red_green.jpg)
![](https://images.proteinatlas.org/77140/1634_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/77140/1634_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/77140/1779_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/77140/1779_B9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZMZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZMZ3 |
| SMART | SM01249;SM00150; |
| UniProt Domain [FT] | DOMAIN 917..975; /note="KASH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00385" |
| InterPro | IPR012315;IPR052403;IPR018159;IPR002017;IPR057932;IPR057933; |
| Pfam | PF10541;PF00435;PF25803;PF25804; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176438-SYNE3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PRPF40A | Opencell | false |
| ST7 | Biogrid | false |
| SUN2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
