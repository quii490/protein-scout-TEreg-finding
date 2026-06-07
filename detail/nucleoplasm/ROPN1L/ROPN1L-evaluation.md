# ROPN1L -- Critical False-Rejection Reevaluation Report

**Gene:** ROPN1L (Ropporin-1-like protein)
**UniProt Accession:** Q96C74
**Protein Name:** Ropporin-1-like protein
**Length:** 230 aa | **Mass:** 26.1 kDa
**Aliases:** ASP, RSPH11
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 7 | HPA main: Primary cilium transition zone, Mid piece, Principal piece, End piece. Additional: Nucleoplasm, Vesicles. Reliability: Supported. UniProt: Cell projection cilium flagellum (ECO:0000250), Cell projection cilium (ECO:0000269). GO-CC: cilium, sperm components, nucleoplasm (IDA:HPA). Nucleoplasm is an ADDITIONAL location, not primary. The primary locations are ciliary/sperm. Nuclear evidence is peripheral -- nucleoplasm appears as secondary, not main. |
| 2. Protein Size | 10 | 10 | 230 aa / 26.1 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 21. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 22 | AlphaFold mean pLDDT: 85.7 (64.8% >90, 18.7% 70-90, 11.3% 50-70, 5.2% <50). PDB: 8J07 (EM, 4.10A, full length 1-230). Good AF confidence. One EM structure at moderate resolution. |
| 5. Regulatory Domains | 50 | 5 | IPR047844. No Pfam domains. Function: Part of axonemal radial spoke complexes for sperm/cilia motility. Involved in PKA-dependent signaling for sperm capacitation. No chromatin, transcriptional, or epigenetic regulatory function. Purely structural/ciliary. |
| 6. PPI Network | 50 | 15 | STRING: Failed (HTTP 502). IntAct: 10 interactors. AKAP14, AKAP5, AKAP7, BEX2, SPA17, RSPH3, RSPH14, AKAP9, CD74. UniProt: AKAP14, AKAP5, AKAP7, BEX2, ROPN1L (self), RSPH3, SPA17. Network is ciliary/sperm signaling (AKAP family, radial spoke proteins). |
| **TOTAL** | **180** | **69** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Primary cilium transition zone, Mid piece, Principal piece, End piece
- **Additional:** Nucleoplasm, Vesicles
- **IF Image Status:** if_display_images_available (8 blue_red_green images)
- **Key Finding:** Nucleoplasm is classified as ADDITIONAL location, not primary. HPA IF images show primary ciliary and sperm tail staining, not nuclear.

### UniProt Subcellular Location
- **Cell projection, cilium, flagellum** -- ECO:0000250 (by similarity)
- **Cell projection, cilium** -- ECO:0000269 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0035869 (ciliary transition zone)** -- IDA:HPA
- **GO:0005929 (cilium)** -- IDA:UniProtKB
- **GO:0031514 (motile cilium)** -- IDA:BHF-UCL
- **GO:0005654 (nucleoplasm)** -- IDA:HPA (additional)
- **GO:0001534 (radial spoke)** -- ISS:UniProtKB
- **GO:0097229, 0097225, 0097228 (sperm components)** -- IDA:HPA

**Summary:** ROPN1L is primarily a ciliary/sperm protein. Nucleoplasm appears as a secondary/additional HPA annotation but is not the primary localization. The functional context is entirely ciliary/sperm motility. Nuclear score: 7/30 -- weak nuclear evidence (additional only).

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 21 |
| Broad (All Fields) | 37 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:40538010** -- Huang X et al. (2025). "Machine Learning-Driven Discovery of TRIM Genes as Diagnostic Biomarkers for Idiopathic Pulmonary Fibrosis." *Med Sci Monit*.
2. **PMID:25124046** -- Rattanachan S et al. (2014). "Opisthorchis viverrini: analysis of the sperm-specific rhophilin associated tail protein 1-like." *Acta Trop*.
3. **PMID:38027210** -- Sun W et al. (2023). "RNA sequencing profiles reveals progressively reduced spermatogenesis with progression in adult cryptorchidism." *Front Endocrinol*.
4. **PMID:35207567** -- Omolaoye TS et al. (2022). "Omics and Male Infertility: Highlighting the Application of Transcriptomic Data." *Life*.
5. **PMID:23303679** -- Fiedler SE et al. (2013). "Loss of R2D2 proteins ROPN1 and ROPN1L causes defects in murine sperm motility, phosphorylation, and fibrous sheath integrity." *Biol Reprod*.

**Assessment:** All literature is focused on sperm biology, cilia, and male fertility. No TE-related publications.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96C74-F1, version 6
- **mean pLDDT: 85.7** (>90: 64.8%, 70-90: 18.7%, 50-70: 11.3%, <50: 5.2%)
- **Assessment:** Good confidence. Well-folded small protein.

### Experimental PDB Structures
- **1 structure:** 8J07 (EM, 4.10A, full length 1-230)
- **Assessment:** Full-length structure at moderate resolution.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING
- **Status:** HTTP Error 502 -- STRING unavailable for this query.

### IntAct (10 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| AKAP14 | Validated 2H | 32296183 | PKA anchoring in sperm |
| AKAP5 | Validated 2H | 32296183 | PKA anchoring |
| AKAP7 | Validated 2H | 32296183 | PKA anchoring |
| SPA17 | Co-IP | 28514442 | Sperm autoantigen |
| RSPH3 | 2H Array | 31515488 | Radial spoke head |
| BEX2 | Validated 2H | 32296183 | Brain expressed |
| AKAP9 | Co-IP | 28514442 | Centrosome/Golgi |
| CD74 | Co-IP | 33961781 | MHC class II |

### PPI Network Assessment
- Network is entirely ciliary/sperm signaling (AKAP family) and radial spoke proteins.
- No chromatin, transcriptional, or nuclear PPI connections.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
ROPN1L was likely rejected due to primarily ciliary/sperm localization with only secondary nucleoplasmic annotation.

### Recheck Analysis
1. **Nuclear evidence:** WEAK. Nucleoplasm is HPA ADDITIONAL location only, not primary. Primary localization is ciliary/sperm.
2. **Functional context:** Radial spoke complex component for cilia/sperm motility. PKA-dependent signaling in sperm capacitation.
3. **PubMed:** 21 strict. LOW.
4. **Structure:** Good AF, one EM structure.
5. **PPI:** Entirely ciliary/sperm. No nuclear partners.

### Verdict
**The original rejection was CORRECT.** ROPN1L is a ciliary/sperm radial spoke protein. The nucleoplasmic annotation is secondary (additional, not primary) and likely reflects non-specific or trace localization. The functional profile is entirely dedicated to sperm/cilia motility with no evidence of nuclear, chromatin, or transcriptional regulatory function. Should remain REJECTED.

---

## TE-Regulator Relevance

NEGLIGIBLE. ROPN1L functions in the axonemal radial spoke complex of motile cilia and sperm flagella. Its biological role is mechanical (ciliary beating, sperm motility) and signaling (PKA in sperm capacitation). No connection to TE biology, chromatin, or nuclear regulation.

---

## Final Decision: REJECTED

Score: 69/180. ROPN1L has weak nuclear evidence (nucleoplasm is additional, not primary), no regulatory domain function, and a dedicated ciliary/sperm functional profile. Not suitable for TE-regulatory investigation. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. ROPN1L is a ropporin family protein that functions as part of the radial spoke complex in cilia and sperm flagella. The nucleoplasmic HPA annotation is "additional" (not primary) and inconsistent with the known biological function. No evidence supports nuclear or chromatin-level regulatory activity. Retaining this gene would be based on a secondary localization annotation rather than functional evidence.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96C74 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 17..46; /note="RIIa" |
| InterPro | IPR047844; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000145491-ROPN1L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SPA17 | Intact, Biogrid | true |
| AKAP14 | Intact | false |
| AKAP5 | Intact | false |
| BEX2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
