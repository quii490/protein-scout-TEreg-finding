---
type: protein-evaluation
gene: "SCNM1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery, high-priority]
status: scored
---

## SCNM1 -- Re-evaluation Report (KEPT: Nuclear Splicing Factor, Low PubMed)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCNM1 / OFD19, MGC3180, Sodium channel modifier 1 |
| Protein Name | Sodium channel modifier 1 (putative RNA splicing factor, minor spliceosome component) |
| Protein Size | ~238-268 aa |
| UniProt ID | Q9BWG6 (SCNM1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 10/10 | x4 | **40** | Nuclear speckle localization; bipartite NLS; minor spliceosome component |
| Protein Size | 10/10 | x1 | **10** | ~238-268 aa, ideal size range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~23 articles (21-40 -> 8) |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold predicted structure available; no experimental PDB |
| Regulatory Domains | 7/10 | x2 | **14** | Zinc finger domain; splicing factor; minor spliceosome functional mimicry |
| PPI Network | 4/10 | x3 | **12** | Spliceosome partners (U1-70K/SNRNP70); LUC7L2; limited overall |
| Cross-Validation Bonus | -- | -- | **+1.5** | Multi-DB nuclear consensus (+1.0); Domain-function consistency (+0.5) |
| **Raw Total** | | | **129.5/180** | |
| **Normalized Total** | | | **71.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus, Nuclear speckle | Primary annotation |
| UniProt feature | Bipartite NLS (aa 4-20) | Sequence motif |
| GO-CC | Nucleus, Nuclear speckle, Nucleoplasm | Database annotation |
| dbPTM | Nucleus | Curated |
| InnateDB | Nucleus | Curated |

**Manual Review Assessment**: SCNM1 has among the strongest nuclear localization evidence in this batch. The protein contains a bipartite nuclear localization signal (NLS) at positions 4-20, directly encoded in its sequence. UniProt annotates nuclear speckle localization -- a subnuclear domain where pre-mRNA splicing factors concentrate. SCNM1 colocalizes with LUC7L2 and SNRNP70 (U1-70K) in nuclear speckles. As a component of the minor (U12-type) spliceosome, SCNM1 functions exclusively in the nucleus. The protein was shown to functionally mimic the SF3a complex of the major spliceosome (Bai et al., Science 2021). Nuclear localization score 10/10 reflects the encoded NLS, experimental colocalization data, and unequivocal nuclear function.

### 4. Protein Size Assessment

SCNM1 is approximately 238-268 amino acids, within the ideal range for recombinant expression, purification, and biochemical characterization. The small size is advantageous for structural studies and functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~23 articles |
| Novelty category | 21-40 -> Score 8 |

SCNM1 was first identified in 1999 as a modifier locus for sodium channelopathy severity in mice (Sprunger et al., Hum Mol Genet). Landmark studies include its identification as a putative RNA splicing factor that modifies disease severity (Buchner et al., Science 2003, PMID: 12920299), demonstration of a direct role in splicing via U1-70K interaction (Howell et al., Hum Mol Genet 2007), and structural characterization of the human minor spliceosome (Bai et al., Science 2021). In 2022, SCNM1 mutations were directly linked to human disease -- orofaciodigital syndrome type 19 due to minor intron splicing defects affecting primary cilia (Iturrate et al., Am J Hum Genet). Most recently (2025), SCNM1 was implicated in hepatocellular carcinoma progression. Despite the high-impact publications, the total article count remains low (~23), making SCNM1 a genuinely novel target with strong biological significance. Score 8/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no isolated experimental structures) |
| Structural Context | Minor spliceosome cryo-EM structure (2021) includes SCNM1 |

SCNM1 has no isolated experimental PDB structure, but its structure as part of the human minor spliceosome has been determined by cryo-EM (Bai et al., Science 2021). This provides some structural information within the larger complex context. AlphaFold prediction is available. The small protein size and zinc finger domain suggest a well-folded structure. Score 4/10 reflects the absence of high-resolution isolated structures balanced against spliceosome complex structural data.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | Zinc finger domain | C2H2-type or C2HC-type zinc finger |
| UniProt | Bipartite NLS (aa 4-20) | Nuclear targeting signal |
| Functional annotation | Minor spliceosome component | U12-type intron splicing; mimics SF3a subunit function |

SCNM1 contains a zinc finger domain, characteristic of DNA/RNA-binding proteins and splicing factors. Its most notable feature is the encoded bipartite NLS, confirming nuclear targeting. The protein functions as a component of the minor spliceosome, specifically involved in U12-type intron splicing. It functionally mimics the SF3a complex subunits of the major spliceosome. The zinc finger domain likely mediates RNA recognition or protein-protein interactions within the spliceosome. Score 7/10 reflects the zinc finger (a canonical regulatory domain), NLS, and defined spliceosome function.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Known Partners | SNRNP70 (U1-70K), LUC7L2, minor spliceosome components |
| STRING | Limited data; spliceosome network expected |
| IntAct | Limited interactions expected |

SCNM1's best-characterized interaction is with SNRNP70 (U1-70K), the U1 snRNP-specific protein (Howell et al., 2007). It colocalizes with LUC7L2 in nuclear speckles. As a minor spliceosome component, it interacts with the broader spliceosome machinery. However, direct PPI studies are limited, and the interactome is not comprehensive. Score 4/10 reflects a partially characterized PPI network centered on spliceosome components.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + dbPTM + InnateDB + sequence NLS | Nuclear speckle | Multi-DB consensus |
| Function | Splicing factor + nuclear speckle localization | Nuclear function | Consistent |
| Disease Link | OFD19 + HCC | Human disease relevance | Validated |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization consensus + sequence-encoded NLS: +1.0
- Domain architecture consistent with splicing factor function: +0.5
- Structural cross-validation in spliceosome context: +0 (partial -- cryo-EM complex only)
- PPI cross-validation with spliceosome: +0 (limited interaction data)
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 71.9/100)

**Core Strengths**:
1. Exceptional nuclear localization evidence: sequence-encoded bipartite NLS + nuclear speckle annotation
2. Biologically significant: minor spliceosome component, directly linked to human genetic disease (OFD19)
3. Genuinely novel: only ~23 PubMed articles despite landmark publications in Science
4. Small protein size (~238-268 aa) ideal for biochemical characterization
5. Disease relevance established (OFD19, HCC) but mechanistic details remain unexplored
6. Minor spliceosome specificity provides a unique angle for TE-related RNA processing studies

**Risks / Uncertainties**:
1. No experimental PDB structure -- AlphaFold prediction only
2. Limited PPI network characterization
3. Specific TE-related biology completely unexplored
4. Minor spliceosome function may be narrowly specialized (U12-type introns only)
5. Harvest packet not available; data from web queries may be incomplete
6. Zinc finger domain type and RNA targets not fully defined

**Next Steps**:
- [ ] Verify nuclear localization by immunofluorescence in relevant cell types
- [ ] Obtain AlphaFold pLDDT/PAE statistics for structural quality assessment
- [ ] Characterize RNA targets of the minor spliceosome involving SCNM1
- [ ] Assess whether SCNM1-regulated splicing affects TE-derived transcripts
- [ ] Investigate SCNM1 expression changes upon TE activation (e.g., stress, viral mimicry)
- [ ] Perform AP-MS to map SCNM1 interactome in nuclear speckles

### 11. Decision

**FINAL DECISION: NOT REJECTED.** Nuclear localization score 10/10 (well above ≤3 threshold), PubMed count ~23 (well below 100 threshold). SCNM1 is one of the most promising candidates in W4. The sequence-encoded NLS, nuclear speckle localization, and minor spliceosome function provide a strong rationale for nuclear biology. The low PubMed count (~23) despite high-impact publications (Science, Am J Hum Genet) indicates an under-explored gene with genuine discovery potential. The link to primary cilia and Hedgehog signaling via OFD19 adds developmental biology relevance. SCNM1 is especially interesting for a TE-regulation screen because minor spliceosome components processing U12-type introns may play roles in splicing TE-derived transcripts or regulating host defense against retroelements. Strongly recommended for inclusion.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWG6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCNM1
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=SCNM1_HUMAN
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/79005
- ClinGen: https://search.clinicalgenome.org/kb/genes/HGNC:23136
- Key publications: Science 2003 (PMID:12920299), Science 2021 (PMID:33509932), Am J Hum Genet 2022 (PMID:36084634)
- Note: Harvest packet not available; data compiled from web database queries
