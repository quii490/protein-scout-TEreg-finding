---
type: protein-evaluation
gene: "RNF114"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RNF114 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF114 / ZNF228, ZNF313 |
| Protein Name | E3 ubiquitin-protein ligase RNF114 |
| Protein Size | 228 aa / 25.7 kDa |
| UniProt ID | Q9Y508 (RN114_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | UniProt: Cytoplasm + Nucleus (dual annotation); GO-CC: cytosol, nucleus, plasma membrane; no nuclear preference |
| Protein Size | 10/10 | x1 | **10** | 228 aa, well within ideal 200-800 aa range |
| Research Novelty | 6/10 | x5 | **30** | PubMed ~78 articles (51-100 -> 6) |
| 3D Structure | 6/10 | x3 | **18** | No PDB entries; AlphaFold prediction available; novel protein baseline (6/10) applies |
| Regulatory Domains | 7/10 | x2 | **14** | RING finger + DUF1247/DUF1241 domains; novel protein baseline (7/10) applies; DUF domains may harbor novel functions |
| PPI Network | 4/10 | x3 | **12** | Limited characterized PPI; ubiquitin ligase context; interaction with spermatogenesis-related proteins |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB dual localization consistency (+0.5) |
| **Raw Total** | | | **104.5/180** | |
| **Normalized Total** | | | **57.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| UniProt (Swiss-Prot) | Nucleus | Reviewed |
| GO-CC | Cytosol | IDA:HPA |
| GO-CC | Nucleus | IDA:HPA |
| GO-CC | Plasma membrane | IDA:HPA |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on UniProt dual annotation and GO-CC.

**Manual Review Assessment**: RNF114 is annotated as both cytoplasmic and nuclear by UniProt. GO-CC lists cytosol, nucleus, and plasma membrane, all with IDA:HPA experimental evidence. The dual annotation pattern is consistent with a protein that undergoes regulated nucleocytoplasmic shuttling. UniProt keywords include both "Cytoplasm" and "Nucleus" as well as "Developmental protein" and "Differentiation", suggesting cell-state-dependent localization.

**Key points for nuclear localization**:
1. UniProt explicitly annotates Nucleus as a subcellular location
2. GO-CC nucleus has IDA:HPA evidence (experimental)
3. Keywords include "Nucleus"
4. However, Cytoplasm is listed equally -- no nuclear preference
5. Plasma membrane localization is also annotated

**Nuclear localization score: 5/10.** The protein has clear evidence of nuclear presence, but it is equally annotated as cytoplasmic. There is no evidence of nuclear enrichment or nuclear-specific function. The dual localization pattern places this below the "mainly nuclear" threshold but above the rejection threshold (≤3). Above the <=3 rejection threshold.

### 4. Protein Size Assessment

RNF114 is 228 amino acids in length, well within the ideal 200-800 aa range for biochemical characterization. This size is excellent for recombinant expression, purification, crystallization trials, and functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~78 |
| Novelty category | 51-100 -> Score 6 |
| Earliest publication | ~2002 |

**Research Context**: RNF114 was initially identified as ZNF313, a zinc finger protein differentially expressed in psoriasis and certain cancers. Studies have examined its role in spermatogenesis, T cell activation, NF-kB signaling, and ubiquitination of substrates including p21/CDKN1A. The protein has been studied as a potential tumor suppressor or oncogene depending on the cellular context.

**Major research themes**:
- Spermatogenesis and male fertility
- NF-kB pathway regulation via ubiquitination
- T cell activation
- Cancer biology (psoriasis, hepatocellular carcinoma)
- Ubiquitin-proteasome system

**Novelty Assessment**: PubMed count of ~78 places RNF114 in the moderately studied category (51-100 -> 6). While not crowded, the protein has received attention across several disease contexts, reducing the novelty premium. Niche space remains for mechanistic studies of its nuclear-specific functions.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Coverage | Predicted only |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on domain architecture and protein size.

**Structure Assessment**: RNF114 has no experimental PDB structures. The protein contains a RING finger domain and DUF1247/DUF1241 domains with a short zinc finger region. At 228 aa, the protein is small enough that the AlphaFold prediction is likely reliable for most of the sequence. However, the lack of experimental validation limits confidence. Score 6/10 applies the novel protein baseline (no PDB + AlphaFold only).

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR008598 (DUF1247-like) | Domain of unknown function |
| InterPro | IPR042716 (RNF114) | Family-specific entry |
| InterPro | IPR001841 (RING finger) | E3 ubiquitin ligase |
| Pfam | PF05605 (zf-C3HC4_2) | RING-type zinc finger |
| Pfam | PF18574 (zf-RING_14) | RING variant |

**Domain Analysis**: RNF114 contains a RING finger domain conferring E3 ubiquitin ligase activity, and DUF1247/DUF1241 domains of unknown function. The DUF domains are the most intriguing feature -- as domains of unknown function, they represent potential novel protein interaction or substrate recognition modules. For a protein in the novel category (PubMed=78, <=100), the domain baseline is 7/10. The DUF domains represent potential for novel function discovery but lack annotation prevents higher scoring. Score 7/10.

### 8. PPI Network Analysis

**Experimentally characterized interactions**:
| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| p21/CDKN1A | Cell cycle regulation | Ubiquitination substrate in certain contexts |
| NF-kB pathway components | Immune signaling | Ubiquitination-dependent regulation |

**PPI Assessment**: RNF114 has a limited set of experimentally validated interaction partners. The E3 ligase activity is established, and substrate identification has been performed for specific pathways (NF-kB, cell cycle). However, a comprehensive PPI network has not been mapped. The dual cytoplasmic/nuclear localization suggests compartment-specific interactomes that remain unexplored. Score 4/10 reflects limited characterized PPI with moderate functional relevance.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Dual Localization | UniProt + GO-CC | Cytoplasm + Nucleus | Multi-DB consistent |
| Nuclear Evidence | UniProt + GO-CC (IDA:HPA) | Nucleus confirmed | Consistent |
| Domain | InterPro + Pfam | RING + DUF domains | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database dual localization (cytoplasm+nucleus) consistency: +0.5
- Limited structure cross-validation (no PDB): +0
- Limited PPI cross-validation: +0
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: CONDITIONALLY RECOMMENDED (Score: 57.1/100)

**Core Strengths**:
1. Clear nuclear presence confirmed by UniProt and GO-CC (IDA:HPA evidence)
2. Small protein size (228 aa) -- excellent for structural and biochemical studies
3. DUF1247/DUF1241 domains represent novel domain biology with discovery potential
4. E3 ubiquitin ligase activity links to proteasome-mediated regulation

**Risks / Uncertainties**:
1. Nuclear localization is not dominant -- equal cytoplasmic/nuclear distribution (score 5/10)
2. Moderate PubMed count (78) reduces novelty premium
3. No experimental PDB structures
4. DUF domains lack functional annotation
5. Nuclear-specific functions not well characterized
6. Competition from active research in cancer/psoriasis contexts

**Next Steps**:
- [ ] Characterize nuclear vs cytoplasmic interactomes separately
- [ ] Determine if nuclear RNF114 has specific substrates
- [ ] Define structural features of DUF1247/DUF1241 domains
- [ ] Assess nuclear localization in different cell types/states
- [ ] Verify NF-kB pathway regulation in nuclear context

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RNF114 clears both nuclear localization threshold (score 5/10, above <=3) and PubMed threshold (78 articles, <=100). However, the dual cytoplasmic/nuclear localization pattern and moderate PubMed count result in a lower priority score (57.1/100). The protein is a viable candidate but should be prioritized below genes with stronger nuclear preference and higher novelty.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y508
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF114%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y508
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9Y508/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y508 |
| SMART | SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008598;IPR042716;IPR051438;IPR034734;IPR027370;IPR001841;IPR013083;IPR017907; |
| Pfam | PF05605;PF13445;PF18574; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124226-RNF114/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBE2D1 | Intact, Biogrid | true |
| UBE2D2 | Intact, Biogrid | true |
| XAF1 | Intact, Biogrid | true |
| HOXD10 | Bioplex | false |
| HSPA5 | Biogrid | false |
| KAT5 | Intact | false |
| LHFPL4 | Bioplex | false |
| MAVS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
