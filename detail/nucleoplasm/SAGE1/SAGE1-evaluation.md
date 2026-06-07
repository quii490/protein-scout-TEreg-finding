# SAGE1 -- Critical False-Rejection Reevaluation Report

**Gene:** SAGE1 (Sarcoma antigen 1)
**UniProt Accession:** Q9NXZ1
**Protein Name:** Sarcoma antigen 1
**Length:** 904 aa | **Mass:** 99.2 kDa
**Aliases:** SAGE
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA main: Nucleoplasm. Additional: Nuclear bodies. Reliability: Enhanced. UniProt: Nucleus (ECO:0000269 -- experimental). GO-CC: nuclear body (IDA:HPA), nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), integrator complex (IBA:GO_Central). STRONG nuclear evidence. Nucleoplasm + nuclear bodies. Integrator complex association suggests involvement in snRNA processing/transcription. |
| 2. Protein Size | 10 | 8 | 904 aa / 99.2 kDa. Large protein. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 10. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 8 | AlphaFold mean pLDDT: 50.2 (3.0% >90, 8.5% 70-90, 30.9% 50-70, 57.6% <50). PDB: 8HPP (X-ray, 3.00A, residues 818-904 only -- C-terminal tail). Very low AF confidence. Mostly disordered. |
| 5. Regulatory Domains | 50 | 20 | IPR029307, IPR051113. PF15300. Function: No annotated molecular function (empty field). Associated with integrator complex (GO-CC IBA). Integrator complex is involved in snRNA 3' end processing and transcription regulation. No annotated molecular function but complex association is suggestive. |
| 6. PPI Network | 50 | 15 | STRING: 15 partners. DDX43 (0.869), SPA17 (0.815), MAGEC2 (0.812), PRSS50 (0.771), GAGE1 (0.754), PAGE5 (0.737). Most partners are cancer-testis antigens (CTAs). INTS14 (0.626), INTS11 (0.613) -- Integrator complex subunits. IntAct: Empty. |
| **TOTAL** | **180** | **89** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Enhanced
- **Main Location:** Nucleoplasm
- **Additional:** Nuclear bodies
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** Nucleoplasm + nuclear bodies. Enhanced reliability. Very strong nuclear evidence.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000269 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0032039 (integrator complex)** -- IBA:GO_Central
- **GO:0016604 (nuclear body)** -- IDA:HPA
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005634 (nucleus)** -- IDA:UniProtKB

**Summary:** Very strong nuclear evidence. HPA Enhanced reliability with nucleoplasm + nuclear bodies. Integrator complex association (IBA). Nuclear score: 28/30.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 10 |
| Broad (All Fields) | 34 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:40415416** -- Chen C et al. (2025). "The progression of multiple myeloma is regulated by LILRB1 via the GATA2-SAGE1 pathway." *Br J Haematol*.
2. **PMID:35651938** -- Yang Y et al. (2022). "Identification of Novel Characteristics in TP53-Mutant Hepatocellular Carcinoma Using Bioinformatics." *Front Genet*.
3. **PMID:39161926** -- Hu J et al. (2024). "Characterization of RNA Processing Genes in Colon Cancer for Predicting Clinical Outcomes." *Biomark Insights*.
4. **PMID:21706474** -- Lim J et al. (2011). "OCT2, SSX and SAGE1 reveal the phenotypic heterogeneity of spermatocytic seminoma reflecting distinct subpopulations of spermatogonia." *J Pathol*.
5. **PMID:38862430** -- Yang X et al. (2024). "Pindel-TD: A Tandem Duplication Detector Based on A Pattern Growth Approach." *Genomics Proteomics Bioinformatics*.

**Assessment:** Cancer-testis antigen literature. SAGE1 is a CTA expressed in testis and various cancers. Very limited functional characterization.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NXZ1-F1, version 6
- **mean pLDDT: 50.2** (>90: 3.0%, 70-90: 8.5%, 50-70: 30.9%, <50: 57.6%)
- **Assessment:** VERY LOW confidence. The majority of the protein is disordered or low-confidence. Only a small C-terminal region is ordered.

### Experimental PDB Structures
- **1 structure:** 8HPP (X-ray, 3.00A, residues 818-904 only)
- **Assessment:** Only the very C-terminal tail is resolved. The bulk of the protein (1-817) has no experimental structure.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| DDX43 | 0.869 | 0 | Cancer-testis antigen |
| SPA17 | 0.815 | 0 | Sperm autoantigen |
| MAGEC2 | 0.812 | 0 | Cancer-testis antigen |
| PRSS50 | 0.771 | 0 | Testis-specific protease |
| INTS14 | 0.626 | 0 | Integrator complex subunit |
| INTS11 | 0.613 | 0 | Integrator complex subunit |

### IntAct
- **Empty.** No interactions recorded.

### PPI Network Assessment
- Network is predominantly cancer-testis antigens (CTAs). No experimental validation.
- Integrator complex connections (INTS14, INTS11) are database-driven, not experimental.
- Very weak PPI evidence overall.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SAGE1 was likely rejected due to very low structural confidence and very limited functional characterization.

### Recheck Analysis
1. **Nuclear evidence:** STRONG. HPA Enhanced: Nucleoplasm + Nuclear bodies. Integrator complex association.
2. **Functional context:** No annotated molecular function. Cancer-testis antigen. Integrator complex association (IBA) suggests involvement in snRNA processing, but no experimental confirmation.
3. **PubMed:** 10 strict. VERY LOW.
4. **Structure:** Very poor. mean pLDDT 50.2 with 57.6% <50.
5. **PPI:** Very weak. Only textmining/database connections to other CTAs.

### Verdict
**The original rejection was CORRECT, but this is a borderline case.** SAGE1 has excellent nuclear evidence (HPA Enhanced, nucleoplasm + nuclear bodies) and Integrator complex association, which is relevant for transcription. However, the complete absence of annotated function, very poor structural confidence (mostly disordered), and lack of experimental PPI data make it difficult to justify retention. Should remain REJECTED with a note for potential future re-evaluation if functional data emerges.

---

## TE-Regulator Relevance

LOW (with caveat). SAGE1 has nuclear localization in nucleoplasm and nuclear bodies, and is associated with the Integrator complex, which processes snRNA and regulates transcription. However, no functional characterization exists. The Integrator complex connection is solely via electronic annotation (IBA), not experimental. Without any functional data, the TE-regulatory relevance is speculative.

---

## Final Decision: REJECTED (borderline)

Score: 89/180. SAGE1 has strong nuclear evidence (HPA Enhanced) and Integrator complex association (IBA), but no annotated molecular function, very poor structural confidence, and almost no experimental PPI data. Rejected due to insufficient functional characterization, with a flag for potential re-evaluation.

---

## Manual Review Note
BORDERLINE REJECTION. SAGE1 has one of the strongest HPA nuclear profiles in this batch (Enhanced reliability, nucleoplasm + nuclear bodies). The Integrator complex association is intriguing because the Integrator regulates snRNA processing and transcription. However, the complete absence of any annotated molecular function, extremely poor AF confidence (mean pLDDT 50.2), and lack of experimental interactions make this gene unsuitable for current pipeline inclusion. Flag for re-evaluation if functional characterization emerges. Cancer-testis antigens like SAGE1 may have reproductive-tissue-specific regulatory roles that remain undiscovered.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000181433-SAGE1/subcellular

![](https://images.proteinatlas.org/3033/1854_G8_4_red_green.jpg)
![](https://images.proteinatlas.org/3033/1854_G8_5_red_green.jpg)
![](https://images.proteinatlas.org/3033/4_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/3033/4_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/3033/5_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/3033/5_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NXZ1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029307;IPR051113; |
| Pfam | PF15300; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181433-SAGE1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
