---
type: protein-evaluation
gene: "SKA3"
date: 2026-06-04
tags: [protein-scout, evaluation, rejected]
status: rejected
---

## SKA3 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SKA3 / C13orf3, RAMA1 |
| Protein Name | Spindle and kinetochore-associated protein 3 |
| Protein Size | 412 aa / 46.4 kDa |
| UniProt ID | Q8IX90 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 3/10 | x4 | **12** | HPA Uncertain; UniProt says Nucleus but HPA uncertain |
| Protein Size | 10/10 | x1 | **10** | 412 aa; ideal range |
| Research Novelty | 6/10 | x5 | **30** | 68 publications; moderate novelty (51-100) |
| 3D Structure | 8/10 | x3 | **24** | PDB (1 entries) + AlphaFold moderate (pLDDT=63.8) |
| Regulatory Domains | 7/10 | x2 | **14** | 1 annotated domain; novel protein baseline. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (3 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+1.0** | PDB + AlphaFold structural data agreement (+0.5) | IntAct + STRING overlap (2 shared partners) (+0.5) |
| **Raw Total** | | | **109.0/183** | |
| **Normalized Total** | | | **59.6/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm, cytoskeleton, spindle | Annotation |
| UniProt | Chromosome, centromere, kinetochore | ECO:0000269, ECO:0000269, ECO:0000269 |
| HPA | Mitotic spindle, Centrosome, Cytosol | Uncertain |

**Assessment**: HPA Uncertain; UniProt says Nucleus but HPA uncertain


**DECISION**: REJECTED. Nuclear localization score 3/10 (threshold: >3). HPA Uncertain; UniProt says Nucleus but HPA uncertain

### 4. Protein Size Assessment

412 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 68 |
| PubMed symbol-only count | 105 |
| PubMed broad count | 138 |
| Novelty category | 51-100 → 6 |

**Key Publications**:
1. Chen Y et al. (2023). "Hypoxia-induced SKA3 promoted cholangiocarcinoma progression and chemoresistance by enhancing fatty acid synthesis via the regulation of PAR-dependent HIF-1a deubiquitylation.". *Journal of experimental & clinical cancer research : CR*. PMID: 37821935
2. Sun Z et al. (2025). "SKA3-mediated hypoxia tolerance and metabolic reprogramming promote liver metastasis in lung adenocarcinoma.". *Cell death & disease*. PMID: 41298345
3. Xie L et al. (2022). "SKA3, negatively regulated by miR-128-3p, promotes the progression of non-small-cell lung cancer.". *Personalized medicine*. PMID: 34533066
4. Wang C et al. (2023). "Circular RNA circ_SKA3 enhances gastric cancer development by targeting miR-520h.". *Histology and histopathology*. PMID: 36134741
5. Wang C et al. (2022). "SKA3 is a prognostic biomarker and associated with immune infiltration in bladder cancer.". *Hereditas*. PMID: 35546682

**Assessment**: 68 publications; moderate novelty (51-100)


**Function Summary**: Component of the SKA1 complex, a microtubule-binding subcomplex of the outer kinetochore that is essential for proper chromosome segregation (PubMed:19289083, PubMed:19360002, PubMed:23085020). The SKA1 complex is a direct component of the kinetochore-microtubule interface and directly associates with microtubules as oligomeric assemblies (PubMed:19289083, PubMed:19360002). The complex facilitates the processive movement of microspheres along a microtubule in a depolymerization-coupled manner (PubMed:19289083). In the complex, it mediates the microtubule-stimulated oligomerization (PubMed:1928

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 63.8 |
| pLDDT > 90 (high confidence) | 24.3% |
| pLDDT 70-90 (moderate) | 11.9% |
| pLDDT 50-70 (low) | 23.5% |
| pLDDT < 50 (disordered) | 40.3% |
| Available PDB Entries | 1 |
| PDB Details |   - 4AJ5: X-ray, 3.32 A, chains 1/2/3/4/U/V/W/X/Y/Z=1-101 |

**Assessment**: PDB (1 entries) + AlphaFold moderate (pLDDT=63.8)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR033341 |  |

**Assessment**: 1 annotated domain; novel protein baseline.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| SKA1 | two hybrid array | 31515488 | physical association | — |
| NOL4 | validated two hybrid | 32296183 | physical association | — |
| ZDHHC17 | two hybrid array | 24705354 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| SKA1 | 0.999 | 0.985 | — |
| SKA2 | 0.999 | 0.980 | — |
| BUB1B | 0.976 | 0.171 | — |
| CENPF | 0.968 | 0.000 | — |
| SPDL1 | 0.947 | 0.099 | — |
| NDC80 | 0.943 | 0.000 | — |
| PLK1 | 0.934 | 0.292 | — |
| BOD1 | 0.933 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- centrosome (IDA:HPA)
- cytosol (IDA:HPA)
- kinetochore (IDA:UniProtKB)
- meiotic spindle (IEA:Ensembl)
- mitotic spindle (IDA:HPA)
- outer kinetochore (IDA:UniProtKB)
- SKA complex (IDA:UniProtKB)
- spindle microtubule (IDA:UniProtKB)

**PPI Assessment**: Physical interactions present (3 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Non-nuclear/ambiguous | Partial/No |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold structural data agreement (+0.5)
- IntAct + STRING overlap (2 shared partners) (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Normalized Score**: 59.6/100 (Raw: 109.0/183)

**Core Reasons for Rejection**:
Nuclear localization score 3/10 (threshold: >3). HPA Uncertain; UniProt says Nucleus but HPA uncertain

### 11. Decision

**FINAL DECISION**: REJECTED. Automatically rejected. Nuclear localization score 3/10 (threshold: >3). HPA Uncertain; UniProt says Nucleus but HPA uncertain

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8IX90
- HPA: https://www.proteinatlas.org/ENSG00000165480-SKA3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SKA3%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
