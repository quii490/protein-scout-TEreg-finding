---
type: protein-evaluation
gene: "SLF2"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SLF2 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SLF2 / C10orf6, FAM178A |
| Protein Name | SMC5-SMC6 complex localization factor protein 2 |
| Protein Size | 1173 aa, ~131.9 kDa |
| UniProt ID | Q8IX21 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Nucleus, Nucleus, PML body; HPA: Nucleoplasm, Vesicles; (Reliability: Approved); GO-CC: chromatin, chromosome, telomeric region, nu |
| Protein Size | 8/10 | x1 | **8** | 1173 aa, ~131.9 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=17 (<=20 -> 10) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=55.0; PDB: 7T5P |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR044276, IPR026161; Pfam: PF14816 |
| PPI Network | 8/10 | x3 | **24** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **143.5/180** | |
| **Normalized Total** | | | **79.7/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Experimental |
| UniProt | Nucleus, PML body | Experimental |
| GO-CC | chromatin | IDA:UniProtKB |
| GO-CC | chromosome, telomeric region | NAS:ComplexPortal |
| GO-CC | nucleoplasm | IDA:HPA |
| GO-CC | nucleus | IDA:UniProtKB |
| GO-CC | PML body | IDA:UniProtKB |
| HPA | Nucleoplasm, Vesicles | Reliability: Approved |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Approved), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nucleus, Nucleus, PML body; HPA: Nucleoplasm, Vesicles; (Reliability: Approved); GO-CC: chromatin, chromosome, telomeric region, nucleoplasm. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SLF2 is 1173 amino acids in length (~131.9 kDa). Acceptable size (1173 aa), suitable for routine experiments. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 17 |
| PubMed broad count | 30 |
| Alias context | Aliases observed but not used for scoring: C10orf6, FAM178A |
| Novelty category | <=20 -> 10 |

**Key Research Context**: Plays a role in the DNA damage response (DDR) pathway by regulating postreplication repair of UV-damaged DNA and genomic stability maintenance (PubMed:25931565). The SLF1-SLF2 complex acts to link RAD18 with the SMC5-SMC6 complex at replication-coupled interstrand cross-links (ICL) and DNA double-st. Published literature indicates growing research activity. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 34780483 | ATRX proximal protein associations boast roles beyond histone deposition. | PLoS genetics |
| 33811831 | The SMC5/6 complex compacts and silences unintegrated HIV-1 DNA and is antagonized by Vpr. | Cell host & microbe |
| 40883817 | Integrative single-cell and bulk transcriptomic analysis reveals the landscape of T cell mitotic catastrophe associated  | Human genomics |
| 33811915 | ON-bipolar cell gene expression during retinal degeneration: Implications for optogenetic visual restoration. | Experimental eye research |
| 37191775 | Characterization of the conserved features of the NSE6 subunit of the Physcomitrium patens SMC5/6 complex. | The Plant journal : for cell and molecular biology |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 1 experimental |
| Mean pLDDT | 55.0 |
| High confidence residues (pLDDT > 90) | 8.7% |
| Confident residues (pLDDT 70-90) | 27.7% |
| Medium confidence (pLDDT 50-70) | 7.8% |
| Low confidence (pLDDT < 50) | 55.8% |
| Ordered region (pLDDT > 70) | 36.4% |
| Available PDB entries | 7T5P |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=55.0), 36.4% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR044276 |  |
| InterPro | IPR026161 |  |
| Pfam | PF14816 |  |

**Domain Analysis**:   The protein contains 2 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SLF1 | 0.999 | 0.826 | 0.5 | 0.987 |
| SMC5 | 0.967 | 0.695 | 0.5 | 0.755 |
| SMC6 | 0.955 | 0.779 | 0.5 | 0.506 |
| NSMCE1 | 0.927 | 0.743 | 0.5 | 0.427 |
| RAD18 | 0.924 | 0.624 | 0.0 | 0.802 |
| NSMCE3 | 0.904 | 0.610 | 0.5 | 0.512 |
| NSMCE2 | 0.883 | 0.610 | 0.5 | 0.396 |
| NSMCE4A | 0.866 | 0.589 | 0.5 | 0.324 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| pelY | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-2845390 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SCHIP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| OPTN | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| NSMCE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366| |
| H2BC20P | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.107 |
| RIN3 | psi-mi:"MI:0399"(two hybrid fragment pooling approach) | pubmed:31413325|imex:IM-26801 |
| TRIM14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI Assessment**: STRING 15 predicted + IntAct 15 experimental interactions. Regulatory partner ratio 40%. Score 8/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus (3 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.5 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 79.7/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (1173 aa) for experimental characterization
3. High novelty (PubMed count ~17)
4. AlphaFold prediction available (pLDDT 55.0)
5. Some domain annotations present (4 domains)
6. Rich PPI network with experimental validation
7. Experimental PDB structures: 7T5P

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 79.7/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8IX21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IX21
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SLF2
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000119906-SLF2/subcellular
- Data harvested: 2026-06-04 03:20:04
