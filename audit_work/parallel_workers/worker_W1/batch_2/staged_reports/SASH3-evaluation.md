---
type: protein-evaluation
gene: "SASH3"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SASH3 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SASH3 / None |
| Protein Name | Unknown |
| Protein Size | 0 aa, ~0.0 kDa |
| UniProt ID | N/A |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Plasma membrane) |
| Protein Size | 0/10 | x1 | **0** | Unknown |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~22 (21-40) |
| 3D Structure | 2/10 | x3 | **6** | No AlphaFold data |
| Regulatory Domains | 0/10 | x2 | **0** | No data |
| PPI Network | 3/10 | x3 | **9** | STRING: 4 medium-confidence interactions; IntAct: 3 interactions |
| Cross-Validation Bonus | -- | -- | **+0.5** | STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **70.5/180** | |
| **Normalized Total** | | | **39.2/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Nucleoplasm, Nuclear bodies, Plasma membrane | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Plasma membrane). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

SASH3 is 0 amino acids in length (~0.0 kDa). Unknown. Score 0/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 22 |
| PubMed broad count | 29 |
| Novelty category | PubMed ~22 (21-40) |

**Key Research Context**: No functional annotation available. Published literature includes studies on SASH3's role in cellular processes. PubMed count of ~22 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 35753512 | Clinical exome sequencing of 1000 families with complex immune phenotypes: Towar... | The Journal of allergy and clinical immu |
| 37963845 | Integrated analysis of single-cell RNA-seq and bulk RNA-seq unravels the heterog... | Aging |
| 33876203 | SASH3 variants cause a novel form of X-linked combined immunodeficiency with imm... | Blood |
| 37646304 | Evans syndrome caused by a deleterious mutation affecting the adaptor protein SA... | British journal of haematology |
| 36341956 | SAM1 domain of SASH1 harbors distinctive structural heterogeneity.... | Journal of structural biology |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Not available |
| PDB Entries | 0 experimental |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: No AlphaFold data. Score 2/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| N/A | No InterPro domains | -- |

**Domain Analysis**: No data. The protein contains 0 InterPro and 0 Pfam domain annotations. Score 0/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 3 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RASAL3 | 0.839 | 0.000 | 0.0 | 0.482 |
| LAPTM5 | 0.719 | 0.000 | 0.0 | 0.402 |
| CD53 | 0.715 | 0.000 | 0.0 | 0.229 |
| ARHGAP30 | 0.707 | 0.000 | 0.0 | 0.413 |
| NCKAP1L | 0.669 | 0.000 | 0.0 | 0.364 |
| ARHGAP9 | 0.663 | 0.000 | 0.0 | 0.335 |
| MYO1F | 0.627 | 0.000 | 0.0 | 0.325 |
| TAGAP | 0.609 | 0.000 | 0.0 | 0.335 |

**PPI Assessment**: STRING: 4 medium-confidence interactions; IntAct: 3 interactions. Score 3/10.

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

**Recommendation Level**: Not prioritized (Score: 39.2/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Moderate novelty (PubMed count ~22)
5. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures
5. Limited PPI network data
6. No HPA IF experimental confirmation
7. No UniProt data available

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 39.2/100 on the /180 scoring system. Not prioritized for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/N/A

- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SASH3%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000122122-SASH3
