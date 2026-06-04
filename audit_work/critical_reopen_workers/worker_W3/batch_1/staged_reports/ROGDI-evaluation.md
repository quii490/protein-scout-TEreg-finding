# ROGDI -- Critical False-Rejection Reevaluation Report

**Gene:** ROGDI
**UniProt Accession:** Q9GZN7
**Protein Name:** Protein rogdi homolog
**Length:** 287 aa | **Mass:** 32.3 kDa
**Aliases:** None
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 12 | UniProt: Nucleus envelope (ECO:0000269 -- experimental), Presynapse (ECO:0000250), Cell projection axon (ECO:0000250), Perikaryon (ECO:0000250), Cell projection dendrite (ECO:0000250), Synaptic vesicle (ECO:0000250). GO-CC: nuclear envelope (IDA:HGNC), axon, dendrite, synaptic vesicle. HPA: localization available but no subcellular location data (reliability=null, all location lists empty). Nuclear annotation is specifically "nuclear envelope" -- nuclear periphery, not nuclear interior. The bulk of localization evidence is neuronal/synaptic. |
| 2. Protein Size | 10 | 10 | 287 aa / 32.3 kDa. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 31. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 26 | AlphaFold mean pLDDT: 89.3 (72.5% >90, 18.8% 70-90, 3.1% 50-70, 5.6% <50). PDB: 5XQH (X-ray, 2.04A, residues 11-276), 5XQI (X-ray, 2.80A, full length 1-287). Excellent confidence and two experimental structures. |
| 5. Regulatory Domains | 50 | 5 | IPR028241. PF10259. Function: No annotated molecular function (empty function field). Known for association with Kohlschutter-Tonz syndrome (intellectual disability, epilepsy, enamel defects). No chromatin, transcriptional, or epigenetic regulatory domains. |
| 6. PPI Network | 50 | 15 | STRING: 15 partners. DMXL1 (0.969), DMXL2 (0.958), WDR7 (0.893), ATP6V1E1 (0.747), ATP6V1B2 (0.722). All top partners are V-ATPase components. IntAct: 15 interactors, mostly Drosophila ortholog interactions and a few human (COPS6, CEP126, CALM1, DISC1). UniProt: CEP63 (3 experiments). Network is centered on V-ATPase complex. |
| **TOTAL** | **180** | **78** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** null
- **Main Location:** No data (empty list)
- **Additional:** No data (empty list)
- **IF Image Status:** no_image_detected
- **Key Finding:** HPA has gene page and subcellular page but does not report any subcellular localization or IF data.

### UniProt Subcellular Location
- **Nucleus envelope** -- ECO:0000269 (experimental) -- sole experimental annotation
- **Presynapse** -- ECO:0000250 (by similarity)
- **Cell projection, axon** -- ECO:0000250
- **Perikaryon** -- ECO:0000250
- **Cell projection, dendrite** -- ECO:0000250
- **Cytoplasmic vesicle, secretory vesicle, synaptic vesicle** -- ECO:0000250

### GO Cellular Component (GO-CC)
- **GO:0005635 (nuclear envelope)** -- IDA:HGNC
- **GO:0043291 (RAVE complex)** -- IBA:GO_Central
- **GO:0030424 (axon)** -- IEA:UniProtKB-SubCell
- **GO:0030425 (dendrite)** -- IEA:UniProtKB-SubCell
- **GO:0008021 (synaptic vesicle)** -- IEA:UniProtKB-SubCell

**Summary:** The only nuclear annotation is nuclear envelope (nuclear periphery, not interior). The bulk of evidence places ROGDI at neuronal compartments (synapse, axon, dendrite) and the RAVE/V-ATPase complex. Nuclear score: 12/30 -- nuclear periphery only, not nuclear interior.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 31 |
| Broad (All Fields) | 39 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:40646309** -- Nardone C et al. (2025). "A heterotrimeric protein complex assembles the metazoan V-ATPase upon dissipation of proton gradients." *Nat Struct Mol Biol*.
2. **PMID:27600704** -- Schossig A et al. (2017). "SLC13A5 is the second gene associated with Kohlschutter-Tonz syndrome." *J Med Genet*.
3. **PMID:29150638** -- Riemann D et al. (2017). "The Kohlschutter-Tonz syndrome associated gene Rogdi encodes a novel presynaptic protein." *Sci Rep*.
4. **PMID:37974187** -- Meng L et al. (2023). "Perampanel effectiveness in treating ROGDI-related Kohlschutter-Tonz syndrome." *BMC Med Genomics*.
5. **PMID:40175429** -- Zuo W, Wang Z (2025). "Identification of ulcerative colitis diagnostic markers from differentially expressed genes shared with Hirschsprung disease." *Sci Rep*.

**Assessment:** Literature is focused on Kohlschutter-Tonz syndrome and V-ATPase complex function. No TE-related publications.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9GZN7-F1, version 6
- **mean pLDDT: 89.3** (>90: 72.5%, 70-90: 18.8%, 50-70: 3.1%, <50: 5.6%)
- **Assessment:** Excellent confidence. Compact, well-folded protein.

### Experimental PDB Structures
- **2 structures:** 5XQH (X-ray, 2.04A, residues 11-276), 5XQI (X-ray, 2.80A, full length 1-287)
- **Assessment:** Excellent experimental structural coverage at high resolution.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| DMXL1 | 0.969 | 0.886 | V-ATPase assembly factor |
| DMXL2 | 0.958 | 0.702 | V-ATPase assembly factor |
| WDR7 | 0.893 | 0.767 | V-ATPase associated |
| ATP6V1E1 | 0.747 | 0.672 | V-ATPase subunit |
| ATP6V1B2 | 0.722 | 0.659 | V-ATPase subunit |
| SKP1 | 0.607 | 0.412 | SCF ubiquitin ligase |

### IntAct (15 interactors)
Mostly Drosophila ortholog (Rogdi) interactions. Human: COPS6 (COP9 signalosome), CEP126 (centrosomal), CALM1 (calmodulin), DISC1.

### PPI Network Assessment
- Network is centered on V-ATPase complex and RAVE complex.
- No chromatin or transcriptional regulatory partners.
- COP9 signalosome interaction (COPS6) is marginally interesting for protein degradation pathways.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
ROGDI was likely rejected due to absent nuclear interior localization and no regulatory domain function.

### Recheck Analysis
1. **Nuclear evidence:** VERY WEAK. Only nuclear envelope annotation (periphery). HPA has no localization data. Bulk of evidence is neuronal/synaptic.
2. **Functional context:** No annotated molecular function. Associated with V-ATPase assembly (RAVE complex). Presynaptic protein.
3. **PubMed:** 31 strict. LOW but not extremely so.
4. **Structure:** Excellent (2 PDB structures, high AF confidence).
5. **PPI:** V-ATPase complex centered. No chromatin partners.

### Verdict
**The original rejection was CORRECT.** ROGDI is a presynaptic/neuronal protein associated with the V-ATPase/RAVE complex. The nuclear envelope annotation is peripheral, not nuclear interior. No chromatin, transcriptional, or epigenetic regulatory domains or functions. No TE-relevant PPI connections. Should remain REJECTED.

---

## TE-Regulator Relevance

VERY LOW. ROGDI is a neuronal protein associated with V-ATPase assembly. Its sole nuclear connection is nuclear envelope localization, which is functionally distinct from nuclear interior chromatin regulation. No evidence supports any role in transcription, chromatin modification, or TE silencing.

---

## Final Decision: REJECTED

Score: 78/180. ROGDI has excellent structural data but very weak nuclear evidence (nuclear envelope only), no regulatory domain function, and a neuronal/synaptic functional profile centered on V-ATPase biology. Not suitable for TE-regulatory investigation. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. ROGDI is a presynaptic protein involved in V-ATPase proton pump assembly and is associated with Kohlschutter-Tonz syndrome (neurodevelopmental disorder). The nuclear envelope localization is likely related to ER/nuclear envelope continuum, not nuclear interior function. Excellent structural data (two X-ray structures at high resolution) but functional profile is entirely unrelated to TE biology.
