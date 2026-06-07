# RSRC1 -- Critical False-Rejection Reevaluation Report

**Gene:** RSRC1 (Serine/Arginine-related protein 53)
**UniProt Accession:** Q96IZ7
**Protein Name:** Serine/Arginine-related protein 53
**Length:** 334 aa | **Mass:** 38.7 kDa
**Aliases:** SRRP53
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 25 | HPA main: Nuclear speckles. Reliability: Approved. UniProt: Nucleus (ECO:0000250), Nucleus speckle (ECO:0000250), Cytoplasm (ECO:0000250). GO-CC: nuclear speck (ISS:UniProtKB), nucleus (ISS:UniProtKB). Nuclear speckles are a well-defined nuclear subcompartment for splicing factors. HPA Approved reliability. Strong evidence for nuclear speckle localization. |
| 2. Protein Size | 10 | 10 | 334 aa / 38.7 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 22. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 8 | AlphaFold mean pLDDT: 58.4 (9.9% >90, 21.3% 70-90, 20.4% 50-70, 48.5% <50). PDB: None. Low structural confidence. Nearly half of residues <50 pLDDT. |
| 5. Regulatory Domains | 50 | 35 | IPR034604. No Pfam. FUNCTION: Role in alternative splicing and transcription regulation (PMID:29522154). Involved in both constitutive and alternative pre-mRNA splicing. May have role in recognition of 3' splice site during second step of splicing. Splicing regulation is a nuclear RNA-processing function with indirect transcriptional regulatory impact. Also involved in transcription regulation directly. |
| 6. PPI Network | 50 | 30 | STRING: 15 partners. FAU (0.988), RPS15 (0.985), RPS18 (0.983), RPS9 (0.983). All top STRING partners are ribosomal proteins -- RSRC1 associates with ribosome. IntAct: 15 interactors. EEF1A1, LSM2, UTP14A, PRPF8 (spliceosome!), SNW1 (spliceosome), SRPK2 (SR protein kinase), SRPK1, NCBP3 (cap-binding), AUTS2, ESR1 (estrogen receptor), SRRM4. UniProt: JMJD6 (histone arginine demethylase), LAMP2, PRPF40A, RAN, SRPK2, SRRM4, YWHAG. Splicing factor network + chromatin connections. |
| **TOTAL** | **180** | **118** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nuclear speckles
- **Additional:** None
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** Nuclear speckles -- canonical subnuclear compartment for pre-mRNA splicing factors.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000250 (by similarity)
- **Nucleus speckle** -- ECO:0000250 (by similarity)
- **Cytoplasm** -- ECO:0000250 (by similarity)

### GO Cellular Component (GO-CC)
- **GO:0016607 (nuclear speck)** -- ISS:UniProtKB
- **GO:0005634 (nucleus)** -- ISS:UniProtKB
- **GO:0005737 (cytoplasm)** -- ISS:UniProtKB

**Summary:** RSRC1 localizes to nuclear speckles (HPA Approved), which are subnuclear domains enriched in pre-mRNA splicing factors. This is a strong nuclear localization relevant to RNA processing/splicing. Nuclear score: 25/30 -- strong nuclear speckle evidence.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 22 |
| Broad (All Fields) | 28 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:29522154** -- Perez Y et al. (2018). "RSRC1 mutation affects intellect and behaviour through aberrant splicing and transcription, downregulating IGFBP3." *Brain*.
2. **PMID:37095490** -- Zhang S et al. (2023). "A novel protein encoded by circRsrc1 regulates mitochondrial ribosome assembly and translation during spermatogenesis." *BMC Biol*.
3. **PMID:29653227** -- Tang J et al. (2018). "RSRC1 and CPZ gene polymorphisms with neuroblastoma susceptibility in Chinese children." *Gene*.
4. **PMID:25937118** -- Chen L et al. (2015). "RSRC1 SUMOylation enhances SUMOylation and inhibits transcriptional activity of estrogen receptor beta." *FEBS Lett*.
5. **PMID:40078563** -- Zhang W et al. (2025). "Improving neuroblastoma risk prediction through a polygenic risk score derived from genome-wide association study-identified loci." *Chin J Cancer Res*.

**Assessment:** RSRC1 has roles in splicing, transcription regulation, and SUMOylation. SUMOylation connection to estrogen receptor beta transcription is notable.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96IZ7-F1, version 6
- **mean pLDDT: 58.4** (>90: 9.9%, 70-90: 21.3%, 50-70: 20.4%, <50: 48.5%)
- **Assessment:** LOW confidence. Nearly half of residues below pLDDT 50. Likely an intrinsically disordered protein or requires binding partners for folding.

### Experimental PDB Structures
- **None.**
- **Assessment:** No experimental structures.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| FAU | 0.988 | 0.967 | Ribosomal protein |
| RPS15 | 0.985 | 0.841 | Ribosomal protein |
| RPS18 | 0.983 | 0.839 | Ribosomal protein |
| RPS9 | 0.983 | 0.839 | Ribosomal protein |
| RPS3 | 0.982 | 0.834 | Ribosomal protein |

All top STRING partners are ribosomal proteins. Strong ribosome association.

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| PRPF8 | TAP | 20360068 | Spliceosome core |
| SNW1 | TAP | 20360068 | Spliceosome |
| SRPK2 | Kinase assay | 23602568 | SR protein kinase |
| SRPK1 | Kinase assay | 23602568 | SR protein kinase |
| NCBP3 | Pull-down | 26382858 | Cap-binding complex |
| ESR1 | TAP | 31527615 | Estrogen receptor |
| SRRM4 | Validated 2H | 32296183 | Splicing regulator |
| AUTS2 | Cross-link | 30021884 | Neurodevelopmental |

### PPI Network Assessment
- Strong splicing factor network (PRPF8, SNW1, SRPK1/2, SRRM4).
- Ribosomal protein association (possible translation coupling).
- ESR1 (estrogen receptor) interaction links to transcriptional regulation.
- JMJD6 (UniProt, 4 experiments) is a histone arginine demethylase -- chromatin connection.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RSRC1 was likely rejected due to low structural confidence and potentially incomplete reporting.

### Recheck Analysis
1. **Nuclear evidence:** STRONG. HPA Approved: Nuclear speckles. This is a well-defined nuclear subcompartment for splicing factors.
2. **Functional context:** Splicing regulation AND transcription regulation. Involved in alternative splicing. SUMOylation modulates ESR1 transcriptional activity.
3. **PubMed:** 22 strict. LOW.
4. **Structure:** Low AF confidence (mean pLDDT 58.4). Likely IDR.
5. **PPI:** Strong splicing factor network with chromatin connections (JMJD6 histone demethylase, ESR1, AUTS2).

### Verdict
**The original rejection was INCORRECT.** RSRC1 is a nuclear speckle protein with roles in alternative splicing and transcription regulation. It interacts with core spliceosome components (PRPF8, SNW1), SR protein kinases, and chromatin-associated proteins (JMJD6, ESR1). While structural confidence is low, the nuclear localization and regulatory function are well-supported. Should be RETAINED.

---

## TE-Regulator Relevance

MODERATE. RSRC1 functions in alternative splicing and transcription regulation. Alternative splicing of TE-derived transcripts could influence TE silencing outcomes. The ESR1 (estrogen receptor) interaction and JMJD6 (histone arginine demethylase) connection suggest potential chromatin-level involvement. SUMOylation of RSRC1 affects its regulatory activity. However, no direct TE silencing function is demonstrated. Worth retaining for its splicing/transcription regulatory role in the nuclear compartment.

---

## Final Decision: RETAINED

Score: 118/180. RSRC1 is a nuclear speckle splicing factor with transcription regulatory function, strong nuclear localization (HPA Approved), good PPI network (spliceosome + chromatin connections), and high novelty (PubMed=22). Retained despite low structural confidence.

---

## Manual Review Note
MODERATE CANDIDATE. RSRC1 (SRRP53) is an SR-related protein that localizes to nuclear speckles and participates in pre-mRNA splicing and transcription regulation. Key strengths: HPA Approved nuclear speckle localization, strong spliceosome PPI network (PRPF8, SNW1, SRPK1/2), chromatin connections (JMJD6, ESR1), SUMOylation-dependent regulatory activity. Key weakness: very low structural confidence (mean pLDDT 58.4) suggesting substantial disorder. Retained for splicing/transcription regulatory potential.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000174891-RSRC1/subcellular

![](https://images.proteinatlas.org/44792/522_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/44792/522_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/44792/527_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/44792/527_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/44792/529_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/44792/529_C1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96IZ7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034604; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174891-RSRC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2B | Biogrid, Opencell | true |
| JMJD6 | Intact, Biogrid | true |
| SRPK2 | Intact, Biogrid | true |
| AAMP | Opencell | false |
| CD2BP2 | Opencell | false |
| CDKN2A | Opencell | false |
| COMMD1 | Opencell | false |
| COMMD2 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
