---
type: protein-evaluation
gene: "SHFL"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHFL -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHFL / C19orf66, FLJ11286, IRAV, RYDEN, SFL |
| Protein Name | Shiftless antiviral inhibitor of ribosomal frameshifting protein |
| Protein Size | 291 aa / 33.1 kDa |
| UniProt ID | Q9NUL5 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Supported + UniProt Nucleus; primarily nuclear |
| Protein Size | 10/10 | x1 | **10** | 291 aa; ideal range |
| Research Novelty | 10/10 | x5 | **50** | 17 publications; extremely novel (≤20) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold high quality (pLDDT=88.1); no PDB |
| Regulatory Domains | 9/10 | x2 | **18** | 2 domains; chromatin/DNA-related function. Moderate regulatory potential. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (15 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0.5** | HPA + UniProt nuclear localization agreement (+0.5) |
| **Raw Total** | | | **156.5/183** | |
| **Normalized Total** | | | **85.5/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269, ECO:0000269 |
| UniProt | Nucleus | ECO:0000269 |
| UniProt | Cytoplasm, P-body | ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm, Cytosol | Supported |

**Assessment**: HPA Supported + UniProt Nucleus; primarily nuclear


### 4. Protein Size Assessment

291 aa; ideal range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 17 |
| PubMed symbol-only count | 25 |
| PubMed broad count | 34 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Wang X et al. (2023). "Functional features of a novel interferon-stimulated gene SHFL: a comprehensive review.". *Frontiers in microbiology*. PMID: 38149274
2. Hatfield D et al. (2023). "The antiviral protein Shiftless blocks p-body formation during KSHV infection.". *bioRxiv : the preprint server for biology*. PMID: 38014318
3. Suzuki Y et al. (2022). "Restriction of Flaviviruses by an Interferon-Stimulated Gene SHFL/C19orf66.". *International journal of molecular sciences*. PMID: 36293480
4. Rodriguez W et al. (2022). "Shiftless, a Critical Piece of the Innate Immune Response to Viral Infection.". *Viruses*. PMID: 35746809
5. Zhang Y et al. (2023). "Mouse Liver-Expressed Shiftless Is an Evolutionarily Conserved Antiviral Effector Restricting Human and Murine Hepaciviruses.". *Microbiology spectrum*. PMID: 37341610

**Assessment**: 17 publications; extremely novel (≤20)


**Function Summary**: Inhibits programmed -1 ribosomal frameshifting (-1PRF) of a variety of mRNAs from viruses, such as HIV1, and cellular genes, such as PEG10. Interacts with the -1PRF signal of target mRNA and translating ribosomes and causes premature translation termination at the frameshifting site (PubMed:30682371). Regulates HIV1 GAG-POL expression by inhibiting -1PRF (PubMed:30682371). Exhibits antiviral activity against dengue virus (DENV) and can inhibit the replication of all DENV serotypes. May block the protein translation of DENV RNA via its association with cellular mRNA-binding proteins and viral R

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 88.1 |
| pLDDT > 90 (high confidence) | 59.1% |
| pLDDT 70-90 (moderate) | 32.6% |
| pLDDT 50-70 (low) | 6.5% |
| pLDDT < 50 (disordered) | 1.7% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold high quality (pLDDT=88.1); no PDB

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR026795 |  |
| Pfam | PF15135 |  |

**Assessment**: 2 domains; chromatin/DNA-related function. Moderate regulatory potential.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| ENSP00000467182.1 | validated two hybrid | 32296183 | physical association | — |
| ENSP00000253110.10 | two hybrid array | 25416956 | physical association | — |
| OCIAD2 | cross-linking study | 30021884 | physical association | — |
| KRTAP10-9 | two hybrid array | 32296183 | physical association | — |
| ADAMTSL4 | two hybrid array | 32296183 | physical association | — |
| KRTAP4-12 | two hybrid array | 32296183 | physical association | — |
| LNX1 | two hybrid array | 32296183 | physical association | — |
| MEOX2 | two hybrid array | 32296183 | physical association | — |
| ... (7 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| MOV10 | 0.705 | 0.000 | — |
| IFI6 | 0.607 | 0.000 | — |
| OAS2 | 0.586 | 0.000 | — |
| ISG15 | 0.579 | 0.000 | — |
| UBE2L6 | 0.568 | 0.000 | — |
| HERC6 | 0.566 | 0.000 | — |
| IFI35 | 0.564 | 0.000 | — |
| IRF7 | 0.547 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- cytoplasm (IDA:UniProtKB)
- cytosol (IDA:HPA)
- nucleoplasm (IDA:HPA)
- nucleus (IDA:UniProtKB)
- P-body (IDA:UniProtKB)

**PPI Assessment**: Physical interactions present (15 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 15 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 85.5/100 (Raw: 156.5/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Excellent research novelty (17 publications)
1. Good 3D structural quality (mean pLDDT 88.1)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 85.5/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUL5
- HPA: https://www.proteinatlas.org/ENSG00000130813-SHFL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHFL%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
