---
type: protein-evaluation
gene: "RIOX1"
date: 2026-06-04
tags: [protein-scout, re-evaluation]
status: scored
---

## RIOX1 -- Re-evaluation Report (NOT REJECTED)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RIOX1 / C14orf169, MAPJD, NO66 |
| Protein Name | Ribosomal oxygenase 1 |
| Protein Size | 641 aa, ~71.1 kDa |
| UniProt ID | Q9H6W3 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoli rim) |
| Protein Size | 8/10 | x1 | **8** | 641 aa, acceptable range |
| Research Novelty | 9/10 | x5 | **45** | PubMed ~7 (6-10) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold good confidence (mean pLDDT 79.9, >90%: 70.4%); Experimental PDB: 4CCJ, 4CCK, 4CCM, 4CCN,  |
| Regulatory Domains | 8/10 | x2 | **16** | 5 annotated domains (InterPro: 3, Pfam: 2) |
| PPI Network | 5/10 | x3 | **15** | STRING: 9 high-confidence interactions (score≥0.7); IntAct: 15 interactions |
| Cross-Validation Bonus | -- | -- | **+3.0** | Multi-DB nuclear localization consensus (+1.0); Domain (5) + AlphaFold (pLDDT 80) consistency (+0.5); STRING + IntAct cr |
| **Raw Total** | | | **147.0/180** | |
| **Normalized Total** | | | **81.7/100** | |



### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus, nucleolus | Experimental |
| UniProt | Nucleus, nucleoplasm | Experimental |
| GO-CC | nucleolus | IDA:HPA |
| GO-CC | nucleoplasm | TAS:Reactome |
| GO-CC | nucleus | ISS:UniProtKB |
| HPA | Nucleoli rim | Reliability: Supported |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: UniProt: Experimental nuclear localization (ECO:0000269); HPA: Nuclear signal (Nucleoli rim). Score 9/10 reflects strong evidence for nuclear localization with experimental support.

### 4. Protein Size Assessment

RIOX1 is 641 amino acids in length (~71.1 kDa). 641 aa, acceptable range. Score 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 7 |
| PubMed broad count | 24 |
| Novelty category | PubMed ~7 (6-10) |

**Key Research Context**: Oxygenase that can act as both a histone lysine demethylase and a ribosomal histidine hydroxylase (PubMed:23103944). Specifically demethylates 'Lys-4' (H3K4me) and 'Lys-36' (H3K36me) of histone H3, thereby playing a central role in histone code (By similarity). Preferentially demethylates trimethyla.... Published literature includes studies on RIOX1's role in cellular processes. PubMed count of ~7 articles, indicating high novelty.

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
| 29914368 | Phylogenetic and genomic analyses of the ribosomal oxygenases Riox1 (No66) and R... | BMC evolutionary biology |
| 35361830 | Four novel candidate causal variants for deficient homozygous haplotypes in Hols... | Scientific reports |
| 35210392 | RIOX1-demethylated cGAS regulates ionizing radiation-elicited DNA repair.... | Bone research |
| 36660551 | Osteoblast-Specific Overexpression of Nucleolar Protein NO66/RIOX1 in Mouse Embr... | Journal of osteoporosis |
| 34624518 | Genome-wide identification, evolution of histone lysine demethylases (KDM) genes... | Comparative biochemistry and physiology. |


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 10 experimental |
| Mean pLDDT | 79.9 |
**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: AlphaFold good confidence (mean pLDDT 79.9, >90%: 70.4%); Experimental PDB: 4CCJ, 4CCK, 4CCM, 4CCN, 4CCO. Score 8/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR003347 | Annotated domain |
| InterPro | IPR039994 | Annotated domain |
| InterPro | IPR049043 | Annotated domain |
| Pfam | PF08007 | Annotated family |
| Pfam | PF21233 | Annotated family |

**Domain Analysis**: 5 annotated domains (InterPro: 3, Pfam: 2). The protein contains 3 InterPro and 2 Pfam domain annotations. Score 8/10 reflects strong domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 15 total interactions |
| IntAct | 15 interactions |
| UniProt Interactions | 1 curated |

**Top STRING Partners**:
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RPL8 | 0.986 | 0.960 | 0.0 | 0.672 |
| PHF19 | 0.940 | 0.000 | 0.0 | 0.940 |
| SP7 | 0.920 | 0.096 | 0.0 | 0.916 |
| RIOK1 | 0.807 | 0.000 | 0.0 | 0.806 |
| RASGEF1A | 0.797 | 0.000 | 0.0 | 0.797 |
| SBNO1 | 0.796 | 0.000 | 0.0 | 0.796 |
| TGFBRAP1 | 0.782 | 0.000 | 0.0 | 0.777 |
| JMJD4 | 0.737 | 0.000 | 0.0 | 0.736 |

**PPI Assessment**: STRING: 9 high-confidence interactions (score≥0.7); IntAct: 15 interactions. Score 5/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nuclear | Consistent |
| Structure | AlphaFold + Domain architecture | Predicted folded | Consistent |
| PPI | STRING + IntAct | Multiple interactions | Consistent |

**Cross-Validation Bonus Details**:
- Multi-DB nuclear localization consensus (+1.0)
- Domain (5) + AlphaFold (pLDDT 80) consistency (+0.5)
- STRING + IntAct cross-validation (+0.5)
- Experimental PDB structural validation (+1.0)
- **Total Cross-Validation Bonus**: +3.0 / max +3.0

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 81.7/100)

**Core Strengths**:
1. Multiple sources support nuclear localization
1. Ideal protein size for experimental characterization
2. High novelty (PubMed count < 20)
3. Adequate structural prediction
4. Well-annotated domain architecture
5. Moderate PPI data available

**Risks / Uncertainties**:
6. No HPA IF experimental confirmation

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context

### 11. Decision

**FINAL DECISION**: NOT REJECTED. The protein scores 81.7/100 on the /180 scoring system. Recommended for further investigation as a TE-regulated protein target.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6W3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/AF-Q9H6W3-F1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RIOX1%22
- STRING: https://string-db.org/
- HPA: https://www.proteinatlas.org/ENSG00000170468-RIOX1
