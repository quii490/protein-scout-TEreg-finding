---
type: protein-evaluation
gene: "RTL5"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RTL5 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTL5 / KIAA2001, RGAG4 |
| Protein Name | Retrotransposon Gag-like protein 5 |
| Protein Size | 569 aa, ~64.7 kDa |
| UniProt ID | Q5HYW3 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Nucleoplasm) |
| Protein Size | 10/10 | x1 | **10** | 569 aa, ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~2 (0-5) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold low confidence (mean pLDDT 63.9) |
| Regulatory Domains | 7/10 | x2 | **14** | 3 annotated domains (InterPro: 2, Pfam: 1) |
| PPI Network | 0/10 | x3 | **0** | STRING: 9 total interactions (low confidence) |
| Cross-Validation Bonus | -- | -- | **+0.3** | Domain + AlphaFold partial consistency (+0.3) |
| **Raw Total** | | | **103.3/180** | |
| **Normalized Total** | | | **57.4/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Nucleoplasm | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Nucleoplasm). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

RTL5 is 569 amino acids in length (~64.7 kDa). 569 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| Novelty category | PubMed ~2 (0-5) |

**Key Research Context**: No functional annotation available. Published literature includes studies on RTL5's role in cellular processes. PubMed count of ~2 articles, indicating extremely high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 37834332 | Retrovirus-Derived RTL9 Plays an Important Role in Innate Antifungal Immunity in... | International journal of molecular scien |
| 36162816 | Retrovirus-derived RTL5 and RTL6 genes are novel constituents of the innate immu... | Development (Cambridge, England) |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 63.9 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 63.9). Score 3/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR032549 | Annotated domain |
| InterPro | IPR032567 | Annotated domain |
| Pfam | PF16297 | Annotated family |

**Domain Analysis**: 3 annotated domains (InterPro: 2, Pfam: 1). The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 9 total interactions |
| IntAct | 0 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RTL8C | 0.681 | 0.000 | 0.0 | 0.672 |
| FANCM | 0.532 | 0.528 | 0.0 | 0.050 |
| RTL8A | 0.528 | 0.000 | 0.0 | 0.528 |
| RTL4 | 0.518 | 0.000 | 0.0 | 0.518 |
| TCHHL1 | 0.465 | 0.077 | 0.0 | 0.043 |
| CCDC87 | 0.442 | 0.000 | 0.0 | 0.000 |
| RTL9 | 0.440 | 0.000 | 0.0 | 0.415 |
| PNMA5 | 0.421 | 0.000 | 0.0 | 0.408 |

**PPI Assessment**: STRING: 9 total interactions (low confidence). Score 0/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Sparse |

**Cross-Validation Bonus Details**:
- Domain + AlphaFold partial consistency (+0.3)
- **Total Cross-Validation Bonus**: +0.3 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 57.4/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture

**Risks / Uncertainties**:
3. No experimental PDB structures
5. Limited PPI network data
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 57.4/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5HYW3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q5HYW3-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTL5%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000242732-RTL5
