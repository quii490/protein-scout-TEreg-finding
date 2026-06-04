---
type: protein-evaluation
gene: "RTRAF"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RTRAF -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RTRAF / C14orf166 |
| Protein Name | tRNA-splicing ligase complex subunit RTRAF |
| Protein Size | 244 aa, ~28.1 kDa |
| UniProt ID | Q9Y224 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm) |
| Protein Size | 10/10 | x1 | **10** | 244 aa, ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~3 (0-5) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold moderate confidence (mean pLDDT 71.6); Experimental PDB: 7P3A |
| Regulatory Domains | 6/10 | x2 | **12** | 2 annotated domains (InterPro: 1, Pfam: 1) |
| PPI Network | 3/10 | x3 | **9** | STRING: No interactions found; IntAct: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+2.5** | Multi-DB nuclear localization consensus (+1.0); Domain (2) + AlphaFold (pLDDT 72) consistency (+0.5); Experimental PDB s |
| **Raw Total** | | | **140.5/180** | |
| **Normalized Total** | | | **78.1/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| UniProt | Cytoplasm, cytosol | Experimental |
| UniProt | Cytoplasm, perinuclear region | Experimental |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Experimental |
| UniProt | Nucleus | Experimental |
| UniProt | Cytoplasm | Experimental |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| GO-CC | perinuclear region of cytoplasm | IDA:UniProtKB |
| HPA | Nucleoplasm | Reliability: Supported |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoplasm). Score 9/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RTRAF is 244 amino acids in length (~28.1 kDa). 244 aa, ideal range. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 3 |
| PubMed broad count | 22 |
| Novelty category | PubMed ~3 (0-5) |

**Key Research Context**: Accessory subunit of the tRNA-splicing ligase complex that acts by directly joining spliced tRNA halves to mature-sized tRNAs by incorporating the precursor-derived splice junction phosphate into the mature tRNA as a canonical 3',5'-phosphodiester (PubMed:21311021, PubMed:24870230). RNA-binding prot.... Published literature includes studies on RTRAF's role in cellular processes. PubMed count of ~3 articles, indicating extremely high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 38503217 | ER-tethered RNA-binding protein controls NADPH oxidase translation for hydrogen ... | Redox biology |
| 30833903 | hCLE/RTRAF-HSPC117-DDX1-FAM98B: A New Cap-Binding Complex That Activates mRNA Tr... | Frontiers in physiology |
| 30698749 | Combined proteomic and miRNome analyses of mouse testis exposed to an endocrine ... | Molecular human reproduction |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 experimental |
| Mean pLDDT | 71.6 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate confidence (mean pLDDT 71.6); Experimental PDB: 7P3A. Score 7/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR019265 | Annotated domain |
| Pfam | PF10036 | Annotated family |

**Domain Analysis**: 2 annotated domains (InterPro: 1, Pfam: 1). The protein contains 1 InterPro and 1 Pfam domain annotations. Score 6/10 reflects moderate domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 0 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 0 curated |



**PPI Assessment**: STRING: No interactions found; IntAct: 15 interactions. Score 3/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Sparse |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- Domain (2) + AlphaFold (pLDDT 72) consistency (+0.5)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +2.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 78.1/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Moderate PPI data available

**Risks / Uncertainties**:
5. Limited PPI network data
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 78.1/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y224
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9Y224-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RTRAF%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000087302-RTRAF
