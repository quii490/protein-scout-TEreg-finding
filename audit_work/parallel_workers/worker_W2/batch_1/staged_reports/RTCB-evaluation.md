---
type: protein-evaluation
gene: "RTCB"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RTCB -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTCB / C22orf28 |
| Protein Name | RNA-splicing ligase RTCB |
| Protein Size | 505 aa / 55.2 kDa |
| UniProt ID | Q9Y3I0 (RTCB_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | UniProt: Nucleus + Cytoplasm; GO-CC: nucleus, nucleoplasm, nuclear envelope + multiple cytoplasmic compartments; dual distribution |
| Protein Size | 10/10 | x1 | **10** | 505 aa, well within ideal 200-800 aa range |
| Research Novelty | REJECTED | x5 | **REJECTED** | PubMed ~107 articles (>100 -> automatic REJECTED) |
| 3D Structure | 10/10 | x3 | **30** | PDB: 7P3B, 8BTT, 8ODO, 8ODP, 8ORJ (5 structures); extensive experimental structural characterization |
| Regulatory Domains | 4/10 | x2 | **8** | RTCB family; RNA ligase; GTP-binding; no DNA/chromatin domains |
| PPI Network | 5/10 | x3 | **15** | tRNA-splicing ligase complex; RNA processing partners; TRPT1, archease |
| Cross-Validation Bonus | -- | -- | **+1.5** | Multi-PDB structural consistency (+0.5); dual localization multi-source consensus (+0.5); domain + enzymatic function alignment (+0.5) |
| **Raw Total** | | | **N/A** | Protein rejected -- scores are informational only |
| **Normalized Total** | | | **N/A** | Protein rejected -- scores are informational only |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Reviewed |
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| GO-CC | Catalytic complex | Curated |
| GO-CC | Cytoplasm | Curated |
| GO-CC | Cytosol | Curated |
| GO-CC | Endoplasmic reticulum membrane | Curated |
| GO-CC | Nuclear envelope | Curated |
| GO-CC | Nucleoplasm | Curated |
| GO-CC | Nucleus | Curated |
| GO-CC | tRNA-splicing ligase complex | Curated |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt and GO-CC.

**Manual Review Assessment**: RTCB has dual nuclear/cytoplasmic localization. UniProt annotates both Nucleus and Cytoplasm as subcellular locations. GO-CC shows a broad distribution across cellular compartments: nucleoplasm, nucleus, nuclear envelope (nuclear), plus cytoplasm, cytosol, endoplasmic reticulum membrane (cytoplasmic/extranuclear). The tRNA-splicing ligase complex localizes to both nucleus and cytoplasm as tRNA processing occurs in both compartments.

**Nuclear localization score: 4/10.** The protein has documented nuclear presence (nucleoplasm, nucleus), but it is equally annotated to multiple cytoplasmic compartments. The dual distribution pattern is consistent with an RNA processing enzyme that functions in both nucleus and cytoplasm. Score 4/10 reflects the nuclear+cytoplasmic distribution with no nuclear preference. This is above the <=3 rejection threshold, but the PubMed count independently disqualifies this protein.

### 4. PubMed Count -- FAILS THRESHOLD (REJECTED)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~107 |
| Rejection threshold | >100 |
| Earliest publication | ~2005 |

**PubMed Assessment**: With approximately 107 PubMed articles, RTCB exceeds the >100 threshold for automatic rejection. The protein has been extensively studied in the context of RNA repair, tRNA splicing, and the mechanism of RNA 2',3'-cyclic phosphate and 5'-OH ligation. RTCB is the catalytic subunit of the tRNA-splicing ligase complex and has been structurally characterized in multiple conformational states.

**RULE: PubMed >100 -> REJECTED.** This is an independent and sufficient rejection ground. The extensive literature means the protein is too crowded for novel discovery-focused research.

### 5. Research Context (Informational)

RTCB is a well-characterized RNA ligase that catalyzes the joining of 2',3'-cyclic phosphate and 5'-OH RNA termini. It functions as part of the tRNA-splicing ligase complex together with archease/TRPT1 and other cofactors. The reaction mechanism involves GTP-dependent activation followed by RNA ligation. RTCB also participates in the repair of spliced XBP1 mRNA during the unfolded protein response (UPR), linking it to endoplasmic reticulum stress signaling.

**Major research themes**:
- tRNA splicing and maturation
- RNA repair and ligation mechanisms
- XBP1 mRNA splicing in UPR
- RNA 2',3'-cyclic phosphate metabolism
- GTP-dependent enzymatic mechanism
- Structural biology of RNA ligation

**Note**: RTCB is an important and fascinating enzyme in RNA biology. The rejection is based on the >100 PubMed threshold for novel discovery-focused research, not on the protein's biological importance.

### 6. 3D Structure Analysis (Informational)

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 5 (7P3B, 8BTT, 8ODO, 8ODP, 8ORJ) |
| PDB Methods | X-ray crystallography, Cryo-EM |
| Structural Coverage | Extensive -- multiple conformational states, complex structures |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on extensive PDB entries.

**Structure Assessment**: RTCB has been extremely well characterized structurally, with 5 PDB entries covering the protein in multiple conformational states (GTP-bound, RNA-bound, complex with cofactors). The structural coverage spans the catalytic cycle, providing atomic-level understanding of the RNA ligation mechanism. This is among the most structurally characterized proteins in the W2 batch. Score 10/10 (informational only for a rejected protein).

### 7. Domain Architecture (Informational)

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001233 (RtcB) | RNA-splicing ligase RtcB family |
| InterPro | IPR036025 (RtcB-like) | GTP-dependent RNA ligase superfamily |
| InterPro | IPR027513 (RTCB) | RTCB catalytic subunit |
| Pfam | PF01139 (RtcB) | tRNA-splicing ligase RtcB |

**Domain Analysis**: RTCB belongs to a conserved family of GTP-dependent RNA ligases. The domain architecture is specialized for RNA ligation chemistry with GTP binding, metal coordination, and RNA substrate recognition. No DNA-binding or chromatin-interacting domains are present. Score 4/10 reflects the specialized RNA ligase function with no chromatin/DNA regulatory potential.

### 8. PPI Network Analysis (Informational)

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| Archease (ZBTB8OS) | tRNA-splicing ligase complex | Cofactor for RTCB activity |
| TRPT1 | tRNA splicing pathway | tRNA 2'-phosphotransferase |
| XBP1 mRNA | Unfolded protein response | Substrate for cytoplasmic splicing |
| tRNA precursors | RNA processing | Canonical substrate |

**PPI Assessment**: RTCB has well-characterized interactions within the tRNA-splicing ligase complex and RNA repair pathways. The interaction network is focused on RNA processing and the unfolded protein response. Score 5/10 reflects the well-characterized but functionally narrow interaction network.

### 9. Cross-Validation Analysis (Informational)

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Dual Localization | UniProt + GO-CC (nucleus + cytoplasm + ER + nuclear envelope) | Multi-compartment distribution | Consistent |
| Structure | PDB (5 entries, X-ray + Cryo-EM) | Extensive structural characterization | Consistent |
| Domain + Function | tRNA-splicing ligase + RNA ligation mechanism | Well-established enzymatic function | Consistent |

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED (PubMed threshold exceeded)

**Core Reasons for Rejection**:
1. PubMed count (107) exceeds the >100 hard threshold -- automatic REJECTION
2. The protein is extensively characterized structurally (5 PDB entries) and mechanistically
3. The RNA ligase field is mature with limited discovery space
4. The dual nuclear/cytoplasmic localization (score 4/10) provides moderate nuclear evidence
5. The protein's function (tRNA splicing, RNA repair) is well-defined with limited chromatin relevance

**Note on biological importance**: RTCB is a fascinating enzyme with a well-characterized GTP-dependent RNA ligation mechanism and important roles in tRNA maturation and the unfolded protein response. The rejection reflects the scope of the nuclear protein screen and the PubMed threshold, not a negative assessment of the protein's scientific value. RTCB would be an excellent target for RNA biology or enzymology research but is too crowded for the TE-regulated nuclear protein discovery screen.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RTCB fails the PubMed threshold (107 articles, >100). While the protein has documented nuclear localization (score 4/10, above the <=3 threshold), the extensive literature precludes this from being a novel discovery target. RTCB is structurally (5 PDB entries) and mechanistically well characterized, with limited unexplored biology remaining.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3I0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTCB%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (7P3B, 8BTT, 8ODO, 8ODP, 8ORJ)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3I0
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9Y3I0/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
