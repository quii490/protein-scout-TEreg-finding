---
type: protein-evaluation
gene: "SHLD2"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHLD2 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHLD2 / FAM35A, RINN2 |
| Protein Name | Shieldin complex subunit 2 |
| Protein Size | 835 aa / 93.7 kDa |
| UniProt ID | Q86V20 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Supported + UniProt Nucleus; primarily nuclear |
| Protein Size | 8/10 | x1 | **8** | 835 aa; acceptable range |
| Research Novelty | 10/10 | x5 | **50** | 10 publications; extremely novel (≤20) |
| 3D Structure | 8/10 | x3 | **24** | PDB (3 entries) + AlphaFold moderate (pLDDT=55.8) |
| Regulatory Domains | 10/10 | x2 | **20** | 7 domains; chromatin/DNA-related function. Direct regulatory potential. |
| PPI Network | 10/10 | x3 | **30** | Physical interactions (IntAct) + 3 chromatin-regulatory partners; high regulatory relevance |
| Cross-Validation Bonus | — | max +3 | **+1.0** | HPA + UniProt nuclear localization agreement (+0.5) | PDB + AlphaFold structural data agreement (+0.5) |
| **Raw Total** | | | **169.0/183** | |
| **Normalized Total** | | | **92.3/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Nucleus | ECO:0000269, ECO:0000269 |
| UniProt | Chromosome | ECO:0000269, ECO:0000305 |
| GO-CC | chromatin | NAS:ComplexPortal |
| GO-CC | chromosome | IDA:UniProtKB |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm, Actin filaments | Supported |

**Assessment**: HPA Supported + UniProt Nucleus; primarily nuclear


### 4. Protein Size Assessment

835 aa; acceptable range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 10 |
| PubMed symbol-only count | 21 |
| PubMed broad count | 26 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Noordermeer SM et al. (2018). "The shieldin complex mediates 53BP1-dependent DNA repair.". *Nature*. PMID: 30022168
2. Pernicone N et al. (2020). "CDH1 binds MAD2L2 in a Rev1-like pattern.". *Biochemical and biophysical research communications*. PMID: 32811646
3. Mirman Z et al. (2018). "53BP1-RIF1-shieldin counteracts DSB resection through CST- and Polα-dependent fill-in.". *Nature*. PMID: 30022158
4. Fackrell K et al. (2020). "FAM35A/SHLD2/RINN2: A novel determinant of double strand break repair pathway choice and genome stability in cancer.". *Environmental and molecular mutagenesis*. PMID: 32306447
5. Lescale C et al. (2025). "CST Is Epistatic With Shieldin to Limit DNA Double-Strand Break End Resection and Promote Repair During Igh Class Switch Recombination.". *European journal of immunology*. PMID: 40178294

**Assessment**: 10 publications; extremely novel (≤20)


**Function Summary**: Component of the shieldin complex, which plays an important role in repair of DNA double-stranded breaks (DSBs) (PubMed:29656893, PubMed:29789392). During G1 and S phase of the cell cycle, the complex functions downstream of TP53BP1 to promote non-homologous end joining (NHEJ) and suppress DNA end resection (PubMed:29656893, PubMed:29789392). Mediates various NHEJ-dependent processes including immunoglobulin class-switch recombination, and fusion of unprotected telomeres (PubMed:29656893)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 55.8 |
| pLDDT > 90 (high confidence) | 15.1% |
| pLDDT 70-90 (moderate) | 23.5% |
| pLDDT 50-70 (low) | 12.6% |
| pLDDT < 50 (disordered) | 48.9% |
| Available PDB Entries | 3 |
| PDB Details |   - 6KTO: X-ray, 3.45 A, chains D=1-52
  - 6WWA: X-ray, 3.80 A, chains X/Y=5-19
  - 7L9P: EM, 3.60 A, chains X/Y=5-19 |

**Assessment**: PDB (3 entries) + AlphaFold moderate (pLDDT=55.8)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR029715 |  |
| InterPro | IPR031589 |  |
| InterPro | IPR049507 |  |
| InterPro | IPR053944 |  |
| Pfam | PF22779 |  |
| Pfam | PF15793 |  |
| Pfam | PF21669 |  |

**Assessment**: 7 domains; chromatin/DNA-related function. Direct regulatory potential.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| alaS | two hybrid pooling approach | 20711500 | physical association | — |
| Mad2l2 | tandem affinity purification | 20360068 | physical association | Yes |
| H2BC5 | cross-linking study | 30021884 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| SHLD3 | 0.999 | 0.900 | — |
| MAD2L2 | 0.999 | 0.973 | Yes |
| SHLD1 | 0.998 | 0.301 | — |
| TP53BP1 | 0.824 | 0.292 | Yes |
| REV3L | 0.720 | 0.000 | — |
| C20orf96 | 0.691 | 0.000 | — |
| CTC1 | 0.661 | 0.000 | — |
| RIF1 | 0.616 | 0.292 | Yes |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- actin cytoskeleton (IDA:HPA)
- chromatin (NAS:ComplexPortal)
- chromosome (IDA:UniProtKB)
- nucleoplasm (IDA:HPA)
- nucleus (IDA:UniProtKB)
- site of double-strand break (IDA:UniProtKB)

**PPI Assessment**: Physical interactions (IntAct) + 3 chromatin-regulatory partners; high regulatory relevance

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 4 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- PDB + AlphaFold structural data agreement (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 92.3/100 (Raw: 169.0/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Excellent research novelty (10 publications)
1. Good 3D structural quality (mean pLDDT 55.8)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 92.3/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q86V20
- HPA: https://www.proteinatlas.org/ENSG00000122376-SHLD2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHLD2%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
