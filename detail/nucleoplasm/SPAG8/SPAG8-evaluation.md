# SPAG8 – Critical False-Rejection Reevaluation Report

**Gene:** SPAG8 (Sperm-associated antigen 8)  
**UniProt Accession:** Q99932  
**Protein Name:** Sperm-associated antigen 8  
**Length:** 485 aa | **Mass:** 51.1 kDa  
**Aliases:** None  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 14 | HPA: Nucleoplasm (additional, Supported), main location is Primary cilium/Acrosome/Equatorial segment/End piece. UniProt: Nucleus (listed among many locations). GO-CC: nucleoplasm (GO:0005654, IDA:HPA), nucleus (GO:0005634, IBA:GO_Central), male germ cell nucleus (GO:0001673, IEA:Ensembl). Nuclear evidence exists (IDA-level nucleoplasm) but is minor relative to the dominant ciliary/flagellar/cytoplasmic localization. The nucleoplasm signal is an ADDITIONAL location, not the main localization. The primary localization (Primary cilium, Acrosome) is non-nuclear. |
| 2. Protein Size | 10 | 6 | 485 aa / 51.1 kDa – moderate size. Deduction for being above small-protein range. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 9 publications. Very understudied. Maximum novelty. |
| 4. 3D Structure | 30 | 10 | AlphaFold mean pLDDT: 56.7. Distribution: 4.3% >90, 27.0% 70-90, 15.7% 50-70, 53.0% <50. Highly disordered – more than half the protein is very low confidence. Experimental PDB: 7UNG (EM, 3.60A, only chain D=1-485) and 8J07 (EM, 4.10A). The cryo-EM structures show SPAG8 as part of axonemal microtubules, not as an isolated structure. The protein is largely disordered outside its microtubule-bound context. |
| 5. Regulatory Domains | 50 | 8 | IPR026124 / PF22584 – uncharacterized domain. Protein functions as a microtubule inner protein (MIP) of ciliary/flagellar axonemes. Plays a role in spermatogenesis through its structural function in the sperm flagellum. No known DNA-binding, chromatin, or transcriptional regulatory domains. Purely structural cytoskeletal function in cilia. |
| 6. PPI Network | 50 | 15 | STRING: 15 partners, all ciliary/flagellar (TEKT3 0.913, CFAP126 0.908, CFAP53 0.859, CFAP52 0.845, PACRG 0.842). High experimental scores for ciliary partners. IntAct: 15 interactors including UBQLN4 (two-hybrid), USP2 (two-hybrid), PRR35 (two-hybrid), KRTAP21-2 (two-hybrid). UBQLN4 (ubiquilin 4) is involved in protein degradation and has been linked to DNA damage response, but the interaction is two-hybrid only. USP2 is a deubiquitinase with some nuclear functions, but again two-hybrid only. No nuclear-specific interacting partners. |
| **TOTAL** | **180** | **63** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Primary cilium, Acrosome, Equatorial segment, End piece
- **Additional Locations:** Nucleoplasm, Cytosol, Principal piece
- **Key Finding:** HPA main localization is exclusively cytoplasmic/ciliary (Primary cilium, Acrosome, sperm-specific compartments). Nucleoplasm is an ADDITIONAL, minor location. This pattern is consistent with a primarily ciliary protein that may have some nuclear presence in specific cell types or conditions.

**Interpretation note:** The nucleoplasm signal as an "additional" location means it is detected at lower intensity or in fewer cells than the main ciliary/acrosomal signal. This suggests SPAG8's primary localization is ciliary, with nuclear localization being a minor or conditional feature.

### UniProt Subcellular Location
- **Cytoplasm** – Listed among many locations.
- **Nucleus** – Listed, but no experimental evidence code specifically attached.
- **Cytoplasmic vesicle, secretory vesicle, acrosome** – Consistent with sperm-specific localization.
- **Cytoplasm, cytoskeleton, spindle** – Mitotic spindle association.
- **Cytoplasm, cytoskeleton, cilium axoneme** – Ciliary localization.
- **Cytoplasm, cytoskeleton, flagellum axoneme** – Flagellar localization.

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA – direct assay evidence from HPA IF. This is the strongest nuclear annotation.
- **GO:0005634 (nucleus)** – Evidence: IBA:GO_Central – phylogenetically conserved.
- **GO:0001673 (male germ cell nucleus)** – Evidence: IEA:Ensembl – electronic annotation.
- **GO:0001669 (acrosomal vesicle)** – Evidence: IDA:HPA – direct assay.
- **GO:0005879 (axonemal microtubule)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0005929 (cilium)** – Evidence: IDA:HPA – direct assay.
- **GO:0005819 (spindle)** – Evidence: IEA:UniProtKB-SubCell.

### Functional Nuclear Context
- SPAG8 is a microtubule inner protein (MIP) structurally integrated into the axoneme of motile cilia and flagella.
- The nuclear localization is likely a minor fraction. SPAG8 has been detected at the mitotic spindle (UniProt), which is consistent with microtubule binding activity but is cytoplasmic, not nuclear.
- The protein has 15 GO-CC annotations. Only 3 relate to the nucleus (nucleoplasm IDA, nucleus IBA, male germ cell nucleus IEA). The remaining 12 relate to cilia, flagella, acrosome, spindle, and cytoplasm.
- PMID:20488182 identifies SPAG8 as a regulator of CREM (cAMP response element modulator) in testis during spermatogenesis. CREM is a transcription factor. SPAG8's interaction with CREM could link it to transcriptional regulation, but this appears to be in the context of the sperm-specific activator of CREM in testis (ACT), which is a cytoplasmic/testis-specific pathway for CREM activation, not classical nuclear CREB/CREM signaling.

**Summary:** SPAG8 has weak nuclear evidence. HPA shows nucleoplasm as an ADDITIONAL (minor) location, with the main localization being ciliary/acrosomal. GO-CC has IDA-level nucleoplasm but this is one annotation among 15, with the majority relating to ciliary/flagellar compartments. SPAG8 is primarily a ciliary structural protein with possible minor or conditional nuclear presence. The CREM link (PMID:20488182) is intriguing but operates in a testis-specific cytoplasmic pathway. Nuclear score: 14/30 – moderate due to the peripheral nature of nuclear evidence.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 9 | `"SPAG8"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 16 | `"SPAG8"[Title/Abstract]` |
| Broad (All Fields) | 26 | `"SPAG8"` |

**Alias Note:** No aliases observed.

### Key Papers (with PMIDs)
1. **PMID:20488182** – Wu H, et al. (2010). "Sperm associated antigen 8 (SPAG8), a novel regulator of activator of CREM in testis during spermatogenesis." – Only paper linking SPAG8 to a transcription-related pathway (CREM/ACT).
2. **PMID:33333720** – Association of TMEM8B and SPAG8 with Mature Weight in Sheep. GWAS/linkage study.
3. **PMID:38847481** – Male infertility and perfluoroalkyl substances: evidence for alterations in phosphorylated proteins including SPAG8.
4. **PMID:36191189** – SPAG8 identified as a microtubule inner protein of ciliary doublet microtubules (structural characterization).
5. **PMID:37865089** – De novo protein identification in mammalian sperm using cryo-ET and AlphaFold2 – includes SPAG8 structural analysis.

### Literature Assessment
- **Total publications:** Very low (9 strict, 26 broad). SPAG8 is poorly studied.
- **Thematic focus:** Sperm biology, cilia/flagella structure, male infertility. The CREM paper (PMID:20488182) is the only functional study with regulatory implications.
- **Critical observation:** The CREM/ACT pathway is testis-specific and operates through a cytoplasmic mechanism distinct from classical nuclear CREB/CREM signaling. SPAG8 was found to interact with ACT (activator of CREM in testis), a testis-specific coactivator that functions in the cytoplasm of haploid spermatids.
- **No publications on TE regulation.**
- **Novelty score:** 10/10 (≤20 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q99932-F1, version 6
- **Mean pLDDT:** 56.7
- **pLDDT Distribution:**
  - >90 (very high confidence): 4.3%
  - 70-90 (confident): 27.0%
  - 50-70 (low confidence): 15.7%
  - <50 (very low confidence): 53.0%
- **Assessment:** Very poor prediction. More than half the protein (53%) is very low confidence, indicating extensive intrinsic disorder. Only 4.3% is very high confidence. This protein is predicted to be largely unstructured in isolation.

### Experimental PDB Structures
- **7UNG** – EM, 3.60A resolution. SPAG8 (chain D=1-485) in the context of axonemal doublet microtubules.
- **8J07** – EM, 4.10A resolution. SPAG8 (chains 5H/5I/5J=1-485) in axonemal microtubules.

### Structural Assessment
- SPAG8 is largely disordered in isolation (AlphaFold) but adopts structure when bound to axonemal microtubules (cryo-EM). This is typical of microtubule inner proteins, which are induced to fold upon binding their tubulin partners.
- The disorder is functionally relevant to its role as an MIP, but very detrimental to structure-based analyses.
- The protein would be difficult to produce recombinantly or crystallize outside its native complex.
- **Score:** 10/30 – Extensive disorder, only folds in complex with microtubules, very poor standalone structure.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| TEKT3 | 0.913 | 0.902 | 0 | Tektin 3, ciliary/flagellar |
| CFAP126 | 0.908 | 0.817 | 0 | Cilia and flagella associated |
| CFAP53 | 0.859 | 0.821 | 0 | Cilia and flagella associated |
| CFAP52 | 0.845 | 0.822 | 0 | Cilia and flagella associated |
| PACRG | 0.842 | 0.821 | 0 | Parkin co-regulated, ciliary |
| CFAP161 | 0.842 | 0.822 | 0 | Cilia and flagella associated |
| CFAP61 | 0.841 | 0.821 | 0 | Cilia and flagella associated |

All 15 STRING partners are ciliary/flagellar proteins with strong experimental scores (0.8-0.9). No non-ciliary partners.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| UBQLN4 | two hybrid array | PMID:25416956 | physical association |
| PRR35 | two hybrid prey pooling | PMID:32296183 | physical association |
| USP2 | two hybrid prey pooling | PMID:32296183 | physical association |
| KRTAP21-2 | two hybrid prey pooling | PMID:32296183 | physical association |
| DDI1 | two hybrid prey pooling | PMID:32296183 | physical association |

### PPI Network Assessment
- **Exclusively ciliary network in STRING:** Every STRING partner with experimental evidence is a ciliary/flagellar protein. This reflects SPAG8's function as an axonemal MIP.
- **IntAct is two-hybrid dominated:** All IntAct interactions are from large-scale two-hybrid screens, which have high false-positive rates. UBQLN4 (ubiquilin 4) is the most interesting hit – it is involved in protein degradation, autophagy, and has been implicated in DNA damage response. USP2 is a deubiquitinase. However, these are low-confidence two-hybrid hits.
- **No nuclear interactors:** None of the validated interactors are nuclear proteins. The network provides no corroboration for the nucleoplasm signal seen in HPA.
- **Score:** 15/50 – High-quality ciliary interactions confirm the known function but provide no nuclear/regulatory context.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SPAG8 was likely auto-rejected because:
1. HPA main localization is ciliary/acrosomal, not nuclear. Nucleoplasm is only an additional location.
2. The protein is highly disordered (53% <50 pLDDT).
3. Function is clearly ciliary structural (MIP of axoneme).
4. The literature does not support nuclear function.

### Recheck Analysis
1. **Nuclear Evidence:** HPA nucleoplasm is an ADDITIONAL (minor) location. The main localization is ciliary/acrosomal. This is a key distinction – SPAG8 is not primarily nuclear.
2. **CREM/ACT Connection (PMID:20488182):** The only functional study with regulatory implications. SPAG8 interacts with ACT (activator of CREM in testis), a testis-specific protein that activates CREM-dependent transcription in a cytoplasmic pathway. This is NOT the classical nuclear CREB/CREM signaling pathway. ACT is a testis-specific coactivator that operates in the cytoplasm of spermatids. SPAG8's role in this pathway is unclear but appears to involve the cytoplasmic CREM activator complex, not direct nuclear transcription regulation.
3. **Structural Function:** Cryo-EM structures confirm SPAG8 is an integral axonemal microtubule component. This is incompatible with a primary nuclear function.
4. **Literature Consensus:** The literature is unanimous in describing SPAG8 as a ciliary/flagellar and sperm protein. No publication claims nuclear function.

### Verdict on False Rejection
**The original rejection appears CORRECT.** SPAG8 is a ciliary/flagellar structural protein with minor nucleoplasm localization (additional in HPA). The CREM/ACT connection (PMID:20488182) involves a testis-specific cytoplasmic pathway, not nuclear transcription regulation. The extensive disorder, ciliary PPI network, and structural characterization as an axonemal MIP all point to SPAG8 being a cytoskeletal protein incorrectly flagged due to incidental nuclear detection.

**This gene should remain rejected.** The nuclear evidence is too weak (additional location only) and the functional evidence overwhelmingly favors a ciliary structural role.

---

## TE-Regulator Relevance Reasoning

1. **Weak Nuclear Localization:** HPA nucleoplasm is an ADDITIONAL (minor) location. The main localization is ciliary/acrosomal. TE regulation would require robust nuclear access, which SPAG8 does not demonstrate.

2. **Ciliary Structural Function:** SPAG8 is a microtubule inner protein of ciliary/flagellar axonemes. Cryo-EM structures confirm its structural integration into the microtubule lumen. This is a cytoskeletal, not regulatory, function.

3. **CREM/ACT Is Cytoplasmic:** The only regulatory connection (PMID:20488182) involves ACT, a testis-specific, cytoplasmically-acting coactivator of CREM. This pathway is distinct from nuclear CREB/CREM transcription regulation and operates in the unique chromatin environment of elongating spermatids.

4. **Extensive Intrinsic Disorder:** 53% of the protein is predicted disordered (pLDDT <50). While disorder can be functional, combined with the ciliary structural role and minor nuclear localization, it does not suggest a nuclear regulatory function.

5. **No Regulatory Domains:** PF22584 is an uncharacterized domain with no known link to DNA binding, chromatin, or transcription.

**Assessment:** SPAG8 is a LOW interest candidate for TE regulation. The protein is primarily a ciliary structural component with incidental nuclear detection. The CREM/ACT connection is specific to testis cytoplasmic signaling and does not establish nuclear regulatory function.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – nuclear evidence insufficient, primary function is ciliary structural**

**Reasoning:** SPAG8's nuclear localization is peripheral (HPA additional location only). The protein's primary function is as a microtubule inner protein of ciliary/flagellar axonemes, confirmed by cryo-EM structures. The CREM/ACT interaction (PMID:20488182) is the only regulatory link but operates in a testis-specific cytoplasmic pathway, not classical nuclear transcription. The highly disordered structure (53% <50 pLDDT), exclusively ciliary PPI network, and literature consensus all support a ciliary structural role. SPAG8 has no plausible connection to TE biology.

**Score: 63/180** – The low score reflects minimal nuclear evidence and a clearly non-regulatory primary function.

**Flag for deletion** – SPAG8 should not be reopened.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – ciliary structural protein with incidental nuclear detection*

SPAG8 illustrates a common pitfall in automated nuclear scoring: the HPA IF shows nucleoplasm as an "additional" location, which triggers a positive nuclear flag, but the biological context is entirely ciliary. The cryo-EM structures showing SPAG8 embedded in axonemal microtubules are definitive – this is a structural protein that is part of the ciliary cytoskeleton. The CREM/ACT paper (PMID:20488182) is worth noting because it establishes a functional connection to a transcription-related pathway, but the pathway is testis-specific and cytoplasmic. For TE regulation screening, SPAG8 offers nothing beyond superficial nuclear detection. Correctly rejected.
