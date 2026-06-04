---
type: protein-evaluation
gene: "SAAL1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## SAAL1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAAL1 / SPACIA1 |
| Protein Name | Serum Amyloid A-Like 1 (Synoviocyte Proliferation-Associated in Collagen-Induced Arthritis Protein 1) |
| Protein Size | 474 aa |
| UniProt ID | Q96ER3 (SAAL1_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Primary nuclear localization confirmed by UniProt; nucleoplasm annotated |
| Protein Size | 10/10 | x1 | **10** | 474 aa, within ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed <10 articles; extremely novel (≤20 -> 10) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold prediction available; no experimental PDB entries |
| Regulatory Domains | 3/10 | x2 | **6** | No canonical regulatory domains annotated; protein is largely uncharacterized |
| PPI Network | 2/10 | x3 | **6** | No characterized PPI data; completely unexplored interactome |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-source nuclear localization consistency (+0.5) |
| **Raw Total** | | | **119.5/180** | |
| **Normalized Total** | | | **66.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | Primary annotation |
| UniProt | Nucleoplasm | Active compartment |
| dbPTM | Nucleus | Curated |
| InnateDB | Nucleus | Curated |
| GO-CC (predicted) | Nucleus | Computational |

**HPA IF Status**: HPA IF original images not available. Nuclear localization assessment based on UniProt primary annotation and multiple database consensus.

**Manual Review Assessment**: SAAL1 is annotated as a nuclear protein by UniProt with nucleoplasm as its primary active compartment. The protein is also annotated with extracellular localization in some GO entries, possibly indicating secretion from synovial fibroblasts under inflammatory conditions. The gene name (Serum Amyloid A-Like 1) is misleading -- SAAL1 is not a serum amyloid protein but rather a synoviocyte proliferation-associated protein (SPACIA1) identified in collagen-induced arthritis models. The nuclear localization is the primary annotation across multiple databases. Score 8/10 reflects strong multi-database nuclear consensus but lack of HPA IF direct image verification and potential context-dependent secretion.

### 4. Protein Size Assessment

SAAL1 is 474 amino acids, well within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | <10 articles |
| Novelty category | ≤20 -> Score 10 |

SAAL1 is an extremely understudied gene. It was identified as SPACIA1 (Synoviocyte Proliferation-Associated in Collagen-Induced Arthritis Protein 1) in the context of rheumatoid arthritis research, where it was found to promote synovial fibroblast proliferation in response to pro-inflammatory stimuli. Beyond this initial characterization, almost no functional follow-up studies exist. The gene is expressed in testis, ovary, lung, spleen, and heart, but tissue-specific functions are completely unexplored. The extreme research scarcity makes SAAL1 a prime candidate for novel discovery. Score 10/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Domain Architecture | Poorly structured (no Pfam/InterPro domains) |

No experimental structural data exists for SAAL1. The AlphaFold prediction is available but confidence metrics are not available without the harvest packet. The protein lacks characterized Pfam or InterPro domains, which may indicate it is largely intrinsically disordered or has a novel fold. The absence of recognizable domain architecture is both a limitation (no structural hypotheses to guide experiments) and an opportunity (potential for novel structural biology). Score 5/10 reflects the structural unknowns balanced against standard AlphaFold availability.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | No characterized domains | Lacks canonical domain annotations |
| Pfam | No characterized domains | May contain novel domain architecture |
| dbPTM | Phosphorylation/PTM sites | Regulatory potential |

SAAL1 lacks any characterized protein domains in InterPro or Pfam. This is unusual for a 474-amino acid protein and suggests either: (1) the protein contains a novel domain architecture not yet classified; (2) the protein is largely intrinsically disordered; or (3) the protein adopts a fold that has not been captured by existing domain databases. The absence of domain annotation is both a weakness (no functional hypotheses from domain homology) and a strength (maximum discovery potential for novel biochemistry). Score 3/10 reflects the lack of domain-based functional inference.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | No data available |
| IntAct | No interactions |
| Known Partners | None characterized |

SAAL1 has a completely unexplored protein-protein interaction network. No interaction partners have been identified or validated. This is consistent with the extremely low PubMed count and the complete lack of functional characterization. Score 2/10 reflects the complete absence of PPI data.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + dbPTM + InnateDB | Nucleus | Multi-DB consensus |
| Domain | InterPro + Pfam | No domains found | Consistent absence |
| PPI | STRING + IntAct | No data | Consistent absence |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization consensus (3+ sources): +0.5
- No structural cross-validation (no PDB, unknown AF confidence): +0
- No PPI cross-validation (insufficient data): +0
- No domain-based cross-validation: +0
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 66.4/100)

**Core Strengths**:
1. Strong nuclear localization evidence from multiple databases (UniProt primary, dbPTM, InnateDB)
2. Extremely novel -- PubMed <10 articles, maximum novelty score
3. Protein size (474 aa) is experimentally tractable
4. Implicated in synovial fibroblast proliferation -- a disease-relevant context
5. Lack of characterized domains suggests potential for novel biochemistry
6. Expression in multiple tissues offers diverse biological contexts for investigation

**Risks / Uncertainties**:
1. Complete absence of functional characterization -- all biological inferences are speculative
2. No domain annotations -- no structural or functional hypotheses from homology
3. Zero characterized interaction partners
4. No experimental structural data
5. HPA IF verification of nuclear localization not available
6. "SAAL1" gene name is misleading (not a serum amyloid protein) -- may have been misclassified in older databases
7. Secreted/extracellular annotation in some contexts may indicate non-nuclear functions

**Next Steps**:
- [ ] Verify nuclear localization by immunofluorescence in relevant cell types (synovial fibroblasts)
- [ ] Perform AlphaFold structural prediction and evaluate pLDDT/PAE metrics
- [ ] Identify interaction partners via AP-MS or BioID in synovial fibroblasts
- [ ] Investigate gene regulation mechanisms (is SAAL1 itself TE-regulated?)
- [ ] Explore functional role beyond synovial proliferation (testis, ovary, lung expression)

### 11. Decision

**FINAL DECISION**: NOT REJECTED. Nuclear localization score 8/10 (well above ≤3 threshold), PubMed count <10 (well below 100 threshold). SAAL1 is one of the most novel candidates in this batch. The strong multi-database nuclear localization consensus combined with extreme research scarcity makes it an attractive target for discovery-oriented investigation. The primary risk is the complete absence of functional characterization -- essentially every aspect of SAAL1 biology remains to be discovered. This is both the greatest strength and the greatest uncertainty. SAAL1 is recommended for inclusion with the caveat that basic characterization (localization, interactome, domain function) should precede any mechanistic studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96ER3
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=SAAL1_HUMAN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAAL1
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SAAL1
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
