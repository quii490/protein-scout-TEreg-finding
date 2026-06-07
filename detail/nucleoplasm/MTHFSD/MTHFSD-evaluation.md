---
type: protein-evaluation
gene: "MTHFSD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MTHFSD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTHFSD |
| 蛋白名称 | Methenyltetrahydrofolate synthase domain-containing protein |
| 蛋白大小 | 383 aa / 42.2 kDa |
| UniProt ID | Q2M296 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 383 aa / 42.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=84.7; PDB: 2E5J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002698, IPR024185, IPR034359, IPR037171, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Copy number variations of MTHFSD gene across pig breeds and its association with litter size traits in Chinese indigenous Xiang pig.. *Journal of animal physiology and animal nutrition*. PMID: 29797367
2. MTHFSD and DDX58 are novel RNA-binding proteins abnormally regulated in amyotrophic lateral sclerosis.. *Brain : a journal of neurology*. PMID: 26525917
3. Associated effects of copy number variants on economically important traits in Spanish Holstein dairy cattle.. *Journal of dairy science*. PMID: 27209136
4. Rare homozygosity in amyotrophic lateral sclerosis suggests the contribution of recessive variants to disease genetics.. *Journal of the neurological sciences*. PMID: 31108397
5. Novel ABCD1 and MTHFSD Variants in Taiwanese Bipolar Disorder: A Genetic Association Study.. *Medicina (Kaunas, Lithuania)*. PMID: 40142297

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 65.8% |
| 置信残基 (pLDDT 70-90) 占比 | 17.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 13.3% |
| 有序区域 (pLDDT>70) 占比 | 83.0% |
| 可用 PDB 条目 | 2E5J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=84.7，有序区 83.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002698, IPR024185, IPR034359, IPR037171, IPR012677; Pfam: PF01812, PF00076 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FTCD | 0.858 | 0.000 | — |
| NOP56 | 0.825 | 0.000 | — |
| SMIM12 | 0.819 | 0.000 | — |
| SNU13 | 0.819 | 0.000 | — |
| UTP15 | 0.789 | 0.000 | — |
| MTHFD2L | 0.724 | 0.000 | — |
| MTHFD2 | 0.711 | 0.000 | — |
| MTHFD1 | 0.697 | 0.103 | — |
| MTHFD1L | 0.693 | 0.103 | — |
| WDR6 | 0.685 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| Nup155 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| REEP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| LRIF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EFCAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000381214 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 2E5J | pLDDT=84.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MTHFSD — Methenyltetrahydrofolate synthase domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小383 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2M296
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103248-MTHFSD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTHFSD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2M296
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000103248-MTHFSD/subcellular

![](https://images.proteinatlas.org/41333/486_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41333/486_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41333/490_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41333/490_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41333/509_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41333/509_E9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2M296-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2M296 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 306..379; /note="RRM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR002698;IPR024185;IPR034359;IPR037171;IPR012677;IPR035979;IPR000504; |
| Pfam | PF01812;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103248-MTHFSD/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
