---
type: protein-evaluation
gene: "SAMD11"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## SAMD11 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SAMD11 |
| Protein Name | Sterile Alpha Motif Domain-Containing Protein 11 |
| Protein Size | 681 aa / 72.7 kDa |
| UniProt ID | Q96NU1 |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | UniProt nucleus + HPA nucleoplasm + GO-CC nucleus + PRC1 complex |
| Protein Size | 10/10 | x1 | **10** | 681 aa, within ideal range |
| Research Novelty | 10/10 | x5 | **50** | PubMed 6-13 articles (≤20 -> 10) |
| 3D Structure | 3/10 | x3 | **9** | AlphaFold mean pLDDT 50.1 (low quality); no PDB entries; 73.6% residues pLDDT <50 |
| Regulatory Domains | 4/10 | x2 | **8** | SAM domain (IPR001660, IPR013761, PF07647); Polycomb group PRC1 complex |
| PPI Network | 5/10 | x3 | **15** | STRING: SAMD7 (0.639), KLHL17 (0.53); IntAct: 15+ Y2H interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | Multi-DB nuclear localization (+0.5); STRING + IntAct Y2H cross-validation (+0.5) |
| **Raw Total** | | | **121.0/180** | |
| **Normalized Total** | | | **67.2/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus | ECO:0000250 (sequence similarity) |
| HPA | Nucleoplasm, Vesicles | Approved |
| GO-CC | Nucleus (GO:0005634) | IBA:GO_Central |
| GO-CC | PRC1 complex (GO:0035102) | ISS:UniProtKB |
| HPA Reliability | Approved | IF images available |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**Manual Review Assessment**: SAMD11 is a component of the Polycomb group (PcG) multiprotein PRC1-like complex, which functions in the nucleus to establish and maintain gene silencing through chromatin modification. Its role in establishing rod photoreceptor cell identity by silencing non-rod gene expression is a nuclear transcriptional repression function. Multiple databases support nuclear localization (UniProt, HPA, GO-CC). The HPA annotation also includes Vesicles as an additional location, but Nucleoplasm is the main location with Approved reliability. Score 7/10 reflects strong multi-source nuclear consensus with minor uncertainty from the additional vesicular annotation. Well above the ≤3 rejection threshold.

### 4. Protein Size Assessment

SAMD11 is 681 amino acids (72.7 kDa), within the ideal 200-800 aa range. This size is amenable to standard biochemical approaches including recombinant expression, purification, and functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query (Title/Abstract + gene/protein/hydrolase) | 6 articles |
| PubMed symbol-only query (Title/Abstract) | 12 articles |
| PubMed broad query | 13 articles |
| Novelty category | ≤20 -> Score 10 |

**Key Research Context**: SAMD11 was identified as a photoreceptor transcriptional co-repressor and component of the PRC1 complex. Key publications include:
1. Kubo et al. (2021, Sci Rep, PMID: 33603070) -- Functional analysis of Samd11 in establishing rod photoreceptor identity
2. Corton et al. (2016, Sci Rep, PMID: 27734943) -- SAMD11 as a novel cause of autosomal recessive retinitis pigmentosa
3. Liu et al. (2024, Int J Biol Macromol, PMID: 39362437) -- METTL16-dependent m6A modification regulating SAMD11 in thyroid cancer

The gene has been studied almost exclusively in the context of retinal development and disease (retinitis pigmentosa). The thyroid cancer connection is recent and preliminary. SAMD11 is an extremely novel gene with <15 publications. Score 10/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (AF-Q96NU1-F1, version 6) |
| PDB Entries | 0 |
| Mean pLDDT | 50.1 |
| pLDDT >90 | 9.3% |
| pLDDT 70-90 | 7.6% |
| pLDDT 50-70 | 9.5% |
| pLDDT <50 | 73.6% |

**PAE**: PAE image URL available via AlphaFold (AF-Q96NU1-F1-predicted_aligned_error_v6.png). Local PAE assessment pending image download.

**Structure Assessment**: The AlphaFold structure prediction quality for SAMD11 is notably poor. With a mean pLDDT of 50.1 and 73.6% of residues below the 50 pLDDT threshold, the majority of the protein is predicted to be disordered or of very low structural confidence. Only 9.3% of residues have high confidence (pLDDT >90). This suggests SAMD11 is largely an intrinsically disordered protein or contains only small folded domains within a predominantly disordered context. The SAM domain region is likely the structured core. No experimental PDB structures exist. Score 3/10 reflects the very low AlphaFold confidence and absence of experimental structural data.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001660 (SAM domain) | Sterile alpha motif -- protein-protein interaction |
| InterPro | IPR013761 (SAM/pointed domain) | SAM domain superfamily |
| Pfam | PF07647 (SAM_2) | SAM domain variant |

The sole annotated domain is the SAM (Sterile Alpha Motif) domain, which mediates protein-protein interactions, often in the context of transcriptional regulation complexes. SAM domains are found in Polycomb group proteins, transcriptional repressors, and signaling scaffolds. The presence of a SAM domain is consistent with SAMD11's role in the PRC1 complex, where SAM domain-mediated interactions may facilitate complex assembly. Beyond the SAM domain, the protein architecture is poorly characterized, consistent with the low AlphaFold pLDDT. Score 4/10 reflects a single characterized domain with known function but limited domain complexity.

### 8. PPI Network Analysis

| Source | Partner | Score/Evidence |
|--------|---------|----------------|
| STRING | SAMD7 | 0.639 (experimental: 0.555, textmining: 0.223) |
| STRING | KLHL17 | 0.53 (textmining: 0.51) |
| STRING | ZNF408 | 0.41 (experimental: 0.063, textmining: 0.396) |
| STRING | NR2E3 | 0.409 (experimental: 0.051, textmining: 0.403) |
| IntAct | PRR20E | Anti-tag coimmunoprecipitation (PMID: 28514442) |
| IntAct | TRAF1 | Two-hybrid array (PMID: 32296183) |
| IntAct | 13+ additional partners | Various Y2H methods |

SAMD11 has a moderate PPI network with 15+ Y2H-identified interactions and one confirmed co-immunoprecipitation (PRR20E). The strongest STRING interaction is with SAMD7 (another SAM domain protein), with experimental evidence (score 0.555). The interaction with NR2E3 (a photoreceptor-specific nuclear receptor) is functionally relevant to the retinal context. However, most interactions derive from high-throughput Y2H screens rather than targeted validation. Score 5/10 reflects a moderate number of reported interactions with limited functional validation.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | Nucleus/Nucleoplasm | Multi-DB consensus |
| PRC1 Complex | UniProt + GO-CC | PRC1 complex component | Consistent |
| Y2H Interactions | IntAct + STRING | 15+ partners, some overlap | Partial validation |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization consensus (3+ sources): +0.5
- IntAct + STRING partial Y2H cross-validation: +0.5
- No structural cross-validation (no PDB, low AF confidence): +0
- Single domain annotation (limited multi-DB domain validation): +0
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: RECOMMENDED (Score: 67.2/100)

**Core Strengths**:
1. Strong nuclear localization evidence from UniProt, HPA (Approved), and GO-CC
2. PRC1 complex component -- canonical nuclear chromatin regulatory function
3. Extremely novel (PubMed 6-13, score 10/10)
4. Disease relevance: autosomal recessive retinitis pigmentosa, thyroid cancer
5. SAM domain provides protein interaction capabilities
6. Retinal photoreceptor biology is a well-defined, tractable research context

**Risks / Uncertainties**:
1. AlphaFold predicts predominantly disordered structure (mean pLDDT 50.1, 73.6% <50)
2. No experimental PDB structures
3. Only one characterized domain (SAM)
4. HPA also annotates Vesicles (additional location) -- dual localization
5. Most PPIs from high-throughput Y2H screens, not targeted validation
6. Functional studies almost exclusively in retinal context -- non-retinal roles unexplored

**Next Steps**:
- [ ] Download and assess PAE image for domain-level structural confidence
- [ ] Verify nuclear vs. vesicular localization by independent IF
- [ ] Characterize SAM domain-mediated interactions within PRC1 complex
- [ ] Investigate non-retinal functions (thyroid, other tissues)
- [ ] Obtain experimental structural data for SAM domain region

### 11. Decision

**FINAL DECISION**: NOT REJECTED. Nuclear localization score 7/10 (above ≤3 threshold), PubMed count 6-13 (below 100 threshold). SAMD11 is a strongly recommended candidate. The gene combines well-supported nuclear localization (PRC1 complex) with extreme novelty (≤13 publications) and disease relevance (retinitis pigmentosa). The primary concern is the poor AlphaFold structure prediction (mean pLDDT 50.1), which suggests the protein is largely disordered. However, disordered proteins in chromatin regulatory complexes often undergo disorder-to-order transitions upon partner binding, which could be mechanistically interesting. SAMD11 is recommended for inclusion.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96NU1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187634-SAMD11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NU1
- STRING: https://string-db.org/network/9606.ENSG00000187634
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAMD11
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/SAMD11.json

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000187634-SAMD11/subcellular

![](https://images.proteinatlas.org/30110/322_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/30110/322_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/30110/327_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/30110/327_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/30110/335_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/30110/335_G9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
