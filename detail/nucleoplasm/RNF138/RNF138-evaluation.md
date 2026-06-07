---
type: protein-evaluation
gene: "RNF138"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RNF138 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF138 / NARF |
| Protein Name | E3 ubiquitin-protein ligase RNF138 |
| Protein Size | 245 aa / 28.2 kDa |
| UniProt ID | Q8WVD3 (RN138_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | UniProt: Chromosome; GO-CC: nucleus, site of double-strand break; DNA-binding keyword; DNA repair function |
| Protein Size | 10/10 | x1 | **10** | 245 aa, well within ideal 200-800 aa range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~44 articles (21-50 -> 8); moderately novel |
| 3D Structure | 6/10 | x3 | **18** | No PDB entries; AlphaFold prediction available; novel protein baseline (6/10) applies |
| Regulatory Domains | 8/10 | x2 | **16** | RING finger (E3 ligase) + DNA-binding annotation; chromatin-associated E3 ligase at DSB sites |
| PPI Network | 5/10 | x3 | **15** | DNA repair pathway proteins; interaction at double-strand break sites; ubiquitin signaling in DNA damage response |
| Cross-Validation Bonus | -- | -- | **+1.5** | Chromosome + DSB site consensus (+0.5); DNA-binding annotation + DNA repair GO (+0.5); domain + DNA repair function alignment (+0.5) |
| **Raw Total** | | | **132.5/180** | |
| **Normalized Total** | | | **72.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Chromosome | Reviewed |
| GO-CC | Nucleus | Curated |
| GO-CC | Site of double-strand break | Curated |
| UniProt Keywords | Chromosome | -- |
| UniProt Keywords | DNA damage, DNA repair | -- |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt chromosome annotation, GO-CC nucleus/DSB site, and functional evidence.

**Manual Review Assessment**: RNF138 stands out among the RNF family for its explicit "Chromosome" subcellular location annotation in UniProt. This is a high-specificity localization -- the protein is not merely nuclear but chromatin-associated at sites of double-strand breaks (DSBs). The DNA-binding keyword further reinforces this. The GO-CC annotation to "site of double-strand break" is particularly informative: RNF138 is recruited to DNA damage sites where it functions as an E3 ubiquitin ligase in the DNA damage response.

**Key points supporting nuclear/chromatin localization**:
1. UniProt explicitly annotates "Chromosome" as subcellular location -- very specific
2. GO-CC: Nucleus and site of double-strand break -- functional localization
3. Keywords include "Chromosome", "DNA damage", "DNA repair", "DNA-binding"
4. The protein functions directly at chromatin/DNA damage sites
5. DNA-binding activity suggests direct chromatin association

**Nuclear localization score: 8/10.** The chromosome/DSB localization is highly specific and functionally validated. The DNA-binding keyword suggests direct chromatin interaction. This is one of the strongest nuclear localization profiles in the RNF family. Well above the <=3 rejection threshold.

### 4. Protein Size Assessment

RNF138 is 245 amino acids in length, placing it within the ideal 200-800 aa range for biochemical characterization. This compact size is excellent for recombinant expression, structural studies, and functional assays. The small size combined with the DNA-binding function makes RNF138 attractive for domain mapping and structural biology. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~44 |
| Novelty category | 21-50 -> Score 8 |
| Earliest publication | ~2003 |

**Research Context**: RNF138 was initially identified as an E3 ubiquitin ligase. Research has focused on its role in DNA damage response, where it ubiquitinates proteins at double-strand break sites to promote DNA repair. Studies have examined its substrates and regulatory mechanisms in homologous recombination and non-homologous end joining pathways. Additional roles in Wnt signaling and embryonic development have been reported.

**Major research themes**:
- DNA double-strand break repair (homologous recombination, NHEJ)
- Ubiquitin signaling at DNA damage sites
- Cell cycle checkpoint regulation
- Wnt/beta-catenin pathway crosstalk
- Cancer biology (genome instability)

**Novelty Assessment**: PubMed count of ~44 places RNF138 in the moderately novel category (21-50 -> 8). The protein has gained attention for its role in DNA repair, but many mechanistic questions remain open. The chromatin/DNA repair context provides clear niche for functional studies.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Coverage | Predicted only |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on domain architecture and protein size.

**Structure Assessment**: RNF138 has no experimental PDB structures. At 245 aa, the protein is small enough for reliable AlphaFold prediction. The domain architecture (RING finger + DUF domains) is expected to produce a well-folded structure. The lack of experimental structures is typical for a protein with moderate publication count. Score 6/10 applies the novel protein baseline.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR008598 (DUF1247-like) | Domain of unknown function |
| InterPro | IPR052498 (RNF138 family) | Family-specific |
| InterPro | IPR001841 (RING finger) | E3 ubiquitin ligase |
| Pfam | PF13923 (zf-RING_7) | RING-type zinc finger |
| Pfam | PF05605 (zf-C3HC4_2) | RING variant |
| UniProt Keyword | DNA-binding | Functional annotation |

**Domain Analysis**: RNF138 contains a RING finger domain for E3 ubiquitin ligase activity and DUF domain regions. The most significant feature is the UniProt "DNA-binding" keyword. While the protein lacks a classical DNA-binding domain (e.g., AT-hook, HMG-box, homeodomain), the DNA-binding annotation suggests either a non-canonical DNA-binding mechanism or structure-mediated DNA interaction. The combination of DNA-binding activity with E3 ligase function at DSB sites positions RNF138 as a chromatin-associated regulatory enzyme.

**Chromatin/Regulatory Potential**: RNF138 represents an E3 ubiquitin ligase that operates directly on chromatin at DNA damage sites. The ubiquitination of chromatin-associated proteins at DSBs is a critical regulatory mechanism in DNA repair pathway choice. Score 8/10 reflects the DNA-binding + E3 ligase dual functionality with clear chromatin/DNA repair relevance.

### 8. PPI Network Analysis

**DNA damage response interaction context**:
| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| DNA repair proteins | Double-strand break sites | Ubiquitination substrates at DSBs |
| Homologous recombination factors | DNA repair pathway choice | Pathway regulation |
| NHEJ factors | Non-homologous end joining | Repair pathway balance |

**PPI Assessment**: RNF138 functions at double-strand break sites where it interacts with and ubiquitinates DNA repair proteins. The PPI network is expected to be enriched in DNA damage response proteins, chromatin modifiers, and ubiquitin-proteasome components. The focused localization (DSB sites) suggests a targeted rather than broad interaction network. Score 5/10 reflects the functionally relevant but incompletely mapped interaction network.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Chromosome Localization | UniProt + GO-CC (DSB site) | Chromosome, site of DSB | Highly consistent |
| DNA-binding | UniProt Keyword + DNA repair GO | DNA-binding annotated | Functionally aligned |
| Domain + Function | RING (E3 ligase) + DNA-binding | Consistent with DSB ubiquitination role | Functionally aligned |

**Cross-Validation Bonus Details**:
- Chromosome annotation + DSB site GO-CC consistency: +0.5
- DNA-binding keyword + DNA repair GO-CC alignment: +0.5
- Domain (RING) + functional localization (DSB) alignment: +0.5
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 72.4/100)

**Core Strengths**:
1. Exceptional nuclear localization specificity -- chromosome/DSB site (score 8/10)
2. Explicit DNA-binding activity annotated by UniProt
3. Direct functional link to chromatin via DNA repair at double-strand breaks
4. Good novelty score (PubMed=44, score 8/10) with research niche available
5. Ideal protein size (245 aa) for structural and biochemical characterization
6. DNA repair + ubiquitin E3 ligase dual function provides clear mechanistic framework
7. Chromatin context well-established through DSB biology

**Risks / Uncertainties**:
1. No experimental PDB structures
2. Limited comprehensive PPI mapping
3. DNA-binding mechanism not structurally characterized
4. DUF domains of unknown function
5. Competition from active DNA repair research community
6. DSB localization may be transient/damage-dependent

**Next Steps**:
- [ ] Determine structural basis of DNA-binding activity
- [ ] Map chromatin interactome at DSB sites
- [ ] Identify full substrate repertoire in DNA repair
- [ ] Characterize domain-level contributions to DSB recruitment
- [ ] Assess chromatin context-specific functions beyond DNA repair

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RNF138 clears the nuclear localization threshold (score 8/10, well above <=3) and PubMed threshold (44 articles, <=100). The protein's chromosome/DSB localization and DNA-binding activity make it a strong candidate with direct chromatin functional relevance. The combination of DNA repair-specific localization with E3 ubiquitin ligase activity provides a well-defined research framework while maintaining moderate novelty. Recommended for inclusion.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8WVD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF138%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WVD3
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q8WVD3/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WVD3 |
| SMART | SM00184; |
| UniProt Domain [FT] | DOMAIN 225..243; /note="UIM"; /evidence="ECO:0000305" |
| InterPro | IPR008598;IPR052498;IPR034734;IPR001841;IPR013083; |
| Pfam | PF13923;PF05605;PF18574; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134758-RNF138/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBE2K | Intact, Biogrid | true |
| ADRB2 | Intact | false |
| EFEMP2 | Intact | false |
| FGFR3 | Intact | false |
| FXN | Intact | false |
| GRIN2C | Intact | false |
| GRN | Intact | false |
| GSN | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
