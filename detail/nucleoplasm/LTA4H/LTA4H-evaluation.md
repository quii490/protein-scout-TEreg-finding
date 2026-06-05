# LTA4H – Critical False-Rejection Reevaluation Report

**Gene:** LTA4H
**UniProt Accession:** P09960
**Protein Name:** Leukotriene A-4 hydrolase
**Length:** 611 aa | **Mass:** 69.3 kDa
**Aliases:** LTA4
**Report Date:** 2026-06-02
**Review Stage:** W1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 17 | HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Supported. | UniProt: No nuclear annotation in UniProt | GO-CC: GO:GO:0005654 (nucleoplasm, IDA); GO:GO:0005634 (nucleu |
| 2. Protein Size | 10 | 8 | 611 aa / 69.3 kDa. Slight deduction for size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 277. Novelty rule: >100=0 (REJECTED). |
| 4. 3D Structure | 30 | 30 | mean pLDDT: 96.3 (>90: 94.4%, 70-90: 5.2%, 50-70: 0.2%, <50: 0.2%). PDB: 77 structures. |
| 5. Regulatory Domains | 50 | 10 | No direct transcription function. No chromatin association. No epigenetic activity. No nucleic acid binding. |
| 6. PPI Network | 50 | 13 | STRING: 15 partners. IntAct: 15 interactors. UniProt: 1 interactors. |
| **TOTAL** | **180** | **78** | **NOTE: REJECTED – PubMed>100 (strict=277)** |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Cytosol
- **Additional:** Nucleoplasm
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** Cytosol

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### UniProt Subcellular Location
- **Cytoplasm** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0070062 (extracellular exosome)** – Evidence: HDA:UniProtKB
- **GO:0005576 (extracellular region)** – Evidence: TAS:Reactome
- **GO:1904813 (ficolin-1-rich granule lumen)** – Evidence: TAS:Reactome
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IBA:GO_Central
- **GO:1904724 (tertiary granule lumen)** – Evidence: TAS:Reactome

### Functional Context
Bifunctional zinc metalloenzyme that comprises both epoxide hydrolase (EH) and aminopeptidase activities. Acts as an epoxide hydrolase to catalyze the conversion of LTA4 to the pro-inflammatory mediator leukotriene B4 (LTB4) (PubMed:11917124, PubMed:12207002, PubMed:15078870, PubMed:18804029, PubMed:1897988, PubMed:1975494, PubMed:2244921, PubMed:2996528). Can utilize LTA5 less effectively as a substrate than LTA4, and produce LTB5 (PubMed:2996528). Also has aminopeptidase activity, with high af

**Summary:** HPA additional nuclear: Nucleoplasm. Nuclear is secondary location. Reliability: Supported. | UniProt: No nuclear annotation in UniProt | GO-CC: GO:GO:0005654 (nucleoplasm, IDA); GO:GO:0005634 (nucleus, IBA)

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 277 |
| Broad (All Fields) | 325 |

**Alias Note:** Aliases observed but not used for scoring: LTA4

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers (with PMIDs)
  - **PMID:40056904** – Yang S, Qiu X, Yang Y (2025 Mar 18). "LTA4H improves the tumor microenvironment and prevents HCC progression via targeting the HNRNPA1/LTBP1/TGF-β axis." *Cell reports. Medicine*.
  - **PMID:33400226** – Cherian A, Ajitha KC, Iype T (2021 Feb). "Neurotuberculosis: an update." *Acta neurologica Belgica*.
  - **PMID:37589142** – Yang M, Zhou X, Pearce SWA (2023 Oct). "Causal Role for Neutrophil Elastase in Thoracic Aortic Dissection in Mice." *Arteriosclerosis, thrombosis, and vascular biology*.
  - **PMID:19077707** – Lima JJ, Blake KV, Tantisira KG (2009 Jan). "Pharmacogenetics of asthma." *Current opinion in pulmonary medicine*.
  - **PMID:40324735** – Ye K, Li J, Huo Z (2025 Aug). "Down-regulating HDAC2-LTA4H pathway ameliorates renal ischemia-reperfusion injury." *Biochimica et biophysica acta. Molecular basis of disease*.

### Literature Assessment
- **Total publications:** Very high (>100, rejected) (277 strict, 325 broad).
- **Novelty score:** 0/10.
- **No publications directly linking LTA4H to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P09960-F1, version 6
- **mean pLDDT: 96.3 (>90: 94.4%, 70-90: 5.2%, 50-70: 0.2%, <50: 0.2%)**
- **Assessment:** Exceptionally high confidence.

### Experimental PDB Structures
- **77 structures available:** 1GW6 (X-ray, 2.20 A); 1H19 (X-ray, 2.10 A); 1HS6 (X-ray, 1.95 A); 1SQM (X-ray, 2.30 A); 2R59 (X-ray, 1.89 A); 2VJ8 (X-ray, 1.80 A); 3B7R (X-ray, 1.81 A); 3B7S (X-ray, 1.47 A); 3B7T (X-ray, 2.30 A); 3B7U (X-ray, 1.90 A) ... +67 more

### Structural Assessment
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

---

## PPI Network

### STRING
- Data available with 15 partners
- **ALOX5** (score: 0.992)
- **LTC4S** (score: 0.992)
- **ALOX5AP** (score: 0.95)
- **CYP4F3** (score: 0.936)
- **CYP4F2** (score: 0.92)

### IntAct
- Total: 15 validated interactors
- **TMEM62** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **ARPC3** (psi-mi:"MI:0398"(two hybrid pooling approach), pubmed:16169070|imex:IM-16517|mint:MINT-)
- **HLA-C** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **HLA-B** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **MCC** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **IKBKE** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **GH1** (psi-mi:"MI:0006"(anti bait coimmunoprecipitation), pubmed:17353931)
- **UBA5** (psi-mi:"MI:0007"(anti tag coimmunoprecipitation), pubmed:20562859|imex:IM-15184)

### PPI Network Assessment
- Moderate interaction network.
- TE-relevant connections: Limited TE-relevant connections

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
LTA4H was likely auto-rejected due to: PubMed>100 (strict=277)

### Recheck Analysis
1. **HPA Evidence:** Cytosol
2. **UniProt Evidence:** Weak or no experimental nuclear evidence
3. **GO-CC Evidence:** Nuclear/chromatin GO annotations present
4. **PubMed Count:** 277 strict, 325 broad – EXCEEDS 100 threshold

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=277) rule.** However, functional evidence may warrant exception review.

**This gene should remain REJECTED** per pipeline rules, but may qualify for exception review.

---

## TE-Regulator Relevance Reasoning

LTA4H has indirect TE-regulatory relevance at best. The protein primarily functions in processes not directly related to TE biology.



---

## Final Decision

**DECISION: REJECTED (PubMed>100 (strict=277))**

Score: 78/180 (shown for completeness, but automatic rejection applies).

**Reasoning:** LTA4H exceeds the PubMed>100 rejection threshold (277 publications). While nuclear evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

This gene exceeds the PubMed>100 threshold for automatic rejection. However, its functional profile is relevant to TE biology. If exception criteria exist, this gene should be considered for waiver review.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000111144-LTA4H/subcellular

![](https://images.proteinatlas.org/8399/1033_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/8399/1033_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/8399/2269_C10_138_red_green.jpg)
![](https://images.proteinatlas.org/8399/2269_C10_88_red_green.jpg)
![](https://images.proteinatlas.org/8399/75_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/8399/75_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
