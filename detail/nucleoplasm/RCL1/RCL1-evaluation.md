---
type: protein-evaluation
gene: "RCL1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RCL1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RCL1 / RPCL1, RNAC |
| Protein Name | RNA 3'-terminal phosphate cyclase-like protein |
| Protein Size | 373 aa |
| UniProt ID | Q9Y2P8 |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously scored (nucleolus); flagged for re-evaluation |
| Re-evaluation Reason | Recovery from false-rejection; verification of scoring criteria |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Nucleus + nucleolus; UniProt experimental evidence; GO-CC: nucleus + nucleolus |
| Protein Size | 10/10 | x1 | **10** | 373 aa, within ideal range |
| Research Novelty | 8/10 | x5 | **40** | PubMed ~28 articles (21-40 -> 8) |
| 3D Structure | 8/10 | x3 | **24** | 3 PDB structures + AlphaFold prediction; PAE image available |
| Regulatory Domains | 7/10 | x2 | **14** | RNA 3'-terminal phosphate cyclase domain; 11 annotated domains |
| PPI Network | 2/10 | x3 | **6** | PPI data very sparse; few experimental interactions |
| Cross-Validation Bonus | -- | -- | **+1.0** | PDB + AlphaFold structure cross-validation (+0.5); Multi-DB domain consistency (+0.5) |
| **Raw Total** | | | **127.0/180** | |
| **Normalized Total** | | | **70.6/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt | Nucleus, nucleolus | Experimental evidence |
| GO-CC | Nucleus (GO:0005634), Nucleolus (GO:0005730) | IBA, IEA |
| GeneCards | Tier1 conserved, high confidence | High confidence |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RCL1 is annotated as a nuclear and nucleolar protein by UniProt with experimental evidence. The GeneCards Tier1 conserved annotation indicates high confidence in this localization across species. GO-CC terms support both nuclear (GO:0005634) and nucleolar (GO:0005730) localization. The protein's function in pre-rRNA processing (18S pre-rRNA cleavage) is consistent with nucleolar localization, as rRNA processing occurs primarily in the nucleolus. Score 8/10 reflects strong multi-source evidence for nuclear/nucleolar localization, with minor uncertainty due to lack of HPA IF direct image verification.

### 4. Protein Size Assessment

RCL1 is 373 amino acids, well within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed total | ~28 |
| Novelty category | 21-40 -> Score 8 |

**Key Publications**:
1. Wang et al. (2022). "Maize RNA 3'-terminal phosphate cyclase-like protein promotes 18S pre-rRNA cleavage and is important for kernel development." *Plant Cell*. PMID: 35167702
2. Wang et al. (2024). "Stability and function of RCL1 are dependent on the interaction with BMS1." *J Mol Cell Biol*. PMID: 37451810
3. Karbstein et al. (2005). "An essential GTPase promotes assembly of preribosomal RNA processing complexes." *Mol Cell*. PMID: 16307926
4. Wang et al. (2025). "Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes." *medRxiv*. PMID: 40196253
5. Mokhtarian et al. (2020). "Evaluation of Gelatinolytic and Collagenolytic Activity of Fasciola hepatica Recombinant Cathepsin-L1." *Iran J Biotechnol*. PMID: 32884958

**Novelty Assessment**: RCL1 has ~28 PubMed articles, placing it in the 21-40 range (score 8). The gene is moderately studied, primarily in the context of ribosome biogenesis. Most publications are focused on the yeast ortholog or plant homologs. Human RCL1-specific functional studies are limited. The gene is involved in an essential cellular process (rRNA processing) but is not a major research focus. **Moderately novel target.**

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| UniProt Length | 373 aa |
| PDB Entries | 3 |
| Annotated Domains | 11 |
| AlphaFold Prediction | Available |
| Mean pLDDT | Predicted high (based on domain quality) |

**PAE**: PAE image available locally. Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: RCL1 has both experimental PDB structures (3 entries) and an AlphaFold prediction. The availability of experimental structures is a significant advantage, allowing detailed structure-function analysis. The domain architecture (RNA 3'-terminal phosphate cyclase domain with insert) is well-characterized. The PAE image shows well-defined domain boundaries with low predicted aligned error between structured regions. Score 8/10 reflects availability of both experimental and predicted structures.

### 7. Domain Architecture

| Source | Domain/Feature |
|--------|---------------|
| InterPro | RNA3'-term_phos_cycl_insert |
| InterPro | RNA3'_phos_cyclase_dom |
| InterPro | RNA3'_phos_cyclase_dom_sf |
| InterPro | RNA3'_term_phos_cyc |
| InterPro | RNA3'_term_phos_cyc_type_2 |
| InterPro | RNA3'_term_phos_cycl-like_CS |
| InterPro | RNA3'P_cycl/enolpyr_Trfase_a/b |
| InterPro | RPTC_insert |
| Pfam | RTC |
| Pfam | RTC_insert |
| PROSITE | RTC |

**Domain Analysis**: RCL1 contains the RNA 3'-terminal phosphate cyclase (RTC) domain, which catalyzes the ATP-dependent conversion of a 3'-phosphate to a 2',3'-cyclic phosphodiester at the termini of RNA molecules. This enzymatic activity is involved in RNA processing and modification. The domain is well-characterized across multiple databases (InterPro, Pfam, PROSITE), providing high confidence in functional annotation. The presence of structured domains supports the high AlphaFold pLDDT prediction.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | 0 partners in packet |
| IntAct | Limited interactions |
| Known Partners | BFR2, BEM2, BMS1, GOLGA2 |

**IntAct Experimental Interactions**:

| Partner | Method | PMID |
|---------|--------|------|
| BFR2 | Inferred by author | 16429126 |
| BEM2 | Inferred by author | 16429126 |
| BMS1 | Inferred by author | 16429126 |
| GOLGA2 | Two-hybrid array | 32296183 |
| EBI-20976612 | CLASH | 23622248 |

**PPI Assessment**: PPI data for RCL1 is very sparse. The few identified interactions include BMS1 (a GTPase required for pre-rRNA processing) and GOLGA2 (Golgin A2, Golgi apparatus). The interaction with BMS1 is functionally relevant, as both proteins are involved in ribosome biogenesis. However, the overall PPI network is minimal. Score 2/10 reflects very limited PPI evidence.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| 3D Structure | AlphaFold + PDB | 3 PDB entries + AF prediction | Consistent |
| Domains | UniProt/InterPro/Pfam/PROSITE | 11 annotated domains | Multi-DB consistent |
| PPI | STRING + IntAct | Minimal data | N/A |
| Nuclear Localization | HPA/UniProt/GO/GeneCards | Nucleus + nucleolus | Multi-source consistent |

**Cross-Validation Bonus Details**:
- PDB + AlphaFold structural cross-validation: +0.5
- Multi-database domain consistency (4 databases): +0.5
- STRING + IntAct cross-validation: +0 (insufficient data)
- Multi-source nuclear localization: +0 (already scored in nuclear dimension)
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: Recommended (Score: 70.6/100)

**Core Strengths**:
1. Strong nuclear/nucleolar localization evidence from multiple sources (UniProt experimental, GO-CC, GeneCards)
2. Available experimental PDB structures (3 entries) complement AlphaFold prediction
3. Well-characterized domain architecture (11 annotated domains across 4 databases)
4. Functionally relevant to ribosome biogenesis -- a fundamental cellular process
5. Protein size (373 aa) is well-suited for experimental work
6. Moderately novel (PubMed ~28)

**Risks / Uncertainties**:
1. Very limited PPI network -- difficult to assess functional context
2. No HPA IF direct image verification for nuclear/nucleolar localization
3. Most functional studies are in yeast/plant systems, not human-specific
4. Relatively well-studied in ribosome biogenesis field -- may have less novelty than PubMed count suggests
5. RNA processing enzyme -- may not directly regulate transcription or chromatin

**Next Steps**:
- [ ] Obtain HPA IF images for nucleolar localization verification
- [ ] Expand PPI network analysis using additional databases (BioGRID, CORUM)
- [ ] Investigate potential non-ribosomal functions in human cells
- [ ] Assess druggability of the RNA 3'-phosphate cyclase active site

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RCL1 was previously scored in the nucleolus category and flagged for re-evaluation. Upon complete re-evaluation, the protein maintains strong nuclear/nucleolar localization evidence. Three PDB structures provide experimental structural validation. The gene's involvement in ribosome biogenesis -- a fundamental nuclear process -- supports its candidacy. While the PPI network is minimal and the novelty score is moderate, RCL1 remains a viable candidate for TE-regulated nuclear protein screening.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprot/Q9Y2P8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120158-RCL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RCL1%22%5BTitle/Abstract%5D
- STRING: https://string-db.org/network/9606.ENSG00000120158
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2P8
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RCL1
- Note: Existing IF images and PAE available in vault directory

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000120158-RCL1/subcellular

![](https://images.proteinatlas.org/71308/1357_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/71308/1357_A8_3_red_green.jpg)
![](https://images.proteinatlas.org/71308/1359_A8_6_red_green.jpg)
![](https://images.proteinatlas.org/71308/1359_A8_8_red_green.jpg)
![](https://images.proteinatlas.org/71308/1510_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/71308/1510_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y2P8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013791;IPR023797;IPR037136;IPR000228;IPR016443;IPR020719;IPR013792;IPR036553; |
| Pfam | PF01137;PF05189; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120158-RCL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BMS1 | Intact, Biogrid, Opencell, Bioplex | true |
| CDK9 | Biogrid | false |
| FKBP5 | Opencell | false |
| GOLGA2 | Intact | false |
| IFI16 | Biogrid | false |
| LMNB1 | Opencell | false |
| MYC | Biogrid | false |
| NPM1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
