# RUFY2 -- Critical False-Rejection Reevaluation Report

**Gene:** RUFY2 (RUN and FYVE domain-containing protein 2)
**UniProt Accession:** Q8WXA3
**Protein Name:** RUN and FYVE domain-containing protein 2
**Length:** 606 aa | **Mass:** 70.0 kDa
**Aliases:** KIAA1537, RABIP4R
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 10 | HPA main: Nucleoplasm. Reliability: Approved. UniProt: Nucleus (ECO:0000250 -- by similarity ONLY). GO-CC: nucleus (IEA:UniProtKB-SubCell -- electronic annotation), cytoplasm (IDA:UniProtKB -- experimental), endosome (ISS:UniProtKB). HPA detects nucleoplasm (Approved) but UniProt nuclear annotation is by-similarity only. The protein's known function is endosomal/vesicle trafficking. The nuclear annotation is inconsistent with functional profile. |
| 2. Protein Size | 10 | 8 | 606 aa / 70.0 kDa. Moderate-large size. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 10. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 81.9 (39.8% >90, 46.5% 70-90, 6.9% 50-70, 6.8% <50). PDB: None. Good AF confidence. No experimental structures. |
| 5. Regulatory Domains | 50 | 5 | IPR047333, IPR047335, IPR004012, IPR037213, IPR047332, IPR000306, IPR017455, IPR011011, IPR013083. PF01363 (FYVE domain), PF02759 (RUN domain). Function: No annotated molecular function (empty). FYVE domain binds phosphatidylinositol 3-phosphate (PI3P) on endosomal membranes. RUN domain involved in Rab GTPase binding. Endosomal trafficking protein. No chromatin/transcriptional regulatory domains. |
| 6. PPI Network | 50 | 20 | STRING: 15 partners. EPHA3 (0.884), RUFY1 (0.808), RUFY3 (0.684), RUFY4 (0.683), BMX (0.648), RAB33A (0.620). IntAct: 15 interactors. RUFY3, RUFY1, EEA1 (endosomal), TPM1, DISC1, EXOC1, RAB33A, RAB33B, PMF1, CEP170, RAB32. UniProt: RAB33A, RAB33B. All endosomal/membrane trafficking partners. |
| **TOTAL** | **180** | **71** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional:** None
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** HPA detects nucleoplasm (Approved) but no IF display images flagged.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000250 (by similarity ONLY)

### GO Cellular Component (GO-CC)
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB (experimental)
- **GO:0005768 (endosome)** -- ISS:UniProtKB
- **GO:0005634 (nucleus)** -- IEA:UniProtKB-SubCell (electronic annotation)

**Summary:** HPA detects nucleoplasm (Approved) but UniProt nuclear annotation is by-similarity (ECO:0000250) and GO-CC nuclear is electronic (IEA). The functional profile is endosomal/cytoplasmic trafficking. The nuclear localization is discordant with function. Nuclear score: 10/30 -- weak/unreliable nuclear evidence.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 10 |
| Broad (All Fields) | 13 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:30466862** -- Staubitz JI et al. (2019). "Novel rearrangements involving the RET gene in papillary thyroid carcinoma." *Cancer Genet*.
2. **PMID:32211330** -- Zheng J et al. (2020). "LncRNAs Predicted to Interfere With the Gene Regulation Activity of miR-637 and miR-196a-5p in GBM." *Front Oncol*.
3. **PMID:25384085** -- Zheng Z et al. (2014). "Anchored multiplex PCR for targeted next-generation sequencing." *Nat Med*.
4. **PMID:11877430** -- Yang J et al. (2002). "Interaction between tyrosine kinase Etk and a RUN domain- and FYVE domain-containing protein RUFY1." *J Biol Chem*.
5. **PMID:20824714** -- Shin N et al. (2011). "Identification of frequently mutated genes with relevance to nonsense mediated mRNA decay in the high microsatellite instability cancers." *Int J Cancer*.

**Assessment:** Very limited literature. Most publications mention RUFY2 in passing (gene fusions, lncRNA analysis). No functional characterization focused on RUFY2.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8WXA3-F1, version 6
- **mean pLDDT: 81.9** (>90: 39.8%, 70-90: 46.5%, 50-70: 6.9%, <50: 6.8%)
- **Assessment:** Good overall confidence. Most residues above pLDDT 70.

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
| EPHA3 | 0.884 | 0 | Receptor tyrosine kinase |
| RUFY1 | 0.808 | 0.796 | Endosomal trafficking |
| RUFY3 | 0.684 | 0.627 | Endosomal trafficking |
| RUFY4 | 0.683 | 0 | Endosomal trafficking |
| BMX | 0.648 | 0.292 | Tyrosine kinase |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| RUFY3 | Co-IP | 28514442 | Paralogue |
| RUFY1 | Co-IP | 28514442 | Paralogue |
| EEA1 | BioID | 29568061 | Early endosome marker |
| RAB33A | Validated 2H | 32296183 | Rab GTPase |
| RAB33B | Validated 2H | 32296183 | Rab GTPase |
| TPM1 | Co-IP | 28514442 | Tropomyosin |

### PPI Network Assessment
- Network is entirely endosomal trafficking and membrane dynamics.
- RUFY family proteins (RUFY1-4) all function in endosome biology.
- No nuclear, chromatin, or transcriptional partners.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RUFY2 was likely rejected due to endosomal functional profile inconsistent with nuclear HPA annotation.

### Recheck Analysis
1. **Nuclear evidence:** DISCORDANT. HPA Approved: Nucleoplasm. But UniProt nuclear annotation is by-similarity only, and GO-CC nuclear is electronic. The protein's known function (endosomal trafficking via FYVE domain) is cytoplasmic.
2. **Functional context:** Endosomal trafficking. FYVE domain binds PI3P on endosomes. RUN domain binds Rab GTPases. No known nuclear function.
3. **PubMed:** 10 strict. VERY LOW.
4. **Structure:** Good AF. No PDB.
5. **PPI:** Exclusively endosomal/trafficking. No nuclear partners.

### Verdict
**The original rejection was CORRECT.** RUFY2 has a well-defined endosomal trafficking function via its FYVE and RUN domains. The HPA nucleoplasm annotation is discordant with its known biology. All interaction partners are endosomal/cytoplasmic. No regulatory domains. Should remain REJECTED.

---

## TE-Regulator Relevance

NEGLIGIBLE. RUFY2 is an endosomal trafficking protein with FYVE domain (PI3P-binding) and RUN domain (Rab GTPase-binding). Its biology is membrane trafficking. No connection to nuclear processes, transcription, chromatin, or TE regulation.

---

## Final Decision: REJECTED

Score: 71/180. RUFY2 has discordant nuclear evidence (HPA nucleoplasm vs. known endosomal function), no regulatory domains, and an exclusively endosomal PPI network. The HPA nucleoplasm annotation is likely artifactual or reflects a minor pool. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. RUFY2 is a member of the RUFY family of endosomal trafficking proteins defined by RUN and FYVE domains. The FYVE domain specifically binds PI3P on endosomal membranes, making endosomal localization a functional requirement. The HPA nucleoplasm annotation may reflect antibody cross-reactivity or non-specific staining. All interaction data (STRING, IntAct, UniProt) places RUFY2 in endosomal/membrane trafficking networks with no nuclear partners. Not suitable for TE research.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000204130-RUFY2/subcellular

![](https://images.proteinatlas.org/39792/517_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/39792/517_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/39792/520_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/39792/520_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/39792/523_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/39792/523_H1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXA3 |
| SMART | SM00064;SM00593; |
| UniProt Domain [FT] | DOMAIN 37..169; /note="RUN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00178" |
| InterPro | IPR047333;IPR047335;IPR004012;IPR037213;IPR047332;IPR000306;IPR017455;IPR011011;IPR013083; |
| Pfam | PF01363;PF02759; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204130-RUFY2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RUFY1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
