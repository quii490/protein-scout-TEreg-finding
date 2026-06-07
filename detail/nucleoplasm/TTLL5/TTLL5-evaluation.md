---
type: protein-evaluation
gene: "TTLL5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTLL5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTLL5 / KIAA0998, STAMP |
| 蛋白名称 | Tubulin polyglutamylase TTLL5 |
| 蛋白大小 | 1281 aa / 143.6 kDa |
| UniProt ID | Q6EMB2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cell projection, cilium; Cytoplasm, cytoskeleton, cilium bas |
| 蛋白大小 | 5/10 | ×1 | 5 | 1281 aa / 143.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004344; Pfam: PF03133 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cell projection, cilium; Cytoplasm, cytoskeleton, cilium basal body; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0998, STAMP |

**关键文献**:
1. Impact of Next Generation Sequencing in Unraveling the Genetics of 1036 Spanish Families With Inherited Macular Dystrophies.. *Investigative ophthalmology & visual science*. PMID: 35119454
2. Disruption of Ttll5/stamp gene (tubulin tyrosine ligase-like protein 5/SRC-1 and TIF2-associated modulatory protein gene) in male mice causes sperm malformation and infertility.. *The Journal of biological chemistry*. PMID: 23558686
3. Impaired glutamylation of RPGR(ORF15) underlies the cone-dominated phenotype associated with truncating distal ORF15 variants.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 36445968
4. Novel TTLL5 Variants Associated with Cone-Rod Dystrophy and Early-Onset Severe Retinal Dystrophy.. *International journal of molecular sciences*. PMID: 34203883
5. TTLL1 and TTLL4 polyglutamylases are required for the neurodegenerative phenotypes in pcd mice.. *PLoS genetics*. PMID: 35404950

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 27.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 48.3% |
| 有序区域 (pLDDT>70) 占比 | 46.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 46.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004344; Pfam: PF03133 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC14 | 0.731 | 0.693 | — |
| TSC22D3 | 0.713 | 0.000 | — |
| RPGR | 0.620 | 0.000 | — |
| C8orf37 | 0.588 | 0.000 | — |
| TTLL4 | 0.577 | 0.000 | — |
| CCDC138 | 0.576 | 0.000 | — |
| ATAT1 | 0.567 | 0.000 | — |
| AGBL5 | 0.567 | 0.000 | — |
| AGTPBP1 | 0.559 | 0.000 | — |
| IQCG | 0.545 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDKN1A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Lim1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG17450 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG5050 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| hpo | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14868 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| VWCE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CACNG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ODAD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 无 | pLDDT=61.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm, cytoskeleton,  / Plasma membrane, Cytosol | 一致 |
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
1. TTLL5 — Tubulin polyglutamylase TTLL5，非常新颖，仅有少数基础研究。
2. 蛋白大小1281 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6EMB2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119685-TTLL5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTLL5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6EMB2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000119685-TTLL5/subcellular

![](https://images.proteinatlas.org/32128/2148_G5_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/32128/2148_G5_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/32128/2165_E3_46_blue_red_green.jpg)
![](https://images.proteinatlas.org/32128/2165_E3_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/32128/376_D10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/32128/376_D10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6EMB2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6EMB2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 62..407; /note="TTL"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00568" |
| InterPro | IPR004344; |
| Pfam | PF03133; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119685-TTLL5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC14 | Biogrid | false |
| CEP135 | Biogrid | false |
| MVD | Opencell | false |
| PCM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
