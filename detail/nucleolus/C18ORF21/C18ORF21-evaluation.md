---
type: gene-evaluation
gene: C18ORF21
date: 2026-06-28
tags: [nucleolus, rRNA-processing, ribonucleoprotein, RNase-MRP]
status: shortlisted
---

# C18ORF21 (RMP24) - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | C18ORF21 (RMP24) |
| **UniProt Accession** | Q32NC0 |
| **Protein Name** | Ribonuclease MRP protein subunit p24 |
| **Protein Length** | 220 aa |
| **Molecular Function** | RNase MRP complex component |
| **Chromosome** | 18q21.1 |
| **PubMed Hits** | 8 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | Sole cellular compartment annotation |
| **GO-CC: Nucleolus** | ×3 | ×5 | 15 | RNase MRP processes pre-rRNA in nucleolus |
| **GO-CC: RNase MRP Complex** | ×4 | ×1 | 4 | Specific ribonucleoprotein complex |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | POP4, RPP25 (MRP/RNase P subunits) |
| **Literature Evidence** | ×2 | ×3 | 6 | Known nucleolar rRNA processing factor |
| **Total** | | | **50** | |



| **加权总分** | | | **50.0/180** | |
| **归一化总分 (÷1.83)** | | | **27.3/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
RMP24 (C18ORF21) is a specific component of the mitochondrial RNA processing (MRP) ribonucleoprotein endoribonuclease complex. Despite its name ("mitochondrial RNA processing"), the RNase MRP complex primarily functions in the nucleolus where it participates in pre-ribosomal RNA (pre-rRNA) processing. It cleaves the internal transcribed spacer 1 (ITS1) of the pre-rRNA transcript, a critical step in 5.8S rRNA maturation.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus (GO:0005634), Ribonuclease MRP complex (GO:0000172)
- **UniProt annotation**: "Nucleus" - sole subcellular location
- RMP24 is exclusively nuclear based on all available evidence
- The RNase MRP complex is localized to the nucleolus where it processes rRNA

### 3.3 Domain Architecture
RMP24 is a 220 aa protein. It is a structural subunit of the RNase MRP complex. The protein likely adopts a specific fold for integration into the RNP complex but lacks obviously characterized catalytic domains.

### 3.4 Protein-Protein Interactions
- **POP4 (RPP29)**: Subunit of both RNase MRP and RNase P complexes, involved in tRNA and rRNA processing
- **RPP25**: Component of RNase P and RNase MRP complexes
- **APP**: Amyloid precursor protein (interaction noted but physiological relevance unclear)
- The interactions with POP4 and RPP25 confirm integration into the nucleolar rRNA processing machinery

### 3.5 Relevance to TE Regulation
The RNase MRP complex is a ribonucleoprotein that processes structured RNA. This mechanism is relevant to TE regulation because:
- Many TEs form RNA secondary structures that could be substrates or inhibitors of RNase MRP
- rRNA processing defects can trigger nucleolar stress responses that affect global translation, potentially influencing TE expression
- RNP complexes in the nucleolus may interact with TE-derived transcripts

## 4. Overall Assessment

**Classification: nucleolus** - Purely nuclear protein with specific nucleolar localization as part of the RNase MRP complex.

**Strengths**:
- Exclusively nuclear localization
- Well-defined function in rRNA processing
- Strong PPI evidence linking it to the nucleolar processing machinery

**Weaknesses**:
- Very few publications (8 total)
- No HPA data
- No direct evidence of TE interaction
- Limited functional characterization beyond complex membership

**Recommendation: Shortlist for TE regulation evaluation.** As a nucleolar rRNA processing factor, RMP24 could influence TE expression through the nucleolar stress pathway or by processing TE-derived structured RNAs.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPP25 | STRING | 801 |
| POP4 | STRING | 798 |
| APP | BioGRID | 1 |
| BAX | BioGRID | 1 |
| HNRNPU | BioGRID | 1 |
| KIF22 | BioGRID | 1 |
| FBXO31 | BioGRID | 1 |
| KIF18A | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C18ORF21

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 41888142 | Structural and evolutionary insights into the eukaryotic RNase MRP ribonucleoprotein complex. |
| 41136609 | RNase MRP subunit composition and role in 40S ribosome biogenesis. |
| 40867056 | Composition and RNA binding specificity of metazoan RNase MRP. |
| 40205054 | Multimodal cell maps as a foundation for structural and functional genomics. |
| 40027791 | Composition and RNA binding specificity of metazoan RNase MRP. |


## 5. Data Sources

- UniProt: Q32NC0 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634), ribonuclease MRP complex (GO:0000172)
- BioGRID PPI: human PPI dataset (POP4, RPP25, APP interactions)
- HPA: unclassified_bare (no nuclear localization data)
