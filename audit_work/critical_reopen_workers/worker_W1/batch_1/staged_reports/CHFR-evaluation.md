# CHFR – Critical False-Rejection Reevaluation Report

**Gene:** CHFR
**UniProt Accession:** Q96EP1
**Protein Name:** E3 ubiquitin-protein ligase CHFR
**Length:** 664 aa | **Mass:** 73.4 kDa
**Aliases:** RNF196
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA main: Nuclear bodies. Reliability: Uncertain. Nuclear is primary location. | UniProt: Nucleus, PML body (ECO:0000269 x3, experimental) | GO-CC: GO:GO:0005634 (nucleus, IDA) |
| 2. Protein Size | 10 | 8 | 664 aa / 73.4 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 207. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 24 | mean pLDDT: 72.0 (>90: 47.9%, 70-90: 14.2%, 50-70: 4.2%, <50: 33.7%). PDB: 6 structures. |
| 5. Regulatory Domains | 50 | 20 | No direct transcription function. No chromatin association. Epigenetic modification: yes. No nucleic acid binding. |
| 6. PPI Network | 50 | 17 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 4 interactors. |
| **TOTAL** | **180** | **97** | **NOTE: REJECTED – PubMed>100 (strict=207)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Uncertain
- **Main Location:** Nuclear bodies, Microtubules
- **Additional:** None
- **IF Image Status:** no_image_detected
- **Key Finding:** Nuclear bodies, Microtubules

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

### UniProt Subcellular Location
- **Nucleus, PML body** – Evidence: ECO:0000269, ECO:0000269, ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0016605 (PML body)** – Evidence: IDA:UniProtKB

### Functional Context
E3 ubiquitin-protein ligase that functions in the antephase checkpoint by actively delaying passage into mitosis in response to microtubule poisons. Acts in early prophase before chromosome condensation, when the centrosome move apart from each other along the periphery of the nucleus. Probably involved in signaling the presence of mitotic stress caused by microtubule poisons by mediating the 'Lys-48'-linked ubiquitination of target proteins, leading to their degradation by the proteasome. Promo

**Summary:** HPA main: Nuclear bodies. Reliability: Uncertain. Nuclear is primary location. | UniProt: Nucleus, PML body (ECO:0000269 x3, experimental) | GO-CC: GO:GO:0005634 (nucleus, IDA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 207 |
| Broad (All Fields) | 309 |

**Alias Note:** Aliases observed but not used for scoring: RNF196

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:34885153** – Wahner Hendrickson AE, Visscher DW, Hou X (2021 Nov 30). "CHFR and Paclitaxel Sensitivity of Ovarian Cancer." *Cancers*.
  - **PMID:18597043** – Brooks L 3rd, Heimsath EG Jr, Loring GL (2008 Nov). "FHA-RING ubiquitin ligases in cell division cycle control." *Cellular and molecular life sciences : CMLS*.
  - **PMID:40234721** – Wu W, Wu W, Xie X (2025 Jul). "DNMT1 is required for efficient DSB repair and maintenance of replication fork stability, and its loss reverses resistance to PARP inhibitors in cancer cells." *Oncogene*.
  - **PMID:24375389** – Derks S, Cleven AH, Melotte V (2014 Mar). "Emerging evidence for CHFR as a cancer biomarker: from tumor biology to precision medicine." *Cancer metastasis reviews*.
  - **PMID:27994471** – Shi H, Wang X, Wang J (2016). "Association between CHFR gene hypermethylation and gastric cancer risk: a meta-analysis." *OncoTargets and therapy*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (207 strict, 309 broad).
- **Novelty score:** 0/10.
- **No publications directly linking CHFR to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96EP1-F1, version 6
- **mean pLDDT: 72.0 (>90: 47.9%, 70-90: 14.2%, 50-70: 4.2%, <50: 33.7%)**
- **Assessment:** Moderate confidence.

### Experimental PDB Structures
- **6 structures available:** 1LGP (X-ray, 2.00 A); 1LGQ (X-ray, 2.10 A); 2XOC (X-ray, 1.89 A); 2XOY (X-ray, 2.60 A); 2XOZ (X-ray, 2.37 A); 2XP0 (X-ray, 1.98 A)

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **APLF** (score: 0.979)
- **PARP1** (score: 0.897)
- **APTX** (score: 0.83)
- **UBE2D2** (score: 0.825)
- **UBE2D3** (score: 0.792)

### IntAct
- Total: 15 validated interactors
- **EEF1G** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **BRD4** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **GABBR1** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **ITGAE** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **WDR47** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **UBE2E3** (psi-mi:"MI:0397"(two hybrid array), imex:IM-11696|pubmed:19549727)
- **UBE2D4** (psi-mi:"MI:0397"(two hybrid array), imex:IM-11696|pubmed:19549727)
- **UBE2W** (psi-mi:"MI:0397"(two hybrid array), imex:IM-11696|pubmed:19549727)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
CHFR was likely auto-rejected due to: PubMed>100 (strict=207)

### Recheck Analysis
1. **HPA Evidence:** Nuclear bodies, Microtubules
2. **UniProt Evidence:** Experimental nuclear evidence present
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 207 strict, 309 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=207) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

CHFR has limited direct evidence for TE regulation but possesses relevant functional features worth investigating.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=207))**

Score: 97/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** CHFR exceeds the PubMed>100 rejection threshold (207 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
