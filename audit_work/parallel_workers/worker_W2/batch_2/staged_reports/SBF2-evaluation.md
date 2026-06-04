---
type: protein-evaluation
gene: "SBF2"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SBF2 -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SBF2 / CMT4B2, KIAA1766, MTMR13 |
| Protein Name | Myotubularin-related protein 13 |
| Protein Size | ~1849 aa (208.5 kDa) |
| UniProt ID | Q86WG5 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SBF2.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 4/10 | x1 | **4** | 1849 aa |
| Research Novelty | 4/10 | x5 | **20** | PubMed strict ~69 |
| 3D Structure | 3/10 | x3 | **9** | PDB: 0, AF: Yes |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: 13, Pfam: 6 |
| PPI Network | 8/10 | x3 | **24** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **90.0/180** | |
| **Normalized Total** | | | **50.0/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm | ECO:0000269 |
| UniProt | Cytoplasm, perinuclear region | ECO:0000250 |
| UniProt | Membrane | ECO:0000269 |
| UniProt | Endosome membrane | ECO:0000250 |
| UniProt | Cell projection, axon | ECO:0000250 |
| GO-CC | axon | IEA:UniProtKB-SubCell |
| GO-CC | cytoplasm | IBA:GO_Central |
| GO-CC | cytosol | TAS:Reactome |
| GO-CC | endosome membrane | IEA:UniProtKB-SubCell |
| GO-CC | membrane | IDA:UniProtKB |
| GO-CC | perinuclear region of cytoplasm | IEA:UniProtKB-SubCell |
| GO-CC | vacuolar membrane | IEA:Ensembl |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Intermediate filaments | IF-based (Approved) |
| HPA (IF) | Cytosol | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

1849 aa -- very large protein, may present challenges for recombinant expression and structural biology. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 69 |
| Broad query count | 152 |
| Alias note | Aliases observed but not used for scoring: CMT4B2, KIAA1766, MTMR13 |
| Novelty score | 4/10 |

PubMed strict count ~69 articles. Well-studied gene, limited novelty. Score: 4/10.

**Key Publications**:

- **PMID:20301532** (1993) -- Charcot-Marie-Tooth Hereditary Neuropathy Overview. ()
- **PMID:30028002** (2018 Nov) -- Novel SBF2 mutations and clinical spectrum of Charcot-Marie-Tooth neuropathy type 4B2. (Clinical genetics)
- **PMID:32626753** (2020) -- Long Noncoding RNASBF2-AS1 Promotes Gastric Cancer Progression via Regulating miR-545/EMS1 Axis. (BioMed research international)
- **PMID:36754932** (2023 Apr) -- YBX1/lncRNA SBF2-AS1 interaction regulates proliferation and tamoxifen sensitivity via PI3K/AKT/MTOR signaling in breast (Molecular biology reports)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| Mean pLDDT | 73.2 |
| PDB Entries | 0 |
| AF pLDDT >90% | 25.6% |
| AF pLDDT <50% | 20.7% |

**Structure Assessment**: No experimental PDB structures available. AlphaFold prediction available (v6) with mean pLDDT: 73.2. pLDDT distribution: >90: 25.6%, 70-90: 43.3%, 50-70: 10.4%, <50: 20.7%.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR001194 | IPR001194 |
| InterPro | IPR005112 | IPR005112 |
| InterPro | IPR043153 | IPR043153 |
| InterPro | IPR004182 | IPR004182 |
| InterPro | IPR037823 | IPR037823 |
| Pfam | PF02141 | PF02141 |
| Pfam | PF02893 | PF02893 |
| Pfam | PF06602 | PF06602 |
| Pfam | PF00169 | PF00169 |
| Pfam | PF12335 | PF12335 |

InterPro domains: 13 | Pfam domains: 6. Total catalogued domains: 19.

Functional annotation: Guanine nucleotide exchange factor (GEF) which activates RAB21 and possibly RAB28 (PubMed:20937701, PubMed:25648148). Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form (PubMed:20937701, PubMed:25648148). In response to starvation-induced autophagy, activates RAB21 which in turn binds to and regulates SNARE protein VAMP8 endolysosomal transport required for SNARE-mediated autophagosome-lysosome fusion (PubMed:25648148). Acts as an ada

**Domain score: 8/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| MTMR2 | Combined: 0.991 | EXP: 0.686 | DB: 1 |
| RAB21 | Combined: 0.816 | EXP: 0.136 | DB: 0 |
| SH3TC2 | Combined: 0.788 | EXP: 0.000 | DB: 0 |
| FGD4 | Combined: 0.786 | EXP: 0.000 | DB: 0 |
| MTMR1 | Combined: 0.765 | EXP: 0.675 | DB: 0 |
| FIG4 | Combined: 0.741 | EXP: 0.000 | DB: 0 |
| GDAP1 | Combined: 0.741 | EXP: 0.000 | DB: 0 |
| ADGRD1 | Combined: 0.719 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- MTMR2 (combined score: 0.99, experimental: 0.69)
- RAB21 (combined score: 0.82, experimental: 0.14)
- SH3TC2 (combined score: 0.79, experimental: 0.00)
- FGD4 (combined score: 0.79, experimental: 0.00)
- MTMR1 (combined score: 0.77, experimental: 0.68)

High-confidence interactors (score >= 0.7): 9. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 8/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | Guanine nucleotide exchange factor (GEF) which activates RAB21 and possibly RAB28 (PubMed:20937701, PubMed:25648148). Pr | -- |
| Structure | AF + PDB | AF only | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (MODERATE). Total score 90.0/180 (50.0/100). The protein passes all hard filters and shows good characteristics for further study, though some dimensions are sub-optimal.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 69 articles 
3. Protein size: 1849 aa -- suboptimal
4. Structure: AlphaFold prediction only
5. PPI network: 15 STRING interactions, 9 high-confidence
6. Domain architecture: 13 InterPro + 6 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 69 <= 100). Total score: 90.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q86WG5
- HPA: https://www.proteinatlas.org/ENSG00000133812-SBF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SBF2%22
- STRING: https://string-db.org/ (search SBF2)
- IntAct: https://www.ebi.ac.uk/intact/ (search SBF2)
- Harvest packet: SBF2.json
