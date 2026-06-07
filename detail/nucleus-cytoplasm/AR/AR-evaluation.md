---
type: protein-evaluation
gene: "AR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AR — REJECTED (研究热度过高 (PubMed strict=20132，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AR / DHTR, NR3C4 |
| 蛋白名称 | Androgen receptor |
| 蛋白大小 | 920 aa / 99.2 kDa |
| UniProt ID | P10275 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 920 aa / 99.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=20132 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.3; PDB: 1E3G, 1GS4, 1T5Z, 1T63, 1T65, 1XJ7, 1XOW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001103, IPR035500, IPR000536, IPR050200, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20132 |
| PubMed broad count | 289143 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DHTR, NR3C4 |

**关键文献**:
1. Novel Therapeutic Strategies for Metastatic Prostate Cancer Care.. *European urology*. PMID: 40685286
2. Androgen insensitivity.. *American journal of medical genetics*. PMID: 10727996
3. Identification of diagnostic signature, molecular subtypes, and potential drugs in allergic rhinitis based on an inflammatory response gene set.. *Frontiers in immunology*. PMID: 38469312
4. Palmitoyl acyltransferase ZDHHC7 inhibits androgen receptor and suppresses prostate cancer.. *Oncogene*. PMID: 37198397
5. Genome-scale CRISPR screens identify PTGES3 as a direct modulator of androgen receptor function in advanced prostate cancer.. *Nature genetics*. PMID: 41193657

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.3 |
| 高置信度残基 (pLDDT>90) 占比 | 26.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 58.2% |
| 有序区域 (pLDDT>70) 占比 | 37.9% |
| 可用 PDB 条目 | 1E3G, 1GS4, 1T5Z, 1T63, 1T65, 1XJ7, 1XOW, 1XQ3, 1Z95, 2AM9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.3），有序残基占 37.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001103, IPR035500, IPR000536, IPR050200, IPR001628; Pfam: PF02166, PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCOA2 | 0.999 | 0.989 | — |
| NCOA4 | 0.999 | 0.988 | — |
| HSP90AB1 | 0.999 | 0.570 | — |
| HSP90AA1 | 0.999 | 0.901 | — |
| MDM2 | 0.998 | 0.920 | — |
| NCOA3 | 0.997 | 0.988 | — |
| KDM1A | 0.996 | 0.632 | — |
| FOXA1 | 0.996 | 0.761 | — |
| CTNNB1 | 0.996 | 0.888 | — |
| KLK3 | 0.995 | 0.872 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000484033.2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18734|pubmed:23518348 |
| IGLV6-57 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DAXX | psi-mi:"MI:0018"(two hybrid) | pubmed:15572661|imex:IM-25086 |
| KAT7 | psi-mi:"MI:0018"(two hybrid) | pubmed:10930412|imex:IM-19701| |
| NCOA4 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15563469 |
| NCOA2 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15563469 |
| SSA4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:22116683|imex:IM-16617 |
| TEF1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:22116683|imex:IM-16617 |
| SSA1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:22116683|imex:IM-16617 |
| TDH3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:22116683|imex:IM-16617 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.3 + PDB: 1E3G, 1GS4, 1T5Z, 1T63, 1T65,  | pLDDT=57.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. AR — Androgen receptor，研究基础较多，新颖性有限。
2. 蛋白大小920 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20132 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 20132 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10275
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169083-AR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10275
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000169083-AR/subcellular

![](https://images.proteinatlas.org/4733/1852_E2_16_cr5afd2f521f036_blue_red_green.jpg)
![](https://images.proteinatlas.org/4733/1852_E2_6_cr5afd2f521f015_blue_red_green.jpg)
![](https://images.proteinatlas.org/4733/1913_G3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4733/1913_G3_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/4733/1914_G6_27_cr5c8779fe8d0bf_blue_red_green.jpg)
![](https://images.proteinatlas.org/4733/1914_G6_5_cr5c8779fe8a87e_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P10275-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P10275 |
| SMART | SM00430;SM00399; |
| UniProt Domain [FT] | DOMAIN 669..900; /note="NR LBD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01189" |
| InterPro | IPR001103;IPR035500;IPR000536;IPR050200;IPR001628;IPR013088; |
| Pfam | PF02166;PF00104;PF00105; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169083-AR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASH2L | Intact, Biogrid | true |
| CCND1 | Intact, Biogrid | true |
| CREBBP | Intact, Biogrid | true |
| CTNNB1 | Intact, Biogrid | true |
| DAXX | Intact, Biogrid | true |
| DMAP1 | Intact, Biogrid | true |
| ERG | Intact, Biogrid | true |
| EZH2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
