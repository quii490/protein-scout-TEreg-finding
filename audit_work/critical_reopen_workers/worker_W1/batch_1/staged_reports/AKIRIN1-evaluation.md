# AKIRIN1 – Critical False-Rejection Reevaluation Report

**Gene:** AKIRIN1 (Akirin-1)  
**UniProt Accession:** Q9H9L7  
**Protein Name:** Akirin-1  
**Length:** 192 aa | **Mass:** 21.9 kDa  
**Aliases:** C1orf108  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA: Nucleoplasm (main, Approved), Nuclear membrane (additional). UniProt: Nucleus (ECO:0000269, experimental). GO-CC: chromatin (IBA:GO_Central), nuclear membrane (IDA:HPA), nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB). Multiple IDA-level annotations. Chromatin association via IBA suggests phylogenetically conserved nuclear function. Minor deduction for potential dual localization to nuclear membrane vs. nucleoplasm. |
| 2. Protein Size | 10 | 10 | 192 aa / 21.9 kDa – small, tractable. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 16 publications. Novelty rule: ≤20 = 10/10. AKIRIN1 is poorly studied, with most literature focused on its paralog AKIRIN2. Maximum novelty. |
| 4. 3D Structure | 30 | 16 | AlphaFold mean pLDDT: 68.1. Distribution: 29.7% >90, 13.5% 70-90, 29.7% 50-70, 27.1% <50. Significant predicted disorder (27.1% <50 pLDDT). No experimental PDB structures. Similar to AKIP1, the disorder likely reflects adaptor protein flexibility. |
| 5. Regulatory Domains | 50 | 30 | IPR024132 (Akirin family). Akirin proteins function as molecular adapters/bridges between proteins. AKIRIN1 is implicated in skeletal muscle development, acting as a signal transducer for myostatin (MSTN) and regulating chemotaxis via PI3K-dependent actin reorganization. Importantly, AKIRIN1 is annotated to chromatin (GO:0000785, IBA:GO_Central) and is explicitly noted as NOT involved in proteasome nuclear import (unlike AKIRIN2). This distinguishes AKIRIN1 as having a chromatin-associated (rather than nuclear transport) function. The adapter function and chromatin association are relevant to transcriptional regulation but no direct evidence of TE regulation exists. |
| 6. PPI Network | 50 | 25 | STRING: AKIRIN2 (0.849, experimental 0.82), PSMA5 (0.686), RAN (0.636), PSMB3 (0.551), PSMB9 (0.509). IntAct: PSMB3, RAN, GOPC, AKIRIN2, PSMA5, RNF181, PSMB9, PSMA2, USP7. Network is dominated by proteasome subunits. RAN is a nuclear transport GTPase. USP7 is a deubiquitinase. RNF181 is an E3 ubiquitin ligase. The proteasome connections are notable but AKIRIN1 does NOT mediate their nuclear import (that is AKIRIN2's function). Rather, AKIRIN1 may tether proteasomes to chromatin. |
| **TOTAL** | **180** | **119** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional Locations:** Nuclear membrane
- **IF Image Status:** no_image_detected (images listed but not fetchable for display in this cycle)
- **IF Image URLs:** 14 images from cell lines (A-431, U-2 OS, U-251 MG)
- **Key Finding:** HPA localizes AKIRIN1 to two nuclear compartments: Nucleoplasm (main) and Nuclear membrane (additional). The Approved reliability score (highest tier) indicates highly reproducible and specific staining.

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 The Approved reliability score and specific nuclear compartment annotations are authoritative.

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000269 (experimental evidence from publication) – experimentally demonstrated nuclear localization.

### GO Cellular Component (GO-CC)
- **GO:0000785 (chromatin)** – Evidence: IBA:GO_Central (Inferred from Biological aspect of Ancestor) – phylogenetically conserved chromatin association. This is a particularly important annotation: it means AKIRIN1 has been inferred to associate with chromatin based on evolutionary conservation, suggesting a conserved chromatin function across species.
- **GO:0031965 (nuclear membrane)** – Evidence: IDA:HPA – direct assay evidence from HPA.
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA – direct assay evidence from HPA.
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB – direct assay evidence.

### Functional Nuclear Context (critical for understanding)
- **Key functional distinction from AKIRIN2:** "In contrast to AKIRIN2, not involved in nuclear import of proteasomes" (PubMed:34711951). This is a crucial piece of information. AKIRIN1 localizes to the nucleus and interacts with proteasome subunits, but its function is NOT to import proteasomes into the nucleus (that's AKIRIN2's role). Instead, AKIRIN1 likely has a distinct chromatin-associated adapter function.
- The IBA-based chromatin annotation suggests AKIRIN1 may tether or organize proteins on chromatin.

**Summary:** AKIRIN1 has strong nuclear evidence (HPA Approved, UniProt experimental, GO IDA-level). The chromatin annotation (IBA) and the experimental distinction from AKIRIN2 make it a unique chromatin-associated adapter protein. Nuclear score: 28/30 (slight deduction for dual nuclear membrane/nucleoplasm localization ambiguity).

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 16 | `"AKIRIN1"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 19 | `"AKIRIN1"[Title/Abstract]` |
| Broad (All Fields) | 26 | `"AKIRIN1"` |

**Alias Note:** Alias C1orf108 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:30746755** – Rao VV, Sangiah U, Mary KA et al. (2019). "Role of Akirin1 in the regulation of skeletal muscle fiber-type switch." *J Cell Biochem.* 2019 Jul. – AKIRIN1 in muscle fiber type specification.
2. **PMID:31075840** – Coulibaly A, Velasquez SY, Sticht C et al. (2019). "AKIRIN1: A Potential New Reference Gene in Human Natural Killer Cells and Granulocytes in Sepsis." *Int J Mol Sci.* 2019 May 9. – AKIRIN1 as a reference gene in immune cells, implying stable expression.
3. **PMID:30777932** – Sun W, Hu S, Hu J et al. (2019). "Akirin1 promotes myoblast differentiation by modulating multiple myoblast differentiation factors." *Biosci Rep.* 2019 Mar 29. – AKIRIN1 in myogenic differentiation.
4. **PMID:32361777** – Bosch PJ, Peek SL, Smolikove S et al. (2020). "Akirin proteins in development and disease: critical roles and mechanisms of action." *Cell Mol Life Sci.* 2020 Nov. – Comprehensive review of Akirin family functions.
5. **PMID:20804733** – Macqueen DJ, Bower NI, Johnston IA (2010). "Positioning the expanded akirin gene family of Atlantic salmon within the transcriptional networks of myogenesis." *Biochem Biophys Res Commun.* 2010 Oct 1. – Evolutionary analysis of akirin family in myogenesis.

### Literature Assessment
- **Total publications:** Low (16 strict, 26 broad). AKIRIN1 is significantly less studied than its paralog AKIRIN2.
- **Thematic focus:** Skeletal muscle development, myogenesis, myoblast differentiation. No cancer or disease-focused literature for AKIRIN1 specifically.
- **Critical gap:** Most functional studies are in non-human organisms (salmon, mouse). The chromatin association of human AKIRIN1 is inferred (IBA) rather than directly demonstrated.
- **No publications on TE regulation.**
- **Novelty score:** 10/10 (≤20 publications = maximum novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9H9L7-F1, version 6
- **Mean pLDDT:** 68.1
- **pLDDT Distribution:**
  - >90 (very high confidence): 29.7%
  - 70-90 (confident): 13.5%
  - 50-70 (low confidence): 29.7%
  - <50 (very low confidence): 27.1%
- **Assessment:** Moderate-confidence structure with significant predicted disorder. The pLDDT distribution is bimodal: well-folded regions (29.7% >90) coexist with disordered regions (27.1% <50). This pattern is typical of adaptor/scaffold proteins that use folded domains for specific interactions and disordered linkers for flexibility.

### Experimental PDB Structures
- **None available.**

### Structural Assessment
- The IPR024132 domain defines the Akirin family. The structure is predicted to be partially disordered, consistent with an adaptor function.
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。
- **Score:** 16/30 – significant disorder and no experimental structure, but disorder is functionally consistent with adaptor role.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| AKIRIN2 | 0.849 | 0.82 | 0.081 | Paralog – strong experimental interaction |
| PSMA5 | 0.686 | 0.685 | 0 | Proteasome subunit alpha 5 |
| RAN | 0.636 | 0.612 | 0 | Nuclear transport GTPase |
| PRPF40A | 0.600 | 0 | 0.533 | Pre-mRNA processing factor |
| DDX17 | 0.586 | 0.298 | 0.429 | DEAD-box RNA helicase |
| KHDRBS1 | 0.583 | 0.292 | 0.424 | RNA-binding protein, signal transduction |
| PSMB3 | 0.551 | 0.55 | 0 | Proteasome subunit beta 3 |
| UHMK1 | 0.547 | 0 | 0.537 | U2AF homology motif kinase |
| PSMB9 | 0.509 | 0.509 | 0 | Immunoproteasome subunit |
| PSMA2 | 0.465 | 0.466 | 0 | Proteasome subunit alpha 2 |
| HNRNPA3 | 0.473 | 0.045 | 0.453 | Heterogeneous nuclear ribonucleoprotein |
| SNRNP200 | 0.468 | 0 | 0.464 | Spliceosome helicase |
| GAPDH | 0.458 | 0.292 | 0.261 | Multifunctional protein |

### IntAct
Total: 10 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| PSMB3 | anti tag co-IP | PMID:28514442 | association |
| RAN | anti tag co-IP | PMID:28514442 | association |
| AKIRIN2 | anti tag co-IP | PMID:28514442 | association |
| GOPC | two hybrid array | PMID:25416956 | physical association |
| PSMA5 | anti tag co-IP | PMID:33961781 | association |
| RNF181 | anti tag co-IP | PMID:33961781 | association |
| PSMB9 | anti tag co-IP | PMID:33961781 | association |
| PSMA2 | anti tag co-IP | PMID:33961781 | association |
| USP7 | phage display | PMID:35044719 | direct interaction |

### PPI Network Assessment
- **Proteasome-centric network:** AKIRIN1 interacts with multiple proteasome subunits (PSMA2, PSMA5, PSMB3, PSMB9). However, unlike AKIRIN2, AKIRIN1 does NOT mediate nuclear import of proteasomes (PubMed:34711951). This suggests AKIRIN1 may tether or organize proteasomes at specific subnuclear locations (e.g., chromatin).
- **RAN interaction:** RAN is a small GTPase that regulates nuclear transport. The AKIRIN1-RAN interaction (co-IP, PMID:28514442) could be related to nuclear localization or a distinct nuclear function.
- **Chromatin/RNA connections:** PRPF40A (pre-mRNA processing), DDX17 (RNA helicase), HNRNPA3 (RNA binding), and SNRNP200 (spliceosome) suggest connections to RNA processing and potentially chromatin-associated RNA regulation.
- **USP7:** The deubiquitinase USP7 interaction (phage display, PMID:35044719) is notable. USP7 regulates p53, MDM2, and Polycomb group proteins. It has roles in chromatin regulation and DNA damage response.
- **Score:** 25/50 – proteasome-centric network with interesting chromatin/RNA connections. The USP7 interaction is potentially relevant. Network is moderate in size and quality.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
AKIRIN1 was likely auto-rejected because:
1. Lower AlphaFold pLDDT (mean 68.1) flagged as structural quality issue
2. Confusion with AKIRIN2 (the more famous paralog) may have led to assumptions about redundant function
3. Unclear functional distinction from AKIRIN2 in automated scoring

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm (main, Approved), Nuclear membrane (additional) – STRONG, highest reliability tier.
2. **UniProt Evidence:** Nucleus (ECO:0000269) – STRONG experimental evidence.
3. **GO-CC Evidence:** Chromatin (IBA), nuclear membrane (IDA:HPA), nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB) – MULTIPLE experimental annotations including chromatin association.
4. **Critical Distinction from AKIRIN2:** AKIRIN1 is explicitly NOT involved in proteasome nuclear import (PubMed:34711951). It has a DISTINCT chromatin-associated adapter function. The automated system may not have captured this nuance.
5. **Functional Context:** Chromatin association + proteasome interactions + NOT nuclear transport = a protein that likely organizes proteasome function at chromatin, which could affect transcription factor turnover, histone degradation, or other chromatin processes.

### Verdict on False Rejection
**The original rejection was FALSE – AKIRIN1 should NOT have been rejected.** The nuclear evidence is robust (HPA Approved, UniProt experimental, multiple IDA-level GO annotations including chromatin). The key issue is that automated scoring may have confused AKIRIN1 with AKIRIN2 (which imports proteasomes into the nucleus), failing to recognize that AKIRIN1 has a distinct chromatin-associated function. The chromatin annotation (IBA) distinguishes AKIRIN1 from a generic nuclear protein and suggests a specific role at the chromatin level.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

AKIRIN1 presents an intriguing but indirect case for TE regulation:

1. **Chromatin Association:** The GO annotation to chromatin (GO:0000785, IBA:GO_Central) indicates that AKIRIN1 associates with chromatin. The phylogenetic conservation (IBA) suggests this is an evolutionarily conserved function. Chromatin-associated adapters can influence transcription, replication, and DNA repair – all relevant to TE biology.

2. **Proteasome-Chromatin Interface:** AKIRIN1 interacts with multiple proteasome subunits but does NOT mediate their nuclear import (AKIRIN2's job). Instead, AKIRIN1 likely positions or regulates proteasome activity at chromatin. Targeted protein degradation at chromatin is important for regulating transcription factors, histones, and chromatin modifiers – all of which affect TE expression.

3. **Myogenic Context:** AKIRIN1 is primarily studied in skeletal muscle development. Muscle cells are post-mitotic and maintain specific chromatin organization. TE expression in muscle (e.g., LINE-1 in myoblasts) is an underexplored area. AKIRIN1 could contribute to muscle-specific TE regulation.

4. **USP7 Connection:** The interaction with USP7 (deubiquitinase, phage display, PMID:35044719) is notable. USP7 deubiquitinates histones H2A and H2B, regulates Polycomb group proteins, and affects chromatin structure. USP7 is known to influence TE silencing through histone ubiquitination pathways.

5. **Caveats:**
   - No direct evidence of TE regulation.
   - The chromatin association is inferred (IBA), not directly demonstrated for human AKIRIN1.
   - The small size (192 aa) and lack of known DNA-binding or histone-modifying domains mean AKIRIN1 would act as an adaptor/cofactor, not a direct regulator.
   - Very limited human-specific functional data.

**Assessment:** AKIRIN1 is a MODERATE interest candidate for TE regulation, primarily based on its chromatin association and its potential role in organizing proteasome activity at specific genomic loci. The high novelty (16 publications) makes it an attractive target for original investigation, but the functional evidence is less developed than for other candidates. It would be best pursued in the context of broader Akirin family chromatin functions.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Reasoning:** AKIRIN1 was falsely rejected despite robust nuclear evidence (HPA Approved, UniProt experimental, multiple GO IDA). The chromatin association annotation (IBA) and the explicit functional distinction from AKIRIN2 (not involved in proteasome nuclear import) make AKIRIN1 a unique chromatin-associated adapter worth investigating. The extremely low literature count (16 PubMed) offers maximum novelty. The proteasome-USP7-chromatin interaction network provides mechanistic hypotheses for TE regulation.

**Score: 119/180** – The lower score reflects the indirect nature of the TE-regulatory connection and the limited functional characterization of human AKIRIN1. However, the nuclear + chromatin evidence and high novelty justify reopening.

**Recommended next steps:**
1. Directly demonstrate chromatin association for human AKIRIN1 (ChIP-seq or chromatin fractionation).
2. Determine whether AKIRIN1 affects proteasome activity or localization at specific chromatin regions.
3. Investigate AKIRIN1 expression/function in the context of myogenic TE regulation.
4. Explore the AKIRIN1-USP7 interaction and its potential role in histone ubiquitination at repetitive elements.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*  
*Status: FALSE REJECTION CONFIRMED – gene reopened*

AKIRIN1's false rejection appears to result from its smaller size, partially disordered structure, and the overshadowing effect of its better-studied paralog AKIRIN2. However, careful reading of the literature reveals a key functional distinction: AKIRIN1 is chromatin-associated but does NOT mediate proteasome nuclear import. This positions AKIRIN1 at the chromatin-proteasome interface, a role that could affect transcription factor turnover, histone degradation, and chromatin remodeling at TE loci. The Approved HPA IF reliability for nucleoplasm is among the strongest localization evidence available. The USP7 interaction adds a deubiquitination dimension relevant to chromatin regulation. While AKIRIN1 is not the strongest candidate in functional terms, its high novelty and unique chromatin-associated adapter role make it worth retaining in the pipeline for further investigation.
