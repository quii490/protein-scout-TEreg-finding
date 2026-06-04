---
type: protein-evaluation
gene: "SBDS"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## SBDS -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SBDS / SDS, SWDS, CGI-97 |
| Protein Name | Ribosome Maturation Protein SBDS (Shwachman-Bodian-Diamond Syndrome Protein) |
| Protein Size | 250 aa / 28.8 kDa |
| UniProt ID | Q9Y3A5 (SBDS_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | Nucleus + nucleolus + nucleoplasm + cytoplasm; ribosomal maturation |
| Protein Size | 10/10 | x1 | **10** | 250 aa, within ideal range |
| Research Novelty | REJECTED | x5 | **--** | PubMed 322 (strict) to 619 (broad); >100 threshold exceeded |
| 3D Structure | 8/10 | x3 | **24** | 6 PDB entries (2 NMR + 4 EM); multiple structural states |
| Regulatory Domains | 5/10 | x2 | **10** | Ribosome maturation factor; EIF6 release; GTPase EFL1 interaction |
| PPI Network | 8/10 | x3 | **24** | EFL1 (0.999), ribosomal proteins (RPL11, RPL4, RPL5, RPS19, etc.) |
| Cross-Validation Bonus | -- | -- | **+1.5** | Nuclear multi-DB (+0.5); PDB structural validation (+0.5); PPI multi-source (+0.5) |
| **Normalized Total** | | | **N/A** | REJECTED for PubMed >100 |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| UniProt (Swiss-Prot) | Nucleus, nucleolus | Reviewed |
| UniProt (Swiss-Prot) | Nucleus, nucleoplasm | Reviewed |
| UniProt (Swiss-Prot) | Cytoplasm, cytoskeleton, spindle | Reviewed |
| GO-CC | Nucleus (GO:0005634) | IDA:UniProtKB |
| GO-CC | Nucleolus | IDA:UniProtKB |
| GO-CC | Nucleoplasm | IDA:HPA |
| GO-CC | Cytoplasm | IDA:UniProtKB |
| GO-CC | Cytosol | IDA:HPA |
| GO-CC | Spindle pole | IDA:UniProtKB |
| HPA | Nucleoplasm (additional), Cytosol (main) | Supported |

**HPA IF Status**: HPA IF images available (if_display_images_available). Subcellular location: Cytosol (main) + Nucleoplasm (additional). HPA reliability: Supported.

**Manual Review Assessment**: SBDS is a dual-localized protein with well-documented presence in both the nucleus (nucleoplasm, nucleolus) and cytoplasm (cytosol, spindle). Its primary function in ribosome maturation involves both compartments: it triggers the GTP-dependent release of EIF6 from 60S pre-ribosomes in the cytoplasm, enabling 80S ribosome assembly and EIF6 recycling back to the nucleus for 60S rRNA processing. The nucleolar localization is functionally relevant to rRNA processing, and the nucleoplasmic localization relates to EIF6 recycling. HPA confirmed nucleoplasm with IDA evidence.

**Key nuclear functions**:
1. Nucleolar rRNA processing -- requires EIF6 recycling
2. Nucleoplasmic EIF6 delivery for 60S rRNA processing and nuclear export
3. DNA damage response (may play a role in cellular response to DNA damage)
4. Cell proliferation regulation

Nuclear localization score: 7/10. Well-documented nuclear presence with IDA-level evidence, but the main HPA localization is cytosol (not nucleus). Score is superseded by PubMed rejection.

### 4. Protein Size Assessment

SBDS is 250 amino acids (28.8 kDa), well within the ideal range for biochemical and structural characterization. The small size has facilitated NMR structural studies (2KDO, 2L9N). Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query (Title/Abstract) | 322 articles |
| PubMed symbol-only query | 589 articles |
| PubMed broad query | 619 articles |
| Novelty category | >100 -> REJECTED |

**REJECTION TRIGGER**: PubMed strict query returns 322 articles (>100 threshold), and broader searches return 589-619 articles. SBDS is well beyond the acceptable novelty threshold.

**Key Research Context**: SBDS is the causative gene for Shwachman-Bodian-Diamond syndrome (SDS), a rare autosomal recessive disorder characterized by exocrine pancreatic insufficiency, bone marrow dysfunction, and leukemia predisposition. The gene has been studied extensively since its identification as the SDS gene (2003). Major research themes include:

1. **Shwachman-Diamond syndrome**: Clinical genetics, genotype-phenotype correlations, patient management (>100 publications)
2. **Bone marrow failure syndromes**: SBDS in the context of inherited bone marrow failure
3. **Ribosome biogenesis**: SBDS as a ribosome maturation factor; EIF6 release mechanism
4. **Leukemia predisposition**: SBDS mutations and risk of myelodysplastic syndrome/AML
5. **Structural biology**: NMR structures (2KDO, 2L9N) + Cryo-EM structures in ribosomal context (5AN9, 5ANB, 5ANC, 6QKL)
6. **Cellular stress response**: SBDS in DNA damage response and stress resistance
7. **Model organisms**: Yeast (SDO1), mouse, zebrafish models of SDS

The gene has been reviewed extensively (>30 reviews) and is a well-established disease gene. There is no meaningful novelty premium remaining.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| PDB Entries | 6 experimental structures |
| 2KDO | NMR, chain A=1-250 (full length) |
| 2L9N | NMR, chain A=1-250 |
| 5AN9 | EM, 3.30 A, chain J=1-250 |
| 5ANB | EM, 4.10 A, chain J=1-250 |
| 5ANC | EM, 4.20 A, chain J=1-250 |
| 6QKL | EM, 3.30 A, chain J=1-250 |
| AlphaFold | mean pLDDT 74.1 (good quality) |

SBDS has excellent structural characterization. Two NMR structures (2KDO, 2L9N) provide solution-state information at full-length, and four Cryo-EM structures capture SBDS in the context of the 60S ribosomal subunit. The AlphaFold prediction (mean pLDDT 74.1) aligns well with experimental data: 3.6% >90, 59.6% at 70-90, 31.2% at 50-70, and only 5.6% <50 pLDDT. Score 8/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR018023 (SBDS, conserved site) | SBDS family signature |
| InterPro | IPR036786 (SBDS, C-terminal domain superfamily) | C-terminal domain fold |
| InterPro | IPR002140 (Ribosome maturation protein SBDS, N-terminal) | N-terminal domain |
| InterPro | IPR039100 (Shwachman-Bodian-Diamond syndrome protein) | Family-specific entry |
| Pfam | PF20268, PF09377, PF01172 | SBDS domain architecture |

SBDS contains a well-characterized three-domain architecture implicated in ribosome maturation. The N-terminal domain, central domain, and C-terminal domain each contribute to the protein's function in EIF6 release from the 60S ribosomal subunit. The domain architecture is conserved across eukaryotes and has been validated by structural and mutagenesis studies. Score 5/10.

### 8. PPI Network Analysis

| Source | Partner | Score/Evidence |
|--------|---------|----------------|
| STRING | EFL1 | 0.999 (experimental: 0.974, textmining: 0.978) |
| STRING | UBA52 | 0.934 (experimental: 0.896) |
| STRING | RPL37A | 0.932 (experimental: 0.507) |
| STRING | RPL11 | 0.902 (experimental: 0.678) |
| STRING | RPL4 | 0.897 (experimental: 0.401, textmining: 0.808) |
| STRING | RPS19 | 0.865 (experimental: 0.507) |
| STRING | EIF6 | 0.859 |
| STRING | RPL5 | 0.84 (experimental: 0.507) |
| STRING | CLN3, DNAJC21, MRTO4, RPS17, RPL35A, RPS24, TPST1 | 0.75-0.82 |
| IntAct | 15+ interactions | Co-IP, pull-down, proximity biotinylation |

SBDS has an extensive and well-validated PPI network centered on ribosomal proteins and the EIF6 release pathway. The interaction with EFL1 (combined score 0.999) is one of the strongest in STRING, reflecting the obligate partnership in triggering EIF6 release. Interactions with multiple ribosomal proteins (RPL11, RPL4, RPL5, RPS19, RPS17, RPL35A, RPS24) reflect the ribosomal context of SBDS function. Score 8/10.

### 9. Cross-Validation Analysis

SBDS biology is cross-validated across structural (6 PDB + AlphaFold pLDDT 74.1), biochemical (EFL1-EIF6 pathway), cellular (dual nuclear-cytoplasmic localization), and clinical (Shwachman-Diamond syndrome) data. Multi-database nuclear localization (UniProt + GO-CC + HPA). PDB structural validation is robust with both NMR and Cryo-EM data. PPI network is cross-validated between STRING and IntAct with high experimental scores.

**Cross-Validation Bonus Details**:
- Multi-database + HPA nuclear localization consensus: +0.5
- PDB (6 entries) + AlphaFold structural cross-validation: +0.5
- STRING + IntAct PPI cross-validation with high experimental scores: +0.5
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED for PubMed >100)

**Core Strengths**:
1. Well-documented dual nuclear/cytoplasmic localization with multiple IDA-level experimental annotations
2. Excellent structural biology (6 PDB: 2 NMR + 4 Cryo-EM) and good AlphaFold prediction (pLDDT 74.1)
3. Strong PPI network with high experimental validation scores
4. Direct disease relevance (Shwachman-Diamond syndrome, bone marrow failure)
5. Small protein size (250 aa) -- excellent for biochemical studies

**Fatal Weakness for Our Screening Purpose**:
1. PubMed strict count 322 (>100 threshold) -- well beyond acceptable novelty limit
2. Gene is the established cause of a named syndrome -- decades of clinical research
3. Ribosome biogenesis pathway is well-characterized and competitive
4. EIF6 release mechanism is structurally and biochemically defined
5. No meaningful unexplored niche for discovery-oriented screening

### 11. Decision

**FINAL DECISION**: REJECTED. PubMed strict count 322 (>100 threshold, 589-619 for broader queries). SBDS is the established causative gene for Shwachman-Diamond syndrome and has been studied for over two decades across clinical genetics, ribosome biology, structural biology, and model organism research. While SBDS would score well on nuclear localization (7/10), structure (8/10), and PPI (8/10), the complete absence of research novelty is disqualifying. The gene is a well-established disease gene with saturated research literature. There is no opportunity for novel discovery relevant to TE-regulated nuclear protein screening.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3A5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126524-SBDS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3A5
- STRING: https://string-db.org/network/9606.ENSG00000126524
- PDB: https://www.rcsb.org/search?q=SBDS
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SBDS
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/SBDS.json
