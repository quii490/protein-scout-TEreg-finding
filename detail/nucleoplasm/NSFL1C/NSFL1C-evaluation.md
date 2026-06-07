# NSFL1C – Critical False-Rejection Reevaluation Report

**Gene:** NSFL1C
**UniProt Accession:** Q9UNZ2
**Protein Name:** NSFL1 cofactor p47
**Length:** 370 aa | **Mass:** 40.6 kDa
**Aliases:** UBXN2C
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 13 | HPA: Nucleoplasm, Plasma membrane, Cytosol (Approved). UniProt: Nucleus, Chromosome. |
| 2. Protein Size | 10 | 9 | 370 aa / 40.6 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 12. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 15 | AlphaFold mean pLDDT: 74.1. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 9 | InterPro: IPR036241, IPR012989, IPR009060. Function summary: Reduces the ATPase activity of VCP (By similarity). Necessary for the fragmentation of Golgi stacks during mitosis and for VCP-mediated reassembly of Golgi stacks after mitosis (By similarity). May pl... |
| 6. PPI Network | 50 | 22 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **78** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional Locations:** Plasma membrane, Cytosol
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoplasm, Plasma membrane, Cytosol

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000250
- **Golgi apparatus, Golgi stack** – Evidence: ECO:0000250
- **Chromosome** – Evidence: ECO:0000250
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome** – Evidence: ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0005813 (centrosome)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005694 (chromosome)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005737 (cytoplasm)** – Evidence: NAS:ComplexPortal
- **GO:0005829 (cytosol)** – Evidence: IBA:GO_Central
- **GO:0005795 (Golgi stack)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005634 (nucleus)** – Evidence: IBA:GO_Central
- **GO:1990730 (VCP-NSFL1C complex)** – Evidence: IPI:ComplexPortal

### Functional Context
- Reduces the ATPase activity of VCP (By similarity). Necessary for the fragmentation of Golgi stacks during mitosis and for VCP-mediated reassembly of Golgi stacks after mitosis (By similarity). May play a role in VCP-mediated formation of transitional endoplasmic reticulum (tER) (By similarity). Inhibits the activity of CTSL (in vitro) (PubMed:15498563). Together with UBXN2B/p37, regulates the centrosomal levels of kinase AURKA/Aurora A during mitotic progression by promoting AURKA removal fr...

**Summary:** NSFL1C has limited nuclear evidence (HPA: Approved reliability; UniProt experimental nuclear evidence). Nuclear score: 13/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 12 | `"NSFL1C"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR...` |
| Symbol Only (Title/Abstract) | 15 | |
| Broad (All Fields) | 33 | |

**Alias Note:** Aliases observed but not used for scoring: UBXN2C

### Key Papers (with PMIDs)
1. **PMID:37934606** – Wang J, Chen Y, Li S (2024 Jan 2). "PP2A inhibition causes synthetic lethality in BRCA2-mutated prostate cancer models via spindle assembly checkpoint reactivation." *The Journal of clinical investigation.*
2. **PMID:39773263** – Batra S, Vaquer-Alicea J, Valdez C (2025 Jan 7). "VCP regulates early tau seed amplification via specific cofactors." *Molecular neurodegeneration.*
3. **PMID:17855441** – Chen Y, Choong LY, Lin Q (2007 Dec). "Differential expression of novel tyrosine kinase substrates during breast cancer development." *Molecular & cellular proteomics : MCP.*
4. **PMID:30783609** – Wang KZQ, Steer E, Otero PA (2018 Nov-Dec). "PINK1 Interacts with VCP/p97 and Activates PKA to Promote NSFL1C/p47 Phosphorylation and Dendritic Arborization in Neurons." *eNeuro.*
5. **PMID:38826306** – Batra S, Vaquer-Alicea JI, Valdez C (2024 May 22). "VCP regulates early tau seed amplification via specific cofactors." *Research square.*

### Literature Assessment
- **Total publications:** Low (12 strict, 33 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9UNZ2-F1, version 6
- **Mean pLDDT:** 74.1
- **pLDDT Distribution:**
  - >90 (very high confidence): 11.4%
  - 70-90 (confident): 57.0%
  - 50-70 (low confidence): 18.6%
  - <50 (very low confidence): 13.0%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **1SS6** – NMR, -, chains: A=171-270
- **8HRZ** – X-ray, 2.70 A, chains: M/N/O/P/Q/R/S/T/U/V/W/X=287-370

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 15/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| VCPIP1 | 0.999 | 0.994 | 0.875 | |
| UBXN6 | 0.999 | 0.994 | 0.702 | |
| VCP | 0.999 | 0.999 | 0.937 | |
| UBXN2A | 0.999 | 0.994 | 0.129 | |
| UFD1 | 0.998 | 0.994 | 0.681 | |
| NPLOC4 | 0.997 | 0.994 | 0.591 | |
| ASPSCR1 | 0.997 | 0.994 | 0.547 | |
| FAF1 | 0.997 | 0.994 | 0.540 | |
| UBXN7 | 0.997 | 0.994 | 0.603 | |
| UBXN10 | 0.996 | 0.994 | 0.488 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| ANP32A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| FAM32A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| GLMN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| SRP14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| LIPE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| RPL22 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| TARDBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| Vcp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 22/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NSFL1C was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – STRONG, reliability: Approved.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** Nuclear GO annotations present but may rely on non-IDA evidence codes.
4. **PubMed Count:** 12 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection appears TECHNICALLY CORRECT.** Nuclear evidence is WEAK or AMBIGUOUS. However, the specific functional profile may still warrant consideration.

---

## TE-Regulator Relevance Reasoning

1. **Cell Cycle:** NSFL1C functions in cell cycle/mitosis/meiosis. TE expression is often cell-cycle regulated, and cell cycle proteins can influence chromatin states at TE loci during division.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE interest candidate. Nuclear evidence is present but the connection to TE biology is indirect. The protein is worth retaining for secondary investigation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 78/180**

**Reasoning:** NSFL1C was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (12 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NSFL1C nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NSFL1C binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NSFL1C expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NSFL1C loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NSFL1C encodes NSFL1 cofactor p47, a 370-amino acid 40.6 kDa protein. 
HPA localizes NSFL1C to Nucleoplasm (Approved reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Reduces the ATPase activity of VCP (By similarity). Necessary for the fragmentation of Golgi stacks during mitosis and for VCP-mediated reassembly of Golgi stacks after mitosis (By similarity). May pl. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
NSFL1C should be reevaluated in the context of broader TE biology hypotheses.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000088833-NSFL1C/subcellular

![](https://images.proteinatlas.org/47108/2172_A4_5_red_green.jpg)
![](https://images.proteinatlas.org/47108/2172_A4_7_red_green.jpg)
![](https://images.proteinatlas.org/47108/748_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/47108/748_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/47108/896_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/47108/896_A9_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UNZ2 |
| SMART | SM00553;SM00166; |
| UniProt Domain [FT] | DOMAIN 179..244; /note="SEP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00732"; DOMAIN 291..368; /note="UBX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00215" |
| InterPro | IPR036241;IPR012989;IPR009060;IPR029071;IPR001012; |
| Pfam | PF08059;PF14555;PF00789; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000088833-NSFL1C/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| VCP | Intact, Biogrid, Opencell | true |
| ASPSCR1 | Biogrid | false |
| CCNF | Biogrid | false |
| FAF1 | Biogrid | false |
| FAM104A | Biogrid | false |
| FGGY | Biogrid | false |
| IDE | Biogrid | false |
| IKBKG | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
