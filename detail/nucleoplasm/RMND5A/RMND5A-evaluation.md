# RMND5A -- Critical False-Rejection Reevaluation Report

**Gene:** RMND5A
**UniProt Accession:** Q9H871
**Protein Name:** E3 ubiquitin-protein transferase RMND5A
**Length:** 391 aa | **Mass:** 44.0 kDa
**Aliases:** None
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 26 | HPA main: Nucleoplasm (Supported). UniProt: Nucleus nucleoplasm (ECO:0000269 x3), Cytoplasm (ECO:0000269 x3). GO-CC: nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB), ubiquitin ligase complex (IDA:UniProtKB). Nucleoplasmic localization is well-supported, but also cytoplasmic. Dual localization reduces nuclear score slightly. |
| 2. Protein Size | 10 | 10 | 391 aa / 44.0 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 16. Novelty rule: 1-50=10. Very few publications. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 89.9 (65.2% >90, 30.7% 70-90, 4.1% 50-70, 0.0% <50). PDB: 8PJN (EM, 3.40A, full length). Good confidence, one experimental structure. |
| 5. Regulatory Domains | 50 | 35 | IPR013144, IPR024964, IPR006595, IPR006594, IPR045098, IPR037680, IPR044063, IPR027370. PF10607, PF13445. Function: Core component of CTLH E3 ubiquitin ligase complex. Mediates ubiquitination and proteasomal degradation of transcription factor HBP1. CTLH complex targets include transcription factors. E3 ligase activity directly regulates protein stability, including transcription factors. Indirect but significant regulatory role. |
| 6. PPI Network | 50 | 35 | STRING: 15 partners with strong experimental support. GID8 (0.999), RANBP9 (0.997), WDR26 (0.997), ARMC8 (0.996), GID4 (0.991), MKLN1 (0.990), MAEA (0.969). IntAct: 15 interactors including RANBP9, MAEA, TENT4A, ZMYND19, H2BC1 (histone!), ARMC8, HTRA2, MKLN1, TCEAL9, YPEL5. UniProt: 15 interactors including TARDBP (TDP-43), ATXN1. Large CTLH complex network. |
| **TOTAL** | **180** | **140** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional:** None
- **IF Image Status:** no_image_detected (red_green images available via image_urls but not flagged as if_display)
- **Key Finding:** Nucleoplasm localization supported.

### UniProt Subcellular Location
- **Nucleus, nucleoplasm** -- ECO:0000269 x3 (experimental)
- **Cytoplasm** -- ECO:0000269 x3 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005634 (nucleus)** -- IDA:UniProtKB
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:0005829 (cytosol)** -- TAS:Reactome
- **GO:0034657 (GID complex)** -- IBA:GO_Central
- **GO:0000151 (ubiquitin ligase complex)** -- IDA:UniProtKB

**Summary:** RMND5A localizes to both nucleoplasm and cytoplasm. Experimental evidence supports nucleoplasmic localization. Nuclear score: 26/30 -- good nuclear evidence with dual localization caveat.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 16 |
| Symbol-only | 25 |
| Broad (All Fields) | 26 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:34079591** -- Chen S et al. (2021). "miR-590-5p targets RMND5A and promotes migration in pancreatic adenocarcinoma cell lines." *Oncol Lett*.
2. **PMID:31285494** -- Maitland MER et al. (2019). "The mammalian CTLH complex is an E3 ubiquitin ligase that targets its subunit muskelin for degradation." *Sci Rep*.
3. **PMID:31885576** -- Huffman N et al. (2019). "The CTLH Complex in Cancer Cell Plasticity." *J Oncol*.
4. **PMID:28731166** -- Liu H, Ye H (2017). "Screening of the prognostic targets for breast cancer based co-expression modules analysis." *Mol Med Rep*.
5. **PMID:40377017** -- Nakagawa T et al. (2025). "E3 ubiquitin ligase RMND5A maintains the self-renewal state of human neural stem/precursor cells by regulating Wnt and mTOR signaling pathways." *FEBS Lett*.

**Assessment:** Very low publication count (16 strict). RMND5A is under-studied, especially regarding TE regulation.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9H871-F1, version 6
- **mean pLDDT: 89.9** (>90: 65.2%, 70-90: 30.7%, 50-70: 4.1%, <50: 0.0%)
- **Assessment:** Excellent confidence. Virtually no low-confidence regions.

### Experimental PDB Structures
- **1 structure:** 8PJN (EM, 3.40A, full length 1-391)
- **Assessment:** Single cryo-EM structure of full protein at moderate resolution.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| GID8 | 0.999 | 0.934 | CTLH complex component |
| RANBP9 | 0.997 | 0.934 | Ran-binding, CTLH complex |
| WDR26 | 0.997 | 0.890 | CTLH complex scaffold |
| ARMC8 | 0.996 | 0.849 | CTLH complex |
| GID4 | 0.991 | 0.859 | Substrate receptor |
| MKLN1 | 0.990 | 0.835 | CTLH complex |
| MAEA | 0.969 | 0.845 | E3 ligase partner |
| RMND5B | 0.901 | 0.782 | Paralog |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| RANBP9 | Co-IP | 28514442 | CTLH complex |
| MAEA | Co-IP | 28514442 | E3 ligase activity |
| H2BC1 | Co-IP | 28514442 | Histone H2B -- chromatin connection |
| MKLN1 | Co-IP | 28514442 | CTLH complex |
| ARMC8 | Co-IP | 28514442 | CTLH complex |

### PPI Network Assessment
- Dense CTLH E3 ubiquitin ligase complex network with strong experimental support.
- Interaction with H2BC1 (histone H2B) is notable for chromatin relevance.
- UniProt interactions with TARDBP (TDP-43, RNA-binding) and ATXN1 (transcription factor).

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RMND5A was likely rejected due to incomplete reporting or placeholder text.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. HPA nucleoplasm (Supported). UniProt experimental nucleoplasm x3.
2. **Functional context:** E3 ubiquitin ligase (CTLH complex). Targets transcription factor HBP1 for degradation. E3 ligase activity is indirect regulatory, but regulation of transcription factor stability has downstream transcriptional effects.
3. **PubMed:** 16 strict. Very low. HIGH NOVELTY.
4. **Structure:** Good AF (mean pLDDT 89.9), one EM structure.
5. **PPI:** H2BC1 histone interaction suggests potential chromatin-level involvement.

### Verdict
**The original rejection was INCORRECT.** RMND5A has nuclear localization (nucleoplasm), functions as an E3 ubiquitin ligase regulating transcription factor stability, has high novelty (PubMed=16), and interacts with histone H2B. Should be RETAINED for further evaluation.

---

## TE-Regulator Relevance

MODERATE. RMND5A is an E3 ubiquitin ligase component of the CTLH complex. Its direct regulatory function is protein ubiquitination and degradation, targeting transcription factor HBP1. The CTLH complex also regulates stem cell self-renewal through Wnt and mTOR pathways. The interaction with histone H2B (H2BC1) suggests potential chromatin-level involvement. As an E3 ligase, RMND5A could regulate stability of TE-associated transcription factors or chromatin modifiers. However, no direct TE silencing function is known.

---

## Final Decision: RETAINED

Score: 140/180. RMND5A is a nucleoplasmic E3 ubiquitin ligase with good nuclear evidence, high novelty, excellent structural confidence, and a chromatin-relevant interaction (H2BC1 histone). The CTLH complex's role in transcription factor degradation provides indirect regulatory potential. Retained for the pipeline.

---

## Manual Review Note
MODERATE CANDIDATE. RMND5A's E3 ligase activity on transcription factors (HBP1) and stem cell self-renewal regulation suggest broad regulatory potential. The H2BC1 (histone H2B) interaction is interesting for chromatin biology. PubMed count of 16 indicates very limited investigation. The CTLH complex (GID complex) is a highly conserved ubiquitin ligase system. Structural data is good with excellent AF confidence and one EM structure. Retained.
