---
type: protein-evaluation
gene: "RMND5A"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RMND5A -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RMND5A / None |
| Protein Name | E3 ubiquitin-protein transferase RMND5A |
| Protein Size | 391 aa, ~44.0 kDa |
| UniProt ID | Q9H871 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm) |
| Protein Size | 10/10 | x1 | **10** | 391 aa, ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~16 (11-20) |
| 3D Structure | 9/10 | x3 | **27** | AlphaFold high confidence (mean pLDDT 89.9, >90%: 65.2%); Experimental PDB: 8PJN |
| Regulatory Domains | 8/10 | x2 | **16** | 10 annotated domains (InterPro: 8, Pfam: 2) |
| PPI Network | 8/10 | x3 | **24** | STRING: 14 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions; UniProt curated: 15 i |
| Cross-Validation Bonus | -- | -- | **+3.0** | Multi-DB nuclear localization consensus (+1.0); Domain (10) + AlphaFold (pLDDT 90) consistency (+0.5); STRING + IntAct c |
| **Raw Total** | | | **156.0/180** | |
| **Normalized Total** | | | **86.7/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus, nucleoplasm | Experimental |
| UniProt | Cytoplasm | Experimental |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm | Reliability: Supported |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm). Score 9/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RMND5A is 391 amino acids in length (~44.0 kDa). 391 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 16 |
| PubMed broad count | 26 |
| Novelty category | PubMed ~16 (11-20) |

**Key Research Context**: Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. MAEA and RMND5A are both required for catalytic activity of the CTLH E3 ubiquitin-protein .... Published literature includes studies on RMND5A's role in cellular processes. PubMed count of ~16 articles, indicating moderate novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 34079591 | miR-590-5p targets RMND5A and promotes migration in pancreatic adenocarcinoma ce... | Oncology letters |
| 31285494 | The mammalian CTLH complex is an E3 ubiquitin ligase that targets its subunit mu... | Scientific reports |
| 31885576 | The CTLH Complex in Cancer Cell Plasticity.... | Journal of oncology |
| 28731166 | Screening of the prognostic targets for breast cancer based co-expression module... | Molecular medicine reports |
| 40377017 | E3 ubiquitin ligase RMND5A maintains the self-renewal state of human neural stem... | FEBS letters |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 experimental |
| Mean pLDDT | 89.9 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high confidence (mean pLDDT 89.9, >90%: 65.2%); Experimental PDB: 8PJN. Score 9/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR013144 | Annotated domain |
| InterPro | IPR024964 | Annotated domain |
| InterPro | IPR006595 | Annotated domain |
| InterPro | IPR045098 | Annotated domain |
| InterPro | IPR006594 | Annotated domain |
| InterPro | IPR037680 | Annotated domain |
| Pfam | PF10607 | Annotated family |
| Pfam | PF13445 | Annotated family |

**Domain Analysis**: 10 annotated domains (InterPro: 8, Pfam: 2). The protein contains 8 InterPro and 2 Pfam domain annotations. Score 8/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 15 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| GID8 | 0.999 | 0.934 | 0.0 | 0.992 |
| RANBP9 | 0.997 | 0.934 | 0.0 | 0.959 |
| WDR26 | 0.997 | 0.890 | 0.5 | 0.947 |
| ARMC8 | 0.996 | 0.849 | 0.5 | 0.948 |
| GID4 | 0.991 | 0.859 | 0.0 | 0.941 |
| MKLN1 | 0.990 | 0.835 | 0.0 | 0.945 |
| RANBP10 | 0.977 | 0.910 | 0.0 | 0.730 |
| MAEA | 0.969 | 0.845 | 0.5 | 0.582 |

**PPI Assessment**: STRING: 14 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions; UniProt curated: 15 interactions. Score 8/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- Domain (10) + AlphaFold (pLDDT 90) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +3.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 86.7/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
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

**FINAL DECISION**: NOT REJECTED. The protein scores 86.7/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H871
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9H871-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RMND5A%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000153561-RMND5A
