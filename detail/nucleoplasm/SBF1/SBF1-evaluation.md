---
type: protein-evaluation
gene: "SBF1"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SBF1 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SBF1 / MTMR5 |
| Protein Name | Myotubularin-related protein 5 |
| Protein Size | ~1868 aa (208.4 kDa) |
| UniProt ID | O95248 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SBF1.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | Moderate nuclear evidence, mixed with cytoplasmic signals |
| Protein Size | 4/10 | x1 | **4** | 1868 aa |
| Research Novelty | 6/10 | x5 | **30** | PubMed strict ~59 |
| 3D Structure | 3/10 | x3 | **9** | PDB: 0, AF: Yes |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: 12, Pfam: 6 |
| PPI Network | 8/10 | x3 | **24** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+0.75** | |
| **Raw Total** | | | **107.8/180** | |
| **Normalized Total** | | | **59.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269, ECO:0000269 |
| UniProt | Cytoplasm, perinuclear region | ECO:0000269 |
| UniProt | Cell projection, neuron projection | ECO:0000269 |
| GO-CC | cytoplasm | IDA:UniProtKB |
| GO-CC | cytosol | TAS:Reactome |
| GO-CC | endoplasmic reticulum membrane | TAS:Reactome |
| GO-CC | membrane | IBA:GO_Central |
| GO-CC | neuron projection | IEA:UniProtKB-SubCell |
| GO-CC | nuclear body | IDA:HPA |
| GO-CC | perinuclear region of cytoplasm | IEA:UniProtKB-SubCell |
| HPA (IF) | Nuclear bodies | IF-based (Supported) |

**HPA IF Status**: IF images available; reliability: Supported.

**Nuclear Score: 6/10.** Moderate nuclear evidence, mixed with cytoplasmic signals.

- HPA IF detects: Nuclear bodies (Reliability: Supported)

- GO-CC annotations include: nuclear body

**Nuclear localization score: 6/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

1868 aa -- very large protein, may present challenges for recombinant expression and structural biology. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 59 |
| Broad query count | 92 |
| Alias note | Aliases observed but not used for scoring: MTMR5 |
| Novelty score | 6/10 |

PubMed strict count ~59 articles. Moderate-to-established field, growing literature. Score: 6/10.

**Key Publications**:

- **PMID:40998285** (2025 Nov 15) -- Selective mitophagy activation and protein aggregate accumulation in MTMR5/SBF1-deficient fibroblasts. (Life sciences)
- **PMID:39664754** (2024) -- A novel SBF1 missense mutation causes autosomal dominant Charcot-Marie-Tooth disease type 4B3. (Frontiers in neurology)
- **PMID:39461113** (2024 Dec) -- Establishment and characterization of three human pluripotent stem cell lines from Charcot-Marie-Tooth disease Type 4B3  (Stem cell research)
- **PMID:25110935** (2014 Oct) -- Recent advances in Charcot-Marie-Tooth disease. (Current opinion in neurology)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 73.8 |
| PDB Entries | 0 |
| AF pLDDT >90% | 31.1% |
| AF pLDDT <50% | 20.6% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 73.8. pLDDT distribution: >90: 31.1%, 70-90: 37.6%, 50-70: 10.7%, <50: 20.6%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR001194 | IPR001194 |
| InterPro | IPR005112 | IPR005112 |
| InterPro | IPR043153 | IPR043153 |
| InterPro | IPR004182 | IPR004182 |
| InterPro | IPR030564 | IPR030564 |
| Pfam | PF02141 | PF02141 |
| Pfam | PF02893 | PF02893 |
| Pfam | PF06602 | PF06602 |
| Pfam | PF00169 | PF00169 |
| Pfam | PF12335 | PF12335 |

InterPro domains: 12 | Pfam domains: 6. Total catalogued domains: 18.

Functional annotation: Acts as an adapter for the phosphatase MTMR2 to regulate MTMR2 catalytic activity and subcellular location (PubMed:12668758). Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form (PubMed:20937701). May function as a guanine nucleotide exchange factor (GEF) activating RAB28 (PubMed:20937701). Acts as a suppressor of autophagy in neurons (PubMed:35580604). Together with its binding partner, the phosphatase MTMR2, plays a role in dephospho

**Domain score: 8/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| MTMR2 | Combined: 0.993 | EXP: 0.756 | DB: 1 |
| MTMR1 | Combined: 0.860 | EXP: 0.704 | DB: 0 |
| FZR1 | Combined: 0.841 | EXP: 0.000 | DB: 0 |
| KMT2A | Combined: 0.755 | EXP: 0.368 | DB: 0 |
| RAB21 | Combined: 0.720 | EXP: 0.136 | DB: 0 |
| MTMR6 | Combined: 0.614 | EXP: 0.000 | DB: 0 |
| FIG4 | Combined: 0.611 | EXP: 0.000 | DB: 0 |
| SH3TC2 | Combined: 0.610 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- MTMR2 (combined score: 0.99, experimental: 0.76)
- MTMR1 (combined score: 0.86, experimental: 0.70)
- FZR1 (combined score: 0.84, experimental: 0.00)
- KMT2A (combined score: 0.76, experimental: 0.37)
- RAB21 (combined score: 0.72, experimental: 0.14)

High-confidence interactors (score >= 0.7): 5. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 8/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Multi-source consistent |
| Function | Literature + GO | Acts as an adapter for the phosphatase MTMR2 to regulate MTMR2 catalytic activity and subcellular location (PubMed:12668 | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Weak cross-validation signal. Bonus: +0.75/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 107.8/180 (59.9/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Moderate nuclear evidence, mixed with cytoplasmic signals
2. PubMed count: 59 articles 
3. Protein size: 1868 aa -- suboptimal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 5 high-confidence
6. Domain architecture: 12 InterPro + 6 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 6 > 3, PubMed 59 <= 100). Total score: 107.8/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O95248
- HPA: https://www.proteinatlas.org/ENSG00000100241-SBF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SBF1%22
- STRING: https://string-db.org/ (search SBF1)
- IntAct: https://www.ebi.ac.uk/intact/ (search SBF1)
- Harvest packet: SBF1.json

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95248 |
| SMART | SM00801;SM00799;SM00568;SM00233;SM00800; |
| UniProt Domain [FT] | DOMAIN 7..185; /note="uDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 204..337; /note="cDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 339..440; /note="dDENN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00304"; DOMAIN 881..969; /note="GRAM"; /evidence="ECO:0000255"; DOMAIN 1121..1597; /note="Myotubularin phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00669"; DOMAIN 1762..1866; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR001194;IPR005112;IPR043153;IPR004182;IPR030564;IPR010569;IPR011993;IPR001849;IPR029021;IPR022096;IPR037516;IPR005113; |
| Pfam | PF02141;PF02893;PF06602;PF00169;PF12335;PF03456; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100241-SBF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MTMR1 | Biogrid, Opencell | true |
| MTMR2 | Biogrid, Opencell | true |
| PTGES3 | Biogrid, Opencell | true |
| CSNK2A2 | Opencell | false |
| CTTN | Opencell | false |
| KRAS | Biogrid | false |
| LAMP1 | Biogrid | false |
| PRKACA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
