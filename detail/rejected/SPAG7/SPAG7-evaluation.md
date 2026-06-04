---
type: protein-evaluation
gene: "SPAG7"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SPAG7 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SPAG7 |
| Protein Name | Sperm-associated antigen 7 |
| Protein Size | 227 aa, ~26.0 kDa |
| UniProt ID | O75391 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Nucleus; HPA: Nucleoplasm; (Reliability: Supported); GO-CC: nucleus |
| Protein Size | 10/10 | x1 | **10** | 227 aa, ~26.0 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=10 (<=20 -> 10) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold v6 pLDDT=85.5; PDB: 2CPM |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: IPR001374, IPR036867, IPR034068, IPR017330; Pfam: PF01424 |
| PPI Network | 4/10 | x3 | **12** | STRING 9 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.0** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **150.0/180** | |
| **Normalized Total** | | | **83.3/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Curated |
| GO-CC | nucleus | IEA:UniProtKB-SubCell |
| HPA | Nucleoplasm | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nucleus; HPA: Nucleoplasm; (Reliability: Supported); GO-CC: nucleus. Score 9/10 reflects Multiple independent data sources confirm nuclear localization with high HPA reliability.

### 4. Protein Size Assessment

SPAG7 is 227 amino acids in length (~26.0 kDa). Ideal size (227 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| Alias context | None |
| Novelty category | <=20 -> 10 |

**Key Research Context**: No functional annotation available. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 37304876 | Alterations in gene expressions of Caco-2 cell responses to LPS and ploy(I:C) stimulation. | PeerJ |
| 39056292 | SPAG7 deletion causes intrauterine growth restriction, resulting in adulthood obesity and metabolic dysfunction. | eLife |
| 24452265 | SPAG7 is a candidate gene for the periodic fever, aphthous stomatitis, pharyngitis and adenopathy (PFAPA) syndrome. | Genes and immunity |
| 34862790 | Sperm associated antigen 7 is activated by T3 during Xenopus tropicalis metamorphosis via a thyroid hormone response ele | Development, growth & differentiation |
| 34009011 | Gene Expression Alteration of Sperm-Associated Antigens in Human Cryopreserved Sperm. | Biopreservation and biobanking |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 1 experimental |
| Mean pLDDT | 85.5 |
| High confidence residues (pLDDT > 90) | 46.7% |
| Confident residues (pLDDT 70-90) | 40.5% |
| Medium confidence (pLDDT 50-70) | 11.9% |
| Low confidence (pLDDT < 50) | 0.9% |
| Ordered region (pLDDT > 70) | 87.2% |
| Available PDB entries | 2CPM |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: PDB experimental structure + AlphaFold high quality (pLDDT=85.5). Structure credible. Score 8/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001374 |  |
| InterPro | IPR036867 |  |
| InterPro | IPR034068 |  |
| InterPro | IPR017330 |  |
| Pfam | PF01424 |  |

**Domain Analysis**:    The protein contains 4 InterPro and 1 Pfam domain annotations. Score 8/10 reflects strong domain architecture. Multiple annotated domains with high AlphaFold quality; domain folds credible.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 9 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| FAM220A | 0.952 | 0.000 | 0.0 | 0.952 |
| CD34 | 0.495 | 0.000 | 0.0 | 0.495 |
| RPAP3 | 0.467 | 0.000 | 0.0 | 0.446 |
| SMIM7 | 0.455 | 0.000 | 0.0 | 0.444 |
| M0QYU9_HUMAN | 0.447 | 0.000 | 0.0 | 0.447 |
| KLHL20 | 0.440 | 0.440 | 0.0 | 0.000 |
| TEX261 | 0.439 | 0.000 | 0.0 | 0.439 |
| ABHD16A | 0.430 | 0.421 | 0.0 | 0.000 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| ABHD16A | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216829 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 |
| RAN | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.107 |
| SLC25A32 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| LXN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLHL20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| KRT27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |

**PPI Assessment**: STRING 9 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Well-folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus (3 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0.5
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +2.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 83.3/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (227 aa) for experimental characterization
3. High novelty (PubMed count ~10)
4. High-quality AlphaFold prediction (pLDDT 85.5)
5. Well-annotated domain architecture (6 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 2CPM

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 83.3/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75391
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75391
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPAG7
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000091640-SPAG7/subcellular
- Data harvested: 2026-06-04 03:25:27
