---
type: protein-evaluation
gene: "SNTB2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SNTB2 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SNTB2 / D16S2531E, SNT2B2, SNTL |
| Protein Name | Beta-2-syntrophin |
| Protein Size | 540 aa, ~58.0 kDa |
| UniProt ID | Q13425 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Membrane, Cytoplasmic vesicle, secretory vesicle membrane, Cell junction; HPA: Golgi apparatus, Plasma membrane, Centriolar satelli |
| Protein Size | 10/10 | x1 | **10** | 540 aa, ~58.0 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=14 (<=20 -> 10) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold v6 pLDDT=78.7; PDB: 2VRF |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR001478, IPR036034, IPR011993, IPR001849, IPR041428; Pfam: PF00595, PF00169, PF18012 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.0** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **140.0/180** | |
| **Normalized Total** | | | **77.8/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Membrane | Curated |
| UniProt | Cytoplasmic vesicle, secretory vesicle membrane | Curated |
| UniProt | Cell junction | By similarity |
| UniProt | Cytoplasm, cytoskeleton | Curated |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Golgi apparatus, Plasma membrane, Centriolar satellite, Basal body; Additional: Nucleoplasm, Primary cilium transition zone | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Membrane, Cytoplasmic vesicle, secretory vesicle membrane, Cell junction; HPA: Golgi apparatus, Plasma membrane, Centriolar satellite; (Reliability: Approved); GO-CC: nucleoplasm. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SNTB2 is 540 amino acids in length (~58.0 kDa). Ideal size (540 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 14 |
| PubMed broad count | 15 |
| Alias context | Aliases observed but not used for scoring: D16S2531E, SNT2B2, SNTL |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Adapter protein that binds to and probably organizes the subcellular localization of a variety of membrane proteins. May link various receptors to the actin cytoskeleton and the dystrophin glycoprotein complex. May play a role in the regulation of secretory granules via its interaction with PTPRN. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 25625330 | Lipid abnormalities in alpha/beta2-syntrophin null mice are independent from ABCA1. | Biochimica et biophysica acta |
| 30014220 | The utrophin-beta 2 syntrophin complex regulates adipocyte lipid droplet size independent of adipogenesis. | Molecular and cellular biochemistry |
| 30990585 | Adipocyte Hypertrophy and Improved Postprandial Lipid Response in Beta 2 Syntrophin Deficient Mice. | Cellular physiology and biochemistry : international journal |
| 23860432 | Adiponectin receptor 1 C-terminus interacts with PDZ-domain proteins such as syntrophins. | Experimental and molecular pathology |
| 26079703 | Evaluation of the specificity of four commercially available antibodies to alpha-syntrophin. | Analytical biochemistry |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 1 experimental |
| Mean pLDDT | 78.7 |
| High confidence residues (pLDDT > 90) | 51.1% |
| Confident residues (pLDDT 70-90) | 22.8% |
| Medium confidence (pLDDT 50-70) | 6.1% |
| Low confidence (pLDDT < 50) | 20.0% |
| Ordered region (pLDDT > 70) | 73.9% |
| Available PDB entries | 2VRF |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: PDB experimental structure + AlphaFold high quality (pLDDT=78.7). Structure credible. Score 8/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001478 |  |
| InterPro | IPR036034 |  |
| InterPro | IPR011993 |  |
| InterPro | IPR001849 |  |
| InterPro | IPR041428 |  |
| InterPro | IPR015482 |  |
| Pfam | PF00595 |  |
| Pfam | PF00169 |  |
| Pfam | PF18012 |  |
| Pfam | PF23012 |  |

**Domain Analysis**:    The protein contains 7 InterPro and 4 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| UTRN | 0.990 | 0.800 | 0.4 | 0.928 |
| DMD | 0.985 | 0.777 | 0.5 | 0.867 |
| DTNA | 0.974 | 0.749 | 0.0 | 0.903 |
| DTNB | 0.937 | 0.762 | 0.0 | 0.745 |
| SNTG2 | 0.927 | 0.708 | 0.5 | 0.502 |
| SNTB1 | 0.923 | 0.686 | 0.5 | 0.498 |
| SNTA1 | 0.905 | 0.596 | 0.5 | 0.511 |
| DAG1 | 0.901 | 0.336 | 0.5 | 0.701 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| ENSMUSP00000148684.2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21115837|imex:IM-26913 |
| EBI-295968 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:9214383 |
| Dmd | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:9214383 |
| UTRN | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:8576247 |
| EBI-368317 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:8576247 |
| ABCA1 | psi-mi:"MI:0004"(affinity chromatography technology) | pubmed:16192269|imex:IM-20073 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| PTPRN | psi-mi:"MI:0018"(two hybrid) | pubmed:11043403 |

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

**Recommendation Level**: Recommended (Score: 77.8/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (540 aa) for experimental characterization
3. High novelty (PubMed count ~14)
4. AlphaFold prediction available (pLDDT 78.7)
5. Well-annotated domain architecture (9 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 2VRF

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 77.8/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q13425
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13425
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNTB2
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000168807-SNTB2/subcellular
- Data harvested: 2026-06-04 03:23:48
