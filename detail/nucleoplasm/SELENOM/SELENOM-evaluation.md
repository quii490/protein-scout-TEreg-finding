---
type: protein-evaluation
gene: "SELENOM"
date: 2026-06-04
tags: [protein-scout, batch-2, worker-W2]
status: accepted
---

## SELENOM -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SELENOM / SELM |
| Protein Name | Selenoprotein M |
| Protein Size | ~145 aa (16.2 kDa) |
| UniProt ID | Q8WWX9 |
| Evaluation Date | 2026-06-04 |
| Source | Harvest packet (SELENOM.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | Weak/minor nuclear signal -- primarily non-nuclear protein |
| Protein Size | 4/10 | x1 | **4** | 145 aa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict ~31 |
| 3D Structure | 0/10 | x3 | **0** | PDB: 0, AF: No |
| Regulatory Domains | 5/10 | x2 | **10** | InterPro: 4, Pfam: 1 |
| PPI Network | 6/10 | x3 | **18** | STRING: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.00** | |
| **Raw Total** | | | **89.0/180** | |
| **Normalized Total** | | | **49.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| UniProt | Cytoplasm, perinuclear region | ECO:0000269 |
| UniProt | Endoplasmic reticulum | ECO:0000305 |
| UniProt | Golgi apparatus | ECO:0000305 |
| GO-CC | endoplasmic reticulum lumen | IBA:GO_Central |
| GO-CC | Golgi apparatus | IEA:UniProtKB-SubCell |
| GO-CC | perinuclear region of cytoplasm | IEA:UniProtKB-SubCell |
| HPA (IF) | Nucleoplasm | IF-based (Approved) |
| HPA (IF) | Cytosol | IF-based (Approved) |

**HPA IF Status**: IF images available; reliability: Approved.

**Nuclear Score: 4/10.** Weak/minor nuclear signal -- primarily non-nuclear protein.

- HPA IF detects: Nucleoplasm (Reliability: Approved)

**Nuclear localization score: 4/10.** Above the <=3 rejection threshold.

### 4. Protein Size Assessment

145 aa -- small protein, at the lower boundary of the workable range. Score: 4/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | 31 |
| Broad query count | 73 |
| Alias note | Aliases observed but not used for scoring: SELM |
| Novelty score | 8/10 |

PubMed strict count ~31 articles. Moderate novelty, some literature but significant unknowns remain. Score: 8/10.

**Key Publications**:

- **PMID:38001759** (2023 Oct 25) -- Deciphering the Role of Selenoprotein M. (Antioxidants (Basel, Switzerland))
- **PMID:28917051** (2018) -- Selenocysteine-Mediated Expressed Protein Ligation of SELENOM. (Methods in molecular biology (Clifton, N.J.))
- **PMID:27645994** (2016 Nov 11) -- Selenoprotein Gene Nomenclature. (The Journal of biological chemistry)
- **PMID:30648404** (2021 Oct 1) -- Selenoprotein M Promotes Hypothalamic Leptin Signaling and Thioredoxin Antioxidant Activity. (Antioxidants & redox signaling)

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Not available |
| Mean pLDDT | N/A |
| PDB Entries | 0 |
| AF pLDDT >90% | N/A% |
| AF pLDDT <50% | N/A% |

**Structure Assessment**: No experimental PDB structures available. No AlphaFold prediction available.

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
| InterPro | IPR038219 | IPR038219 |
| InterPro | IPR039992 | IPR039992 |
| InterPro | IPR014912 | IPR014912 |
| InterPro | IPR036249 | IPR036249 |
| Pfam | PF08806 | PF08806 |

InterPro domains: 4 | Pfam domains: 1. Total catalogued domains: 5.

Functional annotation: May function as a thiol-disulfide oxidoreductase that participates in disulfide bond formation

**Domain score: 5/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
| SELENOT | Combined: 0.892 | EXP: 0.000 | DB: 0 |
| SELENOF | Combined: 0.892 | EXP: 0.000 | DB: 0 |
| SELENOK | Combined: 0.878 | EXP: 0.000 | DB: 0 |
| SELENOS | Combined: 0.876 | EXP: 0.000 | DB: 0 |
| SELENON | Combined: 0.859 | EXP: 0.000 | DB: 0 |
| SELENOO | Combined: 0.858 | EXP: 0.000 | DB: 0 |
| SELENOH | Combined: 0.801 | EXP: 0.000 | DB: 0 |
| SEPHS2 | Combined: 0.792 | EXP: 0.000 | DB: 0 |

Top STRING interaction partners:
- SELENOT (combined score: 0.89, experimental: 0.00)
- SELENOF (combined score: 0.89, experimental: 0.00)
- SELENOK (combined score: 0.88, experimental: 0.00)
- SELENOS (combined score: 0.88, experimental: 0.00)
- SELENON (combined score: 0.86, experimental: 0.00)

High-confidence interactors (score >= 0.7): 15. Total STRING interactions: 15. IntAct entries: 15.

**PPI score: 6/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | Mixed/weak nuclear signal | Partially consistent |
| Function | Literature + GO | May function as a thiol-disulfide oxidoreductase that participates in disulfide bond formation | -- |
| Structure | AF + PDB | Limited | -- |

**Cross-Validation Bonus Details**: Moderate cross-validation support. Bonus: +1.00/3.

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (WEAK). Total score 89.0/180 (49.4/100). The protein passes the hard filters but scores are modest. Consider as a backup candidate.

**Core Observations**:
1. Nuclear localization: Weak/minor nuclear signal -- primarily non-nuclear protein
2. PubMed count: 31 articles 
3. Protein size: 145 aa -- suboptimal
4. Structure: No structural data available
5. PPI network: 15 STRING interactions, 15 high-confidence
6. Domain architecture: 4 InterPro + 1 Pfam entries

### 11. Decision

**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score 4 > 3, PubMed 31 <= 100). Total score: 89.0/180.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWX9
- HPA: https://www.proteinatlas.org/ENSG00000198832-SELENOM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SELENOM%22
- STRING: https://string-db.org/ (search SELENOM)
- IntAct: https://www.ebi.ac.uk/intact/ (search SELENOM)
- Harvest packet: SELENOM.json
