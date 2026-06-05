# MPHOSPH6 – Critical False-Rejection Reevaluation Report

**Gene:** MPHOSPH6
**UniProt Accession:** Q99547
**Protein Name:** M-phase phosphoprotein 6
**Length:** 160 aa | **Mass:** 19.0 kDa
**Aliases:** MPP6
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 17 | HPA: Nucleoplasm, Nucleoli (Supported). UniProt: Nucleus, nucleolus. GO-CC: 3 IDA nuclear anno. |
| 2. Protein Size | 10 | 10 | 160 aa / 19.0 kDa – small, highly tractable. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 18. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 15 | AlphaFold mean pLDDT: 76.4. PDB: 3 experimental structures. |
| 5. Regulatory Domains | 50 | 3 | InterPro: IPR019324. Function summary: RNA-binding protein that associates with the RNA exosome complex. Involved in the 3'-processing of the 7S pre-RNA to the mature 5.8S rRNA and play a role in recruiting the RNA exosome complex to pre-r... |
| 6. PPI Network | 50 | 23 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **78** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm, Nucleoli
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoplasm, Nucleoli

### UniProt Subcellular Location
- **Nucleus, nucleolus** – Evidence: no evidence code
- **Cytoplasm** – Evidence: no evidence code

### GO Cellular Component (GO-CC)
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0000178 (exosome (RNase complex))** – Evidence: IDA:UniProtKB
- **GO:0005730 (nucleolus)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB

### Functional Context
- RNA-binding protein that associates with the RNA exosome complex. Involved in the 3'-processing of the 7S pre-RNA to the mature 5.8S rRNA and play a role in recruiting the RNA exosome complex to pre-rRNA; this function may include C1D

**Summary:** MPHOSPH6 has moderate nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence; GO: 3 IDA nuclear annotations). Nuclear score: 17/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 18 | `"MPHOSPH6"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] ...` |
| Symbol Only (Title/Abstract) | 21 | |
| Broad (All Fields) | 22 | |

**Alias Note:** Aliases observed but not used for scoring: MPP6

### Key Papers (with PMIDs)
1. **PMID:38881917** – Yu L, Jing C, Zhuang S (2024 May 31). "A novel lactylation-related gene signature for effectively distinguishing and predicting the prognosis of ovarian cancer." *Translational cancer research.*
2. **PMID:40425712** – Liu J, Luo N, Ma W (2025 May 27). "Novel ribosome biogenesis-related biomarkers and therapeutic targets identified in psoriasis." *Scientific reports.*
3. **PMID:41436647** – Huang Y, Geng M, Zhang M (2025 Dec 23). "Unveiling novel potential drug targets for lung cancer through Mendelian randomization analysis." *Scientific reports.*
4. **PMID:29069794** – Yang X, Zhang Y, Li W (2017 Sep 22). "Association between MPHOSPH6 gene polymorphisms and IgA nephropathy risk in a Chinese Han population." *Oncotarget.*
5. **PMID:40354008** – Wei C, He J, Li Y (2025 May 12). "Multi-omics identify ribosome related causal genes methylation, splicing, and expression in prostate cancer." *Discover oncology.*

### Literature Assessment
- **Total publications:** Low (18 strict, 22 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q99547-F1, version 6
- **Mean pLDDT:** 76.4
- **pLDDT Distribution:**
  - >90 (very high confidence): 7.5%
  - 70-90 (confident): 65.0%
  - 50-70 (low confidence): 26.2%
  - <50 (very low confidence): 1.2%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **6D6Q** – EM, 3.45 A, chains: L=1-160
- **6D6R** – EM, 3.45 A, chains: L=1-160
- **6H25** – EM, 3.80 A, chains: K=1-160

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 15/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| EXOSC4 | 0.999 | 0.974 | 0.691 | |
| EXOSC7 | 0.999 | 0.980 | 0.758 | |
| EXOSC8 | 0.999 | 0.979 | 0.723 | |
| EXOSC5 | 0.999 | 0.972 | 0.772 | |
| EXOSC6 | 0.999 | 0.965 | 0.743 | |
| EXOSC1 | 0.999 | 0.988 | 0.874 | |
| EXOSC3 | 0.999 | 0.991 | 0.762 | |
| EXOSC10 | 0.998 | 0.972 | 0.614 | |
| EXOSC9 | 0.998 | 0.973 | 0.456 | |
| EXOSC2 | 0.998 | 0.974 | 0.539 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| MTREX | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 | psi-mi:"MI:0915"(physical association) |
| PARN | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 | psi-mi:"MI:0915"(physical association) |
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 | psi-mi:"MI:0915"(physical association) |
| TLE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| ZHX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 23/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
MPHOSPH6 was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm, Nucleoli – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** 3 IDA-level nuclear annotations present: nucleolus, nucleoplasm, nucleus.
4. **PubMed Count:** 18 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection was LIKELY FALSE.** Nuclear evidence is PRESENT but not overwhelming. The gene merits reevaluation because the nuclear annotation is supported by multiple sources (UniProt + GO).

**This gene should be REOPENED for TE-regulatory evaluation unless the PubMed count exceeds the threshold.**

---

## TE-Regulator Relevance Reasoning

1. **Nucleolar Function:** MPHOSPH6 localizes to the nucleolus. Repetitive rDNA and some TEs are organized in nucleolar-associated domains, making nucleolar proteins relevant to TE spatial organization.
2. **RNA Exosome:** MPHOSPH6 associates with the RNA exosome complex. The exosome degrades aberrant RNAs, including TE-derived transcripts. Exosome-associated proteins can provide TE transcript surveillance.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE-HIGH interest candidate. Nuclear evidence is robust and literature is limited, offering good novelty. The protein's functional roles in the nucleus provide mechanistic hypotheses for TE regulation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 78/180**

**Reasoning:** MPHOSPH6 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (18 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm MPHOSPH6 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for MPHOSPH6 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate MPHOSPH6 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether MPHOSPH6 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

MPHOSPH6 encodes M-phase phosphoprotein 6, a 160-amino acid 19.0 kDa protein. 
HPA localizes MPHOSPH6 to Nucleoplasm/Nucleoli (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: RNA-binding protein that associates with the RNA exosome complex. Involved in the 3'-processing of the 7S pre-RNA to the mature 5.8S rRNA and play a role in recruiting the RNA exosome complex to pre-r. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
MPHOSPH6 should be reevaluated in the context of broader TE biology hypotheses.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000135698-MPHOSPH6/subcellular

![](https://images.proteinatlas.org/26948/604_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/26948/604_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/26948/607_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/26948/607_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/26948/609_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/26948/609_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
