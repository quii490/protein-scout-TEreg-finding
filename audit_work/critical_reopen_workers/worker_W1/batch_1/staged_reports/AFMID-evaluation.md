# AFMID – Critical False-Rejection Reevaluation Report

**Gene:** AFMID  
**UniProt Accession:** Q63HM1  
**Protein Name:** Kynurenine formamidase  
**Length:** 303 aa | **Mass:** 34.0 kDa  
**Aliases:** None in harvest data  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 10 | HPA main: Mitochondria (no nuclear signal). UniProt subcellular: Nucleus (ECO:0000255, sequence-based prediction, weak). GO-CC: nucleus IEA only. However, IntAct shows ChIP interactions with Ahr/Esr1 (PMID:25453901) – contextual nuclear evidence via chromatin-associated binding partners. Nuclear evidence is mostly indirect/electronic; HPA IF direct evidence contradicts nuclear localization. Score reduced significantly for this discrepancy. |
| 2. Protein Size | 10 | 10 | 303 aa / 34.0 kDa – moderate size, well within tractable range for biochemical assays. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 13 publications. Novelty = low literature volume, well under ≤20 threshold. Maximum novelty score. |
| 4. 3D Structure | 30 | 28 | AlphaFold mean pLDDT: 94.0 (90.8% >90 pLDDT) – extremely high confidence predicted structure. No experimental PDB structures, but AF quality is exceptional. Deduction of 2 for lack of experimental structure validation. |
| 5. Regulatory Domains | 50 | 20 | IPR013094 (Alpha/beta hydrolase fold), IPR029058 (alpha/beta hydrolase), IPR050300, IPR027519 (arylformamidase). PF07859 (abhydrolase). The arylformamidase activity relates to tryptophan/kynurenine metabolism. No known TE-regulatory domains (no DNA-binding, chromatin-modifying, or RNA-binding domains). Functional catalytic domain but no direct transcriptional regulatory motifs. Low regulatory domain score. |
| 6. PPI Network | 50 | 15 | STRING failed (502). IntAct: 6 interactors – DDIT4L, MEI4, MED18 (two-hybrid), Ahr (ChIP, PMID:25453901), Esr1 (ChIP, PMID:25453901), STC2 (co-IP, PMID:33961781). Small but qualitatively interesting network: ChIP interactions with nuclear receptors Ahr and Esr1 suggest chromatin association context. MED18 is a Mediator complex subunit (transcriptional coactivator). However, total interactor count is low, and most are two-hybrid screening hits without functional validation. |
| **TOTAL** | **180** | **93** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Mitochondria
- **Additional Locations:** None
- **IF Image Status:** if_display_images_available (6 IF images from cell lines: A-431, U-2 OS, U-251 MG)
- **Key Finding:** HPA immunohistochemistry/immunofluorescence localizes AFMID to mitochondria. NO nuclear signal is reported by HPA. This is the strongest direct experimental evidence and it contradicts a nuclear localization.

**Interpretation note:** HPA uses antibody-based detection; mitochondria are the primary annotated compartment. The Approved reliability score indicates reliable staining patterns. However, the protein may shuttle between compartments under specific conditions, or nuclear localization may be context-dependent (e.g., cell type, stress conditions). The HPA images were not directly fetched/displayed in this review cycle (HPA IF images listed but marked "no_image_detected" for in-report viewing), but the localization database entry is authoritative.

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000255 (sequence-based prediction, i.e., inferred from sequence or structural similarity)  
  This is an electronic annotation, meaning it was predicted computationally rather than demonstrated experimentally. Low weight.
- **Cytoplasm, cytosol** – Evidence: ECO:0000255 (same sequence-based prediction)

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell (Inferred from Electronic Annotation)  
  This is the same weak electronic evidence propagated from UniProt to GO. No independent experimental GO annotation for nuclear localization.
- **GO:0005737 (cytoplasm)** – Evidence: IBA:GO_Central (Inferred from Biological aspect of Ancestor) – moderate phylogenetic evidence
- **GO:0005829 (cytosol)** – Evidence: IEA:UniProtKB-SubCell

### Contextual Nuclear Evidence (from PPI data)
- **Ahr (aryl hydrocarbon receptor)** – ChIP assay (PMID:25453901). Ahr is a ligand-activated transcription factor that translocates to the nucleus upon activation. The ChIP interaction places AFMID in a chromatin context, potentially at Ahr target gene promoters.
- **Esr1 (estrogen receptor alpha)** – ChIP assay (PMID:25453901). Esr1 is a nuclear hormone receptor. ChIP interaction similarly suggests chromatin/nuclear association.
- **MED18 (Mediator complex subunit 18)** – two-hybrid (PMID:32296183). MED18 is part of the Mediator coactivator complex that bridges transcription factors and RNA Polymerase II, functioning in the nucleus.

**Summary:** Direct experimental evidence (HPA IF) does NOT support nuclear localization. However, the PPI network reveals chromatin-associated interactions (ChIP with Ahr/Esr1) that place AFMID in a nuclear context indirectly. The UniProt and GO nuclear annotations are purely electronic predictions. ON BALANCE, the nuclear evidence for AFMID is WEAK and CONTRADICTED by the best direct evidence (HPA). This gene should be flagged as HIGH RISK for misclassification – it may have been CORRECTLY excluded rather than falsely rejected.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 13 | `"AFMID"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 22 | `"AFMID"[Title/Abstract]` |
| Broad (All Fields) | 22 | `"AFMID"` |

### Key Papers (with PMIDs)
1. **PMID:15935693** – Pabarcus MK, Casida JE (2005). "Cloning, expression, and catalytic triad of recombinant arylformamidase." *Protein Expr Purif.* 2005 Nov. – Foundational cloning and characterization paper.
2. **PMID:38983772** – Fu L, You Y, Zeng Y (2024). "Varying the ratio of Lys:Met through enhancing methionine supplementation improved milk secretion ability through regulating the mRNA expression in bovine mammary epithelial cells under heat stress." *Front Vet Sci.* 2024. – Mentions AFMID in context of metabolic regulation.
3. **PMID:35442400** – Ladewig E, Michelini F, Jhaveri K (2022). "The Oncogenic PI3K-Induced Transcriptomic Landscape Reveals Key Functions in Splicing and Gene Expression Regulation." *Cancer Res.* 2022 Jun 15. – AFMID identified in PI3K-driven transcriptomic changes in cancer context.
4. **PMID:26432886** – Hugill AJ, Stewart ME, Yon MA (2015). "Loss of arylformamidase with reduced thymidine kinase expression leads to impaired glucose tolerance." *Biol Open.* 2015 Oct 2. – Functional study linking AFMID to metabolic phenotypes.
5. **PMID:35715314** – Chuang TD, Quintanilla D, Boos D (2022). "Further characterization of tryptophan metabolism and its dysregulation in fibroids." *F&S Sci.* 2022 Nov. – AFMID in tryptophan/kynurenine pathway in uterine fibroids.

### Literature Assessment
- **Total publications:** Very low (13 strict, 22 broad). AFMID is a poorly studied gene.
- **Thematic focus:** Tryptophan metabolism, kynurenine pathway, metabolic regulation. No literature on transcriptional regulation or TE-related functions.
- **No publications linking AFMID to transposable element regulation.**
- **Novelty score:** 10/10 (≤20 publications = maximum novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q63HM1-F1, version 6
- **Mean pLDDT:** 94.0
- **pLDDT Distribution:**
  - >90 (very high confidence): 90.8%
  - 70-90 (confident): 5.0%
  - 50-70 (low confidence): 0.7%
  - <50 (very low confidence): 3.6%
- **Assessment:** Exceptionally high-confidence predicted structure. The protein is well-folded with a clear alpha/beta hydrolase fold. The low-confidence regions (3.6% <50) are minimal, likely at flexible N-terminal or loop regions.
- **PAE Image:** Available at AF PAE URL but not locally cached. PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

### Experimental PDB Structures
- **None available.** There are no experimentally determined structures for AFMID in the PDB.

### Structural Assessment
- The alpha/beta hydrolase fold (IPR013094, PF07859) is characteristic of catalytic enzymes with a conserved catalytic triad. This structural family includes esterases, lipases, and amidases. The high pLDDT score (94.0 mean, 90.8% >90) gives very high confidence in the predicted fold.
- No DNA-binding domains, zinc fingers, chromatin-interaction motifs, or other TE-regulatory structural features are present.
- **Score:** 28/30 – exceptional prediction quality, but no experimental structure and no regulatory structural features.

---

## PPI Network

### STRING
- **Status:** FAILED (HTTP Error 502: Bad Gateway) – Data unavailable for this harvest cycle.

### IntAct
Total interactors: 6

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| DDIT4L | two hybrid array | PMID:32296183 | physical association |
| MEI4 | validated two hybrid | PMID:32296183 | physical association |
| MED18 | validated two hybrid | PMID:32296183 | physical association |
| Ahr | ChIP assay | PMID:25453901 | association |
| Esr1 | ChIP assay | PMID:25453901 | association |
| STC2 | anti tag co-IP | PMID:33961781 | physical association |

### PPI Network Assessment
- **Network size:** Small (6 interactors), mostly from high-throughput two-hybrid screens.
- **Notable interactions:**
  - **MED18:** Subunit of the Mediator complex, which is a central transcriptional coactivator complex. This interaction is from a two-hybrid array (PMID:32296183) and has not been independently validated.
  - **Ahr / Esr1:** ChIP interactions. These are chromatin immunoprecipitation experiments, which is a more functionally suggestive assay. Ahr and Esr1 are ligand-activated transcription factors. If AFMID is genuinely chromatin-associated with these nuclear receptors, this provides contextual evidence for nuclear function.
  - **STC2 (stanniocalcin-2):** Co-immunoprecipitation from a large-scale interaction mapping study (PMID:33961781). STC2 is a secreted glycoprotein involved in calcium/phosphate homeostasis; the biological relevance is unclear.
- **No interactions with known TE-regulatory proteins (e.g., KRAB-ZNFs, TRIM28, SETDB1, PIWI proteins).**
- **Score:** 15/50 – small network with no direct TE-regulatory connections. The ChIP interactions are interesting but unvalidated.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
AFMID was likely auto-rejected because the HPA IF data shows mitochondrial localization only, with no nuclear signal. The UniProt and GO nuclear annotations are purely electronic (ECO:0000255, IEA), which may have triggered a nuclear score too low to pass the threshold.

### Recheck Analysis
1. **HPA Evidence:** CONTRADICTS nuclear localization. HPA main location is Mitochondria. Reliability is Approved. This is the strongest single piece of evidence.
2. **UniProt Evidence:** Weakly supports nuclear (ECO:0000255 = sequence prediction), also supports cytosol/cytoplasm.
3. **GO-CC Evidence:** Weakly supports nucleus (IEA only), supports cytoplasm and cytosol.
4. **Contextual PPI Evidence:** ChIP interactions with nuclear receptors Ahr/Esr1 provide an interesting but indirect nuclear link. MED18 interaction suggests possible Mediator complex association.
5. **Functional Context:** AFMID is a metabolic enzyme in the kynurenine pathway. Its primary annotated function is cytoplasmic/mitochondrial. Nuclear localization would represent a non-canonical or moonlighting function.

### Verdict on False Rejection
**The original rejection was LIKELY CORRECT, not false.** The HPA direct experimental evidence places AFMID in mitochondria. The nuclear annotations are electronic predictions only. The ChIP interactions with nuclear receptors are interesting but could represent indirect associations (e.g., through chromatin/protein complexes rather than direct nuclear localization of AFMID itself).

**This gene should be retained in the REJECTED category** unless additional experimental evidence for nuclear localization becomes available.

---

## TE-Regulator Relevance Reasoning

AFMID has essentially no known connection to transposable element regulation:

1. **Function:** Kynurenine formamidase – catalyzes hydrolysis of N-formyl-L-kynurenine to L-kynurenine in the tryptophan degradation pathway. This is a metabolic function, not a gene regulatory one.
2. **Domains:** Alpha/beta hydrolase fold – catalytic domain only. No DNA-binding, chromatin-modifying, histone-modifying, or RNA-binding domains.
3. **Literature:** No publications link AFMID to TE silencing, retrotransposon regulation, or repetitive element control.
4. **PPI:** No interactions with known TE-regulatory proteins (KRAB-ZNFs, TRIM28/KAP1, SETDB1, HP1, PIWI, etc.).
5. **Nuclear localization:** Not experimentally supported.

**Assessment:** AFMID does not meet the criteria for a TE-regulatory protein. The metabolic enzymatic function, lack of regulatory domains, absence from TE-regulatory literature, and weak/contradicted nuclear evidence collectively indicate this gene is not a suitable candidate for TE regulation studies.

---

## Final Decision

**DECISION: REJECTED (confirmed)**

**Reasoning:** Despite the presence of electronic UniProt/GO nuclear annotations, the best direct experimental evidence (HPA IF, Approved reliability) places AFMID in mitochondria, not the nucleus. The protein is a metabolic enzyme (kynurenine formamidase) with an alpha/beta hydrolase catalytic domain and no known regulatory functions. The PubMed literature (13 strict, 22 broad) is focused entirely on tryptophan metabolism. PPI interactions (ChIP with Ahr/Esr1) are interesting but insufficient to establish nuclear localization in the absence of supporting direct evidence.

**Score: 93/180** – well below the typical threshold for inclusion in a TE-regulatory candidate pipeline.

The original auto-rejection appears to have been correct. This gene should NOT be reopened.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*  
*Status: CONFIRMED REJECTION – original exclusion upheld*

AFMID presents a challenging edge case: electronic annotations suggest nuclear localization, but the highest-quality experimental evidence (HPA Approved IF) contradicts this. The ChIP interactions with nuclear receptors (Ahr, Esr1) from PMID:25453901 are intriguing and warrant further investigation – it is possible that AFMID has a context-dependent nuclear function that is not detected by standard HPA IF. However, without any supporting experimental evidence (no nuclear localization demonstrated by immunofluorescence, no nuclear functional assays, no TE-regulatory literature), the conservative approach is to maintain the rejection.

**Recommendation:** If the Ahr/Esr1 ChIP interactions are of specific interest, consider re-examining AFMID only after obtaining direct experimental evidence of nuclear localization (e.g., cellular fractionation + Western blot, or immunofluorescence with nuclear counterstain in relevant cell types). For TE-regulatory purposes, this gene is a very low priority.
