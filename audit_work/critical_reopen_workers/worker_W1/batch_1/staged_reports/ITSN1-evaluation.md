# ITSN1 – Critical False-Rejection Reevaluation Report

**Gene:** ITSN1
**UniProt Accession:** Q15811
**Protein Name:** Intersectin-1
**Length:** 1721 aa | **Mass:** 195.4 kDa
**Aliases:** ITSN, SH3D1A
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 17 | HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Supported. | UniProt: Nucleus envelope (ECO:0000269 x1, experimental) | GO-CC: GO:GO:0005635 (nuclear envelope, IDA) |
| 2. Protein Size | 10 | 8 | 1721 aa / 195.4 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 105. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 26 | mean pLDDT: 72.3 (>90: 33.2%, 70-90: 33.6%, 50-70: 9.0%, <50: 24.2%). PDB: 11 structures. |
| 5. Regulatory Domains | 50 | 20 | No direct transcription function. No chromatin association. Epigenetic modification: yes. No nucleic acid binding. |
| 6. PPI Network | 50 | 21 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 16 interactors. |
| **TOTAL** | **180** | **92** | **NOTE: REJECTED – PubMed>100 (strict=105)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Plasma membrane
- **Additional:** Nucleoplasm
- **IF Image Status:** if_display_images_available
- **Key Finding:** Plasma membrane

**Interpretation note:** HPA IF images available but not displayed in this review.

### UniProt Subcellular Location
- **Endomembrane system** – Evidence: ECO:0000269
- **Synapse, synaptosome** – Evidence: ECO:0000250
- **Cell projection, lamellipodium** – Evidence: ECO:0000269
- **Cell membrane** – Evidence: ECO:0000269, ECO:0000269
- **Membrane, clathrin-coated pit** – Evidence: ECO:0000269, ECO:0000269
- **Recycling endosome** – Evidence: ECO:0000269
- **Endosome** – Evidence: ECO:0000250
- **Cytoplasmic vesicle** – Evidence: ECO:0000250
- **Cytoplasm** – Evidence: ECO:0000269
- **Endomembrane system** – Evidence: ECO:0000269
- **Nucleus envelope** – Evidence: ECO:0000269
- **Endomembrane system** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0097440 (apical dendrite)** – Evidence: IEA:Ensembl
- **GO:0005905 (clathrin-coated pit)** – Evidence: IDA:UniProtKB
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB
- **GO:0005829 (cytosol)** – Evidence: TAS:Reactome
- **GO:0043197 (dendritic spine)** – Evidence: IEA:Ensembl
- **GO:0098978 (glutamatergic synapse)** – Evidence: IEA:Ensembl
- **GO:0097708 (intracellular vesicle)** – Evidence: IBA:GO_Central
- **GO:0030027 (lamellipodium)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0043025 (neuronal cell body)** – Evidence: IEA:Ensembl
- **GO:0005635 (nuclear envelope)** – Evidence: IDA:UniProtKB
- **GO:0005886 (plasma membrane)** – Evidence: IDA:HPA
- **GO:0098871 (postsynaptic actin cytoskeleton)** – Evidence: IEA:Ensembl
- **GO:0098843 (postsynaptic endocytic zone)** – Evidence: IEA:Ensembl
- **GO:0042734 (presynaptic membrane)** – Evidence: IBA:GO_Central
- **GO:0055037 (recycling endosome)** – Evidence: IEA:UniProtKB-SubCell

### Functional Context
Adapter protein that provides a link between the endocytic membrane traffic and the actin assembly machinery (PubMed:11584276, PubMed:29887380). Acts as a guanine nucleotide exchange factor (GEF) for CDC42, and thereby stimulates actin nucleation mediated by WASL and the ARP2/3 complex (PubMed:11584276). Plays a role in the assembly and maturation of clathrin-coated vesicles (By similarity). Recruits FCHSD2 to clathrin-coated pits (PubMed:29887380). Involved in endocytosis of activated EGFR, and

**Summary:** HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Supported. | UniProt: Nucleus envelope (ECO:0000269 x1, experimental) | GO-CC: GO:GO:0005635 (nuclear envelope, IDA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 105 |
| Broad (All Fields) | 163 |

**Alias Note:** Aliases observed but not used for scoring: ITSN, SH3D1A

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:34707297** – Bruel AL, Vitobello A, Thiffault I (2022 Jan). "ITSN1: a novel candidate gene involved in autosomal dominant neurodevelopmental disorder spectrum." *European journal of human genetics : EJHG*.
  - **PMID:39580802** – Jin M, Iwamoto Y, Shirazinejad C (2024 Dec 24). "Intersectin1 promotes clathrin-mediated endocytosis by organizing and stabilizing endocytic protein interaction networks." *Cell reports*.
  - **PMID:39383250** – Yang YM, Fekete A, Arsenault J (2025 Oct). "Intersectin-1 enhances calcium-dependent replenishment of the readily releasable pool of synaptic vesicles during development." *The Journal of physiology*.
  - **PMID:36171198** – Lan C, Zhang H, Wang K (2022 Sep 28). "The alternative splicing of intersectin 1 regulated by PTBP1 promotes human glioma progression." *Cell death & disease*.
  - **PMID:38241230** – Sowndharya S, Rajan KE (2024). "Environmental enrichment improves social isolation-induced memory impairment: The possible role of ITSN1-Reelin-AMPA receptor signaling pathway." *PloS one*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (105 strict, 163 broad).
- **Novelty score:** 0/10.
- **No publications directly linking ITSN1 to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q15811-F1, version 6
- **mean pLDDT: 72.3 (>90: 33.2%, 70-90: 33.6%, 50-70: 9.0%, <50: 24.2%)**
- **Assessment:** Moderate confidence.

### Experimental PDB Structures
- **11 structures available:** 1KI1 (X-ray, 2.30 A); 2KGR (NMR, -); 2KHN (NMR, -); 3FIA (X-ray, 1.45 A); 3QBV (X-ray, 2.65 A); 4IIM (X-ray, 1.80 A); 5HZI (X-ray, 2.60 A); 5HZJ (X-ray, 2.60 A); 5HZK (X-ray, 3.30 A); 6GBU (X-ray, 3.44 A) ... +1 more

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **CDC42** (score: 0.999)
- **WASL** (score: 0.999)
- **FCHO1** (score: 0.999)
- **EPS15** (score: 0.997)
- **AP2B1** (score: 0.992)

### IntAct
- Total: 15 validated interactors
- **CDC42** (psi-mi:"MI:0114"(x-ray crystallography), pubmed:12006984)
- **EEF1A1** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **KIF5A** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **UNC119** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **MRPL20** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **SNX5** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **SMARCC2** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **DISC1** (psi-mi:"MI:0018"(two hybrid), pubmed:12812986|imex:IM-19614)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Some chromatin/transcription interactors identified

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
ITSN1 was likely auto-rejected due to: PubMed>100 (strict=105)

### Recheck Analysis
1. **HPA Evidence:** Plasma membrane
2. **UniProt Evidence:** Experimental nuclear evidence present
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 105 strict, 163 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=105) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

ITSN1 has limited direct evidence for TE regulation but possesses relevant functional features worth investigating.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=105))**

Score: 92/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** ITSN1 exceeds the PubMed>100 rejection threshold (105 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
