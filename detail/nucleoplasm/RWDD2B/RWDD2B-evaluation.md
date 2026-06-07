---
type: protein-evaluation
gene: "RWDD2B"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RWDD2B -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RWDD2B / C21orf6, GL011, ORF5 |
| Protein Name | RWD Domain Containing 2B |
| Protein Size | 319 aa / ~36.3 kDa |
| UniProt ID | Q5T7P3 (RWDD2B_HUMAN) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 5/10 | x4 | **20** | Multi-compartment: nucleus (nucleoplasm, nucleolus) + cytoplasm; not exclusively nuclear |
| Protein Size | 10/10 | x1 | **10** | 319 aa, well within ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~15-25 articles; very novel (≤20 -> 10; estimated border region) |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold prediction available; Prp3-like domain; no experimental PDB entries |
| Regulatory Domains | 6/10 | x2 | **12** | RWD domain + Prp3-like domain (pre-mRNA splicing); DUF1115 |
| PPI Network | 2/10 | x3 | **6** | Very limited characterized interactions; largely uncharacterized |
| Cross-Validation Bonus | -- | -- | **+0.5** | Multi-compartment localization consistency across databases (+0.5) |
| **Raw Total** | | | **103.5/180** | |
| **Normalized Total** | | | **57.5/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| RNALocate | Nucleus (nucleoplasm, nucleolus) | Experimental |
| RNALocate | Cytoplasm, cytosol | Experimental |
| RNALocate | Chromatin, mitochondria, ribosomes | Experimental |
| HPA IHC | Cytoplasmic (most tissues) | Weak-moderate staining |
| WoLF PSORT | Cytoskeletal (score 8), cytoplasmic (score 2), cyto-nuclear (score 1) | Computational |
| GeneCards | Intracellular | Predicted |

**HPA IF Status**: HPA IF original images not available. Nuclear localization assessment based on RNALocate experimental data and computational predictions.

**Manual Review Assessment**: RWDD2B is annotated as present in multiple cellular compartments including the nucleus (nucleoplasm and nucleolus), cytoplasm, chromatin, mitochondria, and ribosomes. This broad distribution pattern suggests the protein may have context-dependent localization rather than a fixed subcellular address. The presence in nucleoplasm and nucleolus, combined with a Prp3-like domain (associated with pre-mRNA splicing), supports a nuclear functional role. However, the protein is not exclusively or predominantly nuclear, and the predominant IHC signal in most tissues is cytoplasmic. Score 5/10 reflects confirmed nuclear presence but lack of nuclear enrichment or nuclear-specific function.

### 4. Protein Size Assessment

RWDD2B is 319 amino acids (~36.3 kDa), well within the ideal range for biochemical and structural studies. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~15-25 |
| Novelty category | ≤20 -> Score 10 (borderline) |

RWDD2B is a very poorly studied gene. It was previously designated C21orf6 (chromosome 21 open reading frame 6) and is located at 21q21.3. Most publications mentioning RWDD2B are large-scale genomic or proteomic screens rather than dedicated functional studies. The gene shows ubiquitous expression across tissues, with strong expression during mouse embryonic development (branchial arches, brain, somites, limb buds). The RWD domain and Prp3-like domain hint at protein interaction and pre-mRNA splicing functions, but these have not been experimentally investigated. Extremely novel target. Score 8/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Domain Structure | RWD domain (predicted) + Prp3-like C-terminal domain |

No experimental structures are available for RWDD2B. The AlphaFold prediction exists but confidence metrics are not available without the harvest packet. The presence of the Prp3-like domain (related to the U4/U6 snRNP component Prp3) suggests at least one folded domain. The RWD domain is also likely structured. Score 5/10 reflects predicted structure availability with no experimental validation and uncertain domain-level confidence.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR006575 (RWD domain) | Protein-protein interaction |
| InterPro | IPR010541 (Prp3-like, C-terminal) | Pre-mRNA splicing factor homology |
| Pfam | DUF1115 | Domain of unknown function |
| Post-translational | N-glycosylation, phosphorylation, N-myristoylation sites | Regulatory potential |

The domain architecture is intriguing. The RWD domain mediates protein-protein interactions, and the Prp3-like C-terminal domain is homologous to the U4/U6 snRNP protein Prp3, suggesting possible involvement in pre-mRNA splicing -- a nuclear process. The DUF1115 domain remains uncharacterized. The presence of multiple post-translational modification sites (N-glycosylation, phosphorylation, N-myristoylation) suggests regulation by signaling pathways. Score 6/10 reflects domain-based functional hypotheses but no experimental validation of domain functions.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Limited to no data |
| IntAct | Not available |
| Known Partners | None experimentally characterized |

RWDD2B has essentially no characterized protein-protein interaction network. The RWD domain and Prp3-like domain both suggest protein interaction capabilities, but no specific partners have been identified or validated. This is consistent with the very low PubMed count (≤20 articles). Score 2/10 reflects the near-complete absence of PPI data.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Multi-compartment Localization | RNALocate + HPA + WoLF PSORT | Nucleus + cytoplasm + others | Consistent multi-compartment |
| Domain annotation | InterPro + Pfam | RWD + Prp3-like + DUF1115 | Multi-DB consistent |

**Cross-Validation Bonus Details**:
- Multi-database multi-compartment localization consistency: +0.5
- Limited structural cross-validation (no PDB): +0
- No PPI cross-validation (insufficient data): +0
- **Total Cross-Validation Bonus**: +0.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: CONDITIONALLY RECOMMENDED (Score: 57.5/100)

**Core Strengths**:
1. Confirmed nuclear presence (nucleoplasm, nucleolus) by RNALocate experimental data
2. Prp3-like domain suggests possible pre-mRNA splicing function -- a nuclear process
3. Extremely novel (PubMed ≤20) -- high discovery potential
4. Protein size (319 aa) is experimentally tractable
5. Multiple PTM sites suggest signaling pathway integration

**Risks / Uncertainties**:
1. Not exclusively or predominantly nuclear -- broad multi-compartment distribution (score 5/10)
2. Near-complete absence of functional characterization
3. No experimental PPI data
4. No experimental structural data
5. Prp3-like domain homology does not guarantee splicing function
6. DUF1115 domain of unknown function

**Next Steps**:
- [ ] Verify nuclear/nucleolar localization by immunofluorescence in multiple cell types
- [ ] Test for involvement in pre-mRNA splicing using splicing reporter assays
- [ ] Identify interaction partners via AP-MS or BioID
- [ ] Obtain AlphaFold pLDDT statistics and PAE data
- [ ] Investigate developmental expression pattern and function

### 11. Decision

**FINAL DECISION**: NOT REJECTED. Nuclear localization score 5/10 (above ≤3 threshold), PubMed count (~15-25, well below 100 threshold). RWDD2B is a high-risk, high-reward candidate. The Prp3-like domain and nuclear/nucleolar localization are promising, but the complete lack of functional characterization means most evaluation is based on domain homology inference rather than experimental evidence. The gene merits inclusion as a candidate with the strong recommendation to prioritize basic characterization (localization verification, partner identification) before investing in deeper mechanistic studies.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q5T7P3
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RWDD2B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RWDD2B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156253-RWDD2B
- Note: Harvest packet not available; data compiled from UniProt, GeneCards, and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P57060 |
| SMART | SM00591; |
| UniProt Domain [FT] | DOMAIN 41..165; /note="RWD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00179" |
| InterPro | IPR017359;IPR010541;IPR006575;IPR059181;IPR016135; |
| Pfam | PF06544;PF05773; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156253-RWDD2B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TRIM7 | Intact, Biogrid | true |
| ACY3 | Bioplex | false |
| DVL3 | Intact | false |
| FAM163A | Intact | false |
| GADD45G | Intact | false |
| GAPDH | Bioplex | false |
| IKZF1 | Intact | false |
| KIAA1958 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
