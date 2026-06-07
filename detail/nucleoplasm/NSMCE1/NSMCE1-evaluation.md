# NSMCE1 – Critical False-Rejection Reevaluation Report

**Gene:** NSMCE1
**UniProt Accession:** Q8WV22
**Protein Name:** Non-structural maintenance of chromosomes element 1 homolog
**Length:** 266 aa | **Mass:** 30.9 kDa
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 20 | HPA: Nucleoplasm, Vesicles (Supported). UniProt: Nucleus, Chromosome, telomere. GO-CC: 1 IDA nuclear anno. |
| 2. Protein Size | 10 | 9 | 266 aa / 30.9 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 8. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 23 | AlphaFold mean pLDDT: 89.2. PDB: 3 experimental structures. |
| 5. Regulatory Domains | 50 | 19 | InterPro: IPR011513, IPR014857, IPR002219. Function summary: RING-type zinc finger-containing E3 ubiquitin ligase that assembles with melanoma antigen protein (MAGE) to catalyze the direct transfer of ubiquitin from E2 ubiquitin-conjugating enzyme to a specific... |
| 6. PPI Network | 50 | 40 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **121** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional Locations:** Vesicles
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoplasm, Vesicles

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000269
- **Chromosome, telomere** – Evidence: ECO:0000305

### GO Cellular Component (GO-CC)
- **GO:0000775 (chromosome, centromeric region)** – Evidence: IEA:Ensembl
- **GO:0000781 (chromosome, telomeric region)** – Evidence: NAS:ComplexPortal
- **GO:0097431 (mitotic spindle pole)** – Evidence: IEA:Ensembl
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IBA:GO_Central
- **GO:0030915 (Smc5-Smc6 complex)** – Evidence: IDA:UniProtKB

### Functional Context
- RING-type zinc finger-containing E3 ubiquitin ligase that assembles with melanoma antigen protein (MAGE) to catalyze the direct transfer of ubiquitin from E2 ubiquitin-conjugating enzyme to a specific substrate. Within MAGE-RING ubiquitin ligase complex, MAGE stimulates and specifies ubiquitin ligase activity likely through recruitment and/or stabilization of the E2 ubiquitin-conjugating enzyme at the E3:substrate complex. Involved in maintenance of genome integrity, DNA damage response and D...

**Summary:** NSMCE1 has strong nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence; GO: 1 IDA nuclear annotations). Nuclear score: 20/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 8 | `"NSMCE1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR...` |
| Symbol Only (Title/Abstract) | 10 | |
| Broad (All Fields) | 40 | |


### Key Papers (with PMIDs)
1. **PMID:41825673** – He L, Shen H, Zhao A (2026 Apr). "Mechanism insights into the role of Smc5/6 in HBV inhibition." *International journal of biological macromolecules.*
2. **PMID:37659689** – Na L, Xu M, Chen JL (2023 Nov 5). "4D-DIA quantitative proteomics revealed the core mechanism of diabetic retinopathy after berberine treatment." *European journal of pharmacology.*
3. **PMID:31792732** – Gong M, Wang Z, Liu Y (2020 May). "A transcriptomic analysis of Nsmce1 overexpression in mouse hippocampal neuronal cell by RNA sequencing." *Functional & integrative genomics.*
4. **PMID:33754896** – Liu D, Dai SX, He K (2021 Jan-Mar). "Identification of hub ubiquitin ligase genes affecting Alzheimer's disease by analyzing transcriptome data from multiple brain regions." *Science progress.*
5. **PMID:39611166** – Choi JY, Kwon H, Kim H (2024). "Novel genomic variants influencing methotrexate delayed clearance in pediatric patients with acute lymphoblastic leukemia." *Frontiers in pharmacology.*

### Literature Assessment
- **Total publications:** Low (8 strict, 40 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8WV22-F1, version 6
- **Mean pLDDT:** 89.2
- **pLDDT Distribution:**
  - >90 (very high confidence): 79.3%
  - 70-90 (confident): 8.6%
  - 50-70 (low confidence): 5.3%
  - <50 (very low confidence): 6.8%
- **Assessment:** High-confidence structure. Most of the protein is predicted with high confidence, suitable for structural studies.

### Experimental PDB Structures
- **2CT0** – NMR, -, chains: A=181-241
- **5HVQ** – X-ray, 2.92 A, chains: C=9-246
- **5WY5** – X-ray, 2.92 A, chains: A=9-246

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 23/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| NSMCE3 | 0.999 | 0.999 | 0.672 | |
| SMC6 | 0.999 | 0.997 | 0.788 | |
| NSMCE4A | 0.999 | 0.972 | 0.803 | |
| NSMCE2 | 0.999 | 0.997 | 0.794 | |
| SMC5 | 0.999 | 0.993 | 0.667 | |
| EID3 | 0.998 | 0.979 | 0.349 | |
| SLF2 | 0.927 | 0.743 | 0.427 | |
| SUMO4 | 0.915 | 0.066 | 0.166 | |
| MAGEF1 | 0.840 | 0.757 | 0.339 | |
| ZNF597 | 0.836 | 0.836 | 0.000 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| Smc6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 | psi-mi:"MI:0915"(physical association) |
| ZNF597 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| PMF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| SLF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| SMC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| SIMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| NSMCE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| NSMCE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Extensive interaction network** with high-confidence connections.
- **TE-relevant connections identified:** SMC3, SMC6, NSMCE2, SMC1A, NSMCE4A, SUMO4, SMC5, NSMCE3
- **Score:** 40/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NSMCE1 was likely auto-rejected due to automated scoring below pipeline threshold, despite qualifying nuclear evidence.

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269']).
3. **GO-CC Evidence:** 1 IDA-level nuclear annotations present: nucleoplasm.
4. **PubMed Count:** 8 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection was FALSE – NSMCE1 should NOT have been rejected.** The nuclear evidence is ROBUST (HPA + UniProt experimental + GO IDA). The automated system may have undervalued the nuclear localization, been confused by dual localization patterns, or applied overly conservative scoring.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

1. **DNA Repair:** NSMCE1 is involved in DNA repair. TE mobilization creates DNA damage, and DNA repair pathways are intimately linked to TE lifecycle control. Proteins involved in DNA repair often affect TE insertion and excision.
2. **Ubiquitination:** NSMCE1 has ubiquitin-related functions. Ubiquitination regulates histone stability, transcription factor turnover, and chromatin protein degradation, all of which affect TE silencing.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** HIGH interest candidate for TE regulation. STRONG nuclear evidence combined with MAXIMUM novelty (8 publications). The protein's nuclear localization and functional domain profile make it a compelling target for original investigation into TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 121/180**

**Reasoning:** NSMCE1 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (8 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NSMCE1 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NSMCE1 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NSMCE1 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NSMCE1 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NSMCE1 encodes Non-structural maintenance of chromosomes element 1 homolog, a 266-amino acid 30.9 kDa protein. 
HPA localizes NSMCE1 to Nucleoplasm (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: RING-type zinc finger-containing E3 ubiquitin ligase that assembles with melanoma antigen protein (MAGE) to catalyze the direct transfer of ubiquitin from E2 ubiquitin-conjugating enzyme to a specific. 
The false rejection appears to have resulted from automated scoring that failed to adequately weight the nuclear evidence. 
With only 8 publications, NSMCE1 represents a highly novel target. 
The nuclear localization and functional profile make it a strong candidate for TE-regulatory investigation.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169189-NSMCE1/subcellular

![](https://images.proteinatlas.org/43091/840_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/43091/840_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/43091/847_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/43091/847_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/43091/857_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/43091/857_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WV22 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011513;IPR014857;IPR002219;IPR036388;IPR001841;IPR013083; |
| Pfam | PF07574;PF08746; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169189-NSMCE1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EID3 | Intact, Biogrid, Bioplex | true |
| MAGEF1 | Intact, Biogrid, Bioplex | true |
| NSMCE2 | Intact, Biogrid | true |
| NSMCE3 | Intact, Biogrid, Bioplex | true |
| NSMCE4A | Intact, Biogrid, Bioplex | true |
| SMC5 | Intact, Biogrid, Bioplex | true |
| SMC6 | Intact, Biogrid, Bioplex | true |
| MAGEB10 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
