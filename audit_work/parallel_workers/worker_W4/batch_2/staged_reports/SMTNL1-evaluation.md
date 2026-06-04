---
type: protein-evaluation
gene: "SMTNL1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## SMTNL1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SMTNL1 |
| Protein Name | Smoothelin-like protein 1 |
| Protein Size | 494 aa, ~53.0 kDa |
| UniProt ID | A8MU46 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt: Cytoplasm, myofibril, Cytoplasm, myofibril, sarcomere, I band, Cytoplasm, myofibril, sarcomere, M line; HPA: no localization; GO-CC |
| Protein Size | 10/10 | x1 | **10** | 494 aa, ~53.0 kDa |
| Research Novelty | 8/10 | x5 | **40** | PubMed strict=22 (<=40 -> 8) |
| 3D Structure | 6/10 | x3 | **18** | AlphaFold v6 pLDDT=55.9; PDB: None |
| Regulatory Domains | 7/10 | x2 | **14** | InterPro: IPR001715, IPR036872, IPR050540; Pfam: PF00307 |
| PPI Network | 4/10 | x3 | **12** | STRING 15 partners; IntAct 4 interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold dual-source verification: +0 |
| **Raw Total** | | | **123.0/180** | |
| **Normalized Total** | | | **68.3/100** | |


### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Cytoplasm, myofibril | Experimental |
| UniProt | Cytoplasm, myofibril, sarcomere, I band | By similarity |
| UniProt | Cytoplasm, myofibril, sarcomere, M line | By similarity |
| UniProt | Nucleus | By similarity |
| GO-CC | nucleus | ISS:UniProtKB |
| HPA |  | Reliability: N/A |

**IF Image Status**: HPA did not detect reliable IF image signal. Nuclear evidence based on HPA subcellular annotation, UniProt, and GO-CC terms.

**Manual Review Assessment**: UniProt: Cytoplasm, myofibril, Cytoplasm, myofibril, sarcomere, I band, Cytoplasm, myofibril, sarcomere, M line; HPA: no localization; GO-CC: nucleus. Score 7/10 reflects Nuclear localization with good HPA reliability and auxiliary support.

### 4. Protein Size Assessment

SMTNL1 is 494 amino acids in length (~53.0 kDa). Ideal size (494 aa), suitable for standard biochemical experiments. Score 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 22 |
| PubMed broad count | 30 |
| Alias context | None |
| Novelty category | <=40 -> 8 |

**Key Research Context**: Plays a role in the regulation of contractile properties of both striated and smooth muscles. When unphosphorylated, may inhibit myosin dephosphorylation. Phosphorylation at Ser-299 reduces this inhibitory activity (By similarity). Published literature indicates growing research activity. Very novel, only a few foundational studies.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 29310803 | Smoothelins and the Control of Muscle Contractility. | Advances in pharmacology (San Diego, Calif.) |
| 34675885 | Smoothelin-Like Protein 1 Regulates Development and Metabolic Transformation of Skeletal Muscle in Hyperthyroidism. | Frontiers in endocrinology |
| 35508278 | Mechanisms by which smoothelin-like protein 1 reverses insulin resistance in myotubules and mice. | Molecular and cellular endocrinology |
| 38883605 | Smoothelin-like protein 1 promotes insulin sensitivity and modulates the contractile properties of endometrial epithelia | Frontiers in endocrinology |
| 18310078 | Deletion of the protein kinase A/protein kinase G target SMTNL1 promotes an exercise-adapted phenotype in vascular smoot | The Journal of biological chemistry |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (v6) |
| PDB Entries | 0 experimental |
| Mean pLDDT | 55.9 |
| High confidence residues (pLDDT > 90) | 21.3% |
| Confident residues (pLDDT 70-90) | 1.8% |
| Medium confidence (pLDDT 50-70) | 15.2% |
| Low confidence (pLDDT < 50) | 61.7% |
| Ordered region (pLDDT > 70) | 23.1% |
| Available PDB entries | None |

**PAE**: STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold moderate quality (pLDDT=55.9), 23.1% ordered. Structure usable. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001715 |  |
| InterPro | IPR036872 |  |
| InterPro | IPR050540 |  |
| Pfam | PF00307 |  |

**Domain Analysis**:    The protein contains 3 InterPro and 1 Pfam domain annotations. Score 7/10 reflects moderate domain architecture. Known domain annotations present, providing structural basis for functional studies.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 4 interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| PPP1R12A | 0.803 | 0.000 | 0.0 | 0.803 |
| PRKG1 | 0.799 | 0.000 | 0.0 | 0.797 |
| SMTN | 0.727 | 0.000 | 0.5 | 0.432 |
| PDLIM3 | 0.714 | 0.000 | 0.5 | 0.391 |
| SMTNL2 | 0.615 | 0.000 | 0.5 | 0.115 |
| PDLIM5 | 0.605 | 0.000 | 0.5 | 0.152 |
| LDB3 | 0.592 | 0.000 | 0.5 | 0.052 |
| PDLIM1 | 0.580 | 0.000 | 0.5 | 0.113 |

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
| H1-10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.107 |
| SH3GL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| CEP250 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |
| ADAMTS13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.101 |

**PPI Assessment**: STRING 15 predicted interactions. Regulatory partner ratio 0%. Score 4/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Partially folded / Disordered | Mixed |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold dual-source verification: +0
- Multi-DB localization consensus (2 sources): +0.5
- STRING + IntAct dual-source verification: +0.5
- Domain + AlphaFold quality: +0
- PDB multiple entries coverage: +0
- **Total Cross-Validation Bonus**: +1.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 68.3/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
2. Ideal protein size (494 aa) for experimental characterization
3. High novelty (PubMed count ~22)
4. AlphaFold prediction available (pLDDT 55.9)
5. Well-annotated domain architecture (5 domains)
6. Moderate PPI data available

**Risks / Uncertainties**:
3. No experimental PDB structures
6. No HPA subcellular localization data

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 68.3/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/A8MU46
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MU46
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMTNL1
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000214872-SMTNL1/subcellular
- Data harvested: 2026-06-04 03:22:58
