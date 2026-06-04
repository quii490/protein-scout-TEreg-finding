---
type: protein-evaluation
gene: "SNF8"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SNF8 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SNF8 / EAP30 |
| Protein Name | Vacuolar-sorting protein SNF8 |
| Protein Size | 258 aa, ~28.9 kDa |
| UniProt ID | Q96H20 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, Endosome membrane, Nucleus; HPA: Cytosol; (Reliability: Supported); GO-CC: nucleoplasm, nucleus, perinuclear region of c |
| Protein Size | 10/10 | x1 | **10** | 258 aa, ~28.9 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=20 (<=20 -> 10) |
| 3D Structure | 9/10 | x3 | **27** | AlphaFold v6 pLDDT=84.9; PDB: 2ZME, 3CUQ |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: IPR016689, IPR040608, IPR036388, IPR036390; Pfam: PF04157 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.0** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **145.0/180** | |
| **Normalized Total** | | | **80.6/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | Curated |
| UniProt | Endosome membrane | Curated |
| UniProt | Nucleus | Curated |
| UniProt | Late endosome membrane | Curated |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| GO-CC | perinuclear region of cytoplasm | IDA:UniProtKB |
| HPA | Cytosol; Additional: Nucleoplasm | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Cytoplasm, Endosome membrane, Nucleus; HPA: Cytosol; (Reliability: Supported); GO-CC: nucleoplasm, nucleus, perinuclear region of cytoplasm. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SNF8 is 258 amino acids in length (~28.9 kDa). Ideal size (258 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 20 |
| PubMed broad count | 38 |
| Alias context | Aliases observed but not used for scoring: EAP30 |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Component of the endosomal sorting complex required for transport II (ESCRT-II), which is required for multivesicular body (MVB) formation and sorting of endosomal cargo proteins into MVBs, and plays a role in autophagy (PubMed:38423010). The MVB pathway mediates delivery of transmembrane proteins i. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 32829877 | VPS-22/SNF8 regulates longevity via modulating the activity of DAF-16 in C. elegans. | Biochemical and biophysical research communications |
| 30154260 | Polygenic Analysis in Absence of Major Effector ATF1 Unveils Novel Components in Yeast Flavor Ester Biosynthesis. | mBio |
| 7785322 | Molecular analysis of the SNF8 gene of Saccharomyces cerevisiae. | Yeast (Chichester, England) |
| 23171048 | SNF8, a member of the ESCRT-II complex, interacts with TRPC6 and enhances its channel activity. | BMC cell biology |
| 32255230 | ESCRT-dependent protein sorting is required for the viability of yeast clathrin-mediated endocytosis mutants. | Traffic (Copenhagen, Denmark) |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 2 experimental |
| Mean pLDDT | 84.9 |
| High confidence residues (pLDDT > 90) | 48.8% |
| Confident residues (pLDDT 70-90) | 36.4% |
| Medium confidence (pLDDT 50-70) | 12.8% |
| Low confidence (pLDDT < 50) | 1.9% |
| Ordered region (pLDDT > 70) | 85.2% |
| Available PDB entries | 2ZME, 3CUQ |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: PDB experimental structures + AlphaFold high quality (pLDDT=84.9). Structure credible. Score 9/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR016689 |  |
| InterPro | IPR040608 |  |
| InterPro | IPR036388 |  |
| InterPro | IPR036390 |  |
| Pfam | PF04157 |  |

**Domain Analysis**:    The protein contains 4 InterPro and 1 Pfam domain annotations. Score 8/10 reflects strong domain architecture. Multiple annotated domains with high AlphaFold quality; domain folds credible.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| VPS25 | 0.999 | 0.997 | 0.9 | 0.999 |
| VPS36 | 0.999 | 0.999 | 0.9 | 0.999 |
| CHMP6 | 0.999 | 0.954 | 0.9 | 0.969 |
| VPS28 | 0.992 | 0.451 | 0.9 | 0.869 |
| TSG101 | 0.984 | 0.492 | 0.9 | 0.707 |
| CHMP2A | 0.980 | 0.288 | 0.9 | 0.709 |
| CHMP3 | 0.979 | 0.129 | 0.9 | 0.775 |
| ELL | 0.971 | 0.594 | 0.0 | 0.931 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT- |
| VPS25 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT- |
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT- |
| VPS36 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15329733 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| ADORA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| VPS20 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Well-folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus (2 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0.5
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +2.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 80.6/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (258 aa) for experimental characterization
3. High novelty (PubMed count ~20)
4. AlphaFold prediction available (pLDDT 84.9)
5. Well-annotated domain architecture (6 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 2ZME, 3CUQ

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 80.6/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96H20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96H20
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNF8
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000159210-SNF8/subcellular
- Data harvested: 2026-06-04 03:23:21
