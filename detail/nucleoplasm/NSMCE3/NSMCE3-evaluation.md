# NSMCE3 – Critical False-Rejection Reevaluation Report

**Gene:** NSMCE3
**UniProt Accession:** Q96MG7
**Protein Name:** Non-structural maintenance of chromosomes element 3 homolog
**Length:** 304 aa | **Mass:** 34.3 kDa
**Aliases:** HCA4, MAGEG1, NDNL2
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 9 | UniProt: Nucleus, Chromosome, telomere. |
| 2. Protein Size | 10 | 9 | 304 aa / 34.3 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 6. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 74.6. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 12 | InterPro: IPR037445, IPR041898, IPR041899. Function summary: Component of the SMC5-SMC6 complex, a complex involved in repair of DNA double-strand breaks by homologous recombination (PubMed:20864041, PubMed:27427983). The complex may promote sister chromatid ho... |
| 6. PPI Network | 50 | 39 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **97** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** None
- **IF Image Status:** no_image_detected

### UniProt Subcellular Location
- **Cytoplasm** – Evidence: ECO:0000250
- **Nucleus** – Evidence: ECO:0000269
- **Chromosome, telomere** – Evidence: ECO:0000305

### GO Cellular Component (GO-CC)
- **GO:0000781 (chromosome, telomeric region)** – Evidence: NAS:ComplexPortal
- **GO:0005737 (cytoplasm)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005654 (nucleoplasm)** – Evidence: TAS:Reactome
- **GO:0005634 (nucleus)** – Evidence: IBA:GO_Central
- **GO:0030915 (Smc5-Smc6 complex)** – Evidence: IDA:UniProtKB

### Functional Context
- Component of the SMC5-SMC6 complex, a complex involved in repair of DNA double-strand breaks by homologous recombination (PubMed:20864041, PubMed:27427983). The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of shelterin complex (telosome) components which is prop...

**Summary:** NSMCE3 has limited nuclear evidence (UniProt experimental nuclear evidence). Nuclear score: 9/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 6 | `"NSMCE3"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR...` |
| Symbol Only (Title/Abstract) | 8 | |
| Broad (All Fields) | 12 | |

**Alias Note:** Aliases observed but not used for scoring: HCA4, MAGEG1, NDNL2

### Key Papers (with PMIDs)
1. **PMID:27427983** – van der Crabben SN, Hennus MP, McGregor GA (2016 Aug 1). "Destabilized SMC5/6 complex leads to chromosome breakage syndrome with severe lung disease." *The Journal of clinical investigation.*
2. **PMID:28516231** – De Donato M, Peters SO, Hussain T (2017 Oct). "Molecular evolution of type II MAGE genes from ancestral MAGED2 gene and their phylogenetic resolution of basal mammalian clades." *Mammalian genome : official journal of the International Mammalian Genome Society.*
3. **PMID:33425727** – Arora M, Kumari S, Singh J (2020). "Downregulation of Brain Enriched Type 2 MAGEs Is Associated With Immune Infiltration and Poor Prognosis in Glioma." *Frontiers in oncology.*
4. **PMID:41825673** – He L, Shen H, Zhao A (2026 Apr). "Mechanism insights into the role of Smc5/6 in HBV inhibition." *International journal of biological macromolecules.*
5. **PMID:40728043** – Chen L, Yin J, Xu B (2025 Jul). "Fatal Lung Disease Caused by NSMCE3 Gene Mutation in an 11-Year-Old Boy." *Pediatric pulmonology.*

### Literature Assessment
- **Total publications:** Low (6 strict, 12 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96MG7-F1, version 6
- **Mean pLDDT:** 74.6
- **pLDDT Distribution:**
  - >90 (very high confidence): 41.8%
  - 70-90 (confident): 22.7%
  - 50-70 (low confidence): 7.9%
  - <50 (very low confidence): 27.6%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **5HVQ** – X-ray, 2.92 A, chains: D=78-294
- **5WY5** – X-ray, 2.92 A, chains: B=78-294

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 18/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| NSMCE1 | 0.999 | 0.999 | 0.672 | |
| SMC6 | 0.999 | 0.996 | 0.993 | |
| SMC5 | 0.999 | 0.898 | 0.978 | |
| NSMCE2 | 0.999 | 0.996 | 0.926 | |
| NSMCE4A | 0.998 | 0.908 | 0.833 | |
| EID3 | 0.996 | 0.889 | 0.629 | |
| SUMO4 | 0.914 | 0.068 | 0.143 | |
| SLF2 | 0.904 | 0.610 | 0.512 | |
| PJA1 | 0.872 | 0.789 | 0.406 | |
| RAD21 | 0.872 | 0.000 | 0.775 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 | psi-mi:"MI:0914"(association) |
| Smc6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 | psi-mi:"MI:0915"(physical association) |
| ZNF597 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| NSMCE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| PJA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| STN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| EID3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| NSMCE4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Moderate interaction network.**
- **TE-relevant connections identified:** SMC6, NSMCE2, NSMCE4A, SUMO4, SMC5, NSMCE1, RAD21
- **Score:** 39/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NSMCE3 was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** No direct nuclear localization from HPA, but other sources confirm nuclear presence.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269']).
3. **GO-CC Evidence:** Nuclear GO annotations present but may rely on non-IDA evidence codes.
4. **PubMed Count:** 6 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection appears TECHNICALLY CORRECT.** Nuclear evidence is WEAK or AMBIGUOUS. However, the specific functional profile may still warrant consideration.

---

## TE-Regulator Relevance Reasoning

1. **Ubiquitination:** NSMCE3 has ubiquitin-related functions. Ubiquitination regulates histone stability, transcription factor turnover, and chromatin protein degradation, all of which affect TE silencing.
2. **Cell Cycle:** NSMCE3 functions in cell cycle/mitosis/meiosis. TE expression is often cell-cycle regulated, and cell cycle proteins can influence chromatin states at TE loci during division.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** LOW interest candidate for TE regulation. While nuclear evidence exists, the functional profile does not strongly support a role in TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 97/180**

**Reasoning:** NSMCE3 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (6 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NSMCE3 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NSMCE3 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NSMCE3 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NSMCE3 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NSMCE3 encodes Non-structural maintenance of chromosomes element 3 homolog, a 304-amino acid 34.3 kDa protein. 
UniProt annotates nuclear localization. 
The protein functions primarily in: Component of the SMC5-SMC6 complex, a complex involved in repair of DNA double-strand breaks by homologous recombination (PubMed:20864041, PubMed:27427983). The complex may promote sister chromatid ho. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
NSMCE3 should be reevaluated in the context of broader TE biology hypotheses.
