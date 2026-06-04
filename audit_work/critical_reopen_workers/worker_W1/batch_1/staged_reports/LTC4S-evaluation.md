# LTC4S – Critical False-Rejection Reevaluation Report

**Gene:** LTC4S
**UniProt Accession:** Q16873
**Protein Name:** Leukotriene C4 synthase
**Length:** 150 aa | **Mass:** 16.6 kDa
**Aliases:** None
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 30 | HPA main: Nucleoplasm. Reliability: Approved. Nuclear is primary location. | UniProt: Nucleus outer membrane (ECO:0000269 x1, experimental); Nucleus membrane (ECO:0000269 x1, experimental) | GO-CC: GO |
| 2. Protein Size | 10 | 10 | 150 aa / 16.6 kDa. Full marks. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 148. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 30 | mean pLDDT: 97.2 (>90: 95.3%, 70-90: 3.3%, 50-70: 1.3%, <50: 0.0%). PDB: 20 structures. |
| 5. Regulatory Domains | 50 | 10 | No direct transcription function. No chromatin association. No epigenetic activity. No nucleic acid binding. |
| 6. PPI Network | 50 | 13 | STRING: 15 partners. IntAct: 9 interactors. UniProt: 10 interactors. |
| **TOTAL** | **180** | **93** | **NOTE: REJECTED – PubMed>100 (strict=148)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional:** Endoplasmic reticulum, Cytosol
- **IF Image Status:** no_image_detected
- **Key Finding:** Nucleoplasm

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

### UniProt Subcellular Location
- **Nucleus outer membrane** – Evidence: ECO:0000269
- **Endoplasmic reticulum membrane** – Evidence: ECO:0000269, ECO:0000269
- **Nucleus membrane** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005783 (endoplasmic reticulum)** – Evidence: IDA:UniProtKB
- **GO:0005789 (endoplasmic reticulum membrane)** – Evidence: IDA:UniProtKB
- **GO:0043231 (intracellular membrane-bounded organelle)** – Evidence: TAS:ProtInc
- **GO:0016020 (membrane)** – Evidence: TAS:ProtInc
- **GO:0005635 (nuclear envelope)** – Evidence: IDA:UniProtKB
- **GO:0031965 (nuclear membrane)** – Evidence: IDA:UniProtKB
- **GO:0005640 (nuclear outer membrane)** – Evidence: IDA:UniProtKB

### Functional Context
Catalyzes the conjugation of leukotriene A4 with reduced glutathione (GSH) to form leukotriene C4 with high specificity (PubMed:23409838, PubMed:27365393, PubMed:27791009, PubMed:7937884, PubMed:9153254). Can also catalyze the transfer of a glutathionyl group from glutathione (GSH) to 13(S),14(S)-epoxy-docosahexaenoic acid to form maresin conjugate in tissue regeneration 1 (MCTR1), a bioactive lipid mediator that possess potent anti-inflammatory and proresolving actions (PubMed:27791009)

**Summary:** HPA main: Nucleoplasm. Reliability: Approved. Nuclear is primary location. | UniProt: Nucleus outer membrane (ECO:0000269 x1, experimental); Nucleus membrane (ECO:0000269 x1, experimental) | GO-CC: GO:GO:0005635 (nuclear envelope, IDA); GO:GO:0031965 (nuclear membrane, IDA); GO:GO:0005640 (nuclear o

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 148 |
| Broad (All Fields) | 214 |



**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:40640882** – Wu Y, Wei P, Li B (2025 Jul 10). "Temporal dynamics of the multi-omic response reveals the modulation of macrophage subsets post-myocardial infarction." *Journal of translational medicine*.
  - **PMID:22884858** – Zhang Y, Huang H, Huang J (2012 Aug). "The -444A/C polymorphism in the LTC4S gene and the risk of asthma: a meta-analysis." *Archives of medical research*.
  - **PMID:19077707** – Lima JJ, Blake KV, Tantisira KG (2009 Jan). "Pharmacogenetics of asthma." *Current opinion in pulmonary medicine*.
  - **PMID:39236243** – Nshimiyimana R, Simard M, Teder T (2024 Sep 10). "Biosynthesis of resolvin D1, resolvin D2, and RCTR1 from 7,8(S,S)-epoxytetraene in human neutrophils and macrophages." *Proceedings of the National Academy of Sciences of the United States of America*.
  - **PMID:25215090** – Wang GN, Zhang JS, Cao WJ (2013). "Association of ALOX5, LTA4H and LTC4S gene polymorphisms with ischemic stroke risk in a cohort of Chinese in east China." *World journal of emergency medicine*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (148 strict, 214 broad).
- **Novelty score:** 0/10.
- **No publications directly linking LTC4S to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q16873-F1, version 6
- **mean pLDDT: 97.2 (>90: 95.3%, 70-90: 3.3%, 50-70: 1.3%, <50: 0.0%)**
- **Assessment:** Exceptionally high confidence.

### Experimental PDB Structures
- **20 structures available:** 2PNO (X-ray, 3.30 A); 2UUH (X-ray, 2.15 A); 2UUI (X-ray, 2.00 A); 3B29 (X-ray, 3.20 A); 3HKK (X-ray, 2.90 A); 3LEO (X-ray, 2.10 A); 3PCV (X-ray, 1.90 A); 4BPM (X-ray, 2.08 A); 4J7T (X-ray, 3.20 A); 4J7Y (X-ray, 2.90 A) ... +10 more

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **LTA4H** (score: 0.992)
- **ALOX5** (score: 0.986)
- **CYSLTR1** (score: 0.946)
- **MGST1** (score: 0.932)
- **CYSLTR2** (score: 0.93)

### IntAct
- Total: 9 validated interactors
- **FXYD3** (psi-mi:"MI:1112"(two hybrid prey pooling approach), pubmed:32296183|imex:IM-25472)
- **TMEM52B** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **EBP** (psi-mi:"MI:1356"(validated two hybrid), pubmed:32296183|imex:IM-25472)
- **CD79A** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **SLC7A14** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **GPR152** (psi-mi:"MI:0397"(two hybrid array), pubmed:32296183|imex:IM-25472)
- **GPR42** (psi-mi:"MI:1356"(validated two hybrid), pubmed:32296183|imex:IM-25472)
- **FFAR3** (psi-mi:"MI:1356"(validated two hybrid), pubmed:32296183|imex:IM-25472)

### PPI Network Assessment
- Small interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
LTC4S was likely auto-rejected due to: PubMed>100 (strict=148)

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm
2. **UniProt Evidence:** Experimental nuclear evidence present
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 148 strict, 214 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=148) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

LTC4S has indirect TE-regulatory relevance at best. The protein primarily functions in processes not directly related to TE biology.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=148))**

Score: 93/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** LTC4S exceeds the PubMed>100 rejection threshold (148 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
