---
type: gene-evaluation
gene: APBB2
date: 2026-06-28
tags: [nucleus-cytoplasm, APP-binding, transcription, ER-Golgi, adaptor-protein]
status: shortlisted
---

# APBB2 - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | APBB2 |
| **UniProt Accession** | Q92870 |
| **Protein Name** | Amyloid beta precursor protein binding family B member 2 |
| **Protein Length** | 758 aa |
| **Molecular Function** | Transcriptional coactivator, adaptor protein |
| **Chromosome** | 4p14-p13 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×3 | ×4 | 12 | Nuclear localization with transcriptional function |
| **Transcriptional Activity** | ×3 | ×5 | 15 | Activates APP transcription |
| **GO-CC: ER/Golgi/Endosome** | ×1 | ×1 | 1 | Also localizes to membrane compartments |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | APP (intracellular domain), EGFR signaling |
| **Literature Evidence** | ×2 | ×3 | 6 | Known adaptor with nuclear shuttling |
| **Total** | | | **43** | |



| **加权总分** | | | **43.0/180** | |
| **归一化总分 (÷1.83)** | | | **23.5/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
APBB2 (FE65-like 1) is an adaptor protein that binds the intracellular domain of amyloid precursor protein (APP). It activates transcription of APP and plays roles in lens transparency, muscle cell strength, hippocampal neurite branching, and spatial memory. APBB2 functions at the interface between membrane signaling and transcriptional regulation.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus, cytoplasm, early endosome, endoplasmic reticulum, Golgi apparatus, growth cone, lamellipodium, membrane
- **UniProt annotation**: "Endoplasmic reticulum; Golgi apparatus; Early endosome"
- APBB2 contains functional nuclear localization signals
- The protein shuttles between cytoplasm and nucleus, with nuclear import triggered by APP intracellular domain binding
- Known to activate transcription in the nucleus
- Nuclear localization is regulated and functionally significant

### 3.3 Domain Architecture
APBB2 is a 758 aa protein containing:
- **WW domain**: Binds proline-rich motifs (PPxY)
- **Two phosphotyrosine-binding (PTB) domains**: Mediate interaction with APP and other membrane proteins
- The PTB domains are also known as PID (phosphotyrosine interaction domain)

### 3.4 Protein-Protein Interactions
- **APP**: Primary binding partner; APP-APBB2 complex translocates to nucleus
- **EGFR**: Growth factor receptor signaling
- **APBB1 (FE65)**: Paralog with similar function
- APP intracellular domain (AICD) cleavage product binds APBB2 and triggers nuclear translocation

### 3.5 Relevance to TE Regulation
APBB2 has potential relevance to TE regulation through:
- Transcriptional coactivator function may influence TE promoter activity
- APP/AICD nuclear signaling pathway interfaces with chromatin
- Nuclear adaptor proteins can modulate transcriptional responses to cellular stress
- However, no direct evidence of TE or chromatin regulatory function

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Moderate confidence. APBB2 has a defined nuclear function as a transcriptional coactivator, but its nuclear localization is conditional on APP/AICD binding. The protein equally localizes to membrane compartments.

**Strengths**:
- Validated transcriptional coactivator function
- Known nuclear import mechanism (AICD-dependent)
- Well-studied protein

**Weaknesses**:
- Conditional nuclear localization
- Primary function is as a membrane-to-nucleus signaling adaptor
- No direct TE/chromatin connection
- No HPA data

**Recommendation: Evaluate at moderate priority.** The transcriptional coactivator function and nuclear shuttling mechanism make APBB2 worth considering for TE promoter regulation. However, the indirect connection to chromatin biology limits its priority.

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000163697-APBB2

![](https://images.proteinatlas.org/23542/196_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23542/196_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23542/195_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23542/195_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23542/197_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23542/197_A2_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00462;SM00456; |
| InterPro | IPR039576;IPR011993;IPR006020;IPR001202;IPR036020; |
| Pfam | PF00640;PF00397; |
| UniProt Domain [FT] | DOMAIN 290..322; /note="WW"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00224"; DOMAIN 413..578; /note="PID 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00148"; DOMAIN 584..736; /note="PID 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00148" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | STRING | 995 |
| APLP1 | STRING | 933 |
| APBA1 | STRING | 810 |
| EGFR | STRING | 738 |
| HSPA8 | BioGRID | 1 |
| TUBA1A | BioGRID | 1 |
| CBWD1 | BioGRID | 1 |
| WDR41 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/APBB2

### PubMed

**Count: 56**

| PMID | Title |
|---|---|
| 42098631 | Integrated transcriptomic and proteomic analyses reveal muscle fiber-type transformation in meat rabbits. |
| 42010059 | Immunopeptidome profiling in pulmonary fibrosis provides a platform for identifying therapeutic targets. |
| 41911647 | The TGFB1-Wnt/β-catenin axis programs a neuroprotective IGF1(+) microglial state during epileptogenesis. |
| 41876515 | Machine learning-based predictive models and subtypes patterns in peripheral blood of schizophrenia based on a machine learning computational framewor |
| 41207179 | Genetic susceptibility and validation of angiographic patterns in Takayasu arteritis. |


## 5. Data Sources

- UniProt: Q92870 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634), cytoplasm (GO:0005737), endoplasmic reticulum (GO:0005783), Golgi apparatus (GO:0005794)
- BioGRID PPI: human PPI dataset (APP, EGFR interactions)
- HPA: unclassified_bare (no nuclear localization data)
