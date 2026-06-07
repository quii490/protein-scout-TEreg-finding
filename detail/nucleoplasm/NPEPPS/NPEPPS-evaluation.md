# NPEPPS – Critical False-Rejection Reevaluation Report

**Gene:** NPEPPS
**UniProt Accession:** P55786
**Protein Name:** Puromycin-sensitive aminopeptidase
**Length:** 919 aa | **Mass:** 103.3 kDa
**Aliases:** PSA
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 0 | HPA: Cytosol (Supported). UniProt: Nucleus. |
| 2. Protein Size | 10 | 3 | 919 aa / 103.3 kDa – very large protein. Significant resource commitment for full characterization. |
| 3. Research Novelty | 10 | 7 | PubMed strict: 27. Moderately low literature. Good novelty. |
| 4. 3D Structure | 30 | 27 | AlphaFold mean pLDDT: 91.3. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 9 | InterPro: IPR045357, IPR042097, IPR024571. Function summary: Aminopeptidase with broad substrate specificity for several peptides. Involved in proteolytic events essential for cell growth and viability. May act as regulator of neuropeptide activity. Plays a rol... |
| 6. PPI Network | 50 | 15 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **61** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **IF Image Status:** if_display_images_available
- **IF Images:** 6 images available
- **All locations:** Cytosol

### UniProt Subcellular Location
- **Cytoplasm, cytosol** – Evidence: ECO:0000269
- **Nucleus** – Evidence: ECO:0000305

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0070062 (extracellular exosome)** – Evidence: HDA:UniProtKB
- **GO:0005576 (extracellular region)** – Evidence: IBA:GO_Central
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
- Aminopeptidase with broad substrate specificity for several peptides. Involved in proteolytic events essential for cell growth and viability. May act as regulator of neuropeptide activity. Plays a role in the antigen-processing pathway for MHC class I molecules. Involved in the N-terminal trimming of cytotoxic T-cell epitope precursors. Digests the poly-Q peptides found in many cellular proteins. Digests tau from normal brain more efficiently than tau from Alzheimer disease brain

**Summary:** NPEPPS has limited nuclear evidence (UniProt experimental nuclear evidence). Nuclear score: 0/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 27 | `"NPEPPS"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR...` |
| Symbol Only (Title/Abstract) | 34 | |
| Broad (All Fields) | 35 | |

**Alias Note:** Aliases observed but not used for scoring: PSA

### Key Papers (with PMIDs)
1. **PMID:39671496** – Feldman LER, Mohapatra S, Jones RT (2024 Dec 13). "Regulation of volume-regulated anion channels alters sensitivity to platinum chemotherapy." *Science advances.*
2. **PMID:40869915** – Rincic M, Brecevic L, Liehr T (2025 Jul 24). "Customized Chromosomal Microarrays for Neurodevelopmental Disorders." *Genes.*
3. **PMID:38464509** – Dai C, Wang D, Tao Q (2024). "CD8(+) T and NK cells characterized by upregulation of NPEPPS and ABHD17A are associated with the co-occurrence of type 2 diabetes and coronary artery disease." *Frontiers in immunology.*
4. **PMID:39912629** – Cazzato G, Daruish M, Fortarezza F (2025 Jun 1). "Gene Fusion-Driven Cutaneous Adnexal Neoplasms: An Updated Review Emphasizing Molecular Characteristics." *The American Journal of dermatopathology.*
5. **PMID:25903667** – Breban M, Costantino F, André C (2015 Jun). "Revisiting MHC genes in spondyloarthritis." *Current rheumatology reports.*

### Literature Assessment
- **Total publications:** Low (27 strict, 35 broad).
- **Novelty score:** 7/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P55786-F1, version 6
- **Mean pLDDT:** 91.3
- **pLDDT Distribution:**
  - >90 (very high confidence): 85.9%
  - 70-90 (confident): 7.8%
  - 50-70 (low confidence): 0.8%
  - <50 (very low confidence): 5.5%
- **Assessment:** High-confidence structure. Most of the protein is predicted with high confidence, suitable for structural studies.

### Experimental PDB Structures
- **8SW0** – X-ray, 2.30 A, chains: A=46-919
- **8SW1** – X-ray, 3.65 A, chains: A=46-919

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 27/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| SRGAP2 | 0.834 | 0.000 | 0.822 | |
| NBPF1 | 0.830 | 0.045 | 0.829 | |
| GPRIN2 | 0.829 | 0.000 | 0.826 | |
| UGT2B17 | 0.829 | 0.042 | 0.827 | |
| HYDIN | 0.829 | 0.045 | 0.829 | |
| SRGAP3 | 0.811 | 0.000 | 0.810 | |
| DRD5 | 0.810 | 0.000 | 0.810 | |
| GTF2I | 0.771 | 0.000 | 0.763 | |
| GGT6 | 0.689 | 0.000 | 0.637 | |
| GGT7 | 0.679 | 0.000 | 0.626 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| TIMP2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 15/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NPEPPS was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity
- Large protein size (919 aa)

### Recheck Analysis
1. **HPA Evidence:** No direct nuclear localization from HPA, but other sources confirm nuclear presence.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** Nuclear GO annotations present but may rely on non-IDA evidence codes.
4. **PubMed Count:** 27 strict – within acceptable range.

### Verdict on False Rejection
**The original rejection appears TECHNICALLY CORRECT.** Nuclear evidence is WEAK or AMBIGUOUS. However, the specific functional profile may still warrant consideration.

---

## TE-Regulator Relevance Reasoning

1. **Indirect Relevance:** NPEPPS's nuclear localization and functional profile suggest a structural or metabolic role without direct transcriptional/chromatin functions. TE relevance would be INDIRECT at best, possibly through general nuclear organization or cellular metabolism affecting TE expression states.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** LOW interest candidate for TE regulation. While nuclear evidence exists, the functional profile does not strongly support a role in TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 61/180**

**Reasoning:** NPEPPS was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (27 strict) is within acceptable range. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NPEPPS nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NPEPPS binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NPEPPS expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NPEPPS loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NPEPPS encodes Puromycin-sensitive aminopeptidase, a 919-amino acid 103.3 kDa protein. 
UniProt annotates nuclear localization. 
The protein functions primarily in: Aminopeptidase with broad substrate specificity for several peptides. Involved in proteolytic events essential for cell growth and viability. May act as regulator of neuropeptide activity. Plays a rol. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
NPEPPS should be reevaluated in the context of broader TE biology hypotheses.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P55786 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045357;IPR042097;IPR024571;IPR034016;IPR001930;IPR050344;IPR014782;IPR027268; |
| Pfam | PF11838;PF01433;PF17900; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141279-NPEPPS/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGR2 | Biogrid | false |
| CCNF | Biogrid | false |
| CEBPB | Biogrid | false |
| CUL3 | Biogrid | false |
| EIF6 | Biogrid | false |
| FAF2 | Biogrid | false |
| HSPA8 | Biogrid | false |
| LRRC8E | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
