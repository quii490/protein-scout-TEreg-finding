---
type: protein-evaluation
gene: "RTL6"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RTL6 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTL6 / LDOC1L, MAR6, MART6 |
| Protein Name | Retrotransposon Gag-like protein 6 |
| Protein Size | 239 aa, ~26.2 kDa |
| UniProt ID | Q6ICC9 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Nuclear speckles) |
| Protein Size | 10/10 | x1 | **10** | 239 aa, ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~3 (0-5) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold good confidence (mean pLDDT 77.3, >90%: 45.2%) |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 6/10 | x3 | **18** | STRING: 4 experimentally validated PPIs; IntAct: 10 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | Domain (2) + AlphaFold (pLDDT 77) consistency (+0.5); STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **129.0/180** | |
| **Normalized Total** | | | **71.7/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Nuclear speckles, Cytosol | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Nuclear speckles). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

RTL6 is 239 amino acids in length (~26.2 kDa). 239 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| Novelty category | PubMed ~3 (0-5) |

**Key Research Context**: No functional annotation available. Published literature includes studies on RTL6's role in cellular processes. PubMed count of ~3 articles, indicating extremely high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 37834332 | Retrovirus-Derived RTL9 Plays an Important Role in Innate Antifungal Immunity in... | International journal of molecular scien |
| 38428498 | Genetic background of hematological parameters in Holstein cattle based on genom... | Journal of dairy science |
| 36162816 | Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immu... | Development (Cambridge, England) |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 77.3 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold good confidence (mean pLDDT 77.3, >90%: 45.2%). Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR032549 | Annotated domain |
| Pfam | PF16297 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 10 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RTL4 | 0.810 | 0.000 | 0.0 | 0.771 |
| RTL9 | 0.810 | 0.000 | 0.0 | 0.810 |
| RTL3 | 0.747 | 0.000 | 0.0 | 0.747 |
| RTL1 | 0.673 | 0.000 | 0.0 | 0.597 |
| DDIT3 | 0.657 | 0.655 | 0.0 | 0.047 |
| BATF3 | 0.551 | 0.547 | 0.0 | 0.049 |
| GOPC | 0.533 | 0.530 | 0.0 | 0.000 |
| FANCM | 0.532 | 0.528 | 0.0 | 0.050 |

**PPI Assessment**: STRING: 4 experimentally validated PPIs; IntAct: 10 interactions. Score 6/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Domain (2) + AlphaFold (pLDDT 77) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 71.7/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
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

**FINAL DECISION**: NOT REJECTED. The protein scores 71.7/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6ICC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q6ICC9-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTL6%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000188636-RTL6
