---
type: protein-evaluation
gene: "SELENOO"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (mitochondrial pseudokinase)"
---

## SELENOO -- Re-evaluation Report (REJECTED: Mitochondrial Pseudokinase, No Nuclear Localization)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SELENOO / SELO, Selenoprotein O |
| Protein Name | Selenoprotein O (protein adenylyltransferase/pseudokinase) |
| Protein Size | 669 aa, ~74.2 kDa (largest known mammalian selenoprotein) |
| UniProt ID | Q9BVL4 (SELO_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | Mitochondrion; no nuclear annotation in any database |
| Protein Size | 6/10 | x1 | **6** | 669 aa, very large (largest selenoprotein) |
| Research Novelty | 8/10 | x5 | **40** | Estimated ~30-50 PubMed articles |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold predicted; pseudokinase fold; no experimental PDB |
| Regulatory Domains | 5/10 | x2 | **10** | Pseudokinase domain; protein adenylyltransferase (AMPylase) |
| PPI Network | 3/10 | x3 | **9** | Limited PPI data; mitochondrial redox network |
| Cross-Validation Bonus | -- | -- | **+0** | Consistent mitochondrial annotation |
| **Raw Total** | | | **84.0/180** | |
| **Normalized Total** | | | **46.7/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 1/10 (threshold: ≤3). SELENOO is a mitochondrial protein with no nuclear localization.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Mitochondrion | Primary annotation |
| GO-CC | Mitochondrion | Multiple evidence codes |
| dbPTM | Mitochondrion | Curated |
| Wikipedia | Mitochondrion | Consensus |

**Manual Review Assessment**: SELENOO is the largest known mammalian selenoprotein and is exclusively mitochondrial. It functions as a pseudokinase with protein adenylyltransferase (AMPylase) activity, transferring AMP to serine/threonine/tyrosine residues of target proteins. This enzymatic activity is involved in the cellular response to oxidative stress and redox homeostasis within mitochondria. The protein contains a selenocysteine (Sec) residue encoded by a UGA codon with a SECIS element. No database annotates nuclear localization. The protein's biology is entirely mitochondrial, with no connection to nuclear functions, transcriptional regulation, or chromatin biology. Nuclear localization score 1/10.

### 4. Protein Size Assessment

SELENOO is 669 amino acids (74.2 kDa), the largest mammalian selenoprotein. This large size is a disadvantage for biochemical characterization, requiring careful optimization for recombinant expression and purification. Size score: 6/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~30-50 articles |
| Novelty category | 31-50 -> Score 8 |

SELENOO research is limited, focusing on its unique AMPylase activity and role in mitochondrial redox signaling. As the largest selenoprotein and one of the few known mammalian AMPylases, it has attracted some specialized interest. Moderate-to-low research activity. Score 8/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Domain | Pseudokinase fold with AMP transferase activity |

The pseudokinase domain is expected to adopt a well-folded structure similar to protein kinases, and AlphaFold typically predicts kinase-like folds with high confidence. No experimental structural data. Score 5/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | Pseudokinase domain | Protein adenylyltransferase (AMPylase); catalytically competent despite "pseudo" designation |
| UniProt | Selenocysteine active site | Sec residue in catalytic domain |

SELENOO contains a pseudokinase domain with AMPylase activity -- a rare enzymatic function in mammals. While this is an interesting biochemical activity, it is not a regulatory domain in the traditional sense (not involved in transcription, chromatin, or signal transduction regulation). It is a metabolic enzyme domain. Score 5/10 reflects the unique enzymatic activity as a partial regulatory feature.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Limited data; mitochondrial redox network |
| Known Partners | Mitochondrial redox targets (substrates for AMPylation) |

PPI data is limited. No nuclear or regulatory interactions characterized. Score 3/10.

### 9. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 1/10. SELENOO is a mitochondrial pseudokinase with no nuclear function.

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVL4
- Wikipedia: https://en.wikipedia.org/wiki/Selenoprotein_O
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=SELO_HUMAN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SELENOO
- Note: Harvest packet not available; data compiled from web database queries
