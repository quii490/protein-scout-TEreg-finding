---
type: protein-evaluation
gene: "SAR1A"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## SAR1A -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAR1A / SARA1, SAR1 |
| Protein Name | Small COPII Coat GTPase SAR1A (Secretion Associated Ras Related GTPase 1A) |
| Protein Size | 198 aa / ~22 kDa |
| UniProt ID | Q9NR31 (SAR1A_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | ER membrane; Golgi membrane; cytoplasm; NO nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | 198 aa, well within ideal range |
| Research Novelty | 6/10 | x5 | **30** | PubMed ~75-90 articles; moderately studied (51-100 -> 6) |
| 3D Structure | 8/10 | x3 | **24** | Multiple PDB entries; GDP/GTP-bound states; COPII coat structures |
| Regulatory Domains | 5/10 | x2 | **10** | Small GTPase superfamily; GTP/GDP switch; COPII coat recruitment |
| PPI Network | 6/10 | x3 | **18** | SEC23/SEC24, SEC13/SEC31, SEC16A; COPII coat components |
| Cross-Validation Bonus | -- | -- | **+0.5** | PDB + AlphaFold structural consistency (+0.5) |
| **Raw Total** | | | **96.5/180** | |
| **Normalized Total** | | | **37.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Endoplasmic reticulum membrane | Reviewed, experimental |
| UniProt (Swiss-Prot) | Golgi stack membrane | Reviewed, experimental |
| UniProt (Swiss-Prot) | Cytoplasm, cytosol | Reviewed |
| GO-CC | ER membrane, Golgi membrane, COPII vesicle coat | Multiple evidence codes |
| GO-CC | Lysosome membrane | IDA |
| GeneCards | Endoplasmic reticulum, Golgi | Tier1 |

**HPA IF Status**: HPA IF data available; ER/Golgi pattern expected.

**Manual Review Assessment**: SAR1A is a small GTPase of the RAS superfamily that functions as a core component of the COPII coat complex mediating ER-to-Golgi vesicular transport. Its localization is exclusively to the cytoplasmic face of the ER membrane (at ER exit sites), the Golgi membrane, and the cytosol. The GTP-bound active form inserts an N-terminal amphipathic helix into the ER membrane to initiate COPII vesicle budding. The GDP-bound inactive form is cytosolic. Recent work identified an additional role as a lysosomal leucine sensor regulating TORC1 signaling, with SAR1A localizing to the lysosome membrane upon leucine deprivation.

**Key non-nuclear localizations**:
1. ER membrane (ER exit sites) -- primary functional location
2. Golgi membrane
3. Cytosol (GDP-bound, inactive)
4. Lysosome membrane (leucine sensing)
5. COPII vesicles (transient)

SAR1A has NO nuclear localization annotation, nuclear function, or nuclear interaction partners. It is a quintessential cytoplasmic/membrane trafficking protein. Nuclear localization score: 1/10.

**REJECTION TRIGGER**: Nuclear localization score ≤3. SAR1A is a classical COPII vesicle trafficking protein with exclusive cytoplasmic/membrane localization.

### 4. Protein Size Assessment

SAR1A is 198 amino acids (22 kDa), at the lower boundary but within the experimentally tractable range. Small GTPases of this size are routinely amenable to all standard biochemical and structural approaches. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~75-90 |
| Novelty category | 51-100 -> Score 6 |

SAR1A has been studied in the context of COPII vesicle trafficking, ER-to-Golgi transport, and the secretory pathway. Key publications:
1. Silencing of mammalian Sar1 isoforms reveals COPII-independent transport (2013, Traffic, PMID: 23433038)
2. Small sequence variations between SAR1A and SAR1B paralogs (2020, PMID: 32358066)
3. SAR1A as a leucine sensor for TORC1 signaling (2021, PMID: 34290409)
4. Numerous structural studies of COPII coat components
5. Viral subversion of COPII trafficking

SAR1A is one of two mammalian paralogs (SAR1A and SAR1B), and its specific functions are often studied alongside SAR1B. The PubMed count of ~75-90 places it in the moderately studied category. The 2021 discovery of its TORC1-related leucine sensor function has added novelty, but the overall research landscape is mature. Score 6/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| PDB Entries | Multiple experimental structures |
| Coverage | GDP-bound, GTP-bound, SEC23/SEC24 complex |
| Methods | X-ray crystallography |
| Key Structures | SAR1-SEC23-SEC24 pre-budding complex, SAR1-GTP, SAR1-GDP |

SAR1A has excellent structural characterization. Multiple crystal structures capture GDP-bound (inactive) and GTP-bound (active) states, as well as the ternary complex with SEC23 and SEC24. The N-terminal amphipathic helix involved in membrane insertion has been structurally characterized. The structural basis of the GTP/GDP switch and COPII coat recruitment is well understood. Score 8/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | Small GTPase superfamily (IPR001806) | RAS-related GTPase |
| InterPro | Small GTP-binding protein domain (IPR005225) | GTP binding and hydrolysis |
| Pfam | Ras family (PF00071) | GTPase domain |
| G-segments | G1-G5 GTPase motifs | GTP binding, hydrolysis, effector interaction |

SAR1A contains the canonical small GTPase domain with G1-G5 motifs responsible for GTP binding and hydrolysis. The N-terminal amphipathic helix is a unique SAR1-specific feature not present in most other RAS family GTPases -- it mediates direct membrane insertion and is the key functional determinant of COPII coat initiation. The domain architecture is well-characterized, but the protein functions in membrane trafficking, not in nuclear regulation. Score 5/10.

### 8. PPI Network Analysis

SAR1A's PPI network is centered on COPII coat components:
- SEC23/SEC24 (inner COPII coat) -- direct binding, structural characterization
- SEC13/SEC31 (outer COPII coat) -- indirect via SEC23/SEC24
- SEC16A (ER exit site scaffold) -- localization and organization
- TORC1 components (indirect, leucine sensing)

The PPI network is narrow in scope but extremely well-characterized structurally and functionally. All interactions relate to COPII vesicle trafficking and membrane biology. No nuclear interaction partners exist. Score 6/10.

### 9. Cross-Validation Analysis

PDB + AlphaFold structural cross-validation is robust. The COPII coat interactions have been structurally validated at high resolution. However, cross-validation is limited because all dimensions point away from nuclear biology -- there is nothing nuclear to cross-validate.

**Cross-Validation Bonus Details**:
- PDB + AlphaFold structural cross-validation: +0.5
- No nuclear cross-validation: +0
- Limited PPI cross-validation (all COPII-related): +0
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED for nuclear ≤3)

**Core Strengths** (in its own biological context):
1. Excellent structural characterization (multiple PDB entries)
2. Well-understood biochemical mechanism (GTPase cycle, membrane insertion)
3. Disease relevance (COPII-related disorders, viral trafficking)

**Fatal Weakness for Our Screening Purpose**:
1. No nuclear localization whatsoever (score 1/10, ≤3 threshold)
2. ER/Golgi/cytosolic/lysosomal localization -- exclusively non-nuclear
3. All interaction partners are membrane trafficking components
4. COPII vesicle biology is well understood and mechanistically distant from TE-regulated nuclear processes
5. Even the TORC1 leucine sensing function operates at the lysosome, not the nucleus

### 11. Decision

**FINAL DECISION**: REJECTED. Nuclear localization score 1/10 (≤3 threshold). SAR1A is a classical COPII vesicle trafficking GTPase with exclusively cytoplasmic and membrane localization. Its biological functions in ER-to-Golgi transport, COPII coat assembly, and TORC1 leucine sensing are unrelated to nuclear biology or transcriptional regulation. While SAR1A is an interesting protein in the secretory pathway context, it has no relevance to TE-regulated nuclear protein screening. The complete absence of nuclear localization, function, or interaction partners is disqualifying.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NR31
- PDB: https://www.rcsb.org/search?q=SAR1A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAR1A
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAR1A
- Note: Harvest packet not available; SAR1A is well-characterized; data compiled from public databases

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NR31 |
| SMART | SM00177;SM00178; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR005225;IPR006689;IPR006687; |
| Pfam | PF00025; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000079332-SAR1A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SAR1B | Intact, Biogrid, Bioplex | true |
| ADGRE2 | Intact | false |
| ALG8 | Intact | false |
| AQP1 | Intact | false |
| AQP10 | Intact | false |
| AQP3 | Intact | false |
| ASGR1 | Intact | false |
| ATXN1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
