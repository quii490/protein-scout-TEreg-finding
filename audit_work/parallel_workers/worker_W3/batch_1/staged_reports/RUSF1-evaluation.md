---
type: protein-evaluation
gene: "RUSF1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RUSF1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RUSF1 / C16orf58, FLJ13638, RUS |
| Protein Name | RUS Family Member 1 |
| Protein Size | 468 aa (main isoform); isoform 2: 206 aa |
| UniProt ID | Q96GQ5 (RUSF1_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | ER membrane protein; no nuclear annotation or evidence |
| Protein Size | 10/10 | x1 | **10** | 468 aa, within ideal range |
| Research Novelty | 10/10 | x5 | **50** | Virtually unstudied; PubMed <5 articles for RUSF1/C16orf58 |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold prediction only; no PDB entries |
| Regulatory Domains | 3/10 | x2 | **6** | DUF647 domain of unknown function; no known regulatory domains |
| PPI Network | 2/10 | x3 | **6** | Limited interaction data (MVD, BSCL2, TSC22D4) |
| Cross-Validation Bonus | -- | -- | **+0** | No cross-validation possible (non-nuclear) |
| **Raw Total** | | | **88.0/180** | |
| **Normalized Total** | | | **31.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Membrane; single-pass membrane protein | Probable |
| GO-CC | GO:0016020 (membrane) | IEA |
| GO-CC | GO:0016021 (integral component of membrane) | IEA |
| GeneCards | Endoplasmic reticulum (predicted) | Computational |

**HPA IF Status**: No HPA IF data available. Protein annotated as ER membrane protein.

**Manual Review Assessment**: RUSF1 is a putative single-pass transmembrane protein localized to the endoplasmic reticulum membrane. It contains a conserved DUF647 domain of unknown function. The plant ortholog (RUS, Root UVB Sensitive) participates in UV-B light sensing during root morphogenesis, but this is a cytoplasmic/membrane function. There is no evidence of nuclear localization from any database or experimental source. The protein's transmembrane topology is incompatible with nuclear localization. Nuclear localization score: 1/10.

**REJECTION TRIGGER**: Nuclear localization score ≤3. RUSF1 is an ER membrane protein with no nuclear annotation, function, or evidence. This gene does not meet the minimum nuclear localization threshold.

### 4. Protein Size Assessment

RUSF1 is 468 amino acids in the main isoform, with a shorter isoform of 206 aa. Both isoforms fall within the experimentally tractable range. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed (RUSF1/C16orf58) | <5 articles |
| Novelty category | ≤20 -> Score 10 |

RUSF1 is virtually unstudied in the human context. The gene was previously designated C16orf58 (chromosome 16 open reading frame 58). The plant ortholog RUS has been studied in the context of UV-B light sensing, but human RUSF1 remains a poorly characterized gene with no dedicated functional studies. While extremely novel, this does not rescue the lack of nuclear localization.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (predicted) |
| PDB Entries | 0 |
| Structural Features | Single-pass transmembrane domain |

No experimental structures exist for RUSF1. The AlphaFold prediction is available but of unknown quality. As a transmembrane protein, structural characterization is inherently more challenging than for soluble proteins. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR006968 (DUF647) | Domain of unknown function |
| Pfam | PF04884 (DUF647) | Uncharacterized |

The sole annotated domain is DUF647, a domain of unknown function. No regulatory domains (zinc fingers, homeoboxes, kinase domains, etc.) are present. The domain architecture provides no support for a nuclear or regulatory function. Score 3/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Limited data |
| Known Partners | MVD (cholesterol biosynthesis), BSCL2/seipin (lipid droplets), TSC22D4 (transcriptional regulation) |

The limited interaction data suggests possible roles in cholesterol metabolism and lipid droplet biology, consistent with ER membrane localization. No interactions with nuclear or chromatin-associated proteins have been reported. Score 2/10.

### 9. Cross-Validation Analysis

No cross-validation possible. The protein is a non-nuclear ER membrane protein with a DUF647 domain of unknown function. No multi-database consistency checks are applicable.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (Score: 31.1/100; REJECTED for nuclear≤3)

**Core Weaknesses**:
1. ER membrane protein with no nuclear localization evidence (FATAL)
2. DUF647 domain of unknown function -- no regulatory domain support
3. No characterized nuclear function or interaction partners
4. Transmembrane topology fundamentally incompatible with nuclear localization
5. No multi-database support for any nuclear annotation

**Note**: While RUSF1 scores well on novelty (10/10) and protein size (10/10), the complete absence of nuclear localization is disqualifying. The gene may have interesting biology related to ER function, lipid metabolism, or stress response (based on plant ortholog), but these are not within the scope of TE-regulated nuclear protein screening.

### 11. Decision

**FINAL DECISION**: REJECTED. Nuclear localization score 1/10 (≤3 threshold). RUSF1 is an ER membrane protein that lacks any evidence of nuclear localization. The nuclear localization failure is fundamental and cannot be remediated by any other scoring dimension. This gene does not qualify as a candidate for TE-regulated nuclear protein screening.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96GQ5
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RUSF1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RUSF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GQ5
- Note: Harvest packet not available; data compiled from UniProt, GeneCards, and literature database queries
