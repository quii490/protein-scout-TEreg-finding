---
type: protein-evaluation
gene: "SEPHS1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery, high-priority]
status: scored
---

## SEPHS1 -- Re-evaluation Report (KEPT: Nuclear Zincore Component, Transcription Factor Stabilizer)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SEPHS1 / SPS1, SELD, Selenide water dikinase 1, Zincore component SEPHS1 |
| Protein Name | Zincore component SEPHS1 (Selenophosphate synthase 1, Selenium donor protein 1) |
| Protein Size | 392 aa, 42.9 kDa |
| UniProt ID | P49903 (SPS1_HUMAN, Swiss-Prot reviewed, annotation score 5/5) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 9/10 | x4 | **36** | Nuclear (zincore complex); direct transcription factor binding at DNA sites |
| Protein Size | 10/10 | x1 | **10** | 392 aa, well within ideal range |
| Research Novelty | 7/10 | x5 | **35** | PubMed ~40 articles (21-40 -> 8, but recent surge may push to 8) |
| 3D Structure | 8/10 | x3 | **24** | 2 experimental PDB entries (3FD5, 3FD6); AlphaFold available |
| Regulatory Domains | 8/10 | x2 | **16** | Zinc finger transcription factor binding; arginine clamp; selenophosphate synthase |
| PPI Network | 5/10 | x3 | **15** | Zincore complex (QRICH1); multiple zinc finger TFs; moderate network |
| Cross-Validation Bonus | -- | -- | **+1.5** | Nuclear localization + PDB structural validation (+1.0); Domain-function consistency (+0.5) |
| **Raw Total** | | | **137.5/180** | |
| **Normalized Total** | | | **76.4/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nuclear (via zincore complex) | Primary annotation |
| UniProt function | Binds zinc finger transcription factors at DNA-binding sites genome-wide | Experimental |
| GO-CC | Nucleus (via zincore complex) | Database annotation |
| dbPTM | Nucleus | Curated |
| InnateDB | Nucleus | Curated |
| Key publication | Zincore complex (SEPHS1 + QRICH1) stabilizes TFs at cognate DNA motifs (Science, 2025, PMID: 40608935) | High-impact journal |

**Manual Review Assessment**: SEPHS1 has exceptionally strong and mechanistically detailed nuclear localization evidence. In 2025, a landmark study published in Science identified SEPHS1 as a core component of the "zincore" complex (together with QRICH1), which acts as a molecular grip to stabilize zinc finger transcription factors at their DNA-binding sites across the genome. SEPHS1 recognizes and binds the backbone of zinc fingers via its arginine clamp in a sequence-independent manner, enhancing TF DNA-binding stability. The zincore complex binds a highly conserved promoter motif (5'-CTTTAAR-3'). This is not a passive nuclear presence -- SEPHS1 actively participates in transcriptional regulation by physically interacting with DNA-bound transcription factors. The protein also has a separate metabolic function in selenophosphate biosynthesis (in vitro), but the zincore function is the key nuclear activity. Multiple databases independently support nuclear localization. Score 9/10 reflects the detailed mechanistic evidence for nuclear function at the transcriptional level.

### 4. Protein Size Assessment

SEPHS1 is 392 amino acids (42.9 kDa), well within the ideal range for recombinant expression, purification, and biochemical characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~40 articles |
| Novelty category | 21-40 -> Score 8 |

SEPHS1 research has seen a dramatic surge since 2020. Key developments include: identification of the zincore complex function (Science 2025, PMID: 40608935), de novo missense variants causing a neurodevelopmental condition (Am J Hum Genet 2024, PMID: 38531365), role in redox homeostasis (2019, PMID: 31607477), role in shaping immunosuppressive tumor microenvironment (Cancer Immunol Immunother 2025), and implications in osteoarthritis (Nat Commun 2022). The zincore discovery in 2025 fundamentally redefined SEPHS1 from a selenophosphate synthase to a nuclear transcription factor stabilizer. Despite the high-impact publications, the total article count remains moderate (~40). The zincore function is brand new and entirely unexplored for most biological contexts. Score 8/10 (could arguably be 10 given the entirely new functional paradigm).

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 2 experimental structures (3FD5, 3FD6, X-ray crystallography) |
| Structure Details | Ligand-bound crystal structures available |

SEPHS1 has two experimental crystal structures (3FD5, 3FD6), providing direct structural information. These structures predate the zincore discovery and likely represent the metabolic/selenophosphate synthase conformation rather than the zincore transcription factor-binding conformation. Nevertheless, they provide high-quality structural data. The AlphaFold prediction is also available and may capture different conformational states. Score 8/10 reflects the availability of experimental PDB structures.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | Arginine clamp | Recognizes zinc finger backbone; sequence-independent TF binding |
| UniProt | Selenophosphate synthase domain | EC 2.7.9.3; selenophosphate biosynthesis (in vitro) |
| Zincore complex | TF-stabilizing grip | Heterotetramer with QRICH1; binds promoter motif 5'-CTTTAAR-3' |

SEPHS1 has a unique dual-function domain architecture. The arginine clamp mediates sequence-independent recognition of zinc finger transcription factors, enabling SEPHS1 to interact with a broad range of TFs (ZFP91, ZNF652, ZNF526, PRDM15, and others). The selenophosphate synthase domain provides metabolic activity. The zincore complex represents a novel mechanism of transcriptional regulation -- rather than being a classical coactivator or corepressor, SEPHS1 acts as a structural stabilizer that enhances TF occupancy at target promoters. This is a regulatory function of the highest relevance to a TE-regulation screen. Score 8/10 reflects the novel transcription factor stabilization mechanism.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Zincore Partner | QRICH1 (obligate heterodimerization partner for zincore complex) |
| TF Partners | ZFP91, ZNF652, ZNF526, PRDM15 (zinc finger transcription factors) |
| STRING | ZRANB1, PTPRF, PDCD6, SEPHS2 (additional interactors) |
| IntAct | Multiple interactors including ZRANB1, PTPRF |

SEPHS1 has a moderate but biologically rich PPI network. The obligate partnership with QRICH1 to form the zincore complex is the most critical interaction. The zincore complex binds dozens of zinc finger transcription factors genome-wide. Additional interactions include SEPHS2 (paralog), ZRANB1 (deubiquitinase), and PTPRF (receptor phosphatase). The interaction with zinc finger TFs makes SEPHS1 a hub in the transcriptional regulatory network. Score 5/10 reflects a moderately characterized network with high biological significance.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + dbPTM + InnateDB + Science 2025 | Nuclear zincore complex | Multi-DB + high-impact publication |
| Structure | PDB 3FD5/3FD6 + AlphaFold | Well-folded | Structural data available |
| Function | Arginine clamp + selenophosphate synthase | Dual-function protein | Consistent with domain architecture |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization + Science 2025 mechanistic validation: +1.0
- PDB structural (2 entries) + domain architecture consistency: +0.5
- PPI cross-validation (zincore complex characterization): +0 (moderate)
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: STRONGLY RECOMMENDED (Score: 76.4/100)

**Core Strengths**:
1. Landmark 2025 Science paper established SEPHS1 as a nuclear transcription factor stabilizer
2. Mechanistically detailed nuclear function: zincore complex stabilizes TFs at DNA-binding sites
3. Binds zinc finger transcription factors -- potential connection to KRAB-ZNF TE repression machinery
4. Experimental PDB structures (3FD5, 3FD6) provide structural foundation
5. Moderate PubMed count (~40) with high-impact publications -- not overstudied
6. Dual-function protein (metabolic + transcriptional) offers unique biology
7. Neurodevelopmental disease link (de novo variants) provides human relevance
8. Tumor microenvironment role suggests immune/oncogenic connections

**Risks / Uncertainties**:
1. Zincore function discovered only in 2025 -- functional characterization is in early stages
2. Relationship between metabolic function and zincore function unclear
3. Full set of zinc finger TF partners not comprehensively mapped
4. Harvest packet not available; data from web queries may be incomplete
5. No direct link to TE regulation established (but zinc finger TF connection is promising)
6. May have context-dependent function (metabolic in some tissues, transcriptional in others)

**Next Steps**:
- [ ] Verify nuclear/zincore localization by IF in TE-relevant cell types
- [ ] Map SEPHS1-bound zinc finger TFs in TE-activating conditions
- [ ] Test whether zincore complex (SEPHS1+QRICH1) stabilizes KRAB-ZNF proteins at TE loci
- [ ] Investigate SEPHS1 expression changes upon TE activation or viral mimicry
- [ ] Characterize zincore complex binding to TE-derived promoter sequences
- [ ] Assess functional separation of metabolic vs. transcriptional roles
- [ ] Obtain AlphaFold pLDDT/PAE for full-length SEPHS1

### 11. Decision

**FINAL DECISION: NOT REJECTED (highest-scoring KEEP in W4).** Nuclear localization score 9/10, PubMed count ~40 (well within limits). SEPHS1 is the highest-scoring candidate in W4 at 76.4/100, marginally ahead of SCRT2 (76.1/100). The 2025 Science discovery of the zincore complex fundamentally transforms SEPHS1 from a metabolic enzyme into a transcription factor stabilizer with direct nuclear function. The mechanism -- stabilizing zinc finger transcription factors at DNA-binding sites across the genome -- is directly relevant to TE regulation. Zinc finger proteins, particularly KRAB-ZNF family members, are the primary transcriptional repressors of transposable elements in mammals. If SEPHS1/QRICH1 zincore complex stabilizes KRAB-ZNF proteins at TE loci, it could be a master regulator of TE silencing. This hypothesis is untested and represents a compelling discovery opportunity. The protein is strongly recommended for priority inclusion.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P49903
- PDB: https://www.rcsb.org/structure/3FD5
- PDB: https://www.rcsb.org/structure/3FD6
- Science 2025 (PMID: 40608935): Zincore complex discovery
- Am J Hum Genet 2024 (PMID: 38531365): Neurodevelopmental variants
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SEPHS1
- dbPTM: https://bioinfo.uth.edu/mutLBSgeneDB/gene_search_result.cgi?page=page&type=quick_search&quick_search=22929
- Note: Harvest packet not available; data compiled from web database queries
