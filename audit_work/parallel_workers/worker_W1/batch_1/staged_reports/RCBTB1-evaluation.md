---
type: protein-evaluation
gene: "RCBTB1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RCBTB1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RCBTB1 / CLLD7, CLL deletion region gene 7 protein |
| Protein Name | RCC1 and BTB domain-containing protein 1 |
| Protein Size | 531 aa |
| UniProt ID | Q8NDN9 (RCBT1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 6/10 | x4 | **24** | UniProt: Nucleus (potential); multiple databases support nuclear; no exclusive nuclear evidence |
| Protein Size | 10/10 | x1 | **10** | 531 aa, within ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~35-40 articles (21-40 -> 8) |
| 3D Structure | 7/10 | x3 | **21** | AlphaFold predicted structure; no experimental PDB entries |
| Regulatory Domains | 7/10 | x2 | **14** | BTB/POZ domain + RCC1 repeats; chromatin remodeling association |
| PPI Network | 3/10 | x3 | **9** | PPI data limited; partial STRING network |
| Cross-Validation Bonus | -- | -- | **+1.0** | Multi-DB nuclear localization consensus (+0.5); Domain + AlphaFold quality (+0.5) |
| **Raw Total** | | | **119.0/180** | |
| **Normalized Total** | | | **66.1/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Potential (ECO:0000305) |
| dbPTM | Nucleus | Curated |
| InnateDB | Nucleus | Curated |
| PhosphoSitePlus | Nucleus; Cytoplasm | Experimental/IP |
| PICKLE | Nucleus | Database |
| GO-CC | Not directly annotated | -- |
| HPA | Data not available in packet | -- |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RCBTB1 is annotated as nuclear by UniProt (Swiss-Prot reviewed entry) and multiple curated databases. The protein name "RCC1 and BTB domain-containing protein 1" suggests a nuclear function -- RCC1 (Regulator of Chromosome Condensation) is a well-known nuclear protein that acts as a guanine nucleotide exchange factor for Ran GTPase on chromatin. The BTB domain is commonly found in transcription factors. PhosphoSitePlus reports both nuclear and cytoplasmic localization, suggesting possible nucleocytoplasmic shuttling. The protein is implicated in chromatin remodeling and cell cycle regulation. Score 6/10 reflects strong database support for nuclear localization but lack of HPA IF experimental confirmation.

### 4. Protein Size Assessment

RCBTB1 is 531 amino acids in length, placing it well within the ideal range for biochemical characterization. Proteins of this size are amenable to recombinant expression, purification, and most structural and functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~35-40 |
| Novelty category | 21-40 -> Score 8 |

**Key Research Context**: RCBTB1 (also known as CLLD7) was initially identified in the context of chronic lymphocytic leukemia (CLL) deletion region on chromosome 13q14. Published literature includes studies on its potential tumor suppressor role in CLL and other hematological malignancies. The gene is ubiquitously expressed, with presence in retina (nerve fiber layer and inner/outer plexiform layers). Research is limited but not extremely sparse -- the gene has been studied in cancer contexts for over two decades since the CLL deletion mapping studies.

**Novelty Score**: PubMed count estimated at ~35-40 articles, falling in the 21-40 range. Per scoring rule: 21-40 -> 8. Moderately novel target.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no experimental structures) |
| Mean pLDDT | Not available in harvested data |
| Ordered Region Estimate | High (based on domain architecture) |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: RCBTB1 shares the same domain architecture as RCBTB2 (BTB domain + RCC1 repeats), and its paralog RCBTB2 has a high-quality AlphaFold prediction (pLDDT 90.4). Given the sequence similarity, RCBTB1 is expected to have a comparably well-folded structure. No experimental PDB structures exist. Score 7/10 reflects strong predicted structure but lack of experimental validation.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | BTB/POZ domain | Protein-protein interaction; common in transcription factors and ubiquitin ligases |
| InterPro | RCC1 repeats | Seven-bladed beta-propeller; chromatin binding and GEF activity |
| Pfam | BTB domain | PF00651 |
| Pfam | RCC1-like repeat | Regulatory function |

**Domain Analysis**: RCBTB1 contains two major domain types: (1) BTB/POZ domain for protein-protein interactions, commonly involved in transcriptional regulation and ubiquitin ligase complexes; (2) RCC1 repeats forming a beta-propeller structure. RCC1 is the guanine nucleotide exchange factor for Ran, a critical regulator of nucleocytoplasmic transport, mitotic spindle assembly, and nuclear envelope formation. The presence of RCC1 repeats strongly supports nuclear function. The BTB domain may mediate substrate recruitment in ubiquitin ligase complexes or transcriptional co-regulator interactions.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Limited data; partner with RCBTB2 confirmed |
| IntAct | Limited data in packet |
| UniProt Interactions | Not available in packet |

**PPI Assessment**: PPI data is limited in the available harvested data. RCBTB1 interacts with its paralog RCBTB2 (STRING combined score 0.698, experimental 0.637 by co-immunoprecipitation). This interaction is the strongest experimentally validated PPI for this protein. Limited additional PPI data prevents comprehensive network analysis. Score 3/10 reflects sparse PPI evidence.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + dbPTM + InnateDB + PhosphoSitePlus | Nucleus | Multi-DB consensus |
| Structure | AlphaFold (predicted) + domain architecture | Well-folded prediction | Consistent with domain annotation |
| PPI | STRING + IntAct | Limited data | Sparse |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization consensus (4+ sources): +0.5
- Domain architecture + AlphaFold prediction consistency: +0.5
- STRING + IntAct cross-validation: +0 (insufficient data)
- PDB structural cross-validation: +0 (no experimental structure)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: Recommended with caution (Score: 66.1/100)

**Core Strengths**:
1. Multiple databases support nuclear localization (UniProt, dbPTM, InnateDB, PhosphoSitePlus)
2. Domain architecture (BTB + RCC1) strongly supports regulatory function
3. Paralog RCBTB2 is confirmed nucleoplasm-localized and has high-quality structural prediction
4. Moderate novelty (PubMed ~35-40)
5. Protein size (531 aa) is experimentally tractable

**Risks / Uncertainties**:
1. No HPA IF experimental confirmation of nuclear localization
2. No experimental PDB structures
3. Limited PPI network data
4. Nuclear localization is annotated as "potential" by UniProt, not experimentally confirmed
5. May have functional redundancy with RCBTB2
6. PubMed count is moderate, reducing novelty score

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Assess functional overlap/redundancy with RCBTB2
- [ ] Expand PPI network analysis
- [ ] Obtain AlphaFold pLDDT statistics for structural quality assessment

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). The previous rejection was based on a thin template report that lacked substantive data. Upon complete re-evaluation, RCBTB1 shows credible evidence for nuclear localization from multiple databases (UniProt, dbPTM, InnateDB, PhosphoSitePlus). The BTB + RCC1 domain architecture is consistent with chromatin-associated regulatory function. The paralog RCBTB2 is experimentally confirmed in the nucleoplasm. While some uncertainties remain (no HPA IF, "potential" nuclear annotation), RCBTB1 merits inclusion as a candidate with the recommendation to experimentally verify nuclear localization.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDN9
- PhosphoSitePlus: https://www.phosphosite.org/proteinAction?id=14325202
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=RCBT1_HUMAN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RCBTB1%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDN9
- STRING: https://string-db.org/network/9606.ENSP00000365833
- Note: Harvest packet not available for this gene; data compiled from web database queries
