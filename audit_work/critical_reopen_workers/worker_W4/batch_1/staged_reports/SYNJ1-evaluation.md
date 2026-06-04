# SYNJ1 – Critical False-Rejection Reevaluation Report

**Gene:** SYNJ1 (Synaptojanin-1)  
**UniProt Accession:** O43426  
**Protein Name:** Synaptojanin-1  
**Length:** 1573 aa | **Mass:** 173.1 kDa  
**Aliases:** KIAA0910  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 16 | HPA: Nucleoplasm, Cytosol (main, Approved), Centrosome (additional). HPA detects nucleoplasm at Approved reliability, which is strong. However, UniProt lists NO nuclear localization – only cytoplasm, perinuclear region. GO-CC: ZERO nuclear annotations among 10 total. All GO-CC terms are cytoplasmic/membrane: clathrin coat, presynapse, synaptic membrane, vesicle membrane, cytosol, membrane. This creates a contradiction: HPA says nucleoplasm (Approved), but UniProt and GO-CC have no nuclear annotation. Scientific literature on SYNJ1 is exclusively synaptic/neuronal. The protein is a phosphoinositide phosphatase that functions at synapses in vesicle recycling. The nuclear annotation in HPA may represent a minor pool, a cross-reacting isoform, or detection of the SAC1-like domain that may have a distinct localization. Given the unanimous non-nuclear functional evidence, the HPA finding must be treated cautiously. |
| 2. Protein Size | 10 | 2 | 1573 aa / 173.1 kDa – very large protein. Among the largest in the CRITICAL reopen set. Experimentally challenging. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 123 publications. Well-studied synaptic protein. Low novelty. |
| 4. 3D Structure | 30 | 16 | AlphaFold mean pLDDT: 67.1. Distribution: 32.4% >90, 21.6% 70-90, 10.0% 50-70, 36.0% <50. Significant disorder (36% <50) consistent with large multi-domain protein with flexible linkers. Experimental PDB: 5 structures of fragments: 1W80 (X-ray, 1.90A, short peptide), 2DNR (NMR, residues 894-971), 2VJ0 (X-ray, 1.60A, peptide), 7A0V (X-ray, 2.30A, 528-873), 7A17 (X-ray, 2.73A, 528-873). Fragments only, covering two domains (SAC1-like domain, proline-rich region). No full-length structure. |
| 5. Regulatory Domains | 50 | 14 | IPR036691 (Endonuclease/exonuclease/phosphatase superfamily), IPR046985 (Synaptojanin-1, SAC1-like domain), IPR000300 (Synaptojanin, 5-phosphatase domain), IPR012677 (Nucleotide-binding alpha-beta plait), IPR035979 (RNA-binding domain superfamily), IPR000504 (RRM domain – RNA recognition motif), IPR002013 (Synaptojanin, SAC1 domain), IPR015047 (Synaptojanin, N-terminal), IPR034971 (Synaptojanin-1-like, RRM domain). Key finding: SYNJ1 contains an RRM (RNA recognition motif) domain (IPR000504). RRM domains bind RNA and are found in many nuclear RNA-binding proteins. The presence of an RRM domain is consistent with a possible nuclear RNA-related function. However, in SYNJ1, the RRM domain has not been functionally characterized for RNA binding. The protein's established functions are: (1) phosphoinositide 5-phosphatase activity at synapses, (2) SAC1-like phosphoinositide phosphatase, (3) synaptic vesicle endocytosis and recycling. Mutations in SYNJ1 cause early-onset Parkinson's disease (PARK20). The Parkinson's disease connection is primarily synaptic, not nuclear. |
| 6. PPI Network | 50 | 24 | STRING: 15 partners. SH3GL2 (endophilin A1, 0.998, exp 0.731), AMPH (amphiphysin, 0.997, exp 0.456), BIN1 (0.994, exp 0.099), SH3GL1 (0.969, exp 0.418), ITSN1 (0.961, exp 0.475). Network is exclusively endocytic/synaptic. IntAct: 15 interactors including GRB2 (co-IP), YWHAZ (cosedimentation), multiple two-hybrid hits. GRB2 is a signaling adaptor involved in receptor tyrosine kinase signaling. ITSN1 (intersectin-1) is a nuclear/cytoplasmic protein with a known nuclear function in signal transduction and endocytosis – it shuttles between nucleus and cytoplasm. |
| **TOTAL** | **180** | **76** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm, Cytosol
- **Additional Locations:** Centrosome
- **Key Finding:** HPA detects SYNJ1 at Nucleoplasm and Cytosol (main) and Centrosome (additional) with Approved reliability. The nucleoplasm signal is strong and reproducible across cell lines and antibodies. This is technically high-quality evidence for nuclear localization.

**Interpretation note:** The HPA nucleoplasm signal is robust (Approved). However, this finding stands in isolation from all other data sources. SYNJ1 literature, UniProt annotation, and GO-CC annotations are exclusively cytoplasmic/synaptic. The discrepancy must be addressed: either (1) SYNJ1 has a minor but real nuclear pool that has been overlooked by the field, (2) the HPA antibody cross-reacts with a nuclear antigen, or (3) a specific isoform localizes to the nucleus. SYNJ1 has multiple isoforms, and the HPA antibody may detect a splice variant with distinct localization.

### UniProt Subcellular Location
- **Cytoplasm, perinuclear region** – The sole subcellular location annotated in UniProt. NO nuclear localization listed. The perinuclear region is the cytoplasm immediately surrounding the nucleus, which could explain HPA signal if the antibody detects perinuclear protein that appears to overlap with the nucleus at the resolution of IF microscopy.

### GO Cellular Component (GO-CC)
- **GO:0005737 (cytoplasm)** – Evidence: IBA:GO_Central.
- **GO:0005829 (cytosol)** – Evidence: TAS:Reactome.
- **GO:0030132 (clathrin coat of coated pit)** – Evidence: ISS:BHF-UCL.
- **GO:0016020 (membrane)** – Evidence: IBA:GO_Central.
- **GO:0098793 (presynapse)** – Evidence: IDA:ParkinsonsUK-UCL.
- **GO:0097060 (synaptic membrane)** – Evidence: ISS:BHF-UCL.
- **GO:0043195 (terminal bouton)** – Evidence: ISS:ParkinsonsUK-UCL.
- **GO:0012506 (vesicle membrane)** – Evidence: ISS:ParkinsonsUK-UCL.
- **GO:0048471 (perinuclear region of cytoplasm)** – Evidence: ISS:UniProtKB.
- **GO:0030117 (membrane coat)** – Evidence: ISS:ParkinsonsUK-UCL.

**ZERO nuclear GO-CC annotations among 10 total.**

### Functional Nuclear Context
- **RRM Domain:** SYNJ1 contains an RRM (RNA recognition motif) domain (IPR000504). RRM domains are the most common RNA-binding domain in eukaryotes and are found in many nuclear proteins (hnRNPs, splicing factors, etc.). However, the SYNJ1 RRM domain has NOT been experimentally shown to bind RNA or to have any functional significance beyond its structural role in the protein.
- **Parkinson's Disease:** SYNJ1 mutations cause autosomal recessive early-onset Parkinson's disease (PARK20). PD pathology involves alpha-synuclein aggregation and synaptic dysfunction. The nuclear connection in PD is indirect: parkin (PARK2) and PINK1 (PARK6) are mitochondrial quality control proteins that also have nuclear functions. SYNJ1's role in PD is primarily at the synapse.
- **ITSN1 Interaction:** ITSN1 (intersectin-1) is a scaffold protein with both cytoplasmic (endocytosis) and nuclear (signal transduction, transcription regulation) functions. ITSN1 shuttles to the nucleus and regulates transcription. The SYNJ1-ITSN1 interaction could potentially bring SYNJ1 to the nucleus, but this is speculative.

**Summary:** SYNJ1's nuclear evidence is contradictory. HPA shows nucleoplasm (Approved, strong), but UniProt, GO-CC, and the entire functional literature are exclusively cytoplasmic/synaptic. The protein is a synaptic phosphoinositide phosphatase with an established role in endocytosis. The RRM domain provides a plausible mechanism for nuclear RNA binding but is functionally uncharacterized. Nuclear score: 16/30 – HPA signal is strong but isolated from all other data, warranting skepticism.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 123 | `"SYNJ1"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 179 | `"SYNJ1"[Title/Abstract]` |
| Broad (All Fields) | 180 | `"SYNJ1"` |

**Alias Note:** Alias KIAA0910 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:35328025** – Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing. SYNJ1 as PARK20.
2. **PMID:20301402** – Monogenic Parkinson Disease Overview. SYNJ1 overview.
3. **PMID:31779813** – 'Atypical' Parkinson's disease – genetic forms. SYNJ1 in atypical PD.
4. **PMID:23804563** – SYNJ1 phosphoinositide phosphatase mechanism.
5. **PMID:27435092** – SYNJ1 mutations impair synaptic vesicle recycling in PD.

### Literature Assessment
- **Total publications:** Well-studied (123 strict, 180 broad). Extensive neuroscience literature.
- **Thematic focus:** Synaptic vesicle endocytosis and recycling, Parkinson's disease, phosphoinositide signaling. SYNJ1 is a central synaptic protein.
- **Key functional theme:** SYNJ1 dephosphorylates phosphoinositides at synapses, facilitating clathrin-mediated endocytosis of synaptic vesicles. It acts at the presynaptic terminal to enable sustained neurotransmission.
- **PD connection:** Loss-of-function mutations cause early-onset Parkinson's disease through defective synaptic vesicle recycling in dopaminergic neurons. This is a synaptic, not nuclear, disease mechanism.
- **No publications on nuclear function or TE regulation.**
- **Novelty score:** 4/10 (>100 publications = lower novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-O43426-F1, version 6
- **Mean pLDDT:** 67.1
- **pLDDT Distribution:**
  - >90 (very high confidence): 32.4%
  - 70-90 (confident): 21.6%
  - 50-70 (low confidence): 10.0%
  - <50 (very low confidence): 36.0%
- **Assessment:** Moderate prediction with substantial disorder (36% <50). This is expected for a large multi-domain protein with flexible linkers connecting the individual catalytic and adaptor domains.

### Experimental PDB Structures
- **1W80** – X-ray, 1.90A. Proline-rich peptide binding (short peptides, 12aa each).
- **2DNR** – NMR. SAC1-like domain (residues 894-971).
- **2VJ0** – X-ray, 1.60A. Proline-rich peptide (12aa).
- **7A0V** – X-ray, 2.30A. 5-phosphatase domain (residues 528-873).
- **7A17** – X-ray, 2.73A. 5-phosphatase domain (residues 528-873).

### Structural Assessment
- Fragment coverage for the 5-phosphatase domain (catalytic core) and SAC1-like domain. These are the key enzymatic domains. The RRM domain and proline-rich regions have not been structurally characterized.
- The fragment structures provide good mechanistic insight into phosphoinositide catalysis but do not cover the domains that could mediate nuclear function (RRM).
- **Score:** 16/30 – Good fragment structures for catalytic domains but poor overall coverage and high disorder in remaining regions.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| SH3GL2 | 0.998 | 0.731 | 0 | Endophilin A1, endocytosis |
| AMPH | 0.997 | 0.456 | 0 | Amphiphysin, endocytosis |
| BIN1 | 0.994 | 0.099 | 0 | Bridging integrator 1, endocytosis |
| SH3GL1 | 0.969 | 0.418 | 0 | Endophilin A2 |
| ITSN1 | 0.961 | 0.475 | 0 | Intersectin-1, endocytosis/signaling |
| SH3GL3 | 0.942 | 0.081 | 0.017 | Endophilin A3 |
| DNM1 | 0.939 | 0.451 | 0.008 | Dynamin-1, synaptic vesicle fission |
| CLTC | 0.909 | 0.148 | 0.227 | Clathrin heavy chain |
| PACSIN1 | 0.906 | 0.079 | 0.018 | Syndapin-1, endocytosis |

**Note:** The network is exclusively endocytic/synaptic. Experimental scores are high for SH3GL2 (0.731), AMPH (0.456), ITSN1 (0.475), and DNM1 (0.451). These represent validated physical interactions at the synapse.

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| GRB2 | anti tag co-IP | PMID:28514442 | association |
| YWHAZ | cosedimentation | PMID:NA | physical association |
| Atp6v1a | anti bait co-IP | PMID:NA | physical association |
| multiple two-hybrid hits | two hybrid | PMID:25416956, 32296183 | physical association |

### PPI Network Assessment
- **Endocytosis network:** The STRING network is one of the strongest and most coherent in the dataset. SYNJ1 interacts with the core endocytic machinery at synapses (endophilin, amphiphysin, dynamin, clathrin). These interactions are functionally validated and have clear mechanistic roles in synaptic vesicle recycling.
- **ITSN1:** Intersectin-1 is a scaffold protein with dual cytoplasmic (endocytosis) and nuclear (transcriptional regulation) functions. ITSN1 translocates to the nucleus and can activate transcription. The SYNJ1-ITSN1 interaction (exp 0.475) is primarily at the synapse for endocytosis, but ITSN1's nuclear function raises the possibility of SYNJ1 nuclear co-translocation.
- **GRB2:** Growth factor receptor-bound protein 2, a signaling adaptor. Co-IP (PMID:28514442). GRB2 functions primarily in cytoplasmic receptor tyrosine kinase signaling but can translocate to the nucleus in some contexts.
- **Score:** 24/50 – Excellent endocytic network quality but no nuclear interaction partners. ITSN1 is the only partner with known nuclear function.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SYNJ1 was likely auto-rejected because:
1. UniProt and GO-CC have ZERO nuclear annotations despite HPA nucleoplasm detection.
2. The protein is a well-characterized synaptic/cytoplasmic enzyme.
3. Very large protein (1573 aa) flagged for tractability.
4. Extensive literature with no mention of nuclear function.

### Recheck Analysis
1. **The Contradiction:** HPA says Nucleoplasm (Approved). UniProt says Cytoplasm, perinuclear region. GO-CC says ZERO nuclear annotations. The literature says synaptic. This is a genuine contradiction between data sources that demands explanation.
2. **Possible Resolutions:**
   - **HPA artifact:** The Approved reliability designation does not guarantee biological accuracy. HPA uses antibody-based IF, and even well-validated antibodies can show cross-reactivity or staining artifacts. The perinuclear cytoplasmic signal could be visually overlapping with the nucleus in IF images.
   - **Isoform-specific localization:** SYNJ1 has multiple splice isoforms (170 kDa and 145 kDa are the major forms). The HPA antibody may detect an isoform with distinct localization not captured by UniProt/GO annotations, which typically reflect the canonical isoform.
   - **Minor nuclear pool:** SYNJ1 may have a small nuclear fraction that is sufficient for HPA detection but not characterized in the literature or GO annotations.
3. **RRM Domain:** The presence of an RRM (RNA recognition motif) is intriguing and provides a structural rationale for potential nuclear RNA-binding function. However, this domain has NOT been shown to bind RNA in SYNJ1.
4. **ITSN1 Connection:** ITSN1's nuclear function provides a plausible mechanism for SYNJ1 nuclear translocation, but this remains speculative.

### Verdict on False Rejection
**The original rejection was PROBABLY CORRECT.** The overwhelming weight of evidence (UniProt, GO-CC, literature, function, PPI network) indicates SYNJ1 is a cytoplasmic/synaptic protein. The HPA nucleoplasm signal, while technically Approved, is contradicted by every other data source. The RRM domain and ITSN1 interaction create theoretical possibilities for nuclear function, but these are far weaker than the established synaptic function. Reopening would require experimental validation of nuclear localization in an independent system.

**This gene should remain rejected unless a specific nuclear isoform is identified.**

---

## TE-Regulator Relevance Reasoning

1. **Contradictory Nuclear Evidence:** HPA shows nucleoplasm (Approved) but this is contradicted by all other data. The weight of evidence favors cytoplasmic/synaptic localization. TE regulation cannot be proposed for a protein whose nuclear localization is uncertain.

2. **Primary Function Is Synaptic:** SYNJ1 is a synaptic phosphoinositide phosphatase essential for vesicle endocytosis. This function is purely cytoplasmic and has no connection to nuclear biology or TE regulation.

3. **RRM Domain – Untested:** The RRM domain provides a theoretical RNA-binding capability, but RRM domains also have non-RNA-binding functions (protein-protein interaction, structural scaffolding). No experimental evidence demonstrates RNA binding by SYNJ1's RRM domain.

4. **Parkinson's Disease Connection:** PD is a neurodegenerative disorder with synaptic pathology. The nuclear dimension of PD (if any) involves parkin, PINK1, and alpha-synuclein, not SYNJ1. There is no known connection between SYNJ1 and TE biology in PD or any other context.

5. **Size and Tractability:** At 1573 aa (173 kDa), SYNJ1 is very large and difficult to study experimentally. Even if nuclear function were confirmed, the protein would be challenging to manipulate.

**Assessment:** SYNJ1 is a VERY LOW interest candidate for TE regulation. The nuclear localization is contradicted by the preponderance of evidence. The established synaptic function has no connection to TE biology. The protein should not be reopened.

---

## Final Decision

**DECISION: REJECTION CONFIRMED – nuclear localization contradicted by evidence preponderance**

**Reasoning:** Despite HPA detecting nucleoplasm at Approved reliability, the unanimous evidence from UniProt (no nuclear), GO-CC (zero nuclear annotations), published literature (exclusively synaptic), and PPI network (entirely endocytic) argues that SYNJ1 is a cytoplasmic/synaptic protein. The HPA finding is most likely explained by perinuclear cytoplasmic signal overlapping with the nucleus in IF images, or isoform-specific detection. The RRM domain and ITSN1 interaction create theoretical nuclear possibilities but do not override the established synaptic function. SYNJ1 has no credible connection to TE biology.

**Score: 76/180** – The score is inflated by the HPA nuclear signal. A more realistic nuclear score based on evidence preponderance would be much lower.

**Flag for deletion** – SYNJ1 should not be reopened. The protein is correctly rejected.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: REJECTION CONFIRMED – HPA signal contradicted by all other data*

SYNJ1 presents the most significant data-source contradiction in the W4 batch. HPA (Approved) says nucleoplasm; everything else says cytoplasm/synapse. In such cases, the preponderance of evidence should prevail. SYNJ1 has been studied extensively (123 publications) as a synaptic protein, and if there were a genuine nuclear function, someone would have reported it by now. The perinuclear region annotation in UniProt is telling: the protein localizes to cytoplasm near the nucleus, which can produce a pseudo-nuclear signal in IF. The RRM domain is interesting but untested. This is a case where the automated screening was correct to reject despite the HPA flag, because the functional context is overwhelmingly non-nuclear. SYNJ1 is an excellent synaptic protein and should be left to neuroscientists. For TE regulation, it offers nothing.
