---
type: protein-evaluation
gene: "SLX1B"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SLX1B -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SLX1B / GIYD1, SLX1 |
| Protein Name | Structure-specific endonuclease subunit SLX1 |
| Protein Size | 275 aa, ~30.8 kDa |
| UniProt ID | Q9BQ83 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Nucleus; HPA: Nucleoplasm; (Reliability: Supported); GO-CC: nucleoplasm |
| Protein Size | 10/10 | x1 | **10** | 275 aa, ~30.8 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=3 (<=20 -> 10) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold v6 pLDDT=83.3; PDB: None |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: IPR000305, IPR035901, IPR027520, IPR048749, IPR050381; Pfam: PF01541, PF21202 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 11 interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **146.5/180** | |
| **Normalized Total** | | | **81.4/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nucleus; HPA: Nucleoplasm; (Reliability: Supported); GO-CC: nucleoplasm. Score 9/10 reflects Multiple independent data sources confirm nuclear localization with high HPA reliability.

### 4. Protein Size Assessment

SLX1B is 275 amino acids in length (~30.8 kDa). Ideal size (275 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| Alias context | Aliases observed but not used for scoring: GIYD1, SLX1 |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Catalytic subunit of the SLX1-SLX4 structure-specific endonuclease that resolves DNA secondary structures generated during DNA repair and recombination. Has endonuclease activity towards branched DNA substrates, introducing single-strand cuts in duplex DNA close to junctions with ss-DNA. Has a prefe. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 37968726 | Dissecting the autism-associated 16p11.2 locus identifies multiple drivers in neuroanatomical phenotypes and unveils a m | Genome biology |
| 33531372 | Premalignant Oligodendrocyte Precursor Cells Stall in a Heterogeneous State of Replication Stress Prior to Gliomagenesis | Cancer research |
| 34715901 | Integration of genetic, transcriptomic, and clinical data provides insight into 16p11.2 and 22q11.2 CNV genes. | Genome medicine |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 83.3 |
| High confidence residues (pLDDT > 90) | 70.2% |
| Confident residues (pLDDT 70-90) | 8.0% |
| Medium confidence (pLDDT 50-70) | 6.2% |
| Low confidence (pLDDT < 50) | 15.6% |
| Ordered region (pLDDT > 70) | 78.2% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high quality prediction (pLDDT=83.3), 78.2% ordered. Structure reliable. Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR000305 |  |
| InterPro | IPR035901 |  |
| InterPro | IPR027520 |  |
| InterPro | IPR048749 |  |
| InterPro | IPR050381 |  |
| InterPro | IPR013083 |  |
| Pfam | PF01541 |  |
| Pfam | PF21202 |  |

**Domain Analysis**:    The protein contains 6 InterPro and 2 Pfam domain annotations. Score 8/10 reflects strong domain architecture. Multiple annotated domains with high AlphaFold quality; domain folds credible.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 11 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SLX4 | 0.981 | 0.640 | 0.9 | 0.480 |
| SLX1A | 0.935 | 0.200 | 0.9 | 0.000 |
| ARPC4 | 0.865 | 0.834 | 0.0 | 0.212 |
| ERCC1 | 0.710 | 0.436 | 0.0 | 0.470 |
| MUS81 | 0.692 | 0.319 | 0.0 | 0.521 |
| RECQL4 | 0.669 | 0.479 | 0.0 | 0.392 |
| BLM | 0.645 | 0.479 | 0.0 | 0.347 |
| BOLA2 | 0.637 | 0.000 | 0.0 | 0.590 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| TUBA1B | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| DUSP10 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GRB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| THAP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLX1A | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| pog | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ERCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |

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

**Recommendation Level**: Recommended (Score: 81.4/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (275 aa) for experimental characterization
3. High novelty (PubMed count ~3)
4. AlphaFold prediction available (pLDDT 83.3)
5. Well-annotated domain architecture (8 domains)
6. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 81.4/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ83
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ83
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SLX1B
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000181625-SLX1B/subcellular
- Data harvested: 2026-06-04 03:20:53
