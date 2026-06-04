# HERC2 – Critical False-Rejection Reevaluation Report

**Gene:** HERC2
**UniProt Accession:** O95714
**Protein Name:** E3 ubiquitin-protein ligase HERC2
**Length:** 4834 aa | **Mass:** 527.2 kDa
**Aliases:** None
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 8 | HPA: Cytosol; GO-CC: nucleoplasm (TAS:Reactome) |
| 2. Protein Size | 10 | 8 | 4834 aa / 527.2 kDa. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 195. Range: >100 (REJ). |
| 4. 3D Structure | 30 | 22 | mean pLDDT: N/A (>90: N/A%, 70-90: N/A%, 50-70: N/A%, <50: N/A%). PDB: 2KEO (NMR, -); 3KCI (X-ray, 1.80 A); 4L1M (X-ray, 2.60 A); 6WW3 (X-ray, 2.10 A); 6WW4 (X-ray, 2.25 A); 7Q40 (X-ray, 2.35 A); 7Q41 (X-ray, 3.01 A); 7Q4 |
| 5. Regulatory Domains | 50 | 20 | TR: no; Chromatin: no; Epigenetic: yes; DNA/RNA bind: no. |
| 6. PPI Network | 50 | 21 | STRING: 15; IntAct: 15; UniProt: 9. |
| **TOTAL** | **180** | **79** | **REJECTED: PubMed>100** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **Additional:** Plasma membrane
- **IF Image Status:** if_display_images_available

**Interpretation note:** HPA IF images were not reliably obtainable for this review cycle. Nuclear localization assessment is based on HPA localization/reliability annotations combined with UniProt subcellular evidence and GO Cellular Component annotations.

### UniProt Subcellular Location
- **Cytoplasm** – Evidence: 
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole** – Evidence: 
- **Nucleus** – Evidence: 

### GO Cellular Component (GO-CC)
- **GO:0005814 (centriole)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0016020 (membrane)** – Evidence: HDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: TAS:Reactome
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0005886 (plasma membrane)** – Evidence: IDA:HPA

### Functional Context
E3 ubiquitin-protein ligase that regulates ubiquitin-dependent retention of repair proteins on damaged chromosomes. Recruited to sites of DNA damage in response to ionizing radiation (IR) and facilitates the assembly of UBE2N and RNF8 promoting DNA damage-induced formation of 'Lys-63'-linked ubiquitin chains. Acts as a mediator of binding specificity between UBE2N and RNF8. Involved in the maintenance of RNF168 levels. E3 ubiquitin-protein ligase that promotes the ubiquitination and proteasomal 

**Summary:** Nuclear score 8/30. Limited nuclear evidence.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 195 |
| Broad (All Fields) | 323 |


**REJECTION TRIGGERED: PubMed strict > 100.**


### Key Papers (with PMIDs)
  - **PMID:37115922** – Choi DJ, Armstrong G, Lozzi B (2023 Apr 28). "The genomic landscape of familial glioma." *Science advances*.
  - **PMID:37480851** – Yagita Y, Zavodszky E, Peak-Chew SY (2023 Aug 3). "Mechanism of orphan subunit recognition during assembly quality control." *Cell*.
  - **PMID:36721234** – Liu Y, Xu Q, Deng F (2023 Feb 1). "HERC2 promotes inflammation-driven cancer stemness and immune evasion in hepatocellular carcinoma by activating STAT3 pathway." *Journal of experimental & clinical cancer research : CR*.
  - **PMID:39522250** – Zhang M, Cui Y, Jia R (2024 Dec). "Hesperidin alleviated dendritic spines through inhibiting ferritinophagy via HERC2-NCOA4 ubiquitination in CUMS mice." *Phytomedicine : international journal of phytotherapy and phytopharmacology*.
  - **PMID:34662013** – Lui F, Stokkermans TJ (2026 Jan). "Heterochromia." **.

### Literature Assessment
- **Total:** Very high – REJECTED (195 strict, 323 broad).
- **Novelty score:** 0/10.
- **TE-relevance in literature:** No publications directly link HERC2 to TE regulation.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** N/A, vN/A
- **mean pLDDT: N/A (>90: N/A%, 70-90: N/A%, 50-70: N/A%, <50: N/A%)**
- **Assessment:** Very low confidence

### Experimental PDB Structures
- **13 structures:** 2KEO (NMR, -); 3KCI (X-ray, 1.80 A); 4L1M (X-ray, 2.60 A); 6WW3 (X-ray, 2.10 A); 6WW4 (X-ray, 2.25 A); 7Q40 (X-ray, 2.35 A); 7Q41 (X-ray, 3.01 A); 7Q42 (X-ray, 1.95 A); 7Q43 (X-ray, 2.40 A); 7Q44 (X-ray, 2.20 A) ... +3 more

### Structural Assessment
- PAE images were not locally generated or reliably fetched for this cycle. Structural judgment based on AlphaFold pLDDT statistics and available PDB structures.
- Score: 22/30.

---

## PPI Network

### STRING
- **RNF8** (score: 0.952)
- **NEURL4** (score: 0.937)
- **UBE3A** (score: 0.91)
- **MYT1** (score: 0.901)
- **DOCK10** (score: 0.901)


### IntAct
- Total: 15 interactors
- **MPDU1** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **DISC1** (psi-mi:"MI:0018"(two hybrid), pubmed:17043677|imex:IM-16650)
- **DBNL** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **MAP1LC3B** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:20562859|imex:IM-15184)
- **ORF** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-17346|pubmed:22190034|psi-mi:"MI)
- **ZRANB1** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-12079|pubmed:19615732)
- **USP19** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-12079|pubmed:19615732)
- **USP20** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-12079|pubmed:19615732)


### PPI Network Assessment
- Network size: Moderate.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
HERC2 was likely auto-rejected due to: PubMed>100

### Recheck Analysis
1. **HPA:** Cytosol
2. **UniProt:** Weak or absent experimental nuclear evidence
3. **GO-CC:** Nuclear/chromatin GO terms present
4. **PubMed:** 195 strict – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT** under the PubMed>100 rule. However, functional evidence may warrant exception review.

**REMAINS REJECTED** per pipeline rules. Exception review recommended if waiver criteria exist.

---

## TE-Regulator Relevance Reasoning

**MODERATE relevance.** HERC2 has functional features potentially relevant to TE regulation .

---

## Final Decision

**DECISION: REJECTED (PubMed>100)**

**Score: 79/180.**

**Reasoning:** HERC2 exceeds the published rejection threshold (PubMed>100 = 195 publications). While functional evidence may be relevant to TE biology, the gene meets exclusion criteria and should remain rejected unless exception waivers are applied.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 – exception review recommended*

This gene exceeds the automated rejection threshold (PubMed>100). While functional evidence is relevant to TE biology, pipeline rules dictate exclusion. If exception or waiver processes are available, this gene should be prioritized for reconsideration based on its functional profile.
