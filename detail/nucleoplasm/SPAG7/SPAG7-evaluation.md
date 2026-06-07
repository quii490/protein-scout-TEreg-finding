# SPAG7 – Critical False-Rejection Reevaluation Report

**Gene:** SPAG7 (Sperm-associated antigen 7)  
**UniProt Accession:** O75391  
**Protein Name:** Sperm-associated antigen 7  
**Length:** 227 aa | **Mass:** 26.0 kDa  
**Aliases:** None  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 20 | HPA: Nucleoplasm (main, Supported) – single location, nuclear-dominant IF pattern. UniProt: Nucleus (no evidence code for the main annotation – the subcellular field has only the location string without attached evidence). GO-CC: nucleus (GO:0005634, IEA:UniProtKB-SubCell) – electronic annotation only, NO experimental GO evidence. Critical problem: the sole GO-CC annotation is IEA-level. UniProt provides no experimental evidence code for nuclear localization. HPA is the only experimental source showing nuclear localization (Supported reliability). The evidence is thin – one HPA Supported detection with no corroborating experimental GO annotations. |
| 2. Protein Size | 10 | 8 | 227 aa / 26.0 kDa – small, slightly above 200 aa for full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 10 publications. Very poorly studied. Maximum novelty. |
| 4. 3D Structure | 30 | 20 | AlphaFold mean pLDDT: 85.5. Distribution: 46.7% >90, 40.5% 70-90, 11.9% 50-70, 0.9% <50. Good quality prediction with minimal disorder. Experimental PDB: 2CPM (NMR, residues 44-124, covering the R3H domain only). Partial experimental coverage. No full-length structure. |
| 5. Regulatory Domains | 50 | 18 | IPR001374 (R3H domain), IPR036867 (R3H-like superfamily), IPR034068 (SPAG7, R3H domain-containing), IPR017330 (SPAG7 family). The R3H domain is a putative single-stranded nucleic acid binding domain found in proteins involved in various aspects of RNA metabolism, transcription regulation, and DNA repair. SPAG7 is a poorly characterized member. No published functional studies specifically demonstrating nucleic acid binding or regulatory activity. The R3H domain is typically found in proteins like RNHI (ribonuclease inhibitor) and transcription factors, but SPAG7's specific function is unknown. |
| 6. PPI Network | 50 | 18 | STRING: 9 partners with NO experimental evidence (all scores from textmining/database). FAM220A (0.952, textmining only), CD34 (0.495), RPAP3 (0.467). IntAct: 15 interactors including LMNA (lamin A/C, proximity labeling, PMID:29568061), H3C1 (histone, proximity labeling), RAN (cross-linking, PMID:30021884), ABHD16A (two-hybrid), SLC25A32 (co-IP). LMNA (nuclear lamina) and RAN (nuclear transport GTPase) interactions are nuclear-relevant. Proximity labeling (BioID) for LMNA indicates SPAG7 is near the nuclear lamina – consistent with nucleoplasm localization. The RAN cross-linking interaction also supports nuclear presence. However, the STRING network is very sparse (only 9 partners) and lacks any experimental confidence scores. |
| **TOTAL** | **180** | **94** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional Locations:** None
- **Key Finding:** HPA localizes SPAG7 exclusively to Nucleoplasm with Supported reliability. The single-location pattern (no additional compartments) suggests a primarily nuclear protein.

**Interpretation note:** HPA shows clean nucleoplasm-only localization with Supported reliability. This is the strongest piece of nuclear evidence for SPAG7, as the GO annotations are entirely electronic (IEA).

### UniProt Subcellular Location
- **Nucleus** – Listed without attached evidence code in the subcellular field. The main function/annotation page lists this as a simple subcellular location. The evidence annotation for this entry is underdeveloped compared to well-characterized proteins.

### GO Cellular Component (GO-CC)
- **GO:0005634 (nucleus)** – Evidence: IEA:UniProtKB-SubCell – Electronic annotation only. This is automatically assigned based on the UniProt subcellular location field.
- **CRITICAL NOTE:** Only ONE GO-CC annotation total. No IDA, IMP, ISS, or IBA-level evidence. This is a severely under-annotated protein.

### Functional Nuclear Context
- No publications directly address SPAG7's subcellular localization experimentally beyond what is captured in HPA.
- The R3H domain is commonly found in nuclear proteins involved in RNA metabolism and transcription. However, domain-only inference is not direct evidence.
- PMID:39056292 reports that SPAG7 deletion causes intrauterine growth restriction, suggesting a developmental role, but does not characterize the molecular mechanism.
- PMID:37304876 shows SPAG7 expression changes in Caco-2 cells upon LPS and poly(I:C) stimulation – potentially linking SPAG7 to innate immune signaling, which has nuclear NF-kB and IRF components.

**Summary:** SPAG7 has modest nuclear evidence. HPA (Supported) shows nucleoplasm-only localization. UniProt lists nucleus but without experimental evidence code. GO-CC is entirely electronic (IEA). The R3H domain suggests nucleic acid binding potential but this has not been experimentally demonstrated. Nuclear score: 20/30 – HPA evidence is solid but the lack of experimental GO annotations and functional characterization is a significant gap.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 10 | `"SPAG7"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 12 | `"SPAG7"[Title/Abstract]` |
| Broad (All Fields) | 12 | `"SPAG7"` |

**Alias Note:** No aliases reported for scoring.

### Key Papers (with PMIDs)
1. **PMID:39056292** – SPAG7 deletion causes intrauterine growth restriction, resulting in adulthood obesity and metabolic syndrome. Primary genetic study linking SPAG7 to developmental phenotypes.
2. **PMID:37304876** – Alterations in gene expressions of Caco-2 cell responses to LPS and poly(I:C) stimulation. SPAG7 identified among differentially expressed genes in innate immune activation.
3. **PMID:24452265** – SPAG7 is a candidate gene for the periodic fever, aphthous stomatitis, pharyngitis and adenopathy (PFAPA) syndrome. Genetic association study.
4. **PMID:36121331** – SPAG7 expression in the context of male infertility. Links SPAG7 to spermatogenesis (consistent with gene name "sperm-associated antigen 7").
5. **PMID:17974005** – Early characterization of the SPAG7 gene family in the context of sperm biology and testis expression.

### Literature Assessment
- **Total publications:** Very low (10 strict). SPAG7 is very poorly studied.
- **Thematic focus:** Sparse literature covering developmental biology (IUGR), inflammation (PFAPA, LPS response), and male reproduction. No unified functional theme emerges.
- **Critical gap:** No mechanistic studies. No protein interaction characterization beyond high-throughput datasets. No structural biology beyond the partial NMR domain structure. No functional assays demonstrating what SPAG7 actually does.
- **No publications on TE regulation.**
- **Novelty score:** 10/10 (≤20 publications).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-O75391-F1, version 6
- **Mean pLDDT:** 85.5
- **pLDDT Distribution:**
  - >90 (very high confidence): 46.7%
  - 70-90 (confident): 40.5%
  - 50-70 (low confidence): 11.9%
  - <50 (very low confidence): 0.9%
- **Assessment:** Good quality prediction. Nearly half the protein is very high confidence, and the combined >70 fraction is 87.2%. Minimal disorder (0.9% <50). The structure is largely well-folded with a small flexible C-terminal tail.

### Experimental PDB Structures
- **2CPM** – NMR, residues 44-124. Covers the R3H domain only. The structure confirms the R3H fold but provides no information on the N-terminal 43 residues or C-terminal 103 residues.

### Structural Assessment
- The R3H domain structure is experimentally validated by NMR (2CPM). The AlphaFold prediction extends this to the full-length protein with good confidence.
- The R3H domain (residues 44-124) is a putative ssDNA/ssRNA binding domain. The structure does not confirm nucleic acid binding activity, which would require experimental demonstration.
- **Score:** 20/30 – Good prediction quality and partial experimental structure, but the functional implications of the R3H domain remain untested.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| FAM220A | 0.952 | 0 | 0.952 | STAT3 inhibitor, transcriptional regulator |
| CD34 | 0.495 | 0 | 0.495 | Hematopoietic stem cell marker |
| RPAP3 | 0.467 | 0 | 0.467 | RNA polymerase II-associated protein |
| SMIM7 | 0.455 | 0 | 0.455 | Small integral membrane protein |
| M0QYU9_HUMAN | 0.447 | 0 | 0.447 | Uncharacterized |
| RNF32 | 0.441 | 0 | 0.441 | RING finger protein |

**Critical note:** None of the STRING partners have ANY experimental confidence scores. All scores derive from textmining, co-occurrence, or database associations. The network quality is very low.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| LMNA | proximity-dependent biotin identification | PMID:29568061 | physical association |
| H3C1 | proximity-dependent biotin identification | PMID:29568061 | physical association |
| RAN | cross-linking study | PMID:30021884 | physical association |
| SLC25A32 | anti tag co-IP | PMID:28514442 | association |
| ABHD16A | two hybrid | PMID:25416956 | physical association |

### PPI Network Assessment
- **LMNA (Lamin A/C) interaction:** Detected by proximity-dependent biotin identification (BioID, PMID:29568061). BioID proximity labeling has a labeling radius of ~10nm, so LMNA proximity means SPAG7 is within ~10nm of the nuclear lamina. This is strong evidence supporting nuclear/nucleoplasmic localization. LMNA is a key component of the nuclear lamina and is involved in chromatin organization.
- **H3C1 (Histone H3.1):** Also from BioID (PMID:29568061), indicating proximity to chromatin.
- **RAN:** Nuclear transport GTPase, cross-linking detection (PMID:30021884). Consistent with nuclear presence.
- **Network quality:** The STRING network is extremely sparse (9 partners) and relies entirely on non-experimental evidence. IntAct provides better evidence through BioID, which specifically interrogates the nuclear compartmental proteome.
- **SPAG7 appears to be a nuclear protein based on interactor context** (LMNA, H3.1, RAN), but the interaction data is from high-throughput proximity labeling and cross-linking studies, not from targeted biochemical validation.
- **Score:** 18/50 – The BioID evidence for nuclear proximity (LMNA, H3C1) is the strongest argument for nuclear localization, but the overall PPI network is very small and lacks experimental depth.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SPAG7 was likely auto-rejected because:
1. GO-CC annotations are entirely electronic (IEA) – no experimental nuclear evidence in GO.
2. UniProt provides no experimental evidence code for nuclear localization.
3. Very sparse STRING network with no experimental interactions.
4. The gene name "sperm-associated antigen 7" might suggest testis/cytoplasmic function.

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm (main, Supported) – solid experimental evidence from immunofluorescence. The single-compartment pattern (nucleoplasm only) strengthens the case for nuclear localization.
2. **BioID Evidence:** The proximity labeling detection of LMNA and H3C1 (PMID:29568061) places SPAG7 in the nuclear compartment, proximal to the nuclear lamina and chromatin. BioID is an orthogonal method to HPA IF and confirms nuclear localization.
3. **R3H Domain:** The R3H domain is a nucleic acid binding domain found in proteins involved in RNA metabolism and transcription. Domain annotation alone does not prove function, but it provides a plausible molecular mechanism consistent with nuclear localization.
4. **Literature:** Extremely sparse (10 publications). No mechanistic studies. No functional characterization. The R3H domain's nucleic acid binding activity has not been experimentally tested for SPAG7.
5. **Problem:** Despite nuclear localization evidence (HPA + BioID), there is essentially no functional characterization of SPAG7. We know it is in the nucleus, but we don't know what it does there.

### Verdict on False Rejection
**BORDERLINE – the rejection was partially false.** SPAG7 does have nuclear localization evidence from HPA (Supported, nucleoplasm-only) and BioID proximity labeling (LMNA, H3C1). However, the complete absence of functional characterization (10 publications, no mechanistic studies) means we cannot assess whether the nuclear function is relevant to TE regulation. The R3H domain suggests nucleic acid binding potential, but this is entirely untested.

**This gene could be reopened at reviewer discretion but is a weak candidate due to functional ignorance.**

---

## TE-Regulator Relevance Reasoning

1. **Nuclear Localization:** HPA shows nucleoplasm-only with Supported reliability. BioID proximity to LMNA and H3C1 confirms nuclear compartment. The localization evidence is sufficient to consider nuclear functions.

2. **R3H Domain:** The R3H domain (residues 44-124) is structurally characterized by NMR (2CPM) and is predicted to bind single-stranded nucleic acids. In other proteins, R3H domains are involved in RNA metabolism, transcription regulation, and DNA repair. However, SPAG7's R3H domain has NOT been experimentally shown to bind nucleic acids.

3. **Developmental Role:** SPAG7 deletion causes intrauterine growth restriction (PMID:39056292), suggesting a role in early development. IUGR can involve epigenetic dysregulation, but the molecular mechanism is unknown.

4. **Innate Immunity Links:** SPAG7 expression changes in Caco-2 cells upon LPS and poly(I:C) stimulation (PMID:37304876). Innate immune signaling involves nuclear NF-kB and IRF transcription factors. SPAG7 was also nominated as a PFAPA candidate gene (PMID:24452265). The link to inflammatory signaling could involve nuclear regulatory functions.

5. **Major Gaps:**
   - No functional studies. We do not know what SPAG7 does.
   - No nucleic acid binding demonstrated for the R3H domain.
   - No target genes or pathways identified.
   - No connection to TE biology whatsoever.
   - The literature is too sparse to infer function from context.

**Assessment:** SPAG7 is a VERY LOW interest candidate for TE regulation due to functional ignorance, NOT due to lack of nuclear evidence. It is a nuclear protein (HPA + BioID) with a nucleic acid binding domain that might be regulatory, but there is no experimental data to support any specific nuclear function. It would be a purely speculative candidate.

---

## Final Decision

**DECISION: BORDERLINE – can be reopened but is a weak speculative candidate**

**Reasoning:** SPAG7 has adequate nuclear localization evidence (HPA Supported nucleoplasm + BioID LMNA/H3C1 proximity) to clear the nuclear gate. However, it fails spectacularly on functional characterization: 10 publications, no mechanistic studies, no demonstrated function. The R3H domain is a tantalizing clue but completely untested. Reopening would place SPAG7 in the low-mid priority tier of candidates that need significant downstream investigation before any TE-relevant hypothesis can be formulated.

**Score: 94/180** – The score reflects the nuclear evidence and structural quality balanced against functional ignorance and weak PPI network.

**Recommended next steps (if reopened):**
1. Experimentally test R3H domain nucleic acid binding (EMSA, FP, SPR).
2. RNA-seq/ChIP-seq to identify target genes/genomic binding sites if nucleic acid binding is confirmed.
3. Investigate SPAG7's role in LPS/poly(I:C) inflammatory signaling pathways.
4. Characterize the interaction with LMNA and nuclear lamina.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: BORDERLINE – nuclear localization confirmed, functional ignorance limits assessment*

SPAG7 is a protein that exists – it localizes to the nucleoplasm, has a potentially interesting R3H nucleic acid binding domain, and shows up in proximity to the nuclear lamina. That is the sum total of what is known about it. The extreme sparsity of the literature (10 publications, none mechanistic) makes it impossible to assess TE-regulatory potential. This is the kind of protein where a "yes" or "no" decision depends on whether the project has bandwidth for speculative candidates that would require extensive characterization before any hypothesis can be tested. The nuclear localization is sufficient to justify studying it, but the functional ignorance is sufficient to justify rejecting it. Reviewer judgment needed.

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75391 |
| SMART | SM00393; |
| UniProt Domain [FT] | DOMAIN 46..109; /note="R3H"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00382" |
| InterPro | IPR001374;IPR036867;IPR034068;IPR017330; |
| Pfam | PF01424; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000091640-SPAG7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| H2BC8 | Biogrid | false |
| LXN | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
