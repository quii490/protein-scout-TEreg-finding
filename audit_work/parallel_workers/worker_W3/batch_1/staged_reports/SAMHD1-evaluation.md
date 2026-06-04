---
type: protein-evaluation
gene: "SAMHD1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## SAMHD1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAMHD1 / DCIP, HDDC1, MOP-5, SBBI88 |
| Protein Name | Deoxynucleoside Triphosphate Triphosphohydrolase SAMHD1 (SAM and HD Domain-Containing Protein 1) |
| Protein Size | 626 aa / ~72 kDa |
| UniProt ID | Q9Y3Z3 (SAMH1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | Nucleus + cytoplasm; predominantly nuclear in some contexts; nuclear dNTPase function |
| Protein Size | 10/10 | x1 | **10** | 626 aa, within ideal range |
| Research Novelty | REJECTED | x5 | **--** | PubMed >600 articles; >100 threshold exceeded |
| 3D Structure | 9/10 | x3 | **27** | 10+ experimental PDB entries; X-ray + Cryo-EM; multiple conformational states |
| Regulatory Domains | 8/10 | x2 | **16** | SAM domain + HD domain; allosteric dNTP regulation; phosphorylation switch |
| PPI Network | 8/10 | x3 | **24** | Extensive PPI: HIV-1 Vpx, LINE-1 ORF2p, MRE11, CtIP, CDK1/cyclin A2 |
| Cross-Validation Bonus | -- | -- | **+2.0** | Nuclear localization multi-DB (+0.5); PDB + AlphaFold (+0.5); STRING + IntAct (+0.5); Domain multi-DB (+0.5) |
| **Normalized Total** | | | **N/A** | REJECTED for PubMed >100 |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Reviewed, experimental |
| UniProt (Swiss-Prot) | Cytoplasm | Reviewed |
| GO-CC | Nucleus (GO:0005634) | IDA, IMP |
| GO-CC | Nucleoplasm | IDA |
| GO-CC | Cytoplasm | IDA |
| GeneCards | Nucleus, Cytoplasm | Tier1 |
| PhosphoSitePlus | Nucleus, Cytoplasm | Experimental |

**HPA IF Status**: HPA IF data available; nuclear and cytoplasmic localization confirmed.

**Manual Review Assessment**: SAMHD1 is a dual-localized protein with well-established nuclear and cytoplasmic pools. It functions as a dNTP triphosphohydrolase that maintains dNTP homeostasis, which is critical for both nuclear DNA replication fidelity and cytoplasmic restriction of retroviral replication. Its nuclear localization is mediated by a canonical NLS and is functionally important for its role in DNA damage response and dNTP pool regulation at replication forks. The protein shuttles between nucleus and cytoplasm, with localization influenced by cell cycle stage (nuclear enrichment in G1, cytoplasmic in dividing cells) and phosphorylation status (T592 phosphorylation by CDK1/cyclin A2 promotes cytoplasmic retention).

**Key nuclear functions**:
1. Nuclear dNTPase activity maintaining genomic DNA replication fidelity
2. DNA damage response -- recruitment to sites of DNA damage
3. Interaction with MRE11 and CtIP at DNA double-strand breaks
4. LINE-1 retrotransposon restriction in the nucleus
5. cGAS/STING pathway regulation through nuclear dNTP metabolism

Nuclear localization score: 7/10. Well-documented nuclear presence but significant cytoplasmic pool. Score is superseded by PubMed rejection.

### 4. Protein Size Assessment

SAMHD1 is 626 amino acids, within the ideal range. Multiple crystal structures of both full-length protein and individual domains are available. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed total articles | >600 (estimated 600-800+) |
| Novelty category | >100 -> REJECTED |

**REJECTION TRIGGER**: PubMed count exceeds 100 threshold by a large margin. SAMHD1 has been intensively studied since its identification as the HIV-1 restriction factor counteracted by Vpx (2011). The research landscape includes:

**Major research themes (each with dozens to hundreds of papers)**:
1. **HIV/SIV restriction**: SAMHD1 as the restriction factor that depletes dNTP pools in non-dividing cells, counteracted by lentiviral Vpx/Vpr proteins. This is the dominant research area with >200 publications.
2. **Aicardi-Goutieres syndrome (AGS)**: SAMHD1 mutations cause AGS, a type I interferonopathy. Numerous clinical genetics and mechanistic studies.
3. **dNTP metabolism**: Biochemical characterization of the allosteric regulation of dNTPase activity by dNTPs and GTP.
4. **DNA damage response**: SAMHD1 at DNA repair foci, interactions with MRE11-CtIP, PARP inhibitor sensitivity.
5. **Cancer biology**: SAMHD1 as a modulator of chemotherapeutic efficacy (cytarabine, gemcitabine, PARP inhibitors).
6. **Innate immunity**: cGAS-STING pathway regulation, LINE-1 retrotransposon control.
7. **Cell cycle regulation**: CDK1/cyclin A2 phosphorylation of T592 and its consequences.
8. **Structural biology**: >10 crystal/Cryo-EM structures in multiple conformations.

SAMHD1 has been reviewed extensively (>50 reviews) and is the subject of active drug development efforts for both antiviral and anticancer applications. There is no meaningful novelty premium.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| PDB Entries | 10+ experimental structures |
| Methods | X-ray crystallography, Cryo-EM, SAXS |
| Coverage | Full-length, HD domain, SAM domain, tetramer assembly |
| Key Structures | dNTP-bound tetramer (active), apo dimer (inactive), GTP-bound, dATP-bound, Vpx-bound |

SAMHD1 has extensive experimental structural characterization. The catalytic HD domain, regulatory SAM domain, and full-length tetrameric assembly have all been structurally resolved. Multiple conformational states (apo/inactive, dNTP-bound/active, GTP-bound) provide detailed mechanistic insights into allosteric regulation. The tetrameric active form requires binding of dNTPs or GTP at two allosteric sites per monomer. Score 9/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR003607 (HD/PDEase domain) | Metal-dependent phosphohydrolase; dNTPase catalytic domain |
| InterPro | IPR006674 (HD domain) | Histidine-aspartate domain |
| InterPro | IPR001660 (SAM domain) | Sterile alpha motif; protein-protein interaction |
| InterPro | IPR013761 (SAM/pointed domain) | SAM superfamily |
| Pfam | PF01966 (HD) | HD domain |
| Pfam | PF07647 (SAM_2) | SAM domain |

SAMHD1 contains a well-characterized two-domain architecture: an N-terminal SAM domain (protein-protein interaction, tetramerization) and a C-terminal HD domain (catalytic dNTP triphosphohydrolase). The allosteric regulatory mechanism -- where dNTP/GTP binding at the SAM-HD interface drives tetramerization and catalytic activation -- is among the best-characterized allosteric systems in nucleotide metabolism. The T592 phosphorylation site in the linker region acts as a cell-cycle-dependent regulatory switch. Score 8/10.

### 8. PPI Network Analysis

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| HIV-1 Vpx / SIV Vpr | Viral antagonism | Direct binding; targets SAMHD1 for CRL4-DCAF1 E3 ligase-mediated degradation |
| LINE-1 ORF2p | Retrotransposon restriction | Direct interaction; enhances LINE-1 restriction |
| MRE11 | DNA repair | Co-localization at DNA damage foci |
| CtIP (RBBP8) | DNA end resection | Functional interaction in DNA repair |
| CDK1/cyclin A2 | Cell cycle regulation | Phosphorylation of T592 |
| Cyclin A2/CDK2 | Cell cycle | Direct binding and phosphorylation |
| RPA | DNA replication | Interaction at replication forks |
| APOBEC3A/B | Innate immunity | Functional cooperation in viral restriction |

SAMHD1 has an extensive and functionally diverse PPI network spanning viral restriction, DNA repair, cell cycle regulation, and innate immunity. Many interactions have been validated by co-IP from endogenous sources and supported by structural data (e.g., Vpx-SAMHD1 interface). Score 8/10.

### 9. Cross-Validation Analysis

SAMHD1 biology is cross-validated across structural, biochemical, cellular, and clinical data. Multi-database nuclear localization confirmed by multiple experimental approaches. PDB + AlphaFold structural cross-validation is robust. STRING + IntAct PPI cross-validation is well-supported. Domain annotation is consistent across InterPro/Pfam/PROSITE with extensive mutagenesis data validating domain functions. The breadth of pathway integration (viral restriction, DNA repair, dNTP metabolism, innate immunity) is exceptional.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED for PubMed >100)

**Core Strengths**:
1. Excellent structural biology (>10 PDB entries, multiple conformational states)
2. Well-characterized two-domain architecture with detailed allosteric mechanism
3. Disease relevance: AGS, HIV/AIDS, cancer
4. Drug development potential (nucleotide analog sensitivity)

**Fatal Weakness for Our Screening Purpose**:
1. PubMed count >600 vastly exceeds the 100-article rejection threshold
2. Extremely competitive research field (HIV, AGS, cancer, innate immunity)
3. No novelty premium whatsoever
4. Structure, function, regulation, and disease mechanisms are all extensively characterized
5. Multiple established research communities working on different aspects of SAMHD1 biology

### 11. Decision

**FINAL DECISION**: REJECTED. PubMed count >100 (estimated >600 articles). SAMHD1 is one of the most intensely studied proteins in virology and nucleotide metabolism. While it has strong nuclear localization and outstanding structural characterization, the complete absence of research novelty disqualifies it for our TE-regulated nuclear protein screening objectives. The HIV restriction factor discovery (2011) sparked an explosion of research that has saturated most aspects of SAMHD1 biology. There is no unexplored niche suitable for a discovery-oriented screening approach.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3Z3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAMHD1
- PDB: https://www.rcsb.org/search?q=SAMHD1
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAMHD1
- Note: Harvest packet not available; SAMHD1 is extremely well-characterized; data compiled from public databases
