---
type: protein-evaluation
gene: "RSRP1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RSRP1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RSRP1 / C1orf63 |
| Protein Name | Arginine/serine-rich protein 1 |
| Protein Size | 290 aa, ~33.6 kDa |
| UniProt ID | Q9BUV0 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm) |
| Protein Size | 10/10 | x1 | **10** | 290 aa, ideal range |
| Research Novelty | 9/10 | x5 | **45** | PubMed ~6 (6-10) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold low confidence (mean pLDDT 51.2) |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 4/10 | x3 | **12** | STRING: No interactions found; IntAct: 15 interactions; UniProt curated: 3 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | Multi-DB nuclear localization consensus (+1.0) |
| **Raw Total** | | | **125.0/180** | |
| **Normalized Total** | | | **69.4/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | Nucleoplasm | Reliability: Approved |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm). Score 9/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RSRP1 is 290 amino acids in length (~33.6 kDa). 290 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| Novelty category | PubMed ~6 (6-10) |

**Key Research Context**: Probably acts as a spliceosomal factor that contributes to spliceosome assembly and regulates the isoform switching of proteins such as PARP6. Published literature includes studies on RSRP1's role in cellular processes. PubMed count of ~6 articles, indicating high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 37255411 | Overlaid Transcriptional and Proteome Analyses Identify Mitotic Kinesins as Impo... | Molecular cancer research : MCR |
| 34042961 | Spliceosome-regulated RSRP1-dependent NF-κB activation promotes the glioblastoma... | Neuro-oncology |
| 33374812 | Alterations in the Genomic Distribution of 5hmC in In Vivo Aged Human Skin Fibro... | International journal of molecular scien |
| 34318869 | Functionathon: a manual data mining workflow to generate functional hypotheses f... | Database : the journal of biological dat |
| 37600067 | Analyzation of the Peripheral Blood Mononuclear Cells Atlas and Cell Communicati... | Journal of immunology research |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 51.2 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 51.2). Score 3/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR029656 | Annotated domain |
| Pfam | PF17069 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 0 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 3 curated |



**PPI Assessment**: STRING: No interactions found; IntAct: 15 interactions; UniProt curated: 3 interactions. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Sparse |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- **Total Cross-Validation Bonus**: +1.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 69.4/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 69.4/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BUV0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9BUV0-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RSRP1%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000117616-RSRP1
