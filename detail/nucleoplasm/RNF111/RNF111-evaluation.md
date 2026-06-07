---
type: protein-evaluation
gene: "RNF111"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RNF111 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF111 / Arkadia |
| Protein Name | E3 ubiquitin-protein ligase Arkadia |
| Protein Size | 994 aa / 108.9 kDa |
| UniProt ID | Q6ZNA4 (RN111_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | UniProt: Nucleus, PML body; GO-CC: nucleoplasm, nucleus, PML body; cytoplasm also annotated but PML body = strong nuclear feature |
| Protein Size | 8/10 | x1 | **8** | 994 aa, in the 800-1200 aa range |
| Research Novelty | 6/10 | x5 | **30** | PubMed ~51 articles (51-100 -> 6) |
| 3D Structure | 8/10 | x3 | **24** | PDB: 2KIZ, 5LG0, 5LG7, 7P2K; experimental NMR/crystallography structures + AlphaFold prediction |
| Regulatory Domains | 8/10 | x2 | **16** | RING-type zinc finger (E3 ligase); SUMO-targeted ubiquitin ligase activity; TGF-beta/SMAD pathway regulator |
| PPI Network | 6/10 | x3 | **18** | SMAD7, AXIN, SKI/SKIL, SMURF1, SUMO pathway; TGF-beta signaling hub |
| Cross-Validation Bonus | -- | -- | **+1.0** | Multi-DB nuclear/PML body localization consensus (+0.5); PDB + domain architecture consistency (+0.5) |
| **Raw Total** | | | **129.0/180** | |
| **Normalized Total** | | | **70.5/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Reviewed |
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| UniProt (Swiss-Prot) | Nucleus, PML body | Reviewed |
| GO-CC | Nucleoplasm | IDA:HPA |
| GO-CC | Nucleus | -- |
| GO-CC | PML body | -- |
| GO-CC | Cytoplasm | -- |
| GO-CC | Cytosol | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on UniProt + GO-CC.

**Manual Review Assessment**: RNF111 (Arkadia) is a well-characterized nuclear E3 ubiquitin ligase that localizes to PML nuclear bodies. PML bodies are nuclear sub-compartments involved in sumoylation, transcriptional regulation, apoptosis, and DNA damage response. The protein also has cytoplasmic annotation, which is consistent with nucleocytoplasmic shuttling behavior observed for many regulatory E3 ligases. The PML body localization is a hallmark of nuclear regulatory function and strongly supports nuclear classification.

**Key points supporting nuclear localization**:
1. UniProt annotates Nucleus + PML body as subcellular locations
2. GO-CC has nucleoplasm with IDA:HPA evidence (experimental)
3. PML body is a strictly nuclear compartment
4. The protein's primary function (TGF-beta/SMAD pathway regulation) occurs in the nucleus
5. Keywords include "Nucleus" in UniProt

**Nuclear localization score: 8/10.** The protein has strong evidence for nuclear localization (PML body, nucleoplasm), but cytoplasmic presence is also annotated. The nuclear signal is dominant and functionally significant. Above the <=3 rejection threshold.

### 4. Protein Size Assessment

RNF111 is 994 amino acids, placing it at the upper end of the 800-1200 aa range. Score 8/10. While slightly larger than the ideal 200-800 aa range for some biochemical assays, the protein has successful experimental structures (multiple PDB entries including NMR and crystallography), demonstrating its tractability for structural and biochemical studies.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~51 |
| Novelty category | 51-100 -> Score 6 |
| Earliest publication | ~2004 |

**Research Context**: RNF111 (Arkadia) was discovered as a positive regulator of Nodal/TGF-beta signaling during embryonic development. It functions as a SUMO-targeted ubiquitin ligase (STUbL) that ubiquitinates SUMO-modified substrates for proteasomal degradation. Key substrates include SKI/SKIL (transcriptional co-repressors) and components of the TGF-beta pathway. Arkadia-mediated degradation of SKI/SKIL derepresses SMAD-dependent transcription.

**Major research themes**:
- TGF-beta/BMP signaling regulation
- SUMO-targeted ubiquitin ligation (STUbL)
- Embryonic development and axis formation
- Cancer biology (tumor suppression via TGF-beta pathway)
- DNA damage response (RNF111 ubiquitinates SUMOylated proteins at damage sites)

**Novelty Assessment**: PubMed count of ~51 places RNF111 in the moderately studied category (51-100 -> 6). The protein has a well-defined molecular mechanism (STUbL activity) but questions remain about its full substrate repertoire and tissue-specific functions. Niche space exists for exploring chromatin context-specific roles and non-canonical substrates.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (canonical isoform) |
| PDB Entries | 4 (2KIZ, 5LG0, 5LG7, 7P2K) |
| PDB Method | NMR (2KIZ); X-ray (5LG0, 5LG7, 7P2K) |
| Structural Coverage | RING domain + N-terminal region |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on PDB entries and domain architecture.

**Structure Assessment**: RNF111 has multiple experimental PDB structures including the RING finger domain (2KIZ by NMR) and larger constructs solved by X-ray crystallography (5LG0, 5LG7, 7P2K). The presence of experimental structures from multiple groups validates the folded nature of the protein. The N-terminal region (RNF111_N domain, PF15303) and RING domain (PF13639) are the structurally characterized regions. The central region may contain disordered segments. Score 8/10 reflects the availability of experimental structures with good resolution.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR029306 (RNF111_N) | E3 ubiquitin-protein ligase Arkadia N-terminal domain |
| InterPro | IPR001841 (RING finger) | Zn-finger, E3 ubiquitin ligase activity |
| InterPro | IPR013083 (Zinc finger, RING/FYVE/PHD-type) | Metal-binding, protein interaction |
| Pfam | PF15303 (RNF111_N) | N-terminal domain |
| Pfam | PF13639 (zf-RING_2) | RING-type zinc finger |

**Domain Analysis**: RNF111 contains the signature RING finger domain characteristic of E3 ubiquitin ligases, which mediates ubiquitin transfer from E2 enzymes to substrates. The N-terminal domain (RNF111_N) is specific to this protein family. The protein also contains SUMO-interacting motifs (SIMs) that enable its function as a SUMO-targeted ubiquitin ligase (STUbL). While these are not classical DNA-binding domains, the STUbL activity directly impacts chromatin-associated processes including transcription regulation and DNA repair. Domain score: 8/10. The RING domain provides clear molecular function, and the STUbL activity links it to chromatin biology.

### 8. PPI Network Analysis

**Experimentally validated interactions**:
| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| SMAD7 | TGF-beta signaling | Substrate recruitment, ubiquitination |
| SKI/SKIL | Transcriptional co-repressors | Ubiquitination targets; degradation releases SMAD-mediated transcription |
| AXIN | Wnt/TGF-beta crosstalk | Regulatory complex |
| SMURF1 | E3 ligase | Cooperative ubiquitination |
| SUMOylated proteins | STUbL substrates | DNA damage response, transcription regulation |

**Pathway context**: RNF111 operates at the interface of TGF-beta/BMP signaling and the SUMO pathway. It is a critical node that links sumoylation to ubiquitin-dependent degradation. The interaction with SMAD7 defines its role as a positive regulator of TGF-beta signaling (SMAD7-SMURF1/2 complex targets TGF-beta receptors, while SMAD7-Arkadia targets nuclear repressors).

**PPI Assessment**: RNF111 has well-characterized interactions with key signaling molecules. The PPI network is focused on the TGF-beta/SMAD pathway and SUMO-regulated processes. While the number of physical interaction partners is moderate, the interactions are functionally deep rather than broad. Partner enrichment in chromatin/transcription is significant (SMAD7, SKI/SKIL are transcriptional regulators). Score 6/10 reflects moderate PPI network size but strong functional relevance to nuclear processes.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + GO-CC + Keywords | Nucleus + PML body | Multi-DB consensus |
| PML Body Localization | UniProt + GO-CC | PML body confirmed | Consistent |
| Structure | PDB (4 entries) + AlphaFold | Experimentally validated fold | Consistent |
| Domain | InterPro + Pfam + UniProt | RING finger + RNF111_N | Consistent |
| Function | Literature + GO | STUbL, TGF-beta regulation | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database nuclear/PML body localization consensus (UniProt + GO-CC): +0.5
- PDB experimental structures + domain architecture consistency: +0.5
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 70.5/100)

**Core Strengths**:
1. Strong nuclear localization with PML body targeting (score 8/10)
2. Well-defined molecular mechanism as SUMO-targeted ubiquitin ligase (STUbL)
3. Experimental PDB structures available (4 entries, NMR + X-ray)
4. Direct functional link to chromatin/transcription regulation via TGF-beta/SMAD pathway
5. Moderate novelty (PubMed ~51) with niche space remaining
6. Protein size (994 aa) is tractable for biochemical studies
7. Deep functional characterization provides foundation for hypothesis-driven research

**Risks / Uncertainties**:
1. PubMed count is moderate (51), reducing novelty score
2. Large protein size (994 aa) may challenge some structural approaches
3. Cytoplasmic annotation may indicate nucleocytoplasmic shuttling -- careful validation needed
4. HPA IF images not available for direct assessment
5. Competition risk from established TGF-beta research community
6. Central disordered regions may complicate full-length structural studies

**Next Steps**:
- [ ] Verify PML body/nuclear localization by HPA IF or independent immunofluorescence
- [ ] Assess chromatin context-specific STUbL substrates
- [ ] Expand PPI network in specific cell types/conditions
- [ ] Evaluate tissue-specific expression and functional relevance

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RNF111 clears both nuclear localization threshold (score 8/10) and PubMed threshold (51 articles, <=100). The protein's PML body localization, STUbL activity, and role in TGF-beta/SMAD transcriptional regulation make it a strong nuclear candidate. Multiple experimental PDB structures and deep functional characterization support experimental feasibility. Recommended for inclusion with caveat about competition from established literature.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZNA4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF111%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (2KIZ, 5LG0, 5LG7, 7P2K)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZNA4
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZNA4 |
| SMART | SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029306;IPR001841;IPR013083;IPR051073; |
| Pfam | PF15303;PF13639; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157450-RNF111/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Intact, Biogrid | true |
| CSNK2B | Biogrid, Opencell | true |
| UBE2D1 | Intact, Biogrid | true |
| UBE2D2 | Intact, Biogrid | true |
| UBE2D3 | Intact, Biogrid | true |
| UBE2D4 | Intact, Biogrid | true |
| UBE2E1 | Intact, Biogrid | true |
| UBE2E3 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
