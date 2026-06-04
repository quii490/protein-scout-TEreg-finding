---
type: protein-evaluation
gene: "RHPN1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RHPN1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RHPN1 / Rhophilin-1 |
| Protein Name | Rhophilin-1 / Rho GTPase-binding protein |
| Protein Size | ~641 aa |
| UniProt ID | Q8TCX5 (RHPN1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, previously listed in garbage reports) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | Cytosol (primary); plasma membrane (predicted); no established nuclear localization; no NLS predicted |
| Protein Size | 10/10 | x1 | **10** | ~641 aa, within ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~15-20 articles (<=20 -> 10) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold prediction only; no PDB; PDZ domain + Rho-binding domain |
| Regulatory Domains | 4/10 | x2 | **8** | PDZ domain; Rho-binding domain; negative regulation of stress fiber assembly |
| PPI Network | 3/10 | x3 | **9** | Limited PPI; RHOA (GTP-bound), ROPN1, CEP70, GOLGA2, LMNA, GFAP |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB cytosol localization consistency (+0.5) |
| **Raw Total** | | | **96.5/180** | |
| **Normalized Total** | | | **53.6/100** | |

### 3. Nuclear Localization Evidence -- FAILS THRESHOLD

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt / Ensembl GO-CC | Cytosol (GO:0005829) | Curated |
| HPA | Cytoplasmic expression in most cell types | IF-based |
| HPA (predicted) | Intracellular | Predicted |
| COMPARTMENTS DB | No strong nuclear evidence | Aggregated |
| Predicted Features | No NLS (nuclear localization signal) predicted | Computational |
| Predicted Features | No signal peptide; no transmembrane domains | Computational |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RHPN1/Rhophilin-1 is primarily a cytosolic protein with no established nuclear localization. Key evidence:

- GO-CC primary annotation: Cytosol (GO:0005829)
- HPA: "Cytoplasmic expression in most cell types of variable expression levels"
- No nuclear localization signal (NLS) predicted
- Function: Negative regulation of stress fiber assembly; downstream effector of Rho GTPase signaling
- The protein interacts with RHOA (GTP-bound), a plasma membrane/cytosolic GTPase

Some interaction partners suggest possible proximity to the nucleus: LMNA (lamin A, nuclear envelope) and CEP70 (centrosomal protein). However, interaction with a nuclear envelope protein does not constitute nuclear localization. The PDZ domain mediates protein-protein interactions at membranes and the cytoskeleton, not in the nucleus.

**Nuclear localization score: 1/10. RULE: Nuclear <=3 -> REJECTED.** The score of 1 (not 0) reflects the formal possibility suggested by some interaction partners (LMNA, CEP70), but there is no direct evidence of RHPN1 in the nucleus.

### 4. Protein Size Assessment

RHPN1 is approximately 641 amino acids, within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~15-20 |
| Novelty category | <=20 -> Score 10 |

**Research Context**: RHPN1 is an extremely understudied gene. Most of the limited literature focuses on its role as a Rho GTPase effector and its interaction with RHOA. The gene has limited functional characterization and no established disease associations.

**Novelty Assessment**: With ~15-20 PubMed articles, RHPN1 falls in the <=20 range (score 10). The gene is extremely novel. However, the high novelty score cannot compensate for the lack of nuclear localization.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Features | N-terminal PDZ domain; Rho-binding domain; predicted largely disordered regions |

**Structure Assessment**: RHPN1 contains an N-terminal PDZ domain and a Rho-binding domain. PDZ domains are well-structured protein-protein interaction modules typically found in scaffolding proteins at membranes. The remainder of the protein may contain disordered regions. AlphaFold prediction quality is expected to be good for the structured domains but lower for inter-domain regions. Score 5/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | PDZ domain | Protein-protein interaction; membrane-associated scaffolding |
| UniProt | Rho-binding domain | Binds GTP-bound RHOA |
| GO Biological Process | Negative regulation of stress fiber assembly | Cytoskeletal regulation |
| GO Molecular Function | Rho GTPase binding | Signal transduction |

**Domain Analysis**: RHPN1 has a simple domain architecture with a PDZ domain for protein-protein interactions and a Rho-binding domain for GTPase binding. PDZ domains are typically found in scaffolding proteins at the plasma membrane or cytoskeleton, not in the nucleus. The domain architecture is consistent with a cytoplasmic signaling adaptor function. Domain score: 4/10.

### 8. PPI Network Analysis

| Partner | Context | Notes |
|---------|---------|-------|
| RHOA (GTP-bound) | Rho signaling | Cytosolic/membrane GTPase |
| ROPN1 | Rhophilin associated tail protein | PDZ-mediated interaction |
| CEP70 | Centrosomal protein | Centrosome |
| GOLGA2 | Golgi apparatus protein | Golgi |
| LMNA | Lamin A (nuclear envelope) | Nuclear periphery -- but not nucleoplasm |
| GFAP | Glial fibrillary acidic protein | Intermediate filament |

**PPI Assessment**: RHPN1 interaction partners are primarily cytoskeletal and membrane-associated proteins. The interaction with LMNA (nuclear lamin) is the closest connection to the nucleus, but lamins are nuclear envelope proteins, not nucleoplasmic proteins. PPI score: 3/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | GO-CC + HPA + COMPARTMENTS + predicted features | Cytosolic | Multi-source consistent |
| Function | Literature + GO | Rho effector, stress fiber regulation | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database cytosol localization consistency: +0.5
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. No established nuclear localization -- primary annotation is cytosol
2. No NLS predicted; no DNA-binding domains; no chromatin-related function
3. Domain architecture (PDZ + Rho-binding) is typical of membrane/cytosolic scaffolding proteins
4. All characterized functions are cytoplasmic (Rho signaling, stress fiber regulation)
5. Extremely novel (PubMed <=20) but novelty cannot compensate for non-nuclear localization

**Why Previous Rejection Was Likely Correct**:
The previous rejection was likely correct. RHPN1 is a cytoplasmic Rho effector protein with a PDZ domain -- a canonical membrane/cytosolic scaffolding architecture. While one interaction partner (LMNA) is at the nuclear envelope, this does not make RHPN1 a nuclear protein.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RHPN1 fails the nuclear localization criterion (score 1/10, threshold <=3). The protein is a cytosolic Rho GTPase effector with a PDZ domain, consistent with membrane/cytosolic scaffolding function. Nuclear score <=3 triggers automatic REJECTED status.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCX5
- HPA: https://www.proteinatlas.org/ENSG00000158106-RHPN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RHPN1%22+OR+%22rhophilin%22
- COMPARTMENTS: https://compartments.jensenlab.org/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
