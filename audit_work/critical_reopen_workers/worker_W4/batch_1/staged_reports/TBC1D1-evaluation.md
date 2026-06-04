# TBC1D1 – Critical False-Rejection Reevaluation Report

**Gene:** TBC1D1 (TBC1 domain family member 1)  
**UniProt Accession:** Q86TI0  
**Protein Name:** TBC1 domain family member 1  
**Length:** 1168 aa | **Mass:** 133.1 kDa  
**Aliases:** KIAA1108  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 16 | HPA: Nucleoli (main, Supported) – single location, nucleolar pattern. No additional locations. UniProt: Nucleus (listed). GO-CC: nucleus (GO:0005634, IEA:UniProtKB-SubCell) – electronic annotation only; Golgi apparatus (GO:0005794, IBA:GO_Central). Nuclear evidence is limited to nucleolar detection (HPA Supported) and IEA-level nucleus annotation. Nucleoli are specialized nuclear sub-compartments for ribosome biogenesis. Nucleolar localization does NOT imply chromatin-associated or transcriptional regulatory function. Most nucleolar proteins are involved in rRNA synthesis, ribosome assembly, or stress responses. No chromatin, nucleoplasm, or transcription-related annotations. |
| 2. Protein Size | 10 | 2 | 1168 aa / 133.1 kDa – very large protein. Challenging for experimental tractability. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 153 publications. Well-studied metabolic protein. Low novelty. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 70.6. Distribution: 34.9% >90, 26.0% 70-90, 7.4% 50-70, 31.7% <50. Moderate prediction with significant disorder (31.7% <50). Experimental PDB: 3QYE (X-ray, 2.20A, residues 746-1072) – covers the TBC/Rab-GAP domain. Single fragment structure at good resolution. No full-length structure. |
| 5. Regulatory Domains | 50 | 14 | IPR021785 (TBC1D1, PTB domain), IPR011993 (PH-like domain superfamily), IPR006020 (PTB/PI domain), IPR000195 (Rab-GAP/TBC domain), IPR035969 (Rab-GAP/TBC superfamily), IPR050302 (TBC1 domain-containing Rab-GAP). The protein is a Rab GTPase-activating protein (Rab-GAP) that regulates GLUT4 trafficking in response to insulin and exercise (AMPK signaling). TBC1D1 is phosphorylated by AKT and AMPK, and its phosphorylation state determines whether GLUT4 vesicles are translocated to the plasma membrane for glucose uptake. This is a key metabolic regulator in muscle and adipose tissue. No known DNA-binding, chromatin, or transcriptional regulatory domains. The PTB domain (phosphotyrosine-binding) is typically involved in phosphotyrosine-mediated protein-protein interactions, not nuclear regulation. TBC1D1 has been implicated in cell cycle regulation (some literature) and is a prognostic biomarker in gliomas (PMID:38529286), but the mechanism is through its metabolic/GAP function, not direct nuclear regulation. |
| 6. PPI Network | 50 | 28 | STRING: 15 partners. RAB10 (0.961, exp 0.057), RAB8A (0.955, exp 0.057), PRKAB1 (0.938, AMPK subunit), PRKAG3 (0.937, AMPK subunit), PRKAB2 (0.935, AMPK subunit). Network is dominated by Rab GTPases (RAB10, RAB8A, RAB2A, RAB14) and AMPK subunits. IntAct: 15 interactors including YWHAG/YWAH (14-3-3 proteins, TAP/co-IP), UBE2E2 (two-hybrid), ROR1 (co-IP), and multiple two-hybrid hits. 14-3-3 proteins are phosphoserine/phosphothreonine-binding adaptors that regulate subcellular localization of their targets. 14-3-3 binding to TBC1D1 regulates its cytoplasmic retention vs. nuclear/nucleolar localization. AMPK phosphorylates TBC1D1, creating 14-3-3 binding sites. The network is functionally coherent (insulin/AMPK signaling, GLUT4 trafficking) but all in a cytoplasmic metabolic context. |
| **TOTAL** | **180** | **82** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoli
- **Additional Locations:** None
- **Key Finding:** HPA localizes TBC1D1 exclusively to Nucleoli with Supported reliability. The nucleolar-only pattern is specific and suggests a genuine nucleolar localization. No additional compartments detected.

**Interpretation note:** Nucleolar localization is biologically interesting because the nucleolus is a dynamic nuclear sub-compartment that, beyond ribosome biogenesis, functions as a stress sensor, regulates cell cycle progression, and sequesters regulatory proteins (e.g., p53 regulation by nucleolar ARF). Nucleolar proteins can have regulatory functions, but these are typically in ribosome biogenesis, stress response, or cell cycle control – not in chromatin-level TE regulation.

### UniProt Subcellular Location
- **Nucleus** – Listed as subcellular location. Simple annotation without experimental evidence code.

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell – electronic annotation only.
- **GO:0005794 (Golgi apparatus)** – Evidence: IBA:GO_Central – phylogenetically conserved Golgi localization (consistent with role in vesicle trafficking).

### Functional Nuclear Context
- **Nucleolar Function:** TBC1D1's nucleolar localization has been noted in some studies. 14-3-3 binding regulates TBC1D1 subcellular distribution between cytoplasm and nucleus/nucleolus. AMPK phosphorylation of TBC1D1 at specific sites (e.g., Ser237) promotes 14-3-3 binding and cytoplasmic retention. In the absence of 14-3-3 binding, TBC1D1 can localize to the nucleolus.
- **GLUT4 Trafficking (Primary Function):** TBC1D1's primary and best-characterized function is cytoplasmic: it acts as a Rab-GAP to regulate GLUT4 vesicle trafficking. This is the function with physiological significance (insulin-stimulated glucose uptake, exercise metabolism, obesity, type 2 diabetes).
- **Glioma Prognostic Marker:** TBC1D1 expression correlates with immunotherapy resistance in gliomas (PMID:38529286). The mechanism may involve metabolic regulation of the tumor microenvironment rather than direct nuclear effects.
- **Cell Cycle Connection:** TBC1D1 has been nominally linked to cell cycle regulation and differentiation of various tissues. Nucleolar proteins can affect cell cycle through ribosome biogenesis control (nucleolar stress pathway). This is consistent with TBC1D1's nucleolar localization but is not a characterized function.

**Summary:** TBC1D1 has moderate nuclear evidence – HPA shows nucleolar localization (Supported). The GO nucleus annotation is electronic (IEA). The nucleolar localization is real and may have functional significance (ribosome biogenesis, stress sensing), but the primary function is cytoplasmic GLUT4 trafficking. Nucleolar localization does NOT imply chromatin-associated or TE-regulatory function. Nuclear score: 16/30 – moderate, given the specific nucleolar pattern and the absence of chromatin/nucleoplasm annotations.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 153 | `"TBC1D1"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 222 | `"TBC1D1"[Title/Abstract]` |
| Broad (All Fields) | 235 | `"TBC1D1"` |

**Alias Note:** Alias KIAA1108 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:38529286** – Novel prognostic biomarker TBC1D1 is associated with immunotherapy resistance in gliomas. Cancer biomarker study.
2. **PMID:25280670** – Roles of TBC1D1 and TBC1D4 in insulin- and exercise-stimulated glucose transport of skeletal muscle. Core metabolic function paper.
3. **PMID:23374713** – The TBC1D1 gene: structure, function, and association with obesity and related traits. Review of TBC1D1 in metabolic disease.
4. **PMID:23349522** – AMPK phosphorylation of TBC1D1 regulates GLUT4 translocation. Mechanism of metabolic regulation.
5. **PMID:19429746** – TBC1D1 mutation in human obesity. Clinical genetics of TBC1D1 in severe obesity.

### Literature Assessment
- **Total publications:** Well-studied (153 strict, 235 broad). Extensive metabolic literature.
- **Thematic focus:** Glucose metabolism, insulin signaling, GLUT4 trafficking, obesity, type 2 diabetes, exercise physiology. TBC1D1 is a central metabolic regulator.
- **Key functional theme:** TBC1D1 is a Rab-GAP that controls GLUT4 vesicle translocation to the plasma membrane. It is a convergence point for insulin (AKT) and exercise (AMPK) signaling. Phosphorylation by these kinases regulates its GAP activity and subcellular localization.
- **Nucleolar connection:** A minority of papers note nucleolar localization, but no functional studies specifically address TBC1D1's nucleolar role. The literature is overwhelmingly cytoplasmic/metabolic.
- **No publications on TE regulation.**
- **Novelty score:** 4/10 (>100 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q86TI0-F1, version 6
- **Mean pLDDT:** 70.6
- **pLDDT Distribution:**
  - >90 (very high confidence): 34.9%
  - 70-90 (confident): 26.0%
  - 50-70 (low confidence): 7.4%
  - <50 (very low confidence): 31.7%
- **Assessment:** Moderate prediction with significant disorder (31.7% <50). The structured regions likely correspond to the PTB domain, Rab-GAP domain, and regulatory phosphorylation regions. The disordered regions may represent flexible linkers and the N-terminal regulatory domain.

### Experimental PDB Structures
- **3QYE** – X-ray, 2.20A. TBC/Rab-GAP domain (residues 746-1072, chains A/B). Covers the catalytic GAP domain at good resolution. The structure reveals the conserved Rab-GAP fold with the catalytic arginine finger.

### Structural Assessment
- Single fragment structure covering the TBC/Rab-GAP domain. The PTB domain (N-terminal) and large disordered regions are not experimentally characterized.
- The TBC domain structure (3QYE) provides mechanistic insight into Rab-GAP catalysis but is not relevant to nuclear function.
- **Score:** 18/30 – Good fragment structure for catalytic domain but limited overall coverage and significant disorder.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| RAB10 | 0.961 | 0.057 | 0.532 | Ras-related protein Rab-10, GLUT4 trafficking |
| RAB8A | 0.955 | 0.057 | 0.526 | Ras-related protein Rab-8A |
| PRKAB1 | 0.938 | 0 | 0.594 | AMPK beta-1 subunit |
| PRKAG3 | 0.937 | 0 | 0.581 | AMPK gamma-3 subunit |
| PRKAB2 | 0.935 | 0 | 0.594 | AMPK beta-2 subunit |
| RAB2A | 0.93 | 0.057 | 0.574 | Ras-related protein Rab-2A |
| RAB14 | 0.926 | 0.057 | 0.573 | Ras-related protein Rab-14 |
| TBC1D4 | 0.925 | 0.103 | 0.675 | TBC1D4/AS160, paralogous Rab-GAP |

**Note:** TBC1D4/AS160 (0.925) is the paralog with similar function in GLUT4 trafficking. Rab GTPases have low experimental scores (0.057) because the GAP-substrate relationship is captured through functional assays, not physical interaction databases.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| YWHAG | anti bait co-IP | PMID:NA | physical association |
| YWHAH | tandem affinity purification | PMID:NA | physical association |
| UBE2E2 | two hybrid | PMID:25416956 | physical association |
| ROR1 | anti bait co-IP | PMID:NA | physical association |
| multiple two-hybrid | two hybrid | PMID:25416956, 32296183 | physical association |

### PPI Network Assessment
- **Metabolic signaling network:** The STRING network reflects TBC1D1's role in AMPK/insulin signaling and GLUT4 trafficking. Rab GTPases are substrates, 14-3-3 proteins (YWHAG, YWHAH) are phospho-dependent regulators, and AMPK subunits (PRKAB1/2, PRKAG3) are upstream kinases.
- **14-3-3 Proteins:** YWHAG and YWHAH are validated physical interactors. 14-3-3 binding is phosphorylation-dependent (AMPK/AKT sites) and determines TBC1D1 subcellular localization: 14-3-3 binding retains TBC1D1 in the cytoplasm; without 14-3-3, TBC1D1 can enter the nucleus/nucleolus. This is a well-characterized regulatory mechanism.
- **No nuclear partners:** None of the validated interactors are nuclear proteins. The network is entirely cytoplasmic metabolic signaling.
- **Score:** 28/50 – High-quality metabolic network with validated phosphorylation-dependent 14-3-3 regulation. However, zero nuclear interaction partners.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
TBC1D1 was likely auto-rejected because:
1. Nucleolar-only localization (not nucleoplasm/chromatin).
2. Very large protein (1168 aa).
3. Well-characterized cytoplasmic metabolic function (GLUT4 trafficking).
4. IEA-only nucleus annotation.

### Recheck Analysis
1. **Nuclear Evidence:** HPA nucleoli (Supported) is real but specific to the nucleolar compartment. TBC1D1 does not localize to the nucleoplasm or chromatin, where TE regulation occurs. Nucleolar proteins typically function in ribosome biogenesis, not chromatin-level gene regulation.
2. **Functional Context:** TBC1D1's primary and best-characterized function is cytoplasmic GLUT4 trafficking. This is a well-defined metabolic role with extensive validation. The nucleolar localization is secondary and its function (if any) is unknown.
3. **14-3-3 Regulation:** The 14-3-3-dependent regulation of TBC1D1 localization (cytoplasmic vs. nucleolar) is well-characterized but establishes a mechanism for cytoplasmic retention, not nuclear function. TBC1D1 enters the nucleolus when it is NOT bound by 14-3-3, which may be a default localization for the unphosphorylated protein rather than a regulated nuclear function.
4. **TBC1D4 Paralogue:** TBC1D4/AS160 is the paralog with overlapping function. TBC1D4 is also primarily cytoplasmic with similar GLUT4 trafficking roles. Neither protein has a characterized nuclear function.

### Verdict on False Rejection
**The original rejection appears CORRECT.** TBC1D1 has nucleolar localization (HPA Supported) but no nucleoplasm or chromatin association. The primary function is cytoplasmic (GLUT4 trafficking, Rab-GAP activity). The nucleolar localization is real but its function is unknown and likely unrelated to TE regulation, which operates at the chromatin/nucleoplasm level. The 14-3-3-dependent localization mechanism positions nuclear entry as the alternative to the primary cytoplasmic function, not as a dedicated regulatory pathway.

**This gene should remain rejected.** Nucleolar localization does not equal TE-regulatory potential.

---

## TE-Regulator Relevance Reasoning

1. **Nucleolar vs. Nucleoplasm:** TBC1D1 localizes to nucleoli, not to the nucleoplasm or chromatin. TE regulation occurs at the chromatin level in the nucleoplasm. Nucleolar proteins are specialized for ribosome biogenesis and nucleolar stress responses. There is no known mechanism by which a nucleolar Rab-GAP would regulate TE expression.

2. **Primary Function Is Metabolic:** TBC1D1's established function is cytoplasmic GLUT4 trafficking. This is a well-defined metabolic role with no connection to nuclear biology beyond the incidental nucleolar localization of a fraction of the protein.

3. **No Chromatin-Associated Domains:** The protein contains a PTB domain (phosphotyrosine-binding for protein interactions), a Rab-GAP domain (GTPase activation), and a PH-like domain (membrane/phosphoinositide binding). None of these are associated with DNA binding, chromatin modification, or transcriptional regulation.

4. **Nucleolar Role Unknown:** Even in the nucleolus, TBC1D1's function is uncharacterized. It is possible that TBC1D1 has a nucleolar stress-related function, but this would involve ribosome biogenesis control, not TE regulation. Nucleolar stress affects p53 through the ARF-MDM2-p53 pathway, which could indirectly affect TE expression, but this is a very indirect and tenuous connection.

5. **Fortuitous Expression in Cancer:** TBC1D1 is a prognostic marker in gliomas (PMID:38529286), but this reflects metabolic reprogramming in tumors, not TE regulation.

**Assessment:** TBC1D1 is a VERY LOW interest candidate for TE regulation. The nucleolar localization is the wrong nuclear compartment for TE biology. The established metabolic function and the absence of any chromatin/nucleoplasm association make TE regulation implausible.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – nucleolar protein without chromatin/nucleoplasm association**

**Reasoning:** TBC1D1 localizes to the nucleolus, not the nucleoplasm or chromatin where TE regulation occurs. The primary function is cytoplasmic GLUT4 trafficking (Rab-GAP), and the nucleolar localization is secondary and uncharacterized. TE regulation requires chromatin or nucleoplasmic localization with DNA/chromatin-associated function, neither of which TBC1D1 possesses. The IEA-only nucleus annotation and the exclusively cytoplasmic PPI network further support rejection.

**Score: 82/180** – Reflects the moderate nucleolar evidence but complete absence of chromatin/nucleoplasm or regulatory function.

**Flag for deletion** – TBC1D1 should not be reopened.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – nucleolar localization is not sufficient for TE regulation*

TBC1D1 is a metabolic protein that happens to go to the nucleolus when not retained in the cytoplasm by 14-3-3. The nucleolar localization is real (HPA Supported) but is the wrong part of the nucleus for TE biology. TE regulation requires chromatin-level access (nucleoplasm, chromatin, nuclear matrix), not nucleolar localization. The nucleolus is a specialized compartment for ribosome biogenesis. TBC1D1's well-characterized function is GLUT4 trafficking – a cytoplasmic metabolic role with clear physiological significance (insulin sensitivity, exercise metabolism, obesity). The protein is important for diabetes and metabolic disease research but has no plausible role in TE regulation. The automated rejection correctly identified this as outside the scope of a TE-regulatory screen. Should not be reopened.
