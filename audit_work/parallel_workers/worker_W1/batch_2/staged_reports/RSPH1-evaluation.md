---
type: protein-evaluation
gene: "RSPH1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: rejected
---

## RSPH1 -- Re-evaluation Report (REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RSPH1 / TSA2, TSGA2 |
| Protein Name | Radial spoke head 1 homolog |
| Protein Size | 309 aa, ~35.1 kDa |
| UniProt ID | Q8WYR4 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 3/10 | x4 | **12** | UniProt: Nuclear by similarity only |
| Protein Size | 10/10 | x1 | **10** | 309 aa, ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~27 (21-40) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate confidence (mean pLDDT 74.2); Experimental PDB: 8J07 |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 6/10 | x3 | **18** | STRING: 3 experimentally validated PPIs; IntAct: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.0** | Domain (2) + AlphaFold (pLDDT 74) consistency (+0.5); STRING + IntAct cross-validation (+0.5); Experimental PDB structur |
| **Raw Total** | | | **110.0/180** | |
| **Normalized Total** | | | **61.1/100** | |

### 3. Rejection Check
**REJECTED** for: Nuclear≤3 (3/10)

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm | By similarity |
| UniProt | Chromosome | By similarity |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme | Experimental |
| UniProt | Cytoplasm, cytoskeleton, flagellum axoneme | By similarity |
| GO-CC | condensed nuclear chromosome | IEA:Ensembl |
| GO-CC | nucleus | HDA:UniProtKB |
| HPA | Centrosome, Basal body, Acrosome, Mid piece | Reliability: Uncertain |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nuclear by similarity only. Score 3/10 reflects weak evidence for nuclear localization. REJECTED: Nuclear score <= 3.

### 4. Protein Size Assessment

RSPH1 is 309 amino acids in length (~35.1 kDa). 309 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 27 |
| PubMed broad count | 43 |
| Novelty category | PubMed ~27 (21-40) |

**Key Research Context**: Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia. Published literature includes studies on RSPH1's role in cellular processes. PubMed count of ~27 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 20301301 | Primary Ciliary Dyskinesia.... |  |
| 37601242 | CCDC189 affects sperm flagellum formation by interacting with CABCOCO1.... | National science review |
| 36820148 | An Integrated Analysis Reveals Ciliary Abnormalities in Antrochoanal Polyps.... | Journal of inflammation research |
| 25789548 | Immunofluorescence Analysis and Diagnosis of Primary Ciliary Dyskinesia with Rad... | American journal of respiratory cell and |
| 36873931 | Pathogenic gene variants in CCDC39, CCDC40, RSPH1, RSPH9, HYDIN, and SPEF2 cause... | Frontiers in genetics |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 experimental |
| Mean pLDDT | 74.2 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate confidence (mean pLDDT 74.2); Experimental PDB: 8J07. Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR003409 | Annotated domain |
| Pfam | PF02493 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 1 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RSPH4A | 0.990 | 0.828 | 0.0 | 0.932 |
| RSPH9 | 0.982 | 0.797 | 0.0 | 0.906 |
| RSPH6A | 0.861 | 0.583 | 0.0 | 0.664 |
| ZMYND10 | 0.844 | 0.144 | 0.0 | 0.772 |
| RSPH3 | 0.832 | 0.139 | 0.0 | 0.794 |
| CCDC114 | 0.814 | 0.000 | 0.0 | 0.787 |
| CCDC103 | 0.813 | 0.000 | 0.0 | 0.786 |
| CCDC40 | 0.781 | 0.114 | 0.0 | 0.748 |

**PPI Assessment**: STRING: 3 experimentally validated PPIs; IntAct: 15 interactions. Score 6/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Non-nuclear/Weak | Inconsistent/Weak |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Domain (2) + AlphaFold (pLDDT 74) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +2.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (Score: 61.1/100)

**Core Strengths**:
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~27)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Rich PPI network with experimental validation

**Risks / Uncertainties**:
1. Nuclear localization score <= 3, automatic rejection criterion
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: REJECTED. Rejected for: Nuclear≤3 (3/10).

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYR4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q8WYR4-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RSPH1%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000160188-RSPH1
