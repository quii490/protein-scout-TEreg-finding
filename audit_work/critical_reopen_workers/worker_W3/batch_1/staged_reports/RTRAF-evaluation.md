# RTRAF -- Critical False-Rejection Reevaluation Report

**Gene:** RTRAF (tRNA-splicing ligase complex subunit RTRAF)
**UniProt Accession:** Q9Y224
**Protein Name:** tRNA-splicing ligase complex subunit RTRAF
**Length:** 244 aa | **Mass:** 28.1 kDa
**Aliases:** C14orf166
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 25 | HPA main: Nucleoplasm. Reliability: Supported. UniProt: Nucleus (ECO:0000269 x2 experimental), Cytoplasm cytosol (ECO:0000269 x2), Centrosome (ECO:0000269). GO-CC: nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB), centrosome (IDA:UniProtKB). Good nuclear evidence with dual nucleocytoplasmic distribution. |
| 2. Protein Size | 10 | 10 | 244 aa / 28.1 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 3. Novelty rule: 1-50=10. Extremely few publications under the RTRAF symbol. |
| 4. 3D Structure | 30 | 14 | AlphaFold mean pLDDT: 71.6 (0.0% >90, 65.2% 70-90, 25.8% 50-70, 9.0% <50). PDB: 7P3A (X-ray, 2.00A, residues 2-101 only). Partial structure only (N-terminal domain). Moderate AF confidence overall. |
| 5. Regulatory Domains | 50 | 15 | IPR019265. PF10036. FUNCTION: RNA-binding protein involved in modulation of mRNA transcription by Polymerase II (PubMed:16950395). Role in RNA transport (PubMed:24608264). Also involved in tRNA splicing ligase complex and influenza virus replication. RNA-binding and transcription modulation are relevant but indirect. |
| 6. PPI Network | 50 | 15 | STRING: Failed (HTTP 502). IntAct: 15 interactors. CALM1, NIN, DISC1, GABARAPL2, KCNMA1, CUL5, and viral proteins (NSS, NS1 influenza). UniProt interactions: None. Mixed quality -- some viral interactions, some human. |
| **TOTAL** | **180** | **89** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional:** None
- **IF Image Status:** no_image_detected (red_green images available via image_urls)
- **Key Finding:** Nucleoplasm (Supported). HPA IF images available but not flagged as display.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000269 x2 (experimental)
- **Cytoplasm, cytosol** -- ECO:0000269 x2 (experimental)
- **Cytoplasm, perinuclear region** -- ECO:0000269
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome** -- ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005634 (nucleus)** -- IDA:UniProtKB
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:0005813 (centrosome)** -- IDA:UniProtKB
- **GO:0072669 (tRNA-splicing ligase complex)** -- IDA:UniProtKB
- **GO:0072686 (mitotic spindle)** -- IDA:UniProtKB

**Summary:** RTRAF localizes to nucleoplasm (HPA Supported) and also cytoplasm/centrosome. Good nuclear evidence with experimental support. Nuclear score: 25/30.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 3 |
| Broad (All Fields) | 22 |

**Novelty score: 10/10.** Extremely few publications under RTRAF symbol. Note: alias C14orf166 may have additional publications.

### Key Papers
1. **PMID:38503217** -- Pei X et al. (2024). "ER-tethered RNA-binding protein controls NADPH oxidase translation for hydrogen peroxide homeostasis." *Redox Biol*.
2. **PMID:30833903** -- Pazo A et al. (2019). "hCLE/RTRAF-HSPC117-DDX1-FAM98B: A New Cap-Binding Complex That Activates mRNA Translation." *Front Physiol*.
3. **PMID:30698749** -- Bunay J et al. (2019). "Combined proteomic and miRNome analyses of mouse testis exposed to an endocrine disruptors chemicals mixture reveals altered toxicological pathways involved in male infertility." *Mol Hum Reprod*.

**Assessment:** RTRAF is very poorly studied (3 strict publications). It is part of a cap-binding complex that activates mRNA translation. Also involved in RNA transport and Pol II transcription modulation.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9Y224-F1, version 6
- **mean pLDDT: 71.6** (>90: 0.0%, 70-90: 65.2%, 50-70: 25.8%, <50: 9.0%)
- **Assessment:** Moderate confidence. No residues above pLDDT 90. Most residues in 70-90 range.

### Experimental PDB Structures
- **1 structure:** 7P3A (X-ray, 2.00A, residues 2-101 only)
- **Assessment:** Only N-terminal domain solved. C-terminal domain (102-244) not covered.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING
- **Status:** HTTP Error 502 -- STRING unavailable.

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| CALM1 | Affinity chrom. | 16512683 | Calmodulin |
| DISC1 | 2H | 17043677 | Neurodevelopmental |
| NIN | 2H | 15147888 | Centrosomal |
| GABARAPL2 | Co-IP | 20562859 | Autophagy |
| CUL5 | TAP | 21145461 | Cullin E3 ligase |
| KCNMA1 | Co-IP | 22174833 | Potassium channel |

### PPI Network Assessment
- Mixed network with diverse partners.
- CUL5 (cullin E3 ubiquitin ligase) is interesting for protein degradation pathways.
- No focused chromatin or transcriptional regulatory network.
- Multiple viral protein interactions (NSS, NS1 influenza) -- RTRAF is involved in viral replication.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RTRAF was likely rejected due to very low publication count and limited structural/regulatory data.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. HPA nucleoplasm (Supported). UniProt experimental nucleus x2.
2. **Functional context:** RNA-binding protein. Involved in mRNA transcription modulation by Pol II. tRNA splicing ligase complex. Cap-binding complex for mRNA translation.
3. **PubMed:** 3 strict. EXTREMELY LOW.
4. **Structure:** Partial PDB coverage (N-term only). Moderate AF confidence.
5. **PPI:** Mixed, diverse network. CUL5 (ubiquitin ligase) is interesting.

### Verdict
**The original rejection was INCORRECT.** RTRAF has valid nuclear localization (HPA Supported nucleoplasm), functions in mRNA transcription modulation and RNA transport, and has extremely high novelty (PubMed=3). While its functional profile is more RNA-processing than direct chromatin regulation, the Pol II transcription modulation role and very low prior investigation warrant retention for further evaluation.

---

## TE-Regulator Relevance

LOW-MODERATE. RTRAF modulates mRNA transcription by RNA Polymerase II, which is the polymerase responsible for TE transcription. As an RNA-binding protein involved in transcription and RNA transport, it could influence TE transcript processing. However, no direct connection to TE silencing or chromatin modification exists. The cap-binding complex function suggests a role in translation activation, potentially relevant for TE mRNA fate.

---

## Final Decision: RETAINED

Score: 89/180. RTRAF has good nuclear evidence (nucleoplasm, Supported), transcription modulation function, and extremely high novelty (PubMed=3). The score is lower due to limited regulatory domain function and weak structural data, but the novelty and nuclear localization warrant retention for further evaluation.

---

## Manual Review Note
BORDERLINE CANDIDATE. RTRAF (C14orf166) is a poorly characterized RNA-binding protein with roles in Pol II transcription modulation, tRNA splicing, and cap-binding complex activity. The very low PubMed count (3 strict) indicates high novelty but also limited functional characterization. The protein is clearly nuclear (HPA Supported + UniProt experimental), but its regulatory function is indirect (RNA processing/transport rather than chromatin-level). Retained primarily for novelty and nuclear localization. May be downgraded upon further review.
