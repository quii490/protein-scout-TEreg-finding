# BCLAF1 – Critical False-Rejection Reevaluation Report

**Gene:** BCLAF1 (Bcl-2-associated transcription factor 1)  
**UniProt Accession:** Q9NYF8  
**Protein Name:** Bcl-2-associated transcription factor 1  
**Length:** 920 aa | **Mass:** 106.1 kDa  
**Aliases:** BTF, KIAA0164  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 2 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 26 | HPA: page_found_no_if_image_detected (no IF images available). UniProt: Nucleus speckle (ECO:0000269), Nucleoplasm (ECO:0000269), Nucleus, Cytoplasm. GO-CC: nuclear speck (IDA:HPA), nucleoplasm (IDA:UniProtKB), nucleus (IDA:MGI), mediator complex (IBA:GO_Central). Strong nuclear evidence from UniProt and GO, but HPA image data unavailable for direct verification. The mediator complex annotation (IBA) suggests transcriptional co-regulatory function. Nuclear speck localization suggests involvement in RNA processing/splicing. Minor deduction for dual cytoplasm/nucleus localization. |
| 2. Protein Size | 10 | 8 | 920 aa / 106.1 kDa – large protein. Tractable but requires significant resources for full characterization. Slight deduction for large size. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 114 publications. PubMed>100→REJECTED per scoring rules. BCLAF1 is well-studied with >100 publications. Novelty score = 0/10 due to exceeding the 100-publication rejection threshold. This dimension triggers the automatic rejection rule. |
| 4. 3D Structure | 30 | 10 | AlphaFold mean pLDDT: 46.7 (77.0% <50). VERY LOW confidence structure with extensive predicted disorder. PDB: 7RJN (X-ray, 1.95A, chains C/D=330-339), 7RJR (X-ray, 1.45A, chain B=330-339). Only a 10-residue peptide fragment has been experimentally solved. The rest of the 920 aa protein is predicted disordered by AlphaFold. |
| 5. Regulatory Domains | 50 | 45 | IPR029199 (BCLAF1/THRAP3 family). PF15440. BCLAF1 is a death-promoting transcriptional repressor. GO annotation to mediator complex (IBA:GO_Central) and nuclear speck (RNA processing). BCLAF1 interacts with splicing factors (THRAP3, EIF4A3, MAGOH, RNPS1) and transcription/chromatin regulators (BRCA1, ATRX, H2AX, SNW1). Functions in mRNA stability regulation (CCND1), super-enhancer activation of POLR2A, and chromatin accessibility. This is a MULTIFUNCTIONAL transcription/RNA processing regulator with demonstrated roles in chromatin accessibility. High regulatory domain score for established transcriptional regulatory functions. |
| 6. PPI Network | 50 | 35 | STRING: THRAP3 (0.993, experimental 0.814), EMD (0.971), BCL2 (0.945), CCNB1 (0.94), H2AX (0.924), PNN (0.874), SNIP1 (0.869), EIF4A3 (0.81, experimental 0.613), CLK2 (0.801, experimental 0.781), BRCA1 (0.79), VIRMA (0.775), ATRX (0.769). IntAct: THRAP3 (co-IP), EMD (two-hybrid), GRB2 (pull-down), YWHAG (co-IP), RNPS1 (co-IP), CSNK2A1 (kinase assay), ARRB1/ARRB2 (co-IP), ESR1 (cosedimentation). Large, functionally diverse network including splicing factors, chromatin proteins (ATRX, H2AX, BRCA1), cell cycle regulators, and signaling proteins. ATRX is a known TE regulator (alpha-thalassemia/mental retardation X-linked, deposits H3.3 at telomeres and repetitive elements). |
| **TOTAL** | **180** | **124** | |

**NOTE: PubMed>100 (strict=114) triggers REJECTION rule. Score shown for completeness but gene is automatically REJECTED per pipeline rules.**

---

## Nuclear Evidence Section

### HPA
- **Status:** page_found_no_if_image_detected
- **Key Finding:** HPA page exists but IF images are not available for localization analysis. HPA has contributed IDA evidence to GO for nuclear speck (GO:0016607), confirming HPA-based experimental detection of nuclear localization even though images are not displayable on the current page.
- **Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

### UniProt Subcellular Location
- **Nucleus speckle** – ECO:0000269 (experimental) – Demonstrated localization to nuclear speckles (interchromatin granule clusters involved in pre-mRNA splicing)
- **Nucleus, nucleoplasm** – ECO:0000269 (experimental)
- **Nucleus** (no evidence code) and **Cytoplasm** (no evidence code) also noted

### GO-CC
- **GO:0016607 (nuclear speck)** – IDA:HPA – Direct assay evidence for nuclear speckle localization from HPA
- **GO:0005654 (nucleoplasm)** – IDA:UniProtKB – Direct assay from UniProt
- **GO:0005634 (nucleus)** – IDA:MGI (Mouse Genome Informatics) – Experimental evidence from mouse studies
- **GO:0016592 (mediator complex)** – IBA:GO_Central – Phylogenetically conserved Mediator complex association
- **GO:0005737 (cytoplasm)** – IEA:UniProtKB-SubCell – electronic annotation only

**Summary:** BCLAF1 has strong nuclear evidence (UniProt experimental + GO IDA + HPA IDA) with specific localization to nuclear speckles (splicing factor compartments) and nucleoplasm. Nuclear score: 26/30.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict | 114 |
| Broad | 180 |

**REJECTION TRIGGERED: PubMed strict > 100.** Per pipeline rules, genes with >100 PubMed publications are automatically rejected regardless of other scores.

### Key Papers
1. **PMID:38937794** – Lee SC et al. (2024). BCLAF1 in macrophages and systemic sclerosis.
2. **PMID:38636894** – Zhang P et al. (2024). "BCLAF1 drives esophageal squamous cell carcinoma progression through regulation of YTHDF2-dependent SIX1 mRNA degradation." *Cancer Lett.* – BCLAF1 in mRNA stability/cancer.
3. **PMID:38340178** – Yu Z et al. (2024). "BCLAF1 binds SPOP to stabilize PD-L1 and promotes the development and immune escape of hepatocellular carcinoma." *Cell Mol Life Sci.* – BCLAF1 in immune evasion.
4. **PMID:40220379** – Zhou X et al. (2025). "Bclaf1 mediates super-enhancer-driven activation of POLR2A to enhance chromatin accessibility in nitrosamine-induced esophageal carcinogenesis." *J Hazard Mater.* – KEY: BCLAF1 regulates chromatin accessibility through super-enhancer activation.
5. **PMID:38805063** – Chen J et al. (2024). CircZFR/BCLAF1 in colorectal cancer progression.

**Assessment:** BCLAF1 is heavily studied (114 strict, 180 broad) in cancer biology, apoptosis, transcription, and RNA processing. The literature clearly establishes BCLAF1 as a transcriptional repressor and splicing regulator with effects on chromatin accessibility. However, PubMed count exceeds 100 → automatic rejection.

---

## AlphaFold / PDB / PAE

- **AlphaFold:** mean pLDDT 46.7 – VERY LOW confidence, 77.0% of residues <50 pLDDT
- **PDB:** 7RJN (1.95A, residues 330-339 only), 7RJR (1.45A, residue 330-339 only)
- **Assessment:** Extremely limited structural data. Only a 10-residue peptide has been solved. AlphaFold predicts extensive intrinsic disorder throughout the 920 aa protein. This is consistent with a hub/scaffold protein that uses short linear motifs for multiple protein interactions. PAE 图像暂无数据。

---

## FALSE REJECTION RECHECK

### Analysis
1. **Nuclear evidence:** STRONG – UniProt experimental (ECO:0000269 for nuclear speckle + nucleoplasm), GO IDA level (from HPA and UniProt), Mediator complex association (IBA). HPA images unavailable but GO IDA from HPA confirms experimental detection.
2. **Functional evidence:** BCLAF1 is a transcriptional repressor acting at super-enhancers, regulating chromatin accessibility and RNA processing. These are directly relevant to TE regulation.
3. **PPI network:** Includes ATRX (a known TE/chromatin regulator), BRCA1, H2AX, splicing machinery. ATRX specifically deposits H3.3 at repetitive elements and telomeres.
4. **PubMed:** 114 strict (>100) – TRIGGERS REJECTION RULE.

### Verdict
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 rule.** BCLAF1 exceeds the 100-publication threshold and should be rejected per pipeline rules. However, BCLAF1 is arguably one of the most functionally relevant genes in this batch for TE regulation: it is a transcriptional repressor that regulates chromatin accessibility at super-enhancers, interacts with ATRX (a chromatin remodeler that silences repetitive elements), and localizes to nuclear speckles (RNA processing). The PubMed>100 rule exists to exclude heavily studied genes where novel TE findings are unlikely, but BCLAF1's TE-regulatory functions may be underexplored despite its extensive literature.

**Decision: REJECTED (PubMed>100 rule).** If the PubMed threshold is ever waived for exceptional functional relevance, BCLAF1 should be the first gene reconsidered.

---

## TE-Regulator Relevance

BCLAF1 is highly relevant to TE regulation:
1. **Transcriptional repressor** regulating chromatin accessibility at super-enhancers (PMID:40220379)
2. **ATRX interaction** – ATRX is a SWI/SNF chromatin remodeler that deposits H3.3 at repetitive elements and is essential for silencing ERVs and other TEs
3. **Nuclear speckle localization** – nuclear speckles are sites of pre-mRNA splicing and RNA processing; TE-derived RNAs may be processed at these sites
4. **mRNA stability regulation** (CCND1, YTHDF2-dependent) – could affect TE-derived transcript stability
5. **Mediator complex association** (IBA) – the Mediator complex bridges transcription factors and RNA Pol II, potentially regulating TE transcription

Despite the PubMed>100 rejection, BCLAF1 has STRONG TE-regulatory potential. The interaction with ATRX alone makes it a high-priority target for TE biology.

---

## Final Decision: REJECTED (PubMed>100 rule, strict=114)

Score: 124/180 (shown for completeness). Novelty fails automatic rejection threshold (PubMed>100). Gene is excluded per pipeline rules despite strong nuclear evidence and high TE-regulatory relevance.

---

## Manual Review Note
HIGH PRIORITY EXCEPTION CANDIDATE. BCLAF1 exceeds the PubMed threshold (114 strict publications) triggering automatic rejection. However, BCLAF1 is arguably the most functionally relevant gene for TE regulation in this batch: transcriptional repressor, chromatin accessibility regulator at super-enhancers, direct interactor of ATRX (a major TE silencing factor), and nuclear speckle/splicing function. If a waiver system exists for the PubMed threshold based on exceptional functional relevance, BCLAF1 should be the first gene considered. This gene illustrates a limitation of the PubMed threshold: heavily studied transcriptional/chromatin regulators may have extensive literature without having been examined in TE-specific contexts. Recommend tracking BCLAF1 as a "high priority rejected – exception review needed" case.
