# PKP1 – Critical False-Rejection Reevaluation Report

**Gene:** PKP1
**UniProt Accession:** Q13835
**Protein Name:** Plakophilin-1
**Length:** 747 aa | **Mass:** 82.9 kDa
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 29 | HPA: Nucleoplasm, Plasma membrane (Approved). UniProt: Nucleus, Nucleus, Cytoplasm, perinuclear region. GO-CC: 4 IDA nuclear anno. |
| 2. Protein Size | 10 | 5 | 747 aa / 82.9 kDa – large protein. Tractable but resource-intensive. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 118 (>100 threshold). Well-studied, REJECTED per pipeline rule. |
| 4. 3D Structure | 30 | 14 | AlphaFold mean pLDDT: 69.0. PDB: 1 experimental structure. |
| 5. Regulatory Domains | 50 | 10 | InterPro: IPR011989, IPR016024, IPR000225. Function summary: A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion (PubMed:23444369). Plays a role in desmosome protein expression regulation and localization... |
| 6. PPI Network | 50 | 27 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **85** | |

**NOTE: PubMed>100 (strict=118) triggers automatic REJECTION rule. Score shown for completeness but gene is automatically REJECTED per pipeline rules.**

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm, Plasma membrane
- **IF Image Status:** no_image_detected
- **Nuclear-relevant locations:** Nucleoplasm, Plasma membrane

### UniProt Subcellular Location
- **Cell junction, desmosome** – Evidence: ECO:0000269
- **Nucleus** – Evidence: ECO:0000269
- **Nucleus** – Evidence: ECO:0000269, ECO:0000269
- **Cytoplasm, perinuclear region** – Evidence: ECO:0000269
- **Cytoplasm** – Evidence: ECO:0000269, ECO:0000269
- **Cell junction, desmosome** – Evidence: ECO:0000269, ECO:0000269
- **Cell membrane** – Evidence: ECO:0000269, ECO:0000269
- **Cytoplasm, Stress granule** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0005912 (adherens junction)** – Evidence: IBA:GO_Central
- **GO:0001533 (cornified envelope)** – Evidence: TAS:Reactome
- **GO:0005737 (cytoplasm)** – Evidence: IDA:UniProtKB
- **GO:0010494 (cytoplasmic stress granule)** – Evidence: IEA:UniProtKB-SubCell
- **GO:0030057 (desmosome)** – Evidence: IDA:UniProtKB
- **GO:0101003 (ficolin-1-rich granule membrane)** – Evidence: TAS:Reactome
- **GO:0005882 (intermediate filament)** – Evidence: TAS:ProtInc
- **GO:0097165 (nuclear stress granule)** – Evidence: IDA:UniProtKB
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0048471 (perinuclear region of cytoplasm)** – Evidence: IDA:UniProtKB
- **GO:0005886 (plasma membrane)** – Evidence: IDA:HPA

### Functional Context
- A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion (PubMed:23444369). Plays a role in desmosome protein expression regulation and localization to the desmosomal plaque, thereby maintaining cell sheet integrity and anchorage of desmosomes to intermediate filaments (PubMed:10852826, PubMed:23444369). Required for localization of DSG3 and YAP1 to the cell membrane in keratinocytes in response to mechanical strain, via the formation of an ...

**Summary:** PKP1 has strong nuclear evidence (HPA: Approved reliability; UniProt experimental nuclear evidence; GO: 4 IDA nuclear annotations). Nuclear score: 29/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 118 | `"PKP1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 152 | |
| Broad (All Fields) | 179 | |


**REJECTION TRIGGERED: PubMed strict > 100 (118).**

### Key Papers (with PMIDs)
1. **PMID:38888207** – Luo Q, Li X, Xie K (2024 Oct). "Plakophilin 1 in carcinogenesis." *Molecular carcinogenesis.*
2. **PMID:19945625** – McGrath JA, Mellerio JE (2010 Jan). "Ectodermal dysplasia-skin fragility syndrome." *Dermatologic clinics.*
3. **PMID:35182388** – Boyero L, Martin-Padron J, Fárez-Vidal ME (2022 Apr). "PKP1 and MYC create a feedforward loop linking transcription and translation in squamous cell lung cancer." *Cellular oncology (Dordrecht, Netherlands).*
4. **PMID:40281492** – Zhang X, Wang Z, Zhao Y (2025 Apr 25). "Multi-omics analysis unveils a four-gene prognostic signature in esophageal squamous carcinoma and the therapeutic potential of PKP1." *BMC cancer.*
5. **PMID:31822797** – Martin-Padron J, Boyero L, Rodriguez MI (2020 Aug). "Plakophilin 1 enhances MYC translation, promoting squamous cell lung cancer." *Oncogene.*

### Literature Assessment
- **Total publications:** High (118 strict, 179 broad).
- **Novelty score:** 0/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q13835-F1, version 6
- **Mean pLDDT:** 69.0
- **pLDDT Distribution:**
  - >90 (very high confidence): 41.2%
  - 70-90 (confident): 16.6%
  - 50-70 (low confidence): 6.7%
  - <50 (very low confidence): 35.5%
- **Assessment:** Moderate-to-low confidence. Significant predicted disorder. The protein likely has intrinsically disordered regions.

### Experimental PDB Structures
- **1XM9** – X-ray, 2.80 A, chains: A=244-721

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 14/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| DSP | 0.995 | 0.548 | 0.981 | |
| DSG1 | 0.994 | 0.663 | 0.959 | |
| DSG3 | 0.951 | 0.134 | 0.835 | |
| JUP | 0.946 | 0.098 | 0.885 | |
| PKP3 | 0.916 | 0.000 | 0.643 | |
| DSC1 | 0.905 | 0.543 | 0.585 | |
| DSG2 | 0.895 | 0.134 | 0.763 | |
| DSC3 | 0.894 | 0.134 | 0.705 | |
| EVPL | 0.890 | 0.045 | 0.774 | |
| PPL | 0.866 | 0.045 | 0.724 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| Nphp4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 | psi-mi:"MI:0914"(association) |
| Mks1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 | psi-mi:"MI:0914"(association) |
| NPHP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 | psi-mi:"MI:0914"(association) |
| PBL35 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 | psi-mi:"MI:0915"(physical association) |
| EIF3G1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 | psi-mi:"MI:0915"(physical association) |
| WRKY7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 | psi-mi:"MI:0915"(physical association) |
| Q93ZY0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 | psi-mi:"MI:0915"(physical association) |
| PBL15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Moderate interaction network.**
- **Score:** 27/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
PKP1 was likely auto-rejected due to:
- PubMed>100 (strict=118)
- Low AlphaFold pLDDT (mean 69.0)
- Dual cytoplasm/nucleus localization may have caused ambiguity

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm, Plasma membrane – STRONG, reliability: Approved.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269']).
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269', 'ECO:0000269']).
2. **UniProt Evidence:** Cytoplasm, perinuclear region – ECO:0000269 (experimental, ['ECO:0000269']).
3. **GO-CC Evidence:** 4 IDA-level nuclear annotations present: nuclear stress granule, nucleoplasm, nucleus, perinuclear region of cytoplasm.
4. **PubMed Count:** 118 strict – EXCEEDS 100 threshold. This likely triggered automatic rejection.

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=118) rule.** The gene exceeds the PubMed publication threshold for automatic rejection. However, the nuclear evidence is robust (SCIENCE EVIDENCE: HPA + UniProt experimental + GO IDA annotations), and functional assessment below evaluates whether an exception is warranted.

---

## TE-Regulator Relevance Reasoning

1. **DNA Repair:** PKP1 is involved in DNA repair. TE mobilization creates DNA damage, and DNA repair pathways are intimately linked to TE lifecycle control. Proteins involved in DNA repair often affect TE insertion and excision.
2. **Translation/Ribosome:** PKP1 is involved in translation. TE transcripts can be translated, and translational regulation is a layer of TE control. Ribosome-associated proteins may affect TE-derived protein production.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE interest candidate. Nuclear evidence is present but the connection to TE biology is indirect. The protein is worth retaining for secondary investigation.

---

## Final Decision

**DECISION: REJECTED (PubMed>100 rule)**

**Score: 85/180**

**Reasoning:** PKP1 exceeds the PubMed>100 rejection threshold (118 publications). While nuclear and functional evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules. If exception criteria exist, this gene should be considered for waiver review based on its functional profile.

**If exception is granted:**
1. Screen PKP1 for TE-regulatory functions despite high literature volume.
2. Focus on TE-specific aspects not covered in existing publications.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

PKP1 encodes Plakophilin-1, a 747-amino acid 82.9 kDa protein. 
HPA localizes PKP1 to Nucleoplasm (Approved reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion (PubMed:23444369). Plays a role in desmosome protein expression regulation and localization. 
However, with 118 strict PubMed publications, PKP1 exceeds the pipeline's 100-publication rejection threshold. 
The extensive literature may contain unexplored TE-relevant functions, particularly given PKP1's nuclear localization and functional roles. 
Recommend tracking PKP1 as a 'high priority rejected – exception review needed' case.
