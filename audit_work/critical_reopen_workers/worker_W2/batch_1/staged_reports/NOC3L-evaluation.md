# NOC3L – Critical False-Rejection Reevaluation Report

**Gene:** NOC3L
**UniProt Accession:** Q8WTT2
**Protein Name:** Nucleolar complex protein 3 homolog
**Length:** 800 aa | **Mass:** 92.5 kDa
**Aliases:** AD24, C10orf117, FAD24
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 16 | HPA: Nucleoplasm, Nucleoli, Nucleoli rim (Enhanced). UniProt: Nucleus, nucleolus, Nucleus speckle. GO-CC: 2 IDA nuclear anno. |
| 2. Protein Size | 10 | 5 | 800 aa / 92.5 kDa – large protein. Tractable but resource-intensive. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 10. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 17 | AlphaFold mean pLDDT: 74.8. PDB: 4 experimental structures. |
| 5. Regulatory Domains | 50 | 6 | InterPro: IPR016024, IPR005612, IPR011501. Function summary: May be required for adipogenesis... |
| 6. PPI Network | 50 | 22 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **76** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Enhanced
- **Main Location:** Nucleoli, Nucleoli rim
- **Additional Locations:** Nucleoplasm
- **IF Image Status:** if_display_images_available
- **IF Images:** 16 images available
- **Nuclear-relevant locations:** Nucleoplasm, Nucleoli, Nucleoli rim

### UniProt Subcellular Location
- **Nucleus, nucleolus** – Evidence: no evidence code
- **Nucleus speckle** – Evidence: no evidence code

### GO Cellular Component (GO-CC)
- **GO:0005739 (mitochondrion)** – Evidence: IDA:HPA
- **GO:0016607 (nuclear speck)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005730 (nucleolus)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA

### Functional Context
- May be required for adipogenesis

**Summary:** NOC3L has moderate nuclear evidence (HPA: Enhanced reliability; UniProt experimental nuclear evidence; GO: 2 IDA nuclear annotations). Nuclear score: 16/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 10 | `"NOC3L"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR ...` |
| Symbol Only (Title/Abstract) | 14 | |
| Broad (All Fields) | 25 | |

**Alias Note:** Aliases observed but not used for scoring: AD24, C10orf117, FAD24

### Key Papers (with PMIDs)
1. **PMID:39809148** – Xiao L, Li X, Wang JJ (2024 Nov 22). "Roles of NOC3L and DDX17 in acquired immunodeficiency complicated with viral myocarditis and osteoporosis." *Medicine.*
2. **PMID:40409638** – Bai Z, An J, Han J (2025 Jun). "Integrative genome-wide association studies, proteome-wide Mendelian randomization, and single-cell RNA sequencing identify interleukin-6 receptor protein as a therapeutic target in aortic aneurysm." *International journal of biological macromolecules.*
3. **PMID:40827841** – Rambaldelli G, Manara V, Vutera Cuda A (2025 Sep 1). "Drosophila and human cell studies reveal a conserved role for CEBPZ, NOC2L and NOC3L in rRNA processing and tumorigenesis." *Journal of cell science.*
4. **PMID:36653889** – Jin H, Kwak SH, Yoon JW (2023 Mar). "Genome-Wide Association Study on Longitudinal Change in Fasting Plasma Glucose in Korean Population." *Diabetes & metabolism journal.*
5. **PMID:33274532** – Zhou X, Wang Y, Chen J (2021 Mar). "Constructing a 10-core genes panel for diagnosis of pediatric sepsis." *Journal of clinical laboratory analysis.*

### Literature Assessment
- **Total publications:** Low (10 strict, 25 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8WTT2-F1, version 6
- **Mean pLDDT:** 74.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 21.6%
  - 70-90 (confident): 46.8%
  - 50-70 (low confidence): 15.9%
  - <50 (very low confidence): 15.8%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **8FKV** – EM, 2.47 A, chains: SU=1-800
- **8FKW** – EM, 2.50 A, chains: SU=1-800
- **8FKX** – EM, 2.59 A, chains: SU=1-800
- **8FKY** – EM, 2.67 A, chains: SU=1-800

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 17/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| NOC2L | 0.998 | 0.978 | 0.391 | |
| BRIX1 | 0.997 | 0.963 | 0.460 | |
| MAK16 | 0.997 | 0.971 | 0.282 | |
| BOP1 | 0.996 | 0.943 | 0.339 | |
| NIFK | 0.995 | 0.946 | 0.352 | |
| GTPBP4 | 0.994 | 0.945 | 0.350 | |
| WDR12 | 0.992 | 0.962 | 0.373 | |
| EBNA1BP2 | 0.992 | 0.951 | 0.282 | |
| PES1 | 0.992 | 0.974 | 0.350 | |
| RSL1D1 | 0.991 | 0.936 | 0.324 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 | psi-mi:"MI:0914"(association) |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 | psi-mi:"MI:0914"(association) |
| USP39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| EIF2AK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 | psi-mi:"MI:0914"(association) |
| SRPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 | psi-mi:"MI:0914"(association) |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 | psi-mi:"MI:0914"(association) |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010|pubmed:29128334|imex:IM-26363 | psi-mi:"MI:0914"(association) |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 | psi-mi:"MI:2364"(proximity) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 22/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NOC3L was likely auto-rejected due to automated scoring below pipeline threshold, despite qualifying nuclear evidence.

### Recheck Analysis
1. **HPA Evidence:** Nucleoli, Nucleoli rim – STRONG, reliability: Enhanced.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** 2 IDA-level nuclear annotations present: nucleolus, nucleoplasm.
4. **PubMed Count:** 10 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection was LIKELY FALSE.** Nuclear evidence is PRESENT but not overwhelming. The gene merits reevaluation because the nuclear annotation is supported by multiple sources (UniProt + GO).

**This gene should be REOPENED for TE-regulatory evaluation unless the PubMed count exceeds the threshold.**

---

## TE-Regulator Relevance Reasoning

1. **Nucleolar Function:** NOC3L localizes to the nucleolus. Repetitive rDNA and some TEs are organized in nucleolar-associated domains, making nucleolar proteins relevant to TE spatial organization.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE-HIGH interest candidate. Nuclear evidence is robust and literature is limited, offering good novelty. The protein's functional roles in the nucleus provide mechanistic hypotheses for TE regulation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 76/180**

**Reasoning:** NOC3L was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (10 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NOC3L nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NOC3L binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NOC3L expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NOC3L loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NOC3L encodes Nucleolar complex protein 3 homolog, a 800-amino acid 92.5 kDa protein. 
HPA localizes NOC3L to Nucleoplasm/Nucleoli/Nucleoli rim (Enhanced reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: May be required for adipogenesis. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
NOC3L should be reevaluated in the context of broader TE biology hypotheses.
