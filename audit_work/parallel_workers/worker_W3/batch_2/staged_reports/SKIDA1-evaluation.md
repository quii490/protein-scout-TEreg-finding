---
type: protein-evaluation
gene: "SKIDA1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKIDA1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SKIDA1 / C10orf140, DLN1 |
| Protein Name | SKI/DACH domain-containing protein 1 |
| Protein Size | 908 aa / 98.1 kDa |
| UniProt ID | Q1XH10 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 8/10 | x1 | **8** | 908 aa; acceptable range |
| Research Novelty | 10/10 | x5 | **50** | 5 publications; extremely novel (≤20) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold poor (pLDDT=49.4); mostly disordered |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains; some domain richness. |
| PPI Network | 5/10 | x3 | **15** | No IntAct; STRING experimental + 3 chromatin-regulatory partner(s) |
| Cross-Validation Bonus | — | max +3 | **+0.5** | IntAct + STRING overlap (5 shared partners) (+0.5) |
| **Raw Total** | | | **121.5/183** | |
| **Normalized Total** | | | **66.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| HPA | Nucleoplasm, Nuclear bodies, Cytosol | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

908 aa; acceptable range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 5 |
| PubMed symbol-only count | 7 |
| PubMed broad count | 7 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Lopes BA et al. (2022). "Novel Diagnostic and Therapeutic Options for KMT2A-Rearranged Acute Leukemias.". *Frontiers in pharmacology*. PMID: 35734412
2. Mendoza-Castrejon J et al. (2026). "SKIDA1 sustains MLL::ENL-expressing hematopoietic progenitors during neonatal stages and promotes B-lineage priming.". *Blood neoplasia*. PMID: 41574310
3. Tamai M et al. (2025). "A characteristic gene expression profile regulated by ACIN1::NUTM1 fusion in a newly identified infant leukaemic cell line and an ACIN1::NUTM1-inducible model.". *British journal of haematology*. PMID: 40884014
4. Berger AH et al. (2021). "Transcriptional Changes in Regulatory T Cells From Patients With Autoimmune Polyendocrine Syndrome Type 1 Suggest Functional Impairment of Lipid Metabolism and Gut Homing.". *Frontiers in immunology*. PMID: 34526996
5. Pyrkova A et al. (2026). "Regulatory Potential of piRNAs Targeting Klotho and Other Genes.". *Genes*. PMID: 41751625

**Assessment**: 5 publications; extremely novel (≤20)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 49.4 |
| pLDDT > 90 (high confidence) | 9.8% |
| pLDDT 70-90 (moderate) | 3.1% |
| pLDDT 50-70 (low) | 14.8% |
| pLDDT < 50 (disordered) | 72.4% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold poor (pLDDT=49.4); mostly disordered

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR009061 |  |
| InterPro | IPR052119 |  |
| InterPro | IPR027971 |  |
| InterPro | IPR003380 |  |
| InterPro | IPR037000 |  |
| Pfam | PF15223 |  |
| Pfam | PF02437 |  |

**Assessment**: 7 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| — | — | — | — | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| MTF2 | 0.764 | 0.614 | Yes |
| PHF19 | 0.735 | 0.612 | Yes |
| EZH2 | 0.700 | 0.620 | Yes |
| SUZ12 | 0.698 | 0.623 | Yes |
| EED | 0.655 | 0.610 | Yes |
| MYSM1 | 0.588 | 0.507 | Yes |
| SMARCB1 | 0.541 | 0.465 | Yes |
| PBRM1 | 0.511 | 0.458 | Yes |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- No complex annotations available

**PPI Assessment**: No IntAct; STRING experimental + 3 chromatin-regulatory partner(s)

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 9 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- IntAct + STRING overlap (5 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 66.4/100 (Raw: 121.5/183)

**Strengths**:
1. Excellent research novelty (5 publications)

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 66.4/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q1XH10
- HPA: https://www.proteinatlas.org/ENSG00000180592-SKIDA1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SKIDA1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
