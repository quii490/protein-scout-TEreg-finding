---
type: protein-evaluation
gene: "SELENOK"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (ER membrane protein, 94 aa)"
---

## SELENOK -- Re-evaluation Report (REJECTED: ER Membrane Protein, No Nuclear Localization)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SELENOK / SELK, Selenoprotein K |
| Protein Name | Selenoprotein K (SelK) |
| Protein Size | 94 aa (very small, single-pass ER membrane protein) |
| UniProt ID | Q9Y6D0 (SELK_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | ER membrane, single-pass TM; cell membrane; no nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 94 aa, very small |
| Research Novelty | 6/10 | x5 | **30** | Estimated ~50-80 PubMed articles |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold predicted; very small single-TM protein; no PDB |
| Regulatory Domains | 2/10 | x2 | **4** | No regulatory domains; single selenocysteine active site |
| PPI Network | 4/10 | x3 | **12** | ERAD complex (Derlin-1); DHHC6 palmitoyltransferase |
| Cross-Validation Bonus | -- | -- | **+0** | Consistent ER annotation; no nuclear evidence |
| **Raw Total** | | | **69.0/180** | |
| **Normalized Total** | | | **38.3/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 1/10 (threshold: ≤3). SELENOK is a very small (94 aa) ER membrane protein with no nuclear localization.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Endoplasmic reticulum membrane (single-pass) | Primary annotation |
| UniProt (Swiss-Prot) | Cell membrane | Additional annotation |
| dbPTM | Endoplasmic reticulum membrane, Cell membrane | Curated |
| Membranome | TM helix aa 19-40, ΔGfold = -6.6 kcal/mol | Biophysical prediction |

**Manual Review Assessment**: SELENOK is a very small (94 aa) single-pass transmembrane protein primarily localized to the ER membrane, with additional detection at the cell membrane. Its transmembrane helix spans residues ~20-42. The protein functions in ER-associated degradation (ERAD) of glycosylated proteins and facilitates protein palmitoylation by stabilizing the acyl-DHHC6 intermediate. The C-terminal selenocysteine residue (position 92) is critical for its redox function. SELENOK is involved in Ca2+ flux regulation in immune cells. The protein contains no DNA-binding domains, no nuclear localization signals, and no nuclear function. All annotated localizations are membrane compartments. Nuclear localization score 1/10.

### 4. Protein Size Assessment

At 94 amino acids, SELENOK is one of the smallest selenoproteins. While very small, this makes it amenable to structural characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~50-80 articles |
| Novelty category | 41-80 -> Score 6 |

SELENOK research focuses on its roles in ERAD, immune cell calcium signaling, and ER stress protection. Moderate but focused literature. Score 6/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structure Type | Single-pass TM helix + short cytosolic tail |

The very small size and single transmembrane helix topology limit structural complexity. AlphaFold predicts a simple structure. Score 3/10.

### 7. Domain Architecture

SELENOK contains no characterized protein domains beyond its transmembrane helix and a short cytoplasmic C-terminal tail containing the selenocysteine active site. No regulatory domains. Score 2/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Known Partners | Derlin-1 (ERAD complex), DHHC6 (palmitoyltransferase) |

PPI data is limited to ER membrane partners. No nuclear or regulatory interactions. Score 4/10.

### 9. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 1/10. SELENOK is an ER membrane protein with no nuclear function.

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6D0
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=SELK_HUMAN
- Membranome: https://biomembhub.org/membranome/proteins/4927
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SELENOK
- Note: Harvest packet not available; data compiled from web database queries
