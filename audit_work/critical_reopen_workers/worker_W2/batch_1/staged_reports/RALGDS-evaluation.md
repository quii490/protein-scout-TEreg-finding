# RALGDS – Critical False-Rejection Reevaluation Report

**Gene:** RALGDS
**UniProt Accession:** Q12967
**Protein Name:** Ral guanine nucleotide dissociation stimulator
**Length:** 914 aa | **Mass:** 100.6 kDa
**Aliases:** KIAA1308, RGF
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 8 | HPA: Nucleoplasm (Uncertain). UniProt: Nucleus. GO-CC: 1 IDA nuclear anno. |
| 2. Protein Size | 10 | 3 | 914 aa / 100.6 kDa – very large protein. Significant resource commitment for full characterization. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 218 (>100 threshold). Well-studied, REJECTED per pipeline rule. |
| 4. 3D Structure | 30 | 13 | AlphaFold mean pLDDT: 63.0. PDB: 4 experimental structures. |
| 5. Regulatory Domains | 50 | 14 | InterPro: IPR000159, IPR015758, IPR008937. Function summary: Functions as a guanine nucleotide exchange factor (GEF) activating either RalA or RalB GTPases and plays an important role in intracellular transport. Interacts and acts as an effector molecule for R-... |
| 6. PPI Network | 50 | 26 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **64** | |

**NOTE: PubMed>100 (strict=218) triggers automatic REJECTION rule. Score shown for completeness but gene is automatically REJECTED per pipeline rules.**

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Uncertain
- **Main Location:** Nucleoplasm
- **IF Image Status:** no_image_detected
- **Nuclear-relevant locations:** Nucleoplasm

### UniProt Subcellular Location
- **Cytoplasm** – Evidence: ECO:0000250
- **Nucleus** – Evidence: ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0005903 (brush border)** – Evidence: IDA:UniProtKB
- **GO:0005829 (cytosol)** – Evidence: IDA:UniProtKB
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0005886 (plasma membrane)** – Evidence: IBA:GO_Central

### Functional Context
- Functions as a guanine nucleotide exchange factor (GEF) activating either RalA or RalB GTPases and plays an important role in intracellular transport. Interacts and acts as an effector molecule for R-Ras, H-Ras, K-Ras, and Rap (By similarity). During bacterial clearance, recognizes 'Lys-33'-linked polyubiquitinated TRAF3 and subsequently mediates assembly of the exocyst complex (PubMed:27438768)

**Summary:** RALGDS has limited nuclear evidence (HPA: Uncertain reliability; UniProt experimental nuclear evidence; GO: 1 IDA nuclear annotations). Nuclear score: 8/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 218 | `"RALGDS"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR...` |
| Symbol Only (Title/Abstract) | 283 | |
| Broad (All Fields) | 283 | |

**Alias Note:** Aliases observed but not used for scoring: KIAA1308, RGF

**REJECTION TRIGGERED: PubMed strict > 100 (218).**

### Key Papers (with PMIDs)
1. **PMID:18540861** – Ferro E, Magrini D, Guazzi P (2008 Oct 1). "G-protein binding features and regulation of the RalGDS family member, RGL2." *The Biochemical journal.*
2. **PMID:11455956** – Zheng Q, Yu L, Zhao Y (2000). "Structure characterization of human RalGDS gene, and the identification of its novel variant." *Molecular biology reports.*
3. **PMID:29524560** – Khan AQ, Kuttikrishnan S, Siveen KS (2019 Feb). "RAS-mediated oncogenic signaling pathways in human malignancies." *Seminars in cancer biology.*
4. **PMID:9365783** – Humphrey D, Kwiatkowska J, Henske EP (1997 Jul). "Cloning and evaluation of RALGDS as a candidate for the tuberous sclerosis gene TSC1." *Annals of human genetics.*
5. **PMID:8710374** – Wolthuis RM, Bauer B, van 't Veer LJ (1996 Jul 18). "RalGDS-like factor (Rlf) is a novel Ras and Rap 1A-associating protein." *Oncogene.*

### Literature Assessment
- **Total publications:** High (218 strict, 283 broad).
- **Novelty score:** 0/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q12967-F1, version 6
- **Mean pLDDT:** 63.0
- **pLDDT Distribution:**
  - >90 (very high confidence): 23.7%
  - 70-90 (confident): 24.7%
  - 50-70 (low confidence): 7.5%
  - <50 (very low confidence): 44.0%
- **Assessment:** Moderate-to-low confidence. Significant predicted disorder. The protein likely has intrinsically disordered regions.

### Experimental PDB Structures
- **1RAX** – NMR, -, chains: A=775-886
- **2B3A** – NMR, -, chains: A=798-884
- **2RGF** – NMR, -, chains: A=788-884
- **3KH0** – X-ray, 2.10 A, chains: A/B=793-914

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 13/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| KRAS | 0.999 | 0.716 | 0.980 | |
| RALA | 0.999 | 0.302 | 0.988 | |
| RRAS | 0.999 | 0.435 | 0.985 | |
| RAP1A | 0.999 | 0.757 | 0.978 | |
| HRAS | 0.999 | 0.989 | 0.919 | |
| RALB | 0.996 | 0.302 | 0.952 | |
| LRPAP1 | 0.996 | 0.230 | 0.996 | |
| NRAS | 0.988 | 0.302 | 0.846 | |
| RAP1B | 0.987 | 0.697 | 0.614 | |
| MRAS | 0.986 | 0.580 | 0.705 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| Rit2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 | psi-mi:"MI:0915"(physical association) |
| RIT1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10545207 | psi-mi:"MI:0915"(physical association) |
| Oog1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16580637|imex:IM-19876 | psi-mi:"MI:0915"(physical association) |
| HRAS | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:9628477 | psi-mi:"MI:0407"(direct interaction) |
| RAP1B | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| RRAS2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| KRAS | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| CD68 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Moderate interaction network.**
- **Score:** 26/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RALGDS was likely auto-rejected due to:
- PubMed>100 (strict=218)
- Low AlphaFold pLDDT (mean 63.0)
- Dual cytoplasm/nucleus localization may have caused ambiguity
- Large protein size (914 aa)

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – PRESENT, reliability: Uncertain.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** 1 IDA-level nuclear annotations present: nucleus.
4. **PubMed Count:** 218 strict – EXCEEDS 100 threshold. This likely triggered automatic rejection.

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=218) rule.** The gene exceeds the PubMed publication threshold for automatic rejection. However, the nuclear evidence is robust (SCIENCE EVIDENCE: HPA + UniProt experimental + GO IDA annotations), and functional assessment below evaluates whether an exception is warranted.

---

## TE-Regulator Relevance Reasoning

1. **Ubiquitination:** RALGDS has ubiquitin-related functions. Ubiquitination regulates histone stability, transcription factor turnover, and chromatin protein degradation, all of which affect TE silencing.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** LOW interest candidate for TE regulation. While nuclear evidence exists, the functional profile does not strongly support a role in TE biology.

---

## Final Decision

**DECISION: REJECTED (PubMed>100 rule)**

**Score: 64/180**

**Reasoning:** RALGDS exceeds the PubMed>100 rejection threshold (218 publications). While nuclear and functional evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules. If exception criteria exist, this gene should be considered for waiver review based on its functional profile.

**If exception is granted:**
1. Screen RALGDS for TE-regulatory functions despite high literature volume.
2. Focus on TE-specific aspects not covered in existing publications.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

RALGDS encodes Ral guanine nucleotide dissociation stimulator, a 914-amino acid 100.6 kDa protein. 
HPA localizes RALGDS to Nucleoplasm (Uncertain reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Functions as a guanine nucleotide exchange factor (GEF) activating either RalA or RalB GTPases and plays an important role in intracellular transport. Interacts and acts as an effector molecule for R-. 
However, with 218 strict PubMed publications, RALGDS exceeds the pipeline's 100-publication rejection threshold. 
The extensive literature may contain unexplored TE-relevant functions, particularly given RALGDS's nuclear localization and functional roles. 
Recommend tracking RALGDS as a 'high priority rejected – exception review needed' case.
