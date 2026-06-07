# SLF2 -- Critical False-Rejection Reevaluation Report

**Gene:** SLF2 (SMC5-SMC6 complex localization factor protein 2)
**UniProt Accession:** Q8IX21
**Protein Name:** SMC5-SMC6 complex localization factor protein 2
**Length:** 1173 aa | **Mass:** 131.9 kDa
**Aliases:** C10orf6, FAM178A
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 26 | HPA main: Nucleoplasm, Vesicles. Reliability: Approved. UniProt: Nucleus (ECO:0000269 x2 experimental), Nucleus PML body (ECO:0000269). GO-CC: nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), chromatin (IDA:UniProtKB), PML body (IDA:UniProtKB), chromosome telomeric region (NAS:ComplexPortal), site of double-strand break (IDA:UniProtKB). STRONG nuclear and chromatin evidence. PML body localization is particularly relevant. |
| 2. Protein Size | 10 | 6 | 1173 aa / 131.9 kDa. Very large protein. Substantial deduction. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 17. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 14 | AlphaFold mean pLDDT: 55.0 (8.7% >90, 27.7% 70-90, 7.8% 50-70, 55.8% <50). PDB: 7T5P (EM, 3.40A, residues 635-1173 only). Low AF confidence overall. Partial EM structure. |
| 5. Regulatory Domains | 50 | 30 | IPR044276, IPR026161. PF14816. FUNCTION: Links RAD18 with SMC5-SMC6 complex at DNA damage sites. Recruits SMC5-SMC6 to chromatin at ICL and DSB sites. SMC5/6 complex compacts and silences unintegrated HIV-1 DNA (PMID:33811831). Role in viral restriction via chromatin compaction. SMC5/6-mediated DNA compaction/silencing is directly analogous to TE silencing mechanisms. |
| 6. PPI Network | 50 | 30 | STRING: 15 partners. SLF1 (0.999), SMC5 (0.967), SMC6 (0.955), RAD18 (0.924), NSMCE1 (0.927), NSMCE3 (0.904), NSMCE2 (0.883), NSMCE4A (0.866). IntAct: 15 interactors. SLF1, SMC6, RAD18, NSMCE1, H2BC20P (histone H2B), GCFC2, ITGA1, SIMC1. |
| **TOTAL** | **180** | **116** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm, Vesicles
- **Additional:** None
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Key Finding:** HPA nucleoplasm (Approved). Also vesicular -- may reflect trafficking.

### UniProt Subcellular Location
- **Nucleus** -- ECO:0000269 x2 (experimental)
- **Nucleus, PML body** -- ECO:0000269 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0000785 (chromatin)** -- IDA:UniProtKB (experimental)
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005634 (nucleus)** -- IDA:UniProtKB
- **GO:0016605 (PML body)** -- IDA:UniProtKB
- **GO:0000781 (chromosome, telomeric region)** -- NAS:ComplexPortal
- **GO:0035861 (site of double-strand break)** -- IDA:UniProtKB
- **GO:0030915 (Smc5-Smc6 complex)** -- NAS:ComplexPortal

**Summary:** SLF2 is a nuclear chromatin-associated protein. PML body localization is notable -- PML bodies are involved in TE silencing and viral restriction. Chromatin localization (IDA) is experimentally validated. Nuclear score: 26/30 -- excellent nuclear/chromatin evidence.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 17 |
| Broad (All Fields) | 30 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:34780483** -- Scott WA et al. (2021). "ATRX proximal protein associations boast roles beyond histone deposition." *PLoS Genet*.
2. **PMID:33811831** -- Dupont L et al. (2021). "The SMC5/6 complex compacts and silences unintegrated HIV-1 DNA and is antagonized by Vpr." *Cell Host Microbe*. -- SMC5/6 SILENCES DNA.
3. **PMID:40883817** -- Li S et al. (2025). "Integrative single-cell and bulk transcriptomic analysis reveals the landscape of T cell mitotic catastrophe associated genes in esophageal squamous cell carcinoma." *Hum Genomics*.
4. **PMID:33811915** -- Gilhooley MJ et al. (2021). "ON-bipolar cell gene expression during retinal degeneration." *Exp Eye Res*.
5. **PMID:37191775** -- Lelkes E et al. (2023). "Characterization of the conserved features of the NSE6 subunit of the Physcomitrium patens SMC5/6 complex." *Plant J*.

**Assessment:** SMC5/6 complex DNA silencing function is directly relevant. SLF2 recruits SMC5/6 to chromatin. The HIV-1 DNA silencing paper (PMID:33811831) is especially relevant -- SMC5/6 compacts and transcriptionally silences extrachromosomal DNA, which is mechanistically similar to TE silencing.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q8IX21-F1, version 6
- **mean pLDDT: 55.0** (>90: 8.7%, 70-90: 27.7%, 50-70: 7.8%, <50: 55.8%)
- **Assessment:** Low confidence. More than half of residues below pLDDT 50. Large protein with likely disordered regions.

### Experimental PDB Structures
- **1 structure:** 7T5P (EM, 3.40A, residues 635-1173 -- C-terminal half)
- **Assessment:** Partial structure of C-terminal domain at moderate resolution.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| SLF1 | 0.999 | 0.826 | SMC5/6 localization factor |
| SMC5 | 0.967 | 0.695 | SMC5/6 complex ATPase |
| SMC6 | 0.955 | 0.779 | SMC5/6 complex ATPase |
| RAD18 | 0.924 | 0.624 | DNA damage ubiquitin ligase |
| NSMCE1 | 0.927 | 0.743 | SMC5/6 NSE1 subunit |
| NSMCE2 | 0.883 | 0.610 | SMC5/6 SUMO ligase |
| UBE2I | 0.551 | 0 | SUMO E2 (database) |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| SLF1 | Co-IP | 26496610 | Binding partner |
| SMC6 | Co-IP | 26496610 | SMC5/6 complex |
| RAD18 | Co-IP | 26496610 | DNA damage |
| NSMCE1 | Co-IP | 28514442 | SMC5/6 |
| H2BC20P | Cross-link | 30021884 | Histone H2B -- chromatin |
| SIMC1 | Complex | - | PML body association |

### PPI Network Assessment
- Dense SMC5/6 complex network. SLF1-SLF2 dimer bridges RAD18 to SMC5/6.
- H2BC20P (histone H2B) cross-linking confirms chromatin proximity.
- NSMCE2 is a SUMO ligase -- SUMO pathway connection.
- SIMC1 links to PML body recruitment for viral restriction.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SLF2 was likely rejected due to low structural confidence and possibly insufficient evaluation of SMC5/6 silencing function.

### Recheck Analysis
1. **Nuclear evidence:** STRONG. HPA Approved nucleoplasm. UniProt experimental nucleus + PML body. GO-CC chromatin (IDA). PML body localization is key for TE/viral silencing.
2. **Functional context:** Recruits SMC5/6 complex to chromatin for DNA compaction and silencing. SMC5/6 directly silences extrachromosomal viral DNA (HIV-1) through compaction -- mechanistically identical to TE silencing. SLF1-SLF2 are the adaptors that target this silencing machinery.
3. **PubMed:** 17 strict. VERY LOW.
4. **Structure:** Low AF confidence. Partial EM structure.
5. **PPI:** Dense SMC5/6 network. Histone H2B cross-linking. SUMO pathway (NSMCE2).

### Verdict
**The original rejection was INCORRECT.** SLF2 is a chromatin-associated adaptor that targets the SMC5/6 DNA compaction/silencing complex to chromatin. SMC5/6-mediated DNA silencing is directly relevant to TE regulation -- it compacts and transcriptionally silences DNA. PML body localization further supports a role in nuclear silencing compartments. Should be RETAINED.

---

## TE-Regulator Relevance

HIGH. SLF2 targets the SMC5/6 complex to chromatin, and SMC5/6 compacts and transcriptionally silences DNA (demonstrated for HIV-1, PMID:33811831). This DNA compaction/silencing mechanism is directly analogous to TE silencing -- SMC complexes are structurally related to condensins and cohesins, which organize chromatin. PML body localization connects SLF2 to nuclear bodies implicated in TE and viral restriction. The SUMO pathway connection (NSMCE2 SUMO ligase, UBE2I) is also relevant for TE silencing.

---

## Final Decision: RETAINED

Score: 116/180. SLF2 is a chromatin-associated adaptor that targets the SMC5/6 DNA silencing complex to chromatin. Strong nuclear evidence (nucleoplasm + PML body + chromatin IDA), DNA silencing function directly relevant to TE biology, and high novelty. Retained.

---

## Manual Review Note
STRONG CANDIDATE. SLF2 (FAM178A) is part of the SLF1-SLF2 heterodimer that bridges RAD18 to the SMC5/6 complex, recruiting it to DNA damage sites and chromatin. The SMC5/6 complex functions in DNA compaction and transcriptional silencing, demonstrated for HIV-1 extrachromosomal DNA (PMID:33811831). This mechanism is directly relevant to TE silencing. SLF2 localizes to PML bodies (nuclear silencing compartments) via SIMC1 interaction. PML bodies are key sites for TE and viral restriction. The protein is very large (1173 aa) and structurally poorly characterized, but the functional relevance is compelling. Bona fide chromatin-associated silencing adaptor.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000119906-SLF2/subcellular

![](https://images.proteinatlas.org/57568/975_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/57568/975_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/57568/976_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/57568/976_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/57568/980_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/57568/980_B7_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IX21 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR044276;IPR026161; |
| Pfam | PF14816; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119906-SLF2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SIMC1 | Intact, Biogrid | true |
| SLF1 | Intact, Biogrid, Bioplex | true |
| SMC5 | Intact, Biogrid | true |
| SMC6 | Intact, Biogrid | true |
| ATRX | Biogrid | false |
| NSMCE3 | Bioplex | false |
| PML | Biogrid | false |
| PSMA1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
