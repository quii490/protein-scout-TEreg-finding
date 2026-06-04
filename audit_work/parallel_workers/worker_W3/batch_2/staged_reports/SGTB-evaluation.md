---
type: protein-evaluation
gene: "SGTB"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGTB -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SGTB / SGT2 |
| Protein Name | Small glutamine-rich tetratricopeptide repeat-containing protein beta |
| Protein Size | 304 aa / 33.4 kDa |
| UniProt ID | Q96EQ0 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA Approved nuclear; UniProt lacks nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 304 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 20 publications; extremely novel (≤20) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold high quality (pLDDT=81.0); no PDB |
| Regulatory Domains | 8/10 | x2 | **16** | 7 annotated domains; some domain richness. |
| PPI Network | 8/10 | x3 | **24** | Physical interactions (IntAct) + 1 chromatin-regulatory partner(s); regulatory relevance |
| Cross-Validation Bonus | — | max +3 | **+0.5** | IntAct + STRING overlap (2 shared partners) (+0.5) |
| **Raw Total** | | | **144.5/183** | |
| **Normalized Total** | | | **79.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| HPA | Nucleoplasm, Nuclear speckles, Microtubules, Primary cilium, Basal body | Approved |

**Assessment**: HPA Approved nuclear; UniProt lacks nuclear annotation


### 4. Protein Size Assessment

304 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 20 |
| PubMed symbol-only count | 56 |
| PubMed broad count | 124 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Vuong TA et al. (2019). "SGTb regulates a surface localization of a guidance receptor BOC to promote neurite outgrowth.". *Cellular signalling*. PMID: 30639199
2. Sun N et al. (2023). "Sevoflurane suppresses hepatocellular carcinoma cell progression via circ_0001649/miR-19a-3p/SGTB axis.". *Histology and histopathology*. PMID: 35747942
3. Yang S et al. (2023). "Circ_0102543 suppresses hepatocellular carcinoma progression through the miR-942-5p/SGTB axis.". *Annals of gastroenterological surgery*. PMID: 37416745
4. Wang B et al. (2021). "LncRNA HOTAIR modulates chondrocyte apoptosis and inflammation in osteoarthritis via regulating miR-1277-5p/SGTB axis.". *Wound repair and regeneration : official publication of the Wound Healing Society [and] the European Tissue Repair Society*. PMID: 33721916
5. Lockhart SM et al. (2025). "Rare Variants in HTRA1, SGTB, and RBM12 Confer Risk of Atherosclerotic Cardiovascular Disease Independent of Traditional Cardiovascular Risk Factors.". *Circulation. Genomic and precision medicine*. PMID: 41190437

**Assessment**: 20 publications; extremely novel (≤20)


**Function Summary**: Co-chaperone that binds directly to HSC70 and HSP70 and regulates their ATPase activity

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 81.0 |
| pLDDT > 90 (high confidence) | 50.3% |
| pLDDT 70-90 (moderate) | 25.0% |
| pLDDT 50-70 (low) | 12.2% |
| pLDDT < 50 (disordered) | 12.5% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold high quality (pLDDT=81.0); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR047150 |  |
| InterPro | IPR032374 |  |
| InterPro | IPR011990 |  |
| InterPro | IPR019734 |  |
| Pfam | PF16546 |  |
| Pfam | PF00515 |  |
| Pfam | PF13414 |  |

**Assessment**: 7 annotated domains; some domain richness.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| EFEMP2 | two hybrid pooling approach | 16189514 | physical association | — |
| RAI2 | two hybrid pooling approach | 16189514 | physical association | — |
| LAMP3 | two hybrid array | 21988832 | physical association | — |
| SMCHD1 | cross-linking study | 30021884 | physical association | Yes |
| IL6ST | two hybrid array | 29892012 | physical association | — |
| NME3 | two hybrid array | 32296183 | physical association | — |
| ADIPOQ | two hybrid prey pooling approach | 32296183 | physical association | — |
| TXNDC12 | two hybrid prey pooling approach | 32296183 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| GET4 | 0.899 | 0.542 | — |
| UBL4A | 0.791 | 0.225 | — |
| GET3 | 0.748 | 0.402 | — |
| BAG6 | 0.681 | 0.183 | — |
| RAI2 | 0.614 | 0.614 | — |
| SGTA | 0.613 | 0.142 | — |
| DNAJA1 | 0.590 | 0.164 | — |
| PLXNB1 | 0.590 | 0.189 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- membrane (IBA:GO_Central)
- TRC complex (IBA:GO_Central)

**PPI Assessment**: Physical interactions (IntAct) + 1 chromatin-regulatory partner(s); regulatory relevance

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear + other | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- IntAct + STRING overlap (2 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 79.0/100 (Raw: 144.5/183)

**Strengths**:
1. Excellent research novelty (20 publications)
1. Good 3D structural quality (mean pLDDT 81.0)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. Sub-optimal nuclear localization (score 5/10)


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 79.0/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96EQ0
- HPA: https://www.proteinatlas.org/ENSG00000197860-SGTB
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SGTB%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
