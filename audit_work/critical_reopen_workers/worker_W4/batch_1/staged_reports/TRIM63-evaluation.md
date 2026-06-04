# TRIM63 – Critical False-Rejection Reevaluation Report

**Gene:** TRIM63 (Tripartite motif containing 63) / MURF1  
**UniProt Accession:** Q969Q1  
**Protein Name:** E3 ubiquitin-protein ligase TRIM63 (Muscle RING-finger protein 1)  
**Length:** 353 aa | **Mass:** 40.2 kDa  
**Aliases:** IRF, MURF1, RNF28, SMRZ  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 8 | HPA: protein detected but reliability=None, all location lists empty – no localization information. UniProt: Nucleus listed among locations (Cytoplasm, Nucleus, sarcomere M line, sarcomere Z line). GO-CC: nucleus (GO:0005634, IEA:UniProtKB-SubCell) – electronic annotation only, NO experimental evidence. Primary localization is cytoplasmic/sarcomeric (M band, Z disc – structural components of the muscle sarcomere). The nuclear annotation is the weakest type (IEA) with no supporting experimental evidence. TRIM63 is a muscle-specific protein whose primary localization is at the sarcomere, a cytoplasmic structure. |
| 2. Protein Size | 10 | 8 | 353 aa / 40.2 kDa – moderate size, tractable. Deduction for being above small-protein range. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 180 publications. Well-studied muscle atrophy protein. Lower novelty. |
| 4. 3D Structure | 30 | 22 | AlphaFold mean pLDDT: 82.8. Distribution: 57.2% >90, 24.1% 70-90, 5.4% 50-70, 13.3% <50. Good prediction with 81.3% high confidence (>70). Experimental PDB: 3 structures of fragments. 2D8U (NMR, B-box domain, residues 119-169), 3DDT (X-ray, 1.90A, B-box domain, residues 117-161), 4M3L (X-ray, 2.10A, coiled-coil domain, residues 214-271). Fragment structures covering the B-box zinc finger and coiled-coil regions. No full-length structure. The key domains (RING finger, B-box, coiled-coil) are at least partially characterized. |
| 5. Regulatory Domains | 50 | 22 | IPR017903 (COILED-COIL), IPR027370 (RING finger, Zn^{2+}-binding), IPR000315 (B-box zinc finger), IPR001841 (Zinc finger, RING-type), IPR013083 (Zinc finger, RING/FYVE/PHD-type), IPR017907 (Zinc finger, RING-type, conserved site). TRIM63 is a member of the TRIM (tripartite motif) protein family, characterized by a conserved RBCC domain architecture: RING finger, B-box(es), and Coiled-Coil. The RING finger confers E3 ubiquitin ligase activity – TRIM63 catalyzes the ubiquitination and subsequent proteasomal degradation of target proteins. TRIM63's established function is in muscle protein turnover: it ubiquitinates sarcomeric proteins (titin, myosin heavy chain, myosin light chain) during muscle atrophy. It is a key mediator of skeletal muscle wasting (cachexia, sarcopenia). TRIM63 is transcriptionally induced by FOXO transcription factors during fasting and denervation. The TRIM family is notable because several members are master regulators of TE silencing: TRIM28/KAP1 is the corepressor for KRAB-ZFPs that silence ERVs and other TEs; TRIM24/TIF1A is a chromatin regulator; TRIM33/TIF1G functions in TGF-beta signaling and chromatin. TRIM proteins often have dual cytoplasmic and nuclear functions, with the nuclear functions involving chromatin regulation. However, TRIM63's characterized functions are exclusively cytoplasmic/sarcomeric (muscle protein degradation). There is no evidence that TRIM63 functions in the nucleus despite the TRIM family precedent. TRIM63 lacks a PHD/Bromodomain (found in TRIM24/28/33 that mediate chromatin binding) – it has only the RBCC core without chromatin reader domains. This domain architecture (RBCC only) is more typical of cytoplasmic TRIMs involved in protein degradation and innate immunity rather than nuclear chromatin regulators. |
| 6. PPI Network | 50 | 10 | STRING: FAILED – 0 partners returned. The STRING harvest failed for TRIM63 (packet shows ok=false). This is a technical harvesting gap. IntAct: 15 interactors including MYBPC2 (two-hybrid), SGCB (two-hybrid), SNAPIN (two-hybrid), LAMA2 (two-hybrid), and multiple other two-hybrid hits. All IntAct interactions are from two-hybrid fragment pooling assays (MI:0399) – low-confidence screening data. No high-confidence physical interaction data available. The STRING failure and low-quality IntAct data severely limit PPI network assessment. |
| **TOTAL** | **180** | **74** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available (protein detected)
- **Reliability (IF):** None
- **Main Location:** [] (empty)
- **Additional Locations:** [] (empty)
- **All Locations:** [] (empty)
- **Key Finding:** HPA detected TRIM63 protein expression but could NOT determine subcellular localization. The protein is detected (protein page exists) but IF images are either unavailable or uninterpretable. As a muscle-specific protein, TRIM63 is likely not expressed in the standard HPA cell lines (A-431, U-2 OS, U-251 MG), explaining the absent localization data.

**Interpretation note:** TRIM63 is predominantly expressed in skeletal and cardiac muscle. HPA's standard IF cell lines are non-muscle cells and would not express TRIM63. The absent HPA localization data is a tissue-specificity artifact but still represents a data gap for the screening pipeline.

### UniProt Subcellular Location
- **Cytoplasm** – Primary localization. TRIM63 functions in the cytoplasm.
- **Nucleus** – Listed among locations. Nuclear localization is noted.
- **Cytoplasm, myofibril, sarcomere, M line** – Sarcomeric M line (center of the sarcomere, where thick filaments are cross-linked).
- **Cytoplasm, myofibril, sarcomere, Z line** – Sarcomeric Z disc (boundary of the sarcomere, where thin filaments are anchored).

The sarcomeric localizations (M line, Z disc) are highly specific and reflect TRIM63's primary function in muscle. The nuclear annotation lacks specificity or functional context.

### GO Cellular Component (GO-CC)
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB – direct assay.
- **GO:0031430 (M band)** – Evidence: IMP:UniProtKB – inferred from mutant phenotype. The sarcomere M band is the primary functional location.
- **GO:0030018 (Z disc)** – Evidence: IMP:UniProtKB – inferred from mutant phenotype.
- **GO:0005874 (microtubule)** – Evidence: NAS:UniProtKB – non-traceable author statement. TRIM63 associates with microtubules for transport.
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell – electronic annotation. WEAKEST evidence type. No experimental nuclear GO annotation.

### Functional Nuclear Context
- **TRIM Family Precedent:** Many TRIM proteins have nuclear functions, most notably TRIM28/KAP1 (the master TE silencer through KRAB-ZFP recruitment and H3K9me3 deposition), TRIM24/TIF1A (chromatin reader/transcriptional regulator), and TRIM33/TIF1G (TGF-beta/SMAD signaling in the nucleus). These nuclear TRIMs contain chromatin reader domains (PHD, Bromodomain) in addition to the RBCC core. TRIM63 lacks these chromatin reader domains – it is an RBCC-only TRIM, which is more typical of cytoplasmic TRIMs.
- **Domain Architecture:** TRIM proteins are defined by the RBCC motif: RING (E3 ligase), B-box(es) (zinc-binding, protein interaction), Coiled-Coil (oligomerization). The C-terminal domain determines subcellular localization and function. TRIM63 has no annotated C-terminal domain (no PRY/SPRY, no PHD, no Bromodomain, no Filamin, no NHL), suggesting it is a minimal RBCC-only TRIM. These minimal TRIMs are typically cytoplasmic and function in protein quality control or innate immunity, not nuclear chromatin regulation.
- **Muscle Atrophy Function:** TRIM63/MURF1 ubiquitinates sarcomeric proteins (myosin heavy chain, myosin light chain, titin, troponin) and targets them for proteasomal degradation during muscle atrophy. This is a cytoplasmic function at the sarcomere. There is no evidence that TRIM63 ubiquitinates nuclear proteins.
- **Transcriptional Regulation:** TRIM63 expression is regulated by FOXO transcription factors (induced during fasting, denervation, and atrophy). This places TRIM63 downstream of nuclear FOXO signaling, not upstream as a nuclear regulator.

**Summary:** TRIM63 has very weak nuclear evidence. HPA has no localization data. The sole nuclear GO annotation is IEA (electronic). UniProt lists both cytoplasm and nucleus, but the characterized functions and sarcomeric localization (M line, Z disc) are exclusively cytoplasmic. As a minimal RBCC-only TRIM without chromatin reader domains, TRIM63 is unlikely to have nuclear functions. Nuclear score: 8/30 – minimal, reflecting the IEA-only annotation and absence of experimental support.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 180 | `"TRIM63"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 238 | `"TRIM63"[Title/Abstract]` |
| Broad (All Fields) | 864 | `"TRIM63"` |

**Alias Note:** Aliases MURF1, IRF, RNF28, SMRZ observed. The broad count (864) is inflated due to the many aliases and overlap with MURF1 literature.

### Key Papers (with PMIDs)
1. **PMID:20301725** – Nonsyndromic Hypertrophic Cardiomyopathy Overview. TRIM63 mutations in cardiomyopathy.
2. **PMID:40745399** – Exogenous Nucleotides Supplementation Attenuates Age-Related Sarcopenia. TRIM63/MURF1 in age-related muscle loss.
3. **PMID:34821076** – Sepsis induces interleukin 6, gp130/JAK2/STAT3, and muscle wasting. TRIM63 in inflammation-induced muscle atrophy.
4. **PMID:14644425** – MURF1/TRIM63 is a key E3 ubiquitin ligase in skeletal muscle atrophy. Foundational characterization.
5. **PMID:11753675** – Identification of MURF1 as a muscle-specific RING finger protein induced during atrophy.

### Literature Assessment
- **Total publications:** Well-studied (180 strict, 864 broad). Extensive muscle biology literature.
- **Thematic focus:** Skeletal muscle atrophy, cardiac hypertrophy, ubiquitin-proteasome system, sarcopenia, cachexia. TRIM63 is a central muscle atrophy gene.
- **Key functional theme:** TRIM63/MURF1 is the master E3 ubiquitin ligase for muscle protein degradation. It is induced during fasting, denervation, immobilization, and systemic inflammation. It ubiquitinates sarcomeric proteins, targeting them for proteasomal degradation, leading to muscle fiber atrophy.
- **Clinical relevance:** TRIM63 mutations cause hypertrophic cardiomyopathy. TRIM63 expression correlates with muscle wasting in cancer cachexia, AIDS, aging, and critical illness.
- **No publications on nuclear function or TE regulation.**
- **Novelty score:** 4/10 (>100 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q969Q1-F1, version 6
- **Mean pLDDT:** 82.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 57.2%
  - 70-90 (confident): 24.1%
  - 50-70 (low confidence): 5.4%
  - <50 (very low confidence): 13.3%
- **Assessment:** Good prediction quality. Over 81% high confidence (>70 pLDDT). The structured regions correspond to the RBCC domains (RING, B-box, coiled-coil), while the disordered fraction (13.3%) likely represents the N-terminal region before the RING domain.

### Experimental PDB Structures
- **2D8U** – NMR. B-box zinc finger domain (residues 119-169). Solution structure of the B-box.
- **3DDT** – X-ray, 1.90A. B-box domain (residues 117-161, chains A/B/C). Crystal structure showing the B-box fold.
- **4M3L** – X-ray, 2.10A. Coiled-coil domain (residues 214-271, chains A/B/C/D). Shows the antiparallel coiled-coil dimerization interface.

### Structural Assessment
- Three fragment structures cover the B-box and coiled-coil domains. The RING finger domain (N-terminal E3 ligase catalytic domain) has not been experimentally determined, though the AlphaFold prediction is high-confidence (pLDDT suggests a well-folded domain).
- The structures confirm TRIM63's membership in the TRIM family through the characteristic B-box and coiled-coil folds.
- The coiled-coil structure (4M3L) reveals the dimeric assembly, which is important for TRIM protein function (RING dimerization is required for E3 ligase activity).
- **Score:** 22/30 – Good fragment coverage of key domains with high-resolution structures.

---

## PPI Network

### STRING (Functional Partners)
- **STRING harvest FAILED** – 0 partners returned with ok=false in the harvest packet. This is a technical failure, not a biological finding. TRIM63 is well-studied in the literature, and STRING normally contains interaction data for TRIM proteins. The failure may be due to a namespace issue (multiple aliases: TRIM63, MURF1, RNF28) or a transient STRING API error during harvesting.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| MYBPC2 | two hybrid fragment pooling | PMID:NA | physical association |
| SGCB | two hybrid fragment pooling | PMID:NA | physical association |
| SNAPIN | two hybrid fragment pooling | PMID:NA | physical association |
| LAMA2 | two hybrid fragment pooling | PMID:NA | physical association |
| ENSP00000363390.3 | two hybrid fragment pooling | PMID:NA | physical association |

### PPI Network Assessment
- **STRING failure creates a critical data gap.** The inability to retrieve STRING data means we cannot assess the functional partner network. Known TRIM63 interactors from the literature (sarcomeric proteins: titin, myosin heavy chain, myosin light chain, troponin) are not captured in the harvest packet.
- **IntAct data is uniformly low-quality:** All 15 interactors are from two-hybrid fragment pooling (MI:0399), a screening method with high false-positive rates. The interactors show no functional coherence: MYBPC2 is a sarcomeric protein (consistent with TRIM63's function), but SNAPIN (vesicle trafficking), LAMA2 (extracellular matrix protein), and SGCB (sarcoglycan) are diverse and suggest promiscuous two-hybrid interactions rather than specific functional partners.
- **Known functional interactions are missing** from the harvest data entirely.
- **Score:** 10/50 – STRING failure and low-quality IntAct data make this dimension essentially unscorable.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
TRIM63 was likely auto-rejected because:
1. Nuclear GO annotation is IEA only (electronic).
2. HPA has no localization data.
3. STRING harvest failed (0 partners), making the PPI network appear empty.
4. The protein is a well-characterized cytoplasmic/sarcomeric E3 ligase (muscle atrophy).

### Recheck Analysis
1. **Nuclear Evidence:** Extremely weak. IEA-only nucleus annotation, no HPA localization data, no experimental nuclear GO term. TRIM63's primary localization is sarcomeric (M line, Z disc) – specific muscle structures in the cytoplasm.
2. **TRIM Family Context:** The TRIM family includes several master TE regulators (TRIM28/KAP1, TRIM24, TRIM33). However, TRIM63 is a minimal RBCC-only TRIM that lacks the chromatin reader domains (PHD, Bromodomain) characteristic of nuclear TRIMs. Domain architecture strongly predicts cytoplasmic function.
3. **Functional Context:** TRIM63's established function is sarcomeric protein degradation during muscle atrophy. This is a cytoplasmic function with no nuclear component. The protein ubiquitinates structural muscle proteins (myosin, titin) at the sarcomere.
4. **STRING Failure:** The STRING harvest failure is a technical artifact that makes the PPI network appear worse than it is, but even with complete STRING data, the network would consist of sarcomeric protein substrates, not nuclear regulatory partners.
5. **Domain Inference:** TRIM63 lacks the C-terminal domains associated with nuclear function in other TRIMs. This is consistent with its cytoplasmic/sarcomeric role and argues against a nuclear TRIM function.

### Verdict on False Rejection
**The original rejection appears CORRECT.** TRIM63 is a cytoplasmic/sarcomeric E3 ubiquitin ligase with no credible nuclear evidence. The TRIM family name is misleading in this context – not all TRIMs are nuclear. TRIM63's domain architecture (RBCC-only, no chromatin reader) and established function (sarcomeric protein degradation) point to an exclusively cytoplasmic role. The IEA-only nucleus annotation is insufficient to justify nuclear localization claims.

**This gene should remain rejected.** The protein is correctly classified as non-nuclear for screening purposes.

---

## TE-Regulator Relevance Reasoning

1. **Very Weak Nuclear Evidence:** The sole nuclear annotation is IEA (electronic, automated). No experimental data support nuclear localization. HPA has no localization data. TRIM63 is a cytoplasmic/sarcomeric protein.

2. **Domain Architecture Predicts Cytoplasmic Function:** TRIM63 is an RBCC-only TRIM. It lacks the PHD finger, Bromodomain, or other chromatin reader domains that mediate nuclear chromatin association in TRIM28, TRIM24, and TRIM33. This is a fundamental structural distinction – TRIM63 simply does not have the molecular hardware to interact with chromatin.

3. **Muscle-Specific Sarcomeric Function:** TRIM63's established function is ubiquitination of sarcomeric proteins (myosin, titin, troponin) at the M line and Z disc of muscle sarcomeres. This is a highly specialized cytoplasmic function that has no connection to nuclear biology or TE regulation.

4. **No Nuclear Substrates:** TRIM63's known substrates are sarcomeric structural proteins. There is no evidence that TRIM63 ubiquitinates nuclear proteins, histones, chromatin modifiers, or transcription factors.

5. **Transcriptional Regulation Is Downstream:** FOXO transcription factors induce TRIM63 expression during muscle atrophy. TRIM63 is the target, not the regulator, of nuclear transcription. It is an effector of the atrophy program that acts in the cytoplasm.

**Assessment:** TRIM63 is a VERY LOW interest candidate for TE regulation. The TRIM family name suggests relevance, but domain architecture and functional characterization reveal a strictly cytoplasmic/sarcomeric E3 ligase. No credible connection to TE biology.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – cytoplasmic sarcomeric E3 ligase, no nuclear evidence**

**Reasoning:** TRIM63 is a muscle-specific E3 ubiquitin ligase that functions at the sarcomere (M line, Z disc) to degrade structural muscle proteins during atrophy. Nuclear evidence is absent (IEA only). The TRIM family association is misleading – TRIM63 lacks the chromatin reader domains characteristic of nuclear TRIMs (TRIM28/KAP1, TRIM24). The STRING harvest failure is a technical artifact but does not change the biological assessment. TRIM63 has no credible connection to TE biology.

**Score: 74/180** – The score reflects very weak nuclear evidence and functional context that is entirely cytoplasmic.

**Flag for deletion** – TRIM63 should not be reopened.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – sarcomeric E3 ligase, correctly rejected*

TRIM63 illustrates the danger of inferring function from family membership. The TRIM (tripartite motif) family includes some of the most important TE regulators (TRIM28/KAP1 is THE master TE silencer), but the family is large and functionally diverse. TRIM63 is a minimal RBCC-only TRIM that functions exclusively at the muscle sarcomere. It lacks the PHD/Bromodomain chromatin reader modules that characterize nuclear TRIMs. The STRING harvest failure is unfortunate (creating the appearance of no interactions), but even complete STRING data would show only sarcomeric substrates, not nuclear partners. TRIM63 is an excellent muscle atrophy gene but has no place in a TE-regulatory screen. Correctly rejected.
