# SULT1E1 – Critical False-Rejection Reevaluation Report

**Gene:** SULT1E1 (Sulfotransferase 1E1)  
**UniProt Accession:** P49888  
**Protein Name:** Sulfotransferase 1E1 (Estrogen sulfotransferase)  
**Length:** 294 aa | **Mass:** 35.1 kDa  
**Aliases:** STE  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 10 | HPA: Nuclear membrane, Cytosol (main). NOT nucleoplasm. The nuclear membrane is the outer boundary of the nucleus but does not represent nucleoplasmic localization. UniProt: Cytoplasm, cytosol (ECO:0000269, experimental) – no nuclear localization with experimental evidence. GO-CC: nuclear membrane (GO:0031965, IDA:HPA) – the only nuclear annotation. No nucleoplasm or nuclear interior annotation. The HPA reliability is Uncertain for this protein. The protein is primarily a cytoplasmic enzyme (sulfotransferase). |
| 2. Protein Size | 10 | 8 | 294 aa / 35.1 kDa – small-moderate. Slightly above tractable small-protein range. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 173 publications. Well-studied protein. Low novelty. |
| 4. 3D Structure | 30 | 30 | AlphaFold mean pLDDT: 97.2. Distribution: 95.2% >90, 3.7% 70-90, 0.7% 50-70, 0.3% <50. Excellent prediction – near-perfect structural confidence. Five (5) high-resolution X-ray crystal structures available: 1G3M (1.70A), 1HY3 (1.80A), 4JVL (1.94A), 4JVM (1.99A), 4JVN (2.05A). All structures cover the full-length protein (1-294). Among the best structurally characterized proteins in the entire screen. Maximum structure score. |
| 5. Regulatory Domains | 50 | 18 | IPR027417 (P-loop containing nucleoside triphosphate hydrolase), IPR000863 (Sulfotransferase domain), PF00685 (Sulfotransferase). The protein is a sulfotransferase that catalyzes the sulfate conjugation of estradiol and estrone using PAPS (3'-phospho-5'-adenylyl sulfate) as a sulfonate donor. This is a key enzyme in estrogen homeostasis – sulfation inactivates estrogens. Has broader substrate specificity: dehydroepiandrosterone (DHEA), pregnenolone, xenobiotics. Also sulfonates 4-ethylphenol (4-EP), a gut microbiota-derived metabolite that crosses the blood-brain barrier and affects myelination and brain connectivity. The enzymatic activity is metabolic (conjugation for inactivation/excretion), not regulatory in the transcriptional sense. However, by controlling estrogen levels, SULT1E1 indirectly regulates estrogen receptor (ER)-mediated transcription. Estrogen receptors are nuclear transcription factors that regulate hundreds of genes. By inactivating estrogens, SULT1E1 modulates the activity of nuclear ER signaling. This is an INDIRECT nuclear regulatory function through hormone metabolism. |
| 6. PPI Network | 50 | 30 | STRING: 15 partners. TERT (0.996, textmining), HSD17B1 (0.962, textmining), UGT1A6 (0.959), CYP19A1 (0.959). Network is dominated by steroid metabolism enzymes (HSD17B1, HSD17B2, CYP19A1, CYP1A1, CYP3A4) and UGT glucuronosyltransferases. TERT (telomerase reverse transcriptase) association is textmining-only. IntAct: 13 interactors including TP53 (two-hybrid, PMID:16169070), SETDB1 (two-hybrid, PMID:16169070), RIF1 (two-hybrid, PMID:16169070), UNC119 (two-hybrid), EEF1A1 (two-hybrid). The TP53 interaction is notable: p53 regulates estrogen signaling and SULT1E1 may influence p53 through estrogen modulation. SETDB1 is HIGHLY relevant: SETDB1 is a histone H3K9 methyltransferase that is the major enzyme responsible for silencing endogenous retroviruses and other TEs in embryonic stem cells and early embryos. SETDB1 deposits H3K9me3 at TE loci, recruiting KRAB-ZFP/KAP1 complexes. RIF1 is involved in DNA double-strand break repair pathway choice and telomere homeostasis. However, all IntAct interactions are from large-scale two-hybrid pooling approaches (MI:0398, PMID:16169070) – low-confidence screening data. |
| **TOTAL** | **180** | **100** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Uncertain
- **Main Location:** Nuclear membrane, Cytosol
- **Additional Locations:** None
- **Key Finding:** HPA detects SULT1E1 at the Nuclear membrane and Cytosol. The reliability is Uncertain (lowest quality tier). Importantly, there is NO nucleoplasm detection. The nuclear membrane is a specialized compartment – it is the lipid bilayer surrounding the nucleus, not the nucleoplasmic interior where chromatin resides. Proteins at the nuclear membrane (e.g., LINC complex, nuclear pore components) are typically structural, not chromatin-interacting.

**Interpretation note:** The Uncertain reliability and lack of nucleoplasm detection are significant negatives for nuclear scoring. Nuclear membrane localization may reflect association with the cytoplasmic face of the outer nuclear membrane (which is continuous with the ER) rather than the inner nuclear membrane. SULT1E1 is a cytosolic enzyme and the nuclear membrane signal could represent ER/nuclear envelope association during estrogen metabolism.

### UniProt Subcellular Location
- **Cytoplasm, cytosol** – Evidence: ECO:0000269 (experimental). The single UniProt subcellular location with experimental evidence. No nuclear localization in UniProt.

### GO Cellular Component (GO-CC)
- **GO:0005737 (cytoplasm)** – Evidence: IBA:GO_Central – phylogenetically conserved.
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA – direct assay.
- **GO:0031965 (nuclear membrane)** – Evidence: IDA:HPA – direct assay. The only nuclear annotation. Specifically nuclear MEMBRANE, not nucleoplasm.

### Functional Nuclear Context
- **Indirect Nuclear Influence:** SULT1E1 is a metabolic enzyme that sulfonates and inactivates estrogens. By controlling the availability of active estrogens, SULT1E1 indirectly modulates estrogen receptor (ER) activity. ER alpha and ER beta are ligand-activated nuclear transcription factors. When estradiol levels are high, ER translocates to the nucleus, dimerizes, binds estrogen response elements (EREs), and activates transcription of target genes. When SULT1E1 sulfonates estradiol, it inactivates the hormone, reducing ER-mediated transcription. This is an indirect, hormone-level regulatory mechanism.
- **Tissue-Specific Impact:** SULT1E1 is expressed in estrogen-sensitive tissues (endometrium, breast, liver). Its activity affects local estrogen concentrations and thus ER signaling intensity in these tissues.
- **No Direct Nuclear Function:** SULT1E1 does not enter the nucleus, bind DNA, modify chromatin, or regulate transcription directly. It is a cytoplasmic enzyme whose products affect nuclear events.

**Summary:** SULT1E1 has weak nuclear evidence. HPA shows nuclear membrane only (not nucleoplasm) with Uncertain reliability. UniProt lists no nuclear localization. The sole nuclear GO annotation is for nuclear membrane, not the nuclear interior. SULT1E1 is a cytoplasmic metabolic enzyme. The only connection to nuclear regulation is indirect (estrogen inactivation modulates ER transcription factor activity). Nuclear score: 10/30 – given for nuclear membrane detection and indirect hormone-mediated influence on nuclear receptors.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 173 | `"SULT1E1"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 329 | `"SULT1E1"[Title/Abstract]` |
| Broad (All Fields) | 329 | `"SULT1E1"` |

**Alias Note:** Alias STE observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:33799763** – Yi M, et al. (2021). "Estrogen Sulfotransferase (SULT1E1): Its Molecular Regulation, Polymorphisms, and Clinical Perspectives." *Int J Mol Sci.* – Comprehensive review of SULT1E1 biology and clinical significance.
2. **PMID:40256713** – Overexpression of SULT1E1 alleviates salt-processed Psoraleae Fructus-induced cholestatic liver damage. Liver disease study.
3. **PMID:39762281** – Estrogen sulfotransferase SULT1E1 expression correlates with progression and prognosis of lung adenocarcinoma. Cancer biomarker study.
4. **PMID:38412094** – Single-cell analysis reveals insights into epithelial abnormalities in ovarian endometriosis.
5. **PMID:32372097** – Metformin inhibits testosterone-induced endoplasmic reticulum stress in ovarian granulosa cells via inactivation of p38 MAPK.

### Literature Assessment
- **Total publications:** Well-studied (173 strict, 329 broad). Extensive literature on estrogen metabolism and cancer.
- **Thematic focus:** Estrogen metabolism, hormone-dependent cancers (breast, endometrial, ovarian), drug metabolism (sulfation of xenobiotics). SULT1E1 is a pharmacologically important enzyme.
- **Key biological role:** SULT1E1 is the primary enzyme that inactivates estrogens through sulfation. Its activity controls local and systemic estrogen levels, which in turn regulate ER-mediated transcription in target tissues.
- **No publications on TE regulation.**
- **Novelty score:** 4/10 (>100 publications = lower novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P49888-F1, version 6
- **Mean pLDDT:** 97.2
- **pLDDT Distribution:**
  - >90 (very high confidence): 95.2%
  - 70-90 (confident): 3.7%
  - 50-70 (low confidence): 0.7%
  - <50 (very low confidence): 0.3%
- **Assessment:** Exceptional prediction quality. 95.2% very high confidence, near-zero disorder (0.3% <50). The AlphaFold model is essentially equivalent to the experimental structures in quality.

### Experimental PDB Structures
- **1G3M** – X-ray, 1.70A. SULT1E1 with product (PAP) bound. Chains A/B cover full-length 1-294.
- **1HY3** – X-ray, 1.80A. SULT1E1 with inactive cofactor. Full-length.
- **4JVL** – X-ray, 1.94A. SULT1E1 with substrate analog. Full-length.
- **4JVM** – X-ray, 1.99A. SULT1E1 with inhibitor. Full-length.
- **4JVN** – X-ray, 2.05A. SULT1E1 with substrate. Full-length.

All five structures are high-resolution (<2.1A), cover the full-length protein, and represent multiple liganded states. This is an exceptionally well-characterized structure.

### Structural Assessment
- SULT1E1 is among the best structurally characterized proteins in the entire dataset. Five high-resolution X-ray structures in multiple liganded states provide atomic-level detail of the catalytic mechanism. The AlphaFold model (mean pLDDT 97.2) independently confirms the high structural quality.
- The sulfotransferase fold (PF00685) is a Rossmann-like alpha/beta fold with a characteristic PAPS-binding site and substrate-binding cleft. The structures show how estradiol and other substrates are positioned for sulfation.
- **Score:** 30/30 – Maximum score. Exceptional structural characterization.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| TERT | 0.996 | 0 | 0.996 | Telomerase, textmining only |
| HSD17B1 | 0.962 | 0 | 0.635 | Hydroxysteroid dehydrogenase, estrogen metabolism |
| UGT1A6 | 0.959 | 0 | 0.591 | UDP-glucuronosyltransferase, detoxification |
| HSD17B2 | 0.959 | 0 | 0.582 | Hydroxysteroid dehydrogenase |
| CYP19A1 | 0.959 | 0 | 0.608 | Aromatase, estrogen synthesis |
| UGT1A10 | 0.958 | 0 | 0.591 | UDP-glucuronosyltransferase |
| UGT1A4 | 0.958 | 0 | 0.591 | UDP-glucuronosyltransferase |
| CYP1A1 | 0.948 | 0 | 0.479 | Cytochrome P450, estrogen metabolism |
| CYP3A4 | 0.947 | 0 | 0.435 | Cytochrome P450, drug metabolism |

**Note:** All scores are textmining/co-occurrence. No experimental interaction confidence. The network is functionally coherent: all partners are enzymes in estrogen biosynthesis, metabolism, or conjugation pathways.

### IntAct
Total: 13 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| BMPR2 | pull down | PMID:15188402 | association |
| SULT2B1 | two hybrid pooling | PMID:16189514 | physical association |
| ENOX1 | two hybrid pooling | PMID:16189514 | physical association |
| TP53 | two hybrid pooling | PMID:16169070 | physical association |
| UNC119 | two hybrid pooling | PMID:16169070 | physical association |
| EEF1A1 | two hybrid pooling | PMID:16169070 | physical association |
| RIF1 | two hybrid pooling | PMID:16169070 | physical association |
| SETDB1 | two hybrid pooling | PMID:16169070 | physical association |

### PPI Network Assessment
- **Metabolic enzyme network in STRING:** Coherent network of Phase I/II drug metabolism and steroidogenic enzymes. Functionally logical.
- **SETDB1 (ERG-associated protein with SET domain, bifurcated 1):** This is the most significant interaction for TE biology. SETDB1 is a histone H3K9 methyltransferase responsible for depositing H3K9me3 at endogenous retroviruses and other TEs. It is the core enzyme in the KRAB-ZFP/KAP1/SETDB1/H3K9me3 TE silencing pathway. SETDB1 is essential for embryonic development because it silences TEs that would otherwise be transcribed and cause genome instability. The SULT1E1-SETDB1 interaction was detected by two-hybrid pooling (PMID:16169070). If validated, this would connect an estrogen-metabolizing enzyme to the TE silencing machinery. However, two-hybrid pooling is a low-confidence screening method with high false-positive rates.
- **TP53:** p53 tumor suppressor. Two-hybrid only. Estrogen metabolism and p53 signaling are interconnected in hormone-dependent cancers, so this association has biological plausibility.
- **RIF1:** DNA repair and telomere homeostasis protein. Two-hybrid only. RIF1 regulates DNA double-strand break repair pathway choice (NHEJ vs HR) and is involved in replication timing. Nuclear protein.
- **Caveat:** All interesting nuclear interactions (SETDB1, TP53, RIF1) come from the same large-scale two-hybrid pooling study (PMID:16169070), which is known for promiscuous interactions. None have been validated by orthogonal methods.
- **Score:** 30/50 – High score due to the SETDB1 interaction (direct relevance to TE silencing) and TP53/RIF1 nuclear connections. However, all interactions are low-confidence two-hybrid and must be interpreted cautiously.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SULT1E1 was likely auto-rejected because:
1. Nuclear localization is limited to nuclear membrane, not nucleoplasm. HPA reliability is Uncertain.
2. The protein is a well-characterized cytoplasmic metabolic enzyme (sulfotransferase).
3. No direct nuclear function. The connection to transcription is indirect (hormone inactivation).

### Recheck Analysis
1. **Nuclear Evidence Quality:** Nuclear membrane only (not nucleoplasm), with Uncertain HPA reliability. UniProt lists no nuclear localization. This is among the weakest nuclear evidence profiles among CRITICAL reopen genes.
2. **SETDB1 Interaction:** The two-hybrid interaction with SETDB1 (PMID:16169070) is the single most significant finding for TE biology. SETDB1 is the master H3K9me3 methyltransferase for TE silencing. If this interaction is real, it could mean SULT1E1 has a non-canonical function in the SETDB1 pathway, perhaps modulating its activity or localization. However, this is a single low-confidence two-hybrid hit.
3. **Estrogen-TE Connection:** Estrogen receptor signaling influences chromatin organization and transcription genome-wide. ER has been shown to affect TE expression indirectly through chromatin remodeling. SULT1E1, by controlling estradiol levels, could influence this ER-TE axis. However, this is a systemic hormonal effect, not a direct SULT1E1 function.
4. **Indirect vs. Direct:** The core problem is that SULT1E1's connection to nuclear biology is indirect (through its metabolic product, estrone/estradiol sulfate, which cannot activate ER). This is fundamentally different from a protein that enters the nucleus and directly regulates transcription or chromatin.

### Verdict on False Rejection
**The original rejection was PROBABLY CORRECT – SULT1E1 is a metabolic enzyme, not a nuclear regulator.** The nuclear membrane detection (Uncertain) does not constitute nucleoplasmic localization. The SETDB1 interaction is intriguing but unvalidated (two-hybrid only). Without the SETDB1 interaction, SULT1E1 would have no plausible direct connection to nuclear regulation. With it, there is a speculative hypothesis that would require substantial experimental validation.

**This gene is BORDERLINE for reopening.** The SETDB1 interaction creates a direct TE-relevant connection, but the weak nuclear localization and primary metabolic function argue against reopening. The structural data (5 X-ray structures, max score) is excellent but irrelevant to TE regulation.

---

## TE-Regulator Relevance Reasoning

1. **Weak Nuclear Localization:** HPA detects only nuclear membrane (not nucleoplasm) with Uncertain reliability. SULT1E1 is a cytoplasmic enzyme and has no demonstrated access to the nuclear interior where chromatin resides.

2. **Indirect Estrogen Modulation:** SULT1E1 inactivates estrogens through sulfation. This reduces estrogen receptor (ER) signaling, which in turn affects ER-mediated transcription at hundreds of genomic loci. This is a systemic hormonal effect, not a direct SULT1E1 function. Estrogen levels modulate TE expression in ER-responsive tissues, so SULT1E1 could influence TE activity indirectly. However, many factors regulate estrogen levels (biosynthesis, other metabolizing enzymes, binding proteins), making SULT1E1 just one component of a complex hormonal system.

3. **SETDB1 Interaction:** The two-hybrid detection of SETDB1 interaction is the most direct TE-relevant connection. SETDB1 silences TEs through H3K9me3 deposition. If SULT1E1 physically interacts with SETDB1, it might modulate SETDB1 activity, localization, or substrate specificity. SULT1E1 could potentially sulfonate SETDB1 (post-translational modification) affecting its function, or the interaction could be in the context of a larger complex. However, this is entirely speculative and based on a single screening hit.

4. **Gut-Brain Axis:** SULT1E1 sulfonates 4-ethylphenol (4-EP), a gut microbiota-derived metabolite. 4-EPS crosses the blood-brain barrier and affects oligodendrocyte maturation and myelination. This demonstrates SULT1E1's role extends beyond estrogen metabolism to broader metabolic regulation, but this function is also enzymatic and cytoplasmic.

5. **Tissue Context:** SULT1E1 is expressed in estrogen-sensitive tissues (endometrium, breast, liver). If the SETDB1 interaction is tissue-specific, it could have a specialized nuclear function in these tissues.

**Assessment:** SULT1E1 is a LOW-MODERATE interest candidate for TE regulation. The SETDB1 interaction provides a tantalizing but unvalidated direct connection. Without validation, SULT1E1 is a metabolic enzyme with incidental nuclear membrane detection. The excellent structural characterization is useful for mechanistic studies if the SETDB1 interaction is confirmed.

---

## Final Decision

**DECISION: BORDERLINE – can be reopened ONLY if the SETDB1 interaction is prioritized for validation**

**Reasoning:** SULT1E1 has weak nuclear localization (nuclear membrane only, Uncertain HPA) and a primary function as a cytoplasmic metabolic enzyme. However, the two-hybrid interaction with SETDB1 (the master H3K9me3 methyltransferase for TE silencing) creates a direct, testable hypothesis for TE-regulatory function. The decision to reopen should depend on whether resources exist to validate the SETDB1 interaction (co-IP in relevant cell types, proximity ligation assay). Without validation, SULT1E1 should remain rejected. With validation, it could represent a novel connection between estrogen metabolism and TE silencing.

**Score: 100/180** – Inflated by the excellent structural score (30/30) and SETDB1 PPI connection. The nuclear localization score (10/30) is the primary weakness.

**Recommended next steps (if reopened):**
1. Validate SULT1E1-SETDB1 interaction by co-IP in estrogen-responsive cell lines (MCF-7, Ishikawa).
2. Determine if SULT1E1 can sulfonate SETDB1 (post-translational modification hypothesis).
3. Investigate whether SULT1E1 overexpression/knockdown affects H3K9me3 levels at TE loci.
4. Examine whether SULT1E1-SETDB1 interaction is regulated by estrogen levels (linking the metabolic and epigenetic functions).

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: BORDERLINE – metabolic enzyme with speculative SETDB1 connection*

SULT1E1 exemplifies a difficult case: the protein is clearly a metabolic enzyme with weak nuclear evidence, but a single high-value interaction (SETDB1) creates a plausible TE-regulatory hypothesis. The decision hinges on whether the SETDB1 two-hybrid hit is real or artifactual. Two-hybrid pooling (MI:0398, PMID:16169070) is a screening method with known false-positive issues. However, SETDB1 is such a central TE-relevant protein that any potential interaction partner deserves scrutiny. The protein's excellent structural characterization (5 X-ray structures at <2.1A) means that if the interaction is validated, detailed mechanistic studies are immediately possible. My recommendation: reopen ONLY if resources are specifically allocated to validate the SETDB1 interaction. Otherwise, the weak nuclear evidence and established metabolic function justify remaining rejected.
