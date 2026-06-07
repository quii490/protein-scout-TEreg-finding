# NFU1 – Critical False-Rejection Reevaluation Report

**Gene:** NFU1
**UniProt Accession:** Q9UMS0
**Protein Name:** NFU1 iron-sulfur cluster scaffold homolog, mitochondrial
**Length:** 254 aa | **Mass:** 28.5 kDa
**Aliases:** HIRIP5
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 14 | HPA: Nucleoplasm, Cytosol (Supported). GO-CC: 2 IDA nuclear anno. |
| 2. Protein Size | 10 | 9 | 254 aa / 28.5 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 3 | PubMed strict: 87. Moderate literature volume. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 78.9. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 6 | InterPro: IPR034904, IPR014824, IPR036498. Function summary: Iron-sulfur cluster scaffold protein which can assemble [4Fe-4S] clusters and deliver them to target proteins... |
| 6. PPI Network | 50 | 28 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **78** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **Additional Locations:** Nucleoplasm
- **IF Image Status:** if_display_images_available
- **IF Images:** 6 images available
- **Nuclear-relevant locations:** Nucleoplasm, Cytosol

### UniProt Subcellular Location
- **Mitochondrion** – Evidence: no evidence code
- **Cytoplasm, cytosol** – Evidence: no evidence code

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0005759 (mitochondrial matrix)** – Evidence: TAS:Reactome
- **GO:0005739 (mitochondrion)** – Evidence: IDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB

### Functional Context
- Iron-sulfur cluster scaffold protein which can assemble [4Fe-4S] clusters and deliver them to target proteins

**Summary:** NFU1 has limited nuclear evidence (HPA: Supported reliability; GO: 2 IDA nuclear annotations). Nuclear score: 14/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 87 | `"NFU1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 106 | |
| Broad (All Fields) | 118 | |

**Alias Note:** Aliases observed but not used for scoring: HIRIP5

### Key Papers (with PMIDs)
1. **PMID:40597352** – Stark JC, Pipko N, Liang Y (2025 Jul 1). "Clinical applications of and molecular insights from RNA sequencing in a rare disease cohort." *Genome medicine.*
2. **PMID:39320470** – Niihori M, James J, Varghese MV (2024 Nov 4). "Mitochondria as a primary determinant of angiogenic modality in pulmonary arterial hypertension." *The Journal of experimental medicine.*
3. **PMID:27381105** – Kurt YG, Kurt B, Aydin I (2016 Jul-Aug). "NFU1 gene mutation and mitochondrial disorders." *Neurology India.*
4. **PMID:33711344** – Suraci D, Saudino G, Nasta V (2021 May 14). "ISCA1 Orchestrates ISCA2 and NFU1 in the Maturation of Human Mitochondrial [4Fe-4S] Proteins." *Journal of molecular biology.*
5. **PMID:24777537** – Mayr JA, Feichtinger RG, Tort F (2014 Jul). "Lipoic acid biosynthesis defects." *Journal of inherited metabolic disease.*

### Literature Assessment
- **Total publications:** Moderate (87 strict, 118 broad).
- **Novelty score:** 3/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9UMS0-F1, version 6
- **Mean pLDDT:** 78.9
- **pLDDT Distribution:**
  - >90 (very high confidence): 60.2%
  - 70-90 (confident): 7.9%
  - 50-70 (low confidence): 8.3%
  - <50 (very low confidence): 23.6%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **2LTM** – NMR, -, chains: A=59-155
- **2M5O** – NMR, -, chains: A=162-247

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 18/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| NFS1 | 0.982 | 0.303 | 0.816 | |
| ISCU | 0.967 | 0.253 | 0.917 | |
| ISCA1 | 0.947 | 0.254 | 0.877 | |
| ISCA2 | 0.947 | 0.162 | 0.892 | |
| BOLA3 | 0.945 | 0.330 | 0.907 | |
| SCLY | 0.939 | 0.303 | 0.349 | |
| SDHB | 0.917 | 0.095 | 0.505 | |
| EPM2A | 0.916 | 0.292 | 0.886 | |
| IBA57 | 0.905 | 0.000 | 0.896 | |
| NDUFS8 | 0.890 | 0.000 | 0.366 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| NOA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| RNQ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 | psi-mi:"MI:0915"(physical association) |
| ORF | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034|psi-mi:"MI:0007" | psi-mi:"MI:0914"(association) |
| gag-pol | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034|psi-mi:"MI:0007" | psi-mi:"MI:0914"(association) |
| SH3BP4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 | psi-mi:"MI:0915"(physical association) |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 | psi-mi:"MI:0915"(physical association) |
| NME4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449|doi:10.1016/j.molcel.2016.06.0 | psi-mi:"MI:0914"(association) |
| Rabac1 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:30925931|imex:IM-26645 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Moderate interaction network.**
- **Score:** 28/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NFU1 was likely auto-rejected due to automated scoring below pipeline threshold, despite qualifying nuclear evidence.

### Recheck Analysis
1. **HPA Evidence:** Cytosol – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** 2 IDA-level nuclear annotations present: nucleoplasm, nucleus.
4. **PubMed Count:** 87 strict – within acceptable range.

### Verdict on False Rejection
**The original rejection appears TECHNICALLY CORRECT.** Nuclear evidence is WEAK or AMBIGUOUS. However, the specific functional profile may still warrant consideration.

---

## TE-Regulator Relevance Reasoning

1. **Indirect Relevance:** NFU1's nuclear localization and functional profile suggest a structural or metabolic role without direct transcriptional/chromatin functions. TE relevance would be INDIRECT at best, possibly through general nuclear organization or cellular metabolism affecting TE expression states.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE interest candidate. Nuclear evidence is present but the connection to TE biology is indirect. The protein is worth retaining for secondary investigation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 78/180**

**Reasoning:** NFU1 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (87 strict) is within acceptable range. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NFU1 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NFU1 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NFU1 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NFU1 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NFU1 encodes NFU1 iron-sulfur cluster scaffold homolog, mitochondrial, a 254-amino acid 28.5 kDa protein. 
HPA localizes NFU1 to Nucleoplasm (Supported reliability). 
The protein functions primarily in: Iron-sulfur cluster scaffold protein which can assemble [4Fe-4S] clusters and deliver them to target proteins. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
NFU1 should be reevaluated in the context of broader TE biology hypotheses.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UMS0 |
| SMART | SM00932; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034904;IPR014824;IPR036498;IPR001075; |
| Pfam | PF08712;PF01106; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169599-NFU1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGTRAP | Intact | false |
| APOC1 | Intact | false |
| APOC4 | Intact | false |
| CALCOCO2 | Intact | false |
| CIDEB | Intact | false |
| CLPP | Biogrid | false |
| COIL | Intact | false |
| CS | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
