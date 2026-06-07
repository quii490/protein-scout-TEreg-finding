# NLE1 – Critical False-Rejection Reevaluation Report

**Gene:** NLE1
**UniProt Accession:** Q9NVX2
**Protein Name:** Notchless protein homolog 1
**Length:** 485 aa | **Mass:** 53.3 kDa
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA: Nucleoplasm, Nucleoli (Supported). UniProt: Nucleus, nucleolus. GO-CC: 2 IDA nuclear anno. |
| 2. Protein Size | 10 | 7 | 485 aa / 53.3 kDa – larger protein, still tractable but requires more resources. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 14. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 30 | AlphaFold mean pLDDT: 93.7. PDB: 14 experimental structures. |
| 5. Regulatory Domains | 50 | 6 | InterPro: IPR012972, IPR015943, IPR001632. Function summary: Plays a role in regulating Notch activity. Plays a role in regulating the expression of CDKN1A and several members of the Wnt pathway, probably via its effects on Notch activity. Required during embry... |
| 6. PPI Network | 50 | 7 | STRING: 0 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **82** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoli
- **Additional Locations:** Nucleoplasm
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoplasm, Nucleoli

### UniProt Subcellular Location
- **Nucleus, nucleolus** – Evidence: ECO:0000269, ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005730 (nucleolus)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA

### Functional Context
- Plays a role in regulating Notch activity. Plays a role in regulating the expression of CDKN1A and several members of the Wnt pathway, probably via its effects on Notch activity. Required during embryogenesis for inner mass cell survival (By similarity)

**Summary:** NLE1 has strong nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence; GO: 2 IDA nuclear annotations). Nuclear score: 22/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 14 | `"NLE1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 46 | |
| Broad (All Fields) | 46 | |


### Key Papers (with PMIDs)
1. **PMID:39423824** – Burban A, Sharanek A, Hernandez-Corchado A (2024 Nov 12). "Targeting glioblastoma with a brain-penetrant drug that impairs brain tumor stem cells via NLE1-Notch1 complex." *Stem cell reports.*
2. **PMID:40625398** – Zhang R, Liu D, Feng X (2025). "WD40 Protein NLE1 as a Novel Diagnostic Biomarker Promoting Hepatocellular Carcinoma Proliferation." *Clinical Medicine Insights. Oncology.*
3. **PMID:36219392** – Loevenich LP, Tschurtschenthaler M, Rokavec M (2022 Dec 16). "SMAD4 Loss Induces c-MYC-Mediated NLE1 Upregulation to Support Protein Biosynthesis, Colorectal Cancer Growth, and Metastasis." *Cancer research.*
4. **PMID:28210849** – Karimzadeh F, Modarres Mousavi SM, Alipour F (2017 Aug). "Developmental changes in Notch1 and NLE1 expression in a genetic model of absence epilepsy." *Brain structure & function.*
5. **PMID:9350976** – Yang Q, Hanesworth JM, Harding JW (1997 Aug 29). "The AT4 receptor agonist [Nle1]-angiotensin IV reduces mechanically induced immediate-early gene expression in the isolated rabbit heart." *Regulatory peptides.*

### Literature Assessment
- **Total publications:** Low (14 strict, 46 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NVX2-F1, version 6
- **Mean pLDDT:** 93.7
- **pLDDT Distribution:**
  - >90 (very high confidence): 85.6%
  - 70-90 (confident): 11.8%
  - 50-70 (low confidence): 0.4%
  - <50 (very low confidence): 2.3%
- **Assessment:** High-confidence structure. Most of the protein is predicted with high confidence, suitable for structural studies.

### Experimental PDB Structures
- **6WAJ** – X-ray, 1.90 A, chains: A=1-97
- **8FL0** – EM, 2.91 A, chains: NJ=1-485
- **8FL2** – EM, 2.67 A, chains: NJ=1-485
- **8FL3** – EM, 2.53 A, chains: NJ=1-485
- **8FL4** – EM, 2.89 A, chains: NJ=1-485
- **8INK** – EM, 3.20 A, chains: W=1-485
- **8IPD** – EM, 3.20 A, chains: W=1-485
- **8IPX** – EM, 4.30 A, chains: W=1-485
- **8IPY** – EM, 3.20 A, chains: W=1-485
- **8IR1** – EM, 3.30 A, chains: N=1-485
- ... and 4 more structures

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 30/30

---

## PPI Network

### STRING (Functional Partners)
- No STRING data available.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2010.11.017 | psi-mi:"MI:0914"(association) |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 | psi-mi:"MI:0914"(association) |
| IGHMBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| PLEKHO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| RPL15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| RPL18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| RBM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 7/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NLE1 was likely auto-rejected due to automated scoring below pipeline threshold, despite qualifying nuclear evidence.

### Recheck Analysis
1. **HPA Evidence:** Nucleoli – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nucleus, nucleolus – ECO:0000269 (experimental, ['ECO:0000269', 'ECO:0000269']).
3. **GO-CC Evidence:** 2 IDA-level nuclear annotations present: nucleolus, nucleoplasm.
4. **PubMed Count:** 14 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection was FALSE – NLE1 should NOT have been rejected.** The nuclear evidence is ROBUST (HPA + UniProt experimental + GO IDA). The automated system may have undervalued the nuclear localization, been confused by dual localization patterns, or applied overly conservative scoring.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

1. **Nucleolar Function:** NLE1 localizes to the nucleolus. Repetitive rDNA and some TEs are organized in nucleolar-associated domains, making nucleolar proteins relevant to TE spatial organization.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** HIGH interest candidate for TE regulation. STRONG nuclear evidence combined with MAXIMUM novelty (14 publications). The protein's nuclear localization and functional domain profile make it a compelling target for original investigation into TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 82/180**

**Reasoning:** NLE1 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (14 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NLE1 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NLE1 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NLE1 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NLE1 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NLE1 encodes Notchless protein homolog 1, a 485-amino acid 53.3 kDa protein. 
HPA localizes NLE1 to Nucleoplasm/Nucleoli (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Plays a role in regulating Notch activity. Plays a role in regulating the expression of CDKN1A and several members of the Wnt pathway, probably via its effects on Notch activity. Required during embry. 
The false rejection appears to have resulted from automated scoring that failed to adequately weight the nuclear evidence. 
With only 14 publications, NLE1 represents a highly novel target. 
The nuclear localization and functional profile make it a strong candidate for TE-regulatory investigation.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000073536-NLE1/subcellular

![](https://images.proteinatlas.org/18807/115_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/18807/115_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/18807/116_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/18807/116_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/18807/117_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/18807/117_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NVX2 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012972;IPR015943;IPR001632;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF08154;PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000073536-NLE1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Biogrid, Bioplex | true |
| GNL3 | Intact, Biogrid | true |
| NSA2 | Biogrid, Bioplex | true |
| CCT5 | Biogrid | false |
| GNL2 | Biogrid | false |
| GPATCH4 | Biogrid | false |
| MDN1 | Biogrid | false |
| MYC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
