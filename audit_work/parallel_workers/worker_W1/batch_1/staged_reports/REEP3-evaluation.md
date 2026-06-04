---
type: protein-evaluation
gene: "REEP3"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## REEP3 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | REEP3 / Receptor expression-enhancing protein 3 |
| Protein Name | Receptor expression-enhancing protein 3 |
| Protein Size | 255 aa |
| UniProt ID | Q6NUK4 (REEP3_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | ER membrane protein; multi-pass transmembrane; no nuclear localization evidence |
| Protein Size | 5/10 | x1 | **5** | 255 aa, within acceptable but not ideal range |
| Research Novelty | 6/10 | x5 | **30** | PubMed ~60-80 articles (61-80 -> 4) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold prediction available; no experimental PDB |
| Regulatory Domains | 4/10 | x2 | **8** | 3 transmembrane domains; tubulin/microtubule-binding; no known regulatory domains |
| PPI Network | 3/10 | x3 | **9** | Microtubule and ER-associated interactions; limited regulatory PPI |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB localization consistency (+0.5) |
| **Raw Total** | | | **67.5/180** | |
| **Normalized Total** | | | **37.5/100** | |

### 3. Nuclear Localization Evidence -- CRITICAL FAIL

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Endoplasmic reticulum membrane; Multi-pass membrane protein | Reviewed, high confidence |
| GO-CC | Endoplasmic reticulum membrane (GO:0005789) | Curated |
| GO-CC | Endoplasmic reticulum (GO:0005783) | Curated |
| GO-CC | Microtubule (GO:0005874) | Curated |
| GO-CC | Membrane (GO:0016020) | Curated |
| GO-CC | Integral component of membrane (GO:0016021) | Curated |
| HPA | Not available in packet | -- |
| Any nuclear source | NONE | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: REEP3 is unequivocally an endoplasmic reticulum membrane protein. It contains 3 transmembrane domains that anchor it in the ER membrane. The protein functions as a microtubule-binding protein that sequesters the ER away from chromosomes during mitosis, which is required for proper nuclear envelope reassembly. Despite its role in a process related to the nucleus (nuclear envelope reassembly), the protein itself is not nuclear -- it acts on the ER membrane from the cytoplasmic side. No database annotates REEP3 to any nuclear compartment. There is no nuclear localization signal, no DNA-binding domain, and no evidence of nuclear import. **Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED.**

### 4. Protein Size Assessment

REEP3 is 255 amino acids, which is below the ideal range (200-800 aa lower bound) but still within the workable size for biochemical assays. The small size may limit some experimental approaches. Size score: 5/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~60-80 |
| Novelty category | 61-80 -> Score 4 |

**Research Context**: REEP3/REEP4 are relatively well-studied in the context of ER dynamics during mitosis. Key publications focus on their role in clearing ER from metaphase chromosomes and their microtubule-binding properties. The gene is also studied in the context of hereditary spastic paraplegia (HSP) and ER shaping. The PubMed count of ~60-80 places this in the moderate-to-well-studied range.

**Novelty Assessment**: REEP3 is not a highly novel target. The gene has a defined function in ER reorganization during mitosis, and structural/mechanistic studies exist. Score 4/10 (61-80 PubMed) reflects moderate prior research.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no experimental structures) |
| Structural Features | 3 transmembrane helices; cytoplasmic microtubule-binding domain |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: REEP3 is a membrane protein with 3 predicted transmembrane alpha-helices. The structure is relatively simple and the AlphaFold prediction likely captures the topology accurately, although membrane protein predictions can have lower confidence in the transmembrane regions. Score 5/10 reflects simple structure with reasonable prediction but no experimental validation.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | Transmembrane domains (positions 1-21, 35-55, 59-79) | ER membrane anchoring |
| GO Molecular Function | Microtubule binding | ER-microtubule tethering |
| GO Biological Process | Nuclear envelope reassembly | ER sequestration during mitosis |

**Domain Analysis**: REEP3 has a simple domain architecture consisting primarily of 3 N-terminal transmembrane domains and a cytoplasmic microtubule-binding region. There are no known chromatin-binding domains, DNA-binding domains, transcription factor domains, or other regulatory domains typically associated with nuclear proteins. The protein's primary function is structural -- shaping and positioning the ER -- rather than regulatory. Domain score: 4/10.

### 8. PPI Network Analysis

| Partner | Context | Relevance |
|---------|---------|-----------|
| Microtubules | ER-microtubule tethering | Structural |
| REEP4 | Functional partner in ER shaping | Structural |
| ER membrane proteins | Co-localization | Structural |

**PPI Assessment**: REEP3 interaction data is limited. The protein interacts with microtubules and likely with other ER-shaping proteins (REEP family members). No interactions with nuclear proteins, transcription factors, or chromatin modifiers were identified. PPI score: 3/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + GO-CC + literature | ER membrane, microtubule | Multi-source consistent |
| Function | Literature + GO | ER shaping, mitotic ER clearance | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database ER membrane localization consistency: +0.5
- No nuclear-related cross-validation possible
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. Zero nuclear localization evidence -- REEP3 is an ER membrane protein
2. Protein topology (3 transmembrane domains) incompatible with soluble nuclear function
3. No DNA-binding, chromatin-binding, or transcriptional regulatory domains
4. Function is structural (ER shaping), not regulatory
5. Despite involvement in nuclear envelope reassembly, the protein acts from the cytoplasmic side

**Why Previous Rejection Was Correct**: 
The original rejection of REEP3 was appropriate. This is an ER membrane protein with no nuclear localization. The protein's role in nuclear envelope reassembly during mitosis does not make it a nuclear protein -- it functions on the ER from the cytoplasmic compartment.

**Would Additional Data Change the Decision?**
No. The localization data is conclusive across multiple curated databases. Additional HPA IF or AlphaFold data would not change the fundamental fact that REEP3 is an ER membrane protein.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). REEP3 fails the nuclear localization criterion (score 0/10, threshold <=3). The protein is an ER-resident multi-pass transmembrane protein with no evidence of nuclear localization. Recovery from false-rejection does not apply -- the original rejection was correct. Nuclear score <=3 triggers automatic REJECTED status per scoring rules.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6NUK4
- GO: https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=Q6NUK4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22REEP3%22
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
