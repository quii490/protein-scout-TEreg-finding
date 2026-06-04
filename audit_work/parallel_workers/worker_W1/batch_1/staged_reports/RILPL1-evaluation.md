---
type: protein-evaluation
gene: "RILPL1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RILPL1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RILPL1 / GOSPEL (GAPDH competitor of SIAH protein enhances life), Rab-interacting lysosomal-like protein 1 |
| Protein Name | RILP-like protein 1 |
| Protein Size | ~407 aa |
| UniProt ID | Q5EBL4 (RIPL1_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (previously listed in garbage reports) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 2/10 | x4 | **8** | Cytosol, centrosome, cilium (primary); HPA detects nucleoplasm (minor); no established nuclear function |
| Protein Size | 10/10 | x1 | **10** | ~407 aa, within ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~35-45 articles (21-40 -> 8) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold prediction only; no PDB; predicted coiled-coil regions |
| Regulatory Domains | 3/10 | x2 | **6** | RILP homology domain; no DNA-binding domains; ciliary transport |
| PPI Network | 4/10 | x3 | **12** | GAPDH (cytosolic sequestration), RAB10 (ciliary), LRRK2 pathway |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB cytosolic/centrosomal localization consistency (+0.5) |
| **Raw Total** | | | **88.5/180** | |
| **Normalized Total** | | | **49.2/100** | |

### 3. Nuclear Localization Evidence -- FAILS THRESHOLD

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm, cytosol | Experimental (PMID:14668488) |
| UniProt | Cytoskeleton, microtubule organizing center, centrosome | By similarity |
| UniProt | Cell projection, cilium | By similarity |
| HPA (IF) | Ciliary basal body, Nucleoplasm, Centrosome, Cilium, Plasma membrane | IF-based |
| GO-CC | Centrosome | -- |
| GO-CC | Cilium | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RILPL1 is a complex case. The protein has multiple annotated subcellular locations:

- Primary UniProt annotation: Cytoplasm, cytosol (experimental evidence)
- HPA detects nucleoplasm signal -- but this is one of several locations (also ciliary basal body, centrosome, cilium, plasma membrane)
- The protein's main characterized functions are cytoplasmic/ciliary: (1) sequestering GAPDH in the cytosol to prevent its apoptotic nuclear translocation; (2) regulating ciliogenesis via RAB10 binding after LRRK2 phosphorylation

The HPA nucleoplasm detection is noteworthy but must be evaluated in context. The protein's experimentally validated primary function (GAPDH sequestration) occurs in the cytosol -- RILPL1 keeps GAPDH OUT of the nucleus. The ciliary functions are also non-nuclear. HPA nucleoplasm signal may represent a minor pool or detection artifact.

**Nuclear localization score: 2/10. RULE: Nuclear <=3 -> REJECTED.** The HPA nucleoplasm detection provides some evidence, but the protein's primary localization and characterized functions are cytoplasmic/ciliary. The nucleoplasm signal is insufficient to overcome the threshold.

### 4. Protein Size Assessment

RILPL1 is approximately 407 amino acids, within the ideal range. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~35-45 |
| Novelty category | 21-40 -> 8 (or 41-60 -> 6) |

**Research Context**: RILPL1 has gained attention in recent years due to its role in the LRRK2 Parkinson's disease pathway. The protein is a RAB10 effector that mediates ciliogenesis inhibition upon LRRK2-mediated RAB10 phosphorylation. Earlier work identified RILPL1 (as GOSPEL) as a neuroprotective protein that binds GAPDH. The literature is growing but still relatively modest.

**Novelty Assessment**: PubMed count estimated at 35-45 articles. Most publications are from the last 5-8 years. Score 8/10 reflects moderate novelty in the 21-40 range (or 6/10 at 41-60).

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Features | Predicted coiled-coil regions; RILP homology domain |

**Structure Assessment**: RILPL1 is predicted to contain coiled-coil regions and a RILP homology domain. The structure is likely elongated and may have flexible/disordered regions. AlphaFold prediction quality for coiled-coil proteins can be variable. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | RILP homology domain | Rab-interacting lysosomal protein family |
| Function | GAPDH binding | Cytosolic sequestration, neuroprotection |
| Function | RAB10 binding | Ciliary transport, ciliogenesis regulation |

**Domain Analysis**: RILPL1 contains a RILP (Rab-interacting lysosomal protein) homology domain, which mediates interactions with Rab GTPases. There are no DNA-binding domains, chromatin-binding domains, transcription factor domains, or other nuclear regulatory domains. Domain score: 3/10.

### 8. PPI Network Analysis

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| GAPDH | Cytosolic sequestration | Prevents GAPDH nuclear translocation and apoptosis |
| RAB10 | Ciliary transport | LRRK2-mediated phosphorylation; ciliogenesis inhibition |
| LRRK2 | Parkinson's disease pathway | Kinase that phosphorylates RAB10 |
| CMIP | Interaction reported | Function unclear |
| MOV10 | Interaction reported | RNA helicase |

**PPI Assessment**: RILPL1 has notable interactions. The GAPDH interaction is functionally significant -- RILPL1 actively keeps GAPDH in the cytosol, preventing its pro-apoptotic nuclear translocation. This is an anti-nuclear function. The RAB10 interaction mediates ciliary regulation. PPI score: 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA | Cytosol, centrosome, cilium (+ nucleoplasm minor) | Partially consistent |
| Function | Literature + GO | GAPDH sequestration, ciliary regulation | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database cytosol/centrosomal localization consistency: +0.5
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED (borderline case)

**Core Reasons for Rejection**:
1. Nuclear localization insufficient (score 2/10, threshold <=3 triggers rejection)
2. Primary localization is cytosol with experimental validation (PMID:14668488)
3. Characterized functions are cytoplasmic (GAPDH sequestration) and ciliary (ciliogenesis)
4. HPA nucleoplasm signal is minor and not supported by other databases
5. No DNA-binding domains or nuclear-specific functions

**Borderline Nature**: RILPL1 is a borderline case. The HPA nucleoplasm detection provides some nuclear evidence, and the interaction with MOV10 (RNA helicase with nuclear functions) is suggestive. However, the overwhelming evidence places RILPL1 in cytosolic and ciliary compartments. A higher-resolution IF analysis might provide more definitive subcellular localization data.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RILPL1 fails the nuclear localization criterion (score 2/10, threshold <=3). The protein is primarily cytosolic and ciliary with minor HPA nucleoplasm signal. Nuclear score <=3 triggers automatic REJECTED status. NOTE: This is a borderline case. If higher-quality IF data becomes available showing stronger nuclear localization, re-evaluation may be warranted.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5EBL4
- HPA: https://www.proteinatlas.org/ (RILPL1)
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RILPL1%22+OR+%22GOSPEL%22
- BioGRID: https://thebiogrid.org/ (RILPL1 interactions)
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
