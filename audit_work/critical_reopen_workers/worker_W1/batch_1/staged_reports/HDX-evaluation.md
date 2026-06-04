# HDX – Critical False-Rejection Reevaluation Report

**Gene:** HDX
**UniProt Accession:** Q7Z353
**Protein Name:** Highly divergent homeobox
**Length:** 690 aa | **Mass:** 77.2 kDa
**Aliases:** CXorf43
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 6 | HPA: Cytosol; GO-CC: chromatin (ISA:NTNU_SB) |
| 2. Protein Size | 10 | 8 | 690 aa / 77.2 kDa. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 1060. Range: >100 (REJ). |
| 4. 3D Structure | 30 | 11 | mean pLDDT: 55.5 (>90: 20.9%, 70-90: 8.4%, 50-70: 10.3%, <50: 60.4%). PDB: 2DA4 (NMR, -) |
| 5. Regulatory Domains | 50 | 25 | TR: no; Chromatin: yes; Epigenetic: no; DNA/RNA bind: no. |
| 6. PPI Network | 50 | 17 | STRING: 4; IntAct: 15; UniProt: 14. |
| **TOTAL** | **180** | **67** | **REJECTED: PubMed>100** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Cytosol
- **Additional:** None
- **IF Image Status:** if_display_images_available

**Interpretation note:** HPA IF images were not reliably obtainable for this review cycle. Nuclear localization assessment is based on HPA localization/reliability annotations combined with UniProt subcellular evidence and GO Cellular Component annotations.

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000255

### GO Cellular Component (GO-CC)
- **GO:0000785 (chromatin)** – Evidence: ISA:NTNU_SB
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
N/A

**Summary:** Nuclear score 6/30. Limited nuclear evidence.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 1060 |
| Broad (All Fields) | 1715 |

**Alias Note:** Aliases observed but not used for scoring: CXorf43

**REJECTION TRIGGERED: PubMed strict > 100.**


### Key Papers (with PMIDs)
  - **PMID:36251047** – Vinciauskaite V, Masson GR (2023 Mar 29). "Fundamentals of HDX-MS." *Essays in biochemistry*.
  - **PMID:40867645** – Hamuro Y, Armstrong A, Branson J (2025 Aug 20). "Enhancement of Protein-Protein Interactions by Destabilizing Mutations Revealed by HDX-MS." *Biomolecules*.
  - **PMID:40482399** – Guffick C, Politis A (2025 Oct). "HDX-MS in micelles and membranes for small molecule and biopharmaceutical development." *Current opinion in structural biology*.
  - **PMID:36636941** – Chow V, Wolf E, Lento C (2023 Mar 29). "Developments in rapid hydrogen-deuterium exchange methods." *Essays in biochemistry*.
  - **PMID:32709043** – Narang D, Lento C, J Wilson D (2020 Jul 17). "HDX-MS: An Analytical Tool to Capture Protein Motion in Action." *Biomedicines*.

### Literature Assessment
- **Total:** Very high – REJECTED (1060 strict, 1715 broad).
- **Novelty score:** 0/10.
- **TE-relevance in literature:** No publications directly link HDX to TE regulation.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q7Z353-F1, v6
- **mean pLDDT: 55.5 (>90: 20.9%, 70-90: 8.4%, 50-70: 10.3%, <50: 60.4%)**
- **Assessment:** Very low confidence

### Experimental PDB Structures
- **1 structures:** 2DA4 (NMR, -)

### Structural Assessment
- PAE images were not locally generated or reliably fetched for this cycle. Structural judgment based on AlphaFold pLDDT statistics and available PDB structures.
- Score: 11/30.

---

## PPI Network

### STRING
- **SMIM1** (score: 0.572)
- **RINT1** (score: 0.556)
- **HOMEZ** (score: 0.417)
- **STX18** (score: 0.403)


### IntAct
- Total: 15 interactors
- **POLR1E** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **Arhgap18** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:32203420|imex:IM-26436)
- **Arhgap33** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:32203420|imex:IM-26436)
- **BOLA1** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **BOLA2-SMG1P6** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **TTC5** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **TSGA10** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **MID2** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)


### PPI Network Assessment
- Network size: Moderate.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
HDX was likely auto-rejected due to: PubMed>100

### Recheck Analysis
1. **HPA:** Cytosol
2. **UniProt:** Weak or absent experimental nuclear evidence
3. **GO-CC:** Nuclear/chromatin GO terms present
4. **PubMed:** 1060 strict – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT** under the PubMed>100 rule. However, functional evidence may warrant exception review.

**REMAINS REJECTED** per pipeline rules. Exception review recommended if waiver criteria exist.

---

## TE-Regulator Relevance Reasoning

**MODERATE relevance.** HDX has functional features potentially relevant to TE regulation .

---

## Final Decision

**DECISION: REJECTED (PubMed>100)**

**Score: 67/180.**

**Reasoning:** HDX exceeds the published rejection threshold (PubMed>100 = 1060 publications). While functional evidence may be relevant to TE biology, the gene meets exclusion criteria and should remain rejected unless exception waivers are applied.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 – exception review recommended*

This gene exceeds the automated rejection threshold (PubMed>100). While functional evidence is relevant to TE biology, pipeline rules dictate exclusion. If exception or waiver processes are available, this gene should be prioritized for reconsideration based on its functional profile.
