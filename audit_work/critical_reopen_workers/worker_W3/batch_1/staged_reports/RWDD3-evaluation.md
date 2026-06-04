# RWDD3 -- Critical False-Rejection Reevaluation Report

**Gene:** RWDD3 (RWD domain-containing protein 3)
**UniProt Accession:** Q9Y3V2
**Protein Name:** RWD domain-containing protein 3
**Length:** 267 aa | **Mass:** 30.5 kDa
**Aliases:** RSUME
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | UniProt: Nucleus (ECO:0000269 -- experimental), Cytoplasm (ECO:0000269). GO-CC: nucleus (IEA:UniProtKB-SubCell), cytoplasm (IEA:UniProtKB-SubCell). HPA: hpa_localization_available but no subcellular location data available (reliability=null, empty location lists). Nuclear evidence is from UniProt experimental only. HPA has no data. |
| 2. Protein Size | 10 | 10 | 267 aa / 30.5 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 18. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 20 | AlphaFold mean pLDDT: 81.6 (24.0% >90, 65.2% 70-90, 3.7% 50-70, 7.1% <50). PDB: 2EBK (NMR, residues 1-121), 4Y1L (X-ray, 2.70A, residues 2-113). Partial structures only (N-terminal RWD domain). Good AF confidence overall. |
| 5. Regulatory Domains | 50 | 40 | IPR006575 (RWD domain), IPR038840, IPR016135. PF05773. FUNCTION: Enhancer of SUMO conjugation. Increases SUMO conjugation to proteins including HIF1A, PIAS, NFKBIA, NR3C1, TOP1. Regulates NF-kappa-B and HIF1A signaling pathways through sumoylation. SUMOylation is a KEY post-translational modification involved in transcriptional regulation, chromatin organization, and TE silencing. Acts through interaction with UBE2I/UBC9 (E2 SUMO enzyme). |
| 6. PPI Network | 50 | 30 | STRING: 9 partners. UBE2I (0.991), SUMO1 (0.753), VHL (0.692), HIF1A (0.676), SAE1 (0.568), UBA2 (0.551). IntAct: 4 interactors. UBE2I (direct interaction, pull-down), SUMO1, NFKBIA, HIF1A. All SUMO pathway partners. |
| **TOTAL** | **180** | **132** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** null
- **Main Location:** No data (empty lists)
- **Additional:** No data (empty lists)
- **IF Image Status:** no_image_detected
- **Key Finding:** HPA has a gene page but does not report any subcellular localization. No IF images.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000269 (experimental)
- **Cytoplasm** -- ECO:0000269 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** -- IEA:UniProtKB-SubCell
- **GO:0005737 (cytoplasm)** -- IEA:UniProtKB-SubCell

**Summary:** UniProt experimental evidence supports both nuclear and cytoplasmic localization. HPA provides no localization data. Nuclear score: 22/30 -- UniProt experimental evidence for nucleus, but limited HPA support.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 18 |
| Broad (All Fields) | 35 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:35528020** -- Fuertes M et al. (2022). "Impact of RSUME Actions on Biomolecular Modifications in Physio-Pathological Processes." *Front Endocrinol*.
2. **PMID:31864228** -- Elguero B et al. (2019). "Modifications in the cellular proteome and their clinical application." *Medicina*.
3. **PMID:29436665** -- Ji CX et al. (2018). "MicroRNA-375 inhibits glioma cell proliferation and migration by downregulating RWDD3 in vitro." *Oncol Rep*.
4. **PMID:34768754** -- Ward Z et al. (2021). "Novel and Annotated Long Noncoding RNAs Associated with Ischemia in the Human Heart." *Int J Mol Sci*.
5. **PMID:29622689** -- Fuertes M et al. (2018). "Protein stabilization by RSUME accounts for PTTG pituitary tumor abundance and oncogenicity." *Endocr Relat Cancer*.

**Assessment:** Literature focuses on RSUME's role in SUMOylation enhancement and cancer biology. Direct relevance to protein modification pathways.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9Y3V2-F1, version 6
- **mean pLDDT: 81.6** (>90: 24.0%, 70-90: 65.2%, 50-70: 3.7%, <50: 7.1%)
- **Assessment:** Good overall confidence. Most residues 70-90.

### Experimental PDB Structures
- **2 structures:** 2EBK (NMR, residues 1-121 -- N-terminal RWD domain), 4Y1L (X-ray, 2.70A, residues 2-113 in complex with UBE2I)
- **Assessment:** Partial structural coverage of the RWD domain. C-terminal region not covered.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (9 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| UBE2I | 0.991 | 0.926 | E2 SUMO-conjugating enzyme |
| SUMO1 | 0.753 | 0.292 | Small ubiquitin-like modifier |
| VHL | 0.692 | 0.510 | E3 ubiquitin ligase |
| HIF1A | 0.676 | 0.510 | Hypoxia transcription factor |
| SAE1 | 0.568 | 0 | SUMO E1 subunit |
| UBA2 | 0.551 | 0 | SUMO E1 subunit |
| RANBP2 | 0.510 | 0 | SUMO E3 ligase / nuclear pore |

### IntAct (4 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| UBE2I | Pull-down (direct) | 17956732 | Core SUMO E2 enzyme |
| SUMO1 | Co-IP | 17956732 | SUMO modifier |
| NFKBIA | Co-IP | 17956732 | NF-kB inhibitor |
| HIF1A | Co-IP | 17956732 | Hypoxia transcription factor |

### PPI Network Assessment
- Dedicated SUMOylation network. UBE2I is the core interaction -- RWDD3 acts as a SUMOylation enhancer.
- HIF1A and NFKBIA sumoylation connects to transcription regulation.
- RANBP2 connection to nuclear pore/SUMO E3 is notable.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RWDD3 was likely rejected due to incomplete HPA data and possibly undervaluation of the SUMOylation regulatory function.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. UniProt experimental nucleus (ECO:0000269). HPA has no data available.
2. **Functional context:** SUMOylation enhancer. Directly enhances SUMO conjugation to target proteins. SUMOylation is a critical PTM for transcriptional regulation, chromatin organization, and TE silencing. Regulates HIF1A (transcription factor) and NFKBIA (NF-kB pathway) through sumoylation.
3. **PubMed:** 18 strict. VERY LOW.
4. **Structure:** Partial PDB structures + good AF confidence.
5. **PPI:** Dedicated SUMO pathway network (UBE2I, SUMO1, RANBP2).

### Verdict
**The original rejection was INCORRECT.** RWDD3/RSUME is a SUMOylation enhancer -- SUMO is a critical pathway for chromatin organization and TE silencing. The protein directly interacts with UBE2I (E2 SUMO enzyme) and enhances SUMO conjugation. While nuclear evidence is UniProt-only (no HPA data), the SUMOylation function is strongly chromatin-relevant. Should be RETAINED.

---

## TE-Regulator Relevance

HIGH. RWDD3 (RSUME) enhances SUMO conjugation to target proteins. SUMOylation is a key post-translational modification involved in transcriptional repression, heterochromatin formation, and TE silencing. The SUMO pathway is directly implicated in KRAB-ZFP/KAP1-mediated TE repression. RWDD3's role as a SUMOylation enhancer positions it upstream of these silencing pathways. The interaction with RANBP2 (SUMO E3 ligase at nuclear pore) further supports nuclear/complex-level SUMO function.

---

## Final Decision: RETAINED

Score: 132/180. RWDD3 is a SUMOylation enhancer with direct relevance to chromatin regulation and TE silencing pathways. Strong PPI network (SUMO pathway core components), good structural data, and very high novelty (PubMed=18). Retained.

---

## Manual Review Note
STRONG CANDIDATE. RWDD3 (RSUME) functions as an enhancer of SUMO conjugation, a pathway directly implicated in TE silencing. The core interaction with UBE2I (SUMO E2) positions RWDD3 as a regulator of global SUMOylation. SUMO modification is critical for KAP1/TRIM28-mediated TE repression, heterochromatin formation, and PML nuclear body function. HIF1A and NFKBIA sumoylation links to hypoxic and inflammatory transcriptional programs that may affect TE expression. The HPA data gap (no localization/images) is the main weakness. Retained for its high regulatory relevance despite limited HPA evidence.
