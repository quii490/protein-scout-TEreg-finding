---
type: protein-evaluation
gene: "RHOQ"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RHOQ -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RHOQ / TC10, Ras-like protein TC10, ras homolog family member Q |
| Protein Name | Rho-related GTP-binding protein RhoQ |
| Protein Size | 205 aa |
| UniProt ID | P17081 (RHOQ_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | Cytoplasm, plasma membrane, actin filament, Golgi vesicle, membrane raft; no nuclear evidence |
| Protein Size | 4/10 | x1 | **4** | 205 aa, at lower limit of workable range |
| Research Novelty | 4/10 | x5 | **20** | PubMed ~80-100 articles (81-100 -> 2) |
| 3D Structure | 6/10 | x3 | **18** | PDB structures available (Rho family); AlphaFold prediction |
| Regulatory Domains | 5/10 | x2 | **10** | Small GTPase; GTP/GDP switching; membrane targeting via prenylation + palmitoylation |
| PPI Network | 6/10 | x3 | **18** | Multiple effector interactions (CDC42EP1-4, PARD6, EXO70, GOPC); well-characterized signaling |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold structural cross-validation (+0.5); Multi-DB localization consistency (+0.5) |
| **Raw Total** | | | **71.0/180** | |
| **Normalized Total** | | | **39.4/100** | |

### 3. Nuclear Localization Evidence -- CRITICAL FAIL

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| UniProt | Cell membrane; Lipid-anchor | Reviewed |
| UniProt | Actin filament | Reviewed |
| UniProt | Golgi-associated vesicle membrane | Reviewed |
| UniProt | Membrane raft | Reviewed |
| UniProt | Extracellular exosome | Reviewed |
| GO-CC | Cytoplasm (GO:0005737) | Curated |
| GO-CC | Plasma membrane (GO:0005886) | Curated |
| GO-CC | Actin filament (GO:0005884) | Curated |
| GO-CC | Golgi-associated vesicle membrane (GO:0030660) | Curated |
| GO-CC | Membrane raft (GO:0045121) | Curated |
| ANY NUCLEAR SOURCE | NONE | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RHOQ is a classical small GTPase of the Rho family, closely related to CDC42. Like all small GTPases, it functions at cellular membranes where it cycles between active GTP-bound and inactive GDP-bound states. Its subcellular localization is exclusively non-nuclear: cytoplasm, plasma membrane (via dual lipid anchors: palmitoylation and polyisoprenylation), actin filaments, Golgi-derived vesicles, membrane rafts, and exosomes. The protein is involved in epithelial cell polarization, filopodia formation, CFTR trafficking, and GLUT4 exocytosis -- all membrane/cytoplasmic processes. There is no nuclear localization signal, no DNA-binding domain, and no evidence of nuclear function. **Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED.**

### 4. Protein Size Assessment

RHOQ is 205 amino acids, at the lower boundary of the ideal workable range. Small GTPases of the Ras superfamily are typically around 200 aa and are well-characterized experimentally. Size score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~80-100 |
| Novelty category | 81-100 -> Score 2 |

**Research Context**: RHOQ/TC10 is a well-studied member of the Rho GTPase family. It has been characterized in the context of insulin signaling (GLUT4 translocation), cell polarity, cytoskeletal regulation, and membrane trafficking. The protein is not novel -- it belongs to one of the most extensively studied protein families in cell biology.

**Novelty Assessment**: With ~80-100 PubMed articles, RHOQ falls in the 81-100 range (score 2). The gene is not a novel target. Most aspects of its biochemistry, regulation, and function are well-characterized. Score 2/10 reflects the extensive existing literature.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| PDB Entries | Multiple (Rho family GTPases well-represented) |
| AlphaFold Prediction | Available |
| Structural Features | Canonical small GTPase fold; GTP/GDP binding pocket; switch I/II regions |

**Structure Assessment**: As a member of the extensively studied Rho GTPase family, RHOQ has a well-characterized structural fold. The canonical GTPase domain with its GTP/GDP binding pocket and conformational switch regions is well understood. Multiple PDB structures exist for closely related family members, and the AlphaFold prediction is expected to be of high quality. Score 6/10 reflects good structural understanding but not specifically for RHOQ itself.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | Small GTPase domain | GTP/GDP binding and hydrolysis |
| UniProt | Effector region (switch I) | Binds CDC42EP1-4, PARD6, EXO70, GOPC |
| UniProt | C-terminal CAAX box | Prenylation (geranylgeranylation) |
| UniProt | N-terminal palmitoylation sites | Membrane targeting |

**Domain Analysis**: RHOQ has the canonical small GTPase domain architecture: a GTP-binding/hydrolysis domain, effector-binding switch regions, and C-terminal lipid modification motifs for membrane targeting. The domain architecture is well-characterized and consistent with its function as a membrane-associated signaling switch. No regulatory domains typically associated with nuclear function (DNA-binding, chromatin-binding, transcription factor) are present. Domain score: 5/10.

### 8. PPI Network Analysis

| Partner | Context | Function |
|---------|---------|----------|
| CDC42EP1-4 | GTP-dependent effector binding | Actin cytoskeleton regulation |
| PARD6 family | Cell polarity complex | Epithelial polarization |
| EXO70 | Exocyst complex component | Vesicle trafficking |
| GOPC | Golgi-associated PDZ protein | Membrane trafficking |

**PPI Assessment**: RHOQ has a well-characterized set of effector interactions typical of Rho family GTPases. These interactions mediate its roles in cytoskeletal regulation, cell polarity, and membrane trafficking. None of the interaction partners are nuclear proteins. PPI score: 6/10 for well-characterized interactions but none relevant to nuclear biology.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + GO-CC + literature | Cytoplasm, membrane, actin, vesicles | Multi-source consistent |
| Structure | PDB (family) + AlphaFold | Canonical GTPase fold | Consistent |
| Function | Literature + GO | GTPase signaling | Well-characterized |

**Cross-Validation Bonus Details**:
- PDB (family) + AlphaFold structural cross-validation: +0.5
- Multi-database non-nuclear localization consistency: +0.5
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. Zero nuclear localization evidence -- classical membrane/cytoplasmic small GTPase
2. Protein function is exclusively in membrane/cytoplasmic signaling
3. Well-studied (PubMed ~80-100), low novelty
4. No domains associated with nuclear function
5. All interaction partners are cytoplasmic/membrane proteins

**Why Previous Rejection Was Correct**:
RHOQ is a small GTPase that functions at the plasma membrane and cytoplasmic vesicles. It has no connection to nuclear biology. The rejection was correct.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RHOQ fails the nuclear localization criterion (score 0/10, threshold <=3). The protein is a classical small GTPase of the Rho family that functions exclusively at cellular membranes and in the cytoplasm. Nuclear score <=3 triggers automatic REJECTED status.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P17081
- Wikipedia: https://en.wikipedia.org/wiki/RHOQ_(gene)
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RHOQ%22+OR+%22TC10%22
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
