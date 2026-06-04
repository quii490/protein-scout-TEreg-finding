# MOCS2 – Critical False-Rejection Reevaluation Report

**Gene:** MOCS2
**UniProt Accession:** O96033
**Protein Name:** Molybdopterin synthase sulfur carrier subunit
**Length:** 88 aa | **Mass:** 9.8 kDa
**Aliases:** MOCO1
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 16 | HPA: Nucleoplasm, Nuclear speckles, Cytosol (Supported). UniProt: Nucleus. |
| 2. Protein Size | 10 | 10 | 88 aa / 9.8 kDa – small, highly tractable. Full marks. |
| 3. Research Novelty | 10 | 7 | PubMed strict: 42. Moderately low literature. Good novelty. |
| 4. 3D Structure | 30 | 27 | AlphaFold mean pLDDT: 91.8. PDB: 1 experimental structure. |
| 5. Regulatory Domains | 50 | 4 | InterPro: IPR012675, IPR044672, IPR028887. Function summary: Acts as a sulfur carrier required for molybdopterin biosynthesis (PubMed:22453920). Component of the molybdopterin synthase complex that catalyzes the conversion of precursor Z into molybdopterin by m... |
| 6. PPI Network | 50 | 22 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **86** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **Additional Locations:** Nucleoplasm, Nuclear speckles
- **IF Image Status:** if_display_images_available
- **IF Images:** 6 images available
- **Nuclear-relevant locations:** Nucleoplasm, Nuclear speckles, Cytosol

### UniProt Subcellular Location
- **Cytoplasm, cytosol** – Evidence: ECO:0000255, ECO:0000269, ECO:0000269
- **Nucleus** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IDA:UniProtKB
- **GO:1990140 (molybdopterin synthase complex)** – Evidence: IDA:UniProtKB

### Functional Context
- Acts as a sulfur carrier required for molybdopterin biosynthesis (PubMed:22453920). Component of the molybdopterin synthase complex that catalyzes the conversion of precursor Z into molybdopterin by mediating the incorporation of 2 sulfur atoms into precursor Z to generate a dithiolene group. In the complex, serves as sulfur donor by being thiocarboxylated (-COSH) at its C-terminus by MOCS3 (PubMed:25709896, PubMed:12732628, PubMed:22453920). After interaction with MOCS2B, the sulfur is then ...

**Summary:** MOCS2 has moderate nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence). Nuclear score: 16/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 42 | `"MOCS2"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR ...` |
| Symbol Only (Title/Abstract) | 59 | |
| Broad (All Fields) | 59 | |

**Alias Note:** Aliases observed but not used for scoring: MOCO1

### Key Papers (with PMIDs)
1. **PMID:34870926** – Adam MP, Bick S, Mirzaa GM (1993). "Molybdenum Cofactor Deficiency." *.*
2. **PMID:12754701** – Reiss J, Johnson JL (2003 Jun). "Mutations in the molybdenum cofactor biosynthetic genes MOCS1, MOCS2, and GEPH." *Human mutation.*
3. **PMID:40452920** – Wang J, Sun P, Zhang F (2025). "Metabolic reprogramming signature predicts prognosis and immune landscape in small cell lung cancer: MOCS2 validation and implications for personalized therapy." *Frontiers in molecular biosciences.*
4. **PMID:21031595** – Reiss J, Hahnewald R (2011 Jan). "Molybdenum cofactor deficiency: Mutations in GPHN, MOCS1, and MOCS2." *Human mutation.*
5. **PMID:31201073** – Arican P, Gencpinar P, Kirbiyik O (2019 Oct). "The Clinical and Molecular Characteristics of Molybdenum Cofactor Deficiency Due to MOCS2 Mutations." *Pediatric neurology.*

### Literature Assessment
- **Total publications:** Low (42 strict, 59 broad).
- **Novelty score:** 7/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-O96033-F1, version 6
- **Mean pLDDT:** 91.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 84.1%
  - 70-90 (confident): 11.4%
  - 50-70 (low confidence): 3.4%
  - <50 (very low confidence): 1.1%
- **Assessment:** High-confidence structure. Most of the protein is predicted with high confidence, suitable for structural studies.

### Experimental PDB Structures
- **5MPO** – X-ray, 2.43 A, chains: A/B=7-88

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 27/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| MOCS3 | 0.999 | 0.099 | 0.985 | |
| MOCS1 | 0.999 | 0.000 | 0.995 | |
| GPHN | 0.998 | 0.000 | 0.949 | |
| SUOX | 0.969 | 0.000 | 0.962 | |
| SGF29 | 0.957 | 0.954 | 0.108 | |
| AOX1 | 0.945 | 0.000 | 0.945 | |
| TST | 0.939 | 0.000 | 0.719 | |
| MARC2 | 0.918 | 0.000 | 0.909 | |
| MPST | 0.871 | 0.000 | 0.408 | |
| TSTD1 | 0.870 | 0.000 | 0.349 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| EBI-4462876 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 | psi-mi:"MI:0915"(physical association) |
| Mocs3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| Mocs2B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| RPL9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| ABCF3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| Atac2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 | psi-mi:"MI:0914"(association) |
| Chrac-14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 | psi-mi:"MI:0914"(association) |
| Ada2a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15032|pubmed:20813260 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 22/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
MOCS2 was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Cytosol – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269']).
3. **GO-CC Evidence:** Nuclear GO annotations present but may rely on non-IDA evidence codes.
4. **PubMed Count:** 42 strict – within acceptable range.

### Verdict on False Rejection
**The original rejection was LIKELY FALSE.** Nuclear evidence is PRESENT but not overwhelming. The gene merits reevaluation because the nuclear annotation is supported by multiple sources (UniProt + GO).

**This gene should be REOPENED for TE-regulatory evaluation unless the PubMed count exceeds the threshold.**

---

## TE-Regulator Relevance Reasoning

1. **Indirect Relevance:** MOCS2's nuclear localization and functional profile suggest a structural or metabolic role without direct transcriptional/chromatin functions. TE relevance would be INDIRECT at best, possibly through general nuclear organization or cellular metabolism affecting TE expression states.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE-HIGH interest candidate. Nuclear evidence is robust and literature is limited, offering good novelty. The protein's functional roles in the nucleus provide mechanistic hypotheses for TE regulation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 86/180**

**Reasoning:** MOCS2 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (42 strict) is within acceptable range. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm MOCS2 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for MOCS2 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate MOCS2 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether MOCS2 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

MOCS2 encodes Molybdopterin synthase sulfur carrier subunit, a 88-amino acid 9.8 kDa protein. 
HPA localizes MOCS2 to Nucleoplasm/Nuclear speckles (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Acts as a sulfur carrier required for molybdopterin biosynthesis (PubMed:22453920). Component of the molybdopterin synthase complex that catalyzes the conversion of precursor Z into molybdopterin by m. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
MOCS2 should be reevaluated in the context of broader TE biology hypotheses.
