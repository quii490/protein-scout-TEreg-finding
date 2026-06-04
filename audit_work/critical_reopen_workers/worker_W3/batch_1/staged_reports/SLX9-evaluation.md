# SLX9 -- Critical False-Rejection Reevaluation Report

**Gene:** SLX9 (Ribosome biogenesis protein SLX9 homolog)
**UniProt Accession:** Q9NSI2
**Protein Name:** Ribosome biogenesis protein SLX9 homolog
**Length:** 230 aa | **Mass:** 25.5 kDa
**Aliases:** C21orf70, FAM207A
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA main: Nucleoli. Additional: Nucleoplasm. Reliability: Supported. UniProt: Nucleus nucleolus (ECO:0000250 -- by similarity). GO-CC: nucleolus (IEA:UniProtKB-SubCell), 90S preribosome (IEA:InterPro), preribosome small subunit precursor (IEA:InterPro). Nucleolar localization is well-supported by HPA. Nucleolus is a nuclear subcompartment but dedicated to ribosome biogenesis, not chromatin regulation. |
| 2. Protein Size | 10 | 10 | 230 aa / 25.5 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 5. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 71.0 (30.9% >90, 21.7% 70-90, 23.9% 50-70, 23.5% <50). PDB: 7WTS (EM, 3.20A), 7WTT (3.10A), 7WTU (3.00A), 7WTV (3.50A), 7WTW (3.20A) -- 5 cryo-EM structures, all full-length in pre-ribosome complexes. Excellent structural coverage. |
| 5. Regulatory Domains | 50 | 5 | IPR028160. PF15341. FUNCTION: May be involved in ribosome biogenesis. Pre-ribosome component. No chromatin, transcriptional, or epigenetic regulatory domains or functions. |
| 6. PPI Network | 50 | 15 | STRING: 15 partners. SENP6 (0.785 experimental), GPR1 (0.712), FAM50B (0.607), PRPF19 (0.604 experimental). IntAct: 15 interactors, mostly yeast ortholog interactions (ribosomal proteins: RPL4A, RPL5, RPS0A, RPS24A, RPS4A, TSR1, HHF1). UniProt: GOLGA2, GOLGA6L9, PICK1. Network is ribosome biogenesis. |
| **TOTAL** | **180** | **86** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoli
- **Additional:** Nucleoplasm
- **IF Image Status:** no_image_detected (red_green images available via image_urls)
- **Key Finding:** Nucleoli (Supported) + nucleoplasm (additional). Nucleolar localization is consistent with ribosome biogenesis function.

### UniProt Subcellular Location
- **Nucleus, nucleolus** -- ECO:0000250 (by similarity)

### GO Cellular Component (GO-CC)
- **GO:0005730 (nucleolus)** -- IEA:UniProtKB-SubCell
- **GO:0030686 (90S preribosome)** -- IEA:InterPro
- **GO:0030688 (preribosome, small subunit precursor)** -- IEA:InterPro

**Summary:** SLX9 is a nucleolar protein involved in pre-ribosome assembly. Nucleolar localization is a specialized nuclear function dedicated to ribosome biogenesis, not chromatin or transcription regulation. Nuclear score: 22/30 -- nucleolar, not chromatin-associated.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 5 |
| Broad (All Fields) | 7 |

**Novelty score: 10/10.** Extremely few publications.

### Key Papers
1. **PMID:31067825** -- Gotz S et al. (2019). "A Novel G-Quadruplex Binding Protein in Yeast-Slx9." *Molecules*. -- NOTE: G-quadruplex binding!
2. **PMID:25895666** -- Fischer U et al. (2015). "A non-canonical mechanism for Crm1-export cargo complex assembly." *eLife*.
3. **PMID:17018574** -- Bax R et al. (2006). "Slx9p facilitates efficient ITS1 processing of pre-rRNA in Saccharomyces cerevisiae." *RNA*.
4. **PMID:20551975** -- Kaiser VB et al. (2011). "A new plant sex-linked gene with high sequence diversity and possible introgression of the X copy." *Heredity*.
5. **PMID:30653518** -- Linnemann J et al. (2019). "Impact of two neighbouring ribosomal protein clusters on biogenesis factor binding and assembly of yeast late small ribosomal subunit precursors." *PLoS One*.

**Assessment:** Yeast Slx9 is a pre-rRNA processing factor and G-quadruplex binding protein. Human SLX9 is very poorly characterized.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NSI2-F1, version 6
- **mean pLDDT: 71.0** (>90: 30.9%, 70-90: 21.7%, 50-70: 23.9%, <50: 23.5%)
- **Assessment:** Moderate confidence. About one-quarter of residues below pLDDT 50.

### Experimental PDB Structures
- **5 structures:** 7WTS (3.20A), 7WTT (3.10A), 7WTU (3.00A), 7WTV (3.50A), 7WTW (3.20A) -- all full-length cryo-EM in pre-ribosome complexes.
- **Assessment:** Excellent structural coverage in the context of ribosome biogenesis intermediates.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| SENP6 | 0.785 | 0.785 | SUMO protease |
| PRPF19 | 0.604 | 0.604 | Spliceosome/DNA repair |
| GPR1 | 0.712 | 0 | G protein-coupled receptor |
| FAM50B | 0.607 | 0 | Uncharacterized |
| MCTS2P | 0.600 | 0 | Pseudogene |

### IntAct (15 interactors)
Mostly yeast Slx9 interaction data with ribosomal proteins (RPL4A, RPL5, RPS0A, RPS24A, RPS4A) and ribosome biogenesis factors (TSR1, BMS1, BFR2).

### PPI Network Assessment
- Network is ribosomal/ribosome biogenesis.
- SENP6 (SUMO protease) interaction is experimentally supported and interesting -- SUMO pathway connection.
- PRPF19 interaction connects to spliceosome, which is nuclear.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SLX9 was likely rejected due to ribosome biogenesis function without regulatory relevance.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. HPA Supported nucleoli. Nucleolar localization, consistent with ribosome biogenesis function.
2. **Functional context:** Pre-rRNA processing and ribosome biogenesis. Yeast ortholog binds G-quadruplex structures -- potentially relevant for nucleic acid structure recognition.
3. **PubMed:** 5 strict. EXTREMELY LOW.
4. **Structure:** 5 cryo-EM structures in pre-ribosome complexes. Excellent.
5. **PPI:** Ribosome biogenesis network. SENP6 (SUMO protease) interaction is notable.

### Verdict
**The original rejection was CORRECT.** SLX9 is a nucleolar ribosome biogenesis factor. Its function is pre-rRNA processing, not chromatin or transcriptional regulation. While the G-quadruplex binding activity (yeast) and SENP6 interaction are interesting, there is no evidence for TE-relevant regulatory function. Should remain REJECTED.

---

## TE-Regulator Relevance

VERY LOW. SLX9 functions in pre-rRNA processing and small ribosomal subunit assembly. Its biological role is ribosomal biogenesis. No evidence for chromatin modification, transcription regulation, or TE silencing. The G-quadruplex binding activity described in yeast could theoretically affect nucleic acid structures, but this is speculative and not demonstrated for human SLX9.

---

## Final Decision: REJECTED

Score: 86/180. SLX9 has good nuclear (nucleolar) localization and excellent structural data, but its function is exclusively ribosomal biogenesis with no chromatin or TE-regulatory activity. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. SLX9 is a conserved ribosome biogenesis factor involved in pre-rRNA ITS1 processing and small ribosomal subunit maturation. 5 cryo-EM structures place it in pre-ribosome complexes. While yeast Slx9 has G-quadruplex nucleic acid binding activity, this likely relates to rRNA processing rather than DNA/chromatin-level regulation. Human SLX9 is very poorly characterized (PubMed=5). Not suitable for TE investigation.
