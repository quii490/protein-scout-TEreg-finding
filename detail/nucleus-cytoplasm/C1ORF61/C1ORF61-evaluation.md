---
type: gene-evaluation
gene: C1ORF61
date: 2026-06-28
tags: [nucleus-cytoplasm, transcription, FOS-pathway, neuronal-development]
status: shortlisted
---

# C1ORF61 (MIR9-1HG/CROC-4) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C1ORF61 (MIR9-1HG/CROC-4) |
| **UniProt Accession** | Q13536 |
| **Protein Name** | Protein CROC-4 |
| **Protein Length** | 156 aa |
| **Molecular Function** | Transcriptional coactivator, FOS pathway |
| **Chromosome** | 1q22 |
| **PubMed Hits** | 8 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | Sole subcellular annotation |
| **Transcription Function** | ×3 | ×5 | 15 | Promotes FOS transcription |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | DDX39A (nuclear RNA helicase), WAPAL (chromatin) |
| **Literature Evidence** | ×2 | ×3 | 6 | Known transcriptional role |
| **Total** | | | **46** | |



| **加权总分** | | | **46.0/180** | |
| **归一化总分 (÷1.83)** | | | **25.1/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
CROC-4 (C1ORF61) may play a role in FOS signaling pathways involved in development and remodeling of neurons. It promotes transcription of the FOS promoter, suggesting a transcriptional coactivator function in the nucleus.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus (GO:0005634) - sole cellular compartment annotation
- **UniProt annotation**: "Nucleus"
- Predicted nuclear localization is consistent with its role in transcriptional activation

### 3.3 Domain Architecture
CROC-4 is a small protein of 156 aa. No well-characterized domains are annotated in InterPro or Pfam. The compact size and lack of recognizable DNA-binding domains suggest it may function as a transcriptional coactivator rather than a direct DNA-binding transcription factor.

### 3.4 Protein-Protein Interactions
- **DDX39A**: DEAD-box RNA helicase involved in mRNA export and splicing - nuclear protein
- **WAPAL (WAPL)**: Cohesin regulator involved in chromatin organization - nuclear protein
- **FAM47E-S待验证1**: Readthrough transcript, function unclear
- Interaction with DDX39A and WAPL supports nuclear localization and function

### 3.5 Relevance to TE Regulation
CROC-4's role in transcriptional regulation connects to TE control:
- FOS/JUN (AP-1) transcription factors are activated by various stress signals including retrotransposon activity
- Transcriptional coactivators can modulate TE promoter activity
- Chromatin-associated interaction partners (WAPL) suggest potential chromatin-level TE regulation

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - The protein has nucleus-only GO-CC annotation and a transcriptional function, but it is a small, poorly characterized protein with no HPA data. The "nucleus-cytoplasm" classification is chosen conservatively since experimental subcellular localization data is absent. The protein could shuttle between nucleus and cytoplasm given its small size and lack of strong NLS signal.

**Strengths**:
- Nuclear GO-CC annotation
- Transcriptional function (FOS promoter activation)
- Nuclear PPI partners (DDX39A, WAPAL)

**Weaknesses**:
- Very small, poorly characterized protein
- No direct experimental subcellular localization
- No HPA data
- Limited functional studies

**Recommendation: Evaluate at lower priority.** The transcriptional role and nuclear annotations support nuclear localization, but the protein is poorly characterized. If resources permit, it warrants investigation for potential TE promoter regulation through AP-1 pathway modulation.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DDX39A | BioGRID | 1 |
| WAPAL | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C1ORF61

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 33915231 | C1orf61 promotes hepatocellular carcinoma metastasis and increases the therapeutic response to sorafenib. |
| 31395792 | Integrative analysis of DNA methylation and gene expression to identify key epigenetic genes in glioblastoma. |
| 30908634 | LncRNA CACNA1G-AS1 facilitates hepatocellular carcinoma progression through the miR-2392/C1orf61 pathway. |
| 29670510 | Differential Expression of Several miRNAs and the Host Genes AATK and DNM2 in Leukocytes of Sporadic ALS Patients. |
| 26200114 | Integrative Analysis of the Developing Postnatal Mouse Heart Transcriptome. |


## 5. Data Sources

- UniProt: Q13536 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634)
- BioGRID PPI: human PPI dataset (DDX39A, WAPAL, FAM47E-S待验证1 interactions)
- HPA: unclassified_bare (no nuclear localization data)
- PubMed: 8 total hits
