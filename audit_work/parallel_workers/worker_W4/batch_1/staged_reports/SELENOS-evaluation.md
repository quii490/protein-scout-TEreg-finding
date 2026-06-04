---
type: protein-evaluation
gene: "SELENOS"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (ER membrane protein, ERAD component)"
---

## SELENOS -- Re-evaluation Report (REJECTED: ER Membrane Protein, No Nuclear Localization)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SELENOS / SELS, VIMP, Selenoprotein S |
| Protein Name | Selenoprotein S (VCP-interacting membrane protein) |
| Protein Size | 189 aa, ~21 kDa |
| UniProt ID | Q9BQE4 (SELS_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | ER membrane, cytoplasm; no nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 189 aa, ideal size range |
| Research Novelty | 5/10 | x5 | **25** | Estimated ~80-120 PubMed articles (well-studied selenoprotein) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold predicted; single-pass TM; no experimental PDB |
| Regulatory Domains | 2/10 | x2 | **4** | No regulatory domains; selenocysteine active site |
| PPI Network | 6/10 | x3 | **18** | Derlin-1/VCP complex; ERAD machinery; well-characterized |
| Cross-Validation Bonus | -- | -- | **+0** | Consistent ER annotation |
| **Raw Total** | | | **76.0/180** | |
| **Normalized Total** | | | **42.2/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 1/10 (threshold: ≤3). SELENOS is an ER membrane protein with no nuclear localization.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Endoplasmic reticulum membrane (single-pass) | Primary annotation |
| UniProt (Swiss-Prot) | Cytoplasm | Additional annotation |
| GO-CC | ER membrane (GO:0005789) | Database annotation |
| GO-CC | Integral component of ER membrane | Database annotation |
| dbPTM | Endoplasmic reticulum membrane, Cytoplasm | Curated |

**Manual Review Assessment**: SELENOS is a single-pass ER membrane protein with its N-terminus in the ER lumen and C-terminus in the cytoplasm. It is a core component of the Derlin-1-VIMP complex (ERAD retrotranslocation complex), linking DERL1 to the VCP/p97 ATPase complex to facilitate transfer of misfolded proteins from the ER to the cytosol for proteasomal degradation. The protein is also associated with cytoplasmic microtubules. Its transmembrane helix spans residues 33-53. No database annotates nuclear localization. The ERAD function is entirely ER/cytoplasmic. Nuclear localization score 1/10.

### 4. Protein Size Assessment

SELENOS is 189 amino acids (21 kDa), an ideal size for biochemical and structural studies. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~80-120 articles |
| Novelty category | 81-120 -> Score 5 |

SELENOS is one of the better-studied selenoproteins. Research covers its role in ERAD, ER stress response, inflammation (NF-kB regulation), and metabolic diseases. Its well-characterized role in the Derlin-1 retrotranslocation complex has generated a substantial literature. Score 5/10 reflects the relatively high research volume.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structure Type | Single-pass TM + cytoplasmic coiled-coil domain |

AlphaFold predicts a single transmembrane helix (33-53) and a cytoplasmic domain likely containing coiled-coil regions for VCP interaction. No experimental structure. Score 5/10.

### 7. Domain Architecture

SELENOS contains a transmembrane domain and a C-terminal coiled-coil domain mediating VCP interaction. It contains a selenocysteine residue at its active site but no canonical regulatory domains (no kinase, phosphatase, DNA-binding, or chromatin domains). Score 2/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Known Partners | DERL1 (ERAD), VCP/p97 (ATPase), Derlin-1 retrotranslocation complex |
| STRING | ERAD network; well-characterized |

SELENOS has a well-characterized PPI network centered on the ERAD machinery. Its interaction with DERL1 and VCP is functionally essential and well-validated. Additional partners include other ER stress proteins. Score 6/10 reflects well-characterized but functionally narrow PPI network.

### 9. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 1/10. SELENOS is an ER membrane protein involved in ERAD with no nuclear function.

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQE4
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=SELS_HUMAN
- Membranome: https://biomembhub.org/membranome/proteins/17738
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SELENOS
- Note: Harvest packet not available; data compiled from web database queries
