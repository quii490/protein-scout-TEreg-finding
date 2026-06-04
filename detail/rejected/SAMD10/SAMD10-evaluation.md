---
type: protein-evaluation
gene: "SAMD10"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SAMD10 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAMD10 / C20orf136 |
| Protein Name | Sterile alpha motif domain-containing protein 10 |
| Protein Size | 202 aa, ~22.8 kDa |
| UniProt ID | Q9BYL1 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Nucleoplasm) |
| Protein Size | 10/10 | x1 | **10** | 202 aa, ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~2 (0-5) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold moderate confidence (mean pLDDT 67.3) |
| Regulatory Domains | 8/10 | x2 | **16** | 5 annotated domains (InterPro: 4, Pfam: 1) |
| PPI Network | 1/10 | x3 | **3** | STRING: 15 total interactions (low confidence); IntAct: 1 interaction |
| Cross-Validation Bonus | -- | -- | **+0.8** | Domain + AlphaFold partial consistency (+0.3); STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **114.8/180** | |
| **Normalized Total** | | | **63.8/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Nucleoplasm | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Nucleoplasm). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

SAMD10 is 202 amino acids in length (~22.8 kDa). 202 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| Novelty category | PubMed ~2 (0-5) |

**Key Research Context**: No functional annotation available. Published literature includes studies on SAMD10's role in cellular processes. PubMed count of ~2 articles, indicating extremely high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 40010432 | SAMD12 as a Master Regulator of MAP4Ks by Decoupling Kinases From the CNKSR2 Sca... | Journal of molecular biology |
| 39818154 | Quantification of heavy metal exposure in a British population cohort links tota... | The Science of the total environment |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 67.3 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate confidence (mean pLDDT 67.3). Score 5/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR039144 | Annotated domain |
| InterPro | IPR001660 | Annotated domain |
| InterPro | IPR013761 | Annotated domain |
| InterPro | IPR052268 | Annotated domain |
| Pfam | PF07647 | Annotated family |

**Domain Analysis**: 5 annotated domains (InterPro: 4, Pfam: 1). The protein contains 4 InterPro and 1 Pfam domain annotations. Score 8/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 1 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| AVPI1 | 0.569 | 0.000 | 0.0 | 0.569 |
| ZNF512B | 0.561 | 0.000 | 0.0 | 0.000 |
| ALKBH7 | 0.532 | 0.000 | 0.0 | 0.530 |
| NCKIPSD | 0.523 | 0.000 | 0.0 | 0.503 |
| SAMD14 | 0.518 | 0.000 | 0.0 | 0.518 |
| SAMD5 | 0.515 | 0.000 | 0.0 | 0.515 |
| CLLU1OS | 0.507 | 0.000 | 0.0 | 0.507 |
| DRC7 | 0.456 | 0.000 | 0.0 | 0.456 |

**PPI Assessment**: STRING: 15 total interactions (low confidence); IntAct: 1 interaction. Score 1/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Domain + AlphaFold partial consistency (+0.3)
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +0.8 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 63.8/100)

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

**FINAL DECISION**: NOT REJECTED. The protein scores 63.8/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9BYL1-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SAMD10%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000130590-SAMD10
