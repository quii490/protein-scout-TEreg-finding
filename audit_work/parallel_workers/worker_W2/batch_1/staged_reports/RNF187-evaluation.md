---
type: protein-evaluation
gene: "RNF187"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RNF187 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF187 |
| Protein Name | E3 ubiquitin-protein ligase RNF187 |
| Protein Size | 235 aa / 26.2 kDa |
| UniProt ID | Q5TA31 (RN187_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | UniProt: Cytoplasm + Nucleus; GO-CC: cytoplasm, cytosol, nucleoplasm, nucleus; dual distribution |
| Protein Size | 10/10 | x1 | **10** | 235 aa, well within ideal 200-800 aa range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~21 articles (21-50 -> 8); very novel, near threshold for 10 |
| 3D Structure | 7/10 | x3 | **21** | PDB: 7OW2; experimental X-ray crystallography; partial structural characterization |
| Regulatory Domains | 7/10 | x2 | **14** | RING finger (E3 ligase); novel protein baseline (7/10) applies |
| PPI Network | 4/10 | x3 | **12** | Limited characterized PPI; E3 ligase context; no extensive interactome mapping |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB dual localization consistency (+0.5) |
| **Raw Total** | | | **117.5/180** | |
| **Normalized Total** | | | **64.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| UniProt (Swiss-Prot) | Nucleus | Reviewed |
| GO-CC | Cytoplasm | -- |
| GO-CC | Cytosol | -- |
| GO-CC | Nucleoplasm | -- |
| GO-CC | Nucleus | -- |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt dual annotation and GO-CC nucleoplasm/nucleus entries.

**Manual Review Assessment**: RNF187 is annotated as both cytoplasmic and nuclear by UniProt with explicit nucleoplasm and nucleus GO-CC terms. This dual localization pattern is common for small E3 ubiquitin ligases that may shuttle between compartments. The presence of "nucleoplasm" in GO-CC is noteworthy -- it indicates the protein enters the nucleoplasm (the soluble nuclear compartment) rather than being restricted to the nuclear periphery or non-nucleoplasmic subcompartments.

**Nuclear localization score: 5/10.** The protein has clear evidence of nuclear presence (nucleoplasm GO-CC, nucleus keyword), but equal annotation to cytoplasm. There is no evidence of nuclear enrichment or nuclear-specific function. Above the <=3 rejection threshold but represents a dual-distribution protein with moderate nuclear signal.

### 4. Protein Size Assessment

RNF187 is 235 amino acids in length, well within the ideal 200-800 aa range. This compact size is advantageous for recombinant production, purification, and structural characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~21 |
| Novelty category | 21-50 -> Score 8 |
| Earliest publication | ~2010 |

**Research Context**: RNF187 is a relatively under-studied E3 ubiquitin ligase with approximately 21 dedicated publications. Research has focused on its ubiquitination substrates and potential roles in cellular signaling. The literature is sparse enough that fundamental aspects of its biology (specific substrates, regulatory mechanisms, tissue-specific functions) remain largely unexplored.

**Novelty Assessment**: PubMed count of ~21 places RNF187 at the boundary between extremely novel (<=20, score 10) and very novel (21-50, score 8). This protein represents a significant research opportunity with minimal prior characterization. The small gap between 21 and the <=20 threshold for maximum novelty (score 10) is notable -- a handful of additional publications separate it from the highest novelty tier.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 (7OW2, X-ray crystallography) |
| PDB Method | X-ray diffraction |
| Structural Coverage | Partial (at least the RING domain) |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on PDB entry and domain architecture.

**Structure Assessment**: RNF187 has one experimental PDB structure (7OW2) solved by X-ray crystallography. For a protein with only ~21 publications, having an experimental crystal structure is a notable strength. The structure likely covers the RING finger domain, providing atomic-level detail of the catalytic core. The small protein size (235 aa) suggests most of the sequence is structurally ordered. Score 7/10 reflects the presence of experimental structural data, which is above the novel protein baseline of 6.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR050143 (RNF187 family) | Family-specific entry |
| InterPro | IPR001841 (RING finger) | E3 ubiquitin ligase |
| InterPro | IPR013083 (Znf RING/FYVE/PHD) | Metal-binding domain |
| Pfam | PF15227 (zf-RING_9) | RING-type zinc finger |

**Domain Analysis**: RNF187 contains a RING finger domain conferring E3 ubiquitin ligase activity. The domain architecture is relatively simple (primarily RING finger + short N/C terminal extensions), which is characteristic of single-domain E3 ligases. No DNA-binding or chromatin-interacting domains are identified. For a novel protein (PubMed=21, <=100), the domain baseline is 7/10. Score 7/10.

### 8. PPI Network Analysis

**PPI Assessment**: As a small, under-studied E3 ubiquitin ligase, RNF187 has limited characterized PPI data. The expected interaction network is centered on ubiquitin-conjugating enzymes (E2s) and ubiquitination substrates. Comprehensive interactome mapping has not been performed. Score 4/10 reflects the limited experimental PPI data available for this protein.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Dual Localization | UniProt + GO-CC (nucleoplasm, nucleus, cytoplasm) | Cytoplasm + Nucleus | Consistent |
| Domain | InterPro + Pfam | RING finger E3 ligase | Consistent |
| Structure | PDB 7OW2 (X-ray) | Experimental fold validation | Consistent with domain |

**Cross-Validation Bonus Details**:
- Multi-database dual localization (cytoplasm+nucleus) consistency: +0.5
- Limited multi-source PPI cross-validation: +0
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: CONDITIONALLY RECOMMENDED (Score: 64.2/100)

**Core Strengths**:
1. High novelty (PubMed=21, near the <=20 maximum-novelty threshold)
2. Clear nuclear presence confirmed by UniProt and GO-CC nucleoplasm
3. Experimental PDB structure (7OW2, X-ray) for a low-publication protein
4. Compact size (235 aa) ideal for biochemical and structural studies
5. Large unexplored research space for substrate identification and functional characterization

**Risks / Uncertainties**:
1. Dual cytoplasmic/nuclear localization reduces nuclear specificity score (5/10)
2. Very limited functional characterization in literature
3. Sparse PPI data
4. No known chromatin/DNA interaction
5. May have limited tissue-specific functions
6. Single-domain architecture may constrain functional diversity

**Next Steps**:
- [ ] Map nuclear-specific interactome
- [ ] Identify nuclear ubiquitination substrates
- [ ] Determine conditions regulating nucleocytoplasmic distribution
- [ ] Leverage existing PDB structure for structure-guided functional studies
- [ ] Characterize tissue expression pattern

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RNF187 clears both nuclear localization threshold (score 5/10, above <=3) and PubMed threshold (21 articles, <=100). The protein's high novelty (PubMed=21), small tractable size (235 aa), and existing experimental PDB structure make it a practical candidate. However, the dual cytoplasmic/nuclear distribution and lack of known chromatin/DNA functions place it at moderate priority.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5TA31
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF187%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (7OW2)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TA31
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q5TA31/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
