---
type: protein-evaluation
gene: "RTKN2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RTKN2 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTKN2 / PLEKHK1 |
| Protein Name | Rhotekin-2 |
| Protein Size | 609 aa, ~69.3 kDa |
| UniProt ID | Q8IZC4 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Nucleoplasm) |
| Protein Size | 8/10 | x1 | **8** | 609 aa, acceptable range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~29 (21-40) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold moderate confidence (mean pLDDT 69.9) |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains (InterPro: 5, Pfam: 2) |
| PPI Network | 3/10 | x3 | **9** | STRING: 4 total interactions (low confidence); IntAct: 6 interactions |
| Cross-Validation Bonus | -- | -- | **+0.8** | Domain + AlphaFold partial consistency (+0.3); STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **103.8/180** | |
| **Normalized Total** | | | **57.7/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm, Mitochondria | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Nucleoplasm). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

RTKN2 is 609 amino acids in length (~69.3 kDa). 609 aa, acceptable range. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 29 |
| PubMed broad count | 45 |
| Novelty category | PubMed ~29 (21-40) |

**Key Research Context**: May play an important role in lymphopoiesis. Published literature includes studies on RTKN2's role in cellular processes. PubMed count of ~29 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 38805063 | CircZFR promotes colorectal cancer progression via stabilizing BCLAF1 and regula... | Science China. Life sciences |
| 36628881 | Immune infiltration patterns and identification of new diagnostic biomarkers GDF... | Translational oncology |
| 38536923 | Lupus susceptibility gene Pbx1 controls the development, stability, and function... | Science advances |
| 37421213 | Depletion of circ_0088046 suppressed cell growth and motility of hepatocellular ... | Journal of viral hepatitis |
| 27082503 | Silencing of RTKN2 by siRNA suppresses proliferation, and induces G1 arrest and ... | Molecular medicine reports |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 69.9 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate confidence (mean pLDDT 69.9). Score 5/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR012966 | Annotated domain |
| InterPro | IPR051364 | Annotated domain |
| InterPro | IPR011072 | Annotated domain |
| InterPro | IPR011993 | Annotated domain |
| InterPro | IPR001849 | Annotated domain |
| Pfam | PF08174 | Annotated family |
| Pfam | PF00169 | Annotated family |

**Domain Analysis**: 7 annotated domains (InterPro: 5, Pfam: 2). The protein contains 5 InterPro and 2 Pfam domain annotations. Score 8/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 4 total interactions |
| IntAct | 6 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RHOC | 0.563 | 0.511 | 0.0 | 0.143 |
| RHOA | 0.556 | 0.189 | 0.0 | 0.475 |
| ARID5B | 0.520 | 0.000 | 0.0 | 0.520 |
| SH3KBP1 | 0.409 | 0.409 | 0.0 | 0.000 |

**PPI Assessment**: STRING: 4 total interactions (low confidence); IntAct: 6 interactions. Score 3/10.

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

**Recommendation Level**: Recommended with caution (Score: 57.7/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~29)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Moderate PPI data available

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

**FINAL DECISION**: NOT REJECTED. The protein scores 57.7/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q8IZC4-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTKN2%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000182010-RTKN2
