# TPPP – Critical False-Rejection Reevaluation Report

**Gene:** TPPP (Tubulin polymerization-promoting protein) / TPPP/p25  
**UniProt Accession:** O94811  
**Protein Name:** Tubulin polymerization-promoting protein  
**Length:** 219 aa | **Mass:** 23.7 kDa  
**Aliases:** TPPP1  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 14 | HPA: protein page found but no IF image detected (status: page_found_no_if_image_detected), Reliability: None, all location lists empty. HPA provides NO localization information. UniProt: Nucleus listed among multiple locations (Golgi outpost, cytoplasm, microtubule organizing center, nucleus, spindle). GO-CC: nucleus (GO:0005634, IDA:UniProtKB) – direct experimental evidence for nuclear localization. Other GO terms: cytoplasm (IDA), cytosol (IDA:HPA), microtubule, mitochondrion (IDA:HPA), mitotic spindle (IDA), perinuclear region (IDA). Nuclear localization is experimentally demonstrated (IDA) but is one of many compartments. The protein's primary localization is cytoplasmic/cytoskeletal (microtubule organizing center, spindle, perinuclear region). The nuclear pool is real but appears to be a minor fraction. |
| 2. Protein Size | 10 | 8 | 219 aa / 23.7 kDa – small protein, tractable. Slightly above 200 aa for full marks. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 152 publications. Well-studied due to Parkinson's disease connection. Lower novelty. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 78.1. Distribution: 40.2% >90, 34.2% 70-90, 7.3% 50-70, 18.3% <50. Good prediction with ~74% high confidence (>70). Experimental PDB: 3 cryo-EM structures. 9J4D (2.93A, residues 44-174), 9J4E (3.32A, full-length 1-219), 9J4F (2.49A, full-length 1-219). Full-length structures available at moderate resolution (2.49-3.32A). The structures show TPPP in complex with microtubules, revealing the mechanism of microtubule binding and polymerization. |
| 5. Regulatory Domains | 50 | 12 | IPR011992 (EF-hand domain pair) – calcium-binding domain typically involved in signal transduction. IPR008907 (TPPP family) / PF05517 (TPPP). TPPP is a microtubule-associated protein that promotes tubulin polymerization and stabilizes microtubules. It functions as a microtubule nucleation factor in oligodendrocytes, promoting elongation of the myelin sheath (PMID:31522887). It also regulates the microtubule network in neurons. TPPP is a key component of pathological inclusions in multiple system atrophy (MSA) and Parkinson's disease – it co-aggregates with alpha-synuclein (SNCA) in oligodendroglial cytoplasmic inclusions (Papp-Lantos bodies). The protein's established functions are exclusively cytoskeletal (microtubule polymerization, stabilization). No known DNA-binding, chromatin modification, or transcriptional regulatory activity. The EF-hand domain suggests calcium-regulated function, but this is also in the context of microtubule regulation, not nuclear signaling. |
| 6. PPI Network | 50 | 24 | STRING: 15 partners. DCTN2 (dynactin 2, 0.968), DCTN1 (dynactin 1, 0.959), SNCA (alpha-synuclein, 0.923, exp 0.694), CAPZA2 (0.902), CAPZA1 (0.900), CAPZB (0.894). Network is cytoskeletal: dynactin complex, capping protein, alpha-synuclein. IntAct: 15 interactors including SNCA (pull down, validated), CDK11B (two-hybrid), H1-4 (histone H1.4, cross-linking), HMGN2 (cross-linking), Invs (co-IP). The H1-4 (histone H1) and HMGN2 (nucleosome-binding protein) interactions are potentially chromatin-relevant. HMGN2 is a high mobility group nucleosome-binding protein that modulates chromatin structure and transcription. Histone H1 is a linker histone involved in higher-order chromatin folding. Both interactions are detected by cross-linking (PMID:30021884) – a proximity-based method. However, the cross-linking context may be mitotic (microtubule-chromatin interface at the mitotic spindle), not interphase nuclear function. |
| **TOTAL** | **180** | **86** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** page_found_no_if_image_detected
- **Reliability (IF):** None
- **Main Location:** [] (empty)
- **Additional Locations:** [] (empty)
- **All Locations:** [] (empty)
- **Key Finding:** HPA could not obtain IF images for TPPP. The protein page exists in HPA but no IF images are available, and no localization could be determined. This is a complete data gap that cannot support or refute nuclear localization.

**Interpretation note:** The absence of HPA IF data is a technical limitation, not biological evidence. TPPP may not be expressed in the standard HPA cell lines (A-431, U-2 OS, U-251 MG), or the available antibodies may not work well in IF. HPA provides zero information for TPPP's subcellular localization.

### UniProt Subcellular Location
- **Golgi outpost** – Golgi-derived structures at specific subcellular locations.
- **Cytoplasm, cytoskeleton, microtubule organizing center** – Primary localization at MTOC.
- **Cytoplasm, cytoskeleton** – Microtubule-associated.
- **Nucleus** – Nuclear localization listed.
- **Cytoplasm, cytoskeleton, spindle** – Mitotic spindle association.

TPPP localizes to multiple compartments, with the dominant localization being cytoskeletal (microtubule organizing center, spindle, cytoskeleton). Nuclear localization is listed but is one of five subcellular locations.

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB – direct experimental assay. Nuclear localization is experimentally validated. This is strong evidence.
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA – direct assay.
- **GO:0072686 (mitotic spindle)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0005739 (mitochondrion)** – Evidence: IDA:HPA – direct assay.
- **GO:0048471 (perinuclear region of cytoplasm)** – Evidence: IDA:HGNC-UCL – direct assay.
- **GO:0005874 (microtubule)** – Evidence: IEA:Ensembl – electronic.
- **GO:0005815 (microtubule organizing center)** – Evidence: IEA:UniProtKB-SubCell.
- **GO:0150051 (postsynaptic Golgi apparatus)** – Evidence: ISS:UniProtKB.

Nuclear evidence: IDA-level experimental validation. However, the protein localizes to 9 different GO-CC compartments, indicating multifocal distribution. The nucleus is one of many destinations, not the primary one.

### Functional Nuclear Context
- **Mitotic Spindle-Chromatin Interface:** TPPP localizes to the mitotic spindle (GO:0072686, IDA). During mitosis, the spindle interacts with chromosomes at kinetochores. The cross-linking interactions with histone H1.4 and HMGN2 (PMID:30021884) may reflect TPPP at the mitotic spindle-chromatin interface, not an interphase nuclear function. This is a critical distinction: mitotic spindle localization is cytoskeletal (microtubule-based), not nuclear regulatory.
- **Microtubule-to-Nucleus Transport:** TPPP, as a microtubule-associated protein, could facilitate transport of cargo along microtubules to the nucleus. However, this would be a trafficking function, not a direct nuclear regulatory function.
- **No Known Nuclear Function:** Despite the IDA-level nucleus annotation, the literature does not describe a specific nuclear function for TPPP. The protein is characterized as a microtubule regulator (polymerization, stabilization). The nuclear pool may be a minor fraction without a characterized function, or it may reflect detection at the nuclear envelope/MTOC interface.

**Summary:** TPPP has moderate nuclear evidence. GO-CC shows nucleus (IDA:UniProtKB) – experimentally validated. UniProt lists nucleus. However, HPA has no data, the nuclear pool appears minor among 9 localization compartments, and no nuclear function has been described. Nuclear score: 14/30 – IDA evidence is real but the primary function is cytoskeletal.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 152 | `"TPPP"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 201 | `"TPPP"[Title/Abstract]` |
| Broad (All Fields) | 262 | `"TPPP"` |

**Alias Note:** Alias TPPP1 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:31522887** – TPPP functions as a microtubule nucleation factor in oligodendrocytes, promoting myelin sheath elongation.
2. **PMID:35000546** – Autophagy mediates the clearance of oligodendroglial SNCA/alpha-synuclein and TPPP/p25A in multiple system atrophy.
3. **PMID:40973885** – Alpha synuclein-mediated cytoskeletal dysfunction impairs myelination in human oligodendrocytes.
4. **PMID:32120304** – TPPP gene methylation and corpus callosum measures in maltreated children. Epigenetic study linking TPPP methylation to brain development.
5. **PMID:23807128** – TPPP/p25 in multiple system atrophy: pathological hallmark of oligodendroglial inclusions.

### Literature Assessment
- **Total publications:** Well-studied (152 strict, 262 broad). Extensive neuroscience literature.
- **Thematic focus:** Microtubule dynamics, myelination, multiple system atrophy (MSA), Parkinson's disease, alpha-synuclein aggregation. TPPP is a neuropathological protein.
- **Key functional theme:** TPPP promotes tubulin polymerization and microtubule stabilization. In oligodendrocytes, it nucleates microtubules for myelin sheath extension. In disease, it co-aggregates with alpha-synuclein in oligodendroglial cytoplasmic inclusions (hallmark of MSA).
- **Epigenetic connection:** TPPP methylation is associated with corpus callosum development (PMID:32120304), but TPPP is the methylation target (epigenetically regulated gene), not the methylator.
- **No publications on nuclear function or TE regulation.**
- **Novelty score:** 4/10 (>100 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-O94811-F1, version 6
- **Mean pLDDT:** 78.1
- **pLDDT Distribution:**
  - >90 (very high confidence): 40.2%
  - 70-90 (confident): 34.2%
  - 50-70 (low confidence): 7.3%
  - <50 (very low confidence): 18.3%
- **Assessment:** Good prediction quality. Nearly 75% of the protein is confidently predicted (>70 pLDDT), with 40% at very high confidence (>90). The 18.3% disordered fraction likely corresponds to the flexible N-terminus.

### Experimental PDB Structures
- **9J4D** – EM, 2.93A. TPPP (residues 44-174) bound to microtubules. Shows the microtubule-binding mode.
- **9J4E** – EM, 3.32A. Full-length TPPP (1-219) on microtubules.
- **9J4F** – EM, 2.49A. Full-length TPPP (1-219) on microtubules. Highest resolution.

### Structural Assessment
- Three cryo-EM structures show full-length TPPP bound to microtubules at moderate resolution (2.49-3.32A). The structures reveal how TPPP interacts with the microtubule lattice to promote polymerization.
- The structures are recent (2024 entries) and provide excellent mechanistic insight into TPPP's microtubule nucleation function.
- All structures are in the microtubule-bound state – no structures of the soluble or nuclear form are available.
- **Score:** 24/30 – Full-length structures at good resolution in the functionally relevant microtubule-bound state.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| DCTN2 | 0.968 | 0 | 0.489 | Dynactin 2, microtubule motor adaptor |
| DCTN1 | 0.959 | 0 | 0.279 | Dynactin 1, microtubule motor |
| SNCA | 0.923 | 0.694 | 0.789 | Alpha-synuclein, MSA/PD protein |
| CAPZA2 | 0.902 | 0 | 0.327 | Capping actin protein, cytoskeletal |
| CAPZA1 | 0.9 | 0 | 0.301 | Capping actin protein |
| CAPZB | 0.894 | 0 | 0.24 | Capping actin protein beta |
| MAPT | 0.887 | 0.596 | 0.783 | Tau, microtubule-associated protein |
| TUBA1A | 0.813 | 0.255 | 0.214 | Tubulin alpha-1A |

**Note:** SNCA has good experimental score (0.694) reflecting the co-aggregation in MSA pathology. MAPT (tau) has experimental score 0.596, consistent with both being microtubule-associated proteins.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| SNCA | pull down | PMID:NA | physical association |
| CDK11B | two hybrid | PMID:25416956 | physical association |
| H1-4 | cross-linking study | PMID:30021884 | physical association |
| HMGN2 | cross-linking study | PMID:30021884 | physical association |
| Invs | anti tag co-IP | PMID:28514442 | association |

### PPI Network Assessment
- **Cytoskeletal network:** The STRING network is cytoskeletal: dynactin complex (microtubule motor), alpha-synuclein (pathological aggregation), capping protein (actin regulation), tau (microtubule binding). This reflects TPPP's function as a microtubule regulator.
- **H1-4 (Histone H1.4):** Linker histone that binds nucleosomes and promotes higher-order chromatin folding. Detected by cross-linking (PMID:30021884). This interaction could represent TPPP at the mitotic spindle-chromatin interface or a genuine interphase nuclear interaction. Cross-linking captures proximity, not functional interaction. The histone interaction is weak evidence for nuclear function.
- **HMGN2:** High mobility group nucleosome-binding protein 2. HMGN2 binds nucleosomes and modulates chromatin structure and transcription. It is a nuclear protein that decompacts chromatin. Cross-linking detection (PMID:30021884). Like H1-4, this could represent mitotic or interphase interaction.
- **SNCA (alpha-synuclein):** Pulled down, validated. Alpha-synuclein is predominantly cytoplasmic/synaptic but has been reported in the nucleus where it may regulate transcription. The SNCA-TPPP interaction is best characterized in the context of pathological protein aggregation in MSA.
- **Score:** 24/50 – Good cytoskeletal network quality. The H1-4 and HMGN2 interactions are chromatin-relevant but detected only by cross-linking. SNCA interaction is validated.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
TPPP was likely auto-rejected because:
1. HPA has no IF images and no localization data.
2. The protein is a well-characterized microtubule regulator with no known nuclear function.
3. Nuclear GO annotation is one of many compartments, and the primary function is cytoskeletal.

### Recheck Analysis
1. **Nuclear Evidence:** The nuclear GO annotation (GO:0005634, IDA:UniProtKB) provides experimental evidence for nuclear localization. However, this is one of 9 GO-CC terms, and the protein's characterized functions are exclusively cytoskeletal. The nuclear pool is real but its function is unknown.
2. **Chromatin Interactions:** Cross-linking interactions with H1-4 (linker histone) and HMGN2 (nucleosome-binding protein) are the only chromatin-relevant data. Cross-linking captures proximity – TPPP may be near chromatin at the mitotic spindle during mitosis, or these may reflect genuine interphase nuclear interactions. Without orthogonal validation, these are weak evidence.
3. **Functional Context:** TPPP's primary and best-characterized function is microtubule polymerization and stabilization. It is a cytoskeletal protein first and foremost. The nuclear localization and chromatin interactions are secondary features that have not been functionally characterized.
4. **Disease Context:** TPPP is primarily a neurodegeneration protein (MSA, Parkinson's). Its pathological role involves microtubule dysfunction and protein aggregation, not nuclear dysregulation.

### Verdict on False Rejection
**The original rejection was PROBABLY CORRECT.** TPPP has experimentally validated nuclear localization (GO IDA) and cross-linking interactions with chromatin proteins (H1-4, HMGN2), but the primary function is unambiguously cytoskeletal (microtubule polymerization). The nuclear function (if any) is unknown and there is no characterized connection to TE biology. The protein's value for a TE-regulatory screen is minimal.

**This gene should remain rejected** unless resources are available for exploratory investigation of its chromatin interactions.

---

## TE-Regulator Relevance Reasoning

1. **Multicompartmental Localization:** TPPP localizes to 9 GO-CC compartments, with the nucleus being one of them (IDA-validated). The nuclear pool is minor compared to the dominant cytoskeletal localization. TE regulation requires robust nuclear/chromatin access, which TPPP may not provide.

2. **Primary Function Is Cytoskeletal:** TPPP promotes tubulin polymerization and microtubule stabilization. This is a purely cytoskeletal function. The connection to nuclear biology is through mitotic spindle function (a microtubule-based structure that interacts with chromosomes), not through direct chromatin or transcriptional regulation.

3. **Weak Chromatin Interactions:** H1-4 and HMGN2 interactions are detected by cross-linking only. These proximity-based interactions do not establish functional relevance. They may reflect: (a) TPPP at the mitotic spindle-chromatin interface during cell division, (b) genuine interphase nuclear interactions, or (c) cross-linking artifacts from abundant chromatin proteins.

4. **No Regulatory Domains:** TPPP has an EF-hand domain (calcium binding) and a TPPP-specific domain. Neither is associated with DNA binding, chromatin modification, or transcriptional regulation. The protein is a structural component of the cytoskeleton.

5. **Neurodegeneration Context:** TPPP's disease relevance is in synucleinopathies (MSA, PD). Protein aggregation in oligodendrocytes is the pathological mechanism. This has no connection to TE biology.

**Assessment:** TPPP is a LOW interest candidate for TE regulation. The nuclear localization is real but minor, the chromatin interactions are weak (cross-linking only), and the primary function is cytoskeletal. TPPP is an excellent microtubule biology/neurodegeneration protein with no credible link to TE regulation.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – cytoskeletal protein with minor, uncharacterized nuclear pool**

**Reasoning:** TPPP has experimentally validated nuclear localization (GO:0005634, IDA) but the nuclear pool is minor among 9 subcellular compartments, and its function is unknown. The primary function is microtubule polymerization, a cytoskeletal process. Cross-linking interactions with H1-4 and HMGN2 are chromatin-relevant but weak evidence (proximity detection only, no functional validation). No characterized connection to TE biology. TPPP should not be reopened.

**Score: 86/180** – Inflated by good structural data (24/30). The nuclear and regulatory scores are appropriately low.

**Flag for deletion** – TPPP should not be reopened.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – cytoskeletal protein, correctly rejected*

TPPP is a microtubule-associated protein that was rightly rejected. The nuclear localization (GO IDA) is a minor feature of a primarily cytoskeletal protein. The cross-linking interactions with chromatin proteins (H1-4, HMGN2) are tantalizing but insufficient to establish nuclear function – they likely reflect the mitotic spindle-chromatin interface. TPPP's established biology is entirely in the cytoskeletal/neurodegeneration space. It is a valuable protein for multiple system atrophy and Parkinson's disease research, but it has no place in a TE-regulatory screen. The excellent cryo-EM structures (3 full-length structures on microtubules) confirm the protein's function as a microtubule regulator. Correctly rejected.
