---
type: protein-evaluation
gene: "SKAP1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKAP1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SKAP1 / SCAP1, SKAP55 |
| Protein Name | Src kinase-associated phosphoprotein 1 |
| Protein Size | 359 aa / 41.4 kDa |
| UniProt ID | Q86WV1 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | HPA Approved + UniProt Nucleus; nuclear with additional locations |
| Protein Size | 10/10 | x1 | **10** | 359 aa; ideal range |
| Research Novelty | 8/10 | x5 | **40** | 43 publications; very novel (21-50) |
| 3D Structure | 8/10 | x3 | **24** | PDB (1 entries) + AlphaFold moderate (pLDDT=69.6) |
| Regulatory Domains | 8/10 | x2 | **16** | 8 annotated domains; some domain richness. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (4 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+1.5** | HPA + UniProt nuclear localization agreement (+0.5) | PDB + AlphaFold structural data agreement (+0.5) | IntAct + STRING overlap (3 shared partners) (+0.5) |
| **Raw Total** | | | **137.5/183** | |
| **Normalized Total** | | | **75.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269, ECO:0000269 |
| UniProt | Nucleus | ECO:0000269, ECO:0000269 |
| UniProt | Cell membrane | ECO:0000269, ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm, Plasma membrane, Cytosol | Approved |

**Assessment**: HPA Approved + UniProt Nucleus; nuclear with additional locations


### 4. Protein Size Assessment

359 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 43 |
| PubMed symbol-only count | 62 |
| PubMed broad count | 106 |
| Novelty category | 21-50 → 8 |

**Key Publications**:
1. Gao J et al. (2024). "SKAP1 Expression in Cancer Cells Enhances Colon Tumor Growth and Impairs Cytotoxic Immunity by Promoting Neutrophil Extracellular Trap Formation via the NFATc1/CXCL8 Axis.". *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39269257
2. Liu C et al. (2023). "Multi-functional adaptor SKAP1: regulator of integrin activation, the stop-signal, and the proliferation of T cells.". *Frontiers in immunology*. PMID: 37325633
3. Dadwal N et al. (2021). "The Multiple Roles of the Cytosolic Adapter Proteins ADAP, SKAP1 and SKAP2 for TCR/CD3 -Mediated Signaling Events.". *Frontiers in immunology*. PMID: 34295339
4. Gao M et al. (2025). "Integrative Analysis of TLS-Associated Gene Signatures, Immune Infiltration and Drug Sensitivity in Pancreatic Cancer.". *IET systems biology*. PMID: 41016829
5. Levillayer L et al. (2024). "Role of two modules controlling the interaction between SKAP1 and SRC kinases comparison with SKAP2 architecture and consequences for evolution.". *PloS one*. PMID: 38483858

**Assessment**: 43 publications; very novel (21-50)


**Function Summary**: Positively regulates T-cell receptor signaling by enhancing the MAP kinase pathway. Required for optimal conjugation between T-cells and antigen-presenting cells by promoting the clustering of integrin ITGAL on the surface of T-cells. May be involved in high affinity immunoglobulin epsilon receptor signaling in mast cells

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 69.6 |
| pLDDT > 90 (high confidence) | 27.6% |
| pLDDT 70-90 (moderate) | 31.5% |
| pLDDT 50-70 (low) | 10.6% |
| pLDDT < 50 (disordered) | 30.4% |
| Available PDB Entries | 1 |
| PDB Details |   - 1U5D: X-ray, 1.70 A, chains A/B/C/D=108-213 |

**Assessment**: PDB (1 entries) + AlphaFold moderate (pLDDT=69.6)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR011993 |  |
| InterPro | IPR001849 |  |
| InterPro | IPR036028 |  |
| InterPro | IPR001452 |  |
| InterPro | IPR035765 |  |
| InterPro | IPR037781 |  |
| Pfam | PF00169 |  |
| Pfam | PF14604 |  |

**Assessment**: 8 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| PRAM1 | two hybrid array | 31515488 | physical association | — |
| EEIG1 | two hybrid array | 31515488 | physical association | — |
| BLCAP | validated two hybrid | 25416956 | physical association | — |
| SH2D4A | validated two hybrid | 25416956 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| FYB1 | 0.998 | 0.803 | — |
| LCP2 | 0.987 | 0.074 | — |
| APBB1IP | 0.981 | 0.000 | — |
| FYN | 0.972 | 0.735 | — |
| LCK | 0.935 | 0.510 | — |
| RAP1A | 0.925 | 0.000 | — |
| RAP1B | 0.911 | 0.000 | — |
| GRB2 | 0.850 | 0.292 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cell-cell junction (IEA:Ensembl)
- cytoplasm (IDA:UniProtKB)
- cytosol (IDA:HPA)
- immunological synapse (IDA:BHF-UCL)
- nucleoplasm (IDA:HPA)
- plasma membrane (IDA:HPA)
- plasma membrane raft (IDA:BHF-UCL)
- T cell receptor complex (IEA:Ensembl)

**PPI Assessment**: Physical interactions present (4 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- PDB + AlphaFold structural data agreement (+0.5)
- IntAct + STRING overlap (3 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 75.1/100 (Raw: 137.5/183)

**Strengths**:
1. Strong nuclear localization (score 7/10)
1. Excellent research novelty (43 publications)
1. Good 3D structural quality (mean pLDDT 69.6)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 75.1/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q86WV1
- HPA: https://www.proteinatlas.org/ENSG00000141293-SKAP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SKAP1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
