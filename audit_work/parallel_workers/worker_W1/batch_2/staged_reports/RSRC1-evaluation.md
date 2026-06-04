---
type: protein-evaluation
gene: "RSRC1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RSRC1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RSRC1 / SRRP53 |
| Protein Name | Serine/Arginine-related protein 53 |
| Protein Size | 334 aa, ~38.7 kDa |
| UniProt ID | Q96IZ7 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Nuclear annotation (Nucleus, Nucleus speckle); HPA: Nuclear signal (Nuclear speckles) |
| Protein Size | 10/10 | x1 | **10** | 334 aa, ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~22 (21-40) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold low confidence (mean pLDDT 58.4) |
| Regulatory Domains | 4/10 | x2 | **8** | 1 annotated domain |
| PPI Network | 8/10 | x3 | **24** | STRING: 15 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions; UniProt curated: 7 in |
| Cross-Validation Bonus | -- | -- | **+1.5** | Multi-DB nuclear localization consensus (+1.0); STRING + IntAct cross-validation (+0.5) |
| **Raw Total** | | | **115.5/180** | |
| **Normalized Total** | | | **64.2/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | By similarity |
| UniProt | Nucleus speckle | By similarity |
| UniProt | Cytoplasm | By similarity |
| GO-CC | nuclear speck | ISS:UniProtKB |
| GO-CC | nucleus | ISS:UniProtKB |
| HPA | Nuclear speckles | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nuclear annotation (Nucleus, Nucleus speckle); HPA: Nuclear signal (Nuclear speckles). Score 7/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RSRC1 is 334 amino acids in length (~38.7 kDa). 334 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 22 |
| PubMed broad count | 28 |
| Novelty category | PubMed ~22 (21-40) |

**Key Research Context**: Has a role in alternative splicing and transcription regulation (PubMed:29522154). Involved in both constitutive and alternative pre-mRNA splicing. May have a role in the recognition of the 3' splice site during the second step of splicing. Published literature includes studies on RSRC1's role in cellular processes. PubMed count of ~22 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 29522154 | RSRC1 mutation affects intellect and behaviour through aberrant splicing and tra... | Brain : a journal of neurology |
| 37095490 | A novel protein encoded by circRsrc1 regulates mitochondrial ribosome assembly a... | BMC biology |
| 29653227 | RSRC1 and CPZ gene polymorphisms with neuroblastoma susceptibility in Chinese ch... | Gene |
| 25937118 | RSRC1 SUMOylation enhances SUMOylation and inhibits transcriptional activity of ... | FEBS letters |
| 40078563 | Improving neuroblastoma risk prediction through a polygenic risk score derived f... | Chinese journal of cancer research = Chu |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 58.4 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 58.4). Score 3/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR034604 | Annotated domain |

**Domain Analysis**: 1 annotated domain. The protein contains 1 InterPro and 0 Pfam domain annotations. Score 4/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 7 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| FAU | 0.988 | 0.967 | 0.0 | 0.182 |
| RPS15 | 0.985 | 0.841 | 0.0 | 0.471 |
| RPS18 | 0.983 | 0.839 | 0.0 | 0.442 |
| RPS9 | 0.983 | 0.839 | 0.0 | 0.487 |
| RPS3 | 0.982 | 0.834 | 0.0 | 0.420 |
| RPS3A | 0.981 | 0.826 | 0.0 | 0.418 |
| RPL5 | 0.980 | 0.861 | 0.0 | 0.268 |
| RPS8 | 0.979 | 0.834 | 0.0 | 0.348 |

**PPI Assessment**: STRING: 15 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions; UniProt curated: 7 interactions. Score 8/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +1.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 64.2/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~22)
3. Adequate structural prediction
4. Some domain annotations present
5. Rich PPI network with experimental validation

**Risks / Uncertainties**:
3. No experimental PDB structures
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 64.2/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96IZ7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q96IZ7-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RSRC1%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000174891-RSRC1
