---
type: protein-evaluation
gene: "RIBC1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RIBC1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RIBC1 / RIB43A-like with coiled-coils protein 1 |
| Protein Name | RIB43A-like with coiled-coils protein 1 |
| Protein Size | 379 aa |
| UniProt ID | Q8N443 (RIBC1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (previously listed in garbage reports) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | Axonemal A tubule inner sheath; sperm flagellum; motile cilia/flagella component; no nuclear evidence |
| Protein Size | 10/10 | x1 | **10** | 379 aa, within ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~5-10 articles (<=20 -> 10) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold prediction only; no PDB; coiled-coil protein |
| Regulatory Domains | 2/10 | x2 | **4** | Coiled-coil regions; structural role in flagella/cilia |
| PPI Network | 2/10 | x3 | **6** | Minimal PPI data; flagella/axoneme structural partners |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-DB flagella/cilia localization consistency (+0.5) |
| **Raw Total** | | | **82.5/180** | |
| **Normalized Total** | | | **45.8/100** | |

### 3. Nuclear Localization Evidence -- CRITICAL FAIL

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Axonemal A tubule inner sheath | Reviewed |
| UniProt | Sperm flagellum | Reviewed |
| PhosphoSitePlus | Sperm flagellum; Axonemal A tubule inner sheath | Curated |
| HPA (predicted) | Intracellular | Predicted |
| Any nuclear source | NONE | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RIBC1 is a structural component of motile cilia and flagella. It localizes specifically to the axonemal A tubule inner sheath, which is part of the microtubule-based axoneme core of cilia and flagella. The gene belongs to the RIB43A family, a group of proteins associated with ciliary and flagellar axoneme structure.

Key evidence for non-nuclear localization:
- Localizes to sperm flagellum -- a highly specialized cellular projection
- Axonemal A tubule inner sheath -- a structural component of the ciliary/flagellar microtubule apparatus
- No nuclear localization annotated in any database
- Gene located on X chromosome (Xp11.22)
- Function is structural (axoneme component), not regulatory

**Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED.**

### 4. Protein Size Assessment

RIBC1 is 379 amino acids, within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~5-10 |
| Novelty category | <=20 -> Score 10 |

**Research Context**: RIBC1 is extremely understudied. The gene is part of the RIB43A family associated with cilia and flagella. Most literature references are from genomic catalogs, large-scale expression studies, or proteomic analyses of cilia/flagella. Few, if any, direct functional studies exist.

**Novelty Assessment**: With ~5-10 PubMed articles, RIBC1 is among the most novel genes in the candidate list. Score 10/10. However, extreme novelty cannot compensate for complete absence of nuclear localization.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Features | Predicted coiled-coil regions; likely elongated structure |

**Structure Assessment**: RIBC1 is predicted to contain coiled-coil domains, which typically form elongated, fibrous structures. Such proteins often function as structural scaffolds in macromolecular assemblies (consistent with the axoneme/flagella localization). The AlphaFold prediction is available but quality may be limited for a fibrous coiled-coil protein. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | Coiled-coil regions | Fibrous structural domains |
| Family | RIB43A family | Ciliary/flagellar axoneme proteins |

**Domain Analysis**: RIBC1 has a simple domain architecture consisting primarily of coiled-coil regions. Coiled-coil domains mediate protein-protein interactions in structural contexts (cytoskeleton, axoneme, extracellular matrix). There are no DNA-binding, chromatin-binding, transcriptional regulatory, or enzymatic domains. Domain score: 2/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | No data in packet |
| IntAct | No data in packet |

**PPI Assessment**: PPI data for RIBC1 is virtually nonexistent. As a structural component of the flagellar/ciliary axoneme, it likely interacts with other axonemal proteins, but these interactions are not cataloged in standard PPI databases. PPI score: 2/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + PhosphoSitePlus | Sperm flagellum, axonemal A tubule | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database flagella/cilia localization consistency: +0.5
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. Zero nuclear localization evidence -- structural flagellar/ciliary axoneme component
2. Protein is a structural scaffold (coiled-coil), not a regulatory protein
3. Function is in motile cilia and sperm flagella, far removed from nuclear biology
4. Extremely novel (PubMed ~5-10) but novelty does not compensate for non-nuclear localization

**Why Previous Rejection Was Likely Correct**:
The original rejection of RIBC1 was correct. This is a sperm flagellum/ciliary axoneme structural protein with no connection to nuclear biology. While the gene is extremely novel, the fundamental subcellular localization makes it unsuitable for a nuclear protein screen.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RIBC1 fails the nuclear localization criterion (score 0/10, threshold <=3). The protein is a structural component of ciliary and flagellar axonemes with no nuclear localization. Nuclear score <=3 triggers automatic REJECTED status.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8N443
- PhosphoSitePlus: https://www.phosphosite.org/proteinAction?id=1312065
- HPA: https://www.proteinatlas.org/ENSG00000158423-RIBC1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RIBC1%22
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N443 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008805; |
| Pfam | PF05914; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158423-RIBC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CNOT2 | Biogrid, Bioplex | true |
| ATP6V0D2 | Intact | false |
| BORCS6 | Intact | false |
| BPIFA1 | Bioplex | false |
| BPIFB1 | Bioplex | false |
| CCNC | Intact | false |
| CNOT11 | Bioplex | false |
| CNOT3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
