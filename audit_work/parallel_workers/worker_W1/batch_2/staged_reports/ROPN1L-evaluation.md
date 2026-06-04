---
type: protein-evaluation
gene: "ROPN1L"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## ROPN1L -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | ROPN1L / ASP, RSPH11 |
| Protein Name | Ropporin-1-like protein |
| Protein Size | 230 aa, ~26.1 kDa |
| UniProt ID | Q96C74 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | HPA: Nuclear detected (Primary cilium transition zone) |
| Protein Size | 10/10 | x1 | **10** | 230 aa, ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~21 (21-40) |
| 3D Structure | 9/10 | x3 | **27** | AlphaFold high confidence (mean pLDDT 85.7, >90%: 64.8%); Experimental PDB: 8J07 |
| Regulatory Domains | 4/10 | x2 | **8** | 1 annotated domain |
| PPI Network | 4/10 | x3 | **12** | STRING: No interactions found; IntAct: 10 interactions; UniProt curated: 7 interactions |
| Cross-Validation Bonus | -- | -- | **+1.3** | Domain + AlphaFold partial consistency (+0.3); Experimental PDB structural validation (+1.0) |
| **Raw Total** | | | **113.3/180** | |
| **Normalized Total** | | | **62.9/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cell projection, cilium, flagellum | By similarity |
| UniProt | Cell projection, cilium | Experimental |
| GO-CC | nucleoplasm | IDA:HPA |
| HPA | Nucleoplasm, Vesicles, Primary cilium transition zone, Mid piece, Principal piece, End piece | Reliability: Supported |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: HPA: Nuclear detected (Primary cilium transition zone). Score 5/10 reflects moderate evidence for nuclear localization.

### 4. Protein Size Assessment

ROPN1L is 230 amino acids in length (~26.1 kDa). 230 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 21 |
| PubMed broad count | 37 |
| Novelty category | PubMed ~21 (21-40) |

**Key Research Context**: Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia. Important for male fertility. With ROPN1, involved in fibrous sheath integrity and sperm motility, plays a role in PKA-dependent signaling processes required for spermatozoa capacitat.... Published literature includes studies on ROPN1L's role in cellular processes. PubMed count of ~21 articles, indicating an established research field.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 40538010 | Machine Learning-Driven Discovery of TRIM Genes as Diagnostic Biomarkers for Idi... | Medical science monitor : international  |
| 25124046 | Opisthorchis viverrini: analysis of the sperm-specific rhophilin associated tail... | Acta tropica |
| 38027210 | RNA sequencing profiles reveals progressively reduced spermatogenesis with progr... | Frontiers in endocrinology |
| 35207567 | Omics and Male Infertility: Highlighting the Application of Transcriptomic Data.... | Life (Basel, Switzerland) |
| 23303679 | Loss of R2D2 proteins ROPN1 and ROPN1L causes defects in murine sperm motility, ... | Biology of reproduction |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 experimental |
| Mean pLDDT | 85.7 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold high confidence (mean pLDDT 85.7, >90%: 64.8%); Experimental PDB: 8J07. Score 9/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR047844 | Annotated domain |

**Domain Analysis**: 1 annotated domain. The protein contains 1 InterPro and 0 Pfam domain annotations. Score 4/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 0 total interactions |
| IntAct | 10 interactions |
| UniProt Interactions | 7 curated |



**PPI Assessment**: STRING: No interactions found; IntAct: 10 interactions; UniProt curated: 7 interactions. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Sparse |

**Cross-Validation Bonus Details**:
- Domain + AlphaFold partial consistency (+0.3)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +1.3 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 62.9/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. Moderate novelty (PubMed count ~21)
3. High-quality structural prediction (pLDDT >= 85)
4. Some domain annotations present
5. Moderate PPI data available

**Risks / Uncertainties**:
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 62.9/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96C74
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q96C74-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ROPN1L%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000145491-ROPN1L
