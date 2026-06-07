# SNTB2 -- Critical False-Rejection Reevaluation Report

**Gene:** SNTB2 (Beta-2-syntrophin)
**UniProt Accession:** Q13425
**Protein Name:** Beta-2-syntrophin
**Length:** 540 aa | **Mass:** 58.0 kDa
**Aliases:** D16S2531E, SNT2B2, SNTL
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 10 | HPA main: Golgi apparatus, Plasma membrane, Centriolar satellite, Basal body. Additional: Nucleoplasm, Primary cilium transition zone. Reliability: Approved. UniProt: Membrane, Secretory vesicle membrane, Cell junction, Cytoplasm cytoskeleton. NO nuclear UniProt annotation. GO-CC: nucleoplasm (IDA:HPA). Nucleoplasm is ADDITIONAL HPA location only. The primary localization is membrane/cytoskeletal/ciliary. |
| 2. Protein Size | 10 | 8 | 540 aa / 58.0 kDa. Moderate size. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 14. Novelty rule: 1-50=10. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 78.7 (51.1% >90, 22.8% 70-90, 6.1% 50-70, 20.0% <50). PDB: 2VRF (X-ray, 2.00A, residues 112-200 only -- PDZ domain). Good AF but limited PDB coverage. |
| 5. Regulatory Domains | 50 | 5 | IPR001478 (PDZ), IPR036034, IPR011993, IPR001849 (PH), IPR041428, IPR015482, IPR055108. PF00595 (PDZ), PF00169 (PH), PF18012, PF23012. FUNCTION: Adapter protein linking membrane proteins to actin cytoskeleton and dystrophin glycoprotein complex. Scaffolding/adaptor -- no catalytic, chromatin, or transcriptional regulatory domains. |
| 6. PPI Network | 50 | 25 | STRING: 15 partners. UTRN (0.990), DMD (0.985), DTNA (0.974), DTNB (0.937), SNTG2 (0.927), SNTB1 (0.923), SNTA1 (0.905), DAG1 (0.901), ADRA1D (0.874). IntAct: 15 interactors. DMD, UTRN, ABCA1, PTPRN, MARK2, LIN7A, MCM7, ESR1, DAG1. |
| **TOTAL** | **180** | **76** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Golgi apparatus, Plasma membrane, Centriolar satellite, Basal body
- **Additional:** Nucleoplasm, Primary cilium transition zone
- **IF Image Status:** if_display_images_available (6 blue_red_green images)
- **Key Finding:** Nucleoplasm is ADDITIONAL only. Primary locations are membrane/cytoskeletal/ciliary. HPA IF images show Golgi/membrane/ciliary staining, not nuclear.

### UniProt Subcellular Location
- **Membrane** -- no evidence code
- **Cytoplasmic vesicle, secretory vesicle membrane** -- no evidence code
- **Cell junction** -- ECO:0000250
- **Cytoplasm, cytoskeleton** -- no evidence code
- **NO nuclear annotation in UniProt**

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** -- IDA:HPA
- **GO:0005737 (cytoplasm)** -- IDA:UniProtKB
- **GO:0005794 (Golgi apparatus)** -- IDA:HPA
- **GO:0005886 (plasma membrane)** -- IDA:HPA
- **GO:0034451 (centriolar satellite)** -- IDA:HPA
- **GO:0016010 (dystrophin-associated glycoprotein complex)** -- IBA:GO_Central
- **GO:0045202 (synapse)** -- IBA:GO_Central

**Summary:** SNTB2 is primarily a membrane-associated adapter protein. Nucleoplasm is an HPA additional location only -- not supported by UniProt. The functional profile is entirely consistent with membrane/cytoskeletal scaffolding. Nuclear score: 10/30 -- very weak nuclear evidence (additional HPA only).

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 14 |
| Broad (All Fields) | 15 |

**Novelty score: 10/10.**

### Key Papers
1. **PMID:25625330** -- Hebel T et al. (2015). "Lipid abnormalities in alpha/beta2-syntrophin null mice are independent from ABCA1." *Biochim Biophys Acta*.
2. **PMID:30014220** -- Krautbauer S et al. (2019). "The utrophin-beta 2 syntrophin complex regulates adipocyte lipid droplet size independent of adipogenesis." *Mol Cell Biochem*.
3. **PMID:30990585** -- Krautbauer S et al. (2019). "Adipocyte Hypertrophy and Improved Postprandial Lipid Response in Beta 2 Syntrophin Deficient Mice." *Cell Physiol Biochem*.
4. **PMID:23860432** -- Neumeier M et al. (2013). "Adiponectin receptor 1 C-terminus interacts with PDZ-domain proteins such as syntrophins." *Exp Mol Pathol*.
5. **PMID:26079703** -- Eisinger K et al. (2015). "Evaluation of the specificity of four commercially available antibodies to alpha-syntrophin." *Anal Biochem*.

**Assessment:** Literature is focused on SNTB2's role in adipocyte biology, lipid metabolism, and dystrophin complex function. No TE-related publications.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q13425-F1, version 6
- **mean pLDDT: 78.7** (>90: 51.1%, 70-90: 22.8%, 50-70: 6.1%, <50: 20.0%)
- **Assessment:** Moderate-good confidence. Some disordered regions.

### Experimental PDB Structures
- **1 structure:** 2VRF (X-ray, 2.00A, residues 112-200 -- PDZ domain only)
- **Assessment:** Only the PDZ domain is structurally characterized. The rest of the protein has no experimental structure.

### PAE
- PAE image URL available.
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| UTRN | 0.990 | 0.800 | Utrophin (dystrophin homolog) |
| DMD | 0.985 | 0.777 | Dystrophin |
| DTNA | 0.974 | 0.749 | Dystrobrevin |
| DTNB | 0.937 | 0.762 | Dystrobrevin |
| SNTG2 | 0.927 | 0.708 | Syntrophin gamma-2 |
| DAG1 | 0.901 | 0.336 | Dystroglycan |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| DMD/Dmd | Co-IP | 9214383, 8576247 | Dystrophin |
| UTRN | Co-IP | 8576247 | Utrophin |
| ABCA1 | Affinity chrom. | 16192269 | Cholesterol transporter |
| ESR1 | TAP | 31527615 | Estrogen receptor |
| MCM7 | Co-IP | 23764002 | DNA replication |
| MARK2 | Co-IP | 19615732 | Polarity kinase |

### PPI Network Assessment
- Core network is dystrophin-associated glycoprotein complex (DGC).
- ESR1 (estrogen receptor) and MCM7 (DNA replication) interactions suggest some nuclear connections.
- Primarily a membrane/cytoskeletal scaffolding network.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SNTB2 was likely rejected due to primarily membrane/cytoskeletal localization and non-regulatory scaffolding function.

### Recheck Analysis
1. **Nuclear evidence:** VERY WEAK. Nucleoplasm is HPA additional only. UniProt has NO nuclear annotation. Primary localization is membrane/cytoskeletal.
2. **Functional context:** Scaffolding adapter. Links membrane proteins to actin cytoskeleton and dystrophin complex. No catalytic or regulatory function.
3. **PubMed:** 14 strict. LOW.
4. **Structure:** PDZ domain only solved. Moderate AF confidence.
5. **PPI:** Dystrophin complex. ESR1 and MCM7 interactions are notable nuclear connections but insufficient to establish a nuclear function.

### Verdict
**The original rejection was CORRECT.** SNTB2 is a membrane-associated scaffolding protein (syntrophin family) with primary function in dystrophin complex organization at the plasma membrane and cytoskeleton. The nucleoplasm HPA annotation is additional only and not supported by UniProt. No chromatin, transcriptional, or TE-regulatory function. Should remain REJECTED.

---

## TE-Regulator Relevance

NEGLIGIBLE. SNTB2 is a PDZ/PH domain scaffolding protein that organizes the dystrophin-associated glycoprotein complex at membranes. Its biology is entirely structural/scaffolding at the membrane-cytoskeleton interface. No evidence for nuclear function beyond a secondary HPA nucleoplasm annotation.

---

## Final Decision: REJECTED

Score: 76/180. SNTB2 has very weak nuclear evidence (HPA additional only, no UniProt nuclear), no regulatory domain function, and a dedicated membrane/cytoskeletal scaffolding role. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. SNTB2 (beta-2-syntrophin) is a member of the syntrophin family of dystrophin-associated scaffold proteins. Its well-characterized function is in organizing the dystrophin glycoprotein complex at the sarcolemma and other plasma membrane domains. The nucleoplasm HPA annotation is classified as "additional" and is not corroborated by UniProt subcellular location data. HPA IF images show membrane/Golgi/centriolar staining, not nuclear. No evidence supports a chromatin or TE-regulatory function.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13425 |
| SMART | SM00228;SM00233; |
| UniProt Domain [FT] | DOMAIN 115..198; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 163..300; /note="PH 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 325..437; /note="PH 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 484..540; /note="SU" |
| InterPro | IPR001478;IPR036034;IPR011993;IPR001849;IPR041428;IPR015482;IPR055108; |
| Pfam | PF00595;PF00169;PF18012;PF23012; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168807-SNTB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABCA1 | Intact, Biogrid | true |
| ADRA1D | Intact, Biogrid | true |
| CASK | Intact, Biogrid | true |
| DMD | Intact, Biogrid | true |
| UTRN | Intact, Biogrid, Opencell | true |
| ANLN | Biogrid | false |
| CFAP36 | Intact | false |
| DTNA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
