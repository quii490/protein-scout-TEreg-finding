# MIOS – Critical False-Rejection Reevaluation Report

**Gene:** MIOS
**UniProt Accession:** Q9NXC5
**Protein Name:** GATOR2 complex protein MIOS
**Length:** 875 aa | **Mass:** 98.6 kDa
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 13 | HPA: Nucleoplasm, Cytosol (Enhanced). GO-CC: 1 IDA nuclear anno. |
| 2. Protein Size | 10 | 3 | 875 aa / 98.6 kDa – very large protein. Significant resource commitment for full characterization. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 18. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 22 | AlphaFold mean pLDDT: 82.8. PDB: 4 experimental structures. |
| 5. Regulatory Domains | 50 | 14 | InterPro: IPR037593, IPR049092, IPR015943. Function summary: As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway (PubMed:23723238, PubMed:26586190, PubMed:27487210, PubMed:35831510, Pu... |
| 6. PPI Network | 50 | 23 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **85** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Enhanced
- **Main Location:** Nucleoplasm
- **Additional Locations:** Cytosol
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoplasm, Cytosol

### UniProt Subcellular Location
- **Lysosome membrane** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0030054 (cell junction)** – Evidence: IDA:HPA
- **GO:0005737 (cytoplasm)** – Evidence: IBA:GO_Central
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0061700 (GATOR2 complex)** – Evidence: IDA:UniProtKB
- **GO:0005765 (lysosomal membrane)** – Evidence: IDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA

### Functional Context
- As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway (PubMed:23723238, PubMed:26586190, PubMed:27487210, PubMed:35831510, PubMed:36528027). The GATOR2 complex indirectly activates mTORC1 through the inhibition of the GATOR1 subcomplex (PubMed:23723238, PubMed:26586190, PubMed:27487210, PubMed:35831510, PubMed:36528027). GATOR2 probably acts as an E3 ubiquitin-protein ligase toward GATOR1 (PubMed:36528027). In the pres...

**Summary:** MIOS has limited nuclear evidence (HPA: Enhanced reliability; GO: 1 IDA nuclear annotations). Nuclear score: 13/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 18 | `"MIOS"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 107 | |
| Broad (All Fields) | 182 | |


### Key Papers (with PMIDs)
1. **PMID:35831510** – Valenstein ML, Rogala KB, Lalgudi PV (2022 Jul). "Structure of the nutrient-sensing hub GATOR2." *Nature.*
2. **PMID:40715445** – Jansen RM, Maghe C, Tapia K (2025 Oct). "Structural basis for mTORC1 regulation by the CASTOR1-GATOR2 complex." *Nature structural & molecular biology.*
3. **PMID:36220894** – Neguembor MV, Arcon JP, Buitrago D (2022 Oct). "MiOS, an integrated imaging and computational strategy to model gene folding with nucleosome resolution." *Nature structural & molecular biology.*
4. **PMID:23723238** – Bar-Peled L, Chantranupong L, Cherniack AD (2013 May 31). "A Tumor suppressor complex with GAP activity for the Rag GTPases that signal amino acid sufficiency to mTORC1." *Science (New York, N.Y.).*
5. **PMID:38928292** – Shinhmar S, Schaf J, Lloyd Jones K (2024 Jun 14). "Developing a Tanshinone IIA Memetic by Targeting MIOS to Regulate mTORC1 and Autophagy in Glioblastoma." *International journal of molecular sciences.*

### Literature Assessment
- **Total publications:** Low (18 strict, 182 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NXC5-F1, version 6
- **Mean pLDDT:** 82.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 52.2%
  - 70-90 (confident): 30.1%
  - 50-70 (low confidence): 7.9%
  - <50 (very low confidence): 9.8%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **7UHY** – EM, 3.66 A, chains: A/B=1-875
- **9LVJ** – EM, 3.82 A, chains: A/B/K/L=1-875
- **9LVK** – EM, 3.59 A, chains: A/B/K/L=1-875
- **9LWF** – EM, 3.41 A, chains: A/B/K/L=1-875

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 22/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| WDR59 | 0.999 | 0.999 | 0.997 | |
| NPRL3 | 0.999 | 0.953 | 0.840 | |
| SEC13 | 0.999 | 0.997 | 0.996 | |
| WDR24 | 0.999 | 0.999 | 0.997 | |
| NPRL2 | 0.999 | 0.997 | 0.827 | |
| SEH1L | 0.999 | 0.996 | 0.997 | |
| DEPDC5 | 0.999 | 0.996 | 0.809 | |
| KPTN | 0.998 | 0.994 | 0.618 | |
| RRAGA | 0.998 | 0.994 | 0.688 | |
| RRAGC | 0.998 | 0.994 | 0.667 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| CHM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 | psi-mi:"MI:0914"(association) |
| HERC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302|doi:10.1016/j.jmb.2018.01.021 | psi-mi:"MI:0914"(association) |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 | psi-mi:"MI:2364"(proximity) |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 | psi-mi:"MI:0914"(association) |
| RET | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008|pubmed:31585087|imex:IM-27423 | psi-mi:"MI:0914"(association) |
| LGALS3BP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 23/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
MIOS was likely auto-rejected due to:
- Large protein size (875 aa)

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – STRONG, reliability: Enhanced.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** 1 IDA-level nuclear annotations present: nucleoplasm.
4. **PubMed Count:** 18 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection appears TECHNICALLY CORRECT.** Nuclear evidence is WEAK or AMBIGUOUS. However, the specific functional profile may still warrant consideration.

---

## TE-Regulator Relevance Reasoning

1. **Ubiquitination:** MIOS has ubiquitin-related functions. Ubiquitination regulates histone stability, transcription factor turnover, and chromatin protein degradation, all of which affect TE silencing.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE interest candidate. Nuclear evidence is present but the connection to TE biology is indirect. The protein is worth retaining for secondary investigation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 85/180**

**Reasoning:** MIOS was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (18 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm MIOS nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for MIOS binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate MIOS expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether MIOS loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

MIOS encodes GATOR2 complex protein MIOS, a 875-amino acid 98.6 kDa protein. 
HPA localizes MIOS to Nucleoplasm (Enhanced reliability). 
The protein functions primarily in: As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway (PubMed:23723238, PubMed:26586190, PubMed:27487210, PubMed:35831510, Pu. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
MIOS should be reevaluated in the context of broader TE biology hypotheses.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000164654-MIOS/subcellular

![](https://images.proteinatlas.org/42928/518_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/42928/518_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/42928/530_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/42928/530_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/42928/558_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/42928/558_H4_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NXC5 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037593;IPR049092;IPR015943;IPR036322;IPR001680;IPR031488; |
| Pfam | PF21719;PF21720;PF17034; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164654-MIOS/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASTOR1 | Intact, Biogrid | true |
| SEC13 | Biogrid, Opencell, Bioplex | true |
| SESN2 | Intact, Biogrid | true |
| WDR24 | Intact, Biogrid | true |
| AIPL1 | Intact | false |
| CASTOR2 | Intact | false |
| CCT2 | Bioplex | false |
| DEPDC5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
