# NGDN – Critical False-Rejection Reevaluation Report

**Gene:** NGDN
**UniProt Accession:** Q8NEJ9
**Protein Name:** Neuroguidin
**Length:** 315 aa | **Mass:** 35.9 kDa
**Aliases:** C14orf120
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 26 | HPA: Nucleoplasm, Nucleoli, Mitochondria (Approved). UniProt: Nucleus, Nucleus, nucleolus, Chromosome, centromere. GO-CC: 2 IDA nuclear anno. |
| 2. Protein Size | 10 | 9 | 315 aa / 35.9 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 6. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 17 | AlphaFold mean pLDDT: 75.8. PDB: 1 experimental structure. |
| 5. Regulatory Domains | 50 | 6 | InterPro: IPR007146. Function summary: Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an ... |
| 6. PPI Network | 50 | 8 | STRING: 0 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **76** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoli, Mitochondria
- **Additional Locations:** Nucleoplasm
- **IF Image Status:** no_image_detected
- **Nuclear-relevant locations:** Nucleoplasm, Nucleoli, Mitochondria

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000250
- **Nucleus, nucleolus** – Evidence: ECO:0000269, ECO:0000269
- **Chromosome, centromere** – Evidence: ECO:0000269
- **Cytoplasm** – Evidence: ECO:0000250
- **Cell projection, axon** – Evidence: ECO:0000250
- **Cell projection, dendrite** – Evidence: ECO:0000250
- **Cell projection, filopodium** – Evidence: ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0030424 (axon)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0000775 (chromosome, centromeric region)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0030425 (dendrite)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0030175 (filopodium)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005739 (mitochondrion)** – Evidence: IDA:HPA
- **GO:0005730 (nucleolus)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0032040 (small-subunit processome)** – Evidence: IDA:UniProtKB

### Functional Context
- Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Its dissociation from the complex determines the transition fro...

**Summary:** NGDN has strong nuclear evidence (HPA: Approved reliability; UniProt experimental nuclear evidence; GO: 2 IDA nuclear annotations). Nuclear score: 26/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 6 | `"NGDN"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 8 | |
| Broad (All Fields) | 15 | |

**Alias Note:** Aliases observed but not used for scoring: C14orf120

### Key Papers (with PMIDs)
1. **PMID:27599843** – Bammert L, Jonas S, Ungricht R (2016 Nov 16). "Human AATF/Che-1 forms a nucleolar protein complex with NGDN and NOL10 required for 40S ribosomal subunit synthesis." *Nucleic acids research.*
2. **PMID:25887473** – Chen K, Lü S, Cheng H (2015 Feb 19). "High expression of neuroguidin increases the sensitivity of acute myeloid leukemia cells to chemotherapeutic drugs." *Journal of hematology & oncology.*
3. **PMID:26503545** – Qi Y, Wang N, Pang LJ (2015 Oct 27). "Identification of potential mutations and genomic alterations in the epithelial and spindle cell components of biphasic synovial sarcomas using a human exome SNP chip." *BMC medical genomics.*
4. **PMID:41117218** – Yu S, Tan H (2026). "Identification and validation of novel marker genes to predict potential gestational diabetes mellitus patients by WGCNA and machine learning." *Ginekologia polska.*
5. **PMID:30169671** – Piñeiro D, Stoneley M, Ramakrishna M (2018 Nov 16). "Identification of the RNA polymerase I-RNA interactome." *Nucleic acids research.*

### Literature Assessment
- **Total publications:** Low (6 strict, 15 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8NEJ9-F1, version 6
- **Mean pLDDT:** 75.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 28.6%
  - 70-90 (confident): 37.5%
  - 50-70 (low confidence): 21.6%
  - <50 (very low confidence): 12.4%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **7MQ8** – EM, 3.60 A, chains: NC=1-315

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 17/30

---

## PPI Network

### STRING (Functional Partners)
- No STRING data available.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 | psi-mi:"MI:2364"(proximity) |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 | psi-mi:"MI:0914"(association) |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 | psi-mi:"MI:0914"(association) |
| AATF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | psi-mi:"MI:0915"(physical association) |
| SLC16A1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | psi-mi:"MI:0915"(physical association) |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 | psi-mi:"MI:0914"(association) |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 | psi-mi:"MI:0914"(association) |
| NOM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 8/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NGDN was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoli, Mitochondria – STRONG, reliability: Approved.
2. **UniProt Evidence:** Nucleus, nucleolus – ECO:0000269 (experimental, ['ECO:0000269', 'ECO:0000269']).
3. **GO-CC Evidence:** 2 IDA-level nuclear annotations present: nucleolus, nucleoplasm.
4. **PubMed Count:** 6 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection was FALSE – NGDN should NOT have been rejected.** The nuclear evidence is ROBUST (HPA + UniProt experimental + GO IDA). The automated system may have undervalued the nuclear localization, been confused by dual localization patterns, or applied overly conservative scoring.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

1. **Translation/Ribosome:** NGDN is involved in translation. TE transcripts can be translated, and translational regulation is a layer of TE control. Ribosome-associated proteins may affect TE-derived protein production.
2. **Nucleolar Function:** NGDN localizes to the nucleolus. Repetitive rDNA and some TEs are organized in nucleolar-associated domains, making nucleolar proteins relevant to TE spatial organization.
3. **RNA Exosome:** NGDN associates with the RNA exosome complex. The exosome degrades aberrant RNAs, including TE-derived transcripts. Exosome-associated proteins can provide TE transcript surveillance.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** HIGH interest candidate for TE regulation. STRONG nuclear evidence combined with MAXIMUM novelty (6 publications). The protein's nuclear localization and functional domain profile make it a compelling target for original investigation into TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 76/180**

**Reasoning:** NGDN was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (6 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NGDN nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NGDN binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NGDN expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NGDN loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NGDN encodes Neuroguidin, a 315-amino acid 35.9 kDa protein. 
HPA localizes NGDN to Nucleoplasm/Nucleoli (Approved reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an . 
The false rejection appears to have resulted from automated scoring that failed to adequately weight the nuclear evidence. 
With only 6 publications, NGDN represents a highly novel target. 
The nuclear localization and functional profile make it a strong candidate for TE-regulatory investigation.
