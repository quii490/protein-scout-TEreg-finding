# AIRIM – Critical False-Rejection Reevaluation Report

**Gene:** AIRIM (AFG2-interacting ribosome maturation factor)  
**UniProt Accession:** Q9NX04  
**Protein Name:** AFG2-interacting ribosome maturation factor  
**Length:** 203 aa | **Mass:** 23.4 kDa  
**Aliases:** C1orf109  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA: no IF images available on page (status: page_found_no_if_image_detected), but HPA IDA evidence for nucleolus + nucleoplasm. UniProt: Nucleus (ECO:0000269, experimental evidence from PubMed:38554706). GO-CC: nucleolus (IDA:HPA), nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB), cytosol (IDA:HPA). Multiple IDA-level annotations strongly support nuclear localization. The protein is chromatin-associated as part of the 55LCC complex. Minor deduction for also being present in cytoplasm/cytosol (dual localization). |
| 2. Protein Size | 10 | 10 | 203 aa / 23.4 kDa – compact, tractable size. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 2 publications. Extremely low literature volume. Gene symbol changed from C1orf109. Maximum novelty. |
| 4. 3D Structure | 30 | 26 | AlphaFold mean pLDDT: 94.2 (87.7% >90) – very high confidence. PDB: 8RHN (EM, 4.50A, chains A/B=1-203) – experimental cryo-EM structure available, though at moderate resolution. High-quality structural data overall. Deduction of 4 for moderate EM resolution and partial chain coverage. |
| 5. Regulatory Domains | 50 | 35 | IPR029159 – single domain of unknown function. However, functional context is highly relevant: AIRIM is part of the 55LCC chromatin-associated ATPase complex that processes replisome substrates on chromatin. This involves chromatin association, ATPase activity, and cysteine protease-dependent cleavage of replisome factors. While no canonical DNA-binding domain is present, the chromatin-associated ATPase activity is a form of chromatin regulation. Points awarded for functional chromatin regulation context. |
| 6. PPI Network | 50 | 30 | STRING failed (404). UniProt: 122 interactors from two-hybrid screens. IntAct: 15 validated interactors including CINP (co-IP, PMID:28514442), ZBED1 (two-hybrid, PMID:32296183), TADA2A (two-hybrid), IHO1, KRT family members, PBX4, ATP23, IKZF3, BORCS6. Large interaction network. CINP is a DNA replication/damage response protein. TADA2A is a histone acetyltransferase complex component (STAGA complex). ZBED1 is a DNA-binding protein. The network includes chromatin-associated and DNA-binding proteins. |
| **TOTAL** | **180** | **139** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** page_found_no_if_image_detected
- **Reliability (IF):** null
- **Main Location:** Not annotated in HPA localization database
- **Additional Locations:** None
- **IF Image Status:** no_image_detected
- **Key Finding:** The HPA page for AIRIM exists but does not contain immunofluorescence images for subcellular localization analysis. However, HPA contributed IDA-level evidence to GO annotations for nucleolus (GO:0005730) and nucleoplasm (GO:0005654), meaning HPA did generate data supporting nuclear localization, even if IF images are not displayed on the current webpage.

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 Despite the absence of displayable IF images, the HPA IDA annotations in GO-CC provide independent experimental support for nucleolar and nucleoplasmic localization.

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000269 (experimental evidence from publication PubMed:38554706)  
  This is a direct experimental assertion, meaning the protein was experimentally demonstrated to localize to the nucleus. High weight.
- **Cytoplasm** – Evidence: ECO:0000269 (experimental evidence, same publication)  
  Dual localization: the protein is present in both nucleus and cytoplasm.

### GO Cellular Component (GO-CC)
- **GO:0005730 (nucleolus)** – Evidence: IDA:HPA (Inferred from Direct Assay by HPA)  
  Direct experimental evidence of nucleolar localization.
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA  
  Direct experimental evidence of nucleoplasmic localization.
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB  
  Direct experimental evidence of nuclear localization from UniProt.
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB  
  Direct experimental evidence of cytoplasmic localization.
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA  
  Direct experimental evidence of cytosolic localization.

**Summary:** AIRIM has STRONG nuclear evidence from multiple independent sources at the IDA (Inferred from Direct Assay) level. The protein localizes to both nucleus (nucleoplasm + nucleolus) and cytoplasm. The chromatin association of the 55LCC complex provides functional context for nuclear localization. Nuclear score: 28/30 (minor deduction for dual localization).

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 2 | `"AIRIM"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 2 | `"AIRIM"[Title/Abstract]` |
| Broad (All Fields) | 8 | `"AIRIM"` |

**Alias Note:** Aliases C1orf109 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:40760247** – Ni C, Wei Y, Vona B (2025). "A programmed decline in ribosome levels governs human early neurodevelopment." *Nat Cell Biol.* 2025 Aug. – Recent high-impact paper identifying AIRIM's role in ribosomal regulation during neurodevelopment.
2. **PMID:38260472** – Ni C, Yu L, Vona B (2024). "An inappropriate decline in ribosome levels drives a diverse set of neurodevelopmental disorders." *bioRxiv.* 2024 Jan 9. – Preprint linking AIRIM-associated ribosome regulation to neurodevelopmental disorders.

### Literature Assessment
- **Total publications:** Extremely low (2 strict, 8 broad). AIRIM is a very poorly studied gene.
- **Thematic focus:** Ribosome biogenesis, neurodevelopment, chromatin-associated ATPase activity.
- **Key functional context:** AIRIM was characterized as part of the 55LCC chromatin-associated heterohexameric ATPase complex (published studies not captured in the keyword search because they use the C1orf109 alias or appear in broader chromatin biology contexts). The 55LCC complex promotes replisome proteostasis on chromatin.
- **No publications directly linking AIRIM to TE regulation.**
- **Novelty score:** 10/10 (≤20 publications = maximum novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q9NX04-F1, version 6
- **Mean pLDDT:** 94.2
- **pLDDT Distribution:**
  - >90 (very high confidence): 87.7%
  - 70-90 (confident): 10.8%
  - 50-70 (low confidence): 1.0%
  - <50 (very low confidence): 0.5%
- **Assessment:** Exceptionally high-confidence predicted structure. Only 0.5% of residues below 50 pLDDT. The protein is almost entirely well-folded.

### Experimental PDB Structures
- **8RHN** – Cryo-EM structure, resolution 4.50 A, chains A/B=1-203 (full-length coverage)  
  This is an experimentally determined structure, providing direct structural validation. The moderate resolution (4.50 A) is typical for cryo-EM of small complexes.

### Structural Assessment
- The IPR029159 domain is of unknown function, but structurally the protein appears well-folded.
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。
- The availability of an experimental cryo-EM structure (even at moderate resolution) is a significant advantage for structural studies.
- **Score:** 26/30 – very high AF confidence plus experimental structure, but moderate EM resolution and no regulatory structural features identified.

---

## PPI Network

### STRING
- **Status:** FAILED (HTTP Error 404: Not Found) – Data unavailable for this harvest cycle.

### UniProt Interactions
Total: 122 interactors (predominantly from two-hybrid screens)

Key interactions (by experiment count):
- **CINP** (15 experiments) – Cyclin-dependent kinase 2-interacting protein, involved in DNA replication checkpoint and damage response.
- **ZBED1** (7 experiments) – Zinc finger BED domain-containing protein 1, a DNA-binding protein.
- Multiple keratin family members (KRT13, KRT16, KRT18, KRT19, KRT24, KRT31, KRT35, KRT40, KRT75, KRT76, KRT80).
- **TADA2A** (6 experiments) – Transcriptional adaptor 2A, component of STAGA histone acetyltransferase complex.
- **IKZF3** (6 experiments) – Ikaros family zinc finger protein 3, a transcription factor.
- **TFIP11** (6 experiments) – Tuftelin-interacting protein 11, involved in spliceosome function.
- **STN1** (5 experiments) – Component of the CST complex, involved in telomere maintenance.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| ENSP00000477159.1 | light scattering | PMID:38554706 | direct interaction |
| Stat2 | two hybrid | PMID:15102471 | physical association |
| CINP | anti tag co-IP | PMID:28514442 | association |
| ZBED1 | two hybrid array | PMID:32296183 | physical association |
| TADA2A | two hybrid array | PMID:32296183 | physical association |
| PBX4 | two hybrid prey pooling | PMID:32296183 | physical association |
| ATP23 | two hybrid prey pooling | PMID:32296183 | physical association |
| IHO1 | two hybrid array | PMID:32296183 | physical association |
| IKZF3 | two hybrid array | PMID:32296183 | physical association |
| BORCS6 | two hybrid array | PMID:32296183 | physical association |
| ADD1 | two hybrid array | PMID:32296183 | physical association |
| KRT16 | two hybrid array | PMID:32296183 | physical association |
| KIFC3 | two hybrid array | PMID:32296183 | physical association |
| KRT75 | two hybrid array | PMID:32296183 | physical association |
| CBY2 | two hybrid array | PMID:32296183 | physical association |

### PPI Network Assessment
- **Network size:** Large (122 UniProt, 15 IntAct). AIRIM appears to be a hub in two-hybrid interaction networks.
- **Notable interactions for TE regulation:**
  - **TADA2A:** Component of the SAGA/STAGA histone acetyltransferase complex. This complex acetylates histones H3 and H2B, regulating chromatin accessibility and transcription. A key chromatin-modifying complex relevant to TE silencing.
  - **ZBED1:** DNA-binding protein that may recognize specific DNA sequences.
  - **IKZF3:** Ikaros transcription factor family member, involved in chromatin remodeling and transcriptional regulation.
  - **CINP:** DNA damage response and replication fork protection protein.
- **Functional network context:** The interactions suggest involvement in chromatin biology (TADA2A, ZBED1), DNA replication/damage response (CINP), and transcription (IKZF3). Combined with AIRIM's own 55LCC chromatin-associated ATPase function, the PPI network reinforces a chromatin/nuclear role.
- **Score:** 30/50 – large network with chromatin-relevant interactors, though most interactions are from high-throughput two-hybrid and lack functional validation specific to TE regulation.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
AIRIM was likely auto-rejected because:
1. HPA page has no displayable IF images (page_found_no_if_image_detected)
2. The gene symbol was changed (formerly C1orf109), potentially causing database lookup issues
3. STRING data was unavailable (HTTP 404)

### Recheck Analysis
1. **HPA Evidence:** Despite no displayable IF images, HPA contributed IDA-level GO annotations for nucleolus and nucleoplasm. This is experimental evidence from HPA, just not in image form.
2. **UniProt Evidence:** STRONG – Nucleus with ECO:0000269 (experimental). This is direct experimental evidence.
3. **GO-CC Evidence:** STRONG – Five IDA-level annotations including nucleolus, nucleoplasm, and nucleus.
4. **Experimental PDB:** 8RHN cryo-EM structure available.
5. **Functional Context:** Chromatin-associated 55LCC ATPase complex. This is fundamentally a nuclear function.
6. **PPI Network:** Interactions with chromatin modifiers (TADA2A, ZBED1) and DNA replication/damage proteins (CINP).

### Verdict on False Rejection
**The original rejection was FALSE – AIRIM should NOT have been rejected.** The nuclear evidence is robust: multiple IDA-level annotations from both UniProt and GO, experimental evidence from PMID:38554706, and functional context as a chromatin-associated protein. The absence of displayable HPA IF images appears to have caused the automated system to miss the strong nuclear evidence elsewhere. This is a clear case of a false rejection driven by incomplete HPA data capture rather than genuine absence of nuclear localization.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

AIRIM has several features that make it a candidate for TE-regulatory investigation, though with caveats:

1. **Chromatin Association:** AIRIM is part of the 55LCC heterohexameric ATPase complex that is chromatin-associated. The complex processes replisome substrates on chromatin using ATPase activity coupled to cysteine protease-dependent cleavage. This represents a form of chromatin regulation.

2. **PPI Network Links to Chromatin Regulation:** AIRIM interacts with TADA2A (STAGA HAT complex), which acetylates histones and regulates chromatin accessibility. Histone acetylation is a key mechanism in TE silencing vs. activation. ZBED1 is a DNA-binding protein with potential for sequence-specific chromatin targeting.

3. **Ribosome Biogenesis Connection:** AIRIM is involved in cytoplasmic maturation of pre-60S ribosomal particles. Ribosome biogenesis and translational control are emerging as relevant to TE regulation (TE-derived RNAs can be translated, and translational repression is a TE silencing mechanism).

4. **Novelty:** Extremely low literature count (2 strict) makes AIRIM a highly novel target unlikely to have been studied in TE contexts.

5. **Caveats:**
   - No canonical DNA-binding domain, zinc finger, or chromatin reader domain.
   - The connection to TE regulation is indirect (via chromatin association + PPI with chromatin modifiers).
   - The specific role of the 55LCC complex in TE silencing has not been investigated.

**Assessment:** AIRIM is a MODERATE-INTEREST candidate for TE regulation. The chromatin association and PPI network connections to histone acetylation machinery are promising. However, the lack of direct DNA-binding or histone modification domains means AIRIM likely acts as a cofactor/adaptor rather than a direct TE regulator. It would be worth investigating in the context of 55LCC complex function at repetitive genomic regions.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Reasoning:** AIRIM was falsely rejected by the automated pipeline due to missing HPA IF images. However, comprehensive review of all evidence sources reveals strong nuclear localization supported by IDA-level experimental evidence from both UniProt and GO. The protein is chromatin-associated as part of the 55LCC ATPase complex. The PPI network includes chromatin-modifying proteins (TADA2A/SAGA, ZBED1). With only 2 PubMed publications, AIRIM represents a highly novel target. The total score of 139/180 places it in the upper-mid range of candidates.

**Score: 139/180** – Strong nuclear evidence, excellent structural data, very high novelty, and chromatin-relevant functional context. The primary limitation is the absence of canonical DNA-binding or histone-modifying domains, and the indirect nature of the TE-regulatory connection.

**Recommended next steps:**
1. Investigate whether the 55LCC complex has a role at repetitive genomic loci.
2. ChIP-seq of AIRIM or 55LCC complex components to determine genomic binding sites.
3. Functional studies: does loss of AIRIM affect TE expression or chromatin marks at repetitive elements?

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*  
*Status: FALSE REJECTION CONFIRMED – gene reopened*

AIRIM represents a clear case of false rejection caused by a database artifact (missing HPA IF images). The nuclear evidence from UniProt (ECO:0000269), GO (multiple IDA), and the functional characterization as a chromatin-associated protein is robust and independent of HPA imaging. The high AlphaFold confidence (mean pLDDT 94.2) and availability of an experimental cryo-EM structure (8RHN) make this gene structurally tractable. The PPI network connections to TADA2A (SAGA HAT complex) provide a mechanistic link to chromatin acetylation, which is directly relevant to TE regulation. This gene should be included in the TE-regulatory candidate pipeline and prioritized for further investigation, particularly regarding the role of the 55LCC complex at repetitive genomic elements.
