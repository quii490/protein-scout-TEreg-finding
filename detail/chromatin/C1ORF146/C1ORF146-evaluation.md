---
type: gene-evaluation
gene: C1ORF146
date: 2026-06-28
tags: [chromatin, chromosome, meiosis, synaptonemal-complex, recombination]
status: shortlisted
---

# C1ORF146 (SPO16) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C1ORF146 (SPO16) |
| **UniProt Accession** | Q5VVC0 |
| **Protein Name** | Protein SPO16 homolog |
| **Protein Length** | 180 aa |
| **Molecular Function** | Synaptonemal complex stabilization |
| **Chromosome** | 1p34.3 |
| **PubMed Hits** | 0 (no Gene-indexed publications) |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Chromosome** | ×4 | ×4 | 16 | Direct chromosomal association |
| **GO-CC: Nucleus (implicit)** | ×3 | ×4 | 12 | Synaptonemal complex = nuclear |
| **Meiotic Function** | ×3 | ×5 | 15 | SC stabilization and recombination |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×2 | ×2 | 4 | LMO1 (nuclear transcription factor) |
| **Literature Evidence** | ×1 | ×3 | 3 | No direct PubMed publications |
| **Total** | | | **53** | |



| **加权总分** | | | **53.0/180** | |
| **归一化总分 (÷1.83)** | | | **29.0/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
SPO16 (C1ORF146) plays a key role in reinforcing the integrity of the central element of the synaptonemal complex (SC), stabilizing SC and ensuring progression of meiotic prophase I in male and female germ cells. It promotes homologous recombination and crossing-over in meiotic prophase I via its association with SHOC1. It is required for the localization of TEX11 and MSH4 to recombination intermediates.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Chromosome (GO:0005694) - sole cellular compartment annotation
- **UniProt annotation**: "Chromosome"
- The synaptonemal complex is a meiosis-specific nuclear structure that assembles between homologous chromosomes
- SPO16 localizes to the central element of the SC

### 3.3 Domain Architecture
SPO16 is a small protein of 180 aa. It contains regions mediating interaction with SHOC1 and other SC components. The compact size suggests it functions primarily as a structural adaptor or stabilizer within the SC central element.

### 3.4 Protein-Protein Interactions
- **CST8 (Cystatin 8)**: Protease inhibitor, testis-specific
- **LMO1 (LIM domain only 1)**: Nuclear transcription factor involved in development
- **CDSN (Corneodesmosin)**: Epidermal adhesion protein (likely non-physiological)
- The interaction with LMO1 suggests potential nuclear regulatory connections

### 3.5 Relevance to TE Regulation
SPO16 connects to TE regulation through meiotic genome defense:
- The synaptonemal complex is crucial for proper chromosome segregation during meiosis
- Meiotic recombination provides a surveillance mechanism against TE insertions
- The piRNA pathway in the germline targets TEs during meiosis
- SC components interact with DNA damage response pathways that recognize TE-induced lesions

## 4. Overall Assessment

**Classification: chromatin** - Chromosome-associated protein functioning in the synaptonemal complex during meiosis.

**Strengths**:
- Direct chromatin/chromosome localization
- Essential role in meiotic chromosome dynamics
- Connection to recombination machinery (SHOC1, TEX11, MSH4)

**Weaknesses**:
- Zero PubMed publications indexed by gene
- Function inferred primarily from orthology (By similarity evidence codes)
- Germline-specific expression
- Very small protein (180 aa) with limited domain information
- No HPA data

**Recommendation: Shortlist with caution.** SPO16 has clear nuclear/chromosomal localization through its role in the synaptonemal complex. However, the lack of direct human studies and germline-restricted expression limit its priority for TE regulation evaluation.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HFM1 | STRING | 885 |
| MSH4 | STRING | 863 |
| G7 | STRING | 810 |
| MSH5-SAPCD1 | STRING | 810 |
| MSH5 | STRING | 810 |
| LMO1 | BioGRID | 1 |
| TSC22D4 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000203910-C1orf146

![](https://images.proteinatlas.org/74051/2036_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/2036_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000203910-C1orf146

![](https://images.proteinatlas.org/74051/2036_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/2036_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000203910-C1orf146

![](https://images.proteinatlas.org/74051/2036_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/2036_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74051/1943_A8_3_blue_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C1ORF146

## 5. Data Sources

- UniProt: Q5VVC0 (accessed 2026-06-28 via REST API)
- GO-CC: chromosome (GO:0005694)
- BioGRID PPI: human PPI dataset (CST8, LMO1, CDSN interactions)
- HPA: unclassified_bare (no nuclear localization data)
- Note: All functional annotations are by similarity (ECO:0000250)

### 深度机制分析

**结构域架构**：C1ORF146/SPO16（UniProt Q5VVC0，180 aa）是一个极为紧凑的蛋白，仅有180个氨基酸残基。如此小尺寸提示其作为结构衔接子或稳定性因子在联会复合体（synaptonemal complex, SC）中央元件中发挥作用，而非催化性角色。目前无实验结构或AlphaFold覆盖的详细域信息，但序列分析预测其存在与SHOC1及其他SC组分交互的短线性基序。小蛋白体积意味着其功能极有可能通过诱导契合或变构调节来实现对SC中央元件的加固。

**PPI互作网络**：STRING互作数据显示HFM1（解旋酶，评分885）和MSH4/MutS家族错配修复蛋白（评分863）为其最高置信度功能伙伴，均属减数分裂重组核心因子。MSH5-SAPCD1复合体（评分810）和G7蛋白（评分810）的强关联表明SPO16嵌于cross-over形成通路。BioGRID证据中的LMO1（评分1）是核心转录因子，TSC22D4（评分1）是转录调控因子——这些互作虽评分较低，但提示SPO16可能通过间接方式与核转录调控网络连接。

**结构-功能关系**：SPO16是SHOC1-TEX11-MSH4重组中间体定位通路的关键节点。其功能机制高度依赖于蛋白-蛋白互作而非酶活性：SPO16通过结合SHOC1，将TEX11和MSH4募集至重组中间体。此过程中SPO16可能作为分子伴侣（adaptor），其小尺寸优势在于可在SC中央元件的拥挤空间中灵活穿行，同时与多个伴侣蛋白形成瞬时复合体。所有功能注释均为"By similarity"（基于酵母/小鼠同源物），人类SPO16的独立实验验证极度匮乏。

**TE调控机制**：SC是减数分裂特异性核结构，负责同源染色体配对和重组——这两过程均是对抗TE插入的基因组监视机制。SC组装的完整性与同源重组的精确度直接关联：SC缺陷可导致不完全的染色体配对和减数分裂停滞，此时未修复的DNA双链断裂可成为TE插入的热点。piRNA通路在减数分裂生殖细胞中靶向新生TE转录本，而SC组分与DNA损伤应答通路的交互是连接转座子监视与染色体动力学的关键桥梁。

**前沿意义**：SPO16的零篇PubMed人类基因索引文献使其成为研究新颖性极高的靶标。其180 aa的极简蛋白架构为结构生物学提供了一个理想的研究模型——如何用最少的残基实现SC中央元件的加固功能。但所有功能注释均基于序列相似性推断、缺乏直接实验验证的现实意味着功能解释存在较大不确定性，CRISPR-Cas9敲除后通过SYCP3/MLH1免疫荧光分析SC组装和交叉形成将是首要验证手段。
