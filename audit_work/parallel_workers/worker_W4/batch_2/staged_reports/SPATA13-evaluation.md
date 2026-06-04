---
type: protein-evaluation
gene: "SPATA13"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPATA13 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPATA13 |
| Protein Name | Spermatogenesis-associated protein 13 |
| Protein Size | 652 aa, ~74.8 kDa |
| UniProt ID | Q96N96 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Cell projection, filopodium, Cell projection, lamellipodium; HPA: Nucleoplasm; (Reliability: Enhanced); GO-CC: nucleopla |
| Protein Size | 10/10 | x1 | **10** | 652 aa, ~74.8 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=18 (<=20 -> 10) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold v6 pLDDT=71.7; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR036028; Pfam: PF00621, PF00018, PF22697 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **136.5/180** | |
| **Normalized Total** | | | **75.8/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | Curated |
| UniProt | Cell projection, filopodium | Curated |
| UniProt | Cell projection, lamellipodium | Curated |
| UniProt | Cell projection, ruffle membrane | Curated |
| UniProt | Cell projection, podosome | By similarity |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm; Additional: Cytosol | Reliability: Enhanced |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Enhanced), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, Cell projection, filopodium, Cell projection, lamellipodium; HPA: Nucleoplasm; (Reliability: Enhanced); GO-CC: nucleoplasm. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SPATA13 is 652 amino acids in length (~74.8 kDa). Ideal size (652 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 18 |
| PubMed broad count | 40 |
| Alias context | None |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Acts as a guanine nucleotide exchange factor (GEF) for RHOA, RAC1 and CDC42 GTPases. Regulates cell migration and adhesion assembly and disassembly through a RAC1, PI3K, RHOA and AKT1-dependent mechanism. Increases both RAC1 and CDC42 activity, but decreases the amount of active RHOA. Required for M. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 40910032 | The ceRNA Regulatory Network in Vitiligo: Evidence from Bioinformatics Analysis. | Clinical, cosmetic and investigational dermatology |
| 32339198 | Mutations in SPATA13/ASEF2 cause primary angle closure glaucoma. | PLoS genetics |
| 41358093 | Identification of Neurotrophic Factor Related Biomarkers and Mechanistic Insights into Neuropathic Pain via Integrated B | ACS omega |
| 31020388 | The guanine nucleotide exchange factor, Spata13, influences social behaviour and nocturnal activity. | Mammalian genome : official journal of the International Mam |
| 41299718 | Overexpression of Hspa1b in the mouse hippocampus may be associated with major depressive disorder. | Behavioral and brain functions : BBF |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 71.7 |
| High confidence residues (pLDDT > 90) | 46.6% |
| Confident residues (pLDDT 70-90) | 18.1% |
| Medium confidence (pLDDT 50-70) | 4.3% |
| Low confidence (pLDDT < 50) | 31.0% |
| Ordered region (pLDDT > 70) | 64.7% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high quality prediction (pLDDT=71.7), 64.7% ordered. Structure reliable. Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR035899 |  |
| InterPro | IPR000219 |  |
| InterPro | IPR011993 |  |
| InterPro | IPR001849 |  |
| InterPro | IPR036028 |  |
| InterPro | IPR001452 |  |
| Pfam | PF00621 |  |
| Pfam | PF00018 |  |
| Pfam | PF22697 |  |

**Domain Analysis**:    The protein contains 7 InterPro and 3 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| APC | 0.983 | 0.630 | 0.9 | 0.581 |
| CDC42 | 0.949 | 0.728 | 0.4 | 0.717 |
| RAC2 | 0.936 | 0.302 | 0.9 | 0.158 |
| RAC3 | 0.933 | 0.302 | 0.9 | 0.125 |
| ARHGEF4 | 0.930 | 0.292 | 0.9 | 0.091 |
| APC2 | 0.903 | 0.051 | 0.9 | 0.000 |
| PPP1R9B | 0.818 | 0.000 | 0.0 | 0.818 |
| YWHAE | 0.772 | 0.771 | 0.0 | 0.044 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| ENSP00000371527.4 | psi-mi:"MI:0096"(pull down) | pubmed:17145773|imex:IM-25725 |
| Shank3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn.4594|imex |
| GLDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |

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

**Recommendation Level**: Recommended (Score: 75.8/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (652 aa) for experimental characterization
3. High novelty (PubMed count ~18)
4. AlphaFold prediction available (pLDDT 71.7)
5. Well-annotated domain architecture (9 domains)
6. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 75.8/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96N96
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96N96
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA13
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000182957-SPATA13/subcellular
- Data harvested: 2026-06-04 03:27:51
