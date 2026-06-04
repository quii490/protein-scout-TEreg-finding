---
type: protein-evaluation
gene: "SHOC1"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHOC1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SHOC1 / C9orf84, ZIP2 |
| Protein Name | Protein shortage in chiasmata 1 ortholog |
| Protein Size | 1444 aa / 165.2 kDa |
| UniProt ID | Q5VXU9 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Approved + UniProt Nucleus; nuclear focused |
| Protein Size | 5/10 | x1 | **5** | 1444 aa; suboptimal range |
| Research Novelty | 10/10 | x5 | **50** | 12 publications; extremely novel (≤20) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold poor (pLDDT=49.1); mostly disordered |
| Regulatory Domains | 9/10 | x2 | **18** | 2 domains; chromatin/DNA-related function. Moderate regulatory potential. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (1 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0.5** | HPA + UniProt nuclear localization agreement (+0.5) |
| **Raw Total** | | | **139.5/183** | |
| **Normalized Total** | | | **76.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Chromosome | ECO:0000250 |
| GO-CC | chromosome | ISS:UniProtKB |
| GO-CC | condensed nuclear chromosome | ISS:UniProtKB |
| HPA | Nucleoplasm, Nuclear bodies | Approved |

**Assessment**: HPA Approved + UniProt Nucleus; nuclear focused


### 4. Protein Size Assessment

1444 aa; suboptimal range. The protein size is outside the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 12 |
| PubMed symbol-only count | 18 |
| PubMed broad count | 18 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Rotte N et al. (2025). "Genotype-specific differences in infertile men due to loss-of-function variants in M1AP or ZZS genes.". *EMBO molecular medicine*. PMID: 40374915
2. Guzmán-Jiménez A et al. (2024). "A comprehensive study of common and rare genetic variants in spermatogenesis-related loci identifies new risk factors for idiopathic severe spermatogenic failure.". *Human reproduction open*. PMID: 39678461
3. Macaisne N et al. (2008). "SHOC1, an XPF endonuclease-related protein, is essential for the formation of class I meiotic crossovers.". *Current biology : CB*. PMID: 18812090
4. Guiraldelli MF et al. (2018). "SHOC1 is a ERCC4-(HhH)2-like protein, integral to the formation of crossover recombination intermediates during mammalian meiosis.". *PLoS genetics*. PMID: 29742103
5. Qi Y et al. (2023). "Pathogenic bi-allelic variants of meiotic ZMM complex gene SPO16 in premature ovarian insufficiency.". *Clinical genetics*. PMID: 37270785

**Assessment**: 12 publications; extremely novel (≤20)


**Function Summary**: ATPase required during meiosis for the formation of crossover recombination intermediates (By similarity). Binds DNA: preferentially binds to single-stranded DNA and DNA branched structures (PubMed:29742103). Does not show nuclease activity in vitro, but shows ATPase activity, which is stimulated by the presence of single-stranded DNA (PubMed:29742103). Plays a key role in homologous recombination and crossing-over in meiotic prophase I in male and female germ cells (By similarity). Required for proper synaptonemal complex assembly and homologous chromosome pairing (By similarity). Requiref fo

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 49.1 |
| pLDDT > 90 (high confidence) | 0.8% |
| pLDDT 70-90 (moderate) | 29.2% |
| pLDDT 50-70 (low) | 7.8% |
| pLDDT < 50 (disordered) | 62.2% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold poor (pLDDT=49.1); mostly disordered

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR039991 |  |
| Pfam | PF17825 |  |

**Assessment**: 2 domains; chromatin/DNA-related function. Moderate regulatory potential.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| maP3 | two hybrid pooling approach | 20711500 | physical association | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| TEX11 | 0.833 | 0.253 | — |
| MSH4 | 0.760 | 0.000 | — |
| HFM1 | 0.740 | 0.000 | — |
| RNF212 | 0.713 | 0.000 | — |
| C1orf146 | 0.666 | 0.000 | — |
| SYCP1 | 0.598 | 0.000 | — |
| MSH5 | 0.584 | 0.000 | — |
| ADAD2 | 0.583 | 0.000 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- chromosome (ISS:UniProtKB)
- condensed nuclear chromosome (ISS:UniProtKB)

**PPI Assessment**: Physical interactions present (1 partners) but no chromatin regulatory partners

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Nuclear confirmed | Yes |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Consistent |
| PPI | IntAct + STRING | 1 IntAct, 15 STRING | Multiple sources |

**Cross-Validation Bonus Details**:
- HPA + UniProt nuclear localization agreement (+0.5)
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: PROMISING

**Normalized Score**: 76.2/100 (Raw: 139.5/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Excellent research novelty (12 publications)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 76.2/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5VXU9
- HPA: https://www.proteinatlas.org/ENSG00000165181-SHOC1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SHOC1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
