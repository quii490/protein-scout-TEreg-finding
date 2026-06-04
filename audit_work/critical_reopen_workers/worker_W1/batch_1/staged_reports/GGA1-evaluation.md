# GGA1 – Critical False-Rejection Reevaluation Report

**Gene:** GGA1
**UniProt Accession:** Q9UJY5
**Protein Name:** ADP-ribosylation factor-binding protein GGA1
**Length:** 639 aa | **Mass:** 70.4 kDa
**Aliases:** None
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 14 | HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Supported. | UniProt: No nuclear annotation in UniProt | GO-CC: GO:GO:0005654 (nucleoplasm, IDA) |
| 2. Protein Size | 10 | 8 | 639 aa / 70.4 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 120. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 26 | mean pLDDT: 73.5 (>90: 44.6%, 70-90: 19.6%, 50-70: 7.2%, <50: 28.6%). PDB: 20 structures. |
| 5. Regulatory Domains | 50 | 20 | No direct transcription function. No chromatin association. Epigenetic modification: yes. No nucleic acid binding. |
| 6. PPI Network | 50 | 17 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 30 interactors. |
| **TOTAL** | **180** | **85** | **NOTE: REJECTED – PubMed>100 (strict=120)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Golgi apparatus, Vesicles
- **Additional:** Nucleoplasm
- **IF Image Status:** no_image_detected
- **Key Finding:** Golgi apparatus, Vesicles

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

### UniProt Subcellular Location
- **Golgi apparatus, trans-Golgi network membrane** – Evidence: ECO:0000269
- **Endosome membrane** – Evidence: ECO:0000269
- **Early endosome membrane** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IEA:GOC
- **GO:0005769 (early endosome)** – Evidence: IDA:UniProtKB
- **GO:0031901 (early endosome membrane)** – Evidence: TAS:Reactome
- **GO:0010008 (endosome membrane)** – Evidence: TAS:Reactome
- **GO:0005794 (Golgi apparatus)** – Evidence: IDA:HPA
- **GO:0016020 (membrane)** – Evidence: HDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0032991 (protein-containing complex)** – Evidence: IMP:CAFA
- **GO:0005802 (trans-Golgi network)** – Evidence: IBA:GO_Central

### Functional Context
Plays a role in protein sorting and trafficking between the trans-Golgi network (TGN) and endosomes. Mediates the ARF-dependent recruitment of clathrin to the TGN and binds ubiquitinated proteins and membrane cargo molecules with a cytosolic acidic cluster-dileucine (DXXLL) motif (PubMed:11301005, PubMed:15886016). Mediates export of the GPCR receptor ADRA2B to the cell surface (PubMed:27901063). Required for targeting PKD1:PKD2 complex from the trans-Golgi network to the cilium membrane (By sim

**Summary:** HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Supported. | UniProt: No nuclear annotation in UniProt | GO-CC: GO:GO:0005654 (nucleoplasm, IDA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 120 |
| Broad (All Fields) | 202 |



**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:31659673** – Uemura T, Waguri S (2020 Jan). "Emerging roles of Golgi/endosome-localizing monomeric clathrin adaptors GGAs." *Anatomical science international*.
  - **PMID:39002678** – Ma L, Kasula RK, Ouyang Q (2024 Aug). "GGA1 interacts with the endosomal Na+/H+ exchanger NHE6 governing localization to the endosome compartment." *The Journal of biological chemistry*.
  - **PMID:26446839** – Tewari R, Bachert C, Linstedt AD (2015 Dec 1). "Induced oligomerization targets Golgi proteins for degradation in lysosomes." *Molecular biology of the cell*.
  - **PMID:22836275** – Walker KR, Kang EL, Whalen MJ (2012 Jul 25). "Depletion of GGA1 and GGA3 mediates postinjury elevation of BACE1." *The Journal of neuroscience : the official journal of the Society for Neuroscience*.
  - **PMID:37551344** – Jiao H, Chen Y, Han T (2023). "GGA1 participates in spermatogenesis in mice under stress." *PeerJ*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (120 strict, 202 broad).
- **Novelty score:** 0/10.
- **No publications directly linking GGA1 to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9UJY5-F1, version 6
- **mean pLDDT: 73.5 (>90: 44.6%, 70-90: 19.6%, 50-70: 7.2%, <50: 28.6%)**
- **Assessment:** Moderate confidence.

### Experimental PDB Structures
- **20 structures available:** 1J2J (X-ray, 1.60 A); 1JWF (X-ray, 2.10 A); 1JWG (X-ray, 2.00 A); 1NA8 (X-ray, 2.30 A); 1NAF (X-ray, 2.80 A); 1NWM (X-ray, 2.40 A); 1O3X (X-ray, 2.10 A); 1OM9 (X-ray, 2.50 A); 1OXZ (X-ray, 2.80 A); 1PY1 (X-ray, 2.60 A) ... +10 more

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **RABEP1** (score: 0.997)
- **ARF1** (score: 0.996)
- **IGF2R** (score: 0.994)
- **CCDC91** (score: 0.989)
- **GGA2** (score: 0.987)

### IntAct
- Total: 15 validated interactors
- **RABEP1** (psi-mi:"MI:0114"(x-ray crystallography), pubmed:15457209)
- **ARF1** (psi-mi:"MI:0018"(two hybrid), pubmed:15143060)
- **TSG101** (psi-mi:"MI:0018"(two hybrid), pubmed:15143060)
- **UBB** (psi-mi:"MI:0018"(two hybrid), pubmed:15143060)
- **RABGEF1** (psi-mi:"MI:0096"(pull down), pubmed:12505986)
- **SSA1** (psi-mi:"MI:0676"(tandem affinity purification), pubmed:16429126)
- **SSA2** (psi-mi:"MI:0676"(tandem affinity purification), pubmed:16429126)
- **SSB1** (psi-mi:"MI:0676"(tandem affinity purification), pubmed:16429126)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
GGA1 was likely auto-rejected due to: PubMed>100 (strict=120)

### Recheck Analysis
1. **HPA Evidence:** Golgi apparatus, Vesicles
2. **UniProt Evidence:** Weak or no experimental nuclear evidence
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 120 strict, 202 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=120) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

GGA1 has limited direct evidence for TE regulation but possesses relevant functional features worth investigating.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=120))**

Score: 85/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** GGA1 exceeds the PubMed>100 rejection threshold (120 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
