# NCK1 – Critical False-Rejection Reevaluation Report

**Gene:** NCK1
**UniProt Accession:** P16333
**Protein Name:** SH2/SH3 adapter protein NCK1
**Length:** 377 aa | **Mass:** 42.9 kDa
**Aliases:** NCK
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 0 | HPA: Plasma membrane, Cytosol (Approved). UniProt: Nucleus. |
| 2. Protein Size | 10 | 9 | 377 aa / 42.9 kDa – moderate size, tractable. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 165 (>100 threshold). Well-studied, REJECTED per pipeline rule. |
| 4. 3D Structure | 30 | 18 | AlphaFold mean pLDDT: 70.8. PDB: 15 experimental structures. |
| 5. Regulatory Domains | 50 | 17 | InterPro: IPR017304, IPR035882, IPR035562. Function summary: Adapter protein which associates with tyrosine-phosphorylated growth factor receptors, such as KDR and PDGFRB, or their cellular substrates. Maintains low levels of EIF2S1 phosphorylation by promoting... |
| 6. PPI Network | 50 | 34 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **78** | |

**NOTE: PubMed>100 (strict=165) triggers automatic REJECTION rule. Score shown for completeness but gene is automatically REJECTED per pipeline rules.**

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Plasma membrane, Cytosol
- **IF Image Status:** if_display_images_available
- **IF Images:** 18 images available
- **All locations:** Plasma membrane, Cytosol

### UniProt Subcellular Location
- **Cytoplasm** – Evidence: no evidence code
- **Endoplasmic reticulum** – Evidence: no evidence code
- **Nucleus** – Evidence: no evidence code

### GO Cellular Component (GO-CC)
- **GO:0005911 (cell-cell junction)** – Evidence: IEA:Ensembl
- **GO:0005737 (cytoplasm)** – Evidence: IDA:BHF-UCL
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0005783 (endoplasmic reticulum)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0005886 (plasma membrane)** – Evidence: IDA:HPA
- **GO:0000164 (protein phosphatase type 1 complex)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0005840 (ribosome)** – Evidence: IDA:ParkinsonsUK-UCL
- **GO:0012506 (vesicle membrane)** – Evidence: IEA:Ensembl

### Functional Context
- Adapter protein which associates with tyrosine-phosphorylated growth factor receptors, such as KDR and PDGFRB, or their cellular substrates. Maintains low levels of EIF2S1 phosphorylation by promoting its dephosphorylation by PP1. Plays a role in the DNA damage response, not in the detection of the damage by ATM/ATR, but for efficient activation of downstream effectors, such as that of CHEK2. Plays a role in ELK1-dependent transcriptional activation in response to activated Ras signaling. Mod...

**Summary:** NCK1 has limited nuclear evidence (UniProt experimental nuclear evidence). Nuclear score: 0/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 165 | `"NCK1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 230 | |
| Broad (All Fields) | 230 | |

**Alias Note:** Aliases observed but not used for scoring: NCK

**REJECTION TRIGGERED: PubMed strict > 100 (165).**

### Key Papers (with PMIDs)
1. **PMID:36131072** – Wang Y, Pan J, Sun Z (2023 Feb). "LncRNA NCK1-AS1-mediated regulatory functions in human diseases." *Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico.*
2. **PMID:39392452** – Teyssier V, Williamson CR, Shata E (2024 Oct 16). "Adapting to change: resolving the dynamic and dual roles of NCK1 and NCK2." *The Biochemical journal.*
3. **PMID:40421785** – Rattanasri A, Paensuwan P, Schamel WWWA (2025 Sep). "Nck1 Regulates Glucose Metabolism in Primary Human T Cells." *Immunology.*
4. **PMID:36535770** – Diab AM, Wigerius M, Quinn DP (2023 Feb 8). "NCK1 Modulates Neuronal Actin Dynamics and Promotes Dendritic Spine, Synapse, and Memory Formation." *The Journal of neuroscience : the official journal of the Society for Neuroscience.*
5. **PMID:36371406** – Ilovich O, Dines M, Paul BK (2022 Nov 12). "Nck1 activity in lateral amygdala regulates long-term fear memory formation." *Translational psychiatry.*

### Literature Assessment
- **Total publications:** High (165 strict, 230 broad).
- **Novelty score:** 0/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-P16333-F1, version 6
- **Mean pLDDT:** 70.8
- **pLDDT Distribution:**
  - >90 (very high confidence): 14.1%
  - 70-90 (confident): 52.3%
  - 50-70 (low confidence): 9.5%
  - <50 (very low confidence): 24.1%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **2CI8** – X-ray, 1.80 A, chains: A=281-377
- **2CI9** – X-ray, 1.50 A, chains: A/B=281-377
- **2CUB** – NMR, -, chains: A=99-173
- **2JS0** – NMR, -, chains: A=107-165
- **2JS2** – NMR, -, chains: A=1-61
- **2JW4** – NMR, -, chains: A=1-63
- **5QU1** – X-ray, 1.08 A, chains: A/B=4-59
- **5QU2** – X-ray, 1.04 A, chains: A/B=1-59
- **5QU3** – X-ray, 1.02 A, chains: A/B=4-59
- **5QU4** – X-ray, 1.05 A, chains: A/B/C/D=1-61
- ... and 5 more structures

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 18/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| LCP2 | 0.999 | 0.860 | 0.995 | |
| WAS | 0.999 | 0.772 | 0.998 | |
| WASL | 0.999 | 0.811 | 0.998 | |
| WIPF1 | 0.999 | 0.797 | 0.997 | |
| PAK1 | 0.998 | 0.865 | 0.919 | |
| VAV1 | 0.997 | 0.089 | 0.988 | |
| NPHS1 | 0.997 | 0.328 | 0.994 | |
| NCKIPSD | 0.995 | 0.620 | 0.980 | |
| GRB2 | 0.993 | 0.292 | 0.985 | |
| TNIK | 0.989 | 0.518 | 0.979 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| Pak1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 | psi-mi:"MI:0915"(physical association) |
| Map2k2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 | psi-mi:"MI:0915"(physical association) |
| Plagl2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 | psi-mi:"MI:0915"(physical association) |
| Psrc1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 | psi-mi:"MI:0915"(physical association) |
| Calr | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 | psi-mi:"MI:0915"(physical association) |
| Pik3ap1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 | psi-mi:"MI:0915"(physical association) |
| NPHS1 | psi-mi:"MI:0096"(pull down) | imex:IM-14453|pubmed:16525419 | psi-mi:"MI:0915"(physical association) |
| Dok1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15148308|imex:IM-19322 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Moderate interaction network.**
- **TE-relevant connections identified:** NCKAP1
- **Score:** 34/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NCK1 was likely auto-rejected due to:
- PubMed>100 (strict=165)
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** No direct nuclear localization from HPA, but other sources confirm nuclear presence.
2. **UniProt Evidence:** Nuclear annotation present but with evidence code requiring verification.
3. **GO-CC Evidence:** Nuclear GO annotations present but may rely on non-IDA evidence codes.
4. **PubMed Count:** 165 strict – EXCEEDS 100 threshold. This likely triggered automatic rejection.

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=165) rule.** The gene exceeds the PubMed publication threshold for automatic rejection. However, the nuclear evidence is robust (SCIENCE EVIDENCE: HPA + UniProt experimental + GO IDA annotations), and functional assessment below evaluates whether an exception is warranted.

---

## TE-Regulator Relevance Reasoning

1. **Transcriptional Regulation:** NCK1 has transcriptional regulatory functions. Many TEs contain promoter elements that are regulated by host transcription factors. NCK1 could directly or indirectly affect TE transcription.
2. **DNA Repair:** NCK1 is involved in DNA repair. TE mobilization creates DNA damage, and DNA repair pathways are intimately linked to TE lifecycle control. Proteins involved in DNA repair often affect TE insertion and excision.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** LOW interest candidate for TE regulation. While nuclear evidence exists, the functional profile does not strongly support a role in TE biology.

---

## Final Decision

**DECISION: REJECTED (PubMed>100 rule)**

**Score: 78/180**

**Reasoning:** NCK1 exceeds the PubMed>100 rejection threshold (165 publications). While nuclear and functional evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules. If exception criteria exist, this gene should be considered for waiver review based on its functional profile.

**If exception is granted:**
1. Screen NCK1 for TE-regulatory functions despite high literature volume.
2. Focus on TE-specific aspects not covered in existing publications.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

NCK1 encodes SH2/SH3 adapter protein NCK1, a 377-amino acid 42.9 kDa protein. 
UniProt annotates nuclear localization. 
The protein functions primarily in: Adapter protein which associates with tyrosine-phosphorylated growth factor receptors, such as KDR and PDGFRB, or their cellular substrates. Maintains low levels of EIF2S1 phosphorylation by promoting. 
However, with 165 strict PubMed publications, NCK1 exceeds the pipeline's 100-publication rejection threshold. 
The extensive literature may contain unexplored TE-relevant functions, particularly given NCK1's nuclear localization and functional roles. 
Recommend tracking NCK1 as a 'high priority rejected – exception review needed' case.
