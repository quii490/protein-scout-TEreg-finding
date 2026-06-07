---
type: protein-evaluation
gene: "RWDD1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RWDD1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RWDD1 / CGI-24, PTD013, DFRP2 |
| Protein Name | RWD Domain Containing 1 (DRG family-regulatory protein 2) |
| Protein Size | 243 aa (isoform a); 147 aa (isoform b) |
| UniProt ID | Q9H446 (RWDD1_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | AR coactivator with nuclear functional role; primarily cytoplasmic localization in mammalian cells |
| Protein Size | 10/10 | x1 | **10** | 243 aa, well within ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~30 articles; moderately novel (21-40 -> 8) |
| 3D Structure | 4/10 | x3 | **12** | Intrinsically unstructured protein; AlphaFold likely low confidence; no PDB entries |
| Regulatory Domains | 5/10 | x2 | **10** | RWD domain (protein interaction); AR coactivator function; sumoylation site |
| PPI Network | 4/10 | x3 | **12** | DRG2 interaction confirmed; AR/GR interaction; limited overall network |
| Cross-Validation Bonus | -- | -- | **+0.5** | AR + GR coactivation consensus (+0.5) |
| **Raw Total** | | | **100.5/180** | |
| **Normalized Total** | | | **55.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| Xenbase (Xenopus) | Nucleus | Developmental model |
| OMIM (Kang et al., 2008) | Cytoplasm (GFP-tagged, 293T cells) | Experimental -- does not translocate to nucleus upon testosterone |
| UniProt (Rat) | Cytoplasm | Experimental |
| Grotsch et al., 2012 | Cytosol (urethral epithelium, mouse) | Experimental |
| OMIM (functional) | Transcription factor activity | Inferred from AR coactivation |

**HPA IF Status**: HPA IF data not available for this protein.

**Manual Review Assessment**: RWDD1 presents a complex localization picture. While annotated as a transcription factor/AR coactivator by OMIM (implying nuclear function), the majority of experimental evidence in mammalian cells places it in the cytoplasm. Xenopus data reports nuclear localization, but this may be species- or developmental stage-specific. The protein functions as a coactivator for androgen receptor (AR) and glucocorticoid receptor (GR) -- nuclear receptors whose transcriptional activity occurs in the nucleus. However, RWDD1 may exert its coactivator function indirectly (e.g., through cytoplasmic modulation of receptor trafficking or stability) rather than through direct nuclear residence. It also protects DRG2 (a cytoplasmic protein) from degradation.

**Key ambiguity**: Does RWDD1 need to be in the nucleus to function as an AR coactivator, or does it act from the cytoplasm? The published data lean toward cytoplasmic action. Score 4/10 reflects some evidence for nuclear relevance (AR coactivator function) but predominantly cytoplasmic localization in mammalian cells. Above the ≤3 rejection threshold.

### 4. Protein Size Assessment

RWDD1 is 243 amino acids (isoform a), well within the ideal 200-800 aa range. Given its classification as an intrinsically unstructured protein (IUP), its small size is advantageous -- smaller IDPs are easier to characterize than large ones. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~25-35 |
| Novelty category | 21-40 -> Score 8 |

RWDD1 has been studied primarily in the context of androgen receptor signaling and as a DRG2-interacting protein. Key publications include characterization of its AR coactivator function and its role in protecting DRG2 from proteolytic degradation. Research is limited but not extremely sparse. Some publications on the broader RWD domain family and sumoylation biology also reference RWDD1. Score 8/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (predicted low confidence) |
| PDB Entries | 0 |
| Protein Class | Intrinsically unstructured protein (IUP) |

RWDD1 is a member of the intrinsically unstructured protein family, sharing high sequence similarity with yeast Gir2. It is sensitive to limited protease digestion and migrates at a higher apparent molecular weight than predicted (~27 kDa), consistent with a partially unfolded state. As an IUP, it is unlikely to have a single well-defined 3D structure, which limits the utility of AlphaFold predictions. Score 4/10 reflects the structural challenges inherent to IDPs rather than poor prediction quality per se.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | RWD domain (IPR006575) | Protein-protein interaction; found in ubiquitin-conjugating enzymes and signaling proteins |
| Pfam | RWD domain (PF05773) | Named after RING finger, WD repeat, DEAD-like helicases |
| Post-translational | Sumoylation site (K90) | Enhances transcriptional repression activity (shown in Urechis) |

The RWD domain is the sole annotated domain. While it mediates protein-protein interactions, it does not directly confer DNA-binding, chromatin-modifying, or other canonical regulatory activities. The sumoylation site at K90 has been shown to enhance transcriptional repression in invertebrate models, suggesting that post-translational modification may modulate RWDD1's regulatory function. Score 5/10 reflects domain-mediated interaction capabilities with limited direct regulatory function.

### 8. PPI Network Analysis

| Partner | Context | Evidence |
|---------|---------|----------|
| AR (Androgen Receptor) | Coactivation | Direct interaction via LBD |
| GR (Glucocorticoid Receptor) | Coactivation | Functional enhancement |
| DRG2 | Protection from degradation | Protein stabilization |

RWDD1 has a focused but functionally relevant interaction network centered on nuclear receptor coactivation and DRG2 stabilization. The interaction with AR is direct (via the C-terminal ligand-binding domain), and the coactivation effect is independent of the AF2 hydrophobic pocket -- a unique mechanism. The PPI network is limited in scope but mechanistically well-defined. Score 4/10 reflects functional relevance of interactions but limited overall network breadth.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| AR Coactivation | OMIM + UniProt + Literature | AR/GR coactivator | Consistent |
| Localization | OMIM (mammalian) + UniProt (rat) | Primarily cytoplasmic | Consistent across mammalian data |
| DRG2 Protection | Literature | Functional interaction | Validated |

**Cross-Validation Bonus Details**:
- AR + GR coactivation consensus from multiple sources: +0.5
- Limited structural cross-validation (IUP, no PDB): +0
- Limited PPI cross-validation: +0
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: CONDITIONALLY RECOMMENDED (Score: 55.8/100)

**Core Strengths**:
1. AR/GR coactivator function provides nuclear functional relevance
2. Small protein size (243 aa) ideal for experimental characterization
3. Unique coactivation mechanism (AF2-independent) offers mechanistic novelty
4. Intrinsically unstructured nature may enable discovery of disorder-to-order transitions
5. RWD domain mediates specific protein-protein interactions

**Risks / Uncertainties**:
1. Localization is predominantly cytoplasmic in mammalian cells -- nuclear relevance is functional, not physical (score 4/10)
2. As an IDP, structural characterization is challenging
3. Limited PPI network scope
4. Species-dependent localization differences (Xenopus nuclear vs. mammalian cytoplasmic)
5. Coactivator function may be indirect (e.g., affecting receptor trafficking rather than direct transcriptional regulation)

**Next Steps**:
- [ ] Determine whether RWDD1 enters the nucleus under specific conditions (cell type, stimulus, cell cycle)
- [ ] Characterize the mechanism of AF2-independent AR coactivation
- [ ] Investigate whether sumoylation at K90 affects subcellular localization
- [ ] Profile disorder-to-order transitions upon partner binding

### 11. Decision

**FINAL DECISION**: NOT REJECTED. Nuclear localization score 4/10 is above the ≤3 rejection threshold, and PubMed count (~25-35) is below the >100 rejection threshold. However, the predominantly cytoplasmic localization pattern and IDP structural nature result in a lower priority score (55.8/100). RWDD1 is a viable candidate but should be prioritized below genes with stronger nuclear enrichment and higher structural tractability. The AF2-independent AR coactivation mechanism is unique and may represent a novel regulatory paradigm worth investigating.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H446
- OMIM: https://www.omim.org/entry/620844
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RWDD1
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RWDD1
- Note: Harvest packet not available; data compiled from UniProt, OMIM, and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H446 |
| SMART | SM00591; |
| UniProt Domain [FT] | DOMAIN 10..114; /note="RWD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00179" |
| InterPro | IPR040213;IPR006575;IPR016135;IPR032378; |
| Pfam | PF16543;PF05773; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111832-RWDD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DRG1 | Intact, Biogrid | true |
| DRG2 | Intact, Biogrid | true |
| DNAJC1 | Biogrid | false |
| DNAJC2 | Biogrid | false |
| HSPA14 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
