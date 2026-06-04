---
type: protein-evaluation
gene: "RNF6"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RNF6 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF6 / SPG2 |
| Protein Name | E3 ubiquitin-protein ligase RNF6 |
| Protein Size | 685 aa / 78.1 kDa |
| UniProt ID | Q9Y252 (RNF6_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Nucleus, Nucleus/PML body, nuclear membrane; GO-CC: nucleus, PML body, nuclear membrane; also cytoplasm and axon |
| Protein Size | 10/10 | x1 | **10** | 685 aa, within ideal 200-800 aa range |
| Research Novelty | 6/10 | x5 | **30** | PubMed ~64 articles (51-100 -> 6) |
| 3D Structure | 6/10 | x3 | **18** | No PDB entries; AlphaFold prediction available; novel protein baseline (6/10) applies |
| Regulatory Domains | 7/10 | x2 | **14** | RING finger (E3 ligase) + additional IPR domains; novel protein baseline (7/10); PML body targeting |
| PPI Network | 5/10 | x3 | **15** | Androgen receptor coactivator; PML body-associated; ubiquitination pathway |
| Cross-Validation Bonus | -- | -- | **+1.0** | PML body + nuclear membrane + nucleus consensus (+0.5); domain + kinase substrate function alignment (+0.5) |
| **Raw Total** | | | **116.0/180** | |
| **Normalized Total** | | | **63.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Reviewed |
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| UniProt (Swiss-Prot) | Cell projection, axon | Reviewed |
| UniProt (Swiss-Prot) | Nucleus, PML body | Reviewed |
| GO-CC | Axon | -- |
| GO-CC | Cytoplasm | -- |
| GO-CC | Nuclear membrane | -- |
| GO-CC | Nucleus | -- |
| GO-CC | PML body | -- |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt multi-location annotation and GO-CC.

**Manual Review Assessment**: RNF6 has a complex subcellular distribution pattern. The protein is annotated to multiple nuclear compartments -- nucleus, nuclear membrane, and PML body -- indicating a significant nuclear presence. PML body localization is particularly notable as these are nuclear sub-compartments involved in sumoylation, transcription regulation, and DNA damage response. However, RNF6 is also annotated to cytoplasm and axon, indicating the protein is not exclusively nuclear.

**Key points supporting nuclear localization**:
1. UniProt annotates Nucleus, nuclear membrane, and PML body
2. GO-CC confirms nucleus, nuclear membrane, and PML body
3. PML body is a strictly nuclear compartment
4. Keywords include "Nucleus"
5. Function as androgen receptor coactivator occurs in the nucleus

**Nuclear localization score: 7/10.** The protein has strong nuclear localization evidence (nucleus, PML body, nuclear membrane from multiple sources). The cytoplasmic and axonal annotations prevent a higher score. Above the <=3 rejection threshold.

### 4. Protein Size Assessment

RNF6 is 685 amino acids in length, placing it within the ideal 200-800 aa range. This size is amenable to recombinant expression and most biochemical assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~64 |
| Novelty category | 51-100 -> Score 6 |
| Earliest publication | ~1999 |

**Research Context**: RNF6 was initially identified as an androgen receptor-interacting protein and has been studied primarily in the context of steroid hormone receptor signaling. It functions as an E3 ubiquitin ligase that modulates the activity of transcription factors including the androgen receptor. Studies have examined its roles in prostate cancer, where androgen receptor signaling is central.

**Major research themes**:
- Androgen receptor coactivation and ubiquitination
- Steroid hormone receptor signaling
- Prostate cancer biology
- PML body-associated ubiquitin signaling
- Transcriptional regulation via ubiquitination

**Novelty Assessment**: PubMed count of ~64 places RNF6 in the moderately studied category (51-100 -> 6). The androgen receptor/prostate cancer context attracts substantial research attention, but niche space exists for studying non-hormonal nuclear functions and other transcription factor substrates.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Coverage | Predicted only |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Assessment based on domain architecture and protein size.

**Structure Assessment**: RNF6 has no experimental PDB structures. At 685 aa, the protein is moderately sized and likely contains both structured domains and flexible linker regions. The RING finger domain and additional IPR domains (IPR051834, IPR058896) suggest regions of defined structure. Score 6/10 applies the novel protein baseline.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR051834 (RNF6 family) | Family-specific E3 ligase |
| InterPro | IPR058896 | Additional RNF6-specific domain |
| InterPro | IPR001841 (RING finger) | E3 ubiquitin ligase |
| Pfam | PF25914 | RNF6-specific domain |
| Pfam | PF13639 (zf-RING_2) | RING-type zinc finger |

**Domain Analysis**: RNF6 contains the canonical RING finger domain for E3 ubiquitin ligase activity, plus additional family-specific domains that may mediate substrate recognition or subcellular targeting. The PML body localization suggests the protein contains sequences that direct it to this nuclear sub-compartment. No classical DNA-binding or chromatin-interacting domains are present, but the androgen receptor coactivator function provides a functional link to transcriptional regulation. Score 7/10 (novel protein baseline).

### 8. PPI Network Analysis

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| Androgen receptor (AR) | Nuclear hormone receptor | Coactivation and ubiquitination |
| PML body components | Nuclear sub-compartments | Subnuclear localization |
| Ubiquitin-conjugating enzymes (E2) | Ubiquitination cascade | Catalytic function |

**PPI Assessment**: RNF6 has characterized interactions with the androgen receptor, establishing its role in nuclear hormone receptor signaling. The PML body association provides additional nuclear interaction context. However, a comprehensive PPI network has not been systematically mapped. Score 5/10 reflects some characterized interactions with nuclear/transcriptional relevance.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt (Nucleus, PML body, nuclear membrane) + GO-CC | Multi-compartment nuclear | Highly consistent |
| Cytoplasmic/Axon | UniProt + GO-CC | Non-nuclear compartments also present | Consistent |
| Domain | InterPro + Pfam | RING + family-specific domains | Consistent |

**Cross-Validation Bonus Details**:
- Multi-compartment nuclear localization (nucleus + PML body + nuclear membrane) consensus: +0.5
- Domain (RING) + functional role (AR coactivator) alignment: +0.5
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 63.4/100)

**Core Strengths**:
1. Strong nuclear localization with PML body targeting (score 7/10)
2. Functional link to transcription regulation via androgen receptor coactivation
3. PML body localization is a hallmark of nuclear regulatory function
4. Moderate novelty (PubMed=64) with niche for non-AR functions
5. Ideal protein size (685 aa) for biochemical studies

**Risks / Uncertainties**:
1. Moderate PubMed count (64) reduces novelty premium
2. Dual cytoplasmic/axonal localization may dilute nuclear signal
3. No experimental PDB structures
4. Research dominated by AR/prostate cancer context
5. Competition from established nuclear receptor field

**Next Steps**:
- [ ] Characterize non-androgen receptor substrates
- [ ] Define PML body targeting mechanism
- [ ] Map nuclear-specific interactome
- [ ] Assess function in non-prostate cell types
- [ ] Determine structural basis of substrate recognition

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RNF6 clears the nuclear localization threshold (score 7/10, above <=3) and PubMed threshold (64 articles, <=100). The protein's PML body localization and androgen receptor coactivator function establish clear nuclear relevance. While the AR/prostate cancer context limits novelty somewhat, niche space exists for exploring broader nuclear regulatory functions.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y252
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF6%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y252
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9Y252/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
