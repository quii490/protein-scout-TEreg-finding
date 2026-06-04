# SNTG1 -- Critical False-Rejection Reevaluation Report

**Gene:** SNTG1 (Gamma-1-syntrophin)
**UniProt Accession:** Q9NSN8
**Protein Name:** Gamma-1-syntrophin
**Length:** 517 aa | **Mass:** 58.0 kDa
**Aliases:** None
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 10 | UniProt: Cytoplasm cytoskeleton, Nucleus (no evidence code). GO-CC: nucleus (IEA:UniProtKB-SubCell -- electronic), cytoplasm (IDA:UniProtKB), cytoskeleton (IDA:LIFEdb), dystrophin-associated glycoprotein complex (IBA:GO_Central), syntrophin complex (TAS:ProtInc). Nuclear annotation has NO evidence code in UniProt and is electronic in GO-CC. HPA: no localization data (reliability=null, empty). Very weak nuclear evidence. |
| 2. Protein Size | 10 | 8 | 517 aa / 58.0 kDa. Moderate size. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 16. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 82.3 (62.3% >90, 18.0% 70-90, 5.4% 50-70, 14.3% <50). PDB: 7PC7 (X-ray, 2.10A, residues 54-143), 7PC8 (X-ray, 2.50A, 54-143), 7QQN (X-ray, 2.45A, 54-143). Good AF. 3 X-ray structures of the PDZ domain. |
| 5. Regulatory Domains | 50 | 5 | IPR001478 (PDZ), IPR036034, IPR001849 (PH), IPR015482, IPR055108. PF00595 (PDZ), PF23012. FUNCTION: Adapter protein linking receptors to actin cytoskeleton and dystrophin glycoprotein complex. May regulate DGK-zeta subcellular location. Scaffolding/adaptor -- no catalytic or chromatin regulatory domains. |
| 6. PPI Network | 50 | 25 | STRING: 15 partners. DMD (0.992), DTNB (0.951), SNTA1 (0.938), DTNA (0.877), SNTB1 (0.874), SNTB2 (0.844), DAG1 (0.839), UTRN (0.798). IntAct: 15 interactors. PLEKHA2, VTN, CES2, RNASEH1, DTNB, MLYCD, DMD, ACADSB, UTRN, CTBP2, SNTA1, SNTB2, SNTB1, LRRC4B, CTNNAL1. |
| **TOTAL** | **180** | **76** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** null
- **Main Location:** No data (empty lists)
- **Additional:** No data (empty lists)
- **IF Image Status:** no_image_detected
- **Key Finding:** HPA has gene page but provides NO subcellular localization data whatsoever.

### UniProt Subcellular Location
- **Cytoplasm, cytoskeleton** -- no evidence code
- **Nucleus** -- no evidence code

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** -- IEA:UniProtKB-SubCell (electronic annotation)
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:0005856 (cytoskeleton)** -- IDA:LIFEdb
- **GO:0016010 (dystrophin-associated glycoprotein complex)** -- IBA:GO_Central
- **GO:0032587 (ruffle membrane)** -- IDA:UniProtKB
- **GO:0016013 (syntrophin complex)** -- TAS:ProtInc

**Summary:** SNTG1's nuclear annotation is extremely weak. UniProt has no evidence code for nucleus. GO-CC nucleus is electronic (IEA) only. HPA has no localization data. The experimentally validated locations are cytoplasmic/cytoskeletal/membrane. Nuclear score: 10/30 -- essentially no reliable nuclear evidence.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 16 |
| Broad (All Fields) | 24 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:39738056** -- Yang MY et al. (2024). "SEAD reference panel with 22,134 haplotypes boosts rare variant imputation and genome-wide association analysis in Asian populations." *Nat Commun*.
2. **PMID:15088139** -- Bashiardes S et al. (2004). "SNTG1, the gene encoding gamma1-syntrophin: a candidate gene for idiopathic scoliosis." *Hum Genet*.
3. **PMID:37982029** -- Broadwin M et al. (2023). "Extracellular vesicle treatment partially reverts epigenetic alterations in chronically ischemic porcine myocardium." *Vessel Plus*.
4. **PMID:34048959** -- Tassano E et al. (2021). "Scoliosis with cognitive impairment in a girl with 8q11.21q11.23 microdeletion and SNTG1 disruption." *Bone*.
5. **PMID:21151896** -- Job B et al. (2010). "Genomic aberrations in lung adenocarcinoma in never smokers." *PLoS One*.

**Assessment:** SNTG1 is studied as a candidate gene for idiopathic scoliosis. Most mentions are from GWAS/genomic studies. No functional characterization.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NSN8-F1, version 6
- **mean pLDDT: 82.3** (>90: 62.3%, 70-90: 18.0%, 50-70: 5.4%, <50: 14.3%)
- **Assessment:** Good confidence overall.

### Experimental PDB Structures
- **3 structures:** 7PC7 (X-ray, 2.10A, residues 54-143), 7PC8 (X-ray, 2.50A, 54-143), 7QQN (X-ray, 2.45A, 54-143) -- all PDZ domain only
- **Assessment:** PDZ domain well-characterized at high resolution. Rest of protein not structurally covered.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| DMD | 0.992 | 0.648 | Dystrophin |
| DTNB | 0.951 | 0.619 | Dystrobrevin beta |
| SNTA1 | 0.938 | 0.597 | Syntrophin alpha-1 |
| DTNA | 0.877 | 0.482 | Dystrobrevin alpha |
| SNTB1 | 0.874 | 0.494 | Syntrophin beta-1 |
| SNTB2 | 0.844 | 0.448 | Syntrophin beta-2 |
| DAG1 | 0.839 | 0 | Dystroglycan |
| UTRN | 0.798 | 0.435 | Utrophin |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| DMD | Co-IP | 33961781 | Dystrophin |
| UTRN | Co-IP | 33961781 | Utrophin |
| SNTA1 | Co-IP | 33961781 | Syntrophin alpha-1 |
| SNTB1 | Co-IP | 33961781 | Syntrophin beta-1 |
| SNTB2 | Co-IP | 33961781 | Syntrophin beta-2 |
| DTNB | Co-IP | 33961781 | Dystrobrevin |
| CTBP2 | Co-IP | 33961781 | Transcriptional corepressor |
| CTNNAL1 | Co-IP | 33961781 | Catenin alpha-like |

### PPI Network Assessment
- Core network is dystrophin-associated glycoprotein complex (DGC).
- Syntrophin family interactions (SNTA1, SNTB1, SNTB2) confirm scaffolding role.
- CTBP2 interaction is interesting -- CTBP2 is a transcriptional corepressor. However, this is from a single high-throughput Co-IP study and may not reflect a functional nuclear interaction.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SNTG1 was likely rejected due to absent nuclear evidence and non-regulatory scaffolding function.

### Recheck Analysis
1. **Nuclear evidence:** ESSENTIALLY ABSENT. HPA has no localization data. UniProt nuclear annotation has no evidence code. GO-CC nucleus is electronic (IEA) only. All experimentally validated locations are cytoplasmic/cytoskeletal.
2. **Functional context:** Scaffolding adapter in the dystrophin-associated glycoprotein complex. Syntrophin family. No catalytic or regulatory function.
3. **PubMed:** 16 strict. LOW.
4. **Structure:** PDZ domain well-characterized. Good AF.
5. **PPI:** Dystrophin complex. CTBP2 association is from a single high-throughput study.

### Verdict
**The original rejection was CORRECT.** SNTG1 is a syntrophin family scaffolding protein that functions in the dystrophin-associated glycoprotein complex. Nuclear evidence is essentially non-existent (no evidence code in UniProt, electronic only in GO-CC, no HPA data). No regulatory domains or functions. Should remain REJECTED.

---

## TE-Regulator Relevance

NEGLIGIBLE. SNTG1 is a PDZ/PH domain scaffolding protein in the syntrophin/dystrophin complex. Its biology is structural organization of membrane protein complexes. No evidence for nuclear function or TE-regulatory activity.

---

## Final Decision: REJECTED

Score: 76/180. SNTG1 has essentially no nuclear evidence (UniProt nucleus lacks evidence code, GO-CC is electronic, HPA has no data), no regulatory domains, and a dedicated membrane/cytoskeletal scaffolding function. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. SNTG1 (gamma-1-syntrophin) is the least characterized member of the syntrophin family. Like other syntrophins, its function is adapter/scaffolding in the dystrophin-associated glycoprotein complex. The nuclear annotation in UniProt has NO evidence code, and GO-CC classifies it as electronic (IEA). HPA provides no localization data. The CTBP2 interaction from a high-throughput study is the only hint of a nuclear connection, but this is insufficient to establish a nuclear function. Not suitable for TE investigation.
