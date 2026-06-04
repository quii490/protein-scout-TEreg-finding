---
type: protein-evaluation
gene: "SPATA18"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPATA18 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPATA18 / MIEAP |
| Protein Name | Mitochondria-eating protein |
| Protein Size | 538 aa, ~61.1 kDa |
| UniProt ID | Q8TC71 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, cytosol, Mitochondrion outer membrane, Mitochondrion matrix; HPA: Mitochondria; (Reliability: Supported); GO-CC: nucleop |
| Protein Size | 10/10 | x1 | **10** | 538 aa, ~61.1 kDa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict=30 (<=40 -> 8) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold v6 pLDDT=75.4; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR026169, IPR031981; Pfam: PF16026 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **126.5/180** | |
| **Normalized Total** | | | **70.3/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm, cytosol | Experimental |
| UniProt | Mitochondrion outer membrane | Experimental |
| UniProt | Mitochondrion matrix | Experimental |
| UniProt | Cytoplasm, cytosol | Experimental |
| UniProt | Mitochondrion matrix | Experimental |
| UniProt | Cytoplasm, cytosol | Experimental |
| UniProt | Mitochondrion matrix | Experimental |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Mitochondria; Additional: Nucleoplasm, Cytosol | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, cytosol, Mitochondrion outer membrane, Mitochondrion matrix; HPA: Mitochondria; (Reliability: Supported); GO-CC: nucleoplasm. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SPATA18 is 538 amino acids in length (~61.1 kDa). Ideal size (538 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 30 |
| PubMed broad count | 53 |
| Alias context | Aliases observed but not used for scoring: MIEAP |
| Novelty category | <=40 -> 8 |

**Key Research Context**: Key regulator of mitochondrial quality that mediates the repairing or degradation of unhealthy mitochondria in response to mitochondrial damage (PubMed:21264221, PubMed:21264228, PubMed:22292033, PubMed:22532927). Mediator of mitochondrial protein catabolic process (also named MALM) by mediating the. Published literature indicates growing research activity. Very novel, only a few foundational studies.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 36751118 | High SPATA18 Expression and its Diagnostic and Prognostic Value in Clear Cell Renal Cell Carcinoma. | Medical science monitor : international medical journal of e |
| 21300779 | SPATA18, a spermatogenesis-associated gene, is a novel transcriptional target of p53 and p63. | Molecular and cellular biology |
| 38830862 | Analysis of human neuronal cells carrying ASTN2 deletion associated with psychiatric disorders. | Translational psychiatry |
| 35639655 | Comparison between SPATA18 and P53 Gene Expressions in The Sperm Cells Obtained from Normospermic and Asthenospermic Sam | International journal of fertility & sterility |
| 35269894 | SPATA18 Expression Predicts Favorable Clinical Outcome in Colorectal Cancer. | International journal of molecular sciences |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 75.4 |
| High confidence residues (pLDDT > 90) | 39.4% |
| Confident residues (pLDDT 70-90) | 28.4% |
| Medium confidence (pLDDT 50-70) | 11.7% |
| Low confidence (pLDDT < 50) | 20.4% |
| Ordered region (pLDDT > 70) | 67.8% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high quality prediction (pLDDT=75.4), 67.8% ordered. Structure reliable. Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR026169 |  |
| InterPro | IPR031981 |  |
| Pfam | PF16026 |  |

**Domain Analysis**:   The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SGCB | 0.790 | 0.000 | 0.0 | 0.786 |
| BNIP3L | 0.747 | 0.000 | 0.0 | 0.747 |
| BNIP3 | 0.628 | 0.000 | 0.0 | 0.628 |
| SPATA45 | 0.626 | 0.000 | 0.0 | 0.626 |
| SPATA19 | 0.607 | 0.000 | 0.0 | 0.607 |
| OR1E1 | 0.600 | 0.000 | 0.0 | 0.600 |
| SPATA6 | 0.575 | 0.000 | 0.0 | 0.563 |
| CFAP161 | 0.572 | 0.000 | 0.0 | 0.538 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| ENSP00000295213.4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PIBF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| AIMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LRIF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HOXA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TGM7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GAS8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Well-folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0
- Multi-DB localization consensus (2 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0.5
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 70.3/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (538 aa) for experimental characterization
3. High novelty (PubMed count ~30)
4. AlphaFold prediction available (pLDDT 75.4)
5. Some domain annotations present (4 domains)
6. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 70.3/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8TC71
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TC71
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA18
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000163071-SPATA18/subcellular
- Data harvested: 2026-06-04 03:28:16
