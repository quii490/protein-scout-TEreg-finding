# SLFN14 -- Critical False-Rejection Reevaluation Report

**Gene:** SLFN14 (Protein SLFN14)
**UniProt Accession:** P0C7P3
**Protein Name:** Protein SLFN14
**Length:** 912 aa | **Mass:** 103.9 kDa
**Aliases:** None
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | UniProt: Nucleus (ECO:0000269 x2 experimental). GO-CC: nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB). HPA: no localization data (reliability=null, empty lists). Nuclear evidence is from UniProt experimental only. Dual nuclear/cytoplasmic localization. |
| 2. Protein Size | 10 | 6 | 912 aa / 103.9 kDa. Very large protein. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 21. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 83.5 (46.2% >90, 39.8% 70-90, 7.7% 50-70, 6.4% <50). PDB: 9JN9 (EM, 3.36A), 9JR9 (2.84A), 9NYY (2.73A), 9UIE (2.88A) -- 4 cryo-EM structures, all full-length. Good structural coverage. |
| 5. Regulatory Domains | 50 | 30 | IPR027417, IPR031450, IPR029684, IPR007421, IPR038461, IPR048729. PF17057, PF04326, PF21026. FUNCTION: Ribosome-associated endoribonuclease. Cleaves mRNAs and rRNAs (PubMed:25996083). RNA surveillance -- recognizes stalled ribosomes and triggers endonucleolytic cleavage of aberrant mRNAs. RNA degradation activity. Schlafen family members in other species have known roles in viral restriction and translational control. |
| 6. PPI Network | 50 | 5 | STRING: 1 partner. FYB1 (0.405 -- very low confidence, textmining only). IntAct: 1 interactor. S100A10 (cross-linking, PMID:30021884). Very limited interaction data. |
| **TOTAL** | **180** | **97** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** null
- **Main Location:** No data (empty lists)
- **Additional:** No data (empty lists)
- **IF Image Status:** no_image_detected
- **Key Finding:** HPA has gene page but no subcellular localization or IF data.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000269 x2 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** -- IDA:UniProtKB (experimental)
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB (experimental)

**Summary:** SLFN14 localizes to both nucleus and cytoplasm (UniProt experimental). HPA provides no data. Nuclear score: 22/30 -- UniProt experimental evidence but limited HPA support and dual localization.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 21 |
| Broad (All Fields) | 32 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:40794453** -- Stapley RJ et al. (2025). "Platelet-specific SLFN14 deletion causes macrothrombocytopenia and platelet dysfunction through dysregulated megakaryocyte and platelet gene expression." *J Clin Invest*.
2. **PMID:36790527** -- Ver Donck F et al. (2023). "Ribosome dysfunction underlies SLFN14-related thrombocytopenia." *Blood*.
3. **PMID:40592880** -- Van Riper J et al. (2025). "CryoEM structure of the SLFN14 endoribonuclease reveals insight into RNA binding and cleavage." *Nat Commun*.
4. **PMID:31378119** -- Stapley RJ et al. (2020). "SLFN14 gene mutations associated with bleeding." *Platelets*.
5. **PMID:40510593** -- Xie H et al. (2025). "Novel mutation SLFN14 T853fs associated with inherited macrothrombocytopenia." *Mol Ther Nucleic Acids*.

**Assessment:** Literature is focused on SLFN14's role in platelet biology and thrombocytopenia. Schlafen family function in RNA degradation is well-established but SLFN14-specific literature is limited.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P0C7P3-F1, version 6
- **mean pLDDT: 83.5** (>90: 46.2%, 70-90: 39.8%, 50-70: 7.7%, <50: 6.4%)
- **Assessment:** Good overall confidence. Well-folded.

### Experimental PDB Structures
- **4 structures:** 9JN9 (EM, 3.36A), 9JR9 (EM, 2.84A), 9NYY (EM, 2.73A), 9UIE (EM, 2.88A)
- All full-length cryo-EM structures at good resolution.
- **Assessment:** Excellent structural coverage with multiple high-resolution structures.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING
- **1 partner only:** FYB1 (score 0.405, textmining only)
- **Assessment:** Essentially no interaction data. Very isolated.

### IntAct
- **1 interactor:** S100A10 (cross-linking, PMID:30021884)
- **Assessment:** Single cross-linking hit. Not validated.

### PPI Network Assessment
- EXTREMELY SPARSE. Only 1-2 low-confidence interactions. SLFN14 appears to function independently or in complexes not captured by current interaction databases.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SLFN14 was likely rejected due to extremely sparse PPI network and ribosome-associated rather than chromatin-associated function.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. UniProt experimental nucleus (ECO:0000269 x2). HPA has no data.
2. **Functional context:** Ribosome-associated endoribonuclease. RNA surveillance/degradation. Schlafen family -- some family members (e.g., SLFN11) have roles in viral restriction and translational control, but these are cytoplasmic functions.
3. **PubMed:** 21 strict. LOW.
4. **Structure:** 4 cryo-EM structures at good resolution. Excellent.
5. **PPI:** Essentially none. Extremely isolated.

### Verdict
**The original rejection was CORRECT.** SLFN14 is an endoribonuclease involved in ribosome-associated RNA surveillance. While it has nuclear localization (UniProt experimental), its function is cytoplasmic/ribosomal RNA degradation, not chromatin or transcriptional regulation. The Schlafen family has diverse functions (some nuclear, mostly cytoplasmic), and SLFN14 specifically shows ribosome association and endoribonuclease activity. The complete absence of PPI data further weakens the case. Should remain REJECTED.

---

## TE-Regulator Relevance

LOW. SLFN14 is a ribosome-associated endoribonuclease. Its RNA degradation activity could theoretically affect TE transcript stability, but this is an indirect and non-specific mechanism. No evidence for chromatin, transcriptional, or epigenetic regulatory function. Other Schlafen family members (SLFN11) have DNA damage response functions, but SLFN14 appears dedicated to ribosomal RNA surveillance.

---

## Final Decision: REJECTED

Score: 97/180. SLFN14 has good structural data (4 cryo-EM structures) and nuclear localization evidence, but its function is cytoplasmic/ribosomal RNA degradation, not chromatin regulation. The complete absence of PPI data and lack of TE-relevant function warrant rejection.

---

## Manual Review Note
CONFIRMED REJECTION. SLFN14 is a Schlafen family endoribonuclease with well-characterized ribosome-associated RNA cleavage activity. While the Schlafen family includes proteins with diverse functions (viral restriction, DNA damage response, translational control), SLFN14 appears specialized for ribosomal RNA surveillance. The 4 cryo-EM structures provide excellent structural characterization. However, the functional profile (ribosome-associated RNAse) and complete absence of interaction partners make it unsuitable for TE-regulatory investigation. Note: could be reconsidered if future data reveals a nuclear/chromatin function.
