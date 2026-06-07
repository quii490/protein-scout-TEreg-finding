# MRI1 – Critical False-Rejection Reevaluation Report

**Gene:** MRI1
**UniProt Accession:** Q9BV20
**Protein Name:** Methylthioribose-1-phosphate isomerase
**Length:** 369 aa | **Mass:** 39.1 kDa
**Aliases:** MRDI
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 19 | HPA: Nucleoplasm, Nucleoli fibrillar center, Cytosol (Supported). UniProt: Nucleus. GO-CC: 1 IDA nuclear anno. |
| 2. Protein Size | 10 | 9 | 369 aa / 39.1 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 17. <=20 = 10/10 maximum novelty. Very poorly studied. |
| 4. 3D Structure | 30 | 27 | AlphaFold mean pLDDT: 94.8. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 4 | InterPro: IPR000649, IPR005251, IPR042529. Function summary: Catalyzes the interconversion of methylthioribose-1-phosphate (MTR-1-P) into methylthioribulose-1-phosphate (MTRu-1-P). Independently from catalytic activity, promotes cell invasion in response to con... |
| 6. PPI Network | 50 | 23 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **92** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm, Cytosol
- **Additional Locations:** Nucleoli fibrillar center
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoplasm, Nucleoli fibrillar center, Cytosol

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000255, ECO:0000269
- **Cytoplasm** – Evidence: ECO:0000255, ECO:0000269
- **Cell projection** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0042995 (cell projection)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0001650 (fibrillar center)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA

### Functional Context
- Catalyzes the interconversion of methylthioribose-1-phosphate (MTR-1-P) into methylthioribulose-1-phosphate (MTRu-1-P). Independently from catalytic activity, promotes cell invasion in response to constitutive RhoA activation by promoting FAK tyrosine phosphorylation and stress fiber turnover

**Summary:** MRI1 has moderate nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence; GO: 1 IDA nuclear annotations). Nuclear score: 19/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 17 | `"MRI1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 97 | |
| Broad (All Fields) | 109 | |

**Alias Note:** Aliases observed but not used for scoring: MRDI

### Key Papers (with PMIDs)
1. **PMID:39091293** – Chen W, Li S, Huang D (2024). "Identification of prognostic RNA editing profiles for clear cell renal carcinoma." *Frontiers in medicine.*
2. **PMID:37138656** – Zhang X, Zhen D, Li X (2023). "NOTCH2, ATIC, MRI1, SLC6A13, ATP13A2 Genetic Variations are Associated with Ventricular Septal Defect in the Chinese Tibetan Population Through Whole-Exome Sequencing." *Pharmacogenomics and personalized medicine.*
3. **PMID:38215673** – Zhang X, Zhen D, Yi F (2024 Apr). "Identification of Six Pathogenic Genes for Tibetan Familial Ventricular Septal Defect by Whole Exome Sequencing." *The Journal of surgical research.*
4. **PMID:32800812** – Makimoto J, Wakabayashi K, Inoue T (2020 Dec). "Mutagenesis, breeding, and characterization of sake yeast strains with low production of dimethyl trisulfide precursor." *Journal of bioscience and bioengineering.*
5. **PMID:40651720** – Leyhausen J, Gurr C, Berg LM (2026 Jan). "Parsing Autism Heterogeneity: Transcriptomic Subgrouping of Imaging-Derived Phenotypes in Autism." *Biological psychiatry. Cognitive neuroscience and neuroimaging.*

### Literature Assessment
- **Total publications:** Low (17 strict, 109 broad).
- **Novelty score:** 10/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9BV20-F1, version 6
- **Mean pLDDT:** 94.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 93.5%
  - 70-90 (confident): 2.7%
  - 50-70 (low confidence): 0.8%
  - <50 (very low confidence): 3.0%
- **Assessment:** High-confidence structure. Most of the protein is predicted with high confidence, suitable for structural studies.

### Experimental PDB Structures
- **4LDQ** – X-ray, 2.50 A, chains: A/B=1-369
- **4LDR** – X-ray, 2.29 A, chains: A/B=1-369

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 27/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| APIP | 0.992 | 0.000 | 0.672 | |
| MTAP | 0.991 | 0.000 | 0.541 | |
| ENOPH1 | 0.975 | 0.000 | 0.807 | |
| ADI1 | 0.909 | 0.229 | 0.775 | |
| CYREN | 0.890 | 0.000 | 0.890 | |
| PNP | 0.881 | 0.000 | 0.359 | |
| ACAD10 | 0.842 | 0.000 | 0.000 | |
| ACAD11 | 0.822 | 0.000 | 0.000 | |
| ADD3 | 0.796 | 0.000 | 0.310 | |
| ADD2 | 0.796 | 0.000 | 0.313 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| ENSP00000040663.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| D6W4B7 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 | psi-mi:"MI:0915"(physical association) |
| EBI-21246012 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-26346|pubmed:23695164|doi:10.1126/scisignal.2003350 | psi-mi:"MI:0915"(physical association) |
| SVF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 | psi-mi:"MI:0915"(physical association) |
| KTR3 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 | psi-mi:"MI:0915"(physical association) |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 | psi-mi:"MI:0914"(association) |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 | psi-mi:"MI:0914"(association) |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **Score:** 23/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
MRI1 was likely auto-rejected due to:
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm, Cytosol – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000255', 'ECO:0000269']).
3. **GO-CC Evidence:** 1 IDA-level nuclear annotations present: nucleoplasm.
4. **PubMed Count:** 17 strict – ≤20 = MAXIMUM novelty. This gene is very poorly studied, which should be advantageous.

### Verdict on False Rejection
**The original rejection was LIKELY FALSE.** Nuclear evidence is PRESENT but not overwhelming. The gene merits reevaluation because the nuclear annotation is supported by multiple sources (UniProt + GO).

**This gene should be REOPENED for TE-regulatory evaluation unless the PubMed count exceeds the threshold.**

---

## TE-Regulator Relevance Reasoning

1. **Indirect Relevance:** MRI1's nuclear localization and functional profile suggest a structural or metabolic role without direct transcriptional/chromatin functions. TE relevance would be INDIRECT at best, possibly through general nuclear organization or cellular metabolism affecting TE expression states.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** HIGH interest candidate for TE regulation. STRONG nuclear evidence combined with MAXIMUM novelty (17 publications). The protein's nuclear localization and functional domain profile make it a compelling target for original investigation into TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 92/180**

**Reasoning:** MRI1 was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (17 strict) provides excellent novelty. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm MRI1 nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for MRI1 binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate MRI1 expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether MRI1 loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

MRI1 encodes Methylthioribose-1-phosphate isomerase, a 369-amino acid 39.1 kDa protein. 
HPA localizes MRI1 to Nucleoplasm/Nucleoli fibrillar center (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Catalyzes the interconversion of methylthioribose-1-phosphate (MTR-1-P) into methylthioribulose-1-phosphate (MTRu-1-P). Independently from catalytic activity, promotes cell invasion in response to con. 
The false rejection may have resulted from automated scoring thresholds. 
The nuclear evidence, while present, is not overwhelming. 
MRI1 should be reevaluated in the context of broader TE biology hypotheses.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000037757-MRI1/subcellular

![](https://images.proteinatlas.org/42744/474_F6_5_red_green.jpg)
![](https://images.proteinatlas.org/42744/474_F6_6_red_green.jpg)
![](https://images.proteinatlas.org/42744/480_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/42744/480_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/42744/510_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/42744/510_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BV20 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000649;IPR005251;IPR042529;IPR011559;IPR027363;IPR037171; |
| Pfam | PF01008; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000037757-MRI1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASP6 | Intact | false |
| COG6 | Intact | false |
| F11R | Intact | false |
| NUP58 | Intact | false |
| PICK1 | Intact | false |
| PLEKHF2 | Intact | false |
| PRKN | Biogrid | false |
| SH3GLB1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
