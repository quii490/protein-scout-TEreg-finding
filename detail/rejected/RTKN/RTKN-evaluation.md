---
type: protein-evaluation
gene: "RTKN"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RTKN -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTKN / RTKN1 |
| Protein Name | Rhotekin |
| Protein Size | 563 aa, ~62.7 kDa |
| UniProt ID | Q9BST9 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Mitochondria) |
| Protein Size | 10/10 | x1 | **10** | 563 aa, ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~25 (21-40) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold moderate confidence (mean pLDDT 72.0) |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains (InterPro: 5, Pfam: 2) |
| PPI Network | 6/10 | x3 | **18** | STRING: 10 high-confidence interactions (score≥0.7); IntAct: 15 interactions; UniProt curated: 10 in |
| Cross-Validation Bonus | -- | -- | **+1.0** | Domain (7) + AlphaFold (pLDDT 72) consistency (+0.5); STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **115.0/180** | |
| **Normalized Total** | | | **63.9/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA | Nucleoplasm, Mitochondria | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Mitochondria). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

RTKN is 563 amino acids in length (~62.7 kDa). 563 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 25 |
| PubMed broad count | 77 |
| Novelty category | PubMed ~25 (21-40) |

**Key Research Context**: Mediates Rho signaling to activate NF-kappa-B and may confer increased resistance to apoptosis to cells in gastric tumorigenesis. May play a novel role in the organization of septin structures. Published literature includes studies on RTKN's role in cellular processes. PubMed count of ~25 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 38150455 | Rhotekin regulates axon regeneration through the talin-Vinculin-Vinexin axis in ... | PLoS genetics |
| 40025790 | Rhotekin-1 is a novel interacting protein and regulator of TRPC6 activity.... | The FEBS journal |
| 15316142 | Overexpression of rho effector rhotekin confers increased survival in gastric ad... | Journal of biomedical science |
| 33844824 | RTKN-1/Rhotekin shields endosome-associated F-actin from disassembly to ensure e... | The Journal of cell biology |
| 26935528 | Inhibition of rhotekin exhibits antitumor effects in lung cancer cells.... | Oncology reports |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 72.0 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate confidence (mean pLDDT 72.0). Score 5/10.

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
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 10 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RHOA | 0.999 | 0.909 | 0.8 | 0.998 |
| SLCO6A1 | 0.986 | 0.000 | 0.0 | 0.986 |
| LIN7B | 0.963 | 0.000 | 0.8 | 0.823 |
| RHOC | 0.952 | 0.368 | 0.5 | 0.857 |
| RHOB | 0.900 | 0.367 | 0.5 | 0.706 |
| CDC42 | 0.894 | 0.000 | 0.0 | 0.894 |
| RHPN1 | 0.877 | 0.000 | 0.0 | 0.874 |
| PKN1 | 0.872 | 0.000 | 0.4 | 0.796 |

**PPI Assessment**: STRING: 10 high-confidence interactions (score≥0.7); IntAct: 15 interactions; UniProt curated: 10 interactions. Score 6/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Domain (7) + AlphaFold (pLDDT 72) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 63.9/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~25)
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

**FINAL DECISION**: NOT REJECTED. The protein scores 63.9/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BST9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9BST9-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTKN%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000114993-RTKN
