---
type: protein-evaluation
gene: "SHLD3"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHLD3 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHLD3 / FLJ26957, RINN1 |
| Protein Name | Shieldin complex subunit 3 |
| Protein Size | 250 aa / 28.8 kDa |
| UniProt ID | Q6ZNX1 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Approved + UniProt Nucleus; nuclear focused |
| Protein Size | 10/10 | x1 | **10** | 250 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 14 publications; extremely novel (≤20) |
| 3D Structure | 9/10 | x3 | **27** | PDB (9 entries) + AlphaFold good quality (pLDDT=78.5) |
| Regulatory Domains | 9/10 | x2 | **18** | 1 domains; chromatin/DNA-related function. Moderate regulatory potential. |
| PPI Network | 5/10 | x3 | **15** | No IntAct; STRING experimental + 2 chromatin-regulatory partner(s) |
| Cross-Validation Bonus | — | max +3 | **+1.0** | HPA + UniProt nuclear localization agreement (+0.5) | PDB + AlphaFold structural data agreement (+0.5) |
| **Raw Total** | | | **157.0/183** | |
| **Normalized Total** | | | **85.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Chromosome | ECO:0000269 |
| GO-CC | chromatin | NAS:ComplexPortal |
| GO-CC | chromosome | IDA:UniProtKB |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm, Nucleoli | Approved |

**Assessment**: HPA Approved + UniProt Nucleus; nuclear focused


### 4. Protein Size Assessment

250 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 14 |
| PubMed symbol-only count | 18 |
| PubMed broad count | 18 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Noordermeer SM et al. (2018). "The shieldin complex mediates 53BP1-dependent DNA repair.". *Nature*. PMID: 30022168
2. Pernicone N et al. (2020). "CDH1 binds MAD2L2 in a Rev1-like pattern.". *Biochemical and biophysical research communications*. PMID: 32811646
3. de Krijger I et al. (2021). "MAD2L2 dimerization and TRIP13 control shieldin activity in DNA repair.". *Nature communications*. PMID: 34521823
4. Mirman Z et al. (2018). "53BP1-RIF1-shieldin counteracts DSB resection through CST- and Polα-dependent fill-in.". *Nature*. PMID: 30022158
5. Li F et al. (2022). "CHAMP1 binds to REV7/FANCV and promotes homologous recombination repair.". *Cell reports*. PMID: 36044844

**Assessment**: 14 publications; extremely novel (≤20)


**Function Summary**: Component of the shieldin complex, which plays an important role in repair of DNA double-stranded breaks (DSBs). During G1 and S phase of the cell cycle, the complex functions downstream of TP53BP1 to promote non-homologous end joining (NHEJ) and suppress DNA end resection. Mediates various NHEJ-dependent processes including immunoglobulin class-switch recombination, and fusion of unprotected telomeres

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 78.5 |
| pLDDT > 90 (high confidence) | 45.6% |
| pLDDT 70-90 (moderate) | 27.2% |
| pLDDT 50-70 (low) | 14.4% |
| pLDDT < 50 (disordered) | 12.8% |
| Available PDB Entries | 9 |
| PDB Details |   - 6K07: X-ray, 2.24 A, chains B=46-74
  - 6K08: X-ray, 2.31 A, chains B=46-74
  - 6KTO: X-ray, 3.45 A, chains C=1-64
  - 6M7A: X-ray, 1.90 A, chains C/D=28-73
  - 6M7B: X-ray, 1.77 A, chains C/D=37-73 |

**Assessment**: PDB (9 entries) + AlphaFold good quality (pLDDT=78.5)

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR039996 |  |

**Assessment**: 1 domains; chromatin/DNA-related function. Moderate regulatory potential.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| — | — | — | — | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| SHLD2 | 0.999 | 0.900 | — |
| MAD2L2 | 0.998 | 0.939 | Yes |
| SHLD1 | 0.994 | 0.000 | — |
| TRIP13 | 0.917 | 0.900 | — |
| TP53BP1 | 0.710 | 0.439 | Yes |
| C20orf96 | 0.648 | 0.000 | — |
| KIZ | 0.558 | 0.000 | — |
| TRAPPC13 | 0.536 | 0.000 | — |
| ... (4 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- chromatin (NAS:ComplexPortal)
- chromosome (IDA:UniProtKB)
- nucleolus (IDA:HPA)
- nucleoplasm (IDA:HPA)
- site of double-strand break (IDA:UniProtKB)

**PPI Assessment**: No IntAct; STRING experimental + 2 chromatin-regulatory partner(s)

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | Experimental structure available | Consistent |
| PPI | IntAct + STRING | 0 IntAct, 12 STRING | Single/No source |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- PDB + AlphaFold structural data agreement (+0.5)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 85.8/100 (Raw: 157.0/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Excellent research novelty (14 publications)
1. Good 3D structural quality (mean pLDDT 78.5)

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 85.8/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZNX1
- HPA: https://www.proteinatlas.org/ENSG00000253251-SHLD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHLD3%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
