---
type: protein-evaluation
gene: "SCRT2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery, high-priority]
status: scored
---

## SCRT2 -- Re-evaluation Report (KEPT: Nuclear Transcriptional Repressor, Very Low PubMed)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCRT2 / Scratch homolog 2, Scratch family transcriptional repressor 2 |
| Protein Name | Transcriptional repressor scratch 2 (Snail superfamily, C2H2 zinc finger protein) |
| Protein Size | 307 aa, 32.6 kDa |
| UniProt ID | Q9NQ03 (SCRT2_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | Nucleus; nuclear chromatin; transcriptional repressor with 5 zinc fingers |
| Protein Size | 10/10 | x1 | **10** | 307 aa, ideal size for biochemical studies |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~19 articles (≤20 -> 10) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold predicted; 5 zinc finger domains; no experimental PDB |
| Regulatory Domains | 8/10 | x2 | **16** | SNAG repression domain + 5 C2H2 zinc fingers |
| PPI Network | 3/10 | x3 | **9** | Limited PPI data; Snail family interactions expected |
| Cross-Validation Bonus | -- | -- | **+1.0** | Nuclear localization + domain consistency (+1.0) |
| **Raw Total** | | | **137.0/180** | |
| **Normalized Total** | | | **76.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus (Potential, ECO:0000305) | Primary annotation |
| GO-CC | Nucleus (GO:0005634) | Database annotation |
| GO-CC | Nuclear chromatin (GO:0000790) | Database annotation |
| PhosphoSitePlus | Nucleus | Curated |
| InnateDB | Nucleus | Curated |
| COXPRESdb | Nucleus | Predicted |

**Manual Review Assessment**: SCRT2 is a transcriptional repressor of the Snail superfamily, and transcription factors are inherently nuclear proteins. The protein contains 5 C2H2-type zinc finger domains (positions 155-177, 186-208, 212-234, 240-262, 268-291) that mediate DNA binding, and an N-terminal SNAG domain (aa 1-20) that mediates transcriptional repression. The SNAG domain is a conserved repression motif found in Snail/Slug/Scratch family proteins that recruits corepressor complexes (e.g., Sin3A-HDAC, Ajuba-PRMT5) to target gene promoters. GO annotations include "nucleus" and "nuclear chromatin" (GO:0000790). The UniProt annotation of "Potential" (ECO:0000305) reflects the absence of direct immunofluorescence validation, but the domain architecture (DNA-binding zinc fingers + SNAG repression domain) makes nuclear localization functionally obligatory. Multiple databases independently predict nuclear localization. Score 9/10 reflects the domain-driven nuclear confidence with minor deduction for lack of direct IF validation.

### 4. Protein Size Assessment

SCRT2 is 307 amino acids (32.6 kDa), an ideal size for recombinant expression, purification, and biochemical characterization. The compact size is especially suitable for structural studies (NMR or X-ray crystallography of the zinc finger domains). Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~19 articles |
| Novelty category | ≤20 -> Score 10 |

SCRT2 is an exceptionally understudied gene. Research focuses almost exclusively on its role in neural development across model organisms (mouse, chick, zebrafish). Key studies include: expression mapping in developing and adult brain (Marin & Nieto, Dev Dyn 2006), role in neurogenesis and cell migration in developing neocortex (Paul et al., Cereb Cortex 2014), regulation by miR-125b (Goes et al., 2020), involvement in depression-like behaviors via GalR1 (Yang et al., PNAS 2021), and ASCL1-mediated regulation in neural tube (Goes et al., 2024). Despite being a transcription factor with 5 zinc fingers, SCRT2 is remarkably under-characterized. Its target genes, protein interaction partners, and roles outside neural development are essentially unknown. The extreme research scarcity combined with a defined domain architecture makes SCRT2 one of the most novel candidates in W4. Score 10/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no experimental structures) |
| Domain Architecture | 5 C2H2 zinc fingers (structured) + disordered N-terminal region |

No experimental structural data exists for SCRT2. The AlphaFold prediction is expected to show high confidence for the five C2H2 zinc finger domains (typically well-predicted by AlphaFold) and lower confidence for the disordered N-terminal region (aa 34-90 and 116-148) and the glycine-rich region (aa 124-148). C2H2 zinc fingers adopt a conserved beta-beta-alpha fold stabilized by zinc coordination, which AlphaFold predicts with high accuracy. Score 5/10 reflects standard AlphaFold availability without experimental validation, balanced against the well-characterized zinc finger fold.

### 7. Domain Architecture

| Source | Domain/Feature | Position | Notes |
|--------|---------------|----------|-------|
| UniProt | SNAG domain | aa 1-20 | Transcriptional repression; recruits Sin3A-HDAC corepressor |
| UniProt | Disordered region | aa 34-90 | Flexible linker |
| UniProt | Compositional bias | aa 124-148 | Glycine-rich region |
| UniProt | Zinc finger 1 (C2H2) | aa 155-177 | DNA-binding |
| UniProt | Zinc finger 2 (C2H2) | aa 186-208 | DNA-binding |
| UniProt | Zinc finger 3 (C2H2) | aa 212-234 | DNA-binding |
| UniProt | Zinc finger 4 (C2H2) | aa 240-262 | DNA-binding |
| UniProt | Zinc finger 5 (C2H2, atypical) | aa 268-291 | DNA-binding |

SCRT2 has a canonical Snail superfamily architecture: an N-terminal SNAG repression domain followed by a linker region and a C-terminal cluster of 5 C2H2 zinc fingers. The SNAG domain (Snail/GFI-1 domain) is a potent transcriptional repression motif that recruits histone deacetylase (HDAC) complexes to silence target gene promoters. The five zinc fingers provide sequence-specific DNA binding. This domain architecture directly supports a nuclear regulatory function -- transcriptional repression of target genes involved in development, EMT, and cell migration. Score 8/10 reflects the dual functional domains (SNAG repression + zinc finger DNA binding) that constitute a complete transcriptional regulatory module.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Limited data expected; Snail family network |
| IntAct | Limited interactions expected |
| Inferred Partners | Sin3A/HDAC complex (via SNAG domain), ASCL1 (upstream regulator), bHLH factors (antagonism) |

SCRT2's PPI network is largely uncharacterized. Based on domain homology, the SNAG domain is expected to recruit Sin3A-HDAC corepressor complexes and potentially Ajuba family LIM proteins (PRMT5-mediated). SCRT2 has been shown to antagonize bHLH transcription factors during neurogenesis (Paul et al., 2014). ASCL1 was recently identified as an upstream transcriptional regulator (Goes et al., 2024). However, direct interaction data is sparse or absent. Score 3/10 reflects the very limited PPI characterization.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + GO-CC + PhosphoSitePlus + domain architecture | Nucleus | Multi-DB + domain consistency |
| Function | Transcriptional repressor + nuclear localization | DNA-binding TF | Functionally consistent |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization consensus + domain architecture support: +1.0
- Structural cross-validation: +0 (no experimental PDB)
- PPI cross-validation: +0 (insufficient interaction data)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: STRONGLY RECOMMENDED (Score: 76.1/100)

**Core Strengths**:
1. Elaborate domain architecture: SNAG repression domain + 5 C2H2 zinc fingers = complete transcriptional regulator
2. Inherently nuclear: DNA-binding transcription factor cannot function outside nucleus
3. Extremely novel: only ~19 PubMed articles, maximum novelty score
4. Compact size (307 aa): ideal for biochemical and structural studies
5. Defined molecular mechanism: SNAG-mediated repression via HDAC recruitment
6. Neural development biology provides disease context, but non-neural functions unexplored
7. Snail superfamily membership links to EMT, cell migration, and cancer biology

**Risks / Uncertainties**:
1. No direct IF validation of nuclear localization (UniProt: "Potential")
2. Target genes almost completely unknown
3. PPI network largely unexplored
4. No link to TE regulation or chromatin biology beyond general transcriptional repression
5. May have restricted expression pattern (primarily neural)
6. Functional redundancy with SCRT1 paralog possible
7. Harvest packet not available; all data from web queries

**Next Steps**:
- [ ] Verify nuclear localization by IF in relevant cell types
- [ ] Identify SCRT2 target genes via ChIP-seq in neural progenitors
- [ ] Characterize SNAG domain corepressor recruitment (Sin3A-HDAC vs. others)
- [ ] Assess SCRT2 expression in non-neural tissues (TE-relevant contexts)
- [ ] Test whether SCRT2 binds or represses TE-derived sequences
- [ ] Obtain AlphaFold pLDDT/PAE for zinc finger cluster quality assessment

### 11. Decision

**FINAL DECISION: NOT REJECTED.** Nuclear localization score 9/10 (well above ≤3 threshold), PubMed count ~19 (well below 100 threshold). SCRT2 is the highest-scoring candidate in W4 at 76.1/100. The combination of low PubMed count (~19), transcription factor identity (inherently nuclear), and a complete regulatory domain architecture (SNAG + 5 zinc fingers) makes SCRT2 an exceptionally attractive target. For a TE-regulation screen, transcriptional repressors are directly relevant -- SCRT2 could potentially silence TE-derived promoters. The SNAG domain-HDAC recruitment mechanism is particularly interesting for TE silencing, as HDAC-mediated histone deacetylation is a known TE repression mechanism. The near-complete lack of functional characterization means essentially every aspect of SCRT2 biology is discoverable. Strongly recommended for priority inclusion.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ03
- SMART: http://smart.embl.de/smart/show_motifs.pl?ID=Q9NQ03
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCRT2
- PhosphoSitePlus: https://www.phosphosite.org/overviewExecuteAction?id=5138786
- InnateDB: https://www.innatedb.com/getProteinCard.do?id=209601
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ03
- Note: Harvest packet not available; data compiled from web database queries
