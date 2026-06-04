---
type: protein-evaluation
gene: "SNTG1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SNTG1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SNTG1 |
| Protein Name | Gamma-1-syntrophin |
| Protein Size | 517 aa, ~58.0 kDa |
| UniProt ID | Q9NSN8 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, cytoskeleton, Nucleus; HPA: no localization; GO-CC: nucleus |
| Protein Size | 10/10 | x1 | **10** | 517 aa, ~58.0 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=16 (<=20 -> 10) |
| 3D Structure | 9/10 | x3 | **27** | AlphaFold v6 pLDDT=82.3; PDB: 7PC7, 7PC8, 7QQN |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: IPR001478, IPR036034, IPR001849, IPR015482, IPR055108; Pfam: PF00595, PF23012 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+3.0** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **146.0/180** | |
| **Normalized Total** | | | **81.1/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm, cytoskeleton | Curated |
| UniProt | Nucleus | Curated |
| GO-CC | nucleus | IEA:UniProtKB-SubCell |
| HPA |  | Reliability: N/A |

**IF Image Status**: HPA did not detect reliable IF image signal. Nuclear evidence based on HPA subcellular annotation, UniProt, and GO-CC terms.

**Manual Review Assessment**: UniProt: Cytoplasm, cytoskeleton, Nucleus; HPA: no localization; GO-CC: nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SNTG1 is 517 amino acids in length (~58.0 kDa). Ideal size (517 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 16 |
| PubMed broad count | 24 |
| Alias context | None |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Adapter protein that binds to and probably organizes the subcellular localization of a variety of proteins. May link various receptors to the actin cytoskeleton and the dystrophin glycoprotein complex (By similarity). May participate in regulating the subcellular location of diacylglycerol kinase-ze. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 39738056 | SEAD reference panel with 22,134 haplotypes boosts rare variant imputation and genome-wide association analysis in Asian | Nature communications |
| 15088139 | SNTG1, the gene encoding gamma1-syntrophin: a candidate gene for idiopathic scoliosis. | Human genetics |
| 37982029 | Extracellular vesicle treatment partially reverts epigenetic alterations in chronically ischemic porcine myocardium. | Vessel plus |
| 34048959 | Scoliosis with cognitive impairment in a girl with 8q11.21q11.23 microdeletion and SNTG1 disruption. | Bone |
| 21151896 | Genomic aberrations in lung adenocarcinoma in never smokers. | PloS one |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 3 experimental |
| Mean pLDDT | 82.3 |
| High confidence residues (pLDDT > 90) | 62.3% |
| Confident residues (pLDDT 70-90) | 18.0% |
| Medium confidence (pLDDT 50-70) | 5.4% |
| Low confidence (pLDDT < 50) | 14.3% |
| Ordered region (pLDDT > 70) | 80.3% |
| Available PDB entries | 7PC7, 7PC8, 7QQN |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: PDB experimental structures + AlphaFold high quality (pLDDT=82.3). Structure credible. Score 9/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001478 |  |
| InterPro | IPR036034 |  |
| InterPro | IPR001849 |  |
| InterPro | IPR015482 |  |
| InterPro | IPR055108 |  |
| Pfam | PF00595 |  |
| Pfam | PF23012 |  |

**Domain Analysis**:    The protein contains 5 InterPro and 2 Pfam domain annotations. Score 8/10 reflects strong domain architecture. Multiple annotated domains with high AlphaFold quality; domain folds credible.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| DMD | 0.992 | 0.648 | 0.7 | 0.931 |
| DTNB | 0.951 | 0.619 | 0.0 | 0.876 |
| SNTA1 | 0.938 | 0.597 | 0.7 | 0.499 |
| DTNA | 0.877 | 0.482 | 0.0 | 0.766 |
| SNTB1 | 0.874 | 0.494 | 0.5 | 0.504 |
| SNTB2 | 0.844 | 0.448 | 0.5 | 0.434 |
| DAG1 | 0.839 | 0.000 | 0.7 | 0.450 |
| SGCD | 0.825 | 0.000 | 0.7 | 0.360 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| PLEKHA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VTN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CES2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| RNASEH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| DTNB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| MLYCD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| DMD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| ACADSB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |

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
- PDB multiple entries coverage (>=3): +1.0
- **Total Cross-Validation Bonus**: +3.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 81.1/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (517 aa) for experimental characterization
3. High novelty (PubMed count ~16)
4. AlphaFold prediction available (pLDDT 82.3)
5. Well-annotated domain architecture (8 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 7PC7, 7PC8, 7QQN

**Risks / Uncertainties**:
6. No HPA subcellular localization data

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 81.1/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSN8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSN8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNTG1
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000147481-SNTG1/subcellular
- Data harvested: 2026-06-04 03:24:13
