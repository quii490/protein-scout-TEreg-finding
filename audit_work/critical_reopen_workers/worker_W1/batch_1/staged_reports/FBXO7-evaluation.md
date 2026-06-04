# FBXO7 – Critical False-Rejection Reevaluation Report

**Gene:** FBXO7
**UniProt Accession:** Q9Y3I1
**Protein Name:** F-box only protein 7
**Length:** 522 aa | **Mass:** 58.5 kDa
**Aliases:** FBX7
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 30 | HPA main: Nucleoplasm. Reliability: Supported. Nuclear is primary location. | UniProt: Nucleus (ECO:0000269 x3, experimental) | GO-CC: GO:GO:0005654 (nucleoplasm, IDA); GO:GO:0005634 (nucleus, IDA) |
| 2. Protein Size | 10 | 8 | 522 aa / 58.5 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 132. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 20 | mean pLDDT: 66.4 (>90: 12.8%, 70-90: 41.4%, 50-70: 12.5%, <50: 33.3%). PDB: 2 structures. |
| 5. Regulatory Domains | 50 | 20 | No direct transcription function. No chromatin association. Epigenetic modification: yes. No nucleic acid binding. |
| 6. PPI Network | 50 | 13 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 0 interactors. |
| **TOTAL** | **180** | **91** | **NOTE: REJECTED – PubMed>100 (strict=132)** |

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
- **Cytoplasm** – Evidence: ECO:0000269, ECO:0000269
- **Nucleus** – Evidence: ECO:0000269, ECO:0000269, ECO:0000269
- **Mitochondrion** – Evidence: ECO:0000269
- **Cytoplasm, cytosol** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0097414 (classical Lewy body)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0005737 (cytoplasm)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0097409 (glial cytoplasmic inclusion)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:1990037 (Lewy body core)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:1990038 (Lewy body corona)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0097462 (Lewy neurite)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0005739 (mitochondrion)** – Evidence: IDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0032991 (protein-containing complex)** – Evidence: IDA:LIFEdb
- **GO:0019005 (SCF ubiquitin ligase complex)** – Evidence: IDA:UniProtKB
- **GO:0000151 (ubiquitin ligase complex)** – Evidence: IDA:UniProtKB

### Functional Context
Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins and plays a role in several biological processes such as cell cycle, cell proliferation, or maintenance of chromosome stability (PubMed:15145941, PubMed:34791250). Recognizes and ubiquitinates BIRC2 and the cell cycle regulator DLGAP5 (PubMed:15145941, PubMed:16510124, PubMed:22212761). Plays a role down

**Summary:** HPA main: Nucleoplasm. Reliability: Supported. Nuclear is primary location. | UniProt: Nucleus (ECO:0000269 x3, experimental) | GO-CC: GO:GO:0005654 (nucleoplasm, IDA); GO:GO:0005634 (nucleus, IDA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 132 |
| Broad (All Fields) | 182 |

**Alias Note:** Aliases observed but not used for scoring: FBX7

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:35328025** – Jia F, Fellner A, Kumar KR (2022 Mar 7). "Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing." *Genes*.
  - **PMID:40583767** – Gong Y, Lu X, Wang X (2025 Jul 22). "Mitochondrial Tumor Suppressor 1A Attenuates Myocardial Infarction Injury by Maintaining the Coupling Between Mitochondria and Endoplasmic Reticulum." *Circulation*.
  - **PMID:38839752** – Luo L, Wu X, Fan J (2024 Jun 5). "FBXO7 ubiquitinates PRMT1 to suppress serine synthesis and tumor growth in hepatocellular carcinoma." *Nature communications*.
  - **PMID:38291374** – Li Y, Yu J, Li R (2024 Jan 30). "New insights into the role of mitochondrial metabolic dysregulation and immune infiltration in septic cardiomyopathy by integrated bioinformatics analysis and experimental validation." *Cellular & molecular biology letters*.
  - **PMID:32613234** – Zhao Y, Qin L, Pan H (2020 Jul 1). "The role of genetics in Parkinson's disease: a large cohort study in Chinese mainland population." *Brain : a journal of neurology*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (132 strict, 182 broad).
- **Novelty score:** 0/10.
- **No publications directly linking FBXO7 to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9Y3I1-F1, version 6
- **mean pLDDT: 66.4 (>90: 12.8%, 70-90: 41.4%, 50-70: 12.5%, <50: 33.3%)**
- **Assessment:** Low confidence.

### Experimental PDB Structures
- **2 structures available:** 4L9C (X-ray, 2.10 A); 4L9H (X-ray, 2.00 A)

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **SKP1** (score: 0.997)
- **PINK1** (score: 0.995)
- **CUL1** (score: 0.992)
- **PSMF1** (score: 0.976)
- **RBX1** (score: 0.965)

### IntAct
- Total: 15 validated interactors
- **CUL1** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:16278047)
- **SKP1** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:16278047)
- **SEC24C** (psi-mi:"MI:0397"(two hybrid array), imex:IM-15364|pubmed:21988832)
- **glpA** (psi-mi:"MI:0398"(two hybrid pooling approach), imex:IM-13779|pubmed:20711500)
- **RBBP6** (psi-mi:"MI:0018"(two hybrid), pubmed:18624398|imex:IM-19021)
- **COPS6** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), imex:IM-12079|pubmed:19615732)
- **COPS5** (psi-mi:"MI:0676"(tandem affinity purification), pubmed:21145461|imex:IM-18651|doi:10.101)
- **COPS2** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:28514442|doi:10.1038/nature22366|)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
FBXO7 was likely auto-rejected due to: PubMed>100 (strict=132)

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm, Cytosol
2. **UniProt Evidence:** Experimental nuclear evidence present
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 132 strict, 182 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=132) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

FBXO7 has limited direct evidence for TE regulation but possesses relevant functional features worth investigating.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=132))**

Score: 91/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** FBXO7 exceeds the PubMed>100 rejection threshold (132 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.
