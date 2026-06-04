---
type: protein-evaluation
gene: "RIPPLY2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: rejected
---

## RIPPLY2 -- Re-evaluation Report (REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RIPPLY2 / C6orf159 |
| Protein Name | Protein ripply2 |
| Protein Size | 128 aa, ~13.9 kDa |
| UniProt ID | Q5TAB7 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 3/10 | x4 | **12** | UniProt: Nuclear by similarity only |
| Protein Size | 7/10 | x1 | **7** | 128 aa, workable range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~31 (21-40) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold low confidence (mean pLDDT 60.9) |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 8/10 | x3 | **24** | STRING: 6 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions; UniProt curated: 12 in |
| Cross-Validation Bonus | -- | -- | **+1.3** | UniProt nuclear annotation (+0.5); Domain + AlphaFold partial consistency (+0.3); STRING + IntAct cross-validation (+0.5 |
| **Raw Total** | | | **100.3/180** | |
| **Normalized Total** | | | **55.7/100** | |

### 3. Rejection Check
**REJECTED** for: Nuclear≤3 (3/10)

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | By similarity |
| GO-CC | nucleus | ISS:UniProtKB |
| HPA | No localization data | Reliability: N/A |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nuclear by similarity only. Score 3/10 reflects weak evidence for nuclear localization. REJECTED: Nuclear score <= 3.

### 4. Protein Size Assessment

RIPPLY2 is 128 amino acids in length (~13.9 kDa). 128 aa, workable range. Score 7/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 31 |
| PubMed broad count | 0 |
| Novelty category | PubMed ~31 (21-40) |

**Key Research Context**: Plays a role in somitogenesis. Required for somite segregation and establishment of rostrocaudal polarity in somites (By similarity). Published literature includes studies on RIPPLY2's role in cellular processes. PubMed count of ~31 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 20301771 | Spondylocostal Dysostosis, Autosomal Recessive.... |  |
| 38097876 | Incomplete spinal cord injury following minor trauma in two siblings with spondy... | Spine deformity |
| 25343988 | Compound heterozygous mutations in RIPPLY2 associated with vertebral segmentatio... | Human molecular genetics |
| 25641698 | Segmental border is defined by Ripply2-mediated Tbx6 repression independent of M... | Developmental biology |
| 17937396 | Mouse Ripply2 is downstream of Wnt3a and is dynamically expressed during somitog... | Developmental dynamics : an official pub |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 60.9 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 60.9). Score 3/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR028127 | Annotated domain |
| Pfam | PF14998 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 12 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| TLE2 | 0.824 | 0.787 | 0.0 | 0.191 |
| MESP2 | 0.807 | 0.000 | 0.0 | 0.807 |
| TLE1 | 0.791 | 0.755 | 0.0 | 0.183 |
| TLE4 | 0.791 | 0.784 | 0.0 | 0.069 |
| TBX6 | 0.750 | 0.000 | 0.0 | 0.750 |
| TLE5 | 0.750 | 0.738 | 0.0 | 0.082 |
| TLE3 | 0.725 | 0.717 | 0.0 | 0.069 |
| PBX2 | 0.625 | 0.591 | 0.0 | 0.123 |

**PPI Assessment**: STRING: 6 experimentally validated PPIs (score≥0.5); IntAct: 15 interactions; UniProt curated: 12 interactions. Score 8/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Non-nuclear/Weak | Inconsistent/Weak |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- UniProt nuclear annotation (+0.5)
- Domain + AlphaFold partial consistency (+0.3)
- STRING + IntAct cross-validation (+0.5)
- **Total Cross-Validation Bonus**: +1.3 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (Score: 55.7/100)

**Core Strengths**:
1. Workable protein size (128 aa)
2. Moderate novelty (PubMed count ~31)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Rich PPI network with experimental validation

**Risks / Uncertainties**:
1. Nuclear localization score <= 3, automatic rejection criterion
3. No experimental PDB structures
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: REJECTED. Rejected for: Nuclear≤3 (3/10).

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5TAB7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q5TAB7-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RIPPLY2%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000203877-RIPPLY2
