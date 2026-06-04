# RMP64 -- Critical False-Rejection Reevaluation Report

**Gene:** RMP64 (Ribonuclease MRP subunit P64)
**UniProt Accession:** Q6NW34
**Protein Name:** Ribonuclease MRP subunit P64
**Length:** 567 aa | **Mass:** 64.6 kDa
**Aliases:** C3orf17, NEPRO
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 20 | UniProt: Nucleus (ECO:0000269 -- experimental), Nucleus nucleolus (ECO:0000250 -- by similarity). GO-CC: nucleolus (ISS:UniProtKB), nucleus (IDA:UniProtKB), ribonuclease MRP complex (IDA:UniProtKB). HPA: page_found_no_if_image_detected -- no HPA localization data available. Nuclear evidence is from UniProt experimental (nucleus) and by-similarity (nucleolus). Valid but weaker than HPA-supported cases. |
| 2. Protein Size | 10 | 8 | 567 aa / 64.6 kDa. Moderate-large size. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 4. Novelty rule: 1-50=10. Extremely few publications. |
| 4. 3D Structure | 30 | 10 | AlphaFold mean pLDDT: 64.0 (20.5% >90, 29.5% 70-90, 10.4% 50-70, 39.7% <50). PDB: None. Low structural confidence overall. No experimental structures. |
| 5. Regulatory Domains | 50 | 5 | IPR052835, IPR027951. PF14780. Function: Specific component of RNase MRP complex involved in pre-rRNA processing. Role in cortex development downstream of Notch signaling. RNase MRP processes pre-rRNA and mitochondrial RNA. No direct transcriptional/chromatin regulatory function. Ribosome biogenesis role, not chromatin-level regulation. |
| 6. PPI Network | 50 | 5 | STRING: Not found (HTTP 404). IntAct: Empty. UniProt interactions: None. No interaction data available. |
| **TOTAL** | **180** | **58** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** page_found_no_if_image_detected
- **Reliability (IF):** null
- **Main Location:** No data
- **Additional:** No data
- **IF Image Status:** no_image_detected
- **Key Finding:** HPA has a gene page for RMP64 but no subcellular localization or IF data.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000269 (experimental)
- **Nucleus, nucleolus** -- ECO:0000250 (by similarity)

### GO Cellular Component (GO-CC)
- **GO:0005730 (nucleolus)** -- ISS:UniProtKB
- **GO:0005634 (nucleus)** -- IDA:UniProtKB
- **GO:0000172 (ribonuclease MRP complex)** -- IDA:UniProtKB

**Summary:** Nuclear localization supported by UniProt experimental evidence (nucleus) and by-similarity (nucleolus). RNase MRP complex localization is in the nucleolus. However, HPA has no localization data available. Nuclear score: 20/30 -- valid nuclear evidence but limited HPA support.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 4 |
| Broad (All Fields) | 4 |

**Novelty score: 10/10.** Extremely few publications (4 strict).

### Key Papers
1. **PMID:40867056** -- Liu Y et al. (2025). "Composition and RNA binding specificity of metazoan RNase MRP." *Nucleic Acids Res*.
2. **PMID:41888142** -- Zhou B et al. (2026). "Structural and evolutionary insights into the eukaryotic RNase MRP ribonucleoprotein complex." *Nat Commun*.
3. **PMID:40413743** -- Che R et al. (2025). "Identification of RMP24 and RMP64, human ribonuclease MRP-specific protein components." *Cell Rep*.
4. **PMID:41136609** -- Smith EM et al. (2026). "RNase MRP subunit composition and role in 40S ribosome biogenesis." *Nat Struct Mol Biol*.

**Assessment:** All 4 publications are about RNase MRP complex characterization. No publications link RMP64 to TE regulation.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q6NW34-F1, version 6
- **mean pLDDT: 64.0** (>90: 20.5%, 70-90: 29.5%, 50-70: 10.4%, <50: 39.7%)
- **Assessment:** Low-moderate overall confidence. Nearly 40% of residues have pLDDT <50.

### Experimental PDB Structures
- **None.**
- **Assessment:** No experimental structures available.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING
- **Status:** HTTP Error 404 -- STRING has no entry for RMP64.

### IntAct
- **Status:** Empty -- no interactions recorded.

### UniProt Interactions
- **None.**

### PPI Network Assessment
- No interaction data available from any source. As a component of the RNase MRP complex, RMP64 likely interacts with other complex subunits, but these interactions are not recorded in public databases.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RMP64 was likely rejected due to very limited data availability and low scores across multiple dimensions.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT but WEAK. UniProt experimental nucleus (ECO:0000269). HPA has no data. No IF images.
2. **Functional context:** RNase MRP complex component. Pre-rRNA processing. Not transcriptional or chromatin regulatory.
3. **PubMed:** 4 strict. Very low. HIGH NOVELTY.
4. **Structure:** Low AF confidence (mean pLDDT 64.0, 39.7% <50). No PDB structures.
5. **PPI:** No data. Empty STRING and IntAct.
6. **Regulatory domains:** Minimal. No chromatin/transcriptional regulatory domains.

### Verdict
**The original rejection was CORRECT.** RMP64 is a ribosome biogenesis factor (RNase MRP complex) without direct transcriptional or chromatin regulatory function. While nuclear localization is supported by UniProt experimental data, the functional profile does not suggest TE-regulatory relevance. The very low structural confidence and absence of PPI data further weaken the case. This gene should remain REJECTED.

---

## TE-Regulator Relevance

VERY LOW. RMP64 functions in pre-rRNA processing as part of the RNase MRP complex. This is a ribosomal biogenesis function, not chromatin or TE regulation. There is no evidence connecting RMP64 to transcriptional regulation, histone modification, DNA methylation, or any TE silencing mechanism. The protein's role is limited to ribosomal RNA maturation.

---

## Final Decision: REJECTED

Score: 58/180. Very low score across all dimensions except novelty. While RMP64 is nuclear (nucleolar), its function is exclusively in ribosome biogenesis (pre-rRNA processing) with no evidence of transcriptional, chromatin, or TE-regulatory activity. Structural data is poor and no interaction network data exists. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. RMP64 is a recently characterized component of the human RNase MRP complex involved in pre-rRNA processing. Its function is ribosomal biogenesis, not chromatin/transcriptional regulation. While it is nucleolar (nuclear subcompartment), this reflects its role in rRNA processing. No evidence supports TE-regulatory function. PubMed count of 4 indicates it is newly identified and under-characterized, but the known function is not relevant to TE biology.
