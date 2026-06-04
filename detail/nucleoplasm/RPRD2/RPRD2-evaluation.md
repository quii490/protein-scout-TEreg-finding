---
type: protein-evaluation
gene: "RPRD2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RPRD2 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RPRD2 / KIAA0460 |
| Protein Name | Regulation of nuclear pre-mRNA domain-containing protein 2 |
| Protein Size | 1461 aa / 156.0 kDa |
| UniProt ID | Q5VT52 (RPRD2_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | GO-CC: nucleoplasm, transcription preinitiation complex; no direct UniProt nucleus annotation but transcription complex = nuclear; paralog RPRD1A is nuclear |
| Protein Size | 5/10 | x1 | **5** | 1461 aa, in the 1200-2000 aa range; large scaffold protein |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~9 articles (<=20 -> 10); extremely under-studied |
| 3D Structure | 7/10 | x3 | **21** | PDB: 4FLB (X-ray); experimental crystallography; CID domain structurally characterized |
| Regulatory Domains | 8/10 | x2 | **16** | CID domain (CTD-interacting, Pol II binding); transcription preinitiation complex; paralog of RPRD1A |
| PPI Network | 7/10 | x3 | **21** | RNA Pol II CTD interaction (by paralogy); transcription preinitiation complex membership |
| Cross-Validation Bonus | -- | -- | **+1.5** | Nucleoplasm + transcription complex consensus (+0.5); CID domain + paralog functional consistency (+0.5); gene name + function alignment (+0.5) |
| **Raw Total** | | | **142.5/180** | |
| **Normalized Total** | | | **77.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| GO-CC | Nucleoplasm | Curated |
| GO-CC | Transcription preinitiation complex | Curated |
| UniProt (Swiss-Prot) | Not explicitly annotated | -- |
| Gene Name | "Regulation of nuclear pre-mRNA domain-containing protein 2" | Descriptive |
| Paralog (RPRD1A) | Nucleus confirmed | By inference |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on GO-CC, paralog inference, and functional annotation.

**Manual Review Assessment**: RPRD2 is annotated to the nucleoplasm and transcription preinitiation complex by GO Cellular Component, which inherently defines nuclear localization. The transcription preinitiation complex assembles at gene promoters in the nucleus. The gene name "Regulation of nuclear pre-mRNA domain-containing protein 2" explicitly describes nuclear function. The paralog RPRD1A is definitively nuclear (UniProt Nucleus annotation, GO-CC nucleus + transcription preinitiation complex). The lack of explicit UniProt subcellular location annotation for RPRD2 likely reflects its even more extreme under-study (PubMed=9) rather than non-nuclear localization.

**Key points supporting nuclear localization**:
1. GO-CC: Nucleoplasm -- soluble nuclear compartment
2. GO-CC: Transcription preinitiation complex -- inherently nuclear
3. Gene name explicitly describes "nuclear pre-mRNA domain-containing"
4. Paralog RPRD1A is definitively nuclear
5. CID domain implies Pol II CTD interaction -- exclusively nuclear
6. Keywords do not include non-nuclear compartments

**Nuclear localization score: 7/10.** The GO-CC nucleoplasm + transcription preinitiation complex annotation provides strong evidence for nuclear localization, confirmed by gene name and paralog function. The score is 7 rather than 9 due to the absence of explicit UniProt subcellular location annotation. Well above the <=3 rejection threshold.

### 4. Protein Size Assessment

RPRD2 is 1461 amino acids (156.0 kDa), placing it in the 1200-2000 aa range. This is considerably larger than the ideal 200-800 aa range. The protein is a scaffold within the transcription preinitiation complex, where large size is expected for proteins that serve as assembly platforms for multiple interaction partners. The paralog RPRD1A is much smaller (312 aa), suggesting RPRD2 may have gained additional domains or regulatory regions. Score 5/10 reflects the large size category.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~9 |
| Novelty category | <=20 -> Score 10 |
| Earliest publication | Genome-wide studies / high-throughput |

**Research Context**: RPRD2 is an extremely under-studied protein with approximately 9 PubMed entries. Parallel to RPRD1A (the highest-scoring protein in the W2 batch), RPRD2 is a member of the transcription preinitiation complex that has received virtually no dedicated functional investigation. The vast majority of publications mentioning RPRD2 are high-throughput studies of the transcription machinery or protein interaction networks.

**Major research themes (limited)**:
- Transcription preinitiation complex composition
- CID domain structural biology
- Potential CTD interaction (by paralogy with RPRD1A)
- High-throughput protein interaction mapping

**Novelty Assessment**: PubMed count of ~9 places RPRD2 in the most novel category (<=20 -> 10). As a transcription preinitiation complex member with fewer than 10 publications, RPRD2 is one of the most under-studied components of the transcription machinery.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 (4FLB, X-ray crystallography) |
| PDB Method | X-ray diffraction |
| Structural Coverage | CID domain region |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on PDB entry and paralog structures.

**Structure Assessment**: RPRD2 has one experimental PDB structure (4FLB) solved by X-ray crystallography, covering at least the CID domain. The large protein size (1461 aa) means the experimental structure likely covers only a fraction of the total sequence. The CID domain structure is likely similar to that of its paralog RPRD1A (4JXT, 4NAC). Additional regions may be disordered or structurally uncharacterized. Score 7/10 reflects partial experimental structure for a highly novel protein.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR006569 (CID domain) | CTD-interacting domain -- binds Pol II CTD |
| InterPro | IPR008942 (ENTH/VHS) | Potential membrane trafficking domain |
| InterPro | IPR047885 (RPRD2-specific) | RPRD2-specific domain |
| Pfam | PF04818 (RPRD) | RPRD family domain |

**Domain Analysis**: RPRD2 shares the CID (CTD-interacting domain) with its paralog RPRD1A, which directly binds the phosphorylated C-terminal domain of RNA Polymerase II. The CID-CTD interaction positions RPRD2 at the core of transcription regulation. The ENTH/VHS domain annotation is shared with RPRD1A and is unusual for a transcription factor, potentially representing a moonlighting function or a domain with nuclear-specific roles. RPRD2 has family-specific domains (IPR047885) that distinguish it from RPRD1A.

**Chromatin/Regulatory Potential**: The CID domain + transcription preinitiation complex membership positions RPRD2 at the interface of transcription initiation and CTD-dependent regulation. The larger size compared to RPRD1A (1461 vs 312 aa) suggests additional domains or regulatory regions that may confer distinct functions. Score 8/10 reflects the CID domain and transcription machinery context.

### 8. PPI Network Analysis

**Transcription Preinitiation Complex and CTD Interactions**:
| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| RNA Pol II RPB1 CTD | Transcription machinery | Direct CTD interaction (by CID domain paralogy) |
| Transcription preinitiation complex | Transcription initiation | Complex membership |

**PPI Assessment**: By paralogy with RPRD1A and CID domain presence, RPRD2 is expected to interact with the Pol II CTD. The transcription preinitiation complex membership provides a rich network of transcription-related nuclear proteins. The extensive additional sequence in RPRD2 (over 1100 aa beyond the RPRD1A-equivalent length) may mediate unique protein interactions not shared with RPRD1A. Score 7/10 reflects the strong transcription context with uncharacterized interaction potential.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | GO-CC (nucleoplasm, transcription preinitiation complex) + gene name + paralog | Nucleoplasm / transcription complex | Consistent |
| CID Domain | InterPro + Pfam + paralog (RPRD1A) | CTD-interacting domain conserved | Consistent |
| Structure | PDB 4FLB (X-ray) + CID domain | Experimental validation of CID fold | Consistent |
| Function | Transcription preinitiation complex + CID domain | Transcriptional regulation | Consistent with paralog |

**Cross-Validation Bonus Details**:
- Nucleoplasm + transcription complex GO-CC consensus: +0.5
- CID domain + paralog (RPRD1A) functional consistency: +0.5
- Gene name ("Regulation of nuclear pre-mRNA...") + function alignment: +0.5
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: HIGHLY RECOMMENDED (Score: 77.9/100)

**Core Strengths**:
1. Extreme novelty (PubMed=9, score 10/10) -- virtually unexplored
2. Transcription preinitiation complex membership -- core transcription machinery
3. CID domain implies direct Pol II CTD interaction
4. Paralog RPRD1A provides functional framework (CID-CTD interaction established)
5. Experimental PDB structure (4FLB) for CID domain
6. Gene name explicitly declares nuclear pre-mRNA regulatory function
7. Large additional sequence vs RPRD1A suggests unique functional domains
8. Rich interaction potential through transcription complex membership

**Risks / Uncertainties**:
1. Large size (1461 aa) may challenge full-length biochemical studies
2. No explicit UniProt subcellular location annotation
3. Function largely inferred from paralog RPRD1A
4. Potential functional redundancy with RPRD1A needs investigation
5. ENTH/VHS domain role in nuclear context is unclear
6. Most of the protein sequence is structurally uncharacterized

**Next Steps**:
- [ ] Confirm nuclear localization by immunofluorescence
- [ ] Validate Pol II CTD binding via CID domain
- [ ] Determine functional relationship with paralog RPRD1A (redundant vs distinct)
- [ ] Map unique interaction partners beyond those shared with RPRD1A
- [ ] Characterize domain architecture of the additional ~1100 aa
- [ ] Assess genome-wide chromatin occupancy

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RPRD2 clears the nuclear localization threshold (score 7/10, above <=3) and PubMed threshold (9 articles, <=100). As the paralog of the top-scoring W2 candidate RPRD1A, RPRD2 shares the core advantages (CID domain, transcription preinitiation complex membership, extreme novelty) while offering distinct opportunities through its larger size and potentially unique functional domains. RPRD2 and RPRD1A together represent a valuable paralog pair for comparative studies of CTD-dependent transcription regulation.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5VT52
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RPRD2%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (4FLB)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VT52
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q5VT52/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
