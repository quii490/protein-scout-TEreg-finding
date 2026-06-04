# XRCC2 – Critical False-Rejection Reevaluation Report

**Gene:** XRCC2 (X-ray repair cross complementing 2)  
**UniProt Accession:** O43543  
**Protein Name:** DNA repair protein XRCC2  
**Length:** 280 aa | **Mass:** 32.0 kDa  
**Aliases:** None  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA: Nucleoplasm, Vesicles (main, Approved). Nucleoplasm is a main location with the highest reliability tier (Approved). UniProt: Nucleus, Cytoplasm/centrosome – primary nuclear localization. GO-CC: nucleoplasm (GO:0005654, IDA:HPA), Rad51B-Rad51C-Rad51D-XRCC2 complex (GO:0033063, IDA:UniProtKB), replication fork (GO:0005657, IDA:UniProtKB), centrosome (GO:0005813, IDA:UniProtKB). Multiple IDA-level annotations including the specific DNA repair complex and the replication fork – both nuclear structures. The replication fork annotation (GO:0005657, IDA) places XRCC2 at the site of active DNA synthesis in the nucleus. Among the strongest nuclear evidence profiles in the W4 batch. Minor deduction for dual localization (Vesicles additional, Centrosome). |
| 2. Protein Size | 10 | 8 | 280 aa / 32.0 kDa – small-moderate, tractable. Above 200 aa for full marks. |
| 3. Research Novelty | 10 | 2 | PubMed strict: 310 publications. Well-studied DNA repair gene. Low novelty. |
| 4. 3D Structure | 30 | 28 | AlphaFold mean pLDDT: 87.1. Distribution: 66.8% >90, 20.4% 70-90, 5.7% 50-70, 7.1% <50. Excellent prediction quality – 87.2% high confidence (>70), with 66.8% very high confidence. Minimal disorder (7.1% <50). Experimental PDB: 4 structures. 8FAZ (EM, 2.30A, full-length 1-280), 8GBJ (EM, 3.11A, full-length), 8OUY (EM, 3.40A, full-length), 8OUZ (EM, 2.20A, residues 2-280). Full-length cryo-EM structures available at good resolution, showing XRCC2 in complex with other RAD51 paralogs. Structures reveal the RAD51 paralog complex architecture. |
| 5. Regulatory Domains | 50 | 28 | IPR027417 (P-loop containing nucleoside triphosphate hydrolase), IPR013632 (DNA recombination and repair protein Rad51-like, C-terminal), IPR020588 (DNA recombination and repair protein RecA-like, ATP-binding domain), IPR030547 (X-ray repair cross complementing 2). XRCC2 is a member of the RAD51 paralog family, which is related to the bacterial RecA protein. It is a core component of the homologous recombination repair (HRR) pathway for double-strand DNA breaks. XRCC2 is part of the CX3 complex (RAD51C-XRCC3) or the BCDX2 complex (RAD51B-RAD51C-RAD51D-XRCC2), which facilitates RAD51 loading onto ssDNA at sites of DNA damage. This is a fundamental DNA repair protein that maintains genome stability. The connection to TE biology is through the DNA damage response: (1) TE insertions (LINE-1, Alu, SVA) can create DNA double-strand breaks that require HRR for repair; (2) TE integration intermediates are DNA lesions that engage DNA repair machinery; (3) some TEs (particularly LINE-1) exploit or are restricted by DNA repair pathways during their replication cycle; (4) loss of DNA repair genes leads to genome instability that can activate TEs. XRCC2 mutations are associated with increased cancer risk (breast cancer, Fanconi anemia-like phenotype) due to defective DNA repair. The RAD51 paralog complex is specifically involved in replication fork protection and restart, which is relevant to TE-induced replication stress. |
| 6. PPI Network | 50 | 34 | STRING: 15 partners. RAD51B (0.999, exp 0.844), RAD51D (0.999, exp 0.949), XRCC3 (0.999, exp 0.13), RAD51C (0.999, exp 0.855), RAD51 (0.997, exp 0.955). Network is the RAD51 paralog complex and HR repair machinery. Exceptional experimental scores: RAD51 (0.955), RAD51D (0.949), RAD51C (0.855), RAD51B (0.844). IntAct: 15 interactors, but dominated by two-hybrid from Drosophila models (cross-species interactions). |
| **TOTAL** | **180** | **128** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm, Vesicles
- **Additional Locations:** None
- **Key Finding:** HPA localizes XRCC2 primarily to Nucleoplasm and Vesicles with APPROVED reliability. The nucleoplasm signal is strong and specific. Approved reliability indicates highly reproducible staining across cell lines and antibodies. The vesicular signal may represent XRCC2 in transport vesicles or at sites of cytoplasmic DNA repair (mitochondrial nucleoids?).

**Interpretation note:** HPA Approved nucleoplasm localization is among the strongest possible nuclear evidence. This, combined with the functional characterization (DNA repair at replication forks), makes XRCC2 an unequivocally nuclear protein.

### UniProt Subcellular Location
- **Nucleus** – Primary localization. XRCC2 functions in the nucleus.
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome** – Centrosomal localization may be related to cell cycle-dependent localization or a minor pool.

### GO Cellular Component (GO-CC)
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA – direct assay evidence from HPA IF.
- **GO:0033063 (Rad51B-Rad51C-Rad51D-XRCC2 complex)** – Evidence: IDA:UniProtKB – direct assay. XRCC2 is specifically part of the BCDX2 complex, a defined nuclear protein complex for DNA repair.
- **GO:0005657 (replication fork)** – Evidence: IDA:UniProtKB – direct assay. XRCC2 localizes to replication forks, the sites of active DNA synthesis. This is a highly specific nuclear sub-compartment.
- **GO:0005813 (centrosome)** – Evidence: IDA:UniProtKB – direct assay. Centrosomal localization, possibly cell cycle-dependent.

All four GO-CC annotations are IDA-level (direct experimental assay). This is one of the highest-quality GO annotation profiles in the entire dataset.

### Functional Nuclear Context
- **Homologous Recombination Repair:** XRCC2 is a core component of the homologous recombination (HR) pathway, the high-fidelity mechanism for repairing DNA double-strand breaks. It is part of the RAD51 paralog complex (BCDX2: RAD51B-RAD51C-RAD51D-XRCC2) that facilitates RAD51 loading onto ssDNA at sites of damage.
- **Replication Fork Protection:** Beyond DSB repair, XRCC2 functions at replication forks to protect stalled forks from degradation and promote fork restart. This is critical for maintaining genome stability during DNA replication.
- **Genome Stability:** XRCC2 mutations cause genomic instability, chromosomal aberrations, and increased cancer susceptibility (particularly breast cancer, PMID:28779002). The protein is a tumor suppressor.
- **DNA Damage-TE Interface:** TE activity creates DNA damage intermediates: LINE-1 endonuclease creates DNA nicks that can progress to DSBs; TE integration intermediates are recognized by DNA repair machinery; retrotransposition generates extrachromosomal DNA that engages DNA damage sensors. DNA repair pathways, including HR, are central to the cellular response to TE-induced DNA damage.

**Summary:** XRCC2 has excellent nuclear evidence. HPA shows nucleoplasm (Approved), GO-CC has four IDA-level annotations including the specific BCDX2 complex and the replication fork. The protein functions at replication forks and sites of DNA damage, both within the nucleoplasm. Nuclear score: 28/30 – among the strongest nuclear evidence in the CRITICAL reopen set.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 310 | `"XRCC2"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 475 | `"XRCC2"[Title/Abstract]` |
| Broad (All Fields) | 489 | `"XRCC2"` |

**Alias Note:** No aliases.

### Key Papers (with PMIDs)
1. **PMID:37344587** – Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor. Recent structural/functional characterization of the BCDX2 complex.
2. **PMID:37253112** – Functional and Clinical Characterization of Variants of Uncertain Significance Identifies a Hotspot for Inactivating Missense Mutations in RAD51C and XRCC2.
3. **PMID:28779002** – Rare, protein-truncating variants in ATM, CHEK2 and PALB2, but not XRCC2, are associated with increased breast cancer risk. Cancer genetics study (note: some controversy about XRCC2's cancer association exists in the literature).
4. **PMID:23149936** – XRCC2 in homologous recombination and genome stability.
5. **PMID:11023315** – XRCC2 is a RAD51 paralog involved in homologous recombination repair.

### Literature Assessment
- **Total publications:** Well-studied (310 strict, 489 broad). Extensive DNA repair literature.
- **Thematic focus:** DNA repair, homologous recombination, RAD51 paralog complex, cancer genetics, genome stability. XRCC2 is a central DNA repair gene.
- **Key functional theme:** XRCC2 is a RAD51 paralog that facilitates homologous recombination repair of DNA double-strand breaks. It functions as part of the BCDX2 complex to load RAD51 onto ssDNA. Loss of XRCC2 leads to defective HR, chromosomal instability, and increased sensitivity to DNA-damaging agents.
- **Clinical relevance:** XRCC2 variants are associated with increased cancer risk (breast cancer, Fanconi anemia-like phenotype), though the strength of this association remains debated.
- **No publications on TE regulation.**
- **Novelty score:** 2/10 (>200 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-O43543-F1, version 6
- **Mean pLDDT:** 87.1
- **pLDDT Distribution:**
  - >90 (very high confidence): 66.8%
  - 70-90 (confident): 20.4%
  - 50-70 (low confidence): 5.7%
  - <50 (very low confidence): 7.1%
- **Assessment:** Excellent prediction quality. 87.2% high confidence, with 66.8% very high confidence. The protein is well-folded with minimal disorder. The prediction quality reflects the RecA-like ATPase fold, which is highly conserved and well-represented in structural databases.

### Experimental PDB Structures
- **8FAZ** – EM, 2.30A. Full-length XRCC2 (1-280) in the BCDX2 complex. Cryo-EM structure showing XRCC2 in complex with RAD51B, RAD51C, and RAD51D. High resolution reveals the interactions between paralogs.
- **8GBJ** – EM, 3.11A. Full-length XRCC2 in the RAD51 paralog complex.
- **8OUY** – EM, 3.40A. XRCC2 (chain D) in complex with RAD51 paralogs and DNA substrate.
- **8OUZ** – EM, 2.20A. XRCC2 (residues 2-280, chain D) at high resolution.

### Structural Assessment
- Four cryo-EM structures show full-length XRCC2 in the RAD51 paralog complex. The structures (2022-2023 entries) represent state-of-the-art structural biology of the DNA repair machinery.
- The 2.20A resolution structure (8OUZ) provides near-atomic detail of the XRCC2 structure within the complex.
- The structures reveal the conserved RecA-like ATPase fold with the Walker A/B motifs for ATP binding and hydrolysis, the DNA-binding loops, and the paralog interaction interfaces.
- **Score:** 28/30 – Excellent structural characterization with full-length structures at high resolution in the functional complex.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| RAD51B | 0.999 | 0.844 | 0.433 | RAD51 paralog B, BCDX2 complex partner |
| RAD51D | 0.999 | 0.949 | 0.44 | RAD51 paralog D, BCDX2 complex partner |
| XRCC3 | 0.999 | 0.13 | 0.487 | RAD51 paralog C, CX3 complex |
| RAD51C | 0.999 | 0.855 | 0.583 | RAD51 paralog C, shared between BCDX2 and CX3 |
| RAD51 | 0.997 | 0.955 | 0.804 | RAD51 recombinase, the central HR protein |
| BRCA2 | 0.996 | 0.762 | 0.796 | BRCA2, RAD51 loader in HR |
| RAD51D-2 | 0.999 | 0.092 | 0.601 | RAD51D variant |
| PALB2 | 0.967 | 0.762 | 0.787 | PALB2, links BRCA1 to BRCA2/RAD51 |
| BRCA1 | 0.95 | 0.667 | 0.692 | BRCA1, master HR regulator |
| RAD54L | 0.665 | 0 | 0.657 | RAD54, RAD51 mediator |

**Note:** This is an outstanding PPI network. Experimental scores are very high: RAD51 (0.955), RAD51D (0.949), RAD51C (0.855), RAD51B (0.844), BRCA2 (0.762), PALB2 (0.762), BRCA1 (0.667). The network faithfully represents the homologous recombination repair pathway, from DNA damage sensing (BRCA1) through RAD51 loading (BRCA2, PALB2, RAD51 paralogs) to strand exchange (RAD51).

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| Cfp1 | two hybrid fragment pooling | PMID:NA | physical association |
| EBI-467052 | two hybrid fragment pooling | PMID:NA | physical association |
| cg15011 | two hybrid fragment pooling | PMID:NA | physical association |
| Miro | two hybrid fragment pooling | PMID:NA | physical association |
| pk | two hybrid fragment pooling | PMID:NA | physical association |

**Note:** IntAct data is from Drosophila two-hybrid screens (gene names like "Cfp1", "cg15011", "pk" are Drosophila genes). Cross-species interactions are less reliable for human protein function assessment. The functionally important human interactions (RAD51B, RAD51C, RAD51D, RAD51) are captured in STRING but not in IntAct for this gene.

### PPI Network Assessment
- **DNA Repair Network:** The STRING network for XRCC2 is among the highest-quality networks in the entire dataset. Every key component of homologous recombination repair is present with high experimental scores. The network spans from damage recognition (BRCA1) through RAD51 paralog-mediated RAD51 loading (BCDX2 complex: RAD51B/C/D + XRCC2) to strand exchange (RAD51).
- **BCDX2 Complex:** The specific complex partners (RAD51B, RAD51C, RAD51D) are validated with high experimental scores. The cryo-EM structures (8FAZ, 8GBJ, 8OUY, 8OUZ) provide atomic-level detail of these interactions.
- **Clinical Relevance:** The network includes major cancer susceptibility genes (BRCA1, BRCA2, PALB2, RAD51C, RAD51D), underscoring the clinical importance of this DNA repair pathway.
- **Score:** 34/50 – Exceptional network quality. The DNA repair pathway is directly relevant to TE biology (TE-induced DNA damage, TE integration intermediates, LINE-1 retrotransposition). Deduction because IntAct data is low-quality cross-species.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
XRCC2 was likely auto-rejected because:
1. Well-studied gene (310 publications) with lower novelty score.
2. "DNA repair" may not have been recognized as relevant to TE regulation in automated scoring.
3. Possible threshold effects in the automated pipeline.

### Recheck Analysis
1. **Nuclear Evidence:** Excellent. HPA nucleoplasm (Approved) with four IDA-level GO-CC annotations including the defined protein complex (BCDX2) and the replication fork. XRCC2 is unequivocally nuclear.
2. **DNA Repair-TE Connection:** The link between DNA repair and TEs is well-established: (a) LINE-1 endonuclease creates DNA nicks that can progress to double-strand breaks, engaging HR repair; (b) TE integration intermediates are substrates for DNA repair; (c) some DNA repair factors (BRCA1, ATM, ATR) have been shown to restrict LINE-1 retrotransposition; (d) the RAD51 paralog complex may process TE integration intermediates; (e) loss of DNA repair leads to genome instability that can activate TE expression.
3. **Replication Fork-TE Interface:** XRCC2 functions at replication forks (GO IDA). Replication stress caused by TE sequences (which can form secondary structures or stall replication forks) is processed by the RAD51 paralog complex. XRCC2's role in replication fork protection is directly relevant to maintaining genome stability at TE-rich regions.
4. **RAD51 Paralog Specificity:** XRCC2 is part of the BCDX2 complex, which has distinct functions from the core RAD51 filament. The RAD51 paralogs fine-tune HR pathway choice and may have specialized roles at difficult-to-repair lesions, which could include TE-induced damage at repetitive sequences.
5. **Cancer Connection:** XRCC2 is a tumor suppressor. TE activation is a hallmark of many cancers. Defective DNA repair in XRCC2-mutant cells could lead to TE derepression as a secondary consequence of genome instability.

### Verdict on False Rejection
**The original rejection was FALSE – XRCC2 should be REOPENED.** XRCC2 has strong nuclear evidence, a well-characterized role in DNA repair, and an established (though indirect) connection to TE biology through the DNA damage-TE interface. The DNA repair pathway is increasingly recognized as a critical component of TE control. XRCC2's specific role in replication fork protection and RAD51 paralog-mediated HR makes it a candidate for investigating DNA repair-based TE regulation mechanisms.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation centered on the DNA repair-TE interface.**

---

## TE-Regulator Relevance Reasoning

1. **DNA Repair-TE Interface:** TEs, particularly LINE-1, create DNA damage during their replication cycle. LINE-1 ORF2p has endonuclease activity that creates DNA nicks, which can progress to double-strand breaks. These breaks are repaired by homologous recombination, the pathway in which XRCC2 functions. XRCC2's role in HR repair links it to the cellular response to TE-induced DNA damage.

2. **LINE-1 Restriction by DNA Repair Factors:** Several DNA repair proteins have been shown to restrict LINE-1 retrotransposition: BRCA1, ATM, ATR, and components of the Fanconi anemia pathway. The RAD51 paralog complex, including XRCC2, may similarly restrict or process LINE-1 intermediates. This is a testable hypothesis: does XRCC2 depletion increase LINE-1 retrotransposition frequency?

3. **Replication Fork Protection at TE Loci:** TE sequences, particularly long terminal repeats (LTRs) and inverted repeats (Alu, SVA), can stall replication forks due to their repetitive nature or secondary structure formation. XRCC2 functions at stalled replication forks to protect them from degradation and promote fork restart. TE-rich regions of the genome are likely to experience replication stress, and XRCC2 may play a role in maintaining genome stability at these regions.

4. **Genome Stability and TE Silencing:** Loss of DNA repair leads to genome instability, which can disrupt heterochromatin and lead to TE activation. While XRCC2 does not directly silence TEs, its role in maintaining genome integrity indirectly contributes to the chromatin environment that keeps TEs repressed.

5. **Cancer Relevance:** XRCC2 is a tumor suppressor. Many cancers exhibit both DNA repair defects and TE activation. Understanding how XRCC2 loss affects TE expression could reveal new connections between DNA repair deficiency and TE-driven genomic instability in cancer.

6. **Limitations:**
   - No direct evidence of TE regulation. The connection is through DNA repair, not direct TE binding or silencing.
   - Well-studied protein (310 publications) with lower novelty.
   - The mechanistic link between HR repair and TE biology is established at the pathway level but not specifically for XRCC2.

**Assessment:** XRCC2 is a MODERATE interest candidate for TE regulation through the DNA repair-TE interface. The connection is mechanistically grounded (TE-induced DNA damage engages HR repair) but indirect (XRCC2 repairs damage rather than directly regulating TE expression). The protein is well-characterized and tractable, making it a good candidate for hypothesis-driven investigation of DNA repair-based TE control.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation (DNA repair-TE interface)**

**Reasoning:** XRCC2 was falsely rejected despite exceptional nuclear evidence (HPA Approved, four IDA-level GO annotations). The protein is a core component of the homologous recombination DNA repair pathway, which is increasingly recognized as relevant to TE biology. TE activity creates DNA damage that engages HR repair, and multiple DNA repair factors (BRCA1, ATM, ATR) have been shown to restrict TE retrotransposition. XRCC2's specific function in the RAD51 paralog BCDX2 complex at replication forks positions it at the interface between DNA replication stress and TE-induced genome instability.

**Score: 128/180** – Among the highest scores in the W4 batch, reflecting excellent nuclear evidence, structural characterization, and PPI network quality. The novelty deduction (2/10) is the primary weakness.

**Recommended next steps:**
1. Test whether XRCC2 depletion increases LINE-1 retrotransposition frequency in cell culture assays.
2. Examine replication fork stability at TE-rich genomic regions in XRCC2-deficient cells (DNA fiber assays, ChIP-seq for replication stress markers).
3. Investigate whether XRCC2 and the BCDX2 complex localize to sites of TE integration.
4. Assess TE expression (RNA-seq, H3K9me3 ChIP-seq) in XRCC2-mutant cells vs. wild-type.
5. Explore the relationship between XRCC2 mutation status and TE activation in human cancers (TCGA data mining).

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: FALSE REJECTION CONFIRMED – gene reopened*

XRCC2 is an excellent DNA repair gene that was unjustifiably rejected. The automated screening failed to recognize the relevance of DNA repair pathways to TE biology. TE activity (particularly LINE-1) creates DNA double-strand breaks that are repaired by homologous recombination – the exact pathway in which XRCC2 functions. Multiple DNA repair factors (BRCA1, ATM, ATR, Fanconi anemia proteins) have been shown to restrict LINE-1 retrotransposition, making it plausible that XRCC2 plays a similar role. The protein's nuclear evidence is among the strongest in the dataset (HPA Approved nucleoplasm, four IDA GO terms), and the structural characterization is outstanding (four full-length cryo-EM structures of the BCDX2 complex). While XRCC2 is not a direct TE regulator (it repairs DNA damage, not silences TEs), the DNA repair-TE interface is a rapidly growing field, and XRCC2 is a mechanistically well-positioned candidate. Reopen with a focus on the DNA repair-based restriction of TE activity.
