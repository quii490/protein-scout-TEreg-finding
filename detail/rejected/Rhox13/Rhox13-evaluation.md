---
type: protein-evaluation
gene: "Rhox13"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: rejected
---

## Rhox13 -- Re-evaluation Report (REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | Rhox13 / None |
| Protein Name | Unknown |
| Protein Size | 0 aa, ~0.0 kDa |
| UniProt ID | N/A |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | No nuclear localization evidence found |
| Protein Size | 0/10 | x1 | **0** | Unknown |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~5 (0-5) |
| 3D Structure | 2/10 | x3 | **6** | No AlphaFold data |
| Regulatory Domains | 0/10 | x2 | **0** | No data |
| PPI Network | 0/10 | x3 | **0** | STRING: No interactions found; IntAct: No interactions |
| Cross-Validation Bonus | -- | -- | **+0.0** | Insufficient cross-validation data |
| **Raw Total** | | | **56.0/180** | |
| **Normalized Total** | | | **31.1/100** | |

### 3. Rejection Check
**REJECTED** for: Nuclear≤3 (0/10)

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | No localization data | Reliability: N/A |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: No nuclear localization evidence found. Score 0/10 reflects no evidence for nuclear localization. REJECTED: Nuclear score <= 3.

### 4. Protein Size Assessment

Rhox13 is 0 amino acids in length (~0.0 kDa). Unknown. Score 0/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| Novelty category | PubMed ~5 (0-5) |

**Key Research Context**: No functional annotation available. Published literature includes studies on Rhox13's role in cellular processes. PubMed count of ~5 articles, indicating extremely high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 24179867 | Rhox in mammalian reproduction and development.... | Clinical and experimental reproductive m |
| 23926285 | Translational activation of developmental messenger RNAs during neonatal mouse t... | Biology of reproduction |
| 22190708 | Rhox13 is translated in premeiotic germ cells in male and female mice and is reg... | Biology of reproduction |
| 18675325 | Identification and characterization of Rhox13, a novel X-linked mouse homeobox g... | Gene |
| 27486269 | Rhox13 is required for a quantitatively normal first wave of spermatogenesis in ... | Reproduction (Cambridge, England) |


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
| STRING | 0 total interactions |
| IntAct | 0 interactions |
| UniProt Interactions | 0 curated |



**PPI Assessment**: STRING: No interactions found; IntAct: No interactions. Score 0/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Non-nuclear/Weak | Inconsistent/Weak |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Sparse / None | Sparse |

**Cross-Validation Bonus Details**:
- Insufficient cross-validation data
- **Total Cross-Validation Bonus**: +0.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (Score: 31.1/100)

**Core Strengths**:
2. High novelty (PubMed count < 20)

**Risks / Uncertainties**:
1. Nuclear localization score <= 3, automatic rejection criterion
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

**FINAL DECISION**: REJECTED. Rejected for: Nuclear≤3 (0/10).

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/N/A

- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22Rhox13%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/
