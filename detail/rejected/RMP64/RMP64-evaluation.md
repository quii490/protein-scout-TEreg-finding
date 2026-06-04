---
type: protein-evaluation
gene: "RMP64"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RMP64 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RMP64 / C3orf17, NEPRO |
| Protein Name | Ribonuclease MRP subunit P64 |
| Protein Size | 567 aa, ~64.6 kDa |
| UniProt ID | Q6NW34 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Experimental nuclear localization (ECO:0000269) |
| Protein Size | 10/10 | x1 | **10** | 567 aa, ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~4 (0-5) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold low confidence (mean pLDDT 64.0) |
| Regulatory Domains | 7/10 | x2 | **14** | 3 annotated domains (InterPro: 2, Pfam: 1) |
| PPI Network | 0/10 | x3 | **0** | STRING: No interactions found; IntAct: No interactions |
| Cross-Validation Bonus | -- | -- | **+0.8** | UniProt nuclear annotation (+0.5); Domain + AlphaFold partial consistency (+0.3) |
| **Raw Total** | | | **111.8/180** | |
| **Normalized Total** | | | **62.1/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| UniProt | Nucleus, nucleolus | By similarity |
| GO-CC | nucleolus | ISS:UniProtKB |
| GO-CC | nucleus | IDA:UniProtKB |
| HPA | No localization data | Reliability: N/A |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269). Score 7/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RMP64 is 567 amino acids in length (~64.6 kDa). 567 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| Novelty category | PubMed ~4 (0-5) |

**Key Research Context**: Specific component of the MRP ribonucleoprotein endoribonuclease, Rnase/Mrp complex, a ribonucleoprotein complex involved in pre-rRNA processing (PubMed:28115465, PubMed:40413743). May play a role in cortex development as part of the Notch signaling pathway. Downstream of Notch may repress the expre.... Published literature includes studies on RMP64's role in cellular processes. PubMed count of ~4 articles, indicating extremely high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 40867056 | Composition and RNA binding specificity of metazoan RNase MRP.... | Nucleic acids research |
| 41888142 | Structural and evolutionary insights into the eukaryotic RNase MRP ribonucleopro... | Nature communications |
| 40413743 | Identification of RMP24 and RMP64, human ribonuclease MRP-specific protein compo... | Cell reports |
| 41136609 | RNase MRP subunit composition and role in 40S ribosome biogenesis.... | Nature structural & molecular biology |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 experimental |
| Mean pLDDT | 64.0 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold low confidence (mean pLDDT 64.0). Score 3/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR052835 | Annotated domain |
| InterPro | IPR027951 | Annotated domain |
| Pfam | PF14780 | Annotated family |

**Domain Analysis**: 3 annotated domains (InterPro: 2, Pfam: 1). The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 0 total interactions |
| IntAct | 0 interactions |
| UniProt Interactions | 0 curated |



**PPI Assessment**: STRING: No interactions found; IntAct: No interactions. Score 0/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Sparse / None | Sparse |

**Cross-Validation Bonus Details**:
- UniProt nuclear annotation (+0.5)
- Domain + AlphaFold partial consistency (+0.3)
- **Total Cross-Validation Bonus**: +0.8 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 62.1/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture

**Risks / Uncertainties**:
3. No experimental PDB structures
5. Limited PPI network data
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 62.1/100 on the /180 scoring system. Recommended with caution for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q6NW34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q6NW34-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RMP64%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/
