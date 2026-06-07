---
type: protein-evaluation
gene: "BUB3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BUB3 — REJECTED (研究热度过高 (PubMed strict=241，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BUB3 |
| 蛋白名称 | Mitotic checkpoint protein BUB3 |
| 蛋白大小 | 328 aa / 37.2 kDa |
| UniProt ID | O43684 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere, kinetochore |
| 蛋白大小 | 10/10 | ×1 | 10 | 328 aa / 37.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=241 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR020472, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- bub1-bub3 complex (GO:1990298)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- mitotic checkpoint complex (GO:0033597)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 241 |
| PubMed broad count | 393 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Deleterious Germline Mutations in Patients With Apparently Sporadic Pancreatic Adenocarcinoma.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 28767289
2. BUB3, beyond the Simple Role of Partner.. *Pharmaceutics*. PMID: 35631670
3. Functional profiling of murine glioma models highlights targetable immune evasion phenotypes.. *Acta neuropathologica*. PMID: 39592459
4. Research progress of Bub3 gene in malignant tumors.. *Cell biology international*. PMID: 34882895
5. CAFs promote immune evasion in gastric cancer through histone lactylation-mediated suppression of NCAPG ubiquitination.. *Journal of translational medicine*. PMID: 40898336

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.0 |
| 高置信度残基 (pLDDT>90) 占比 | 92.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 98.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.0，有序区 98.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR020472, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BUB1 | 0.999 | 0.973 | — |
| CDC20 | 0.999 | 0.995 | — |
| BUB1B | 0.999 | 0.998 | — |
| CDC27 | 0.999 | 0.994 | — |
| MAD2L1 | 0.999 | 0.845 | — |
| ANAPC4 | 0.998 | 0.994 | — |
| ZNF207 | 0.997 | 0.919 | — |
| KNL1 | 0.996 | 0.267 | — |
| MAD1L1 | 0.980 | 0.435 | — |
| CDC23 | 0.979 | 0.803 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BUB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TEF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BubR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| BuGZ | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CDC20 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15879521|imex:IM-19342 |
| CDC27 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15879521|imex:IM-19342 |
| MAD3 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15879521|imex:IM-19342 |
| MAD2 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15879521|imex:IM-19342 |
| MAD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11726501|imex:IM-19053| |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.0 + PDB: 无 | pLDDT=96.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BUB3 — Mitotic checkpoint protein BUB3，研究基础较多，新颖性有限。
2. 蛋白大小328 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 241 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 241 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43684
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154473-BUB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BUB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43684
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000154473-BUB3/subcellular

![](https://images.proteinatlas.org/3601/35_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/3601/35_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/3601/36_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/3601/36_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/3601/37_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/3601/37_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43684-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43684 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR020472;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154473-BUB3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANAPC4 | Biogrid, Opencell | true |
| BUB1 | Intact, Biogrid | true |
| BUB1B | Intact, Biogrid, Opencell | true |
| ZNF207 | Intact, Biogrid | true |
| ATXN1 | Intact | false |
| BRCA1 | Biogrid | false |
| CCT2 | Biogrid | false |
| CCT4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
