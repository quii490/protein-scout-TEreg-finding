---
type: protein-evaluation
gene: "SMPD4"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SMPD4 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SMPD4 / KIAA1418, SKNY |
| Protein Name | Sphingomyelin phosphodiesterase 4 |
| Protein Size | 866 aa, ~97.8 kDa |
| UniProt ID | Q9NXE4 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Endoplasmic reticulum membrane, Golgi apparatus membrane, Nucleus envelope; HPA: Nuclear membrane; (Reliability: Approved); GO-CC:  |
| Protein Size | 8/10 | x1 | **8** | 866 aa, ~97.8 kDa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict=24 (<=40 -> 8) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold v6 pLDDT=71.2; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR024129; Pfam: PF14724 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **124.5/180** | |
| **Normalized Total** | | | **69.2/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Endoplasmic reticulum membrane | Experimental |
| UniProt | Golgi apparatus membrane | Experimental |
| UniProt | Nucleus envelope | Experimental |
| UniProt | Cell membrane, sarcolemma | By similarity |
| GO-CC | nuclear envelope | ISS:UniProtKB |
| GO-CC | nuclear outer membrane | IDA:UniProtKB |
| HPA | Nuclear membrane; Additional: Cytosol | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Endoplasmic reticulum membrane, Golgi apparatus membrane, Nucleus envelope; HPA: Nuclear membrane; (Reliability: Approved); GO-CC: nuclear envelope, nuclear outer membrane. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SMPD4 is 866 amino acids in length (~97.8 kDa). Acceptable size (866 aa), suitable for routine experiments. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 24 |
| PubMed broad count | 39 |
| Alias context | Aliases observed but not used for scoring: KIAA1418, SKNY |
| Novelty category | <=40 -> 8 |

**Key Research Context**: Catalyzes the hydrolysis of membrane sphingomyelin to form phosphorylcholine and ceramide (PubMed:16517606, PubMed:25180167). It has a relevant role in the homeostasis of membrane sphingolipids, thereby influencing membrane integrity, and endoplasmic reticulum organization and function (PubMed:31495. Published literature indicates growing research activity. Very novel, only a few foundational studies.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 33060286 | Neurogenetic fetal akinesia and arthrogryposis: genetics, expanding genotype-phenotypes and functional genomics. | Journal of medical genetics |
| 38168190 | SMPD4 mediated sphingolipid metabolism regulates brain and primary cilia development. | bioRxiv : the preprint server for biology |
| 39470011 | SMPD4-mediated sphingolipid metabolism regulates brain and primary cilia development. | Development (Cambridge, England) |
| 40211349 | High expression of SMPD4 promotes liver cancer and is associated with poor prognosis. | BMC research notes |
| 34621002 | Growth and neurodevelopmental disorder with arthrogryposis, microcephaly and structural brain anomalies caused by Bi-all | Journal of human genetics |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 71.2 |
| High confidence residues (pLDDT > 90) | 28.4% |
| Confident residues (pLDDT 70-90) | 33.1% |
| Medium confidence (pLDDT 50-70) | 13.7% |
| Low confidence (pLDDT < 50) | 24.7% |
| Ordered region (pLDDT > 70) | 61.5% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high quality prediction (pLDDT=71.2), 61.5% ordered. Structure reliable. Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR024129 |  |
| Pfam | PF14724 |  |

**Domain Analysis**:  The protein contains 1 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SMPD3 | 0.996 | 0.000 | 0.9 | 0.969 |
| SMPD2 | 0.994 | 0.000 | 0.9 | 0.947 |
| SMPD1 | 0.969 | 0.000 | 0.9 | 0.707 |
| SGMS1 | 0.968 | 0.000 | 0.9 | 0.649 |
| SGMS2 | 0.959 | 0.000 | 0.9 | 0.551 |
| ENPP7 | 0.959 | 0.000 | 0.9 | 0.609 |
| DEGS1 | 0.952 | 0.000 | 0.9 | 0.537 |
| CERS6 | 0.952 | 0.000 | 0.9 | 0.542 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| EXOSC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.101 |
| ISG15 | psi-mi:"MI:0096"(pull down) | pubmed:26259872|imex:IM-26283 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| CLN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Well-folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0
- Multi-DB localization consensus (3 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0.5
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 69.2/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (866 aa) for experimental characterization
3. High novelty (PubMed count ~24)
4. AlphaFold prediction available (pLDDT 71.2)
5. Some domain annotations present (3 domains)
6. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 69.2/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXE4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXE4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMPD4
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000136699-SMPD4/subcellular
- Data harvested: 2026-06-04 03:22:07
