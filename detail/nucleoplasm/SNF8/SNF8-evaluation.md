# SNF8 -- Critical False-Rejection Reevaluation Report

**Gene:** SNF8 (Vacuolar-sorting protein SNF8)
**UniProt Accession:** Q96H20
**Protein Name:** Vacuolar-sorting protein SNF8
**Length:** 258 aa | **Mass:** 28.9 kDa
**Aliases:** EAP30
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 18 | HPA main: Cytosol. Additional: Nucleoplasm. Reliability: Supported. UniProt: Cytoplasm, Endosome membrane, Nucleus (ECO:0000305), Late endosome membrane. GO-CC: nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB), endosome membrane (IDA:UniProtKB), ESCRT II complex (IDA:UniProtKB), transcription regulator complex (IDA:MGI). Nucleoplasm is ADDITIONAL, not primary. Nuclear annotation has ECO:0000305 (curator inference). |
| 2. Protein Size | 10 | 10 | 258 aa / 28.9 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 20. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 84.9 (48.8% >90, 36.4% 70-90, 12.8% 50-70, 1.9% <50). PDB: 2ZME (X-ray, 2.90A, full-length), 3CUQ (X-ray, 2.61A, residues 25-258). Good AF and two X-ray structures. |
| 5. Regulatory Domains | 50 | 20 | IPR016689, IPR040608, IPR036388, IPR036390. PF04157. FUNCTION: ESCRT-II complex component for MVB sorting. ALSO: may play a role in transcription regulation by participating in derepression of transcription by RNA polymerase II, possibly via interaction with ELL (PubMed:). ESCRT-II components have moonlighting nuclear functions in transcription. ELL is a transcription elongation factor. |
| 6. PPI Network | 50 | 30 | STRING: 15 partners. VPS25 (0.999), VPS36 (0.999), CHMP6 (0.999), VPS28 (0.992). ELL (0.971 experimental). IntAct: 15 interactors. VPS25, VPS36, VPS20, NIF3L1, DVL2, ADORA1. UniProt: 29 interactors including ELL, KDM1A (LSD1 histone demethylase!), POLR2A (RNA Pol II), PRMT6 (arginine methyltransferase), SMARCD1 (SWI/SNF chromatin remodeler), MCM2. |
| **TOTAL** | **180** | **112** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **Additional:** Nucleoplasm
- **IF Image Status:** if_display_images_available (4 blue_red_green images)
- **Key Finding:** Cytosol is main, nucleoplasm is additional. ESCRT-II is primarily endosomal but has documented nuclear moonlighting.

### UniProt Subcellular Location
- **Cytoplasm** -- no evidence code
- **Endosome membrane** -- no evidence code
- **Nucleus** -- ECO:0000305 (curator inference)
- **Late endosome membrane** -- no evidence code

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005634 (nucleus)** -- IDA:UniProtKB
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:0000814 (ESCRT II complex)** -- IDA:UniProtKB
- **GO:0005667 (transcription regulator complex)** -- IDA:MGI
- **GO:0010008 (endosome membrane)** -- IDA:UniProtKB

**Summary:** SNF8 has dual localization: cytosolic/endosomal (ESCRT-II) and nuclear (transcription regulator complex). Nuclear/mucleoplasm evidence is from HPA and UniProt. The transcription regulator complex annotation (MGI) supports nuclear regulatory function. Nuclear score: 18/30 -- nucleus is secondary to endosomal function.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 20 |
| Broad (All Fields) | 38 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:32829877** -- Han S et al. (2020). "VPS-22/SNF8 regulates longevity via modulating the activity of DAF-16 in C. elegans." *Biochem Biophys Res Commun*.
2. **PMID:30154260** -- Holt S et al. (2018). "Polygenic Analysis in Absence of Major Effector ATF1 Unveils Novel Components in Yeast Flavor Ester Biosynthesis." *mBio*.
3. **PMID:7785322** -- Yeghiayan P et al. (1995). "Molecular analysis of the SNF8 gene of Saccharomyces cerevisiae." *Yeast*.
4. **PMID:23171048** -- Carrasquillo R et al. (2012). "SNF8, a member of the ESCRT-II complex, interacts with TRPC6 and enhances its channel activity." *BMC Cell Biol*.
5. **PMID:32255230** -- Hoban K et al. (2020). "ESCRT-dependent protein sorting is required for the viability of yeast clathrin-mediated endocytosis mutants." *Traffic*.

**Assessment:** SNF8 is primarily studied as an ESCRT-II component in endosomal sorting. The nuclear transcription role (via ELL interaction) is acknowledged but not the main research focus.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96H20-F1, version 6
- **mean pLDDT: 84.9** (>90: 48.8%, 70-90: 36.4%, 50-70: 12.8%, <50: 1.9%)
- **Assessment:** Good confidence. Well-folded.

### Experimental PDB Structures
- **2 structures:** 2ZME (X-ray, 2.90A, full length), 3CUQ (X-ray, 2.61A, residues 25-258)
- **Assessment:** Good experimental coverage with two X-ray structures at moderate resolution.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| VPS25 | 0.999 | 0.997 | ESCRT-II subunit |
| VPS36 | 0.999 | 0.999 | ESCRT-II subunit |
| CHMP6 | 0.999 | 0.954 | ESCRT-III |
| ELL | 0.971 | 0.594 | Transcription elongation factor |

### UniProt Interactions (key nuclear-relevant)
| Partner | Experiments | Function |
|---------|------------|----------|
| KDM1A | 2 | LSD1 -- histone H3K4 demethylase |
| POLR2A | 2 | RNA Polymerase II largest subunit |
| PRMT6 | 2 | Protein arginine methyltransferase |
| SMARCD1 | 3 | SWI/SNF chromatin remodeler subunit |
| MCM2 | 8 | DNA replication licensing |
| ELL | 3 | Transcription elongation factor |
| STAU1 | 3 | RNA-binding protein |

### PPI Network Assessment
- PRIMARY: ESCRT-II/MVB sorting (VPS25, VPS36, CHMP6, etc.)
- SECONDARY (moonlighting): Nuclear transcription network -- ELL, KDM1A (LSD1), POLR2A, PRMT6, SMARCD1 (SWI/SNF), MCM2. These nuclear interactions are of moderate quality (2-8 experiments) but collectively suggest a real nuclear moonlighting function.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SNF8 was likely rejected due to primarily endosomal (ESCRT-II) function with nuclear localization being secondary.

### Recheck Analysis
1. **Nuclear evidence:** SECONDARY but PRESENT. HPA nucleoplasm (additional). Nucleus (UniProt, curator inference). GO-CC transcription regulator complex (IDA:MGI).
2. **Functional context:** ESCRT-II MVB sorting (primary). Moonlighting nuclear function in transcription regulation via ELL interaction and RNA Pol II derepression. UniProt interactions with KDM1A (LSD1 histone demethylase), POLR2A, PRMT6, and SMARCD1 (SWI/SNF) strongly suggest a nuclear regulatory role.
3. **PubMed:** 20 strict. LOW.
4. **Structure:** Good AF and 2 X-ray structures.
5. **PPI:** Nuclear transcription PPI network is surprisingly rich -- KDM1A (histone demethylase), SMARCD1 (SWI/SNF), ELL, POLR2A, PRMT6.

### Verdict
**The original rejection was INCORRECT.** While SNF8 is primarily an ESCRT-II endosomal protein, its nuclear moonlighting role in transcription regulation is well-supported by PPI data (KDM1A/LSD1 histone demethylase, POLR2A, SMARCD1/SWI-SNF, ELL, PRMT6). The transcription regulator complex annotation (MGI) and ELL-mediated transcription derepression function provide a direct nuclear regulatory role. Should be RETAINED.

---

## TE-Regulator Relevance

MODERATE-HIGH. SNF8's nuclear PPI network includes KDM1A (LSD1 -- H3K4me1/me2 demethylase), SMARCD1 (SWI/SNF chromatin remodeler), POLR2A (RNA Pol II), PRMT6 (arginine methyltransferase), and ELL (transcription elongation factor). KDM1A/LSD1 is a key histone demethylase directly involved in chromatin regulation and TE silencing. SWI/SNF is a major chromatin remodeling complex. While SNF8's primary role is endosomal, the quality and composition of its nuclear interaction network strongly suggests chromatin-level regulatory involvement.

---

## Final Decision: RETAINED

Score: 112/180. SNF8 has a documented nuclear moonlighting function in transcription regulation with rich nuclear PPI connections including LSD1, SWI/SNF, POLR2A, PRMT6, and ELL. Retained despite its primary ESCRT-II endosomal role.

---

## Manual Review Note
MODERATE CANDIDATE with nuclear moonlighting. SNF8 (EAP30) is a core component of ESCRT-II, a complex essential for multivesicular body sorting at endosomes. However, SNF8 has a well-documented moonlighting role in the nucleus: it participates in transcription derepression through interaction with ELL (transcription elongation factor). The UniProt interaction network is striking -- KDM1A/LSD1 (histone demethylase), SMARCD1 (SWI/SNF), POLR2A, and PRMT6 all point to chromatin-level function. The HPA detects SNF8 in nucleoplasm (additional location). While the primary function is endosomal, the nuclear PPI connections are too chromatin-relevant to dismiss. Retained for further evaluation of its nuclear regulatory function.
