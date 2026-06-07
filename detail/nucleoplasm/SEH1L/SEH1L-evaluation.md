# SEH1L -- Critical False-Rejection Reevaluation Report

**Gene:** SEH1L (Nucleoporin SEH1)
**UniProt Accession:** Q96EE3
**Protein Name:** Nucleoporin SEH1
**Length:** 360 aa | **Mass:** 39.6 kDa
**Aliases:** SEC13L, SEH1
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 15 | UniProt: Chromosome centromere kinetochore (ECO:0000269 x2), Nucleus nuclear pore complex (ECO:0000269 x2), Lysosome membrane (ECO:0000269). GO-CC: nuclear pore, nuclear envelope, nuclear pore outer ring, kinetochore. HPA: no localization data (reliability=null, empty). SEH1L is a nuclear pore complex component. This is nuclear periphery, NOT nuclear interior. NPC function in nucleocytoplasmic transport. Also kinetochore and lysosome (GATOR2). |
| 2. Protein Size | 10 | 10 | 360 aa / 39.6 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 15. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 26 | AlphaFold mean pLDDT: 86.9 (73.3% >90, 11.7% 70-90, 5.6% 50-70, 9.4% <50). PDB: 8 structures. 7UHY (EM, 3.66A), 9LVJ (3.82A), 9LVK (3.59A), 9LWF (3.41A) -- all cryo-EM of nuclear pore and GATOR2 complexes. Good structural coverage. |
| 5. Regulatory Domains | 50 | 10 | IPR037363, IPR015943, IPR020472, IPR036322, IPR001680. PF00400 (WD40 repeat). Function: NPC component + GATOR2 complex (mTORC1 activator). WD40 repeat beta-propeller -- a scaffold domain, not a catalytic domain. No chromatin/transcriptional regulatory function. NPC-mediated transport and mTORC1 amino acid sensing. |
| 6. PPI Network | 50 | 35 | STRING: 15 partners. NUP133 (0.999), NUP107 (0.999), NUP85 (0.999), NUP43 (0.999), SEC13 (0.999), NUP37 (0.999), MIOS (0.999), WDR59 (0.999), WDR24 (0.999), NPRL2 (0.999). HUGE NPC and GATOR2 network. IntAct: 15 interactors. NUP107, NUP98, SLX4, BECN1, COPS5, HERC2, LMNA, NCBP2, CEP192. |
| **TOTAL** | **180** | **106** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** null
- **Main Location:** No data (empty lists)
- **Additional:** No data (empty lists)
- **IF Image Status:** no_image_detected
- **Key Finding:** HPA has gene page but no subcellular localization data or IF images.

### UniProt Subcellular Location
- **Chromosome, centromere, kinetochore** -- ECO:0000269 x2 (experimental)
- **Nucleus, nuclear pore complex** -- ECO:0000269 x2 (experimental)
- **Lysosome membrane** -- ECO:0000269 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0005643 (nuclear pore)** -- NAS:ComplexPortal
- **GO:0005635 (nuclear envelope)** -- IDA:ComplexPortal
- **GO:0031080 (nuclear pore outer ring)** -- IDA:UniProtKB
- **GO:0000776 (kinetochore)** -- IEA:UniProtKB-KW
- **GO:0061700 (GATOR2 complex)** -- IDA:UniProtKB
- **GO:0005765 (lysosomal membrane)** -- IDA:UniProtKB

**Summary:** SEH1L is a nuclear pore complex outer ring component (Nup107-160 subcomplex) and GATOR2 complex component. Nuclear pore is nuclear periphery, not nuclear interior. Also localizes to kinetochore and lysosome. Nuclear score: 15/30 -- nuclear periphery (pore), not interior.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 15 |
| Broad (All Fields) | 24 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:35831510** -- Valenstein ML et al. (2022). "Structure of the nutrient-sensing hub GATOR2." *Nature*.
2. **PMID:23723238** -- Bar-Peled L et al. (2013). "A Tumor suppressor complex with GAP activity for the Rag GTPases that signal amino acid sufficiency to mTORC1." *Science*.
3. **PMID:40781725** -- Wei Y et al. (2025). "Screening, identification, and experimental validation of SUMOylation biomarkers in Parkinson's disease." *Hereditas*.
4. **PMID:38372438** -- Yang C et al. (2024). "New insights into GATOR2-dependent interactions and its conformational changes in amino acid sensing." *Biosci Rep*.
5. **PMID:38505924** -- Yuan D et al. (2024). "Identification of Key Ubiquitination-Related Genes and Their Association with Immune Infiltration in Osteoarthritis Based on the mRNA-miRNA Network." *Crit Rev Immunol*.

**Assessment:** Literature focuses on NPC biology and GATOR2/mTORC1 amino acid sensing. No TE-related publications.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96EE3-F1, version 6
- **mean pLDDT: 86.9** (>90: 73.3%, 70-90: 11.7%, 50-70: 5.6%, <50: 9.4%)
- **Assessment:** Good confidence. WD40 beta-propeller is well-folded.

### Experimental PDB Structures
- **8 structures:** 5A9Q (EM, 23A), 7PEQ (35A), 7R5J (50A), 7R5K (12A), 7UHY (3.66A), 9LVJ (3.82A), 9LVK (3.59A), 9LWF (3.41A)
- All cryo-EM structures in NPC or GATOR2 complexes
- **Assessment:** Extensive structural coverage, mostly in complex. Resolution varies widely.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| NUP133 | 0.999 | 0.998 | NPC Nup107-160 complex |
| NUP107 | 0.999 | 0.998 | NPC Nup107-160 |
| NUP85 | 0.999 | 0.999 | NPC Nup107-160 |
| SEC13 | 0.999 | 0.997 | NPC + GATOR2 |
| MIOS | 0.999 | 0.996 | GATOR2 |
| WDR59 | 0.999 | 0.999 | GATOR2 |
| WDR24 | 0.999 | 0.999 | GATOR2 |
| NPRL2 | 0.999 | 0.997 | GATOR1 (inhibited by GATOR2) |

### IntAct (15 interactors)
Strong NPC interaction network: NUP107, NUP98, LMNA (nuclear lamina), NCBP2 (cap-binding complex).
Also: SLX4 (DNA repair), BECN1 (autophagy), COPS5 (COP9 signalosome), HERC2 (E3 ligase).

### PPI Network Assessment
- Very dense, well-validated network spanning NPC and GATOR2/mTORC1.
- LMNA interaction connects to nuclear lamina/chromatin interface.
- NCBP2 interaction connects to mRNA cap-binding.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SEH1L was likely rejected due to nuclear periphery (NPC) rather than nuclear interior localization, and non-regulatory function.

### Recheck Analysis
1. **Nuclear evidence:** NUCLEAR PERIPHERY. NPC component. Nuclear pore outer ring. NOT nuclear interior/nucleoplasm.
2. **Functional context:** Nucleocytoplasmic transport (NPC) and mTORC1 amino acid sensing (GATOR2). Both are non-chromatin functions.
3. **PubMed:** 15 strict. LOW.
4. **Structure:** 8 PDB structures, good AF. Excellent structural data.
5. **PPI:** Dense NPC + mTORC1 network. Well-validated.

### Verdict
**The original rejection was CORRECT.** SEH1L is a nuclear pore complex component (Nup107-160 subcomplex) and GATOR2/mTORC1 regulator. Its nuclear localization is at the nuclear pore (periphery), not the nuclear interior where chromatin/transcription regulation occurs. Neither NPC transport nor mTORC1 signaling represent direct TE-regulatory functions. Should remain REJECTED.

---

## TE-Regulator Relevance

LOW. SEH1L functions in nucleocytoplasmic transport and mTORC1 activation. While NPC-mediated transport could theoretically affect TE transcript export, this is an indirect and non-specific mechanism. The GATOR2/mTORC1 function is metabolic signaling, not TE-specific. No evidence for direct chromatin or transcriptional regulatory activity.

---

## Final Decision: REJECTED

Score: 106/180. SEH1L has excellent structural data and a dense PPI network, but its localization is nuclear periphery (NPC), not nuclear interior, and its functions (NPC transport, mTORC1 signaling) are not directly TE-regulatory. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. SEH1L is a well-studied nucleoporin (Nup107-160 subcomplex) with dual function in nuclear pore transport and GATOR2-mediated mTORC1 activation. While the NPC is nuclear-associated, NPC proteins function at the nuclear-cytoplasmic interface, not in the nuclear interior. SEH1L has no chromatin, transcriptional, or epigenetic regulatory domains or functions. The GATOR2 role in mTORC1 signaling is metabolic, not TE-regulatory. Rejected despite excellent structural data and dense PPI network.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96EE3 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037363;IPR015943;IPR020472;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000085415-SEH1L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NUP43 | Intact, Biogrid | true |
| NUP85 | Intact, Biogrid | true |
| SEC13 | Intact, Biogrid, Opencell | true |
| AHCTF1 | Intact | false |
| CCNF | Biogrid | false |
| MIOS | Biogrid | false |
| MTMR14 | Biogrid | false |
| MYC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
