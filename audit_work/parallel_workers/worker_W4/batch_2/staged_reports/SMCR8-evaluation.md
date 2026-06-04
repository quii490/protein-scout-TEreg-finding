---
type: protein-evaluation
gene: "SMCR8"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SMCR8 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SMCR8 |
| Protein Name | Guanine nucleotide exchange protein SMCR8 |
| Protein Size | 937 aa, ~105.0 kDa |
| UniProt ID | Q8TEV9 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Nucleus, Presynapse; HPA: Nucleoplasm; (Reliability: Enhanced); GO-CC: chromatin, nucleoplasm |
| Protein Size | 8/10 | x1 | **8** | 937 aa, ~105.0 kDa |
| Research Novelty | 6/10 | x5 | **30** | PubMed strict=45 (<=60 -> 6) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=62.2; PDB: 6LT0, 6V4U, 7EL6, 7MGE, 7O2W |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR037521, IPR037520; Pfam: PF11704 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.5** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **112.5/180** | |
| **Normalized Total** | | | **62.5/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | Experimental |
| UniProt | Nucleus | Experimental |
| UniProt | Presynapse | By similarity |
| UniProt | Postsynapse | By similarity |
| GO-CC | chromatin | IDA:HGNC |
| GO-CC | nucleoplasm | IDA:HGNC |
| HPA | Nucleoplasm | Reliability: Enhanced |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Enhanced), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, Nucleus, Presynapse; HPA: Nucleoplasm; (Reliability: Enhanced); GO-CC: chromatin, nucleoplasm. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SMCR8 is 937 amino acids in length (~105.0 kDa). Acceptable size (937 aa), suitable for routine experiments. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 45 |
| PubMed broad count | 52 |
| Alias context | None |
| Novelty category | <=60 -> 6 |

**Key Research Context**: Component of the C9orf72-SMCR8 complex, a complex that has guanine nucleotide exchange factor (GEF) activity and regulates autophagy (PubMed:20562859, PubMed:27103069, PubMed:27193190, PubMed:27559131, PubMed:27617292, PubMed:28195531, PubMed:32303654). In the complex, C9orf72 and SMCR8 probably con. Published literature indicates an established research field. Moderately novel with unexplored niches.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 36692217 | Stress granule homeostasis is modulated by TRIM21-mediated ubiquitination of G3BP1 and autophagy-dependent elimination o | Autophagy |
| 37317656 | C9orf72 protein quality control by UBR5-mediated heterotypic ubiquitin chains. | EMBO reports |
| 38064514 | ALS-linked C9orf72-SMCR8 complex is a negative regulator of primary ciliogenesis. | Proceedings of the National Academy of Sciences of the Unite |
| 38293807 | The C9orf72-SMCR8 complex suppresses primary ciliogenesis as a RAB8A GAP. | Autophagy |
| 32678027 | C9orf72-associated SMCR8 protein binds in the ubiquitin pathway and with proteins linked with neurological disease. | Acta neuropathologica communications |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 5 experimental |
| Mean pLDDT | 62.2 |
| High confidence residues (pLDDT > 90) | 23.2% |
| Confident residues (pLDDT 70-90) | 25.2% |
| Medium confidence (pLDDT 50-70) | 8.1% |
| Low confidence (pLDDT < 50) | 43.5% |
| Ordered region (pLDDT > 70) | 48.4% |
| Available PDB entries | 6LT0, 6V4U, 7EL6, 7MGE, 7O2W |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=62.2), 48.4% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR037521 |  |
| InterPro | IPR037520 |  |
| Pfam | PF11704 |  |

**Domain Analysis**:   The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| C9orf72 | 0.999 | 0.982 | 0.8 | 0.995 |
| WDR41 | 0.999 | 0.926 | 0.8 | 0.998 |
| RAB39B | 0.979 | 0.301 | 0.9 | 0.729 |
| RAB8A | 0.972 | 0.301 | 0.9 | 0.632 |
| ULK1 | 0.965 | 0.474 | 0.9 | 0.398 |
| TBK1 | 0.959 | 0.292 | 0.9 | 0.462 |
| TANK | 0.925 | 0.000 | 0.9 | 0.286 |
| ARF1 | 0.924 | 0.900 | 0.0 | 0.271 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| RB1CC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| COX14 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| TOMM22 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus (3 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage (>=3): +1.0
- **Total Cross-Validation Bonus**: +2.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 62.5/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (937 aa) for experimental characterization
3. Moderate novelty (PubMed count ~45)
4. AlphaFold prediction available (pLDDT 62.2)
5. Some domain annotations present (4 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 6LT0, 6V4U, 7EL6

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 62.5/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8TEV9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TEV9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMCR8
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000176994-SMCR8/subcellular
- Data harvested: 2026-06-04 03:21:42
