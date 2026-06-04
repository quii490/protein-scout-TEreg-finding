---
type: protein-evaluation
gene: "RPRD1A"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RPRD1A -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RPRD1A / P15RS |
| Protein Name | Regulation of nuclear pre-mRNA domain-containing protein 1A |
| Protein Size | 312 aa / 35.7 kDa |
| UniProt ID | Q96P16 (RPR1A_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Nucleus; GO-CC: nucleoplasm, nucleus, transcription preinitiation complex; gene name itself indicates nuclear function |
| Protein Size | 10/10 | x1 | **10** | 312 aa, well within ideal 200-800 aa range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~17 articles (<=20 -> 10); extremely under-studied |
| 3D Structure | 8/10 | x3 | **24** | PDB: 4JXT (X-ray), 4NAC (X-ray); experimental crystallography structures |
| Regulatory Domains | 8/10 | x2 | **16** | CID domain (CTD-interacting, Pol II binding); transcription preinitiation complex member; direct Pol II CTD interaction |
| PPI Network | 7/10 | x3 | **21** | RNA Pol II CTD interaction; transcription preinitiation complex; CID domain mediates specific Pol II binding |
| Cross-Validation Bonus | -- | -- | **+2.0** | Nucleus + transcription complex consensus (+0.5); PDB + CID domain consistency (+0.5); CID + Pol II CTD interaction alignment (+0.5); gene name + function alignment (+0.5) |
| **Raw Total** | | | **159.0/180** | |
| **Normalized Total** | | | **86.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Reviewed |
| GO-CC | Nucleoplasm | Curated |
| GO-CC | Nucleus | Curated |
| GO-CC | Transcription preinitiation complex | Curated |
| Gene Name | "Regulation of nuclear pre-mRNA domain-containing protein 1A" | Descriptive |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt, GO-CC, and functional annotation.

**Manual Review Assessment**: RPRD1A exhibits unequivocal nuclear localization. The protein is annotated exclusively to the nucleus and transcription preinitiation complex. The gene name itself declares its nuclear function: "Regulation of nuclear pre-mRNA domain-containing protein 1A." The protein is a member of the transcription preinitiation complex, which assembles at gene promoters in the nucleus to initiate RNA polymerase II transcription.

**Key points establishing definitive nuclear localization**:
1. UniProt subcellular location: Nucleus (exclusive)
2. GO-CC: Nucleoplasm, Nucleus, Transcription preinitiation complex
3. Keywords include "Nucleus"
4. CID domain mediates CTD interaction -- the Pol II CTD is exclusively nuclear
5. The transcription preinitiation complex functions exclusively in the nucleus
6. The gene name "Regulation of nuclear pre-mRNA..." explicitly describes nuclear function

**Nuclear localization score: 9/10.** This is one of the most definitive nuclear localization profiles in the W2 batch. Exclusive nucleus annotation, transcription preinitiation complex membership, and a gene name that explicitly describes nuclear function. Near-perfect nuclear confidence, with the only limitation being the absence of directly reviewed HPA IF images.

### 4. Protein Size Assessment

RPRD1A is 312 amino acids in length, well within the ideal 200-800 aa range. This size is optimal for recombinant expression, purification, crystallization (validated by existing PDB structures), and functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~17 |
| Novelty category | <=20 -> Score 10 |
| Earliest publication | ~2006 |

**Research Context**: RPRD1A (also known as P15RS) is an extremely under-studied protein with approximately 17 dedicated publications. Despite its membership in the transcription preinitiation complex and its direct interaction with the RNA Polymerase II CTD via the CID domain, the protein has received remarkably little research attention. Most publications are high-throughput studies or structural characterizations of the CID domain.

**Major research themes (limited)**:
- RNA Polymerase II CTD interaction
- Transcription preinitiation complex composition
- Potential role in CTD phosphorylation-dependent regulation
- Structural characterization of CID domain
- Cell cycle regulation (P15RS originally named for p15(INK4b)-related sequence)

**Novelty Assessment**: PubMed count of ~17 places RPRD1A in the most novel category (<=20 -> 10). For a protein that directly binds the Pol II CTD and is a member of the transcription preinitiation complex, this level of under-study is striking. The protein represents a major gap in our understanding of the transcription initiation machinery.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 2 (4JXT, 4NAC, both X-ray crystallography) |
| PDB Method | X-ray diffraction |
| Structural Coverage | CID domain + additional regions |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on PDB entries.

**Structure Assessment**: RPRD1A has two experimental PDB structures solved by X-ray crystallography (4JXT, 4NAC). These structures provide atomic-resolution views of the protein, likely including the CID domain that mediates Pol II CTD interaction. For a protein with only 17 publications, having multiple X-ray structures is a significant strength. Score 8/10 reflects experimental structural characterization above the novel protein baseline.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR006569 (CID domain) | CTD-interacting domain -- binds phosphorylated Pol II CTD |
| InterPro | IPR008942 (ENTH/VHS) | Potential membrane trafficking domain |
| InterPro | IPR032337 (RPRD1A/B) | RPRD family conserved region |
| InterPro | IPR047884 (RPRD1A-specific) | Family-specific domain |
| Pfam | PF04818 (RPRD) | RPRD family domain |
| Pfam | PF16566 (CID) | CTD-interacting domain |

**Domain Analysis**: The CID (CTD-interacting domain) is the defining functional domain of RPRD1A. This domain directly recognizes and binds the phosphorylated C-terminal domain (CTD) of the largest subunit of RNA Polymerase II (RPB1). The Pol II CTD serves as a dynamic regulatory platform that recruits transcription and RNA processing factors in a phosphorylation-dependent manner. By binding the CTD, RPRD1A positions itself at the heart of transcription regulation and co-transcriptional RNA processing.

**Chromatin/Regulatory Potential**: The CID domain-mediated Pol II CTD interaction is one of the most direct links to chromatin biology possible. The CTD is the landing pad for factors that regulate transcription initiation, elongation, termination, and co-transcriptional RNA processing (capping, splicing, polyadenylation). RPRD1A's role in the transcription preinitiation complex further reinforces its regulatory function. Score 8/10 reflects the CID domain + transcription complex membership.

### 8. PPI Network Analysis

**Transcription Preinitiation Complex and CTD Interactions**:
| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| RNA Pol II RPB1 CTD | Transcription machinery | Direct CTD interaction via CID domain |
| Transcription preinitiation complex components | Transcription initiation | Complex membership |
| CTD phosphatases/kinases | CTD phosphorylation cycle | Regulatory interactions |

**PPI Assessment**: RPRD1A's interaction network is defined by its CID domain, which directly binds the Pol II CTD -- one of the most important regulatory platforms in the nucleus. The transcription preinitiation complex membership provides a rich network of functionally related nuclear proteins. The CID-CTD interaction is specific, well-characterized structurally, and mechanistically significant. Score 7/10 reflects the high-quality interaction with the Pol II CTD and transcription complex membership.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt (Nucleus) + GO-CC (Nucleoplasm, nucleus, transcription preinitiation complex) + gene name | Nucleus / transcription complex | Highly consistent |
| CID Domain | InterPro + Pfam | CTD-interacting domain | Consistent |
| Structure | PDB (4JXT, 4NAC) + CID domain | Experimental validation | Consistent |
| Function | CTD binding + transcription preinitiation complex | Transcriptional regulation | Consistent |

**Cross-Validation Bonus Details**:
- Nucleus + transcription complex consensus from multiple sources: +0.5
- PDB structures + CID domain consistency: +0.5
- CID domain + Pol II CTD interaction alignment: +0.5
- Gene name ("Regulation of nuclear pre-mRNA...") + function alignment: +0.5
- **Total Cross-Validation Bonus**: +2.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: HIGHLY RECOMMENDED (Score: 86.9/100) -- TOP CANDIDATE IN W2 BATCH

**Core Strengths**:
1. Definitive nuclear localization (score 9/10) -- exclusive nucleus + transcription complex
2. Extreme novelty (PubMed=17, score 10/10) -- remarkable for a core transcription factor
3. CID domain directly interacts with Pol II CTD -- one of the most important regulatory platforms
4. Experimental PDB structures (4JXT, 4NAC, both X-ray)
5. Ideal protein size (312 aa, score 10/10)
6. Transcription preinitiation complex membership
7. Gene name explicitly declares nuclear pre-mRNA regulatory function
8. Virtually all aspects of RPRD1A biology remain unexplored
9. CTD interaction provides direct functional link to transcription regulation and chromatin biology
10. Highest composite score in the W2 batch (86.9/100)

**Risks / Uncertainties**:
1. Function within the transcription preinitiation complex is largely uncharacterized
2. The ENTH/VHS domain annotation is unusual for a transcription factor
3. Limited functional studies -- most characterization is structural
4. Specific role in CTD code reading is unknown
5. Tissue-specific expression and function unexplored

**Next Steps**:
- [ ] Characterize specific role in transcription initiation
- [ ] Determine CTD phosphorylation state specificity of CID binding
- [ ] Map full interactome within and beyond the transcription preinitiation complex
- [ ] Investigate the function of the ENTH/VHS domain
- [ ] Assess genome-wide chromatin occupancy via ChIP-seq
- [ ] Explore potential roles in co-transcriptional RNA processing

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RPRD1A achieves the highest score in the W2 batch (86.9/100). The protein clears both thresholds decisively (nuclear score 9/10, PubMed 17 articles). RPRD1A is an exceptionally promising candidate: it combines extreme novelty with a direct mechanistic link to RNA Polymerase II via the CID domain-CTD interaction. As a member of the transcription preinitiation complex that has been largely overlooked by the research community, RPRD1A represents a unique opportunity to discover new regulatory mechanisms at the core of eukaryotic transcription.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96P16
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RPRD1A%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (4JXT, 4NAC)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96P16
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q96P16/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
