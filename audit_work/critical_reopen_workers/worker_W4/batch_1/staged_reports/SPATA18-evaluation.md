# SPATA18 – Critical False-Rejection Reevaluation Report

**Gene:** SPATA18 (Spermatogenesis-associated protein 18) / MIEAP (Mitochondria-eating protein)  
**UniProt Accession:** Q8TC71  
**Protein Name:** Mitochondria-eating protein  
**Length:** 538 aa | **Mass:** 61.1 kDa  
**Aliases:** MIEAP  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 12 | HPA: Mitochondria (main), Nucleoplasm and Cytosol (additional). Nucleoplasm is an ADDITIONAL (minor) location. UniProt: Exclusively cytoplasmic/mitochondrial (cytosol, mitochondrial outer membrane, mitochondrial matrix). No nuclear localization in UniProt. GO-CC: nucleoplasm (GO:0005654, IDA:HPA) – direct assay from HPA IF. This is the only nuclear GO annotation among 7 total. The primary localization is mitochondrial and cytoplasmic. The nucleoplasm signal likely represents a minor fraction or detection in specific cell types. |
| 2. Protein Size | 10 | 6 | 538 aa / 61.1 kDa – moderate-large size. Deduction for scale. |
| 3. Research Novelty | 10 | 8 | PubMed strict: 30 publications. Low-moderate publication count. Novelty still high but above the ≤20 threshold for full marks. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 75.4. Distribution: 39.4% >90, 28.4% 70-90, 11.7% 50-70, 20.4% <50. Moderate-good prediction quality. Nearly 40% very high confidence, but 20% is very low confidence (likely disordered). No experimental PDB structures. |
| 5. Regulatory Domains | 50 | 10 | IPR026169 (SPATA18 family) / PF16026 (DUF4795). The domains are uncharacterized (DUF = Domain of Unknown Function). The protein's established function is as a mitochondrial quality control factor (mitochondria-eating protein, MIEAP). It mediates the repair or degradation of unhealthy mitochondria in response to damage (PubMed:21264221, PubMed:21264228). Regulates mitophagy by interacting with BNIP3 and BNIP3L (mitophagy receptors). Also designated as a p53/p63 transcriptional target (PMID:21300779), connecting it to the p53 tumor suppressor pathway. However, the protein itself is not a transcription factor – it is a p53 target gene. No known DNA-binding, chromatin, or direct transcriptional regulatory domains. |
| 6. PPI Network | 50 | 22 | STRING: 15 partners. SGCB (0.79), BNIP3L (0.747), BNIP3 (0.628), ATG5 (0.535), MAP1LC3B (0.498). Network is dominated by mitochondrial/autophagy proteins (BNIP3, BNIP3L are mitophagy receptors; ATG5 and MAP1LC3B are core autophagy machinery). ATG9A (0.513) is an autophagy transmembrane protein. IntAct: 15 interactors including LRIF1 (nuclear receptor interacting factor, two-hybrid), PIBF1 (progesterone-induced blocking factor, two-hybrid), AIMP2 (aminoacyl-tRNA synthetase complex-interacting multifunctional protein 2, two-hybrid), GOLGA2 (golgin A2, two-hybrid). LRIF1 is the most interesting: it interacts with nuclear receptors, is involved in chromatin organization, and localizes to the nucleus. However, this is a two-hybrid hit only. AIMP2 has a secondary nuclear function in p53 activation (forms a complex with p53 after DNA damage). |
| **TOTAL** | **180** | **76** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Mitochondria
- **Additional Locations:** Nucleoplasm, Cytosol
- **Key Finding:** HPA main localization is mitochondrial. Nucleoplasm is an ADDITIONAL (minor) location. The mitochondrial signal is dominant, consistent with the protein's established function as MIEAP (mitochondria-eating protein). The nucleoplasm detection is secondary and may represent a small fraction of protein or detection in specific cell contexts (e.g., upon stress).

**Interpretation note:** Detection of nucleoplasm as an additional location could reflect: (1) a genuine minor nuclear pool with distinct function, (2) detection of newly synthesized protein before mitochondrial import, or (3) protein released from damaged mitochondria during HPA sample preparation. The mitochondrial-dominant pattern makes the first interpretation most plausible, but the functional significance is unknown.

### UniProt Subcellular Location
- **Cytoplasm, cytosol** – Listed multiple times, likely reflecting different conditions (inactive and active states).
- **Mitochondrion outer membrane** – Localizes to the outer membrane for mitophagy initiation.
- **Mitochondrion matrix** – Can translocate to the mitochondrial matrix.
- **Note:** No nuclear localization in UniProt subcellular locations.

### GO Cellular Component (GO-CC)
- **GO:0005739 (mitochondrion)** – Evidence: IDA:HPA – direct assay.
- **GO:0005759 (mitochondrial matrix)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0005741 (mitochondrial outer membrane)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA – direct assay.
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA – direct assay. The only nuclear annotation.
- **GO:0043231 (intracellular membrane-bounded organelle)** – Evidence: IDA:UniProtKB.

### Functional Nuclear Context
- **p53 Target Gene:** SPATA18/MIEAP is a direct transcriptional target of p53 and p63 (PMID:21300779). The p53 binding site is in the SPATA18 promoter. When p53 is activated by DNA damage, SPATA18 is transcriptionally upregulated. This links SPATA18 to the nuclear p53 pathway, but SPATA18 is the target (output), not the regulator (input).
- **Potential Nuclear Role:** AIMP2 (interactor by two-hybrid) has a nuclear function as a p53 activator. AIMP2 translocates to the nucleus upon DNA damage and directly interacts with p53 to prevent MDM2-mediated degradation. This connection could place SPATA18 in a feedback loop: p53 activates SPATA18 transcription; SPATA18 protein may interact with AIMP2; AIMP2 feeds back to stabilize p53. However, this is speculative and based on weak two-hybrid evidence.
- **LRIF1 Interaction:** LRIF1 (ligand-dependent nuclear receptor interacting factor 1) is a nuclear protein that interacts with nuclear hormone receptors and is involved in chromatin organization. Two-hybrid only.

**Summary:** SPATA18 has weak nuclear evidence. HPA shows nucleoplasm as an ADDITIONAL (minor) location. UniProt lists no nuclear localization. Only 1 of 7 GO-CC annotations is nuclear. The primary localization and function are mitochondrial (mitophagy). The p53 target gene connection is real but positions SPATA18 as downstream of nuclear signaling, not as a nuclear regulator. Nuclear score: 12/30 – moderate, given the secondary nucleoplasm detection and the absence of dedicated nuclear annotations.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 30 | `"SPATA18"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 37 | `"SPATA18"[Title/Abstract]` |
| Broad (All Fields) | 53 | `"SPATA18"` |

**Alias Note:** Alias MIEAP observed but not used for scoring. Alias MIEAP (mitochondria-eating protein) is commonly used in the mitochondrial/mitophagy literature.

### Key Papers (with PMIDs)
1. **PMID:21300779** – Bornstein C, et al. (2011). "SPATA18, a spermatogenesis-associated gene, is a novel transcriptional target of p53 and p63." – Establishes SPATA18 as a p53/p63 target gene, linking it to the DNA damage response pathway.
2. **PMID:21264221** – Kitamura N, et al. (2011). "Mieap, a p53-inducible protein, controls mitochondrial quality by repairing or eliminating unhealthy mitochondria." – Primary characterization of MIEAP/SPATA18 function as a mitochondrial quality control factor.
3. **PMID:21264228** – Nakamura Y, et al. (2011). "BNIP3 and NIX mediate Mieap-induced accumulation of lysosomal proteins within mitochondria." – Mechanism of MIEAP-mediated mitophagy through BNIP3/BNIP3L.
4. **PMID:36751118** – High SPATA18 Expression and its Diagnostic and Prognostic Value in Clear Cell Renal Cell Carcinoma. Cancer biomarker study.
5. **PMID:38830862** – Analysis of human neuronal cells carrying ASTN2 deletion – SPATA18 among altered genes.

### Literature Assessment
- **Total publications:** Low-moderate (30 strict, 53 broad). Focused but not extensive literature.
- **Thematic focus:** Dominated by mitochondrial biology (mitophagy, mitochondrial quality control). Secondary cancer biomarker literature (SPATA18 as a p53 target with possible tumor suppressor function).
- **Key functional theme:** SPATA18/MIEAP is a mitochondrial quality control protein. It functions at mitochondria to either repair damaged mitochondria or target them for lysosomal degradation (mitophagy). The mechanism involves BNIP3 and BNIP3L (mitophagy receptors) and lysosomal proteins.
- **p53 connection:** SPATA18 is transcriptionally regulated by p53, making it part of the p53-mediated DNA damage response. This is a nuclear-to-mitochondrial signaling axis: nuclear p53 activates SPATA18 transcription, the protein goes to mitochondria to control quality.
- **No publications on TE regulation.**
- **Novelty score:** 8/10 (31-50 publications range).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8TC71-F1, version 6
- **Mean pLDDT:** 75.4
- **pLDDT Distribution:**
  - >90 (very high confidence): 39.4%
  - 70-90 (confident): 28.4%
  - 50-70 (low confidence): 11.7%
  - <50 (very low confidence): 20.4%
- **Assessment:** Moderate-good prediction with significant disorder (20.4% very low confidence). The structured regions likely form the core mitochondrial interaction domains, while disordered regions may mediate dynamic localization or protein-protein interactions.

### Experimental PDB Structures
- **None available.**

### Structural Assessment
- The structure is partially well-folded (67.8% >70 confidence) but contains substantial disordered regions (20.4% <50). This is consistent with a mitochondrial quality control protein that needs to interact with multiple partners (mitochondrial membranes, BNIP3, ATG proteins, lysosomal proteins).
- The DUF4795 domain (PF16026) is functionally uncharacterized but likely mediates protein-protein interactions in the mitophagy pathway.
- **Score:** 18/30 – Moderate prediction quality with no experimental structure. The disorder is functionally consistent with the dynamic localization and multi-partner interactions.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| SGCB | 0.79 | 0 | 0.79 | Sarcoglycan beta, muscle |
| BNIP3L | 0.747 | 0 | 0.747 | BCL2 interacting protein 3 like, mitophagy receptor |
| BNIP3 | 0.628 | 0 | 0.628 | BCL2 interacting protein 3, mitophagy receptor |
| SPATA45 | 0.626 | 0 | 0.57 | Spermatogenesis-associated 45 |
| SPATA19 | 0.607 | 0 | 0.569 | Spermatogenesis-associated 19 |
| ATG5 | 0.535 | 0 | 0.36 | Autophagy protein 5 |
| MAP1LC3B | 0.498 | 0 | 0.319 | LC3B, autophagosome marker |
| BNIP1 | 0.494 | 0 | 0.454 | BCL2 interacting protein 1 |

**Note:** All STRING scores are textmining/co-occurrence based. No experimental confidence scores.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| PIBF1 | two hybrid array | PMID:25416956 | physical association |
| AIMP2 | two hybrid array | PMID:25416956 | physical association |
| GOLGA2 | two hybrid array | PMID:25416956 | physical association |
| LRIF1 | validated two hybrid | PMID:32296183 | physical association |
| ENSP00000295213.4 | two hybrid prey pooling | PMID:32296183 | physical association |

### PPI Network Assessment
- **Mitochondrial/autophagy context:** The literature-established interactions (BNIP3, BNIP3L) are supported by functional studies (PMID:21264228) but show no STRING experimental scores – indicating the functional studies are not captured in STRING's interaction databases. The IntAct network (all two-hybrid) does not include these functionally validated interactions, revealing a gap between functional literature and interaction databases for this protein.
- **LRIF1:** The most nuclear-relevant interactor. LRIF1 is a nuclear receptor co-factor involved in chromatin organization and nuclear receptor signaling. Validated two-hybrid (PMID:32296183). This is a weak but interesting connection to nuclear chromatin function.
- **AIMP2:** Aminoacyl-tRNA synthetase complex-interacting multifunctional protein 2. Has a well-characterized nuclear function as a p53 activator (translocates to nucleus upon DNA damage, binds p53, prevents MDM2-mediated degradation). Two-hybrid only for SPATA18 interaction. Potentially forms a p53-SPATA18-AIMP2 regulatory circuit.
- **Network weakness:** All validated interactors are from large-scale two-hybrid screens. The functionally important interactions (BNIP3, BNIP3L, ATG5) are not captured in IntAct. The interaction data is incomplete and biased toward two-hybrid-detectable interactions.
- **Score:** 22/50 – The literature-established mitochondrial interactions are well-supported functionally but poorly captured in databases. The LRIF1 and AIMP2 connections are intriguing but low-confidence (two-hybrid only).

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SPATA18 was likely auto-rejected because:
1. Primary localization is mitochondrial, not nuclear.
2. UniProt lists no nuclear localization.
3. The protein's known function (mitophagy) has no connection to nuclear biology or TE regulation.
4. Nuclear detection (HPA additional location) is secondary.

### Recheck Analysis
1. **Nuclear Evidence:** HPA shows nucleoplasm as an ADDITIONAL (minor) location. UniProt lists NO nuclear localization. Only 1 of 7 GO-CC annotations is nuclear. The nuclear signal is real but minor.
2. **Functional Context:** SPATA18/MIEAP is a mitochondrial quality control protein. Its established function is at mitochondria (repair/degrade damaged mitochondria). This is a cytoplasmic/mitochondrial function with no direct nuclear component.
3. **p53 Connection:** SPATA18 is a p53 transcriptional target (promoter contains p53 binding site). This places SPATA18 in the p53 pathway but as a target (output), not a regulator (input). p53 regulates SPATA18 expression; SPATA18 does not regulate p53 or nuclear events.
4. **AIMP2-LRIF1 Connections:** Two-hybrid interactions with nuclear proteins (AIMP2, LRIF1) are weak evidence that does not override the primary mitochondrial function and localization.

### Verdict on False Rejection
**The original rejection appears CORRECT.** SPATA18 is primarily a mitochondrial protein with minor nucleoplasm detection. The established function is mitochondrial quality control (mitophagy). The p53 connection positions SPATA18 downstream of nuclear signaling, not as a nuclear regulator. The weak nuclear interactor data (AIMP2, LRIF1, two-hybrid only) does not establish a nuclear function.

**This gene should remain rejected.** SPATA18 is a valuable mitochondrial/mitophagy protein but has no plausible role in TE regulation.

---

## TE-Regulator Relevance Reasoning

1. **Minor Nuclear Detection:** HPA nucleoplasm is additional, not main. The protein is primarily mitochondrial. For TE regulation, robust nuclear localization is a prerequisite, and SPATA18 does not meet this threshold.

2. **Mitochondrial Function:** The established function is mitochondrial quality control (mitochondria-eating protein). Mitophagy, while important for cellular homeostasis, is a cytoplasmic process with no direct connection to TE regulation.

3. **p53 Pathway Position:** SPATA18 is a p53 target gene, not a p53 regulator. The protein is induced by p53 and acts at mitochondria. This is a downstream effector role. While p53 is relevant to TE regulation (through DNA damage response and apoptosis), SPATA18 is far downstream and operates in the wrong compartment (mitochondria).

4. **Weak Nuclear Interactions:** AIMP2 (p53 activator) and LRIF1 (nuclear receptor co-factor) interactions are two-hybrid only and do not establish a nuclear function for SPATA18. These may be false positives from large-scale screens.

5. **No Regulatory Domains:** The DUF4795 domain is functionally uncharacterized. No known DNA-binding, chromatin, or transcriptional domains.

**Assessment:** SPATA18 is a LOW interest candidate for TE regulation. The mitochondrial/mitophagy function, minor nuclear localization, and downstream position in the p53 pathway all argue against a nuclear regulatory role.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – mitochondrial protein with minor nuclear detection**

**Reasoning:** SPATA18/MIEAP is a well-characterized mitochondrial quality control protein. The nucleoplasm detection is secondary (HPA additional location only). The protein's function is at mitochondria (mitophagy), not in the nucleus. The p53 connection is as a target gene, not as a regulator. The weak two-hybrid interactions with nuclear proteins (AIMP2, LRIF1) cannot overturn the primary localization and functional evidence. SPATA18 has no credible connection to TE biology.

**Score: 76/180** – The score reflects weak nuclear evidence and a clearly non-nuclear primary function.

**Flag for deletion** – SPATA18 should not be reopened.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – mitochondrial protein, correctly rejected*

SPATA18 is an excellent mitochondrial protein with a clear and important function in mitochondrial quality control. It should not have been included in the false-rejection queue. The nuclear detection (HPA additional nucleoplasm) likely represents a minor soluble pool or pre-mitochondrial newly synthesized protein. The p53 target gene relationship is real and interesting for cancer biology, but SPATA18 is the effector that acts at mitochondria after being induced by nuclear p53. For a TE-regulatory screen, SPATA18 offers nothing: no nuclear function, no chromatin interaction, no transcriptional regulatory activity. Correctly rejected; should not be reopened.
