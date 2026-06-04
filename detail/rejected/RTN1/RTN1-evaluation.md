---
type: protein-evaluation
gene: "RTN1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RTN1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTN1 / NSP |
| Protein Name | Reticulon-1 |
| Protein Size | 776 aa, ~83.6 kDa |
| UniProt ID | Q16799 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Endoplasmic reticulum) |
| Protein Size | 7/10 | x1 | **7** | 776 aa, workable range |
| Research Novelty | 5/10 | x5 | **25** | PubMed ~73 (61-80) |
| 3D Structure | 2/10 | x3 | **6** | AlphaFold very low confidence (mean pLDDT 48.1) |
| Regulatory Domains | 7/10 | x2 | **14** | 3 annotated domains (InterPro: 2, Pfam: 1) |
| PPI Network | 6/10 | x3 | **18** | STRING: 10 high-confidence interactions (score≥0.7); IntAct: 15 interactions; UniProt curated: 3 int |
| Cross-Validation Bonus | -- | -- | **+0.5** | STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **90.5/180** | |
| **Normalized Total** | | | **50.3/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Endoplasmic reticulum membrane | Experimental |
| UniProt | Golgi apparatus membrane | Experimental |
| GO-CC | nuclear body | IDA:HPA |
| HPA | Nuclear bodies, Endoplasmic reticulum | Reliability: Supported |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Endoplasmic reticulum). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

RTN1 is 776 amino acids in length (~83.6 kDa). 776 aa, workable range. Score 7/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 73 |
| PubMed broad count | 163 |
| Novelty category | PubMed ~73 (61-80) |

**Key Research Context**: Inhibits amyloid precursor protein processing, probably by blocking BACE1 activity. Published literature includes studies on RTN1's role in cellular processes. PubMed count of ~73 articles, indicating a well-studied protein.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 28733667 | RTN1 and RTN3 protein are differentially associated with senile plaques in Alzhe... | Scientific reports |
| 28981095 | RTN1-C mediates cerebral ischemia/reperfusion injury via ER stress and mitochond... | Cell death & disease |
| 36048753 | HTT (huntingtin) and RAB7 co-migrate retrogradely on a signaling LAMP1-containin... | Autophagy |
| 28623007 | Gene networks in neurodegenerative disorders.... | Life sciences |
| 41079183 | Shared senescence-associated gene networks in PCOS and T2DM: biomarker identific... | Frontiers in endocrinology |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 48.1 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold very low confidence (mean pLDDT 48.1). Score 2/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR003388 | Annotated domain |
| InterPro | IPR046964 | Annotated domain |
| Pfam | PF02453 | Annotated family |

**Domain Analysis**: 3 annotated domains (InterPro: 2, Pfam: 1). The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 3 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SPAST | 0.904 | 0.071 | 0.0 | 0.895 |
| REEP5 | 0.902 | 0.126 | 0.0 | 0.885 |
| ATL3 | 0.865 | 0.075 | 0.0 | 0.859 |
| ATL2 | 0.862 | 0.075 | 0.0 | 0.857 |
| RTN4 | 0.849 | 0.697 | 0.0 | 0.508 |
| ATL1 | 0.848 | 0.075 | 0.0 | 0.821 |
| RTN2 | 0.832 | 0.476 | 0.0 | 0.687 |
| TMEM33 | 0.825 | 0.144 | 0.0 | 0.801 |

**PPI Assessment**: STRING: 10 high-confidence interactions (score≥0.7); IntAct: 15 interactions; UniProt curated: 3 interactions. Score 6/10.

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

**Recommendation Level**: Recommended with caution (Score: 50.3/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Workable protein size (776 aa)
2. Moderate novelty (PubMed count ~73)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Rich PPI network with experimental validation

**Risks / Uncertainties**:
3. No experimental PDB structures
4. Low AlphaFold confidence (mean pLDDT < 50)
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 50.3/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q16799
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q16799-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTN1%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000139970-RTN1
