---
type: protein-evaluation
gene: "SAXO4"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## SAXO4 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAXO4 / PPP1R32, C11orf66, IIIG9 |
| Protein Name | Stabilizer of Axonemal Microtubules 4 |
| Protein Size | ~430 aa / ~48 kDa (estimated) |
| UniProt ID | Q7Z5V6 (SAXO4_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | Ciliary basal body; sperm flagellum; axoneme; NO nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | ~430 aa, within ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~15-25 articles; very novel (≤20 -> 10 or 21-40 -> 8) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold predicted; no experimental PDB entries |
| Regulatory Domains | 4/10 | x2 | **8** | Microtubule inner protein; phosphatase 1 regulatory subunit |
| PPI Network | 2/10 | x3 | **6** | Limited characterized interactions; SAXO family members |
| Cross-Validation Bonus | -- | -- | **+0** | No nuclear cross-validation possible |
| **Raw Total** | | | **83.0/180** | |
| **Normalized Total** | | | **27.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Ciliary basal body | Reviewed |
| GO-CC | Ciliary basal body (GO:0036064) | ISS |
| GO-CC | Cilium (GO:0005929) | ISS |
| GO-CC | Cytoplasm (GO:0005737) | ISS |
| GO-CC | Sperm flagellum (GO:0036126) | ISS |
| PhosphoSitePlus | Cytoplasm | Predicted |
| GeneCards | Not annotated as nuclear | -- |

**HPA IF Status**: HPA IF data not available for this protein.

**Manual Review Assessment**: SAXO4 (Stabilizer of Axonemal Microtubules 4) is a microtubule inner protein (MIP) component of sperm flagellar doublet microtubules and ciliary axonemes. It localizes to cilia, flagella, the ciliary basal body, and cytoplasm. The SAXO protein family (SAXO1-4) mediates tubulin turnover in axonemal microtubules, with SAXO proteins localizing between the peripheral microtubules of the axoneme and the ciliary membrane. The protein also functions as a protein phosphatase 1 regulatory subunit (PPP1R32).

**Key localizations (all non-nuclear)**:
1. Ciliary axoneme -- primary functional location
2. Ciliary basal body
3. Sperm flagellum
4. Cytoplasm
5. Ependymal cell cilia (brain), tracheal epithelium, testis, ovaries

SAXO4 has ZERO nuclear localization annotation, nuclear function, or nuclear interaction partners. It is a dedicated ciliary/flagellar protein with no connection to nuclear biology. Nuclear localization score: 1/10.

**REJECTION TRIGGER**: Nuclear localization score ≤3. SAXO4 is a ciliary/axonemal protein with exclusive cytoplasmic and ciliary localization.

### 4. Protein Size Assessment

SAXO4 is approximately 430 amino acids (~48 kDa), well within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~15-25 |
| Novelty category | ≤20 -> Score 10 (borderline) |

SAXO4 is a very poorly studied gene. It was previously designated C11orf66 (chromosome 11 open reading frame 66) before being renamed as part of the SAXO family. Key publications:
1. Zhang et al. (2025, J Cell Sci, PMID: 40421755) -- SAXO proteins mediate tubulin turnover in axonemal microtubules of Chlamydomonas
2. A small number of studies on PPP1R32 (protein phosphatase 1 regulatory subunit 32) function

The gene is significantly understudied in humans. Most functional knowledge comes from model organisms (Chlamydomonas, mouse, Xenopus). Single SAXO knockouts show no phenotype; multiple knockouts are needed to reveal ciliary defects. This functional redundancy may explain the limited research attention. Score 8/10 for novelty (borderline ≤20/21-40).

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Context | Microtubule inner protein; likely partially ordered |

No experimental structures exist for SAXO4. As a microtubule inner protein that binds to the inner surface of axonemal microtubules, it likely contains ordered microtubule-binding domains. The AlphaFold prediction is available but confidence metrics are not available without the harvest packet. Score 5/10 reflects predicted structure availability without experimental validation.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | PPP1R32 (protein phosphatase 1 regulatory subunit) | Phosphatase binding |
| Functional | Microtubule inner protein (MIP) | Axonemal microtubule binding |
| Functional | Ciliary targeting signals | Cilium-specific localization |

SAXO4 contains domains for microtubule binding (as a MIP) and phosphatase regulation (as PPP1R32). The microtubule-binding function is consistent with its role in regulating tubulin turnover in axonemal microtubules. The phosphatase regulatory function may link to signaling pathways controlling ciliary assembly and maintenance. Neither function relates to nuclear biology. Score 4/10.

### 8. PPI Network Analysis

SAXO4's PPI network is focused on ciliary/axonemal components:
- Tubulin (direct microtubule binding)
- Other SAXO family members (SAXO1, SAXO2, SAXO3)
- Axonemal dynein and associated proteins
- Protein phosphatase 1 catalytic subunit (PPP1CC)

All interaction partners are ciliary, cytoskeletal, or cytoplasmic. No nuclear partners exist. Score 2/10.

### 9. Cross-Validation Analysis

No cross-validation relevant to nuclear biology is possible. All biological data consistently point to ciliary/axonemal function. The consistent non-nuclear localization pattern is itself cross-validated across UniProt, GO-CC, and functional studies.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED for nuclear ≤3)

**Core Strengths** (in its own biological context):
1. Well-defined functional niche (axonemal microtubule stabilization)
2. Novel gene family with recent mechanistic insights (2025)
3. Functional redundancy with other SAXO family members provides comparative biology opportunities
4. Disease relevance: ciliopathies, male infertility

**Fatal Weakness for Our Screening Purpose**:
1. No nuclear localization whatsoever (score 1/10, ≤3 threshold)
2. Dedicated ciliary/flagellar protein
3. All interaction partners are cytoskeletal or ciliary
4. Ciliary biology is mechanistically distant from TE-regulated nuclear processes
5. Protein functions in a membrane-enclosed organelle (cilium) that is physically separated from the nucleus

### 11. Decision

**FINAL DECISION**: REJECTED. Nuclear localization score 1/10 (≤3 threshold). SAXO4 is a ciliary/axonemal microtubule inner protein with exclusive localization to cilia, flagella, ciliary basal bodies, and cytoplasm. The gene has zero connection to nuclear biology, transcriptional regulation, or chromatin. While the SAXO family represents genuinely novel biology with recent mechanistic insights (2025), this novelty is in the ciliary/cytoskeletal domain and is not relevant to TE-regulated nuclear protein screening. The complete absence of nuclear localization, function, or interaction partners is disqualifying.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z5V6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAXO4
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAXO4
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z5V6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031410; |
| Pfam | PF15691; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
