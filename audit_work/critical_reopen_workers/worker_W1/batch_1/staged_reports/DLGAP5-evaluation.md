# DLGAP5 – Critical False-Rejection Reevaluation Report

**Gene:** DLGAP5
**UniProt Accession:** Q15398
**Protein Name:** Disks large-associated protein 5
**Length:** 846 aa | **Mass:** 95.1 kDa
**Aliases:** DLG7, KIAA0008
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 8 | HPA: Cytosol. NO nuclear annotation from HPA. Reliability: Supported. | UniProt: Nucleus (no evidence code) | GO-CC: GO:GO:0005634 (nucleus, IDA) |
| 2. Protein Size | 10 | 8 | 846 aa / 95.1 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 204. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 18 | mean pLDDT: 55.6 (>90: 16.4%, 70-90: 11.0%, 50-70: 11.8%, <50: 60.8%). PDB: 4 structures. |
| 5. Regulatory Domains | 50 | 20 | No direct transcription function. No chromatin association. Epigenetic modification: yes. No nucleic acid binding. |
| 6. PPI Network | 50 | 13 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 3 interactors. |
| **TOTAL** | **180** | **67** | **NOTE: REJECTED – PubMed>100 (strict=204)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **Additional:** Mitotic spindle
- **IF Image Status:** if_display_images_available
- **Key Finding:** Cytosol

**Interpretation note:** HPA IF images available but not displayed in this review.

### UniProt Subcellular Location
- **Nucleus** – Evidence: 
- **Cytoplasm** – Evidence: 
- **Cytoplasm, cytoskeleton, spindle** – Evidence: 

### GO Cellular Component (GO-CC)
- **GO:0005737 (cytoplasm)** – Evidence: IBA:GO_Central
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0072686 (mitotic spindle)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0031616 (spindle pole centrosome)** – Evidence: IDA:UniProtKB

### Functional Context
Potential cell cycle regulator that may play a role in carcinogenesis of cancer cells. Mitotic phosphoprotein regulated by the ubiquitin-proteasome pathway. Key regulator of adherens junction integrity and differentiation that may be involved in CDH1-mediated adhesion and signaling in epithelial cells

**Summary:** HPA: Cytosol. NO nuclear annotation from HPA. Reliability: Supported. | UniProt: Nucleus (no evidence code) | GO-CC: GO:GO:0005634 (nucleus, IDA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 204 |
| Broad (All Fields) | 271 |

**Alias Note:** Aliases observed but not used for scoring: DLG7, KIAA0008

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:38414025** – Chen M, Zhang S, Wang F (2024 Feb 27). "DLGAP5 promotes lung adenocarcinoma growth via upregulating PLK1 and serves as a therapeutic target." *Journal of translational medicine*.
  - **PMID:39990228** – Deng Z, Zhou F, Li M (2025). "DLGAP5 enhances bladder cancer chemoresistance by regulating glycolysis through MYC stabilization." *Theranostics*.
  - **PMID:41516135** – Alvarado-Camacho DA, Castillo-Velázquez R, Granados-López AJ (2025 Dec 26). "Differentially Expressed Genes Associated with the Development of Cervical Cancer." *International journal of molecular sciences*.
  - **PMID:40944860** – Chen F, Luo Y, Lv F (2025 Sep 13). "DLGAP5 facilitates glioblastoma growth and tumor-associated macrophage M2 polarization." *Journal of molecular histology*.
  - **PMID:40796344** – Hu H, Wan X, Sun J (2025 Oct 1). "Biallelic variants in DLGAP5 cause spindle assembly defects and human early embryonic arrest." *Human reproduction (Oxford, England)*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (204 strict, 271 broad).
- **Novelty score:** 0/10.
- **No publications directly linking DLGAP5 to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q15398-F1, version 6
- **mean pLDDT: 55.6 (>90: 16.4%, 70-90: 11.0%, 50-70: 11.8%, <50: 60.8%)**
- **Assessment:** Very low confidence – significant predicted disorder.

### Experimental PDB Structures
- **4 structures available:** 7ZX4 (X-ray, 2.08 A); 8X9P (EM, 3.54 A); 9DHZ (EM, 3.10 A); 9DUQ (EM, 2.80 A)

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **HMMR** (score: 0.999)
- **CEP55** (score: 0.999)
- **KIF11** (score: 0.997)
- **ASPM** (score: 0.994)
- **BUB1** (score: 0.986)

### IntAct
- Total: 15 validated interactors
- **TRAF2** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16189514|imex:IM-16520|mint:MINT-)
- **TRIM37** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16189514|imex:IM-16520|mint:MINT-)
- **FRMD8P1** (psi-mi:"MI:0030"(cross-linking study), pubmed:30021884|imex:IM-26653|doi:10.107)
- **H2BC9** (psi-mi:"MI:0030"(cross-linking study), pubmed:30021884|imex:IM-26653|doi:10.107)
- **RCN1** (psi-mi:"MI:0030"(cross-linking study), pubmed:30021884|imex:IM-26653|doi:10.107)
- **GOLGA2** (psi-mi:"MI:0397"(two hybrid array), imex:IM-27438|doi:10.1038/s41467-019-119)
- **B2M** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)
- **KPNB1** (psi-mi:"MI:0096"(pull down), pubmed:28330616|imex:IM-25671)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
DLGAP5 was likely auto-rejected due to: PubMed>100 (strict=204)

### Recheck Analysis
1. **HPA Evidence:** Cytosol
2. **UniProt Evidence:** Weak or no experimental nuclear evidence
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 204 strict, 271 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=204) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

DLGAP5 has limited direct evidence for TE regulation but possesses relevant functional features worth investigating.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=204))**

Score: 67/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** DLGAP5 exceeds the PubMed>100 rejection threshold (204 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
