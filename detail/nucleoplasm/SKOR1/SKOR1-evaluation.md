# SKOR1 -- Critical False-Rejection Reevaluation Report

**Gene:** SKOR1 (SKI family transcriptional corepressor 1)
**UniProt Accession:** P84550
**Protein Name:** SKI family transcriptional corepressor 1
**Length:** 965 aa | **Mass:** 99.8 kDa
**Aliases:** CORL1, FUSSEL15, LBXCOR1
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA main: Nucleoplasm. Reliability: Approved. UniProt: Nucleus (ECO:0000250 -- by similarity). GO-CC: nucleus (IBA:GO_Central), transcription regulator complex (IBA:GO_Central), cytoplasm (IBA:GO_Central), dendrite (IDA:UniProtKB), neuronal cell body (IDA:UniProtKB). HPA nucleoplasm is strong, but UniProt nuclear annotation is by-similarity only. Protein also localizes to neuronal compartments. |
| 2. Protein Size | 10 | 8 | 965 aa / 99.8 kDa. Large protein. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 18. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 8 | AlphaFold mean pLDDT: 54.1 (18.3% >90, 9.3% 70-90, 7.9% 50-70, 64.5% <50). PDB: None. VERY low confidence. Majority of protein is low-confidence. |
| 5. Regulatory Domains | 50 | 40 | IPR014890, IPR009061, IPR010919, IPR003380, IPR037000, IPR023216. PF08782, PF02437. FUNCTION: Acts as transcriptional corepressor of LBX1. Inhibits BMP signaling. SKI family transcriptional corepressor -- SKI family proteins are well-established transcriptional repressors involved in TGF-beta/BMP and other signaling pathways. Transcriptional corepressor with direct regulatory function. |
| 6. PPI Network | 50 | 25 | STRING: 15 partners. MAP2K5 (0.974), LBX1 (0.887), BTBD9 (0.884), MEIS1 (0.844), TLE1 (0.746, experimental), SMAD3 (0.613, experimental), CTBP1 (0.532, experimental). IntAct: 10 interactors. HDAC1 (Co-IP), TLE1 (Co-IP), CTBP1 (Co-IP), LBX1 (cross-link), HIPK2, TRIM27, PRKAA1, HDAC6, DYRK1B. |
| **TOTAL** | **180** | **113** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional:** None
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** HPA nucleoplasm (Approved). Consistent with transcriptional corepressor function.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000250 (by similarity)

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** -- IBA:GO_Central
- **GO:0005667 (transcription regulator complex)** -- IBA:GO_Central
- **GO:0005737 (cytoplasm)** -- IBA:GO_Central
- **GO:0030425 (dendrite)** -- IDA:UniProtKB
- **GO:0043025 (neuronal cell body)** -- IDA:UniProtKB

**Summary:** SKOR1 localizes to nucleoplasm (HPA Approved) and is associated with transcription regulator complexes. Also found in neuronal compartments (dendrite, cell body). Nuclear score: 22/30 -- good HPA data but UniProt annotation is by-similarity.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 18 |
| Broad (All Fields) | 38 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:39695147** -- Li G et al. (2024). "Overexpression of PDSS2-Del2 in HCC promotes tumor metastasis by interacting with macrophages." *Cell Death Discov*.
2. **PMID:38267254** -- Tan BJ et al. (2024). "Genetic Association Studies in Restless Legs Syndrome: Risk Variants & Ethnic Differences." *Can J Neurol Sci*.
3. **PMID:32572201** -- Sarayloo F et al. (2020). "SKOR1 has a transcriptional regulatory role on genes involved in pathways related to restless legs syndrome." *Eur J Hum Genet*.
4. **PMID:25817513** -- Gan-Or Z et al. (2015). "Genetic markers of Restless Legs Syndrome in Parkinson disease." *Parkinsonism Relat Disord*.
5. **PMID:36209572** -- Martins TF et al. (2022). "Functional analysis of litter size and number of teats in pigs: From GWAS to post-GWAS." *Theriogenology*.

**Assessment:** SKOR1 is primarily studied in restless legs syndrome genetics. Key paper (PMID:32572201) directly demonstrates transcriptional regulatory function.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P84550-F1, version 6
- **mean pLDDT: 54.1** (>90: 18.3%, 70-90: 9.3%, 50-70: 7.9%, <50: 64.5%)
- **Assessment:** VERY LOW confidence. Nearly two-thirds of residues below pLDDT 50. Likely a largely disordered protein that requires binding partners for folding.

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
| MAP2K5 | 0.974 | 0 | MEK5 kinase |
| LBX1 | 0.887 | 0 | Transcription factor (SKOR1 targets) |
| BTBD9 | 0.884 | 0 | RLS-associated |
| MEIS1 | 0.844 | 0 | Homeobox TF |
| TLE1 | 0.746 | 0.095 | Transcriptional corepressor |
| SMAD3 | 0.613 | 0.071 | TGF-beta/BMP signaling |
| CTBP1 | 0.532 | 0.095 | Transcriptional corepressor |

### IntAct (10 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| HDAC1 | Co-IP | 15528197 | Histone deacetylase -- CHROMATIN |
| TLE1 | Co-IP | 15528197 | Transcriptional corepressor |
| CTBP1 | Co-IP | 15528197 | Transcriptional corepressor |
| LBX1 | Cross-link | 15528197 | Direct target TF |
| HIPK2 | Colocalization | 15528197 | Homeodomain kinase |
| HDAC6 | Co-IP | 33961781 | Histone deacetylase |
| TRIM27 | Co-IP | 33961781 | E3 ubiquitin ligase |
| DYRK1B | Co-IP | 33961781 | Dual-specificity kinase |

### PPI Network Assessment
- Strong transcriptional corepressor network.
- HDAC1 interaction (Co-IP, PMID:15528197) is KEY -- direct connection to histone deacetylation/chromatin modification.
- TLE1 and CTBP1 are well-established corepressors.
- LBX1 cross-linking confirms direct transcription factor interaction.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SKOR1 was likely rejected due to low structural confidence and potentially underestimated regulatory function.

### Recheck Analysis
1. **Nuclear evidence:** PRESENT. HPA Approved: Nucleoplasm. Associated with transcription regulator complex (GO-CC).
2. **Functional context:** SKI family transcriptional corepressor. Directly represses transcription via LBX1. Inhibits BMP signaling. SKI family proteins are prototypical transcriptional repressors.
3. **PubMed:** 18 strict. LOW.
4. **Structure:** Very low AF confidence. Likely disordered.
5. **PPI:** HDAC1 interaction (histone deacetylase) is a direct chromatin modification connection. TLE1 and CTBP1 corepressors confirm transcriptional regulatory role.

### Verdict
**The original rejection was INCORRECT.** SKOR1 is a SKI family transcriptional corepressor with direct transcription regulation function. The HDAC1 interaction (histone deacetylase, Co-IP validated) provides a direct chromatin-level regulatory connection. HPA nucleoplasm (Approved) supports nuclear localization. The SKI protein family is well-characterized for transcriptional repression. Should be RETAINED.

---

## TE-Regulator Relevance

HIGH. SKOR1 is a transcriptional corepressor of the SKI family, which represses gene expression through recruitment of HDAC-containing complexes. The HDAC1 interaction is directly relevant to histone deacetylation and chromatin condensation -- core mechanisms for TE silencing. SKI family proteins also interact with SMAD proteins in TGF-beta/BMP signaling, which can regulate chromatin states. As a corepressor, SKOR1 could potentially be recruited to TE loci to mediate transcriptional silencing.

---

## Final Decision: RETAINED

Score: 113/180. SKOR1 is a SKI family transcriptional corepressor with HPA Approved nucleoplasm localization, HDAC1 interaction (direct chromatin modification link), and high novelty (PubMed=18). Retained despite low structural confidence.

---

## Manual Review Note
STRONG CANDIDATE. SKOR1 (CORL1/LBXCOR1) is a SKI family transcriptional corepressor that interacts with HDAC1, establishing a direct link to histone deacetylation-mediated gene repression. The SKI protein family (SKI, SKIL/SNO) is well-characterized for transcriptional repression. SKOR1 acts as a corepressor for LBX1 and inhibits BMP signaling. The HDAC1 interaction (PMID:15528197) and TLE1/CTBP1 corepressor network strongly support a chromatin-level regulatory role. Despite very poor structural data (mean pLDDT 54.1) -- common for transcriptional regulators with disordered activation/repression domains -- the functional evidence is compelling. Prioritized for TE investigation.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188779-SKOR1/subcellular

![](https://images.proteinatlas.org/40673/2062_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/40673/2062_A2_3_red_green.jpg)
![](https://images.proteinatlas.org/40673/418_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/40673/418_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/40673/424_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/40673/424_F1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
