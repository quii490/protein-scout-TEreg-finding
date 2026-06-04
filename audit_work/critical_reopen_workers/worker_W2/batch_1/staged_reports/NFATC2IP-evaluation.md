# NFATC2IP – Critical False-Rejection Reevaluation Report

**Gene:** NFATC2IP
**UniProt Accession:** Q8NCF5
**Protein Name:** NFATC2-interacting protein
**Length:** 419 aa | **Mass:** 45.8 kDa
**Aliases:** NIP45
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 12 | HPA: Nucleoplasm (Approved). UniProt: Nucleus. |
| 2. Protein Size | 10 | 7 | 419 aa / 45.8 kDa – larger protein, still tractable but requires more resources. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 15. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 13 | AlphaFold mean pLDDT: 65.2. PDB: 3 experimental structures. |
| 5. Regulatory Domains | 50 | 30 | InterPro: IPR052324, IPR022617, IPR000626. Function summary: In T-helper 2 (Th2) cells, regulates the magnitude of NFAT-driven transcription of a specific subset of cytokine genes, including IL3, IL4, IL5 and IL13, but not IL2. Recruits PRMT1 to the IL4 promote... |
| 6. PPI Network | 50 | 9 | STRING: 0 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **81** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **IF Image Status:** no_image_detected
- **Nuclear-relevant locations:** Nucleoplasm

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000250
- **Cytoplasm** – Evidence: ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0005737 (cytoplasm)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
- In T-helper 2 (Th2) cells, regulates the magnitude of NFAT-driven transcription of a specific subset of cytokine genes, including IL3, IL4, IL5 and IL13, but not IL2. Recruits PRMT1 to the IL4 promoter; this leads to enhancement of histone H4 'Arg-3'-methylation and facilitates subsequent histone acetylation at the IL4 locus, thus promotes robust cytokine expression (By similarity). Down-regulates formation of poly-SUMO chains by UBE2I/UBC9 (By similarity)

**Summary:** NFATC2IP has limited nuclear evidence (HPA: Approved reliability; UniProt experimental nuclear evidence). Nuclear score: 12/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 15 | `"NFATC2IP"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] ...` |
| Symbol Only (Title/Abstract) | 17 | |
| Broad (All Fields) | 31 | |

**Alias Note:** Aliases observed but not used for scoring: NIP45

### Key Papers (with PMIDs)
1. **PMID:38503515** – Cho T, Hoeg L, Setiaputra D (2024 Apr 17). "NFATC2IP is a mediator of SUMO-dependent genome integrity." *Genes & development.*
2. **PMID:38982223** – Qiang J, Yu S, Li J (2024 Dec 20). "Single-cell landscape of alternative polyadenylation in human lymphoid hematopoiesis." *Journal of molecular cell biology.*
3. **PMID:38894694** – Zhao L, Qian X, Ren Z (2024 Jun). "miR-31-5p suppresses myocardial hypertrophy by targeting Nfatc2ip." *Journal of cellular and molecular medicine.*
4. **PMID:35901591** – Huang T, Gu W, Liu E (2022 Sep 1). "miR-301b-5p and its target gene nfatc2ip regulate inflammatory responses in the liver of rainbow trout (Oncorhynchus mykiss) under high temperature stress." *Ecotoxicology and environmental safety.*
5. **PMID:37630855** – Qi L, Heianza Y, Li X (2023 Aug 21). "Toward Precision Weight-Loss Dietary Interventions: Findings from the POUNDS Lost Trial." *Nutrients.*

### Literature Assessment
- **Total publications:** Low (15 strict, 31 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8NCF5-F1, version 6
- **Mean pLDDT:** 65.2
- **pLDDT Distribution:**
  - >90 (very high confidence): 23.9%
  - 70-90 (confident): 16.5%
  - 50-70 (low confidence): 21.0%
  - <50 (very low confidence): 38.7%
- **Assessment:** Moderate-to-low confidence. Significant predicted disorder. The protein likely has intrinsically disordered regions.

### Experimental PDB Structures
- **2JXX** – NMR, -, chains: A=342-419
- **2L76** – NMR, -, chains: A=244-338
- **3RD2** – X-ray, 1.60 A, chains: A=345-419

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 13/30

---

## PPI Network

### STRING (Functional Partners)
- No STRING data available.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 | psi-mi:"MI:0914"(association) |
| RPL26 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | psi-mi:"MI:0915"(physical association) |
| NMNAT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| DNAL4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| C22orf39 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| CCDC157 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| P4HA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| EIF4G3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 9/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NFATC2IP was likely auto-rejected due to:
- Low AlphaFold pLDDT (mean 65.2)
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – STRONG, reliability: Approved.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** Nuclear GO annotations present but may rely on non-IDA evidence codes.
4. **PubMed Count:** 15 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection appears TECHNICALLY CORRECT.** Nuclear evidence is WEAK or AMBIGUOUS. However, the specific functional profile may still warrant consideration.

---

## TE-Regulator Relevance Reasoning

1. **Histone Modification:** NFATC2IP functions in histone acetylation/methylation, which directly regulates chromatin accessibility at TE loci. Histone modifications are primary mechanisms of TE silencing and activation.
2. **Transcriptional Regulation:** NFATC2IP has transcriptional regulatory functions. Many TEs contain promoter elements that are regulated by host transcription factors. NFATC2IP could directly or indirectly affect TE transcription.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE interest candidate. Nuclear evidence is present but the connection to TE biology is indirect. The protein is worth retaining for secondary investigation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 81/180**

**Reasoning:** NFATC2IP was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (15 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NFATC2IP nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NFATC2IP binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NFATC2IP expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NFATC2IP loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NFATC2IP encodes NFATC2-interacting protein, a 419-amino acid 45.8 kDa protein. 
HPA localizes NFATC2IP to Nucleoplasm (Approved reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: In T-helper 2 (Th2) cells, regulates the magnitude of NFAT-driven transcription of a specific subset of cytokine genes, including IL3, IL4, IL5 and IL13, but not IL2. Recruits PRMT1 to the IL4 promote. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
NFATC2IP should be reevaluated in the context of broader TE biology hypotheses.
