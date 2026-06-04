# CARD8 – Critical False-Rejection Reevaluation Report

**Gene:** CARD8 (Caspase recruitment domain-containing protein 8)  
**UniProt Accession:** Q9Y2G2  
**Protein Name:** Caspase recruitment domain-containing protein 8  
**Length:** 537 aa | **Mass:** 60.7 kDa  
**Aliases:** DACAR, KIAA0955, NDPP1  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 2 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA: Nucleoplasm (main, Supported). UniProt: Cytoplasm (ECO:0000269 x3), Nucleus (ECO:0000269 x2), Inflammasome (ECO:0000269 x4). GO-CC: nucleoplasm (IDA:HPA), nucleus (IDA:HGNC-UCL), cytoplasm (IDA:UniProtKB), CARD8 inflammasome complex (IDA), NLRP3 inflammasome complex (IDA). Strong nuclear evidence (HPA + UniProt + GO all IDA-level). However, CARD8's primary functional compartment is the cytoplasm (inflammasome) – nuclear localization may be secondary or regulatory. |
| 2. Protein Size | 10 | 10 | 537 aa / 60.7 kDa – moderate-large size. Full marks. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 172. PubMed>100→REJECTED. CARD8 is very well-studied in inflammasome biology, innate immunity, and HIV-1 sensing. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 71.0 (41.7% >90, 23.3% 70-90, 31.3% <50). PDB: 4IKM (X-ray, 2.46A, CARD domain), 6K9F (EM, 3.70A, CARD filament), 6XKJ (EM, 3.54A), 7JKQ (EM, 3.30A, full-length), 7JN7 (EM, 3.30A, full-length). Five experimental structures including full-length. Good structural coverage. |
| 5. Regulatory Domains | 50 | 30 | IPR001315 (CARD domain), IPR011029 (DEATH-like domain), IPR025307 (FIIND domain), IPR051249. PF00619 (CARD), PF13553 (FIIND). CARD8 is an inflammasome sensor that activates caspase-1 and induces pyroptosis. It also inhibits NF-kB activation. NF-kB regulates TE expression in inflammatory contexts. CARD8 senses HIV-1 protease activity, linking it to retroviral biology. Functionally relevant to TE regulation through NF-kB pathway modulation, but primarily an innate immune protein, not a chromatin/transcriptional regulator. |
| 6. PPI Network | 50 | 35 | STRING: NLRP3 (0.998), CASP1 (0.997), PYCARD (0.996), CASP5 (0.989), AIM2 (0.981), DPP9 (0.972, experimental 0.9), NLRP1 (0.956), GSDMD (0.902), DHX33 (0.9). IntAct: HDAC3 (co-IP), TADA2A (co-IP), TADA3 (co-IP), VPS72 (co-IP), LRIF1 (co-IP), NFRKB (co-IP), E2F6 (co-IP), TAB1 (co-IP). KEY FINDINGS: HDAC3 is a histone deacetylase that contributes to TE silencing. TADA2A/TADA3 are SAGA/STAGA HAT complex components. VPS72 is a chromatin remodeling factor. These chromatin-modifying interactions (all co-IP, PMID:28514442) are HIGHLY RELEVANT to TE biology. |
| **TOTAL** | **180** | **121** | |

**NOTE: PubMed>100 (strict=172) triggers REJECTION rule.**

---

## Nuclear Evidence Section

### HPA
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional:** None
- **Key Finding:** HPA detects CARD8 exclusively in the nucleoplasm. No cytoplasmic annotation in HPA despite cytoplasmic inflammasome function. This is notable – the IF-based HPA annotation is nuclear, while the functional (inflammasome) context is cytoplasmic.

### UniProt Subcellular Location
- **Cytoplasm** – ECO:0000269 x3 (experimental, multiple publications)
- **Nucleus** – ECO:0000269 x2 (experimental)
- **Inflammasome** – ECO:0000269 x4 (experimental, the primary functional compartment)

### GO-CC
- **GO:0005654 (nucleoplasm)** – IDA:HPA
- **GO:0005634 (nucleus)** – IDA:HGNC-UCL
- **GO:0005737 (cytoplasm)** – IDA:UniProtKB
- **GO:0140634 (CARD8 inflammasome complex)** – IDA:UniProtKB
- **GO:0072559 (NLRP3 inflammasome complex)** – IDA:UniProtKB

**Summary:** CARD8 has strong nuclear evidence (HPA Nucleoplasm + UniProt experimental + GO IDA), but its primary functional role is cytoplasmic (inflammasome). Nuclear localization may represent a regulatory pool or a non-canonical function. Nuclear score: 22/30 – strong evidence but competing cytoplasmic/inflammasome annotations reduce specificity.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict | 172 |
| Broad | 297 |

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers
1. **PMID:35857590** – Robinson KS et al. (2022). ZAKalpha-driven ribotoxic stress activates NLRP1 inflammasome. *Science.*
2. **PMID:39351983** – Pandey A et al. (2025). Molecular mechanisms of inflammasome complexes. *Immunol Rev.*
3. **PMID:32558991** – Taabazuing CY et al. (2020). "The NLRP1 and CARD8 inflammasomes." *Immunol Rev.* – Comprehensive review.
4. **PMID:33542150** – Wang Q et al. (2021). "CARD8 is an inflammasome sensor for HIV-1 protease activity." *Science.* – KEY: CARD8 senses retroviral protease, linking to retroviral/ERV biology.
5. **PMID:36745138** – de Lima JD et al. (2023). Genetic and epigenetic regulation of innate immune response to gout.

---

## AlphaFold / PDB / PAE

- **AlphaFold:** mean pLDDT 71.0
- **PDB:** 5 structures: 4IKM (CARD domain, 2.46A), 6K9F (CARD filament), 6XKJ, 7JKQ (full-length, 3.30A), 7JN7 (full-length, 3.30A)
- **Assessment:** Good structural coverage with full-length and domain structures. PAE 图像暂无数据。

---

## FALSE REJECTION RECHECK

### Analysis
1. **Nuclear evidence:** STRONG (HPA Nucleoplasm + UniProt experimental + GO IDA)
2. **PPI network:** EXCEPTIONALLY RELEVANT to TE biology – interactions with HDAC3 (histone deacetylase), TADA2A/TADA3 (SAGA HAT complex), VPS72 (chromatin remodeling), E2F6 (transcription factor), NFRKB (NF-kB-related). All from co-IP (PMID:28514442).
3. **HIV-1 sensing:** CARD8 detects HIV-1 protease activity (PMID:33542150). HIV-1 is a retrovirus evolutionarily related to endogenous retroviruses. CARD8's role as a retroviral sensor suggests potential involvement in detecting/reacting to endogenous retroelements.
4. **NF-kB inhibition:** CARD8 inhibits NF-kB, which regulates TE expression.
5. **PubMed:** 172 strict >100 → automatic rejection.

### Verdict
**The original rejection was TECHNICALLY CORRECT under PubMed>100 rule.** However, CARD8 has the most TE-relevant PPI network of any gene in this batch (HDAC3, TADA2A/TADA3, VPS72) and senses retroviral protease activity (HIV-1). The PubMed>100 rule excludes it, but the connection between inflammasome/chromatin biology and TE regulation is underexplored. CARD8 could link innate immune sensing of retroelements to chromatin modifications.

**Decision: REJECTED (PubMed>100 rule).** Exception candidate.

---

## TE-Regulator Relevance

CARD8 is HIGHLY relevant:
1. **Interacts with HDAC3** – HDAC3 is a histone deacetylase that contributes to TE silencing by maintaining repressive chromatin states.
2. **Interacts with TADA2A/TADA3** – Components of SAGA/STAGA HAT complexes that acetylate histones and regulate transcription.
3. **Interacts with VPS72** – Chromatin remodeling factor.
4. **Senses HIV-1 protease** – Retroviral sensing mechanism could extend to endogenous retrovirus detection.
5. **NF-kB pathway regulation** – NF-kB drives TE expression in inflammatory contexts; CARD8 inhibits NF-kB.

---

## Final Decision: REJECTED (PubMed>100 rule, strict=172)

Score: 121/180. PubMed literature count exceeds threshold. Exception candidate for chromatin-modifying interactor network and retroviral sensing function.

---

## Manual Review Note
HIGH PRIORITY EXCEPTION CANDIDATE. Despite PubMed>100 rejection, CARD8's PPI network includes multiple chromatin-modifying proteins (HDAC3, TADA2A, TADA3, VPS72) that are directly involved in TE silencing pathways. Additionally, CARD8's function as an HIV-1 protease sensor (PMID:33542150, Science 2021) demonstrates retroviral recognition capability that could extend to endogenous retroelements. The NF-kB inhibitory function links innate immunity to TE expression control. If the PubMed threshold is ever waived, CARD8 should be prioritized for its unique position at the intersection of innate immune sensing, chromatin modification, and retroviral biology. BCLAF1 and CARD8 are the two strongest "rejected but highly relevant" candidates in this batch.
