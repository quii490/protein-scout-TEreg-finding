# INPP5E – Critical False-Rejection Reevaluation Report

**Gene:** INPP5E
**UniProt Accession:** Q9NRR6
**Protein Name:** Phosphatidylinositol polyphosphate 5-phosphatase type IV
**Length:** 644 aa | **Mass:** 70.2 kDa
**Aliases:** None
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 13 | HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Uncertain. | UniProt: Nucleus (ECO:0000250, non-experimental) | GO-CC: GO:GO:0005634 (nucleus, ISS:UniProtKB) |
| 2. Protein Size | 10 | 8 | 644 aa / 70.2 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 101. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 20 | mean pLDDT: 71.2 (>90: 49.5%, 70-90: 5.1%, 50-70: 5.7%, <50: 39.6%). PDB: 1 structures. |
| 5. Regulatory Domains | 50 | 10 | No direct transcription function. No chromatin association. No epigenetic activity. No nucleic acid binding. |
| 6. PPI Network | 50 | 13 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 3 interactors. |
| **TOTAL** | **180** | **64** | **NOTE: REJECTED – PubMed>100 (strict=101)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Uncertain
- **Main Location:** Golgi apparatus
- **Additional:** Nucleoplasm, Focal adhesion sites
- **IF Image Status:** if_display_images_available
- **Key Finding:** Golgi apparatus

**Interpretation note:** HPA IF images available but not displayed in this review.

### UniProt Subcellular Location
- **Cytoplasm, cytoskeleton, cilium axoneme** – Evidence: ECO:0000269, ECO:0000269, ECO:0000269
- **Golgi apparatus, Golgi stack membrane** – Evidence: ECO:0000250
- **Cell membrane** – Evidence: ECO:0000250
- **Cell projection, ruffle** – Evidence: ECO:0000250
- **Cytoplasm** – Evidence: ECO:0000250
- **Nucleus** – Evidence: ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0005930 (axoneme)** – Evidence: IDA:UniProtKB
- **GO:0005929 (cilium)** – Evidence: TAS:Reactome
- **GO:0005829 (cytosol)** – Evidence: TAS:Reactome
- **GO:0005794 (Golgi apparatus)** – Evidence: IBA:GO_Central
- **GO:0032580 (Golgi cisterna membrane)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0000139 (Golgi membrane)** – Evidence: IEA:Ensembl
- **GO:0005634 (nucleus)** – Evidence: ISS:UniProtKB
- **GO:0005886 (plasma membrane)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0001726 (ruffle)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
Phosphatidylinositol (PtdIns) phosphatase that specifically hydrolyzes the 5-phosphate of phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3), phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) and phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2) (By similarity) (PubMed:10764818). Specific for lipid substrates, inactive towards water soluble inositol phosphates (PubMed:10764818). Plays an essential role in the primary cilium by controlling ciliary growth and phosphoinositide 3-kin

**Summary:** HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Uncertain. | UniProt: Nucleus (ECO:0000250, non-experimental) | GO-CC: GO:GO:0005634 (nucleus, ISS:UniProtKB)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 101 |
| Broad (All Fields) | 149 |



**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:20301500** – Adam MP, Bick S, Mirzaa GM (1993). "Joubert Syndrome." **.
  - **PMID:29140789** – Kösling SK, Fansa EK, Maffini S (2018 Feb 23). "Mechanism and dynamics of INPP5E transport into and inside the ciliary compartment." *Biological chemistry*.
  - **PMID:39871753** – Gupta M, Lewis TR, Stuck MW (2025 Feb 15). "Inpp5e is crucial for photoreceptor outer segment maintenance." *Journal of cell science*.
  - **PMID:38285286** – Wang X, Yu J, Yue H (2024 Sep). "Inpp5e Regulated the Cilium-Related Genes Contributing to the Neural Tube Defects Under 5-Fluorouracil Exposure." *Molecular neurobiology*.
  - **PMID:37670137** – Chiu TY, Lo CH, Lin YH (2023 Sep 5). "INPP5E regulates CD3ζ enrichment at the immune synapse by phosphoinositide distribution control." *Communications biology*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (101 strict, 149 broad).
- **Novelty score:** 0/10.
- **No publications directly linking INPP5E to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NRR6-F1, version 6
- **mean pLDDT: 71.2 (>90: 49.5%, 70-90: 5.1%, 50-70: 5.7%, <50: 39.6%)**
- **Assessment:** Moderate confidence.

### Experimental PDB Structures
- **1 structures available:** 2XSW (X-ray, 1.90 A)

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **PDE6D** (score: 0.98)
- **ARL13B** (score: 0.956)
- **PIP5K1B** (score: 0.944)
- **INPP4A** (score: 0.943)
- **PIP5K1C** (score: 0.939)

### IntAct
- Total: 15 validated interactors
- **BMPR2** (psi-mi:"MI:0096"(pull down), pubmed:15188402)
- **-** (psi-mi:"MI:0018"(two hybrid), pubmed:14605208|imex:IM-16524|mint:MINT-)
- **"BEST:LD39762"** (psi-mi:"MI:0018"(two hybrid), pubmed:14605208|imex:IM-16524|mint:MINT-)
- **bdg** (psi-mi:"MI:0018"(two hybrid), pubmed:14605208|imex:IM-16524|mint:MINT-)
- **MARK2** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-12079|pubmed:19615732)
- **YWHAH** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)
- **YWHAB** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)
- **CA5A** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
INPP5E was likely auto-rejected due to: PubMed>100 (strict=101)

### Recheck Analysis
1. **HPA Evidence:** Golgi apparatus
2. **UniProt Evidence:** Weak or no experimental nuclear evidence
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 101 strict, 149 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=101) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

INPP5E has indirect TE-regulatory relevance at best. The protein primarily functions in processes not directly related to TE biology.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=101))**

Score: 64/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** INPP5E exceeds the PubMed>100 rejection threshold (101 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
