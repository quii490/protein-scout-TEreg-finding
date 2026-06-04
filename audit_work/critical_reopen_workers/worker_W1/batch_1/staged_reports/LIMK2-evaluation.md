# LIMK2 – Critical False-Rejection Reevaluation Report

**Gene:** LIMK2
**UniProt Accession:** P53671
**Protein Name:** LIM domain kinase 2
**Length:** 638 aa | **Mass:** 72.2 kDa
**Aliases:** None
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 29 | HPA: Nucleoplasm (primary, Supported); UniProt: experimental nuclear evidence; GO-CC: nucleus (IBA:GO_Central) |
| 2. Protein Size | 10 | 8 | 638 aa / 72.2 kDa. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 150. Range: >100 (REJ). |
| 4. 3D Structure | 30 | 24 | mean pLDDT: 76.2 (>90: 34.0%, 70-90: 37.5%, 50-70: 13.0%, <50: 15.5%). PDB: 1X6A (NMR, -); 4TPT (X-ray, 2.60 A); 5NXD (X-ray, 1.90 A); 7QHG (X-ray, 1.45 A); 8GI4 (X-ray, 2.06 A); 8S3X (X-ray, 2.59 A); 8WSW (X-ray, 2.50 A) |
| 5. Regulatory Domains | 50 | 30 | TR: yes; Chromatin: no; Epigenetic: no; DNA/RNA bind: no. |
| 6. PPI Network | 50 | 13 | STRING: 15; IntAct: 15; UniProt: 4. |
| **TOTAL** | **180** | **104** | **REJECTED: PubMed>100** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional:** Cytosol
- **IF Image Status:** no_image_detected

**Interpretation note:** HPA IF images were not reliably obtainable for this review cycle. Nuclear localization assessment is based on HPA localization/reliability annotations combined with UniProt subcellular evidence and GO Cellular Component annotations.

### UniProt Subcellular Location
- **Cytoplasm, cytoskeleton, spindle** – Evidence: ECO:0000269
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome** – Evidence: ECO:0000269
- **Cytoplasm** – Evidence: ECO:0000269
- **Nucleus** – Evidence: ECO:0000269
- **Cytoplasm** – Evidence: ECO:0000269
- **Cytoplasm, perinuclear region** – Evidence: ECO:0000269
- **Nucleus** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005813 (centrosome)** – Evidence: IDA:UniProtKB
- **GO:0005801 (cis-Golgi network)** – Evidence: IEA:Ensembl
- **GO:0005737 (cytoplasm)** – Evidence: IBA:GO_Central
- **GO:0072686 (mitotic spindle)** – Evidence: IDA:UniProtKB
- **GO:0005634 (nucleus)** – Evidence: IBA:GO_Central
- **GO:0048471 (perinuclear region of cytoplasm)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
Serine/threonine-protein kinase that plays an essential role in the regulation of actin filament dynamics (PubMed:10436159, PubMed:11018042). Acts downstream of several Rho family GTPase signal transduction pathways (PubMed:10436159, PubMed:11018042). Involved in astral microtubule organization and mitotic spindle orientation during early stages of mitosis by mediating phosphorylation of TPPP (PubMed:22328514). Displays serine/threonine-specific phosphorylation of myelin basic protein and histon

**Summary:** Nuclear score 29/30. Experimental support from HPA/UniProt/GO.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 150 |
| Broad (All Fields) | 286 |


**REJECTION TRIGGERED: PubMed strict > 100.**


### Key Papers (with PMIDs)
  - **PMID:38580197** – Chong ZX, Ho WY, Yeap SK (2024 Jun 15). "Decoding the tumour-modulatory roles of LIMK2." *Life sciences*.
  - **PMID:39201250** – Ferrito N, Báez-Flores J, Rodríguez-Martín M (2024 Aug 6). "Biomarker Landscape in RASopathies." *International journal of molecular sciences*.
  - **PMID:34066036** – Sooreshjani MA, Nikhil K, Kamra M (2021 May 12). "LIMK2-NKX3.1 Engagement Promotes Castration-Resistant Prostate Cancer." *Cancers*.
  - **PMID:39153710** – Gong C, Chang L, Huang R (2024 Oct). "LIM kinase 2 activates cardiac fibroblasts and exacerbates postinfarction left ventricular remodeling via crosstalk between the canonical and non-canonical Wnt pathways." *Pharmacological research*.
  - **PMID:35011645** – Park J, Kim SW, Cho MC (2021 Dec 28). "The Role of LIM Kinase in the Male Urogenital System." *Cells*.

### Literature Assessment
- **Total:** Very high – REJECTED (150 strict, 286 broad).
- **Novelty score:** 0/10.
- **TE-relevance in literature:** No publications directly link LIMK2 to TE regulation.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P53671-F1, v6
- **mean pLDDT: 76.2 (>90: 34.0%, 70-90: 37.5%, 50-70: 13.0%, <50: 15.5%)**
- **Assessment:** Moderate confidence

### Experimental PDB Structures
- **7 structures:** 1X6A (NMR, -); 4TPT (X-ray, 2.60 A); 5NXD (X-ray, 1.90 A); 7QHG (X-ray, 1.45 A); 8GI4 (X-ray, 2.06 A); 8S3X (X-ray, 2.59 A); 8WSW (X-ray, 2.50 A)

### Structural Assessment
- PAE images were not locally generated or reliably fetched for this cycle. Structural judgment based on AlphaFold pLDDT statistics and available PDB structures.
- Score: 24/30.

---

## PPI Network

### STRING
- **CFL1** (score: 0.995)
- **CFL2** (score: 0.99)
- **ROCK1** (score: 0.967)
- **LIMK1** (score: 0.962)
- **PAK4** (score: 0.943)


### IntAct
- Total: 15 interactors
- **A0A0G2RMD1** (psi-mi:"MI:0398"(two hybrid pooling approach), imex:IM-13779|pubmed:20711500)
- **EBI-1380405** (psi-mi:"MI:0096"(pull down), pubmed:17721511|imex:IM-19952)
- **EBI-1380984** (psi-mi:"MI:0096"(pull down), pubmed:17721511|imex:IM-19952)
- **HSP90AB1** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-17906|pubmed:22939624|psi-mi:"MI)
- **ATP5F1E** (psi-mi:"MI:0030"(cross-linking study), pubmed:30021884|imex:IM-26653|doi:10.107)
- **TRIM35** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)
- **SLC18A1** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)
- **UNC119** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)


### PPI Network Assessment
- Network size: Moderate.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
LIMK2 was likely auto-rejected due to: PubMed>100

### Recheck Analysis
1. **HPA:** Nucleoplasm
2. **UniProt:** Experimental nuclear evidence present (ECO:0000269)
3. **GO-CC:** Nuclear/chromatin GO terms present
4. **PubMed:** 150 strict – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT** under the PubMed>100 rule. However, functional evidence may warrant exception review.

**REMAINS REJECTED** per pipeline rules. Exception review recommended if waiver criteria exist.

---

## TE-Regulator Relevance Reasoning

**HIGH relevance.** LIMK2 has functional features directly relevant to TE regulation .

---

## Final Decision

**DECISION: REJECTED (PubMed>100)**

**Score: 104/180.**

**Reasoning:** LIMK2 exceeds the published rejection threshold (PubMed>100 = 150 publications). While functional evidence may be relevant to TE biology, the gene meets exclusion criteria and should remain rejected unless exception waivers are applied.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 – exception review recommended*

This gene exceeds the automated rejection threshold (PubMed>100). While functional evidence is relevant to TE biology, pipeline rules dictate exclusion. If exception or waiver processes are available, this gene should be prioritized for reconsideration based on its functional profile.
