---
type: protein-evaluation
gene: "SPAG8"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPAG8 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPAG8 |
| Protein Name | Sperm-associated antigen 8 |
| Protein Size | 485 aa, ~51.1 kDa |
| UniProt ID | Q99932 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Nucleus, Cytoplasmic vesicle, secretory vesicle, acrosome; HPA: Primary cilium, Acrosome, Equatorial segment; (Reliabili |
| Protein Size | 10/10 | x1 | **10** | 485 aa, ~51.1 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=9 (<=20 -> 10) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=56.7; PDB: 7UNG, 8J07 |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR026124; Pfam: PF22584 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **133.5/180** | |
| **Normalized Total** | | | **74.2/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | By similarity |
| UniProt | Nucleus | By similarity |
| UniProt | Cytoplasmic vesicle, secretory vesicle, acrosome | Experimental |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center | Experimental |
| UniProt | Cytoplasm, cytoskeleton, spindle | Experimental |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme | Experimental |
| UniProt | Cytoplasm, cytoskeleton, flagellum axoneme | By similarity |
| GO-CC | male germ cell nucleus | IEA:Ensembl |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IBA:GO_Central |
| HPA | Primary cilium, Acrosome, Equatorial segment, End piece; Additional: Nucleoplasm, Cytosol, Principal piece | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, Nucleus, Cytoplasmic vesicle, secretory vesicle, acrosome; HPA: Primary cilium, Acrosome, Equatorial segment; (Reliability: Supported); GO-CC: male germ cell nucleus, nucleoplasm, nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SPAG8 is 485 amino acids in length (~51.1 kDa). Ideal size (485 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 9 |
| PubMed broad count | 26 |
| Alias context | None |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating (PubMed:36191189). Plays a role in spermatogenesis by enhancing the binding of CREM isoform tau to its coactivator FHL5 and increasing the FHL5-regula. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 33333720 | Association of TMEM8B and SPAG8 with Mature Weight in Sheep. | Animals : an open access journal from MDPI |
| 20488182 | Sperm associated antigen 8 (SPAG8), a novel regulator of activator of CREM in testis during spermatogenesis. | FEBS letters |
| 38847481 | Male infertility and perfluoroalkyl and poly-fluoroalkyl substances: evidence for alterations in phosphorylation of prot | Biology of reproduction |
| 30883840 | Detecting selection signatures in three Iranian sheep breeds. | Animal genetics |
| 19452925 | Expression signatures for a model androgen and antiandrogen in the fathead minnow (Pimephales promelas) ovary. | Environmental science & technology |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 2 experimental |
| Mean pLDDT | 56.7 |
| High confidence residues (pLDDT > 90) | 4.3% |
| Confident residues (pLDDT 70-90) | 27.0% |
| Medium confidence (pLDDT 50-70) | 15.7% |
| Low confidence (pLDDT < 50) | 53.0% |
| Ordered region (pLDDT > 70) | 31.3% |
| Available PDB entries | 7UNG, 8J07 |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=56.7), 31.3% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR026124 |  |
| Pfam | PF22584 |  |

**Domain Analysis**:  The protein contains 1 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| TEKT3 | 0.913 | 0.902 | 0.0 | 0.000 |
| CFAP126 | 0.908 | 0.817 | 0.0 | 0.473 |
| CFAP53 | 0.859 | 0.821 | 0.0 | 0.000 |
| CFAP52 | 0.845 | 0.822 | 0.0 | 0.000 |
| PACRG | 0.842 | 0.821 | 0.0 | 0.136 |
| EFHC2 | 0.838 | 0.817 | 0.0 | 0.000 |
| TEKT2 | 0.838 | 0.817 | 0.0 | 0.000 |
| EFHC1 | 0.835 | 0.817 | 0.0 | 0.000 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827|mint:MINT- |
| ENSP00000340982.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRR35 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| USP2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP21-2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP11-1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PEF1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP7-1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus (2 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 74.2/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (485 aa) for experimental characterization
3. High novelty (PubMed count ~9)
4. AlphaFold prediction available (pLDDT 56.7)
5. Some domain annotations present (3 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 7UNG, 8J07

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 74.2/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q99932
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99932
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPAG8
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000137098-SPAG8/subcellular
- Data harvested: 2026-06-04 03:25:51
