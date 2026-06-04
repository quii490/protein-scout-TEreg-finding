# RIOX1 -- Critical False-Rejection Reevaluation Report

**Gene:** RIOX1 (Ribosomal oxygenase 1)
**UniProt Accession:** Q9H6W3
**Protein Name:** Ribosomal oxygenase 1
**Length:** 641 aa | **Mass:** 71.1 kDa
**Aliases:** C14orf169, MAPJD, NO66
**Report Date:** 2026-06-04
**Review Stage:** W3 Batch 1 -- CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA main: Nucleoli rim (Supported). HPA IF images available (blue_red_green). UniProt: Nucleus nucleolus (ECO:0000269 x2), Nucleus nucleoplasm (ECO:0000269). GO-CC: nucleolus (IDA:HPA), nucleoplasm (TAS:Reactome), nucleus (ISS:UniProtKB). Strong nuclear evidence -- nucleolar localization confirmed by multiple independent sources. |
| 2. Protein Size | 10 | 8 | 641 aa / 71.1 kDa. Moderate-large size, slight deduction. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 7. Novelty rule: 1-50=10. Very few publications. Highly novel target. |
| 4. 3D Structure | 30 | 26 | AlphaFold mean pLDDT: 79.9 (70.4% >90, 1.6% 70-90, 0.2% 50-70, 27.9% <50). PDB: 10 structures (4CCJ 2.15A, 4CCK 2.15A, 4CCM 2.51A, 4CCN 2.23A, 4CCO 2.30A, 4DIQ 2.40A, 4E4H 2.28A, 4Y33 2.70A, 4Y3O 2.20A, 4Y4R 3.30A). Extensive experimental structural coverage of catalytic domain (residues ~176-641). |
| 5. Regulatory Domains | 50 | 45 | IPR003347, IPR039994, IPR049043. PF08007, PF21233. KEY FUNCTION: Histone lysine demethylase -- specifically demethylates H3K4me3, H3K4me1, and H3K36me2. This is a DIRECT epigenetic regulatory activity. Also hydroxylates ribosomal protein L8. Participates in MYC-induced transcriptional activation. Demethylates cGAS. RIOX1 is a BONA FIDE histone modifier with direct chromatin-level regulatory function. |
| 6. PPI Network | 50 | 35 | STRING: 15 partners including RPL8 (0.986), PHF19 (0.940), SP7 (0.920), RIOK1 (0.807). PHF19 is a Polycomb component -- relevant for chromatin. MYC (0.604 experimental). IntAct: 15 interactors including MKI67 (proliferation marker), HNRNPU (RNA-binding), EIF3A (translation initiation), NOP56 (nucleolar), multiple ribosomal proteins. UniProt: SP7 (6 experiments). Network connects ribosomal biogenesis with chromatin/transcription. |
| **TOTAL** | **180** | **152** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoli rim
- **Additional:** None
- **IF Image Status:** if_display_images_available (6 blue_red_green images)
- **Key Finding:** Strong nucleolar rim staining pattern, consistent with nucleolar localization.

### UniProt Subcellular Location
- **Nucleus, nucleolus** -- ECO:0000269 x2 (experimental)
- **Nucleus, nucleoplasm** -- ECO:0000269 (experimental)

### GO Cellular Component (GO-CC)
- **GO:0005730 (nucleolus)** -- IDA:HPA
- **GO:0005654 (nucleoplasm)** -- TAS:Reactome
- **GO:0005634 (nucleus)** -- ISS:UniProtKB

**Summary:** RIOX1 is a nucleolar and nucleoplasmic protein. Strong experimental evidence from HPA IF (nucleoli rim pattern), UniProt (experimental), and GO-CC. Nuclear score: 28/30 -- excellent nuclear localization.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict (Title/Abstract) | 7 |
| Broad (All Fields) | 24 |

**Novelty score: 10/10.** RIOX1 is a very under-studied gene.

### Key Papers
1. **PMID:29914368** -- Brauer KE et al. (2018). "Phylogenetic and genomic analyses of the ribosomal oxygenases Riox1 (No66) and Riox2 (Mina53) provide new insights into their evolution." *BMC Evol Biol*.
2. **PMID:35210392** -- Xiao Y et al. (2022). "RIOX1-demethylated cGAS regulates ionizing radiation-elicited DNA repair." *Bone Res*.
3. **PMID:36660551** -- Chen Q et al. (2023). "Osteoblast-Specific Overexpression of Nucleolar Protein NO66/RIOX1 in Mouse Embryos Leads to Osteoporosis in Adult Mice." *J Osteoporos*.
4. **PMID:34624518** -- Qin Z et al. (2022). "Genome-wide identification, evolution of histone lysine demethylases (KDM) genes and their expression during gonadal development in Nile tilapia." *Comp Biochem Physiol B*.
5. **PMID:35361830** -- Hafliger IM et al. (2022). "Four novel candidate causal variants for deficient homozygous haplotypes in Holstein cattle." *Sci Rep*.

**Assessment:** Very low publication count. Highly underexplored. Direct connection to histone demethylation (H3K4me3, H3K36me2) is clear.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9H6W3-F1, version 6
- **mean pLDDT: 79.9** (>90: 70.4%, 70-90: 1.6%, 50-70: 0.2%, <50: 27.9%)
- **Assessment:** Good overall confidence. The N-terminal region (~residues 1-180) has lower confidence, but the catalytic C-terminal domain (183-641) is well resolved.

### Experimental PDB Structures
- **10 structures:** 4CCJ (2.15A), 4CCK (2.15A), 4CCM (2.51A), 4CCN (2.23A), 4CCO (2.30A), 4DIQ (2.40A), 4E4H (2.28A), 4Y33 (2.70A), 4Y3O (2.20A), 4Y4R (3.30A)
- All X-ray crystallography, covering the catalytic domain (residues ~176-641).
- **Assessment:** Excellent experimental structural coverage of the histone demethylase catalytic domain.

### PAE
- PAE image URL available: AF-Q9H6W3-F1-predicted_aligned_error_v6.png
- PAE assessment pending image retrieval.

---

## PPI Network

### STRING (15 partners)
| Partner | Score | Experimental | Function |
|---------|-------|-------------|----------|
| RPL8 | 0.986 | 0.960 | Ribosomal protein (hydroxylation target) |
| PHF19 | 0.940 | 0 | Polycomb group protein (chromatin) |
| SP7 | 0.920 | 0.096 | Osteoblast transcription factor |
| RIOK1 | 0.807 | 0 | Ribosomal biogenesis kinase |
| MYC | 0.604 | 0.292 | Oncogenic transcription factor |
| TRRAP | 0.674 | 0.292 | Histone acetyltransferase complex |
| KDM8 | 0.648 | 0 | Histone demethylase |
| KDM2B | 0.626 | 0 | Histone demethylase |

### IntAct (15 interactors)
| Partner | Method | PMID | Relevance |
|---------|--------|------|-----------|
| MKI67 | Co-IP | 26949251 | Proliferation marker |
| HNRNPU | Co-IP | 26496610 | RNA binding, chromatin |
| EIF3A | Co-IP | 26496610 | Translation initiation |
| NOP56 | Co-IP | 26496610 | Nucleolar rRNA processing |
| RPL4, RPLP0, RPL7A | Co-IP | 33961781 | Ribosomal proteins |
| RPS6 | BioID | 29568061 | Ribosomal protein |
| USP42 | Co-IP | 19615732 | Deubiquitinase |

### PPI Network Assessment
- Moderate interaction network linking ribosomal biogenesis with chromatin regulation.
- PHF19 (Polycomb) and MYC/TRRAP connections are chromatin-relevant.
- Multiple histone demethylase family connections (KDM8, KDM2B).

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
RIOX1 was likely rejected due to incomplete scoring or placeholder text in original report.

### Recheck Analysis
1. **Nuclear evidence:** STRONG. HPA main location: Nucleoli rim (Supported). UniProt experimental evidence for nucleolus and nucleoplasm. IF images available.
2. **Functional context:** DIRECT histone demethylase activity (H3K4me3, H3K36me2). This is core epigenetic regulation -- directly relevant to TE silencing.
3. **PubMed:** 7 strict. Very low. HIGH NOVELTY.
4. **Structure:** 10 PDB structures plus good AlphaFold. Excellent structural coverage.
5. **PPI:** PHF19 (Polycomb), MYC, TRRAP -- all chromatin-relevant partners.

### Verdict
**The original rejection was INCORRECT.** RIOX1 is a histone lysine demethylase with direct epigenetic regulatory function, strong nuclear localization, excellent structural data, and very high novelty (PubMed=7). It should be RETAINED.

---

## TE-Regulator Relevance

HIGH. RIOX1 is a histone H3K4me3 and H3K36me2 demethylase. H3K4me3 is a hallmark of active promoters, and H3K36me2 is associated with transcription elongation. Both marks are relevant to TE silencing mechanisms. The protein also demethylates cGAS, connecting it to innate immune sensing of cytosolic DNA -- potentially relevant for TE-derived DNA sensing. The interaction with PHF19 (Polycomb repressive complex component) further supports a chromatin-level regulatory role. MYC interaction connects to broad transcriptional programs. This is a strong candidate for TE-regulatory investigation.

---

## Final Decision: RETAINED

Score: 152/180. RIOX1 is a histone lysine demethylase with direct epigenetic regulatory function, strong nuclear localization, excellent structural data (10 PDB, good AF), very high novelty (PubMed=7), and chromatin-relevant PPI network. The protein demethylates H3K4me3 and H3K36me2 -- histone marks directly relevant to TE silencing. This gene should NOT have been rejected.

---

## Manual Review Note
STRONG CANDIDATE. RIOX1 demethylates H3K4me3 (active promoter mark) and H3K36me2 (transcription elongation mark). Both are critical for TE regulation. The protein localizes to nucleoli/nucleoplasm (HPA + UniProt experimental). PubMed count of 7 indicates extremely low prior investigation -- high novelty for TE biology. The PHF19 (Polycomb) interaction suggests connection to repressive chromatin complexes. Structural data is excellent with 10 PDB entries. This gene should be prioritized for TE-regulatory investigation.
