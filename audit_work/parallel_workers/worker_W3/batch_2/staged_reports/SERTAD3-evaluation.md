---
type: protein-evaluation
gene: "SERTAD3"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SERTAD3 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERTAD3 / RBT1 |
| Protein Name | SERTA domain-containing protein 3 |
| Protein Size | 196 aa / 21.8 kDa |
| UniProt ID | Q9UJW9 |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | HPA Approved + UniProt Nucleus; nuclear focused |
| Protein Size | 8/10 | x1 | **8** | 196 aa; acceptable range |
| Research Novelty | 10/10 | x5 | **50** | 12 publications; extremely novel (≤20) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold marginal (pLDDT=66.8); novel protein baseline |
| Regulatory Domains | 10/10 | x2 | **20** | 3 domains; chromatin/DNA-related function. Direct regulatory potential. |
| PPI Network | 6/10 | x3 | **18** | Physical interactions present (13 partners) but no chromatin regulatory partners |
| Cross-Validation Bonus | — | max +3 | **+0.5** | HPA + UniProt nuclear localization agreement (+0.5) |
| **Raw Total** | | | **150.5/183** | |
| **Normalized Total** | | | **82.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Nucleus | ECO:0000269 |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoli | Approved |

**Assessment**: HPA Approved + UniProt Nucleus; nuclear focused


### 4. Protein Size Assessment

196 aa; acceptable range. The protein size is within the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 12 |
| PubMed symbol-only count | 15 |
| PubMed broad count | 16 |
| Novelty category | ≤20 → 10 |

**Key Publications**:
1. Sun N et al. (2023). "SERTAD3 induces proteasomal degradation of ZIKV capsid protein and represents a therapeutic target.". *Journal of medical virology*. PMID: 36594413
2. Chen Y et al. (2025). "SERTAD3 interacts with porcine reproductive and respiratory syndrome virus nonstructural protein 9 and inhibits virus replication.". *International journal of biological macromolecules*. PMID: 40187446
3. Ramírez-Medina E et al. (2020). "The MGF360-16R ORF of African Swine Fever Virus Strain Georgia Encodes for a Nonessential Gene That Interacts with Host Proteins SERTAD3 and SDCBP.". *Viruses*. PMID: 31947814
4. Zhang S et al. (2020). "MicroRNA-92a Targets SERTAD3 and Regulates the Growth, Invasion, and Migration of Prostate Cancer Cells via the P53 Pathway.". *OncoTargets and therapy*. PMID: 32606766
5. Xia L et al. (2024). "Analysis of chromatin accessibility in peripheral blood mononuclear cells from patients with early-stage breast cancer.". *Frontiers in pharmacology*. PMID: 39376611

**Assessment**: 12 publications; extremely novel (≤20)


**Function Summary**: Antiviral interferon-stimulated protein that plays a role in innate immunity and in the suppression of viruses through different mechanisms (PubMed:33147462, PubMed:36594413). Plays a role in the late phase response of TLR-induced immune effector expression (By similarity). During influenza infection, interacts with PB2, PB1, and PA to disrupt the formation of the viral RdRp complex (PubMed:33147462). Inhibits zika virus by interacting with the capsid protein in the nucleolus and reducing its abundance through proteasomal degradation (PubMed:36594413). Strong transcriptional coactivator (PubMe

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | 66.8 |
| pLDDT > 90 (high confidence) | 17.9% |
| pLDDT 70-90 (moderate) | 27.0% |
| pLDDT 50-70 (low) | 29.6% |
| pLDDT < 50 (disordered) | 25.5% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold marginal (pLDDT=66.8); novel protein baseline

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR009263 |  |
| InterPro | IPR039585 |  |
| Pfam | PF06031 |  |

**Assessment**: 3 domains; chromatin/DNA-related function. Direct regulatory potential.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| USHBP1 | two hybrid pooling approach | 16189514 | physical association | — |
| A0A0J1HYA4 | two hybrid pooling approach | 20711500 | physical association | — |
| Q81N50 | two hybrid pooling approach | 20711500 | physical association | — |
| A0A0G2RM27 | two hybrid pooling approach | 20711500 | physical association | — |
| pdpD2 | two hybrid pooling approach | 20711500 | physical association | — |
| tolC | two hybrid pooling approach | 20711500 | physical association | — |
| ypeB | two hybrid pooling approach | 20711500 | physical association | — |
| ENSP00000375882.3 | two hybrid pooling approach | 20711500 | physical association | — |
| ... (5 more) | | | | |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| RPA2 | 0.868 | 0.292 | — |
| STN1 | 0.783 | 0.000 | — |
| SERTAD2 | 0.644 | 0.000 | — |
| SERTAD4 | 0.642 | 0.000 | — |
| UBL5 | 0.592 | 0.591 | — |
| SNRPB | 0.591 | 0.591 | — |
| TMEM50A | 0.580 | 0.000 | — |
| USHBP1 | 0.539 | 0.539 | — |
| ... (7 more) | | | |

**Known Complex Membership (GO Cellular Component)**:
- nucleus (IDA:UniProtKB)

**PPI Assessment**: Physical interactions present (13 partners) but no chromatin regulatory partners

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

**Normalized Score**: 82.2/100 (Raw: 150.5/183)

**Strengths**:
1. Strong nuclear localization (score 9/10)
1. Excellent research novelty (12 publications)
1. Promising PPI network with physical interaction evidence

**Weaknesses**:
1. No major identified weaknesses beyond novelty limitations


### 11. Decision

**FINAL DECISION**: SCORED — Eligible for further evaluation. Normalized score: 82.2/100. Strong candidate for follow-up studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJW9
- HPA: https://www.proteinatlas.org/ENSG00000167565-SERTAD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SERTAD3%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
