---
type: protein-evaluation
gene: "SEH1L"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SEH1L -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SEH1L / SEC13L, SEH1 |
| Protein Name | Nucleoporin SEH1 |
| Protein Size | ~360 aa (39.6 kDa) |
| UniProt ID | Q96EE3 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SEH1L.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 10/10 | x4 | **40** | Strongly nuclear -- primary localization confirmed by multiple databases |
| Protein Size | 10/10 | x1 | **10** | 360 aa |
| Research Novelty | 9/10 | x5 | **45** | PubMed strict ~15 |
| 3D Structure | 8/10 | x3 | **24** | PDB: 8, AF: Yes |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 5, Pfam: 1 |
| PPI Network | 10/10 | x3 | **30** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.50** | |
| **Raw Total** | | | **160.5/180** | |
| **Normalized Total** | | | **89.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Chromosome, centromere, kinetochore | ECO:0000269, ECO:0000269 |
| UniProt | Nucleus, nuclear pore complex | ECO:0000269, ECO:0000269 |
| UniProt | Lysosome membrane | ECO:0000269 |
| GO-CC | cytosol | TAS:Reactome |
| GO-CC | GATOR2 complex | IDA:UniProtKB |
| GO-CC | kinetochore | IEA:UniProtKB-KW |
| GO-CC | lysosomal membrane | IDA:UniProtKB |
| GO-CC | nuclear envelope | IDA:ComplexPortal |
| GO-CC | nuclear pore | NAS:ComplexPortal |
| GO-CC | nuclear pore outer ring | IDA:UniProtKB |
| GO-CC | Seh1-associated complex | IBA:GO_Central |

**HPA IF Status**: No HPA IF data available.

**Nuclear Score: 10/10.** Strongly nuclear -- primary localization confirmed by multiple databases.

- UniProt annotates: Chromosome, centromere, kinetochore, Nucleus, nuclear pore complex

- GO-CC annotations include: nuclear envelope, nuclear pore, nuclear pore outer ring

**Nuclear localization score: 10/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

360 aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 15 |
| Broad query count | 24 |
| Alias note | Aliases observed but not used for scoring: SEC13L, SEH1 |
| Novelty score | 9/10 |

PubMed strict count ~15 articles. High novelty with limited prior characterization. Score: 9/10.

**Key Publications**:

- **PMID:35831510** (2022 Jul) -- Structure of the nutrient-sensing hub GATOR2. (Nature)
- **PMID:23723238** (2013 May 31) -- A Tumor suppressor complex with GAP activity for the Rag GTPases that signal amino acid sufficiency to mTORC1. (Science (New York, N.Y.))
- **PMID:40781725** (2025 Aug 8) -- Screening, identification, and experimental validation of SUMOylation biomarkers in Parkinson's disease. (Hereditas)
- **PMID:38372438** (2024 Mar 29) -- New insights into GATOR2-dependent interactions and its conformational changes in amino acid sensing. (Bioscience reports)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 86.9 |
| PDB Entries | 8 |
| AF pLDDT >90% | 73.3% |
| AF pLDDT <50% | 9.4% |

**Structure Assessment**: PDB entries available (8 total): 5A9Q (EM, 23.00 A), 7PEQ (EM, 35.00 A), 7R5J (EM, 50.00 A), 7R5K (EM, 12.00 A) AlphaFold prediction available (v6) with mean pLDDT: 86.9. pLDDT distribution: >90: 73.3%, 70-90: 11.7%, 50-70: 5.6%, <50: 9.4%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR037363 | IPR037363 |
| InterPro | IPR015943 | IPR015943 |
| InterPro | IPR020472 | IPR020472 |
| InterPro | IPR036322 | IPR036322 |
| InterPro | IPR001680 | IPR001680 |
| Pfam | PF00400 | PF00400 |

InterPro domains: 5 | Pfam domains: 1. Total catalogued domains: 6.

Functional annotation: Component of the Nup107-160 subcomplex of the nuclear pore complex (NPC). The Nup107-160 subcomplex is required for the assembly of a functional NPC (PubMed:15146057, PubMed:17363900). The Nup107-160 subcomplex is also required for normal kinetochore microtubule attachment, mitotic progression and chromosome segregation. This subunit plays a role in recruitment of the Nup107-160 subcomplex to the kinetochore (PubMed:15146057, PubMed:17363900) As a component of the GATOR2 complex, functions as an

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| NPRL2 | Combined: 0.999 | EXP: 0.997 | DB: 1 |
| NUP155 | Combined: 0.999 | EXP: 0.976 | DB: 1 |
| NUP205 | Combined: 0.999 | EXP: 0.979 | DB: 1 |
| MIOS | Combined: 0.999 | EXP: 0.996 | DB: 1 |
| NUP133 | Combined: 0.999 | EXP: 0.998 | DB: 1 |
| NUP43 | Combined: 0.999 | EXP: 0.986 | DB: 1 |
| NUP98 | Combined: 0.999 | EXP: 0.991 | DB: 1 |
| WDR59 | Combined: 0.999 | EXP: 0.999 | DB: 1 |

Top STRING interaction partners:
- NPRL2 (combined score: 1.00, experimental: 1.00)
- NUP155 (combined score: 1.00, experimental: 0.98)
- NUP205 (combined score: 1.00, experimental: 0.98)
- MIOS (combined score: 1.00, experimental: 1.00)
- NUP133 (combined score: 1.00, experimental: 1.00)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 10/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Nuclear consensus | Multi-source consistent |
| Function | Literature + GO | Component of the Nup107-160 subcomplex of the nuclear pore complex (NPC). The Nup107-160 subcomplex is required for the  | -- |
| Structure | AF + PDB | Both AF and experimental | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.50/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (STRONG). Total score 160.5/180 (89.2/100) places this protein in the top tier of candidates. Strong nuclear localization combined with favorable size, novelty, and structural characteristics.

**Core Observations**:
1. Nuclear localization: Strongly nuclear -- primary localization confirmed by multiple databases
2. PubMed count: 15 articles 
3. Protein size: 360 aa -- ideal
4. Structure: Experimental PDB available (8 entries)
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 5 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 10 > 3, PubMed 15 <= 100). Total score: 160.5/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96EE3
- HPA: https://www.proteinatlas.org/ENSG00000085415-SEH1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SEH1L%22
- STRING: https://string-db.org/ (search SEH1L)
- IntAct: https://www.ebi.ac.uk/intact/ (search SEH1L)
- Harvest packet: SEH1L.json
