---
type: protein-evaluation
gene: "SAP130"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## SAP130 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAP130 / Sin3A-Associated Protein 130 (histone deacetylase complex subunit SAP130) |
| Protein Name | Histone Deacetylase Complex Subunit SAP130 (Sin3-associated polypeptide p130) |
| Protein Size | ~1,048 aa / ~130 kDa (estimated) |
| UniProt ID | Q9H0E3 (SAP130_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

**NOMENCLATURE NOTE**: SAP130 refers to the Sin3A-associated protein 130, a subunit of the HDAC-dependent SIN3A corepressor complex. This protein is distinct from SF3B3 (splicing factor 3b subunit 3), which is also sometimes referred to as SAP130 (spliceosome-associated protein 130) in older literature. The gene evaluated here is GeneID 79595, the HDAC complex component.

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | SIN3A-HDAC corepressor complex; nuclear transcriptional repression |
| Protein Size | 7/10 | x1 | **7** | ~1,048 aa / ~130 kDa; slightly above ideal 200-800 aa range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~25-35 articles; moderately novel (21-40 -> 8) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold predicted; no experimental PDB entries; large protein |
| Regulatory Domains | 7/10 | x2 | **14** | HDAC complex subunit; transcriptional corepressor; SIN3A interaction |
| PPI Network | 6/10 | x3 | **18** | SIN3A complex members (SIN3A, SUDS3/SAP45, ARID4B/SAP180, HDAC1/2) |
| Cross-Validation Bonus | -- | -- | **+1.0** | Nuclear localization multi-DB (+0.5); HDAC complex membership consensus (+0.5) |
| **Raw Total** | | | **124.0/180** | |
| **Normalized Total** | | | **68.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | By similarity (SIN3A complex) |
| GO-CC | Nucleus (GO:0005634) | ISS |
| GO-CC | SIN3-type complex (GO:0070822) | ISS |
| GeneCards | Nucleus | Predicted |
| Functional Context | SIN3A-HDAC corepressor complex | Nuclear transcriptional repression |

**HPA IF Status**: HPA IF data not available in accessible databases for this protein.

**Manual Review Assessment**: SAP130 is a subunit of the SIN3A-HDAC corepressor complex, which functions exclusively in the nucleus to mediate transcriptional repression through histone deacetylation. The SIN3A complex is recruited to target gene promoters by sequence-specific transcription factors and represses transcription via HDAC1/HDAC2-mediated histone deacetylation. As a core component of this complex, SAP130's function is intrinsically nuclear. The protein does not contain a recognizable NLS in public annotations, but its incorporation into the nuclear SIN3A complex ensures nuclear localization.

**Key evidence for nuclear localization**:
1. Component of the SIN3A-HDAC nuclear corepressor complex
2. Transcriptional repression function (nuclear process)
3. Interaction with nuclear proteins (SIN3A, HDAC1/HDAC2)
4. GO-CC annotations support nuclear localization

Score 8/10 reflects strong functional evidence for nuclear localization through HDAC complex membership, with the caveat that direct experimental localization data is limited.

### 4. Protein Size Assessment

SAP130 is a large protein at approximately 130 kDa (~1,048 aa), which is above the ideal 200-800 aa experimental range. Large proteins (>100 kDa) present technical challenges for recombinant expression, purification, and structural characterization. However, the modular nature of HDAC complex subunits may allow domain-level studies. Size score: 7/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~25-35 |
| Novelty category | 21-40 -> Score 8 |

**Key Research Context**: SAP130 was identified by Fleischer et al. (2003, PMID: 12724404) as a subunit of the SIN3A corepressor complex. Research since then has focused primarily on its role within the HDAC complex. Key publications include:
1. Fleischer et al. (2003) -- Identification and preliminary characterization of SAP130 as a SIN3A-associated polypeptide
2. Additional studies on SIN3A complex composition and function that reference SAP130

SAP130 is notably less studied than other SIN3A complex components (SIN3A itself, HDAC1/2). Most publications mentioning SAP130 do so in the context of SIN3A complex characterization rather than as a dedicated research focus. However, the PubMed count includes papers on SIN3A complex biology that list SAP130 among complex components. Score 8/10 reflects moderate novelty.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (predicted) |
| PDB Entries | 0 (no experimental structures for SAP130 alone) |
| Structural Context | SIN3A complex structures may contain SAP130 density |

No experimental structures exist for SAP130 in isolation. Recent Cryo-EM structures of the SIN3A complex may contain SAP130 density, but the resolution and assignment may be limited. As a 130 kDa protein, full-length structural characterization is challenging. AlphaFold prediction is available but confidence metrics are not available without the harvest packet. Score 4/10 reflects the absence of dedicated experimental structures and the size-related challenges.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | SIN3A interaction region | Mediates incorporation into SIN3A complex |
| InterPro | Limited annotation | Large protein with sparse domain annotation |
| Functional | Histone deacetylase complex subunit | Transcriptional corepressor |

SAP130's domain architecture is poorly annotated. The protein's defining feature is its interaction with SIN3A, which enables its incorporation into the HDAC corepressor complex. Unlike many transcriptional regulators, SAP130 does not contain recognizable DNA-binding domains, histone modification domains, or other canonical chromatin regulatory modules. This suggests it may function as a scaffold or assembly factor within the SIN3A complex rather than possessing intrinsic enzymatic or DNA-binding activity. Score 7/10 reflects well-defined functional complex membership despite limited domain annotation.

### 8. PPI Network Analysis

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| SIN3A | HDAC complex scaffold | Core interaction; defines complex membership |
| SUDS3/SAP45 | SIN3A complex subunit | HDAC complex component |
| ARID4B/SAP180 | SIN3A complex subunit | DNA/chromatin targeting |
| HDAC1 | Histone deacetylase | Enzymatic core of the complex |
| HDAC2 | Histone deacetylase | Enzymatic core of the complex |
| CLEC4E | Dead/dying cell signaling | Reported interaction |

SAP130's PPI network is focused on the SIN3A-HDAC corepressor complex. The interactions with SIN3A, SUDS3, ARID4B, HDAC1, and HDAC2 are well-established through complex purification studies. The interaction with CLEC4E was identified through high-throughput screens and may represent a context-dependent function outside the SIN3A complex. The PPI network is narrow in scope but functionally well-defined. Score 6/10 reflects focused complex membership with high functional relevance but limited network breadth.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| SIN3A Complex | UniProt + GO-CC + Literature | SAP130 is a SIN3A-HDAC subunit | Multi-source consensus |
| Nuclear Function | Complex membership + GO-CC | Nuclear transcriptional repression | Consistent |
| HDAC Association | HDAC1/2 co-purification | Histone deacetylase complex | Validated |

**Cross-Validation Bonus Details**:
- Multi-source SIN3A-HDAC complex membership consensus: +0.5
- Nuclear localization through complex function consistency: +0.5
- No structural cross-validation (no PDB): +0
- Limited PPI cross-validation (beyond SIN3A complex): +0
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 68.9/100)

**Core Strengths**:
1. Strong nuclear functional context through SIN3A-HDAC corepressor complex membership
2. Direct involvement in transcriptional regulation via histone deacetylation
3. Moderately novel (PubMed ~25-35) with dedicated studies being rare
4. Well-defined functional context provides clear experimental framework
5. Disease relevance: HDAC complexes are therapeutic targets in cancer

**Risks / Uncertainties**:
1. Large protein size (~130 kDa, ~1,048 aa) presents technical challenges (score 7/10)
2. No experimental PDB structures; structural characterization will be difficult
3. Direct experimental nuclear localization evidence is limited
4. Poorly annotated domain architecture
5. May function as a scaffold rather than possessing intrinsic enzymatic activity
6. Research focus on SIN3A complex as a whole, not SAP130 specifically

**Next Steps**:
- [ ] Verify nuclear localization by IF in relevant cell types
- [ ] Map SAP130 interaction surfaces within SIN3A complex by truncation/domain analysis
- [ ] Investigate whether SAP130 has SIN3A-independent functions
- [ ] Obtain AlphaFold pLDDT statistics and PAE data for domain identification
- [ ] Assess SAP130-specific contributions to HDAC complex function (vs. other subunits)

### 11. Decision

**FINAL DECISION**: NOT REJECTED. Nuclear localization score 8/10 (above ≤3 threshold), PubMed count ~25-35 (below 100 threshold). SAP130 is a recommended candidate with good scores across most dimensions. Its membership in the SIN3A-HDAC corepressor complex provides a strong nuclear functional context and well-defined experimental framework. The primary concerns are the large protein size (~130 kDa) and lack of structural data. However, as a scaffold protein within a well-studied complex, focused domain-level studies may be productive without requiring full-length protein characterization. SAP130 is recommended for inclusion, ideally with a focus on defining its specific role within the SIN3A complex and any SIN3A-independent functions.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0E3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAP130
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAP130
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/79595
- Note: SAP130 is distinct from SF3B3; harvest packet not available; data compiled from UniProt and literature database queries
