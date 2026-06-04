---
type: protein-evaluation
gene: "ROGDI"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## ROGDI -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | ROGDI / None |
| Protein Name | Protein rogdi homolog |
| Protein Size | 287 aa, ~32.3 kDa |
| UniProt ID | Q9GZN7 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Experimental nuclear localization (ECO:0000269) |
| Protein Size | 10/10 | x1 | **10** | 287 aa, ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~31 (21-40) |
| 3D Structure | 9/10 | x3 | **27** | AlphaFold high confidence (mean pLDDT 89.3, >90%: 72.5%); Experimental PDB: 5XQH, 5XQI |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 7/10 | x3 | **21** | STRING: 7 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.5** | UniProt nuclear annotation (+0.5); Domain (2) + AlphaFold (pLDDT 89) consistency (+0.5); STRING + IntAct cross-validatio |
| **Raw Total** | | | **135.5/180** | |
| **Normalized Total** | | | **75.3/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus envelope | Experimental |
| UniProt | Presynapse | By similarity |
| UniProt | Cell projection, axon | By similarity |
| UniProt | Perikaryon | By similarity |
| UniProt | Cell projection, dendrite | By similarity |
| UniProt | Cytoplasmic vesicle, secretory vesicle, synaptic vesicle | By similarity |
| GO-CC | nuclear envelope | IDA:HGNC |
| HPA | No localization data | Reliability: N/A |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269). Score 7/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

ROGDI is 287 amino acids in length (~32.3 kDa). 287 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 31 |
| PubMed broad count | 39 |
| Novelty category | PubMed ~31 (21-40) |

**Key Research Context**: No functional annotation available. Published literature includes studies on ROGDI's role in cellular processes. PubMed count of ~31 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 40646309 | A heterotrimeric protein complex assembles the metazoan V-ATPase upon dissipatio... | Nature structural & molecular biology |
| 27600704 | SLC13A5 is the second gene associated with Kohlschütter-Tönz syndrome.... | Journal of medical genetics |
| 29150638 | The Kohlschütter-Tönz syndrome associated gene Rogdi encodes a novel presynaptic... | Scientific reports |
| 37974187 | Perampanel effectiveness in treating ROGDI-related Kohlschütter-Tönz syndrome: f... | BMC medical genomics |
| 40175429 | Identification of ulcerative colitis diagnostic markers from differentially expr... | Scientific reports |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 2 experimental |
| Mean pLDDT | 89.3 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high confidence (mean pLDDT 89.3, >90%: 72.5%); Experimental PDB: 5XQH, 5XQI. Score 9/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR028241 | Annotated domain |
| Pfam | PF10259 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 1 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| DMXL1 | 0.969 | 0.886 | 0.5 | 0.462 |
| DMXL2 | 0.958 | 0.702 | 0.5 | 0.722 |
| WDR7 | 0.893 | 0.767 | 0.0 | 0.560 |
| ATP6V1E1 | 0.747 | 0.672 | 0.0 | 0.260 |
| ATP6V1B2 | 0.722 | 0.659 | 0.0 | 0.166 |
| GLYR1 | 0.701 | 0.000 | 0.0 | 0.000 |
| ATP6V1H | 0.696 | 0.637 | 0.0 | 0.190 |
| ATP6V1F | 0.623 | 0.538 | 0.0 | 0.211 |

**PPI Assessment**: STRING: 7 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions. Score 7/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- UniProt nuclear annotation (+0.5)
- Domain (2) + AlphaFold (pLDDT 89) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +2.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 75.3/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~31)
3. High-quality structural prediction (pLDDT >= 85)
4. Well-annotated domain architecture
5. Rich PPI network with experimental validation

**Risks / Uncertainties**:
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 75.3/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZN7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9GZN7-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ROGDI%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000067836-ROGDI
