# SPATA13 -- Critical False-Rejection Reevaluation Report

**Gene:** SPATA13 (Spermatogenesis-associated protein 13)
**UniProt Accession:** Q96N96
**Protein Name:** Spermatogenesis-associated protein 13
**Length:** 652 aa | **Mass:** 74.8 kDa
**Aliases:** None
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 12 | HPA main: Nucleoplasm. Additional: Cytosol. Reliability: Enhanced. UniProt: Cytoplasm, Filopodium, Lamellipodium, Ruffle membrane, Podosome (ECO:0000250). NO nuclear UniProt annotation. GO-CC: nucleoplasm (IDA:HPA), cytosol (IDA:HPA), cytoplasm (IDA:UniProtKB), filopodium (IDA:UniProtKB), lamellipodium (IDA:UniProtKB), ruffle membrane (IDA:UniProtKB). HPA Enhanced nucleoplasm vs. NO UniProt nuclear annotation -- discordant. |
| 2. Protein Size | 10 | 8 | 652 aa / 74.8 kDa. Moderate-large size. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 18. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 14 | AlphaFold mean pLDDT: 71.7 (46.6% >90, 18.1% 70-90, 4.3% 50-70, 31.0% <50). PDB: None. Moderate AF confidence. No experimental structures. |
| 5. Regulatory Domains | 50 | 15 | IPR035899, IPR000219 (DH domain), IPR011993, IPR001849 (PH domain), IPR036028, IPR001452 (SH3 domain), IPR055251. PF00621 (RhoGEF), PF00018 (SH3), PF22697. FUNCTION: GEF for RHOA, RAC1, CDC42 GTPases. Regulates cell migration and adhesion. Also known as ASEF2. RhoGEF function is signaling (cytoplasmic), not nuclear/chromatin regulation. DH-PH domains are prototypical GEF modules. |
| 6. PPI Network | 50 | 25 | STRING: 15 partners. APC (0.983), CDC42 (0.949), RAC2 (0.936), RAC3 (0.933), ARHGEF4 (0.930), APC2 (0.903), YWHAE (0.772). IntAct: 15 interactors. SHANK3, GLDC, YWHAQ, YWHAB, YWHAG, YWHAE, YWHAZ, YWHAH, APC, CTNNB1, CDC42, RAC1, ARHGEF4. |
| **TOTAL** | **180** | **84** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Enhanced
- **Main Location:** Nucleoplasm
- **Additional:** Cytosol
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** HPA detects nucleoplasm at Enhanced reliability. But this is discordant with UniProt and functional context.

### UniProt Subcellular Location
- **Cytoplasm** -- no evidence code
- **Cell projection, filopodium** -- no evidence code
- **Cell projection, lamellipodium** -- no evidence code
- **Cell projection, ruffle membrane** -- no evidence code
- **Cell projection, podosome** -- ECO:0000250
- **NO nuclear annotation in UniProt**

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005829 (cytosol)** -- IDA:HPA
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:0030175 (filopodium)** -- IDA:UniProtKB
- **GO:0030027 (lamellipodium)** -- IDA:UniProtKB
- **GO:0032587 (ruffle membrane)** -- IDA:UniProtKB

**Summary:** Discordant nuclear evidence. HPA (Enhanced) detects nucleoplasm, but UniProt has NO nuclear annotation. The functional context (RhoGEF, cell migration, filopodia/lamellipodia) is entirely cytoplasmic/membrane. The HPA nucleoplasm annotation may be an artifact or reflect a minor pool. Nuclear score: 12/30 -- discordant, unreliable nuclear evidence.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 18 |
| Broad (All Fields) | 40 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:40910032** -- Yang H et al. (2025). "The ceRNA Regulatory Network in Vitiligo: Evidence from Bioinformatics Analysis." *Clin Cosmet Investig Dermatol*.
2. **PMID:32339198** -- Waseem NH et al. (2020). "Mutations in SPATA13/ASEF2 cause primary angle closure glaucoma." *PLoS Genet*.
3. **PMID:41358093** -- Liu J et al. (2025). "Identification of Neurotrophic Factor Related Biomarkers and Mechanistic Insights into Neuropathic Pain via Integrated Bioinformatics Analysis." *ACS Omega*.
4. **PMID:31020388** -- Bourbia N et al. (2019). "The guanine nucleotide exchange factor, Spata13, influences social behaviour and nocturnal activity." *Mamm Genome*.
5. **PMID:41299718** -- Zhao X et al. (2025). "Overexpression of Hspa1b in the mouse hippocampus may be associated with major depressive disorder." *Behav Brain Funct*.

**Assessment:** SPATA13 (ASEF2) is studied as a RhoGEF in cell migration and cancer. Primary angle closure glaucoma association. No TE-related publications.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96N96-F1, version 6
- **mean pLDDT: 71.7** (>90: 46.6%, 70-90: 18.1%, 50-70: 4.3%, <50: 31.0%)
- **Assessment:** Moderate confidence. About one-third of residues below pLDDT 50.

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
| APC | 0.983 | 0.630 | Adenomatous polyposis coli |
| CDC42 | 0.949 | 0.728 | Rho GTPase (GEF substrate) |
| RAC2 | 0.936 | 0.302 | Rho GTPase |
| RAC3 | 0.933 | 0.302 | Rho GTPase |
| ARHGEF4 | 0.930 | 0.292 | Related RhoGEF |
| YWHAE | 0.772 | 0.771 | 14-3-3 epsilon |
| RAC1 | 0.709 | 0.484 | Rho GTPase (GEF substrate) |
| RHOA | 0.624 | 0.128 | Rho GTPase (GEF substrate) |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| APC | Pull-down (direct) | 17599059 | Tumor suppressor scaffold |
| CTNNB1 | Co-IP | 10947987 | Beta-catenin -- WNT pathway |
| CDC42 | GEF assay | 17145773 | Direct GEF substrate |
| RAC1 | Pull-down | 17145773 | Direct GEF substrate |
| YWHAE/Q/B/G/Z/H | Co-IP | 28514442 | 14-3-3 family |

### PPI Network Assessment
- Core function: RhoGEF for CDC42, RAC1, RHOA.
- APC interaction connects to WNT signaling and cell migration.
- CTNNB1 (beta-catenin) interaction is notable for WNT pathway connection.
- Network is cytoplasmic signaling/migration, not nuclear/chromatin.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SPATA13 was likely rejected due to primarily cytoplasmic signaling function and discordant nuclear evidence.

### Recheck Analysis
1. **Nuclear evidence:** DISCORDANT. HPA Enhanced nucleoplasm is contradicted by UniProt (no nuclear annotation) and functional context (RhoGEF, cell migration). HPA may be detecting a minor or artifactual nuclear pool.
2. **Functional context:** RhoGEF (DH-PH domains). Activates CDC42, RAC1, RHOA. Regulates cell migration, adhesion, tumor angiogenesis. Cytoplasmic signaling.
3. **PubMed:** 18 strict. LOW.
4. **Structure:** Moderate AF. No PDB.
5. **PPI:** RhoGEF signaling network. APC/CTNNB1 WNT pathway connection is interesting but cytoplasmic.

### Verdict
**The original rejection was CORRECT.** SPATA13 is a RhoGEF (ASEF2) that functions in cytoplasmic signal transduction (small GTPase activation) and cell migration. The HPA nucleoplasm annotation is discordant with UniProt (no nuclear) and the well-characterized cytoplasmic function. No chromatin, transcriptional, or TE-regulatory function. Should remain REJECTED.

---

## TE-Regulator Relevance

NEGLIGIBLE. SPATA13 is a RhoGEF that activates small GTPases (CDC42, RAC1, RHOA) to regulate actin cytoskeleton dynamics, cell migration, and adhesion. Its biology is cytoplasmic signal transduction and cytoskeletal regulation. No evidence for nuclear function or chromatin/TE regulation.

---

## Final Decision: REJECTED

Score: 84/180. SPATA13 has discordant nuclear evidence (HPA nucleoplasm vs. no UniProt nuclear annotation), cytoplasmic signaling function (RhoGEF), and no chromatin or TE-regulatory activity. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. SPATA13 (ASEF2) is a well-characterized RhoGEF containing DH-PH and SH3 domains. Its function is activation of small GTPases (CDC42, RAC1, RHOA) at the plasma membrane to regulate actin dynamics and cell migration. The APC interaction connects it to WNT pathway and colorectal cancer. The HPA nucleoplasm annotation at Enhanced reliability is discordant with the known biology -- RhoGEFs function at membranes, not in the nucleus. The absence of any UniProt nuclear annotation strongly suggests the HPA signal is non-specific or represents a minor/artifactual pool. Not suitable for TE investigation.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000182957-SPATA13/subcellular

![](https://images.proteinatlas.org/40185/461_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/40185/461_C3_4_red_green.jpg)
![](https://images.proteinatlas.org/40185/462_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/40185/462_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/40185/464_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/40185/464_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
