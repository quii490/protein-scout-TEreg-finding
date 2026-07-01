---
type: gene-evaluation
gene: DICER1
date: 2026-06-28
tags: [nucleoplasm, RNAi, miRNA, siRNA, ribonuclease, RNA-processing, genome-defense]
status: shortlisted
---

# DICER1 - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DICER1 |
| **UniProt Accession** | Q9UPY3 |
| **Protein Name** | Endoribonuclease Dicer |
| **Protein Length** | 1922 aa |
| **Molecular Function** | dsRNA endoribonuclease, miRNA/siRNA processing |
| **Chromosome** | 14q32.13 |
| **PubMed Hits** | 2453 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | Well-annotated nuclear localization |
| **Nuclear RNAi Function** | ×4 | ×5 | 20 | Nuclear miRNA processing and RNAi |
| **GO-CC: RISC Complex** | ×3 | ×1 | 3 | Cytoplasmic but functionally linked to nuclear RNAi |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×4 | ×2 | 8 | AGO1-4 in RISC loading complex |
| **Literature Evidence** | ×4 | ×3 | 12 | Extensively studied (2453 publications) |
| **Total** | | | **62** | |



| **加权总分** | | | **62.0/180** | |
| **归一化总分 (÷1.83)** | | | **33.9/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DICER1 is a double-stranded RNA (dsRNA) endoribonuclease that plays a central role in short dsRNA-mediated post-transcriptional gene silencing. It cleaves naturally occurring long dsRNAs and short hairpin pre-microRNAs (miRNA) into fragments of 21-23 nucleotides with 3' overhangs of two nucleotides, producing small interfering RNAs (siRNA) and mature microRNAs. These serve as guides to direct the RNA-induced silencing complex (RISC) to complementary RNAs for degradation or translational repression.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus (GO:0005634), Cytoplasm (GO:0005737), Cytosol (GO:0005829), RISC complex (GO:0016442), RISC-loading complex (GO:0070578), Perinuclear region (GO:0048471)
- **UniProt annotation**: "Cytoplasm; Cytoplasm, perinuclear region"
- While DICER1 is canonically cytoplasmic, substantial evidence supports nuclear localization and function:
  - Nuclear DICER1 processes miRNA precursors in the nucleus
  - DICER1 contains a bipartite nuclear localization signal
  - Nuclear DICER1 is involved in transcriptional gene silencing through RNA-directed DNA methylation-like pathways
  - DICER1 associates with chromatin at specific genomic loci

### 3.3 Domain Architecture
DICER1 is a large 1922 aa protein with the following domain organization:
- **DExH-box helicase domain** (N-terminal): ATP-dependent RNA unwinding
- **DUF283 domain**: dsRNA-binding fold
- **PAZ domain**: Binds the 3' overhang of dsRNA substrates
- **Two RNase III domains** (RNase IIIa and RNase IIIb): Form an intramolecular dimer for dsRNA cleavage
- **dsRNA-binding domain (dsRBD)** (C-terminal): Substrate recognition

This domain architecture makes DICER1 a molecular ruler that measures approximately 22 nt from the 3' end of dsRNA substrates.

### 3.4 Protein-Protein Interactions
Extensive PPI network including:
- **AGO1, AGO2, AGO3, AGO4**: Argonaute proteins, core components of RISC - DICER1 loads processed small RNAs onto AGO
- **TRBP (TARBP2)**: dsRNA-binding protein that bridges DICER1 to AGO proteins
- **PACT (PRKRA)**: Activator of DICER1 in response to cellular stress
- **LIN28**: Inhibitor of let-7 miRNA processing by DICER1

### 3.5 Relevance to TE Regulation
DICER1 is arguably the most important protein for TE regulation in this set:
- **Primary TE defense**: Processes TE-derived dsRNAs into siRNAs that target TE transcripts for degradation
- **piRNA pathway interface**: In some contexts, DICER1-processed siRNAs complement piRNA-mediated TE silencing
- **Nuclear TE silencing**: Nuclear DICER1 contributes to transcriptional silencing of TE loci through heterochromatin formation
- **LTR retrotransposon defense**: DICER1 processes dsRNA from bidirectional LTR transcription
- **DNA damage response**: DICER1 produces damage-induced small RNAs at DNA break sites, including TE-induced breaks
- **Germline genome defense**: DICER1 is essential in oocytes for TE suppression

Key references:
- Fukagawa et al. (2004) - DICER1 is essential for heterochromatin formation
- Kanellopoulou et al. (2005) - DICER1-deficient cells show TE upregulation
- White et al. (2014) - Nuclear DICER1 in transcriptional gene silencing

## 4. Overall Assessment

**Classification: nucleoplasm** - Despite predominantly cytoplasmic canonical function, DICER1 has well-documented nuclear roles including nuclear miRNA processing, transcriptional gene silencing, and chromatin-associated RNAi. The presence of a functional NLS, association with chromatin, and role in nuclear TE silencing warrant nucleoplasm classification.

**Strengths**:
- Central player in RNA interference
- Direct TE regulation via siRNA/miRNA pathways
- Nuclear localization with functional evidence
- Extensive literature (2453 publications)
- Well-characterized domain architecture
- Direct link to heterochromatin and TE silencing

**Weaknesses**:
- Canonically considered cytoplasmic (nuclear role often overlooked)
- HPA does not show nuclear staining (unclassified_bare)
- Large protein makes structural studies challenging
- Nuclear function is context-dependent

**Recommendation: HIGH PRIORITY for TE regulation evaluation.** DICER1 is the cornerstone of RNA-based TE defense. Its nuclear functions in transcriptional gene silencing directly connect to TE regulation. This should be among the highest-priority genes evaluated.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AGO2 | STRING | 999 |
| TARBP2 | STRING | 999 |
| PRKRA | STRING | 999 |
| RAX | STRING | 999 |
| PACT | STRING | 999 |
| AGO1 | STRING | 999 |
| TNRC6A | STRING | 998 |
| XPO5 | STRING | 995 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100697-DICER1

![](https://images.proteinatlas.org/68185/1538_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1538_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1539_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1539_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1540_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1540_E1_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100697-DICER1

![](https://images.proteinatlas.org/68185/1538_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1538_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1539_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1539_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1540_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1540_E1_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100697-DICER1

![](https://images.proteinatlas.org/68185/1538_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1538_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1539_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1539_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1540_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68185/1540_E1_3_blue_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DICER1

## 5. Data Sources

- UniProt: Q9UPY3 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634), cytoplasm (GO:0005737), RISC complex (GO:0016442)
- BioGRID PPI: human PPI dataset (extensive: AGO1-4, TARBP2, PRKRA, LIN28A, etc.)
- PubMed: 2453 total hits
- Key reviews: RNAi pathway, miRNA processing, nuclear RNAi
- HPA: unclassified_bare (no nuclear localization data)

## 6. Key References

1. Fukagawa T, et al. (2004) - Dicer is essential for formation of the heterochromatin structure in vertebrate cells. Nat Cell Biol.
2. Kanellopoulou C, et al. (2005) - Dicer-deficient mouse embryonic stem cells are defective in differentiation and centromeric silencing. Genes Dev.
3. White E, et al. (2014) - Human nuclear Dicer restricts the deleterious accumulation of endogenous double-stranded RNA. Nat Struct Mol Biol.
4. Burger K & Gullerova M (2015) - Swiss army knives: non-canonical functions of nuclear Drosha and Dicer. Nat Rev Mol Cell Biol.
