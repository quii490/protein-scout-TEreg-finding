---
type: protein-evaluation
gene: "SOCS5"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: rejected
---

## SOCS5 -- REJECTED (PubMed strict count 114 > 100 (over-studied))

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SOCS5 / CIS6, CISH5, CISH6, KIAA0671 |
| Protein Name | Suppressor of cytokine signaling 5 |
| Protein Size | 536 aa, ~61.2 kDa |
| UniProt ID | O75159 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | UniProt: no subcellular annotation; HPA: Cytosol; (Reliability: Approved) |
| Protein Size | 10/10 | x1 | **10** | 536 aa, ~61.2 kDa |
| Research Novelty | 0/10 | x5 | **0** | PubMed strict=114 (>100 -> REJECTED) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=61.8; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR000980, IPR036860, IPR022252, IPR037343, IPR001496; Pfam: PF00017, PF12610, PF07525 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 11 interactions |
| Cross-Validation Bonus | -- | -- | **+0.5** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **70.5/180** | |
| **Normalized Total** | | | **39.2/100** | |

### 3. Rejection Check

**REJECTED** for: PubMed strict count 114 > 100 (over-studied)

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Cytosol; Additional: Nucleoplasm, Plasma membrane | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: no subcellular annotation; HPA: Cytosol; (Reliability: Approved). Score 4/10 reflects Weak nuclear signal with multiple sources showing mixed or non-nuclear preference.

### 4. Protein Size Assessment

SOCS5 is 536 amino acids in length (~61.2 kDa). Ideal size (536 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 114 |
| PubMed broad count | 219 |
| Alias context | Aliases observed but not used for scoring: CIS6, CISH5, CISH6, KIAA0671 |
| Novelty category | >100 -> REJECTED |

**Key Research Context**: SOCS family proteins form part of a classical negative feedback system that regulates cytokine signal transduction. May be a substrate-recognition component of a SCF-like ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent pro. Published literature indicates a mature research field. Over-studied (>100 articles), fails novelty threshold.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 33724154 | Pathogenicity and virulence of Japanese encephalitis virus: Neuroinflammation and neuronal cell damage. | Virulence |
| 33391546 | H3K27 acetylation activated-COL6A1 promotes osteosarcoma lung metastasis by repressing STAT1 and activating pulmonary ca | Theranostics |
| 22081311 | SOCS5 and SOCS6 have similar expression patterns in normal and cancer tissues. | Tumour biology : the journal of the International Society fo |
| 36319626 | SOCS5 knockdown suppresses metastasis of hepatocellular carcinoma by ameliorating HIF-1α-dependent mitochondrial damage. | Cell death & disease |
| 31406106 | SOCS5 inhibition induces autophagy to impair metastasis in hepatocellular carcinoma cells via the PI3K/Akt/mTOR pathway. | Cell death & disease |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 61.8 |
| High confidence residues (pLDDT > 90) | 26.3% |
| Confident residues (pLDDT 70-90) | 14.0% |
| Medium confidence (pLDDT 50-70) | 11.4% |
| Low confidence (pLDDT < 50) | 48.3% |
| Ordered region (pLDDT > 70) | 40.3% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=61.8), 40.3% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR000980 |  |
| InterPro | IPR036860 |  |
| InterPro | IPR022252 |  |
| InterPro | IPR037343 |  |
| InterPro | IPR001496 |  |
| InterPro | IPR036036 |  |
| Pfam | PF00017 |  |
| Pfam | PF12610 |  |
| Pfam | PF07525 |  |

**Domain Analysis**:    The protein contains 6 InterPro and 3 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 11 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| IL4R | 0.970 | 0.328 | 0.5 | 0.914 |
| JAK2 | 0.952 | 0.191 | 0.9 | 0.449 |
| JAK1 | 0.920 | 0.191 | 0.7 | 0.738 |
| STAT1 | 0.919 | 0.359 | 0.7 | 0.665 |
| CUL5 | 0.911 | 0.613 | 0.5 | 0.546 |
| SOCS6 | 0.872 | 0.000 | 0.5 | 0.708 |
| SOCS3 | 0.844 | 0.000 | 0.5 | 0.674 |
| ELOC | 0.840 | 0.435 | 0.5 | 0.471 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14968112 |
| TMBIM1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CASP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.101 |
| MIMAT0000441 | psi-mi:"MI:2285"(miRNA interference luciferase reporter assay) | imex:IM-26514|pubmed:22773185 |
| CUL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| KIT | psi-mi:"MI:0053"(fluorescence polarization spectroscopy) | pubmed:24728074|imex:IM-22269 |
| MET | psi-mi:"MI:0053"(fluorescence polarization spectroscopy) | pubmed:24728074|imex:IM-22269 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Non-nuclear/Weak | Inconsistent/Weak |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0
- Multi-DB localization consensus: +0
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +0.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED) (Score: 39.2/100)

**Core Strengths**:
1. Ideal protein size (536 aa) for experimental characterization
2. AlphaFold prediction available (pLDDT 61.8)
3. Well-annotated domain architecture (9 domains)
4. Moderate PPI data available

**Risks / Uncertainties**:
1. Moderate/weak nuclear localization evidence
2. PubMed count > 100, automatic rejection criterion
3. No experimental PDB structures

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context
**PubMed count 114 > 100: REJECTED per novelty threshold.**

### 11. Decision

**FINAL DECISION**: REJECTED. Rejected for: PubMed strict count 114 > 100 (over-studied).

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75159
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75159
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOCS5
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000171150-SOCS5/subcellular
- Data harvested: 2026-06-04 03:24:38
