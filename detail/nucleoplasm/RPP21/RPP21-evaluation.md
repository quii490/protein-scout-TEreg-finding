---
type: protein-evaluation
gene: "RPP21"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RPP21 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RPP21 / C6orf135, CAT60 |
| Protein Name | Ribonuclease P protein subunit p21 |
| Protein Size | 154 aa / 17.6 kDa |
| UniProt ID | Q9H633 (RPP21_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Nucleus, nucleolus; GO-CC: nucleolar ribonuclease P complex, nucleoplasm; nucleolus is definitive nuclear sub-compartment |
| Protein Size | 8/10 | x1 | **8** | 154 aa, in the 100-200 aa range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~48 articles (21-50 -> 8); moderately novel |
| 3D Structure | 8/10 | x3 | **24** | PDB: 6AHR, 6AHU; experimental cryo-EM structures of ribonuclease P holoenzyme |
| Regulatory Domains | 7/10 | x2 | **14** | Ribonuclease P subunit; RNA-binding; zinc finger; novel protein baseline (7/10) applies |
| PPI Network | 5/10 | x3 | **15** | Ribonuclease P complex member; well-defined complex but limited to tRNA processing |
| Cross-Validation Bonus | -- | -- | **+1.5** | Nucleolus + nucleoplasm multi-source consensus (+0.5); PDB cryo-EM + domain consistency (+0.5); RNA-binding + ribozyme complex alignment (+0.5) |
| **Raw Total** | | | **138.5/180** | |
| **Normalized Total** | | | **75.7/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus, nucleolus | Reviewed |
| GO-CC | Multimeric ribonuclease P complex | Curated |
| GO-CC | Nucleolar ribonuclease P complex | Curated |
| GO-CC | Nucleoplasm | Curated |
| UniProt Keywords | Nucleus | Annotated |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt and GO-CC.

**Manual Review Assessment**: RPP21 exhibits definitive nuclear localization with specificity for the nucleolus -- a distinct nuclear sub-compartment. The annotation to "Nucleus, nucleolus" and "nucleolar ribonuclease P complex" provides fine-grained subnuclear localization information. The nucleolus is the site of ribosomal RNA transcription, processing, and ribosome assembly, but also functions in additional regulatory processes including cell cycle control and stress responses.

**Key points supporting nuclear localization**:
1. UniProt explicitly annotates Nucleus and Nucleolus as subcellular locations
2. GO-CC confirms nucleolar ribonuclease P complex and nucleoplasm
3. Keywords include "Nucleus"
4. The ribonuclease P complex functions in tRNA precursor processing in the nucleolus/nucleoplasm
5. Nucleolus is a strictly nuclear sub-compartment
6. No cytoplasmic or non-nuclear annotations

**Nuclear localization score: 9/10.** The nucleolar localization is definitive evidence of nuclear residence. The nucleolus is one of the most prominent nuclear sub-compartments and is exclusively nuclear. The combination of nucleus + nucleolus annotation from UniProt and nucleolar complex membership from GO-CC provides near-maximum confidence.

### 4. Protein Size Assessment

RPP21 is 154 amino acids (17.6 kDa), falling in the 100-200 aa range. While below the ideal 200-800 aa range, proteins of this size are tractable and have been successfully characterized structurally (PDB structures exist for the ribonuclease P complex containing RPP21). Score 8/10 reflects the slightly small size category (100-200 aa).

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~48 |
| Novelty category | 21-50 -> Score 8 |
| Earliest publication | ~2004 |

**Research Context**: RPP21 was identified as a subunit of the human ribonuclease P (RNase P) complex, a ribonucleoprotein enzyme that cleaves the 5' leader sequence of precursor tRNAs. The majority of publications mentioning RPP21 are in the context of RNase P complex characterization, cryo-EM structural studies, and tRNA processing. The protein has not been extensively studied outside the RNase P complex context.

**Major research themes**:
- Ribonuclease P complex composition and structure
- tRNA precursor processing and maturation
- Cryo-EM structural biology of the RNase P holoenzyme
- Evolution of RNase P subunits

**Novelty Assessment**: PubMed count of ~48 places RPP21 in the moderately novel category (21-50 -> 8). Most publications focus on RPP21 as part of the RNase P complex rather than independent studies of RPP21 biochemistry or function.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 2 (6AHR, 6AHU) |
| PDB Method | Cryo-EM |
| Structural Coverage | In context of RNase P holoenzyme |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on PDB entries and domain architecture.

**Structure Assessment**: RPP21 has been structurally characterized as part of the human ribonuclease P holoenzyme by cryo-electron microscopy (6AHR, 6AHU). These structures provide near-atomic resolution views of RPP21 within its native complex, which is more informative than isolated domain structures. The presence of cryo-EM structures for a protein of this size is notable. Score 8/10 reflects experimental structural characterization within the functional complex.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR007175 (RPP21) | Ribonuclease P subunit p21 family |
| Pfam | PF04032 (R3H) | RNA-binding domain |
| UniProt | RNA-binding | Functional annotation |

**Domain Analysis**: RPP21 contains an R3H domain, which is an RNA-binding module. The R3H domain is found in various RNA-processing proteins including ribonucleases, RNA helicases, and splicing factors. While the domain is RNA-binding rather than DNA-binding, RNA-binding proteins in the nucleolus participate in rRNA processing, ribosome biogenesis, and regulatory RNA metabolism. Score 7/10 (novel protein baseline for a family-specific domain with RNA-binding function).

### 8. PPI Network Analysis

**Ribonuclease P Complex Membership**:
| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| RPP subunits (POP1, RPP14, RPP20, RPP25, RPP29, RPP30, RPP38, RPP40) | Ribonuclease P complex | Core complex components |
| H1 RNA (RPPH1) | Ribonuclease P complex | Catalytic RNA subunit |
| tRNA precursors | Substrate | tRNA 5' processing |

**PPI Assessment**: RPP21 is a subunit of the well-characterized ribonuclease P complex. Its interaction network is defined by its integration into this multi-subunit ribonucleoprotein enzyme. The complex has been structurally resolved by cryo-EM, providing detailed interaction interfaces. Score 5/10 reflects the well-defined but functionally narrow interaction network (limited to RNase P and tRNA processing).

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nucleolar Localization | UniProt (Nucleus, nucleolus) + GO-CC (nucleolar RNase P complex, nucleoplasm) | Nucleolus/nucleoplasm | Highly consistent |
| RNA-binding | UniProt Keyword + Pfam R3H domain | RNA-binding | Consistent |
| Structure | PDB (6AHR, 6AHU) + domain annotation | Structural confirmation | Consistent |

**Cross-Validation Bonus Details**:
- Nucleolus + nucleoplasm localization from multiple sources: +0.5
- PDB cryo-EM structures + domain annotation consistency: +0.5
- RNA-binding annotation + R3H domain alignment: +0.5
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: HIGHLY RECOMMENDED (Score: 75.7/100)

**Core Strengths**:
1. Definitive nucleolar localization (score 9/10) -- strong nuclear sub-compartment specificity
2. Experimental cryo-EM structures available (6AHR, 6AHU)
3. Good novelty (PubMed=48, score 8/10)
4. RNA-binding function in the nucleolus
5. Well-characterized complex membership provides functional context
6. Compact size (154 aa) amenable to biochemical studies
7. Nucleolar localization connects to ribosome biogenesis and nuclear metabolism

**Risks / Uncertainties**:
1. Small size (154 aa) limits domain complexity
2. Function narrowly defined by RNase P complex membership
3. RNA-binding rather than DNA-binding
4. Limited independent functional studies outside RNase P context
5. May have restricted biological roles beyond tRNA processing

**Next Steps**:
- [ ] Assess RPP21 function independent of RNase P complex
- [ ] Investigate nucleolar localization determinants
- [ ] Explore potential roles in non-tRNA RNA processing
- [ ] Characterize RNA-binding specificity
- [ ] Determine expression across tissues and conditions

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RPP21 clears the nuclear localization threshold (score 9/10, well above <=3) and PubMed threshold (48 articles, <=100). The protein's nucleolar localization and RNase P complex membership provide definitive nuclear classification. Experimental cryo-EM structures and moderate novelty make this a strong candidate. The RNA-binding/nucleolar profile offers a distinct angle from the DNA-binding/chromatin focus of many other candidates.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H633
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RPP21%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (6AHR, 6AHU)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H633
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9H633/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H633 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007175; |
| Pfam | PF04032; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000241370-RPP21/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPP40 | Intact, Biogrid | true |
| NACC2 | Bioplex | false |
| OBI1 | Bioplex | false |
| POP1 | Bioplex | false |
| POP4 | Bioplex | false |
| POP5 | Bioplex | false |
| POP7 | Bioplex | false |
| PSME3IP1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
