---
type: protein-evaluation
gene: "SEPTIN7"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SEPTIN7 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SEPTIN7 / CDC10, SEPT7 |
| Protein Name | Septin-7 |
| Protein Size | ~437 aa (50.7 kDa) |
| UniProt ID | Q16181 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SEPTIN7.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Primarily nuclear with experimental support |
| Protein Size | 10/10 | x1 | **10** | 437 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~34 |
| 3D Structure | 8/10 | x3 | **24** | PDB: 8, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 4, Pfam: 1 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.25** | |
| **Raw Total** | | | **147.2/180** | |
| **Normalized Total** | | | **81.8/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Chromosome, centromere, kinetochore | ECO:0000269 |
| UniProt | Cytoplasm, cytoskeleton, spindle | ECO:0000269 |
| UniProt | Cleavage furrow | ECO:0000269 |
| UniProt | Midbody | ECO:0000269 |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme | ECO:0000250 |
| UniProt | Cell projection, cilium, flagellum | ECO:0000269 |
| GO-CC | axoneme | IDA:GO_Central |
| GO-CC | cell division site | IBA:GO_Central |
| GO-CC | cleavage furrow | IEA:UniProtKB-SubCell |
| GO-CC | cytosol | TAS:Reactome |
| GO-CC | extracellular exosome | HDA:UniProtKB |
| GO-CC | kinetochore | IEA:UniProtKB-KW |
| GO-CC | microtubule cytoskeleton | IBA:GO_Central |
| GO-CC | midbody | IEA:UniProtKB-SubCell |
| GO-CC | non-motile cilium | IDA:GO_Central |
| GO-CC | nucleus | IDA:UniProtKB |
| GO-CC | septin complex | IDA:UniProtKB |
| GO-CC | septin ring | IBA:GO_Central |
| GO-CC | sperm annulus | IDA:UniProtKB |
| GO-CC | spindle | IEA:UniProtKB-SubCell |
| GO-CC | stress fiber | IDA:UniProtKB |
| HPA (IF) | Actin filaments | IF-based (Supported) |
| HPA (IF) | Cytokinetic bridge | IF-based (Supported) |
| HPA (IF) | Midbody | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 8/10.** Primarily nuclear with experimental support.

- UniProt annotates: Chromosome, centromere, kinetochore

- GO-CC annotations include: nucleus

**Nuclear localization score: 8/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

437 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 34 |
| Broad query count | 135 |
| Alias note | Aliases observed but not used for scoring: CDC10, SEPT7 |
| Novelty score | 8/10 |

PubMed strict count ~34 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:37083129** (2023 May 20) -- Single-cell RNA sequencing reveals the transcriptomic landscape of kidneys in patients with ischemic acute kidney injury (Chinese medical journal)
- **PMID:37508490** (2023 Jul 11) -- Migration of Myogenic Cells Is Highly Influenced by Cytoskeletal Septin7. (Cells)
- **PMID:33572403** (2021 Feb 9) -- Protein Kinase A-Mediated Septin7 Phosphorylation Disrupts Septin Filaments and Ciliogenesis. (Cells)
- **PMID:24055994** (2013 Dec) -- The human septin7 and the yeast CDC10 septin prevent Bax and copper mediated cell death in yeast. (Biochimica et biophysica acta)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 80.2 |
| PDB Entries | 8 |
| AF pLDDT >90% | 34.1% |
| AF pLDDT <50% | 10.8% |

**Structure Assessment**: PDB entries available (8 total): 2QAG (X-ray, 4.00 A), 3T5D (X-ray, 3.30 A), 3TW4 (X-ray, 3.35 A), 6N0B (X-ray, 1.74 A) AlphaFold prediction available (v6) with mean pLDDT: 80.2. pLDDT distribution: >90: 34.1%, 70-90: 46.2%, 50-70: 8.9%, <50: 10.8%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR030379 | IPR030379 |
| InterPro | IPR027417 | IPR027417 |
| InterPro | IPR016491 | IPR016491 |
| InterPro | IPR008115 | IPR008115 |
| Pfam | PF00735 | PF00735 |

InterPro domains: 4 | Pfam domains: 1. Total catalogued domains: 5.

Functional annotation: Filament-forming cytoskeletal GTPase. Required for normal organization of the actin cytoskeleton. Required for normal progress through mitosis. Involved in cytokinesis. Required for normal association of CENPE with the kinetochore. Plays a role in ciliogenesis and collective cell movements. Forms a filamentous structure with SEPTIN12, SEPTIN6, SEPTIN2 and probably SEPTIN4 at the sperm annulus which is required for the structural integrity and motility of the sperm tail during postmeiotic differe

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SEPTIN6 | Combined: 0.999 | EXP: 0.926 | DB: 1 |
| SEPTIN2 | Combined: 0.999 | EXP: 0.923 | DB: 1 |
| SEPTIN11 | Combined: 0.999 | EXP: 0.917 | DB: 1 |
| SEPTIN9 | Combined: 0.999 | EXP: 0.933 | DB: 1 |
| SEPTIN4 | Combined: 0.998 | EXP: 0.791 | DB: 1 |
| SEPTIN5 | Combined: 0.993 | EXP: 0.898 | DB: 1 |
| SEPTIN12 | Combined: 0.992 | EXP: 0.913 | DB: 1 |
| SEPTIN8 | Combined: 0.989 | EXP: 0.914 | DB: 1 |

Top STRING interaction partners:
- SEPTIN6 (combined score: 1.00, experimental: 0.93)
- SEPTIN2 (combined score: 1.00, experimental: 0.92)
- SEPTIN11 (combined score: 1.00, experimental: 0.92)
- SEPTIN9 (combined score: 1.00, experimental: 0.93)
- SEPTIN4 (combined score: 1.00, experimental: 0.79)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Filament-forming cytoskeletal GTPase. Required for normal organization of the actin cytoskeleton. Required for normal pr | -- |
| Structure | AF + PDB | Both AF and experimental | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.25/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 147.2/180 (81.8/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Primarily nuclear with experimental support
2. PubMed count: 34 articles 
3. Protein size: 437 aa -- ideal
4. Structure: Experimental PDB available (8 entries)
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 4 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 8 > 3, PubMed 34 <= 100). Total score: 147.2/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q16181
- HPA: https://www.proteinatlas.org/ENSG00000122545-SEPTIN7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEPTIN7%22
- STRING: https://string-db.org/ (search SEPTIN7)
- IntAct: https://www.ebi.ac.uk/intact/ (search SEPTIN7)
- Harvest packet: SEPTIN7.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16181 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 47..316; /note="Septin-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01056" |
| InterPro | IPR030379;IPR027417;IPR016491;IPR008115; |
| Pfam | PF00735; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000122545-SEPTIN7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SEPTIN10 | Intact, Biogrid | true |
| SEPTIN11 | Intact, Biogrid, Opencell | true |
| SEPTIN2 | Intact, Biogrid, Opencell | true |
| SEPTIN3 | Biogrid, Opencell | true |
| SEPTIN5 | Intact, Biogrid, Opencell | true |
| SEPTIN6 | Intact, Biogrid, Opencell | true |
| SEPTIN8 | Intact, Biogrid, Opencell | true |
| SEPTIN9 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
