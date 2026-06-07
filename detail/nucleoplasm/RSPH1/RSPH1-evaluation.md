# RSPH1 -- Critical False-Rejection Reevaluation Report

**Gene:** RSPH1 (Radial spoke head 1 homolog)
**UniProt Accession:** Q8WYR4
**Protein Name:** Radial spoke head 1 homolog
**Length:** 309 aa | **Mass:** 35.1 kDa
**Aliases:** TSA2, TSGA2
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 10 | HPA main: Centrosome, Basal body, Mid piece. Additional: Acrosome. Reliability: Uncertain. NO nuclear HPA annotation. UniProt: Cytoplasm (ECO:0000250), Chromosome (ECO:0000250 -- by similarity only), Cilium axoneme (ECO:0000269), Flagellum axoneme (ECO:0000250). GO-CC: condensed nuclear chromosome (IEA:Ensembl -- electronic annotation), nucleus (HDA:UniProtKB -- high-throughput), meiotic spindle (IEA:Ensembl). The chromosome annotation is by-similarity (ECO:0000250) only, and GO-CC nuclear annotations are electronic or high-throughput. Primary localization is ciliary/centrosomal. |
| 2. Protein Size | 10 | 10 | 309 aa / 35.1 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 27. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 74.2 (56.3% >90, 6.5% 70-90, 5.2% 50-70, 32.0% <50). PDB: 8J07 (EM, 4.10A, full length 1-309). Moderate AF confidence with significant disordered regions. |
| 5. Regulatory Domains | 50 | 0 | IPR003409. PF02493. Function: Part of axonemal radial spoke complexes for sperm/cilia motility. No chromatin, transcriptional, or epigenetic regulatory function. |
| 6. PPI Network | 50 | 20 | STRING: 15 partners. RSPH4A (0.990), RSPH9 (0.982), RSPH6A (0.861), ZMYND10 (0.844), RSPH3 (0.832). All radial spoke and ciliary partners. IntAct: 15 interactors including MORN3, TSPY2, METAP2, RSPH4A, RSPH6A, FBXO16, CCN2, EZR, FRMD4B, SH3GLB2, SF1, PDE4DIP, UBC, BTBD1, TUBB3. UniProt: MORN3 (7 experiments). All ciliary/cytoskeletal. |
| **TOTAL** | **180** | **68** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Uncertain
- **Main Location:** Centrosome, Basal body, Mid piece
- **Additional:** Acrosome
- **IF Image Status:** if_display_images_available (14 blue_red_green images)
- **Key Finding:** HPA does NOT detect RSPH1 in the nucleus. All HPA annotations are centrosomal/basal body/ciliary/sperm.

### UniProt Subcellular Location
- **Cytoplasm** -- ECO:0000250 (by similarity)
- **Chromosome** -- ECO:0000250 (by similarity) -- NOTE: "chromosome" not "nucleus"
- **Cytoplasm, cytoskeleton, cilium axoneme** -- ECO:0000269 (experimental)
- **Cytoplasm, cytoskeleton, flagellum axoneme** -- ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0000794 (condensed nuclear chromosome)** -- IEA:Ensembl (electronic annotation)
- **GO:0005634 (nucleus)** -- HDA:UniProtKB (high-throughput)
- **GO:0072687 (meiotic spindle)** -- IEA:Ensembl (electronic)
- **GO:0031514 (motile cilium)** -- IDA:UniProtKB
- **GO:0001535 (radial spoke head)** -- ISS:UniProtKB

**Summary:** HPA (Uncertain reliability) detects RSPH1 at centrosome/basal body/mid piece, NOT nucleus. UniProt has "chromosome" by similarity (not nucleus). The GO-CC nuclear annotations are electronic (IEA) or high-throughput (HDA). The "chromosome" annotation may relate to meiotic spindle association, not nucleoplasmic function. Nuclear score: 10/30 -- very weak nuclear evidence.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 27 |
| Broad (All Fields) | 43 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:20301301** -- Adam MP et al. (1993/updated). "Primary Ciliary Dyskinesia." *GeneReviews*.
2. **PMID:37601242** -- Wang M et al. (2023). "CCDC189 affects sperm flagellum formation by interacting with CABCOCO1." *Natl Sci Rev*.
3. **PMID:36820148** -- Zi X et al. (2023). "An Integrated Analysis Reveals Ciliary Abnormalities in Antrochoanal Polyps." *J Inflamm Res*.
4. **PMID:25789548** -- Frommer A et al. (2015). "Immunofluorescence Analysis and Diagnosis of Primary Ciliary Dyskinesia with Radial Spoke Defects." *Am J Respir Cell Mol Biol*.
5. **PMID:36873931** -- Aprea I et al. (2023). "Pathogenic gene variants in CCDC39, CCDC40, RSPH1, RSPH9, HYDIN, and SPEF2 cause defects of sperm flagella composition and male infertility." *Front Genet*.

**Assessment:** All literature is about primary ciliary dyskinesia, sperm flagella, and ciliary biology. No TE-related publications.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8WYR4-F1, version 6
- **mean pLDDT: 74.2** (>90: 56.3%, 70-90: 6.5%, 50-70: 5.2%, <50: 32.0%)
- **Assessment:** Moderate confidence. One-third of residues are low-confidence (<50).

### Experimental PDB Structures
- **1 structure:** 8J07 (EM, 4.10A, full length 1-309, in complex with radial spoke)
- **Assessment:** Full-length structure at moderate resolution in the radial spoke complex.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| RSPH4A | 0.990 | 0.828 | Radial spoke head |
| RSPH9 | 0.982 | 0.797 | Radial spoke head |
| RSPH6A | 0.861 | 0.583 | Radial spoke head |
| ZMYND10 | 0.844 | 0.144 | Ciliary protein |
| RSPH3 | 0.832 | 0.139 | Radial spoke head |

### IntAct (15 interactors)
Mostly Y2H interactions from PMID:35914814. Few validated: MORN3 (Y2H array), RSPH4A (Co-IP), RSPH6A (Co-IP), TSPY2 (Co-IP).

### PPI Network Assessment
- Network is exclusively ciliary/radial spoke/flagellar.
- No nuclear, chromatin, or transcriptional partners.
- No TE-relevant connections.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RSPH1 was likely rejected due to absence of nuclear HPA annotation and purely ciliary functional profile.

### Recheck Analysis
1. **Nuclear evidence:** VERY WEAK. HPA does NOT detect RSPH1 in nucleus (only centrosome/basal body). UniProt "chromosome" annotation is by similarity. GO-CC nuclear annotations are electronic or high-throughput.
2. **Functional context:** Axonemal radial spoke head component. Sperm/cilia motility. No regulatory function.
3. **PubMed:** 27 strict. LOW.
4. **Structure:** Moderate AF, one EM structure.
5. **PPI:** Exclusively ciliary/radial spoke. No nuclear connections.

### Verdict
**The original rejection was CORRECT.** RSPH1 is a dedicated ciliary/flagellar structural protein. The nuclear/chromosome annotations are weak (by-similarity, electronic, high-throughput) and HPA explicitly does not detect it in the nucleus. No regulatory function. Should remain REJECTED.

---

## TE-Regulator Relevance

NEGLIGIBLE. RSPH1 is a structural component of the axonemal radial spoke head complex, essential for ciliary and flagellar motility. Its biology is entirely mechanical (ciliary beating). No connection to TE regulation, chromatin modification, or transcription.

---

## Final Decision: REJECTED

Score: 68/180. RSPH1 has very weak nuclear evidence (HPA detects centrosome only, not nucleus), no regulatory domain function, and a dedicated ciliary/flagellar structural role. Not suitable for TE investigation. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. RSPH1 is a classic radial spoke head protein with well-established function in ciliary and flagellar motility. The "chromosome" UniProt annotation (ECO:0000250) and electronic GO-CC nuclear annotations are weak and inconsistent with the overwhelming ciliary functional evidence. Mutations in RSPH1 cause primary ciliary dyskinesia. No plausible TE-regulatory role.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WYR4 |
| SMART | SM00698; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003409; |
| Pfam | PF02493; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160188-RSPH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MORN3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
