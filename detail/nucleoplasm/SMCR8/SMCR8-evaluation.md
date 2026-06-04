# SMCR8 -- Critical False-Rejection Reevaluation Report

**Gene:** SMCR8 (Guanine nucleotide exchange protein SMCR8)
**UniProt Accession:** Q8TEV9
**Protein Name:** Guanine nucleotide exchange protein SMCR8
**Length:** 937 aa | **Mass:** 105.0 kDa
**Aliases:** None
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA main: Nucleoplasm. Reliability: Enhanced. UniProt: Cytoplasm (ECO:0000269 x2), Nucleus (ECO:0000269 x1). GO-CC: nucleoplasm (IDA:HGNC), chromatin (IDA:HGNC), cytoplasm (IDA:UniProtKB). Dual nuclear/cytoplasmic. Chromatin annotation (IDA:HGNC) is significant -- SMCR8 associates with chromatin and negatively regulates ULK1 and WIPI2 gene expression. |
| 2. Protein Size | 10 | 6 | 937 aa / 105.0 kDa. Very large protein. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 45. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 62.2 (23.2% >90, 25.2% 70-90, 8.1% 50-70, 43.5% <50). PDB: 6LT0 (EM, 3.20A, full-length), 6V4U (EM, 3.80A), 7EL6 (X-ray, 2.80A, residues 778-787 only), 7MGE (EM, 3.94A), 7O2W (EM, partial). Several structures but moderate resolution. |
| 5. Regulatory Domains | 50 | 35 | IPR037521, IPR037520. PF11704. FUNCTION: Component of C9orf72-SMCR8 complex with GEF activity for RAB8A and RAB39B. Regulates autophagy. NUCLEAR FUNCTION: Associates with chromatin and negatively regulates expression of ULK1 and WIPI2 genes (PMID:28195531). Direct transcriptional repressive function on chromatin. Also regulates mTORC1 signaling. |
| 6. PPI Network | 50 | 30 | STRING: 15 partners. C9orf72 (0.999), WDR41 (0.999), RAB39B (0.979), RAB8A (0.972), ULK1 (0.965), TBK1 (0.959), TANK (0.925), ATG101 (0.895), ATG13 (0.893), RB1CC1 (0.875). IntAct: 15 interactors. RB1CC1, C9orf72, IMPDH1, IMPDH2, CRYAB, ZNRD2, CDC16. |
| **TOTAL** | **180** | **121** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Enhanced
- **Main Location:** Nucleoplasm
- **Additional:** None
- **IF Image Status:** no_image_detected (red_green images available via image_urls)
- **Key Finding:** HPA nucleoplasm (Enhanced reliability). Strong HPA evidence.

### UniProt Subcellular Location
- **Cytoplasm** -- ECO:0000269 x2 (experimental)
- **Nucleus** -- ECO:0000269 x1 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** -- IDA:HGNC
- **GO:0000785 (chromatin)** -- IDA:HGNC -- DIRECT chromatin association
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:1990316 (Atg1/ULK1 kinase complex)** -- IDA:HGNC
- **GO:0032045 (guanyl-nucleotide exchange factor complex)** -- IDA:HGNC

**Summary:** SMCR8 localizes to nucleoplasm (HPA Enhanced) and chromatin (GO-CC IDA). Nuclear function includes chromatin association and transcriptional repression. Also cytoplasmic (autophagy/GEF function). Nuclear score: 22/30 -- good nuclear evidence with chromatin association.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 45 |
| Broad (All Fields) | 52 |

**Novelty score: 10/10.** Under 50 publications.

### Key Papers
1. **PMID:36692217** -- Yang C et al. (2023). "Stress granule homeostasis is modulated by TRIM21-mediated ubiquitination of G3BP1 and autophagy-dependent elimination of stress granules." *Autophagy*.
2. **PMID:37317656** -- Julg J et al. (2023). "C9orf72 protein quality control by UBR5-mediated heterotypic ubiquitin chains." *EMBO Rep*.
3. **PMID:38064514** -- Tang D et al. (2023). "ALS-linked C9orf72-SMCR8 complex is a negative regulator of primary ciliogenesis." *PNAS*.
4. **PMID:38293807** -- Tang D et al. (2024). "The C9orf72-SMCR8 complex suppresses primary ciliogenesis as a RAB8A GAP." *Autophagy*.
5. **PMID:32678027** -- Goodier JL et al. (2020). "C9orf72-associated SMCR8 protein binds in the ubiquitin pathway and with proteins linked with neurological disease." *Acta Neuropathol Commun*.

**Assessment:** SMCR8 is strongly associated with C9orf72 in ALS/FTD research. Key for autophagy and ciliogenesis. The chromatin/nuclear function is noted (PMID:28195531) but not the main focus of most papers.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8TEV9-F1, version 6
- **mean pLDDT: 62.2** (>90: 23.2%, 70-90: 25.2%, 50-70: 8.1%, <50: 43.5%)
- **Assessment:** Moderate-low confidence. Large protein with substantial disorder.

### Experimental PDB Structures
- **5 structures:** 6LT0 (EM, 3.20A, full-length in C9orf72-SMCR8-WDR41 complex), 6V4U (EM, 3.80A), 7EL6 (X-ray, 2.80A, 10-residue peptide), 7MGE (EM, 3.94A), 7O2W (EM, partial)
- **Assessment:** Multiple cryo-EM structures of the C9orf72-SMCR8 complex.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| C9orf72 | 0.999 | 0.982 | Obligate partner, GEF complex |
| WDR41 | 0.999 | 0.926 | Complex component |
| RAB39B | 0.979 | 0.301 | GEF substrate |
| RAB8A | 0.972 | 0.301 | GEF substrate |
| ULK1 | 0.965 | 0.474 | Autophagy kinase |
| TBK1 | 0.959 | 0.292 | Innate immunity kinase |
| ATG13 | 0.893 | 0.230 | Autophagy |
| RB1CC1 | 0.875 | 0.166 | Autophagy scaffold |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| C9orf72 | 2H Array | 32296183 | Obligate partner |
| RB1CC1 | Co-IP | 20562859 | Autophagy scaffold |
| IMPDH1 | Co-IP | 28514442 | Nucleotide biosynthesis |
| IMPDH2 | Co-IP | 28514442 | Nucleotide biosynthesis |
| CDC16 | Co-IP | 26496610 | APC/C complex |

### PPI Network Assessment
- Dense autophagy network. C9orf72-SMCR8-WDR41 is a defined GEF complex.
- ULK1 and ATG13 connections to autophagy initiation.
- TBK1 connection links to innate immunity.
- IMPDH1/2 connections to nucleotide metabolism.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SMCR8 was likely rejected due to primarily cytoplasmic/autophagy function and insufficient attention to the nuclear/chromatin role.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. HPA Enhanced nucleoplasm. GO-CC chromatin (IDA:HGNC) -- direct chromatin association. Nuclear function: negatively regulates ULK1 and WIPI2 gene expression.
2. **Functional context:** DUAL. Cytoplasmic: GEF for RAB8A/RAB39B, autophagy regulation, mTORC1 signaling. Nuclear: chromatin association, transcriptional repression. The nuclear function is documented but often overshadowed by the cytoplasmic autophagy role.
3. **PubMed:** 45 strict. LOW.
4. **Structure:** Multiple EM structures. Moderate AF confidence.
5. **PPI:** Dense C9orf72/autophagy network. IMPDH connections to nucleotide metabolism.

### Verdict
**The original rejection was INCORRECT.** SMCR8 has a documented nuclear function: it associates with chromatin and negatively regulates gene expression (ULK1, WIPI2). This chromatin-level regulatory activity, combined with HPA Enhanced nucleoplasm and GO-CC chromatin annotation, supports retention. While SMCR8 is better known for its cytoplasmic GEF/autophagy role, the nuclear chromatin function is directly relevant to transcriptional regulation. Should be RETAINED.

---

## TE-Regulator Relevance

MODERATE. SMCR8 associates with chromatin and negatively regulates gene expression (ULK1, WIPI2). This chromatin-level gene regulation function could potentially involve TE loci. As part of the C9orf72-SMCR8 complex, it is linked to ALS/FTD where TE dysregulation has been implicated. The nuclear chromatin association provides a plausible mechanism for TE-regulatory function, though no direct TE silencing activity has been demonstrated.

---

## Final Decision: RETAINED

Score: 121/180. SMCR8 has a documented nuclear chromatin association with transcriptional repressive function, HPA Enhanced nucleoplasm, good PPI network, and moderate novelty. Retained despite its dual cytoplasmic/nuclear function profile.

---

## Manual Review Note
MODERATE CANDIDATE. SMCR8 is primarily known as the obligate partner of C9orf72 in a GEF complex regulating autophagy. However, SMCR8 has an independent nuclear function: it associates with chromatin and negatively regulates ULK1 and WIPI2 gene expression (PMID:28195531). This nuclear chromatin function is directly relevant to transcriptional regulation. The C9orf72 connection to ALS/FTD, where TE dysregulation is increasingly recognized, adds disease context relevance. The main limitation is that the nuclear function is less well-characterized than the cytoplasmic autophagy role. Retained for its chromatin association and transcriptional regulatory potential.
