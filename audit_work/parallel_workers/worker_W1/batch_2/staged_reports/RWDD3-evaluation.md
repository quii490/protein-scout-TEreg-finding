---
type: protein-evaluation
gene: "RWDD3"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RWDD3 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RWDD3 / RSUME |
| Protein Name | RWD domain-containing protein 3 |
| Protein Size | 267 aa, ~30.5 kDa |
| UniProt ID | Q9Y3V2 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Experimental nuclear localization (ECO:0000269) |
| Protein Size | 10/10 | x1 | **10** | 267 aa, ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~18 (11-20) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold good confidence (mean pLDDT 81.6, >90%: 24.0%); Experimental PDB: 2EBK, 4Y1L |
| Regulatory Domains | 7/10 | x2 | **14** | 4 annotated domains (InterPro: 3, Pfam: 1) |
| PPI Network | 5/10 | x3 | **15** | STRING: 3 experimentally validated PPIs; IntAct: 4 interactions |
| Cross-Validation Bonus | -- | -- | **+2.5** | UniProt nuclear annotation (+0.5); Domain (4) + AlphaFold (pLDDT 82) consistency (+0.5); STRING + IntAct cross-validatio |
| **Raw Total** | | | **133.5/180** | |
| **Normalized Total** | | | **74.2/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| UniProt | Cytoplasm | Experimental |
| GO-CC | nucleus | IEA:UniProtKB-SubCell |
| HPA | No localization data | Reliability: N/A |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269). Score 7/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RWDD3 is 267 amino acids in length (~30.5 kDa). 267 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 18 |
| PubMed broad count | 35 |
| Novelty category | PubMed ~18 (11-20) |

**Key Research Context**: Enhancer of SUMO conjugation. Via its interaction with UBE2I/UBC9, increases SUMO conjugation to proteins by promoting the binding of E1 and E2 enzymes, thioester linkage between SUMO and UBE2I/UBC9 and transfer of SUMO to specific target proteins which include HIF1A, PIAS, NFKBIA, NR3C1 and TOP1. I.... Published literature includes studies on RWDD3's role in cellular processes. PubMed count of ~18 articles, indicating moderate novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 35528020 | Impact of RSUME Actions on Biomolecular Modifications in Physio-Pathological Pro... | Frontiers in endocrinology |
| 31864228 | Modifications in the cellular proteome and their clinical application.... | Medicina |
| 29436665 | MicroRNA-375 inhibits glioma cell proliferation and migration by downregulating ... | Oncology reports |
| 34768754 | Novel and Annotated Long Noncoding RNAs Associated with Ischemia in the Human He... | International journal of molecular scien |
| 29622689 | Protein stabilization by RSUME accounts for PTTG pituitary tumor abundance and o... | Endocrine-related cancer |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 2 experimental |
| Mean pLDDT | 81.6 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold good confidence (mean pLDDT 81.6, >90%: 24.0%); Experimental PDB: 2EBK, 4Y1L. Score 8/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR006575 | Annotated domain |
| InterPro | IPR038840 | Annotated domain |
| InterPro | IPR016135 | Annotated domain |
| Pfam | PF05773 | Annotated family |

**Domain Analysis**: 4 annotated domains (InterPro: 3, Pfam: 1). The protein contains 3 InterPro and 1 Pfam domain annotations. Score 7/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 9 total interactions |
| IntAct | 4 interactions |
| UniProt Interactions | 0 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| UBE2I | 0.991 | 0.926 | 0.4 | 0.829 |
| SUMO1 | 0.753 | 0.292 | 0.4 | 0.446 |
| VHL | 0.692 | 0.510 | 0.0 | 0.399 |
| HIF1A | 0.676 | 0.510 | 0.0 | 0.364 |
| SAE1 | 0.568 | 0.000 | 0.4 | 0.311 |
| UBA2 | 0.551 | 0.000 | 0.4 | 0.272 |
| SENP1 | 0.542 | 0.000 | 0.0 | 0.542 |
| RANBP2 | 0.510 | 0.000 | 0.0 | 0.503 |

**PPI Assessment**: STRING: 3 experimentally validated PPIs; IntAct: 4 interactions. Score 5/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- UniProt nuclear annotation (+0.5)
- Domain (4) + AlphaFold (pLDDT 82) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +2.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 74.2/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Moderate PPI data available

**Risks / Uncertainties**:
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 74.2/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3V2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9Y3V2-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RWDD3%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000122481-RWDD3
