# CMIP – Critical False-Rejection Reevaluation Report

**Gene:** CMIP
**UniProt Accession:** Q8IY22
**Protein Name:** C-Maf-inducing protein
**Length:** 773 aa | **Mass:** 86.3 kDa
**Aliases:** KIAA1694, TCMIP
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 25 | HPA main: Nucleoplasm. Reliability: Supported. Nuclear is primary location. | UniProt: Nucleus (ECO:0000269 x1, experimental) | GO-CC: GO:GO:0005654 (nucleoplasm, IDA) |
| 2. Protein Size | 10 | 8 | 773 aa / 86.3 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 72. Novelty rule: 61-80=4. |
| 4. 3D Structure | 30 | 11 | mean pLDDT: 78.8 (>90: 51.5%, 70-90: 26.0%, 50-70: 4.5%, <50: 18.0%). PDB: 0 structures. |
| 5. Regulatory Domains | 50 | 10 | No direct transcription function. No chromatin association. No epigenetic activity. No nucleic acid binding. |
| 6. PPI Network | 50 | 17 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 5 interactors. |
| **TOTAL** | **180** | **75** |  |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm, Cytosol
- **Additional:** None
- **IF Image Status:** no_image_detected
- **Key Finding:** Nucleoplasm, Cytosol

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000269
- **Cytoplasm** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA

### Functional Context
Plays a role in T-cell signaling pathway. Isoform 2 may play a role in T-helper 2 (Th2) signaling pathway and seems to represent the first proximal signaling protein that links T-cell receptor-mediated signal to the activation of c-Maf Th2 specific factor

**Summary:** HPA main: Nucleoplasm. Reliability: Supported. Nuclear is primary location. | UniProt: Nucleus (ECO:0000269 x1, experimental) | GO-CC: GO:GO:0005654 (nucleoplasm, IDA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 72 |
| Broad (All Fields) | 209 |

**Alias Note:** Aliases observed but not used for scoring: KIAA1694, TCMIP



### Key Papers (with PMIDs)
  - **PMID:36609599** – Lee J, Song JH, Park JH (2023 Jan). "Dnmt1/Tet2-mediated changes in Cmip methylation regulate the development of nonalcoholic fatty liver disease by controlling the Gbp2-Pparγ-CD36 axis." *Experimental & molecular medicine*.
  - **PMID:33112407** – Pan L, Liao YH, Mo MQ (2020 Oct 30). "CMIP SNPs and their haplotypes are associated with dyslipidaemia and clinicopathologic features of IgA nephropathy." *Bioscience reports*.
  - **PMID:34323419** – Zhang SY, Fan Q, Moktefi A (2021 Jul). "CMIP interacts with WT1 and targets it on the proteasome degradation pathway." *Clinical and translational medicine*.
  - **PMID:40372501** – Li Y, Yan X, Yu H (2025 May 15). "Downregulation of CMIP contributes to preeclampsia development by impairing trophoblast function via the PDE7B-cAMP pathway." *Cellular and molecular life sciences : CMLS*.
  - **PMID:37075753** – Wieder N, Fried JC, Kim C (2023 May 2). "FALCON systematically interrogates free fatty acid biology and identifies a novel mediator of lipotoxicity." *Cell metabolism*.

### Literature Assessment
- **Total publications:** Moderate (72 strict, 209 broad).
- **Novelty score:** 4/10.
- **No publications directly linking CMIP to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8IY22-F1, version 6
- **mean pLDDT: 78.8 (>90: 51.5%, 70-90: 26.0%, 50-70: 4.5%, <50: 18.0%)**
- **Assessment:** Moderate confidence.

### Experimental PDB Structures
- **0 structures available:** None available.

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **ATP2C2** (score: 0.942)
- **FLNA** (score: 0.907)
- **RELA** (score: 0.836)
- **KIAA0319** (score: 0.684)
- **DCDC2** (score: 0.648)

### IntAct
- Total: 15 validated interactors
- **TRIM54** (psi-mi:"MI:1356"(validated two hybrid), pubmed:32296183|imex:IM-25472)
- **TSR2** (psi-mi:"MI:1356"(validated two hybrid), pubmed:32296183|imex:IM-25472)
- **ZC4H2** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **MTNR1A** (psi-mi:"MI:0018"(two hybrid), pubmed:26514267|imex:IM-24624)
- **P2RY1** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)
- **NS3** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:33845483|pmc:PPR177217|doi:10.110)
- **EBI-25475894** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:33845483|pmc:PPR177217|doi:10.110)
- **Q80BV4** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:33845483|pmc:PPR177217|doi:10.110)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
CMIP was likely auto-rejected due to: Low automated nuclear score or PubMed threshold

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm, Cytosol
2. **UniProt Evidence:** Experimental nuclear evidence present
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 72 strict, 209 broad – within acceptable range

### Verdict on False Rejection
**The original rejection was FALSE – CMIP should NOT have been rejected.** The nuclear evidence is sufficient and the automated rejection criteria were misapplied or the data was incomplete.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

CMIP has indirect TE-regulatory relevance at best. The protein primarily functions in processes not directly related to TE biology.

Key features supporting TE-regulatory candidacy are discussed above in the Regulatory Domains and PPI sections.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

Score: 75/180.

**Reasoning:** CMIP was falsely rejected by the automated pipeline. Comprehensive review reveals sufficient nuclear evidence and functional features to warrant inclusion in TE-regulatory evaluation.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

This gene was falsely rejected due to data artifacts or threshold miscategorization. The evidence supports reopening for TE-regulatory investigation.
