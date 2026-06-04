---
type: protein-evaluation
gene: "SAGE1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SAGE1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAGE1 / SAGE |
| Protein Name | Sarcoma antigen 1 |
| Protein Size | 904 aa, ~99.2 kDa |
| UniProt ID | Q9NXZ1 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm, Nuclear  |
| Protein Size | 5/10 | x1 | **5** | 904 aa, challenging |
| Research Novelty | 9/10 | x5 | **45** | PubMed ~10 (6-10) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold low confidence (mean pLDDT 50.2); Experimental PDB: 8HPP |
| Regulatory Domains | 7/10 | x2 | **14** | 3 annotated domains (InterPro: 2, Pfam: 1) |
| PPI Network | 2/10 | x3 | **6** | STRING: 7 high-confidence interactions (score≥0.7) |
| Cross-Validation Bonus | -- | -- | **+2.0** | Multi-DB nuclear localization consensus (+1.0); Experimental PDB structural validation (+1.0) |
| **Raw Total** | | | **123.0/180** | |
| **Normalized Total** | | | **68.3/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| GO-CC | nuclear body | IDA:HPA |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm, Nuclear bodies | Reliability: Enhanced |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm, Nuclear bodies). Score 9/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

SAGE1 is 904 amino acids in length (~99.2 kDa). 904 aa, challenging. Score 5/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 10 |
| PubMed broad count | 34 |
| Novelty category | PubMed ~10 (6-10) |

**Key Research Context**: No functional annotation available. Published literature includes studies on SAGE1's role in cellular processes. PubMed count of ~10 articles, indicating high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 40415416 | The progression of multiple myeloma is regulated by LILRB1 via the GATA2-SAGE1 p... | British journal of haematology |
| 35651938 | Identification of Novel Characteristics in TP53-Mutant Hepatocellular Carcinoma ... | Frontiers in genetics |
| 39161926 | Characterization of RNA Processing Genes in Colon Cancer for Predicting Clinical... | Biomarker insights |
| 21706474 | OCT2, SSX and SAGE1 reveal the phenotypic heterogeneity of spermatocytic seminom... | The Journal of pathology |
| 38862430 | Pindel-TD: A Tandem Duplication Detector Based on A Pattern Growth Approach.... | Genomics, proteomics & bioinformatics |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 experimental |
| Mean pLDDT | 50.2 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 50.2); Experimental PDB: 8HPP. Score 5/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR029307 | Annotated domain |
| InterPro | IPR051113 | Annotated domain |
| Pfam | PF15300 | Annotated family |

**Domain Analysis**: 3 annotated domains (InterPro: 2, Pfam: 1). The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 0 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| DDX43 | 0.869 | 0.000 | 0.0 | 0.869 |
| SPA17 | 0.815 | 0.000 | 0.0 | 0.815 |
| MAGEC2 | 0.812 | 0.000 | 0.0 | 0.772 |
| PRSS50 | 0.771 | 0.000 | 0.0 | 0.771 |
| GAGE1 | 0.754 | 0.000 | 0.0 | 0.714 |
| PAGE5 | 0.737 | 0.000 | 0.0 | 0.720 |
| MAGEA1 | 0.727 | 0.000 | 0.0 | 0.655 |
| ADAM2 | 0.698 | 0.000 | 0.0 | 0.690 |

**PPI Assessment**: STRING: 7 high-confidence interactions (score≥0.7). Score 2/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Sparse |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +2.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 68.3/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Workable protein size (904 aa)
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture

**Risks / Uncertainties**:
5. Limited PPI network data
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 68.3/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXZ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9NXZ1-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SAGE1%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000181433-SAGE1
