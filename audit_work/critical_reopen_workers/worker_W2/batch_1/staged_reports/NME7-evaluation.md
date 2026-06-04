# NME7 – Critical False-Rejection Reevaluation Report

**Gene:** NME7
**UniProt Accession:** Q9Y5B8
**Protein Name:** Nucleoside diphosphate kinase 7
**Length:** 376 aa | **Mass:** 42.5 kDa
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA: Nucleoplasm, Cytosol (Supported). UniProt: Nucleus. GO-CC: 2 IDA nuclear anno. |
| 2. Protein Size | 10 | 9 | 376 aa / 42.5 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 7 | PubMed strict: 32. Moderately low literature. Good novelty. |
| 4. 3D Structure | 30 | 27 | AlphaFold mean pLDDT: 93.2. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 9 | InterPro: IPR006602, IPR057579, IPR034907. Function summary: Possesses an intrinsic kinase activity (PubMed:24807905, PubMed:34764205). Phosphorylates GSK3B at 'Ser-9', leading to the activation of Wnt/beta-catenin signaling (PubMed:34764205). Additionally, exh... |
| 6. PPI Network | 50 | 22 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **96** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional Locations:** Cytosol
- **IF Image Status:** no_image_detected
- **Nuclear-relevant locations:** Nucleoplasm, Cytosol

### UniProt Subcellular Location
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome** – Evidence: ECO:0000269, ECO:0000269, ECO:0000269
- **Nucleus** – Evidence: ECO:0000269, ECO:0000305
- **Cytoplasm** – Evidence: ECO:0000269
- **Cytoplasm, cytoskeleton, spindle** – Evidence: ECO:0000269
- **Cytoplasm, cytoskeleton, cilium axoneme** – Evidence: ECO:0000269, ECO:0000269
- **Cytoplasm, cytoskeleton, flagellum axoneme** – Evidence: ECO:0000250
- **Cell projection, cilium** – Evidence: ECO:0000269, ECO:0000269
- **Cytoplasm, cytoskeleton, cilium basal body** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0160111 (axonemal A tubule inner sheath)** – Evidence: ISS:UniProtKB
- **GO:0005879 (axonemal microtubule)** – Evidence: IDA:UniProtKB
- **GO:0005813 (centrosome)** – Evidence: IDA:UniProtKB
- **GO:0036064 (ciliary basal body)** – Evidence: IDA:UniProtKB
- **GO:0005929 (cilium)** – Evidence: IDA:UniProtKB
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0005576 (extracellular region)** – Evidence: IEA:GOC
- **GO:0000931 (gamma-tubulin ring complex)** – Evidence: IDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0005886 (plasma membrane)** – Evidence: IEA:GOC
- **GO:0036126 (sperm flagellum)** – Evidence: ISS:UniProtKB
- **GO:0005819 (spindle)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
- Possesses an intrinsic kinase activity (PubMed:24807905, PubMed:34764205). Phosphorylates GSK3B at 'Ser-9', leading to the activation of Wnt/beta-catenin signaling (PubMed:34764205). Additionally, exhibits a 3'-5'-DNA exonuclease activity that removes single nucleotides from the 3' terminus of single-stranded DNA substrates and digests overhanging mismatched 3' termini from double-stranded DNA substrates, possibly participating in DNA nucleolytic processing (PubMed:16313181). In vitro, does n...

**Summary:** NME7 has strong nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence; GO: 2 IDA nuclear annotations). Nuclear score: 22/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 32 | `"NME7"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 45 | |
| Broad (All Fields) | 47 | |


### Key Papers (with PMIDs)
1. **PMID:29058704** – Puts GS, Leonard MK, Pamidimukkala NV (2018 Feb). "Nuclear functions of NME proteins." *Laboratory investigation; a journal of technical methods and pathology.*
2. **PMID:36533556** – Wang J, Thomas HR, Thompson RG (2022 Dec 1). "Variable phenotypes and penetrance between and within different zebrafish ciliary transition zone mutants." *Disease models & mechanisms.*
3. **PMID:25597950** – Garcia-Esparcia P, Hernández-Ortega K, Ansoleaga B (2015 Dec). "Purine metabolism gene deregulation in Parkinson's disease." *Neuropathology and applied neurobiology.*
4. **PMID:34764205** – Ren X, Rong Z, Liu X (2022 Jan 1). "The Protein Kinase Activity of NME7 Activates Wnt/β-Catenin Signaling to Promote One-Carbon Metabolism in Hepatocellular Carcinoma." *Cancer research.*
5. **PMID:27060491** – Reish O, Aspit L, Zouella A (2016 Aug). "A Homozygous Nme7 Mutation Is Associated with Situs Inversus Totalis." *Human mutation.*

### Literature Assessment
- **Total publications:** Low (32 strict, 47 broad).
- **Novelty score:** 7/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9Y5B8-F1, version 6
- **Mean pLDDT:** 93.2
- **pLDDT Distribution:**
  - >90 (very high confidence): 80.1%
  - 70-90 (confident): 17.8%
  - 50-70 (low confidence): 1.3%
  - <50 (very low confidence): 0.8%
- **Assessment:** High-confidence structure. Most of the protein is predicted with high confidence, suitable for structural studies.

### Experimental PDB Structures
- **7UNG** – EM, 3.60 A, chains: 5/6=1-376
- **8J07** – EM, 4.10 A, chains: 4O/4P/4Q/4R=1-376

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 27/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| MZT1 | 0.988 | 0.786 | 0.734 | |
| TUBGCP5 | 0.987 | 0.829 | 0.661 | |
| TUBGCP4 | 0.975 | 0.627 | 0.688 | |
| NEDD1 | 0.964 | 0.478 | 0.678 | |
| MZT2B | 0.963 | 0.626 | 0.542 | |
| ITPA | 0.960 | 0.053 | 0.323 | |
| AK9 | 0.952 | 0.000 | 0.395 | |
| NTPCR | 0.948 | 0.000 | 0.195 | |
| HDDC3 | 0.946 | 0.000 | 0.182 | |
| DTYMK | 0.944 | 0.000 | 0.271 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| KRT18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| ZNF263 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| NT5C2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| TCHP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| FKBP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| TNIP1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| TUFT1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| DDX1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 22/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NME7 was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269', 'ECO:0000305']).
3. **GO-CC Evidence:** 2 IDA-level nuclear annotations present: nucleoplasm, nucleus.
4. **PubMed Count:** 32 strict – within acceptable range.

### Verdict on False Rejection
**The original rejection was FALSE – NME7 should NOT have been rejected.** The nuclear evidence is ROBUST (HPA + UniProt experimental + GO IDA). The automated system may have undervalued the nuclear localization, been confused by dual localization patterns, or applied overly conservative scoring.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

1. **Indirect Relevance:** NME7's nuclear localization and functional profile suggest a structural or metabolic role without direct transcriptional/chromatin functions. TE relevance would be INDIRECT at best, possibly through general nuclear organization or cellular metabolism affecting TE expression states.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE-HIGH interest candidate. Nuclear evidence is robust and literature is limited, offering good novelty. The protein's functional roles in the nucleus provide mechanistic hypotheses for TE regulation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 96/180**

**Reasoning:** NME7 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (32 strict) is within acceptable range. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NME7 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NME7 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NME7 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NME7 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NME7 encodes Nucleoside diphosphate kinase 7, a 376-amino acid 42.5 kDa protein. 
HPA localizes NME7 to Nucleoplasm (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Possesses an intrinsic kinase activity (PubMed:24807905, PubMed:34764205). Phosphorylates GSK3B at 'Ser-9', leading to the activation of Wnt/beta-catenin signaling (PubMed:34764205). Additionally, exh. 
The false rejection appears to have resulted from automated scoring that failed to adequately weight the nuclear evidence. 
With only 32 publications, NME7 represents a highly novel target. 
The nuclear localization and functional profile make it a strong candidate for TE-regulatory investigation.
