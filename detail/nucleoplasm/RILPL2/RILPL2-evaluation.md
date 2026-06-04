---
type: protein-evaluation
gene: "RILPL2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RILPL2 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RILPL2 / Rab-interacting lysosomal protein-like 2, p40phox-binding protein |
| Protein Name | RILP-like protein 2 |
| Protein Size | ~204 aa |
| UniProt ID | Q969X0 (RIPL2_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | Cytosol, centrosome, cilium (primary); no established nuclear function |
| Protein Size | 4/10 | x1 | **4** | ~204 aa, at lower limit of workable range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~30-40 articles (21-40 -> 8) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold prediction only; no PDB; small protein |
| Regulatory Domains | 3/10 | x2 | **6** | RILP homology domain; myosin-Va binding; ciliary transport |
| PPI Network | 4/10 | x3 | **12** | Myosin Va, RAB10, LRRK2 pathway; Rac1, PAK1 signaling |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB cytosolic/centrosomal consistency (+0.5) |
| **Raw Total** | | | **78.5/180** | |
| **Normalized Total** | | | **43.6/100** | |

### 3. Nuclear Localization Evidence -- FAILS THRESHOLD

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm, cytosol | Reviewed, annotation score 5/5 |
| UniProt | Cytoskeleton, microtubule organizing center, centrosome | Reviewed |
| UniProt | Cell projection, cilium | Reviewed |
| GO-CC | Cytoplasm (GO:0005737) | Curated |
| GO-CC | Cytosol (GO:0005829) | Curated |
| GO-CC | Centrosome (GO:0005813) | Curated |
| GO-CC | Cilium (GO:0005929) | Curated |
| GO-CC | Ciliary basal body (GO:0036064) | Curated |
| GO-CC | Membrane (GO:0016020) | Curated |
| Any nuclear source | NONE | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RILPL2 is a cytosolic and ciliary protein with no credible nuclear localization evidence. Key findings:

- UniProt (Swiss-Prot, annotation score 5/5): Cytoplasm, cytosol, centrosome, cilium -- no nuclear annotation
- GO-CC: 7 cellular component terms, none of which are nuclear
- The protein is involved in cell shape maintenance, neuronal morphogenesis (dendritic spine formation), and protein transport away from primary cilia
- RILPL2 acts via activation of RAC1 and PAK1 -- cytoplasmic signaling pathways
- The protein interacts with Myosin Va for cargo transport -- a cytoplasmic motor protein

Unlike RILPL1, which has a minor HPA nucleoplasm signal, RILPL2 has NO nuclear localization evidence from any source. The annotation score of 5/5 on UniProt indicates the highest level of curation confidence for the non-nuclear annotations.

**Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED.**

### 4. Protein Size Assessment

RILPL2 is approximately 204 amino acids, at the lower boundary of the workable range. Small proteins can present challenges for some experimental approaches. Size score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~30-40 |
| Novelty category | 21-40 -> Score 8 |

**Research Context**: RILPL2 research has grown in recent years, particularly in the context of the LRRK2 Parkinson's disease pathway. The protein functions as a RAB10 effector that, upon LRRK2 phosphorylation, sequesters Myosin Va and blocks ciliogenesis. Additional studies have examined RILPL2 in cancer (cervical squamous cell carcinoma, breast cancer, NSCLC). The gene is also involved in migrasome transport.

**Novelty Assessment**: PubMed count of ~30-40 places RILPL2 in the 21-40 range (score 8). Research is growing due to the Parkinson's disease connection but remains moderate.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Features | Small protein with RILP homology domain |

**Structure Assessment**: RILPL2 is a relatively small protein with a RILP homology domain. The structure is likely to include coiled-coil regions for protein-protein interactions. AlphaFold prediction quality for a small protein of this type should be reasonable. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | RILP homology domain | Rab-interacting lysosomal protein family |
| Function | Myosin Va binding | Cargo transport, ciliogenesis |
| Function | RAB10 binding | Ciliary regulation |

**Domain Analysis**: RILPL2 contains a RILP homology domain that mediates interactions with Rab GTPases. No DNA-binding domains, chromatin-binding domains, or transcription factor domains are present. Domain score: 3/10.

### 8. PPI Network Analysis

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| Myosin Va | Cargo transport | Sequestered by RILPL2 during ciliogenesis blockade |
| RAB10 | Ciliary regulation | LRRK2-phosphorylated; binds RILPL2 |
| Rac1 | Cytoskeletal signaling | Cell shape regulation |
| PAK1 | Cytoskeletal signaling | Downstream kinase |
| LRRK2 | Parkinson's disease | Kinase pathway |
| TUBB3 | Microtubule | Cytoskeletal interaction |
| HEXD | Interaction reported | Function unclear |

**PPI Assessment**: RILPL2 has a network of interactions centered on cytoskeletal and ciliary regulation. The Myosin Va interaction is functionally significant for ciliogenesis. All interaction partners are cytoplasmic, membrane, or cytoskeletal proteins -- none are nuclear. PPI score: 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + GO-CC | Cytosol, centrosome, cilium | Multi-source consistent |
| Function | Literature + GO | Ciliary transport, cell shape | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database cytosol/centrosomal localization consistency (UniProt annotation score 5/5): +0.5
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. Zero credible nuclear localization evidence -- complete absence of nuclear in 7 GO-CC terms
2. UniProt annotation score 5/5 for cytoplasmic/centrosomal/ciliary localization
3. All characterized functions are cytoplasmic (Rac1/PAK1 signaling) or ciliary (ciliogenesis blockade)
4. All interaction partners are cytoplasmic/membrane proteins
5. Moderately novel (PubMed ~30-40) but novelty cannot compensate for non-nuclear localization

**Why Previous Rejection Was Likely Correct**:
The original rejection of RILPL2 was correct. The protein has the highest confidence annotation (score 5/5) for exclusively non-nuclear localization. There is no evidence from any database supporting nuclear localization.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RILPL2 fails the nuclear localization criterion (score 0/10, threshold <=3). The protein is exclusively cytosolic, centrosomal, and ciliary with UniProt annotation score 5/5. Nuclear score <=3 triggers automatic REJECTED status.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q969X0
- HPA Subcellular: https://v21.proteinatlas.org/ENSG00000150977-RILPL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RILPL2%22
- FACTA: https://www.nactem.ac.uk/facta/ (RILPL2)
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
