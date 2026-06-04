---
type: protein-evaluation
gene: "RIT2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RIT2 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RIT2 / RIN, ROC2 |
| Protein Name | GTP-binding protein Rit2 |
| Protein Size | 217 aa, ~24.7 kDa |
| UniProt ID | Q99578 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm, Golgi ap |
| Protein Size | 10/10 | x1 | **10** | 217 aa, ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~38 (21-40) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold high confidence (mean pLDDT 87.8, >90%: 68.7%) |
| Regulatory Domains | 8/10 | x2 | **16** | 5 annotated domains (InterPro: 4, Pfam: 1) |
| PPI Network | 6/10 | x3 | **18** | STRING: 2 experimentally validated PPIs; IntAct: 11 interactions |
| Cross-Validation Bonus | -- | -- | **+2.0** | Multi-DB nuclear localization consensus (+1.0); Domain (5) + AlphaFold (pLDDT 88) consistency (+0.5); STRING + IntAct cr |
| **Raw Total** | | | **138.0/180** | |
| **Normalized Total** | | | **76.7/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| UniProt | Cell membrane | Experimental |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:ParkinsonsUK-UCL |
| HPA | Nucleoplasm, Golgi apparatus, Cytosol | Reliability: Supported |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm, Golgi apparatus, Cytosol). Score 9/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RIT2 is 217 amino acids in length (~24.7 kDa). 217 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 38 |
| PubMed broad count | 67 |
| Novelty category | PubMed ~38 (21-40) |

**Key Research Context**: Binds and exchanges GTP and GDP. Binds and modulates the activation of POU4F1 as gene expression regulator. Published literature includes studies on RIT2's role in cellular processes. PubMed count of ~38 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 38198537 | Molecular profiling of human substantia nigra identifies diverse neuron types as... | Science advances |
| 29860660 | RIT2: responsible and susceptible gene for neurological and psychiatric disorder... | Molecular genetics and genomics : MGG |
| 26188085 | RIT2 rs12456492 polymorphism and the risk of Parkinson's disease: A meta-analysi... | Neuroscience letters |
| 40240380 | Prioritizing Parkinson's disease risk genes in genome-wide association loci.... | NPJ Parkinson's disease |
| 31818509 | Association of RIT2 and RAB7L1 with Parkinson's disease: a case-control study in... | Neurobiology of aging |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 87.8 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high confidence (mean pLDDT 87.8, >90%: 68.7%). Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR027417 | Annotated domain |
| InterPro | IPR005225 | Annotated domain |
| InterPro | IPR001806 | Annotated domain |
| InterPro | IPR020849 | Annotated domain |
| Pfam | PF00071 | Annotated family |

**Domain Analysis**: 5 annotated domains (InterPro: 4, Pfam: 1). The protein contains 4 InterPro and 1 Pfam domain annotations. Score 8/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 11 interactions |
| UniProt Interactions | 2 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RIT1 | 0.893 | 0.788 | 0.5 | 0.063 |
| POU4F1 | 0.833 | 0.292 | 0.0 | 0.775 |
| LZTR1 | 0.802 | 0.788 | 0.0 | 0.102 |
| BRAF | 0.801 | 0.284 | 0.5 | 0.471 |
| SLC6A3 | 0.707 | 0.333 | 0.0 | 0.575 |
| POU4F2 | 0.702 | 0.000 | 0.0 | 0.702 |
| SYT4 | 0.661 | 0.000 | 0.0 | 0.478 |
| CALM1 | 0.628 | 0.355 | 0.0 | 0.428 |

**PPI Assessment**: STRING: 2 experimentally validated PPIs; IntAct: 11 interactions. Score 6/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- Domain (5) + AlphaFold (pLDDT 88) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +2.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 76.7/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~38)
3. High-quality structural prediction (pLDDT >= 85)
4. Well-annotated domain architecture
5. Rich PPI network with experimental validation

**Risks / Uncertainties**:
3. No experimental PDB structures
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 76.7/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q99578
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q99578-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RIT2%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000152214-RIT2
