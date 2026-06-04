---
type: protein-evaluation
gene: "SGSM2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGSM2 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SGSM2 / KIAA0397, RUTBC1 |
| Protein Name | Small G protein signaling modulator 2 |
| Protein Size | 1006 aa / 113.3 kDa |
| UniProt ID | O43147 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 8/10 | x1 | **8** | 1006 aa; acceptable range |
| Research Novelty | 10/10 | x5 | **50** | 14 publications; extremely novel (≤20) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate quality (pLDDT=70.8); no PDB |
| Regulatory Domains | 8/10 | x2 | **16** | 10 annotated domains; some domain richness. |
| PPI Network | 8/10 | x3 | **24** | Physical interactions (IntAct) + 1 chromatin-regulatory partner(s); regulatory relevance |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **139/183** | |
| **Normalized Total** | | | **76.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Melanosome | ECO:0000269 |
| HPA | Nucleoplasm, Cytosol | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

1006 aa; acceptable range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 14 |
| PubMed symbol-only count | 17 |
| PubMed broad count | 19 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Su X et al. (2022). "SGSM2 inhibits thyroid cancer progression by activating RAP1 and enhancing competitive RAS inhibition.". *Cell death & disease*. PMID: 35264562
2. Liang D et al. (2024). "SGSM2 in Uveal Melanoma: Implications for Survival, Immune Infiltration, and Drug Sensitivity.". *Protein and peptide letters*. PMID: 39501960
3. Lin JH et al. (2019). "Small G protein signalling modulator 2 (SGSM2) is involved in oestrogen receptor-positive breast cancer metastasis through enhancement of migratory cell adhesion via interaction with E-cadherin.". *Cell adhesion & migration*. PMID: 30744493
4. Xiao J et al. (2024). "Clinical efficacy and gene chip expression analysis of Shenzhu Guanxin recipe granules in patients with intermediate coronary lesions.". *Journal of traditional Chinese medicine = Chung i tsa chih ying wen pan*. PMID: 38767639
5. Picolo BU et al. (2024). "Salivary proteomics profiling reveals potential biomarkers for chronic kidney disease: a pilot study.". *Frontiers in medicine*. PMID: 39895822

**Assessment**: 14 publications; extremely novel (≤20)


**Function Summary**: Possesses GTPase activator activity towards RAB32, RAB33B and RAB38 (PubMed:21808068, PubMed:26620560). Regulates the trafficking of melanogenic enzymes TYR, TYRP1 and DCT/TYRP2 to melanosomes in melanocytes by inactivating RAB32 and RAB38. Inhibits RAB32 and RAB38 activation both directly by promoting their GTPase activity and indirectly by disrupting the RAB9A-HPS4 interaction which is required for RAB32/38 activation (PubMed:26620560)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 70.8 |
| pLDDT > 90 (high confidence) | 38.9% |
| pLDDT 70-90 (moderate) | 24.1% |
| pLDDT 50-70 (low) | 6.6% |
| pLDDT < 50 (disordered) | 30.5% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold moderate quality (pLDDT=70.8); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR000195 |  |
| InterPro | IPR035969 |  |
| InterPro | IPR004012 |  |
| InterPro | IPR037213 |  |
| InterPro | IPR047345 |  |
| InterPro | IPR037745 |  |
| InterPro | IPR021935 |  |
| Pfam | PF12068 |  |
| Pfam | PF00566 |  |
| Pfam | PF02759 |  |

**Assessment**: 10 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| PTN | two hybrid pooling approach | 16169070 | physical association | — |
| PNO1 | two hybrid pooling approach | 16169070 | physical association | — |
| MPP1 | two hybrid pooling approach | 16169070 | physical association | — |
| FNBP1L | two hybrid pooling approach | 16169070 | physical association | — |
| CA12 | two hybrid pooling approach | 16169070 | physical association | — |
| CHD3 | two hybrid pooling approach | 16169070 | physical association | Yes |
| EGFR | two hybrid pooling approach | 16169070 | physical association | — |
| GDPD2 | two hybrid pooling approach | 16169070 | physical association | — |
| ... (6 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| SGSM3 | 0.909 | 0.000 | — |
| RAB9A | 0.836 | 0.491 | — |
| RAP1B | 0.763 | 0.000 | — |
| RAB4A | 0.758 | 0.000 | — |
| RAB3A | 0.750 | 0.230 | — |
| RAP2A | 0.716 | 0.000 | — |
| RAB11A | 0.696 | 0.000 | — |
| RAB8A | 0.675 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IDA:UniProtKB)
- melanosome (IDA:UniProtKB)

**PPI Assessment**: Physical interactions (IntAct) + 1 chromatin-regulatory partner(s); regulatory relevance

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- No bonus criteria met across databases.
- **Total Cross-Validation Bonus**: +0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 76.0/100 (Raw: 139/183)

**Strengths**:
1. Excellent research novelty (14 publications)
1. Good 3D structural quality (mean pLDDT 70.8)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 76.0/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O43147
- HPA: https://www.proteinatlas.org/ENSG00000141258-SGSM2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SGSM2%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
