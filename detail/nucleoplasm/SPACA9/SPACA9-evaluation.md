# SPACA9 – Critical False-Rejection Reevaluation Report

**Gene:** SPACA9 (Sperm acrosome-associated protein 9)  
**UniProt Accession:** Q96E40  
**Protein Name:** Sperm acrosome-associated protein 9  
**Length:** 222 aa | **Mass:** 25.2 kDa  
**Aliases:** C9orf9  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 8 | UniProt: Nucleus (ECO:0000250, sequence similarity only). HPA: Vesicles (main), Cytosol/End piece (additional) – no nucleoplasm detection. GO-CC: nucleus (GO:0005634, ISS:UniProtKB) – inferred from sequence similarity, NO direct experimental (IDA) evidence. The nuclear annotation is weak (ISS only). HPA does NOT detect nuclear localization. The protein is primarily a microtubule inner protein (MIP) of ciliary/flagellar axonemes, which is a cytoplasmic structure. The nuclear localization claim rests solely on sequence similarity inference. Most GO-CC terms relate to ciliary/flagellar compartments (acrosomal vesicle, axoneme, sperm flagellum, ciliary basal body). |
| 2. Protein Size | 10 | 8 | 222 aa / 25.2 kDa – small and tractable. Slightly above 200 aa threshold for full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 3 publications. Extremely understudied. Maximum novelty. |
| 4. 3D Structure | 30 | 22 | AlphaFold mean pLDDT: 80.3. Distribution: 67.1% >90, 3.6% 70-90, 7.2% 50-70, 22.1% <50. Three experimental cryo-EM PDB structures available (7UN1 at 6.00A, 7UNG at 3.60A, 8J07 at 4.10A) showing the protein in the context of axonemal doublet microtubules. Good structural coverage (67% very high confidence) with some disordered regions (22% <50). The cryo-EM structures provide experimental validation. |
| 5. Regulatory Domains | 50 | 8 | IPR027818 / PF15120 – structurally defined but functionally uncharacterized domain. Protein functions as a microtubule inner protein (MIP) cross-linking the lumen of axonemal doublet microtubules in cilia and flagella. No known DNA-binding, chromatin, or transcriptional regulatory domains. No link to gene regulation. Function is purely structural (cytoskeletal). |
| 6. PPI Network | 50 | 15 | STRING: 15 partners, all ciliary/flagellar proteins (CFAP77 0.901, CCDC173 0.891, EFHC1 0.823, TUBB4B 0.823). IntAct: 15 interactors including DDX24 (two-hybrid), SEPHS1 (two-hybrid), H3-4 (cross-linking), RIOX2 (co-IP). The H3-4 (histone H3.4) cross-linking interaction (PMID:30021884) is notable since it links this flagellar protein to chromatin, but this may be an artifact of proximity labeling in a cellular context. Most interactions are with ciliary/flagellar structural proteins. DDX24 (DEAD-box helicase) is a nuclear RNA helicase, the interaction was detected by two-hybrid (MI:0398) – weak evidence. RIOX2 (ribosomal oxygenase 2) is nuclear and involved in histone modification (co-IP, PMID:28514442) – this is the most interesting interaction but is a single low-confidence hit among otherwise exclusively ciliary partners. |
| **TOTAL** | **180** | **71** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Vesicles
- **Additional Locations:** Cytosol, End piece
- **Key Finding:** HPA does NOT detect nucleoplasm localization. The protein is detected in Vesicles (main), Cytosol, and End piece (additional). This is consistent with SPACA9's role as a sperm acrosome-associated and ciliary protein. The absence of nucleoplasm detection is significant for nuclear re-evaluation.

**Interpretation note:** The HPA data argues strongly AGAINST nuclear localization in the cell types examined (A-431, U-2 OS, U-251 MG). The IF images (14 total) show vesicular and cytosolic staining consistent with acrosomal/flagellar localization, not nuclear.

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000250 (inferred from sequence similarity by UniProtKB) – This is the weakest form of UniProt evidence, based on automated sequence analysis rather than experimental evidence.
- **Cytoplasm** – ECO:0000250 (sequence similarity)
- **Cytoplasmic vesicle, secretory vesicle, acrosome** – ECO:0000250 (sequence similarity)
- **Cytoplasm, cytoskeleton, cilium axoneme** – ECO:0000269 (experimental evidence) x2 – experimentally validated localization to ciliary axoneme.
- **Cytoplasm, cytoskeleton, flagellum axoneme** – ECO:0000250 (sequence similarity)

### GO Cellular Component (GO-CC)
- **GO:0005879 (axonemal microtubule)** – Evidence: IDA:UniProtKB – direct assay evidence.
- **GO:0005930 (axoneme)** – Evidence: IDA:UniProtKB – direct assay evidence.
- **GO:0005881 (cytoplasmic microtubule)** – Evidence: IDA:UniProtKB – direct assay evidence.
- **GO:0001669 (acrosomal vesicle)** – Evidence: IBA:GO_Central – phylogenetically conserved.
- **GO:0036126 (sperm flagellum)** – Evidence: IBA:GO_Central – phylogenetically conserved.
- **GO:0097546 (ciliary base)** – Evidence: IBA:GO_Central – phylogenetically conserved.
- **GO:0005634 (nucleus)** – Evidence: ISS:UniProtKB – sequence similarity only. NO experimental evidence.

### Functional Nuclear Context
- **SPACA9 is a microtubule inner protein (MIP)** that cross-links the lumen of axonemal doublet microtubules in cilia and flagella (PubMed:36191189). Cryo-EM structures (7UNG, 8J07) show SPACA9 decorating the interior of axonemal microtubules.
- **The nuclear annotation (ISS:UniProtKB) is weak and contradicted by HPA data**, which shows exclusively non-nuclear localization (Vesicles, Cytosol, End piece).
- **This protein is structurally embedded in axonemal microtubules** – it is an integral component of the ciliary/flagellar cytoskeleton, not a soluble protein that shuttles to the nucleus.

**Summary:** SPACA9 has essentially no credible nuclear evidence. The sole nuclear annotation (ISS:UniProtKB) is sequence similarity-based and not supported by any experimental data. HPA shows no nuclear localization. The protein has strong experimental evidence for localization to ciliary/flagellar axonemes and the acrosome. Nuclear score: 8/30 (generous, recognizing the ISS annotation).

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 3 | `"SPACA9"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 3 | `"SPACA9"[Title/Abstract]` |
| Broad (All Fields) | 6 | `"SPACA9"` |

**Alias Note:** Alias C9orf9 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:37865089** – Chen Z, Shiozaki M, et al. (2023). "De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking." *Cell.* – Identification of SPACA9 as an axonemal microtubule inner protein.
2. **PMID:36191189** – Gui M, Croft JT, et al. (2022). "SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules." *Proc Natl Acad Sci USA.* – Primary characterization of SPACA9 as a ciliary MIP.
3. **PMID:40453182** – Development of a procedure for isolation, identification and quality assessment of bovine spermatids.

### Literature Assessment
- **Total publications:** Extremely low (3 strict, 6 broad). SPACA9 is one of the least studied human proteins.
- **Thematic focus:** Sperm biology, cilia/flagella structure, microtubule inner proteins. The entire literature is structural/cell biology of the male reproductive system.
- **Critical gap:** No functional studies beyond structural characterization. No disease associations. No links to nuclear biology or gene regulation.
- **No publications on TE regulation.**
- **Novelty score:** 10/10 (≤20 publications = maximum novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96E40-F1, version 6
- **Mean pLDDT:** 80.3
- **pLDDT Distribution:**
  - >90 (very high confidence): 67.1%
  - 70-90 (confident): 3.6%
  - 50-70 (low confidence): 7.2%
  - <50 (very low confidence): 22.1%
- **Assessment:** Good overall structure with 67% very high confidence. The 22% disordered fraction is moderate and likely represents flexible loops in the context of the MIP fold.

### Experimental PDB Structures
- **7UN1** – EM, 6.00A resolution. SPACA9 in the context of axonemal doublet microtubules (multiple chains spanning full length).
- **7UNG** – EM, 3.60A resolution. SPACA9 as part of the axonemal microtubule doublet inner sheath.
- **8J07** – EM, 4.10A resolution. SPACA9 with multiple chains representing the protein's periodic arrangement along the microtubule.

### Structural Assessment
- The three cryo-EM structures confirm SPACA9's role as an integral component of axonemal microtubules. The protein is structurally well-characterized in its native context.
- The fold (PF15120) is specific to microtubule inner proteins and has no association with DNA binding or nuclear functions.
- **Score:** 22/30 – Good structural coverage with experimental validation, but modest disordered fraction.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| CFAP77 | 0.901 | 0.8 | 0.474 | Cilia and flagella associated protein |
| CCDC173 | 0.891 | 0.8 | 0.479 | Coiled-coil domain protein, ciliary |
| C5orf49 | 0.835 | 0.8 | 0.204 | Uncharacterized ciliary protein |
| FAM183A | 0.827 | 0.8 | 0.135 | Family with sequence similarity 183A |
| EFHC1 | 0.823 | 0.8 | 0 | EF-hand containing, ciliary |
| TUBB4B | 0.823 | 0.8 | 0.154 | Tubulin beta 4B |
| C9orf116 | 0.822 | 0.8 | 0 | Ciliary protein |
| EFHC2 | 0.819 | 0.8 | 0 | EF-hand containing 2, ciliary |
| CFAP126 | 0.818 | 0.8 | 0 | Cilia and flagella associated protein |
| CFAP45 | 0.817 | 0.8 | 0 | Cilia and flagella associated protein |
| TEKT1 | 0.815 | 0.8 | 0 | Tektin 1, microtubule inner protein |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| DDX24 | two hybrid pooling | PMID:16169070 | physical association |
| SEPHS1 | two hybrid pooling | PMID:16169070 | physical association |
| RIOX2 | anti tag co-IP | PMID:28514442 | association |
| MUCL1 | anti tag co-IP | PMID:28514442 | association |
| H3-4 | cross-linking study | PMID:30021884 | physical association |
| EFEMP2 | two hybrid array | PMID:32296183 | physical association |
| KRTAP1-1 | validated two hybrid | PMID:32296183 | physical association |

### PPI Network Assessment
- **Ciliary/flagellar-centric network:** The STRING network is dominated by ciliary and flagellar associated proteins with uniformly high experimental scores (0.8). This reflects SPACA9's role as a structural component of the axoneme.
- **H3-4 interaction:** The cross-linking detection of histone H3-4 (PMID:30021884) is the only chromatin-associated hit. This is likely a proximity artifact from cross-linking mass spectrometry of whole cells, where the abundance of histones creates many spurious interactions.
- **DDX24:** Nuclear DEAD-box RNA helicase detected by two-hybrid (pooling approach). Very indirect evidence – DDX24 is a promiscuous two-hybrid prey.
- **RIOX2:** A nuclear ribosomal oxygenase involved in histone modification (H3K9me3/H3K36me3 demethylation). Detected by co-IP (PMID:28514442). This is the most interesting nuclear-relevant interaction, but is a single hit among 15 interactors.
- **Score:** 15/50 – Overwhelmingly ciliary network. The few nuclear connections are low-confidence or likely artifactual.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SPACA9 was likely auto-rejected because:
1. HPA shows NO nucleoplasm localization (Vesicles, Cytosol, End piece only).
2. Nuclear localization evidence is ISS only (sequence similarity) – the weakest annotation type.
3. The protein is structurally characterized as a ciliary/flagellar axoneme component, making nuclear function improbable.

### Recheck Analysis
1. **Nuclear Evidence Quality:** The sole nuclear annotation (GO:0005634, ISS:UniProtKB) is automated, similarity-based, and NOT supported by any experimental data. HPA (highest resolution spatial data) explicitly shows NO nuclear localization.
2. **Functional Context:** SPACA9 is an integral structural component of axonemal microtubules. Cryo-EM structures show it decorating the microtubule lumen. This is incompatible with a nuclear function – it is physically embedded in the ciliary cytoskeleton.
3. **Tissue Specificity:** SPACA9 expression is testis/sperm-specific. The protein is part of the specialized flagellar apparatus. Testis-specific expression with no evidence of expression in other tissues where nuclear functions would be expected.
4. **Literature Consensus:** Every publication describes SPACA9 as a ciliary/flagellar structural protein. No publication mentions nuclear localization or function.

### Verdict on False Rejection
**The original rejection appears CORRECT – SPACA9 should remain rejected.** The nuclear annotation (ISS:UniProtKB) is weak, automated, and contradicted by HPA experimental data. SPACA9 is a structural component of cilia/flagella and has no plausible role in nuclear biology or TE regulation. The absence of any HPA nucleoplasm detection is decisive – this protein does not localize to the nucleus in any cell type tested.

**However**, given the request for re-evaluation, the protein's extreme novelty (3 publications) and the RIOX2 and H3-4 interactions merit acknowledgment even though they cannot redeem the localization deficiency.

---

## TE-Regulator Relevance Reasoning

1. **No Nuclear Localization:** HPA shows no nucleoplasm detection. The protein primarily localizes to vesicles, cytosol, and the acrosome/end piece (sperm flagellum). TE regulation requires nuclear access, which SPACA9 lacks.

2. **Structural/Flagellar Function Only:** SPACA9's known function is as a microtubule inner protein cross-linking the lumen of axonemal doublet microtubules. This is a purely structural/cytoskeletal role with no connection to gene regulation.

3. **Testis-Specific Expression:** SPACA9 is expressed in testis and sperm cells. While sperm biology involves unique chromatin organization (protamine replacement), SPACA9 acts on the cilium/flagellum, not on chromatin.

4. **Weak Nuclear Interactions:** The few nuclear-relevant interactors (DDX24, RIOX2, H3-4) are:
   - DDX24: Two-hybrid only (low specificity assay).
   - RIOX2: Interesting histone demethylase, but single co-IP hit.
   - H3-4: Cross-linking likely artifactual due to histone abundance.
   None of these are sufficient to override the primary localization evidence.

5. **Caveat:** The extreme novelty (3 publications) means there could be undiscovered functions. However, the cryo-EM structures showing SPACA9 embedded in axonemal microtubules make a moonlighting nuclear function extremely unlikely.

**Assessment:** SPACA9 is a LOW interest candidate for TE regulation. The structural evidence for ciliary/flagellar localization is definitive, and there is no credible evidence of nuclear function.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – nuclear evidence insufficient**

**Reasoning:** Despite extreme novelty (3 PubMed publications), SPACA9 lacks any credible nuclear localization evidence. HPA (Supported reliability) shows NO nucleoplasm detection. The sole nuclear GO annotation is ISS (sequence similarity, automated). The protein is structurally characterized as an integral axonemal microtubule component. The few nuclear-relevant interactions (RIOX2, DDX24) are low-confidence and cannot compensate for the absence of nuclear localization. This is a ciliary/flagellar structural protein with no plausible role in TE biology.

**Score: 71/180** – The low score reflects the fundamental gap: no experimental nuclear localization, no regulatory domains, and a purely structural ciliary function.

**Flag for deletion** – SPACA9 should not consume further analysis resources. The rejection was correct.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – nuclear localization absent*

SPACA9 is a valuable protein for cilia/flagella biology but has no place in a TE-regulatory protein screen. The key evidence against nuclear function is: (1) HPA detects no nucleoplasm signal, (2) the sole nuclear GO annotation is ISS (automated), (3) cryo-EM structures show SPACA9 physically embedded in axonemal microtubules, (4) expression is testis-specific with no suggestion of nuclear function in any publication. The three publications characterize SPACA9 exclusively as a ciliary structural component. While the RIOX2 interaction (histone demethylase) is intriguing, a single co-IP hit among 15 ciliary interactors does not constitute evidence of nuclear function. This gene is correctly rejected and should not be reopened.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96E40 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027818; |
| Pfam | PF15120; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165698-SPACA9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EFEMP2 | Intact | false |
| EXOC5 | Intact | false |
| KRTAP1-1 | Intact | false |
| KRTAP10-5 | Intact | false |
| KRTAP10-7 | Intact | false |
| KRTAP10-8 | Intact | false |
| KRTAP10-9 | Intact | false |
| TUBB2B | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
