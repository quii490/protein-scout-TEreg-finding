---
type: protein-evaluation
gene: "SCAMP1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (membrane trafficking protein)"
---

## SCAMP1 -- Re-evaluation Report (REJECTED: Non-Nuclear Membrane Protein)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCAMP1 / SCAMP |
| Protein Name | Secretory carrier-associated membrane protein 1 |
| Protein Size | 338 aa, 37.9 kDa |
| UniProt ID | O15126 (SCAM1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Full harvest packet available |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 2/10 | x4 | **8** | Golgi/TGN/endosome/PM membranes; no nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 338 aa, well within ideal range |
| Research Novelty | 6/10 | x5 | **30** | PubMed strict=50, broad=68 (41-80 -> 6) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold mean pLDDT 79.0; no experimental PDB |
| Regulatory Domains | 3/10 | x2 | **6** | SCAMP family domain only; no known regulatory domains |
| PPI Network | 5/10 | x3 | **15** | 20 UniProt interactors; STRING top score 0.833 (ITSN1) |
| Cross-Validation Bonus | -- | -- | **+0** | No multi-DB nuclear consensus; membrane localization consistent |
| **Raw Total** | | | **90.0/180** | |
| **Normalized Total** | | | **50.0/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 2/10 (threshold: ≤3). SCAMP1 is a membrane trafficking protein localized to Golgi, TGN, recycling endosomes, and plasma membrane. No credible nuclear localization evidence exists.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Golgi apparatus, trans-Golgi network membrane | Experimental (ECO:0000269) |
| UniProt (Swiss-Prot) | Recycling endosome membrane | Experimental (ECO:0000269) |
| GO-CC | Clathrin-coated vesicle, membrane, plasma membrane, recycling endosome membrane, synaptic vesicle membrane, trans-Golgi network | Multiple evidence levels |
| HPA IF | Nucleoplasm, Vesicles, Cell Junctions | Reliability: **Uncertain** |
| HPA Main | Cell Junctions | -- |

**Manual Review Assessment**: SCAMP1 is unambiguously a membrane trafficking protein. Its UniProt primary annotations place it at Golgi/trans-Golgi network and recycling endosome membranes. The HPA IF data annotates nucleoplasm but with "Uncertain" reliability, and this is listed as an additional (not main) location. The HPA main location is "Cell Junctions," consistent with its membrane trafficking role. The nucleoplasm annotation likely reflects non-specific IF signal rather than bona fide nuclear localization. No GO-CC nuclear terms are annotated. The protein functions in post-Golgi recycling pathways as a carrier to the cell surface -- entirely cytoplasmic/membrane processes. Nuclear localization score 2/10 reflects near-complete absence of credible nuclear evidence.

### 4. Protein Size Assessment

SCAMP1 is 338 amino acids (37.9 kDa), well within the ideal range for recombinant expression, purification, and biochemical characterization. Size score: 10/10. (This dimension is irrelevant given the rejection for non-nuclear localization.)

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 50 articles |
| PubMed broad count | 68 articles |
| Novelty category | 41-80 -> Score 6 |

SCAMP1 has been studied since the late 1990s. Key research includes its role in post-Golgi recycling, insulin secretion (palmitoylation in beta-cells), cancer cell migration/invasion, and its structural characterization. The SCAMP family (SCAMP1-5) is a well-established group of membrane carriers. Research activity is moderate, placing SCAMP1 in the "moderately studied" category. PubMed score 6/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (AF-O15126-F1, v6) |
| PDB Entries | 0 (no experimental structures) |
| Mean pLDDT | 79.0 |
| pct pLDDT >90 | 41.7% |
| pct pLDDT 70-90 | 27.5% |
| pct pLDDT <50 | 10.4% |

AlphaFold predicts a well-folded structure with 69.2% of residues above pLDDT 70. The structure quality is good but not exceptional. No experimental PDB entries exist. Score 7/10 reflects the solid predicted structure without experimental validation.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR007273 | SCAMP family domain; no name assigned |
| Pfam | PF04144 | SCAMP family; no name assigned |

SCAMP1 contains a single Pfam/InterPro domain of the SCAMP family. This domain is characteristic of secretory carrier membrane proteins but is not a canonical regulatory domain (no kinase, phosphatase, ubiquitin ligase, or transcription factor domains). Score 3/10 reflects the absence of characterized regulatory domains.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Strong interactions: ITSN1 (0.833), SYNRG (0.829), SCAMP2 (0.646, experimental 0.618), RAB5A, SNAP23 |
| IntAct | 15 interactors including TP53, UBE3A, RAB11A, RAB9A, LAMP1, DNAJC5 |
| UniProt Interactions | 20 interactors (ARFIP1, ARFIP2, CASP6, CFTR, DNAJC13, GAD2, LAMP2, etc.) |

SCAMP1 has a reasonably well-characterized PPI network. Key partners include ITSN1 and SYNRG (high STRING scores), RAB GTPases (RAB5A, RAB9A, RAB11A), and SNARE proteins (SNAP23, SNAP25, STX7, VAMP8). The interactions are consistent with its role in membrane trafficking. CFTR interaction (7 experiments) is notable. Score 5/10 reflects moderate PPI characterization.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Membrane Localization | UniProt + GO-CC + HPA + STRING | Membrane trafficking | Fully consistent |
| PPI | STRING + IntAct + UniProt | Membrane trafficking partners | Consistent |

No cross-validation bonus awarded: SCAMP1 lacks nuclear localization across all databases, and no structural cross-validation is possible (no experimental PDB). Cross-validation bonus: +0.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED)

**Primary Rejection Reason**: SCAMP1 is a membrane trafficking protein with no credible nuclear localization. Its primary subcellular compartments are Golgi, trans-Golgi network, recycling endosomes, and plasma membrane. The weak HPA nucleoplasm annotation ("Uncertain" reliability, additional location only) is insufficient to override the clear membrane localization evidence from UniProt (experimental ECO:0000269) and GO-CC annotations. The protein functions in post-Golgi recycling -- a cytoplasmic process entirely unrelated to nuclear functions or TE regulation.

### 11. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 2/10 (threshold: ≤3 → REJECTED). SCAMP1 is a well-characterized membrane trafficking protein. Its biology -- post-Golgi recycling, vesicle transport, insulin secretion, and cancer cell migration -- is unrelated to nuclear functions or transposable element regulation. The rejection is based on unambiguous non-nuclear localization supported by experimental evidence (ECO:0000269) across multiple databases. No appeal pathway: this rejection is confident and irreversible based on the nuclear≤3 rule.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O15126
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15126
- STRING: https://string-db.org/network/9606.ENSP00000481022
- HPA: https://www.proteinatlas.org/ENSG00000085365-SCAMP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SCAMP1%22
- Harvest Packet: SCAMP1.json (full data available)
