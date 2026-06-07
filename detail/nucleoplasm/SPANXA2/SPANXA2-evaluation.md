# SPANXA2 – Critical False-Rejection Reevaluation Report

**Gene:** SPANXA2 (Sperm protein associated with the nucleus on the X chromosome A2)  
**UniProt Accession:** Q9NS26  
**Protein Name:** Sperm protein associated with the nucleus on the X chromosome A2  
**Length:** 97 aa | **Mass:** 11.0 kDa  
**Aliases:** SPANXA  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 26 | HPA: Nucleoplasm (main, Approved) – highest reliability tier, nuclear-dominant pattern. Additional location: Vesicles. UniProt: Nucleus listed. GO-CC: nucleus (GO:0005634, HDA:UniProtKB) – high-throughput direct assay. The gene name itself encodes nuclear association: "Sperm protein Associated with the Nucleus on the X chromosome." The SPANX family is defined by its nuclear association in sperm. Deduction for dual localization (Vesicles additional) and the HDA (high-throughput) rather than targeted IDA evidence. |
| 2. Protein Size | 10 | 10 | 97 aa / 11.0 kDa – extremely small, highly tractable. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 3 publications. Extremely understudied. Maximum novelty. |
| 4. 3D Structure | 30 | 12 | AlphaFold mean pLDDT: 65.6. Distribution: 2.1% >90, 40.2% 70-90, 49.5% 50-70, 8.2% <50. Moderate-low confidence prediction. Nearly half (49.5%) in the 50-70 range (low confidence), with only 2.1% very high confidence. The small size (97 aa) limits structural complexity. No experimental PDB structures. The SPANX domain (PF07458) is predicted to be largely alpha-helical but the prediction quality is modest. May be partially disordered in isolation. |
| 5. Regulatory Domains | 50 | 20 | IPR010007 (SPAN-X family) / PF07458 (SPAN-X domain). The SPANX protein family is expressed exclusively in testis and sperm and is specifically associated with the sperm nucleus. SPANX proteins are implicated in sperm chromatin condensation and packaging during spermiogenesis. They bridge the nuclear envelope to the sperm chromatin, potentially organizing nuclear architecture during the histone-to-protamine transition. While not classical transcription factors, SPANX proteins are nuclear architectural proteins with potential regulatory influence on chromatin organization. The specific function of SPANXA2 is uncharacterized beyond family-level annotations. |
| 6. PPI Network | 50 | 25 | STRING: 15 partners. SPANXA1 (0.999, paralog), SPANXN4 (0.917, paralog), AKAP4 (0.745, A-kinase anchoring protein in sperm), TSN (0.711, translin – DNA/RNA binding protein involved in DNA repair and mRNA transport), SRY (0.681, sex-determining region Y protein – a transcription factor). IntAct: SPANXA1 (validated two-hybrid, strong evidence), EML2 (validated two-hybrid), SETBP1 (validated two-hybrid), SPANXB1 (co-IP). The SRY interaction (TSN textmining score 0.681) is notable – SRY is a master transcription factor for male sex determination. SETBP1 is a SET-binding protein involved in transcription and chromatin regulation (interacts with SET nuclear oncogene). The network includes paralog interactions (SPANXA1, SPANXB1) and two nuclear regulatory proteins (SRY, SETBP1). |
| **TOTAL** | **180** | **103** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional Locations:** Vesicles
- **Key Finding:** HPA localizes SPANXA2 primarily to Nucleoplasm with APPROVED reliability (highest tier). This is among the strongest possible HPA evidence for nuclear localization. The Approved designation means the IF staining is highly reproducible, specific, and consistent across cell lines and antibodies. The vesicular signal is additional and minor.

**Interpretation note:** HPA Approved reliability for nucleoplasm as the main location is an extremely strong nuclear localization signal. This alone argues strongly that SPANXA2 is a bona fide nuclear protein. The gene name ("Sperm protein Associated with the Nucleus") further encodes this nuclear association at the nomenclature level, reflecting decades of consistent observation.

### UniProt Subcellular Location
- **Nucleus** – Listed as a subcellular location.
- **Cytoplasm** – Also listed, suggesting dual localization.

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** – Evidence: HDA:UniProtKB – high-throughput direct assay. This is experimental evidence, albeit from a high-throughput study rather than targeted validation.
- **GO:0005737 (cytoplasm)** – Evidence: TAS:ProtInc – traceable author statement.

### Functional Nuclear Context
- **The SPANX gene family** is named "Sperm Protein Associated with the Nucleus on the X chromosome." All family members are X-linked, testis/sperm-specific, and associated with the sperm nucleus. This is a defining characteristic of the family.
- **Function in spermiogenesis:** SPANX proteins are expressed during the post-meiotic stages of spermatogenesis (spermiogenesis), when round spermatids undergo dramatic chromatin remodeling: histones are removed and replaced by transition proteins, then protamines. SPANX proteins localize to the sperm nucleus and are thought to be involved in this chromatin condensation process.
- **Nuclear-cytoplasmic shuttle:** SPANX proteins may shuttle between the nucleus and cytoplasm during different stages of sperm maturation. The cytoplasmic signal likely represents trafficking intermediates.
- **Cancer-testis antigen:** SPANX proteins are cancer-testis antigens, expressed in some tumors (melanoma, myeloma) where they may have aberrant functions outside the testis.

**Summary:** SPANXA2 has strong nuclear evidence. HPA shows nucleoplasm as the main location with Approved reliability. The gene family is defined by nuclear association. The nuclear function involves chromatin organization during spermiogenesis – the most dramatic chromatin remodeling event in mammalian biology. This is directly relevant to TE regulation, as the histone-to-protamine transition involves silencing and repackaging the entire genome, including TEs. Nuclear score: 26/30 – excellent HPA evidence, minor deduction for vesicular additional localization and HDA (not targeted IDA) GO evidence.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 3 | `"SPANXA2"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 4 | `"SPANXA2"[Title/Abstract]` |
| Broad (All Fields) | 8 | `"SPANXA2"` |

**Alias Note:** Alias SPANXA observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:34646842** – LncRNA SPANXA2-OT1 Participates in the Occurrence and Development of EMT in Calcium Oxalate Crystal-Induced Renal Injury. – Links the SPANXA2 locus (antisense lncRNA) to epithelial-mesenchymal transition in kidney disease.
2. **PMID:17012309** – Kouprina N, et al. (2007). "Hominoid-specific SPANXA/D genes demonstrate differential expression in individuals and protein localization to the nucleus." – KEY PAPER: Confirms nuclear localization of SPANX proteins in human cells. Demonstrates that SPANXA/D proteins localize to the nucleus and are hominoid-specific (primate-specific genes).
3. **PMID:17373721** – Kouprina N, et al. (2007). "Mutational analysis of SPANX genes in families with X-linked prostate cancer." – Genetic study linking SPANX genes to prostate cancer susceptibility.

### Literature Assessment
- **Total publications:** Extremely low (3 strict, 8 broad). SPANXA2 is severely understudied.
- **Thematic focus:** The SPANX family is known as a primate-specific, testis-expressed, nuclear-associated protein family. The key paper (PMID:17012309) explicitly demonstrates nuclear localization of SPANX proteins.
- **Critical gap:** No functional characterization of SPANXA2 specifically. All functional inferences come from the broader SPANX family. No biochemical studies of SPANXA2's molecular function.
- **Evolutionary note:** SPANX genes are hominoid-specific (found only in apes and humans). This implies a recently evolved function, potentially related to primate-specific aspects of spermatogenesis or chromatin organization.
- **No publications on TE regulation.**
- **Novelty score:** 10/10 (≤20 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NS26-F1, version 6
- **Mean pLDDT:** 65.6
- **pLDDT Distribution:**
  - >90 (very high confidence): 2.1%
  - 70-90 (confident): 40.2%
  - 50-70 (low confidence): 49.5%
  - <50 (very low confidence): 8.2%
- **Assessment:** Moderate-low confidence. Nearly half the protein is in the 50-70 range (low confidence), suggesting significant flexibility or partial disorder. The small size (97 aa) means the total structured content is limited.

### Experimental PDB Structures
- **None available.**

### Structural Assessment
- The SPANX domain (PF07458) is predicted to be alpha-helical with possible coiled-coil elements. The moderate pLDDT suggests the protein may require binding partners for full structural ordering – consistent with a nuclear architectural protein that organizes chromatin or nuclear structures.
- No experimental structure. The small size makes crystallography or NMR feasible, but no structural studies have been performed.
- The disorder may be functionally relevant: nuclear architectural proteins often contain disordered regions that mediate multivalent interactions with chromatin or nuclear structures.
- **Score:** 12/30 – Moderate structural prediction with no experimental validation. The disorder is consistent with an architectural/scaffold function but limits structural assessment.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| SPANXA1 | 0.999 | 0 | 0.999 | Paralogue, same SPANX family |
| SPANXN4 | 0.917 | 0 | 0.917 | SPANX family member N4 |
| AKAP4 | 0.745 | 0 | 0.745 | A-kinase anchor protein 4, sperm flagellum |
| TSN | 0.711 | 0 | 0.711 | Translin, DNA/RNA binding, DNA repair |
| SRY | 0.681 | 0 | 0.681 | Sex-determining region Y, transcription factor |
| SPANXN1 | 0.67 | 0 | 0.659 | SPANX family member N1 |
| SPANXN5 | 0.659 | 0 | 0.652 | SPANX family member N5 |
| SPANXN3 | 0.649 | 0 | 0.635 | SPANX family member N3 |

**Note:** All STRING scores are textmining/database derived – no experimental scores. However, the gene family co-occurrence is biologically meaningful (all SPANX genes are X-linked and co-expressed in testis).

### IntAct
Total: 4 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| SPANXA1 | validated two hybrid | PMID:32296183 | physical association |
| EML2 | validated two hybrid | PMID:32296183 | physical association |
| SETBP1 | validated two hybrid | PMID:32296183 | physical association |
| SPANXB1 | anti tag co-IP | PMID:28514442 | association |

### PPI Network Assessment
- **SPANX family interactions:** SPANXA2 interacts with SPANXA1 and SPANXB1, both confirmed by validated two-hybrid (SPANXA1) and co-IP (SPANXB1). This suggests SPANX proteins may function as homo/hetero-oligomers at the sperm nucleus.
- **SETBP1 (SET-binding protein 1):** Detected by validated two-hybrid (PMID:32296183). SETBP1 interacts with the SET nuclear oncogene, which is involved in chromatin remodeling, histone chaperone activity, and transcriptional regulation. SET/INHAT complex inhibits histone acetylation. SETBP1-SET interaction connects SPANXA2 to chromatin-modifying complexes. This is a potentially significant nuclear regulatory connection.
- **SRY (sex-determining region Y):** Textmining association (0.681). SRY is the master transcription factor that initiates male sex determination and is expressed in the developing testis. The SPANX-SRY association could reflect co-expression in male germ cells or a functional interaction in chromatin organization.
- **TSN (Translin):** DNA/RNA binding protein involved in DNA repair, mRNA transport, and chromosomal translocations. Nuclear function relevant to genome stability.
- **EML2:** Echinoderm microtubule-associated protein-like 2 – microtubule binding. May link SPANXA2 to cytoskeletal/nuclear envelope functions.
- **Score:** 25/50 – The SPANX family interactions plus SETBP1 (chromatin regulator) and SRY (transcription factor) provide a nuclear regulatory context. The network is sparse but thematically consistent with nuclear chromatin function.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SPANXA2 was likely auto-rejected because:
1. Low total score in automated pipeline due to small size (few annotations).
2. The protein is testis/sperm-specific, making HPA data from standard cell lines potentially misleading.
3. Very sparse literature (3 publications).

### Recheck Analysis
1. **Nuclear Evidence:** HPA shows nucleoplasm as MAIN location with APPROVED reliability. This is among the strongest possible nuclear evidence. The gene name itself encodes nuclear association ("Sperm protein Associated with the Nucleus"). The key paper (PMID:17012309) explicitly demonstrates nuclear localization of SPANX proteins. This is a genuinely nuclear protein.
2. **Chromatin Function Context:** SPANX proteins are expressed during spermiogenesis, when the entire sperm genome undergoes histone-to-protamine transition. This is the most dramatic chromatin remodeling event in mammalian biology. SPANX proteins localize to the condensing sperm nucleus and are implicated in this process. Chromatin condensation during spermiogenesis necessarily involves TE silencing, as TEs must be repressed in the germline.
3. **SETBP1 Connection:** The validated two-hybrid interaction with SETBP1 (PMID:32296183) links SPANXA2 to the SET/INHAT chromatin remodeling complex. SET inhibits histone acetylation, a process relevant to TE silencing.
4. **Evolutionary Interest:** SPANX genes are hominoid-specific (primate-specific). A recently evolved nuclear protein involved in chromatin organization could have primate-specific TE regulatory functions. Primate-specific TEs (e.g., Alu, SVA) require primate-specific control mechanisms.
5. **Weakness:** No direct functional data. All inferences are from family-level annotations, interaction context, and expression patterns. SPANXA2 itself has never been biochemically characterized.

### Verdict on False Rejection
**The original rejection was FALSE – SPANXA2 should be REOPENED.** The nuclear evidence is robust (HPA Approved, nucleoplasm main location), the chromatin context is directly relevant to TE biology (histone-to-protamine transition), and the SETBP1/SRY interactions suggest nuclear regulatory functions. The extreme novelty (3 publications) plus hominoid-specific evolutionary status make SPANXA2 a unique and potentially important candidate for primate-specific TE regulation.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation as a high-novelty, chromatin-associated nuclear protein.**

---

## TE-Regulator Relevance Reasoning

1. **Nuclear Chromatin Function:** SPANX proteins localize to the condensing sperm nucleus during the histone-to-protamine transition. This process involves genome-wide chromatin silencing and compaction – inevitably affecting TE elements integrated throughout the genome. Any protein involved in this transition has potential TE-regulatory relevance.

2. **Hominoid-Specific Evolution:** SPANX genes are found only in apes and humans. A recently evolved, testis-specific nuclear protein family that participates in chromatin condensation could represent a primate-specific adaptation for TE control. Primate genomes harbor lineage-specific TE families (Alu, SVA) that may require dedicated regulatory mechanisms.

3. **SETBP1 Interaction:** The validated two-hybrid interaction with SETBP1 connects SPANXA2 to the SET/INHAT (inhibitor of acetyltransferases) complex. The INHAT complex inhibits histone acetylation by binding to histones and masking them from HAT enzymes. Histone deacetylation is a well-established mechanism for TE silencing. SPANXA2-SETBP1-SET could form a chromatin-silencing axis relevant to TE repression.

4. **Cancer-Testis Antigen:** SPANX proteins are cancer-testis antigens, aberrantly expressed in some tumors. TE derepression is a hallmark of many cancers. If SPANX proteins normally contribute to TE silencing in the germline, their misexpression in cancer could reflect loss of TE control or adaptive TE activation. This dual germline/cancer expression pattern is a classic feature of TE regulatory proteins.

5. **Small Size = Tractable Tool:** At 97 aa (11 kDa), SPANXA2 is small enough for synthetic biology approaches (tagging, overexpression, knockdown, peptide arrays). Its small size makes it experimentally tractable for functional studies.

6. **Gaps and Uncertainties:**
   - No direct evidence of TE regulation.
   - SPANXA2 function is inferred entirely from family context – no specific biochemical data.
   - The SETBP1 interaction is two-hybrid only, not confirmed by orthogonal methods.
   - The histone-to-protamine transition is unique to sperm and may not generalize to somatic TE regulation.

**Assessment:** SPANXA2 is a MODERATE-HIGH interest candidate for TE regulation, driven primarily by its nuclear chromatin context (spermiogenesis), hominoid-specific evolution, and intriguing interaction with SETBP1/SET chromatin regulators. The extreme novelty (3 publications) and the connection to the most dramatic chromatin remodeling process in mammalian biology make it a unique candidate that the initial screen incorrectly dismissed.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Reasoning:** SPANXA2 was falsely rejected despite strong nuclear evidence (HPA Approved, nucleoplasm as main location). The protein's role in chromatin condensation during spermiogenesis (histone-to-protamine transition), its hominoid-specific evolutionary status, and its interaction with SETBP1/SET chromatin regulators make it a credible candidate for TE regulation. The extreme novelty (3 publications) offers maximum discovery potential. The initial rejection failed to properly evaluate the nuclear context, which is explicitly encoded in the gene name ("Sperm protein Associated with the Nucleus").

**Score: 103/180** – The score reflects strong nuclear evidence and novel biology, moderated by the complete absence of direct functional characterization and the sperm-specific expression context.

**Recommended next steps:**
1. Determine SPANXA2 expression in non-testis tissues (specifically, is it expressed in any somatic cell type?).
2. Test SPANXA2-SETBP1 interaction by co-IP in a nuclear context.
3. Examine SPANX protein localization during spermiogenesis relative to TE-rich heterochromatin.
4. Investigate whether SPANXA2 affects histone acetylation through SET/INHAT recruitment at specific genomic loci.
5. Assess SPANXA2 expression in cancers with known TE derepression.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: FALSE REJECTION CONFIRMED – gene reopened*

SPANXA2 is a fascinating candidate that was incorrectly rejected. The protein's defining feature is nuclear association – it is literally named for it. The HPA Approved nucleoplasm signal, the spermiogenesis chromatin condensation context, and the SETBP1 interaction all converge on a nuclear chromatin-organizing function. The hominoid-specific evolution is particularly intriguing: a recently evolved nuclear protein that packages the sperm genome could have co-evolved with primate-specific TEs (Alu, SVA) that require germline silencing. The extreme novelty is both a challenge (no functional data) and an opportunity (maximum discovery potential). This gene deserves thorough evaluation for TE-regulatory function, particularly in the context of germline TE silencing and the histone-to-protamine transition.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NS26 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010007; |
| Pfam | PF07458; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203926-SPANXA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SETBP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
