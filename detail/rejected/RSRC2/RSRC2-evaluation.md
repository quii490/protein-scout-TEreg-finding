---
type: protein-evaluation
gene: "RSRC2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RSRC2 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RSRC2 / None |
| Protein Name | Arginine/serine-rich coiled-coil protein 2 |
| Protein Size | 434 aa, ~50.6 kDa |
| UniProt ID | Q7L4I2 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Nuclear speckles) |
| Protein Size | 10/10 | x1 | **10** | 434 aa, ideal range |
| Research Novelty | 9/10 | x5 | **45** | PubMed ~8 (6-10) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold low confidence (mean pLDDT 55.8) |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 5/10 | x3 | **15** | STRING: 2 medium-confidence interactions; IntAct: 15 interactions; UniProt curated: 16 interactions |
| Cross-Validation Bonus | -- | -- | **+0.5** | STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **111.5/180** | |
| **Normalized Total** | | | **61.9/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Nucleoli fibrillar center, Nuclear speckles, Cytosol | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Nuclear speckles). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

RSRC2 is 434 amino acids in length (~50.6 kDa). 434 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| Novelty category | PubMed ~8 (6-10) |

**Key Research Context**: No functional annotation available. Published literature includes studies on RSRC2's role in cellular processes. PubMed count of ~8 articles, indicating high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 17203224 | A novel gene, RSRC2, inhibits cell proliferation and affects survival in esophag... | International journal of oncology |
| 38201443 | RSRC2 Expression Inhibits Malignant Progression of Triple-Negative Breast Cancer... | Cancers |
| 35669517 | Differential Degradation of TRA2A and PYCR2 Mediated by Ubiquitin E3 Ligase E4B.... | Frontiers in cell and developmental biol |
| 41841495 | RSRC2 is a novel RNA-binding protein that safeguards mitotic fidelity by interac... | Nucleic acids research |
| 20444257 | Array-based gene expression, CGH and tissue data defines a 12q24 gain in neurobl... | BMC cancer |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 55.8 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 55.8). Score 3/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR028124 | Annotated domain |
| Pfam | PF15477 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 16 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RBM25 | 0.869 | 0.000 | 0.0 | 0.312 |
| ARID4B | 0.750 | 0.000 | 0.0 | 0.000 |
| KNTC1 | 0.689 | 0.000 | 0.0 | 0.675 |
| SRSF11 | 0.678 | 0.000 | 0.0 | 0.000 |
| TRA2A | 0.617 | 0.000 | 0.0 | 0.540 |
| RBM39 | 0.613 | 0.081 | 0.0 | 0.000 |
| YTHDC1 | 0.608 | 0.000 | 0.0 | 0.000 |
| ZCCHC8 | 0.599 | 0.000 | 0.0 | 0.359 |

**PPI Assessment**: STRING: 2 medium-confidence interactions; IntAct: 15 interactions; UniProt curated: 16 interactions. Score 5/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 61.9/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 61.9/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q7L4I2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q7L4I2-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RSRC2%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000111011-RSRC2
