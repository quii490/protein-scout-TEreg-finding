# NEK1 – Critical False-Rejection Reevaluation Report

**Gene:** NEK1
**UniProt Accession:** Q96PY6
**Protein Name:** Serine/threonine-protein kinase Nek1
**Length:** 1258 aa | **Mass:** 142.8 kDa
**Aliases:** KIAA1901
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 22 | HPA: Nucleoplasm, Primary cilium, Centriolar satellite, Cytosol (Supported). UniProt: Nucleus. GO-CC: 2 IDA nuclear anno. |
| 2. Protein Size | 10 | 1 | 1258 aa / 142.8 kDa – very large protein. Significant resource commitment for full characterization. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 147 (>100 threshold). Well-studied, REJECTED per pipeline rule. |
| 4. 3D Structure | 30 | 8 | AlphaFold mean pLDDT: 56.9. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 7 | InterPro: IPR011009, IPR051131, IPR000719. Function summary: Phosphorylates serines and threonines, but also appears to possess tyrosine kinase activity (PubMed:20230784). Involved in DNA damage checkpoint control and for proper DNA damage repair (PubMed:202307... |
| 6. PPI Network | 50 | 20 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **58** | |

**NOTE: PubMed>100 (strict=147) triggers automatic REJECTION rule. Score shown for completeness but gene is automatically REJECTED per pipeline rules.**

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional Locations:** Primary cilium, Centriolar satellite, Cytosol
- **IF Image Status:** no_image_detected
- **Nuclear-relevant locations:** Nucleoplasm, Primary cilium, Centriolar satellite, Cytosol

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000269, ECO:0000305
- **Cytoplasm, cytoskeleton, microtubule organizing center, centrosome** – Evidence: ECO:0000250
- **Cytoplasm** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0034451 (centriolar satellite)** – Evidence: IDA:HPA
- **GO:0005813 (centrosome)** – Evidence: IDA:UniProtKB
- **GO:0005929 (cilium)** – Evidence: IDA:HPA
- **GO:0005737 (cytoplasm)** – Evidence: IDA:MGI
- **GO:0005829 (cytosol)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:MGI
- **GO:0000242 (pericentriolar material)** – Evidence: IDA:UniProtKB

### Functional Context
- Phosphorylates serines and threonines, but also appears to possess tyrosine kinase activity (PubMed:20230784). Involved in DNA damage checkpoint control and for proper DNA damage repair (PubMed:20230784). In response to injury that includes DNA damage, NEK1 phosphorylates VDAC1 to limit mitochondrial cell death (PubMed:20230784). May be implicated in the control of meiosis (By similarity). Involved in cilium assembly (PubMed:21211617)

**Summary:** NEK1 has strong nuclear evidence (HPA: Supported reliability; UniProt experimental nuclear evidence; GO: 2 IDA nuclear annotations). Nuclear score: 22/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 147 | `"NEK1"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR h...` |
| Symbol Only (Title/Abstract) | 206 | |
| Broad (All Fields) | 256 | |

**Alias Note:** Aliases observed but not used for scoring: KIAA1901

**REJECTION TRIGGERED: PubMed strict > 100 (147).**

### Key Papers (with PMIDs)
1. **PMID:30837838** – Prasad A, Bharathi V, Sivalingam V (2019). "Molecular Mechanisms of TDP-43 Misfolding and Pathology in Amyotrophic Lateral Sclerosis." *Frontiers in molecular neuroscience.*
2. **PMID:34729299** – Jiang M, Jia K, Wang L (2021 Oct). "Alterations of DNA damage response pathway: Biomarker and therapeutic strategy for cancer immunotherapy." *Acta pharmaceutica Sinica. B.*
3. **PMID:34544842** – Chen YP, Yu SH, Wei QQ (2022 Sep). "Role of genetics in amyotrophic lateral sclerosis: a large cohort study in Chinese mainland population." *Journal of medical genetics.*
4. **PMID:31735643** – Zhu Y, Gu L, Lin X (2020 Jan 2). "Dynamic Regulation of ME1 Phosphorylation and Acetylation Affects Lipid Metabolism and Colorectal Tumorigenesis." *Molecular cell.*
5. **PMID:40389989** – Noh MY, Oh SI, Kim YE (2025 May 20). "Mutations in NEK1 cause ciliary dysfunction as a novel pathogenic mechanism in amyotrophic lateral sclerosis." *Molecular neurodegeneration.*

### Literature Assessment
- **Total publications:** High (147 strict, 256 broad).
- **Novelty score:** 0/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q96PY6-F1, version 6
- **Mean pLDDT:** 56.9
- **pLDDT Distribution:**
  - >90 (very high confidence): 16.9%
  - 70-90 (confident): 26.8%
  - 50-70 (low confidence): 6.9%
  - <50 (very low confidence): 49.4%
- **Assessment:** Moderate-to-low confidence. Significant predicted disorder. The protein likely has intrinsically disordered regions.

### Experimental PDB Structures
- **4APC** – X-ray, 2.10 A, chains: A/B=1-328
- **4B9D** – X-ray, 1.90 A, chains: A/B=1-328

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 8/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| CFAP410 | 0.982 | 0.609 | 0.956 | |
| DYNC2H1 | 0.972 | 0.000 | 0.969 | |
| ALS2 | 0.942 | 0.778 | 0.746 | |
| KIF3A | 0.802 | 0.230 | 0.733 | |
| CHCHD10 | 0.733 | 0.000 | 0.733 | |
| VAPB | 0.717 | 0.000 | 0.715 | |
| MATR3 | 0.661 | 0.000 | 0.656 | |
| MATR3-2 | 0.661 | 0.000 | 0.656 | |
| RCC1L | 0.658 | 0.000 | 0.658 | |
| CEP290 | 0.635 | 0.112 | 0.338 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| ENSP00000408020.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| ZNF350 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| FEZ2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| FEZ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| YWHAH | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| ATRX | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| MRE11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| TP53BP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Limited interaction network.**
- **TE-relevant connections identified:** CHCHD10, MATR3, MATR3-2
- **Score:** 20/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NEK1 was likely auto-rejected due to:
- PubMed>100 (strict=147)
- Low AlphaFold pLDDT (mean 56.9)
- Dual cytoplasm/nucleus localization may have caused ambiguity
- Large protein size (1258 aa)

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm – PRESENT, reliability: Supported.
2. **UniProt Evidence:** Nucleus – ECO:0000269 (experimental, ['ECO:0000269', 'ECO:0000305']).
3. **GO-CC Evidence:** 2 IDA-level nuclear annotations present: nucleoplasm, nucleus.
4. **PubMed Count:** 147 strict – EXCEEDS 100 threshold. This likely triggered automatic rejection.

### Verdict on False Rejection
**The original rejection was TECHNICALLY CORRECT under the PubMed>100 (strict=147) rule.** The gene exceeds the PubMed publication threshold for automatic rejection. However, the nuclear evidence is robust (SCIENCE EVIDENCE: HPA + UniProt experimental + GO IDA annotations), and functional assessment below evaluates whether an exception is warranted.

---

## TE-Regulator Relevance Reasoning

1. **DNA Repair:** NEK1 is involved in DNA repair. TE mobilization creates DNA damage, and DNA repair pathways are intimately linked to TE lifecycle control. Proteins involved in DNA repair often affect TE insertion and excision.
2. **Cell Cycle:** NEK1 functions in cell cycle/mitosis/meiosis. TE expression is often cell-cycle regulated, and cell cycle proteins can influence chromatin states at TE loci during division.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE interest candidate. Nuclear evidence is present but the connection to TE biology is indirect. The protein is worth retaining for secondary investigation.

---

## Final Decision

**DECISION: REJECTED (PubMed>100 rule)**

**Score: 58/180**

**Reasoning:** NEK1 exceeds the PubMed>100 rejection threshold (147 publications). While nuclear and functional evidence may be present, the high literature volume triggers automatic exclusion per pipeline rules. If exception criteria exist, this gene should be considered for waiver review based on its functional profile.

**If exception is granted:**
1. Screen NEK1 for TE-regulatory functions despite high literature volume.
2. Focus on TE-specific aspects not covered in existing publications.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: CONFIRMED REJECTION per PubMed>100 rule – exception review recommended*

NEK1 encodes Serine/threonine-protein kinase Nek1, a 1258-amino acid 142.8 kDa protein. 
HPA localizes NEK1 to Nucleoplasm (Supported reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Phosphorylates serines and threonines, but also appears to possess tyrosine kinase activity (PubMed:20230784). Involved in DNA damage checkpoint control and for proper DNA damage repair (PubMed:202307. 
However, with 147 strict PubMed publications, NEK1 exceeds the pipeline's 100-publication rejection threshold. 
The extensive literature may contain unexplored TE-relevant functions, particularly given NEK1's nuclear localization and functional roles. 
Recommend tracking NEK1 as a 'high priority rejected – exception review needed' case.
