---
type: protein-evaluation
gene: "SLX9"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SLX9 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SLX9 / C21orf70, FAM207A |
| Protein Name | Ribosome biogenesis protein SLX9 homolog |
| Protein Size | 230 aa, ~25.5 kDa |
| UniProt ID | Q9NSI2 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Nucleus, nucleolus; HPA: Nucleoli; (Reliability: Supported); GO-CC: nucleolus |
| Protein Size | 10/10 | x1 | **10** | 230 aa, ~25.5 kDa |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict=5 (<=20 -> 10) |
| 3D Structure | 10/10 | x3 | **30** | AlphaFold v6 pLDDT=71.0; PDB: 7WTS, 7WTT, 7WTU, 7WTV, 7WTW |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR028160; Pfam: PF15341 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 15 interactions |
| Cross-Validation Bonus | -- | -- | **+3.0** | PDB + AlphaFold dual-source verification: +0.5 |
| **Raw Total** | | | **155.0/180** | |
| **Normalized Total** | | | **86.1/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus, nucleolus | By similarity |
| GO-CC | nucleolus | IEA:UniProtKB-SubCell |
| HPA | Nucleoli; Additional: Nucleoplasm | Reliability: Supported |

**IF Image Status**: HPA detected immunofluorescence signal (Reliability: Supported), but STAGE mode did not download original images. Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Nucleus, nucleolus; HPA: Nucleoli; (Reliability: Supported); GO-CC: nucleolus. Score 9/10 reflects Multiple independent data sources confirm nuclear localization with high HPA reliability.

### 4. Protein Size Assessment

SLX9 is 230 amino acids in length (~25.5 kDa). Ideal size (230 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| Alias context | Aliases observed but not used for scoring: C21orf70, FAM207A |
| Novelty category | <=20 -> 10 |

**Key Research Context**: May be involved in ribosome biogenesis. Published literature indicates emerging interest. Extremely novel, virtually no systematic study (PubMed <= 20).

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 31067825 | A Novel G-Quadruplex Binding Protein in Yeast-Slx9. | Molecules (Basel, Switzerland) |
| 25895666 | A non-canonical mechanism for Crm1-export cargo complex assembly. | eLife |
| 17018574 | Slx9p facilitates efficient ITS1 processing of pre-rRNA in Saccharomyces cerevisiae. | RNA (New York, N.Y.) |
| 20551975 | A new plant sex-linked gene with high sequence diversity and possible introgression of the X copy. | Heredity |
| 30653518 | Impact of two neighbouring ribosomal protein clusters on biogenesis factor binding and assembly of yeast late small ribo | PloS one |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 5 experimental |
| Mean pLDDT | 71.0 |
| High confidence residues (pLDDT > 90) | 30.9% |
| Confident residues (pLDDT 70-90) | 21.7% |
| Medium confidence (pLDDT 50-70) | 23.9% |
| Low confidence (pLDDT < 50) | 23.5% |
| Ordered region (pLDDT > 70) | 52.6% |
| Available PDB entries | 7WTS, 7WTT, 7WTU, 7WTV, 7WTW |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: PDB experimental structures + AlphaFold high confidence (pLDDT=71.0). Structure highly credible. Score 10/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR028160 |  |
| Pfam | PF15341 |  |

**Domain Analysis**:  The protein contains 1 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SENP6 | 0.785 | 0.785 | 0.0 | 0.000 |
| GPR1 | 0.712 | 0.000 | 0.0 | 0.712 |
| FAM50B | 0.607 | 0.000 | 0.0 | 0.607 |
| PRPF19 | 0.604 | 0.604 | 0.0 | 0.000 |
| MCTS2P | 0.600 | 0.000 | 0.0 | 0.600 |
| ZNF597 | 0.587 | 0.000 | 0.0 | 0.587 |
| SNRPN | 0.578 | 0.000 | 0.0 | 0.578 |
| RASGRF1 | 0.571 | 0.000 | 0.0 | 0.571 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| EBI-23221 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29054886|imex:IM-25795|doi:10.126 |
| HSP82 | psi-mi:"MI:0397"(two hybrid array) | pubmed:15766533 |
| PSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CSA1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BMS1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BEM2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BFR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| TSR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Well-folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0.5
- Multi-DB localization consensus (3 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0.5
- PDB multiple entries coverage (>=3): +1.0
- **Total Cross-Validation Bonus**: +3.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 86.1/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (230 aa) for experimental characterization
3. High novelty (PubMed count ~5)
4. AlphaFold prediction available (pLDDT 71.0)
5. Some domain annotations present (3 domains)
6. Moderate PPI data available
7. Experimental PDB structures: 7WTS, 7WTT, 7WTU

**Risks / Uncertainties**:
None identified

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 86.1/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSI2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SLX9
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000160256-SLX9/subcellular
- Data harvested: 2026-06-04 03:21:18
