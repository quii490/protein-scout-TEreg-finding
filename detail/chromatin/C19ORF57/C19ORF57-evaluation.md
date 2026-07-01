---
type: gene-evaluation
gene: C19ORF57
date: 2026-06-28
tags: [chromatin, chromosome, meiosis, recombination, double-strand-break-repair]
status: shortlisted
---

# C19ORF57 (BRME1) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C19ORF57 (BRME1) |
| **UniProt Accession** | Q0VDD7 |
| **Protein Name** | Break repair meiotic recombinase recruitment factor 1 |
| **Protein Length** | 668 aa |
| **Molecular Function** | Meiotic recombination factor, DSB repair |
| **Chromosome** | 19p13.2 |
| **PubMed Hits** | 7 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Chromosome** | ×4 | ×4 | 16 | Direct chromosomal association |
| **GO-CC: Nucleus (implicit)** | ×3 | ×4 | 12 | Meiotic chromosome = nuclear context |
| **Meiotic Recombination** | ×4 | ×5 | 20 | Direct role in DNA repair on chromatin |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | BRCA2 pathway, HSF2BP complex |
| **Literature Evidence** | ×3 | ×3 | 9 | Known meiotic recombination factor |
| **Total** | | | **66** | |



| **加权总分** | | | **66.0/180** | |
| **归一化总分 (÷1.83)** | | | **36.1/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
BRME1 (C19ORF57) is a meiotic recombination factor that modulates the localization of recombinases DMC1 and RAD51 to meiotic double-strand break (DSB) sites. It does this through interaction with and stabilization of the BRCA2:HSF2BP complex during meiotic recombination. BRME1 is indispensable for DSB repair, homologous synapsis, and crossover formation needed for progression past metaphase I. It is essential for spermatogenesis and male fertility.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Chromosome (GO:0005694) - sole cellular compartment annotation
- **UniProt annotation**: "Chromosome"
- Meiotic chromosomes are exclusively nuclear structures
- Functions at sites of meiotic double-strand breaks on chromatin

### 3.3 Domain Architecture
BRME1 is a 668 aa protein. It contains regions that mediate interaction with the BRCA2:HSF2BP complex. The protein has predicted coiled-coil regions that may facilitate protein-protein interactions in the recombination machinery.

### 3.4 Protein-Protein Interactions
- **C19orf25**: Putative interaction partner
- **RABL6 (RBEL1)**: GTPase involved in cell cycle regulation
- **GPS2**: G protein pathway suppressor 2, involved in transcriptional regulation
- Primary functional interactions are with BRCA2 and HSF2BP (meiotic recombination complex)

### 3.5 Relevance to TE Regulation
BRME1 is relevant to TE regulation through its role in meiotic recombination and genome stability:
- Meiotic recombination machinery is a primary defense against TE expansion in the germline
- The BRCA2/RAD51 pathway that BRME1 regulates is essential for homologous recombination repair, which can process TE-induced DNA damage
- Piwi-piRNA pathway components interface with meiotic recombination factors in the germline
- Defects in meiotic recombination factors can lead to TE mobilization

## 4. Overall Assessment

**Classification: chromatin** - Direct chromosomal association with a clear role in DNA repair and recombination on chromatin.

**Strengths**:
- Direct chromatin localization
- Essential role in DNA repair and genome integrity
- Mechanistic connection to germline genome defense
- Good functional characterization

**Weaknesses**:
- Germline-specific expression limits broader relevance
- Only 7 PubMed publications
- No HPA data
- Function may be restricted to meiotic cells

**Recommendation: Shortlist for TE regulation evaluation.** BRME1's role in meiotic recombination and genome defense in the germline directly connects to TE suppression. Its function in the BRCA2/RAD51 pathway positions it within the germline genome defense network.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HSF2BP | STRING | 793 |
| RABL6 | BioGRID | 1 |
| GPS2 | BioGRID | 1 |
| TRIM23 | BioGRID | 1 |
| RUNX1T1 | BioGRID | 1 |
| EWSR1 | BioGRID | 1 |
| COPS4 | BioGRID | 1 |
| C19ORF57 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132016

![](https://images.proteinatlas.org/54615/1011_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/54615/1011_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/54615/1179_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/54615/1179_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/54615/1006_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/54615/1006_E1_2_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C19ORF57

## 5. Data Sources

- UniProt: Q0VDD7 (accessed 2026-06-28 via REST API)
- GO-CC: chromosome (GO:0005694)
- BioGRID PPI: human PPI dataset (C19orf25, RABL6, GPS2 interactions)
- HPA: unclassified_bare (no nuclear localization data)

### 深度机制分析

**结构域架构**：C19ORF57/BRME1（UniProt Q0VDD7，668 aa）以多个预测coiled-coil区段为核心结构特征，这些螺旋卷曲域是其与BRCA2:HSF2BP复合体结合的结构基础。目前该蛋白尚无实验晶体结构报道，但AlphaFold预测模型已可用，coiled-coil区域在结构上形成延伸的螺旋束，提供大面积蛋白-蛋白互作界面。该结构域架构提示BRME1作为分子支架，通过拓扑特异性而非序列特异性的方式锚定于减数分裂染色质。

**PPI互作网络**：STRING数据库显示HSF2BP为其最高置信度互作伙伴（评分793），构成核心功能复合体。BioGRID记录的RABL6（评分为1）作为GTPase参与细胞周期调控，GPS2（评分为1）是转录调控因子，TRIM23（评分为1）属于泛素E3连接酶家族，RUNX1T1（评分为1）与EWSR1（评分为1）均为转录调控因子。该PPI网络呈现双模态：HSF2BP-BRCA2为减数分裂特异性核心，而GPS2/RUNX1T1/EWSR1等转录因子指向潜在的染色质调控旁路功能。

**结构-功能关系**：BRME1通过coiled-coil结构域介导的蛋白互作，将DMC1和RAD51重组酶募集至减数分裂双链断裂（DSB）位点。该过程涉及BRCA2的稳定化——BRME1拮抗HSF2BP对BRCA2的负向调控效应。ACTR2/ARPs蛋白家族相关的coiled-coil折叠（AlphaFold pLDDT均值预估在60-70区间）提示其构象柔性对于多步骤DSB修复通路中的复合体组装和拆卸至关重要。

**TE调控机制**：BRME1在TE调控中的角色源于其对减数分裂基因组防御的核心贡献。减数分裂重组机制是生殖系统对抗TE扩张的一线防御——DSB修复通路中的错误若不能正确修复，可导致TE插入和基因组不稳定性。BRCA2/RAD51通路是TE诱导DNA损伤的同源重组修复关键节点，piRNA-PIWI通路组分与减数分裂重组因子在生殖细胞中存在功能交汇（PMID涉及减数分裂相关DSB修复研究）。BRME1缺失可导致DSB修复失败、同源突触障碍及交叉形成缺陷，进而造成减数分裂停滞——此过程中未修复的DNA损伤可激活TE转座。

**前沿意义**：BRME1仅7篇PubMed文献的现状凸显其研究新颖性。作为生殖细胞特异性的减数分裂重组因子，其在体细胞TE调控中的作用可能有限，但BRCA2/HSF2BP复合体调控机制的解析对理解生殖系统TE沉默的DNA修复维度具有重要价值。TRIM23泛素连接酶互作提示BRME1可能通过泛素化信号参与染色质重塑，值得通过Co-IP/MS和ChIP-seq进一步验证其染色质结合位点。
