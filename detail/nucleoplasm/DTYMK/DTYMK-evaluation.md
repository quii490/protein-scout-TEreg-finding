---
type: gene-evaluation
gene: DTYMK
date: 2026-06-28
tags: [nucleoplasm, nucleotide-metabolism, TMP-kinase, DNA-synthesis, transcription]
status: shortlisted
---

# DTYMK - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DTYMK |
| **UniProt Accession** | P23919 |
| **Protein Name** | Thymidylate kinase |
| **Protein Length** | 212 aa |
| **Molecular Function** | dTMP kinase (ATP:dTMP phosphotransferase) |
| **Chromosome** | 2q37.3 |
| **PubMed Hits** | 57 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | Nuclear localization annotated |
| **Nucleotide Metabolism** | ×3 | ×5 | 15 | DNA precursor synthesis in nucleus |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×4 | ×2 | 8 | CDK9 (nuclear kinase), MEPCE (7SK snRNP) |
| **Literature Evidence** | ×3 | ×3 | 9 | 57 publications |
| **Total** | | | **51** | |



| **加权总分** | | | **51.0/180** | |
| **归一化总分 (÷1.83)** | | | **27.9/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DTYMK (thymidylate kinase) catalyzes the phosphorylation of thymidine monophosphate (dTMP) to thymidine diphosphate (dTDP), the immediate precursor for the DNA building block dTTP. This reaction uses ATP as the preferred phosphoryl donor in the presence of Mg2+. DTYMK is a critical enzyme in the nucleotide salvage pathway for DNA synthesis.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus (GO:0005634), Cytoplasm (GO:0005737), Cytosol (GO:0005829), Mitochondrion (GO:0005739)
- **UniProt annotation**: No specific subcellular location annotated by UniProt
- DTYMK is found in the nucleus where it provides dTDP for DNA synthesis
- Nuclear localization is consistent with its role in providing nucleotide precursors for DNA replication and repair
- Association with CDK9 and MEPCE (7SK snRNP component) supports nuclear localization

### 3.3 Domain Architecture
DTYMK is a 212 aa protein with:
- **Thymidylate kinase domain**: Catalyzes phosphoryl transfer from ATP to dTMP
- **P-loop (Walker A motif)**: Nucleotide-binding (ATP)
- **DRX motif**: dTMP binding and specificity
- The enzyme belongs to the nucleoside monophosphate kinase family

### 3.4 Protein-Protein Interactions
- **CDK9 (Cyclin-dependent kinase 9)**: Nuclear kinase, component of P-TEFb involved in transcription elongation by RNA polymerase II. The CDK9-DTYMK interaction was identified in a high-throughput study (Jeronimo C, 2007) and suggests DTYMK may localize near transcription complexes.
- **MEPCE (Methylphosphate capping enzyme)**: Component of the 7SK snRNP complex involved in transcription regulation. Nuclear protein.
- **HSD17B7**: 17-beta-hydroxysteroid dehydrogenase (likely non-nuclear interaction)

### 3.5 Relevance to TE Regulation
DTYMK connects to TE regulation through nucleotide metabolism and transcription:
- dNTP pool balance affects genome stability - imbalanced dNTPs increase mutation rates
- dTTP supply affects retrotransposon reverse transcription efficiency
- The CDK9 interaction links DTYMK to RNA polymerase II transcription elongation, which reads through TE sequences
- MEPCE (7SK snRNP) interaction connects to transcription elongation control, relevant for TE transcript processing
- Nucleotide metabolism enzymes near transcription sites may locally supply dNTPs for DNA repair at TE-induced lesions

## 4. Overall Assessment

**Classification: nucleoplasm** - Nuclear localization with functionally relevant nuclear interaction partners (CDK9, MEPCE) in transcription elongation complexes.

**Strengths**:
- Nuclear GO-CC annotation
- Critical enzyme for DNA synthesis
- Nuclear PPI partners in transcription elongation
- 57 publications

**Weaknesses**:
- Multi-compartment localization (cytoplasm, mitochondrion, nucleus)
- Primary function is metabolic, not regulatory
- No direct evidence of chromatin/DNA binding
- No HPA data
- Connection to TE regulation is indirect (dNTP pools, transcription proximity)

**Recommendation: Shortlist at lower priority.** DTYMK's nuclear localization and transcription-associated PPI network provide a plausible connection to TE regulation through nucleotide supply for DNA repair and transcription elongation. However, the connection is indirect compared to dedicated nuclear regulatory proteins.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RRM1 | STRING | 975 |
| NME2 | STRING | 958 |
| RRM2 | STRING | 953 |
| CMPK1 | STRING | 946 |
| NT5C | STRING | 944 |
| NME7 | STRING | 944 |
| RRM2B | STRING | 941 |
| POMP | STRING | 926 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168393-DTYMK

![](https://images.proteinatlas.org/42719/487_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/487_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/481_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/481_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/491_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/491_C9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168393-DTYMK

![](https://images.proteinatlas.org/42719/487_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/487_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/481_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/481_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/491_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/491_C9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168393-DTYMK

![](https://images.proteinatlas.org/42719/487_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/487_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/481_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/481_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/491_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42719/491_C9_2_blue_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DTYMK

## 5. Data Sources

- UniProt: P23919 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634), cytoplasm (GO:0005737), cytosol (GO:0005829), mitochondrion (GO:0005739)
- BioGRID PPI: human PPI dataset (CDK9, MEPCE, HSD17B7 interactions)
- PubMed: 57 total hits
- HPA: unclassified_bare (no nuclear localization data)
