---
type: protein-evaluation
gene: "SMTN"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SMTN -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SMTN / SMSMO |
| Protein Name | Smoothelin |
| Protein Size | 917 aa, ~99.1 kDa |
| UniProt ID | P53814 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | UniProt: Cytoplasm, cytoskeleton; HPA: Nucleoplasm; (Reliability: Supported) |
| Protein Size | 8/10 | x1 | **8** | 917 aa, ~99.1 kDa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict=40 (<=40 -> 8) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=59.0; PDB: 2D87 |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR001715, IPR036872, IPR050540, IPR022189; Pfam: PF00307, PF12510 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **109.0/180** | |
| **Normalized Total** | | | **60.6/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm, cytoskeleton | Curated |
| HPA | Nucleoplasm; Additional: Actin filaments | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, cytoskeleton; HPA: Nucleoplasm; (Reliability: Supported). Score 4/10 reflects Weak nuclear signal with multiple sources showing mixed or non-nuclear preference.

### 4. Protein Size Assessment

SMTN is 917 amino acids in length (~99.1 kDa). Acceptable size (917 aa), suitable for routine experiments. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 40 |
| PubMed broad count | 158 |
| Alias context | Aliases observed but not used for scoring: SMSMO |
| Novelty category | <=40 -> 8 |

**Key Research Context**: Structural protein of the cytoskeleton. Published literature indicates growing research activity. Very novel, only a few foundational studies.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 41477349 | The cytoskeletal protein smoothelin maintains homologous recombination repair by stabilizing RAD51 in an HUWE1-dependent | Acta pharmaceutica Sinica. B |
| 29310803 | Smoothelins and the Control of Muscle Contractility. | Advances in pharmacology (San Diego, Calif.) |
| 30990690 | Identification of Filamin A Mechanobinding Partner I: Smoothelin Specifically Interacts with the Filamin A Mechanosensit | Biochemistry |
| 17398105 | Changes in inflammatory processes associated with selective vulnerability following mild impairment of oxidative metabol | Neurobiology of disease |
| 17482317 | Responses of the mitochondrial alpha-ketoglutarate dehydrogenase complex to thiamine deficiency may contribute to region | Neurochemistry international |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 1 experimental |
| Mean pLDDT | 59.0 |
| High confidence residues (pLDDT > 90) | 17.6% |
| Confident residues (pLDDT 70-90) | 20.3% |
| Medium confidence (pLDDT 50-70) | 10.0% |
| Low confidence (pLDDT < 50) | 52.1% |
| Ordered region (pLDDT > 70) | 37.9% |
| Available PDB entries | 2D87 |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=59.0), 37.9% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001715 |  |
| InterPro | IPR036872 |  |
| InterPro | IPR050540 |  |
| InterPro | IPR022189 |  |
| Pfam | PF00307 |  |
| Pfam | PF12510 |  |

**Domain Analysis**:    The protein contains 4 InterPro and 2 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| MYH11 | 0.803 | 0.000 | 0.0 | 0.780 |
| CNN1 | 0.799 | 0.000 | 0.0 | 0.758 |
| TAGLN | 0.798 | 0.000 | 0.0 | 0.762 |
| HIRA | 0.763 | 0.000 | 0.0 | 0.763 |
| SMTNL1 | 0.727 | 0.000 | 0.5 | 0.432 |
| MYOCD | 0.715 | 0.000 | 0.0 | 0.681 |
| FLNA | 0.673 | 0.087 | 0.0 | 0.591 |
| PDLIM7 | 0.652 | 0.000 | 0.5 | 0.089 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Nphp4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| BRMS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16919237|imex:IM-19611 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technology) | imex:IM-13781|pubmed:21182203 |
| ENSP00000328635.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| GEM | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Non-nuclear/Weak | Inconsistent/Weak |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus: +0
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 60.6/100)

**Core Strengths**:
1. Ideal protein size (917 aa) for experimental characterization
2. High novelty (PubMed count ~40)
3. AlphaFold prediction available (pLDDT 59.0)
4. Well-annotated domain architecture (7 domains)
5. Moderate PPI data available
6. Experimental PDB structures: 2D87

**Risks / Uncertainties**:
1. Moderate/weak nuclear localization evidence

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 60.6/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P53814
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53814
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMTN
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000183963-SMTN/subcellular
- Data harvested: 2026-06-04 03:22:33
