---
type: protein-evaluation
gene: "REP15"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## REP15 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | REP15 / RAB15EP, Rab15 effector protein |
| Protein Name | Rab15 effector protein |
| Protein Size | 236 aa |
| UniProt ID | Q6BDI9 (REP15_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | Early endosome membrane; endocytic recycling compartment; no nuclear evidence |
| Protein Size | 5/10 | x1 | **5** | 236 aa, near lower limit of workable range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~5-10 articles (<=20 -> 10) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold prediction only; no PDB; small membrane-associated protein |
| Regulatory Domains | 2/10 | x2 | **4** | No known regulatory domains; RAB effector binding only |
| PPI Network | 2/10 | x3 | **6** | Interaction with GTP-bound RAB15 only |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB localization consistency (+0.5) |
| **Raw Total** | | | **77.5/180** | |
| **Normalized Total** | | | **43.1/100** | |

### 3. Nuclear Localization Evidence -- CRITICAL FAIL

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Early endosome membrane | Reviewed |
| UniProt | Endocytic recycling compartment | Reviewed |
| HPA | Not available in packet | -- |
| Any nuclear source | NONE | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: REP15 is an endosomal membrane protein. It localizes specifically to the early endosome membrane and the endocytic recycling compartment, where it regulates transferrin receptor recycling from the endocytic recycling compartment back to the cell surface. The protein colocalizes with RAB11 and RAB15. There is zero evidence for nuclear localization from any database. The gene is intronless, which is sometimes a feature of retrotransposed genes. **Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED.**

### 4. Protein Size Assessment

REP15 is 236 amino acids, at the lower end of the workable size range. Small proteins can be more challenging for some biochemical assays but are generally still tractable. Size score: 5/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~5-10 |
| Novelty category | <=20 -> Score 10 |

**Research Context**: REP15 is extremely understudied. The gene was identified as a RAB15 effector involved in endocytic recycling. There are very few publications directly studying REP15. Most references are from large-scale interaction screens or gene catalogs. No disease associations have been established.

**Novelty Assessment**: REP15 is an extremely novel target with minimal published research. Score 10/10 reflects the very low PubMed count (<=20). However, the high novelty score is negated by the complete absence of nuclear localization.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Features | Small protein, likely RAB-binding domain |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: REP15 is a small protein with limited structural characterization. AlphaFold prediction is available but quality is uncertain for a protein of this size with limited domain annotation. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | RAB15 binding region | Protein-protein interaction |
| Gene Features | Intronless gene | Retrotransposed origin |

**Domain Analysis**: REP15 has minimal domain annotation. The protein functions as a binding partner for GTP-bound RAB15. No known regulatory domains (DNA-binding, chromatin-binding, transcription factor, enzyme, etc.) are present. Domain score: 2/10.

### 8. PPI Network Analysis

| Partner | Context | Evidence |
|---------|---------|----------|
| RAB15 (GTP-bound) | Endocytic recycling regulation | Direct interaction |
| RAB11 | Colocalization in recycling compartment | Colocalization |

**PPI Assessment**: REP15 interacts primarily with RAB15 in its GTP-bound form. This interaction mediates its role in endocytic recycling. No interactions with nuclear proteins, transcription factors, chromatin modifiers, or other regulatory proteins were identified. PPI score: 2/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + literature | Early endosome, recycling compartment | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database endosomal localization consistency: +0.5
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. Zero nuclear localization evidence -- REP15 is an endosomal membrane protein
2. Function is exclusively in endocytic recycling, not nuclear regulation
3. No regulatory domains of any kind
4. Minimal PPI network, limited to endosomal RAB GTPases
5. Gene is intronless, consistent with retrotransposed origin

**Why Previous Rejection Was Correct**:
The original rejection of REP15 was appropriate. This is an endosomal protein with no connection to nuclear biology. The gene is extremely novel and understudied, but this does not compensate for the complete absence of nuclear localization.

**Would Additional Data Change the Decision?**
No. REP15 functions in endocytic membrane trafficking. No amount of additional structural or interaction data would change the cellular compartment in which it functions.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). REP15 fails the nuclear localization criterion (score 0/10, threshold <=3). The protein is an early endosome membrane protein involved in endocytic recycling. Nuclear score <=3 triggers automatic REJECTED status per scoring rules. Recovery from false-rejection does not apply -- the original rejection was correct.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6BDI9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22REP15%22
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/387849
- Ensembl: https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174236
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
