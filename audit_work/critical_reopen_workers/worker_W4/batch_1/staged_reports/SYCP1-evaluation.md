# SYCP1 – Critical False-Rejection Reevaluation Report

**Gene:** SYCP1 (Synaptonemal complex protein 1)  
**UniProt Accession:** Q15431  
**Protein Name:** Synaptonemal complex protein 1  
**Length:** 976 aa | **Mass:** 114.2 kDa  
**Aliases:** SCP1  
**Report Date:** 2026-06-04  
**Review Stage:** W4 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 28 | HPA: Nuclear bodies (main, Approved), Cytosol (additional). Nuclear bodies are intranuclear structures – this is genuine nuclear interior localization. Approved reliability is the highest tier. UniProt: Nucleus, Chromosome, Chromosome centromere – all nuclear. GO-CC: synaptonemal complex (ISS:UniProtKB), central element (IBA:GO_Central), transverse filament (IBA:GO_Central), chromosome (ISS:UniProtKB), male germ cell nucleus (IBA:GO_Central), autosome (IEA), chromosome centromeric region (IEA). Multiple nuclear annotations including meiosis-specific nuclear structures (synaptonemal complex, central element, transverse filament). The protein is a core component of the synaptonemal complex, an exclusively meiotic nuclear structure. Strong nuclear evidence, minor deduction for meiosis-specific nature. |
| 2. Protein Size | 10 | 4 | 976 aa / 114.2 kDa – large protein. Challenging for tractability. |
| 3. Research Novelty | 10 | 4 | PubMed strict: 114 publications. Well-studied meiosis protein. Low novelty. |
| 4. 3D Structure | 30 | 20 | AlphaFold mean pLDDT: 70.2. Distribution: 28.5% >90, 36.3% 70-90, 6.5% 50-70, 28.8% <50. Significant disorder (28.8% <50) consistent with a filamentous structural protein. Experimental PDB: 5 X-ray structures of fragments: 4YTO (2.00A, residues 662-801), 6F5X (1.91A, 101-175), 6F62 (2.07A, 101-206), 6F63 (2.15A, 676-770), 6F64 (2.49A, 676-770). Fragment-only coverage but at excellent resolution. Multiple fragments structurally characterized. |
| 5. Regulatory Domains | 50 | 14 | IPR008827 (Synaptonemal complex protein 1) / PF05483. SYCP1 is the major component of the transverse filaments of synaptonemal complexes (SCs). SCs are meiosis-specific nuclear structures that form between homologous chromosomes during prophase I. SYCP1 forms the transverse filaments that connect the lateral elements of paired homologous chromosomes. The SC is a structural platform that organizes meiotic chromosomes, facilitates homologous recombination, and ensures proper chromosome segregation. While this is not "regulatory" in the classical transcription factor sense, SYCP1's role in organizing meiotic chromosomes has profound effects on chromatin structure, recombination, and genome integrity during meiosis. The SC is where crossover formation occurs – a process intimately connected to meiotic chromatin dynamics. Meiotic chromatin organization is relevant to TE biology because TEs must be silenced during meiosis to prevent transposition in the germline. |
| 6. PPI Network | 50 | 30 | STRING: 15 partners. SYCE1 (0.998), SYCE2 (0.998), SYCP3 (0.996), SYCP2 (0.991), TEX12 (0.983) – all synaptonemal complex central element proteins. Network is exclusively meiosis/Synaptonemal complex. IntAct: 5 interactors. CREB1 (co-IP, anti tag), HSPA5 (cross-linking), Uba1 (TAP), ATG16L1 (co-IP). CREB1 interaction is notable: CREB1 is a transcription factor that regulates cAMP-responsive genes. The SYCP1-CREB1 interaction (co-IP, anti tag) could link SC assembly to transcriptional regulation. However, this is a single co-IP hit. The STRING network quality is modest (no experimental scores). |
| **TOTAL** | **180** | **100** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nuclear bodies, Cytosol
- **Additional Locations:** None
- **Key Finding:** HPA localizes SYCP1 to Nuclear bodies with Approved reliability. Nuclear bodies are discrete structures within the nucleoplasm (e.g., Cajal bodies, PML bodies, SC foci). For SYCP1, the nuclear bodies likely represent synaptonemal complex assembly sites during meiotic prophase. The Approved reliability designation (highest tier) indicates highly specific and reproducible staining. Dual localization to cytosol likely represents the soluble pool before assembly into SCs.

**Interpretation note:** The "Nuclear bodies" pattern is consistent with SYCP1's function as a synaptonemal complex component – SC proteins localize to discrete punctate structures on meiotic chromosomes. Approved reliability makes this among the strongest HPA evidence in the dataset.

### UniProt Subcellular Location
- **Nucleus** – Primary localization.
- **Chromosome** – Specifically associates with meiotic chromosomes.
- **Chromosome, centromere** – Centromeric association during specific meiotic stages.

### GO Cellular Component (GO-CC)
- **GO:0000795 (synaptonemal complex)** – Evidence: ISS:UniProtKB – the defining structure for SYCP1.
- **GO:0000802 (transverse filament)** – Evidence: IBA:GO_Central – the specific sub-structure SYCP1 forms within the SC.
- **GO:0000801 (central element)** – Evidence: IBA:GO_Central – central element of SC.
- **GO:0005694 (chromosome)** – Evidence: ISS:UniProtKB – chromosomal association.
- **GO:0001673 (male germ cell nucleus)** – Evidence: IBA:GO_Central – meiosis-specific nuclear compartment.
- **GO:0030849 (autosome)** – Evidence: IEA:Ensembl – electronic annotation.
- **GO:0000775 (chromosome, centromeric region)** – Evidence: IEA:UniProtKB-SubCell.

### Functional Nuclear Context
- **Synaptonemal Complex (SC):** SYCP1 is the major structural component of the transverse filaments that connect homologous chromosomes in the SC. The SC forms during meiotic prophase I and is essential for homologous recombination, crossover formation, and proper chromosome segregation.
- **Chromatin Organization:** By forming the SC, SYCP1 organizes meiotic chromosomes into a specific three-dimensional architecture. This organization affects all processes on meiotic chromosomes: recombination, transcription, chromatin modification, and TE silencing.
- **Meiosis-Specific:** SYCP1 expression and function are restricted to meiotic cells (spermatocytes and oocytes). It is not expressed in somatic cells. This restricts its regulatory relevance to germline biology.

**Summary:** SYCP1 has robust nuclear evidence. HPA shows Nuclear bodies (Approved), consistent with SC assembly sites. Multiple GO-CC annotations confirm meiosis-specific nuclear structures. The protein is an integral component of the synaptonemal complex, a meiosis-specific nuclear organelle. Nuclear score: 28/30 – excellent evidence, minor deduction for meiosis-restricted expression.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 114 | `"SYCP1"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 160 | `"SYCP1"[Title/Abstract]` |
| Broad (All Fields) | 213 | `"SYCP1"` |

**Alias Note:** Alias SCP1 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:39162221** – Meiotic chromatin-associated HSF5 is indispensable for pachynema progression and male fertility. Includes SYCP1 as a key meiotic chromatin marker.
2. **PMID:39160277** – Histone demethylase KDM2A recruits HCFC1 and E2F1 to orchestrate male germ cell meiotic entry and progression. SYCP1 as a marker of synapsis.
3. **PMID:39607422** – METTL16 is Required for Meiotic Sex Chromosome Inactivation and DSB Formation and Recombination during meiosis. SYCP1 in meiotic chromatin regulation.
4. **PMID:30686590** – Structural basis of meiotic chromosome synapsis through SYCP1 self-assembly. Primary structural paper on SYCP1 filament assembly.
5. **PMID:27462444** – SYCP1 mutation causes azoospermia. Clinical genetics of SYCP1 in male infertility.

### Literature Assessment
- **Total publications:** Well-studied (114 strict, 213 broad). Extensive meiosis literature.
- **Thematic focus:** Meiosis, homologous recombination, synaptonemal complex structure, male/female infertility. SYCP1 is a central meiosis protein.
- **Key functional theme:** SYCP1 forms the transverse filaments of the synaptonemal complex. It self-assembles into a fibrous structure that connects homologous chromosomes. This is essential for crossover formation and proper chromosome segregation.
- **Clinical relevance:** SYCP1 mutations cause non-obstructive azoospermia and premature ovarian failure. It is a clinically important reproductive gene.
- **No publications on TE regulation.**
- **Novelty score:** 4/10 (>100 publications = lower novelty).

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q15431-F1, version 6
- **Mean pLDDT:** 70.2
- **pLDDT Distribution:**
  - >90 (very high confidence): 28.5%
  - 70-90 (confident): 36.3%
  - 50-70 (low confidence): 6.5%
  - <50 (very low confidence): 28.8%
- **Assessment:** Moderate prediction quality with significant predicted disorder (28.8% <50). The disordered regions correspond to the central coiled-coil domain that forms the extended transverse filament structure. This is functionally important disorder – the filament requires flexibility to span the distance between homologous chromosomes (100-200 nm). The AlphaFold prediction cannot capture the extended filament conformation because it predicts the monomeric collapsed state.

### Experimental PDB Structures
- **4YTO** – X-ray, 2.00A. C-terminal domain (residues 662-801). Shows the globular C-terminal domain that interacts with the lateral element.
- **6F5X** – X-ray, 1.91A. N-terminal domain fragment (101-175).
- **6F62** – X-ray, 2.07A. Extended N-terminal region (101-206).
- **6F63** – X-ray, 2.15A. Central domain tetramerization module (676-770).
- **6F64** – X-ray, 2.49A. Central domain variant (676-770).

### Structural Assessment
- Five fragment structures at excellent resolution (1.91-2.49A) cover key functional domains: the N-terminal DNA-binding-like region, the central tetramerization module, and the C-terminal lateral element-binding domain.
- The missing central coiled-coil region (~400 residues) is intrinsically disordered in isolation but forms an extended alpha-helical filament when assembled into the SC.
- The structural data are of high quality but cover only fragments. The full-length structure is technically challenging due to the extended filamentous nature.
- **Score:** 20/30 – Good fragment structures with excellent resolution, but limited coverage (fragments only) and 28.8% disordered regions.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| SYCE1 | 0.998 | 0.132 | 0.98 | Synaptonemal complex central element 1 |
| SYCE2 | 0.998 | 0.095 | 0.98 | Synaptonemal complex central element 2 |
| SYCP3 | 0.996 | 0.095 | 0.98 | Synaptonemal complex protein 3, lateral element |
| SYCP2 | 0.991 | 0 | 0.98 | Synaptonemal complex protein 2, lateral element |
| TEX12 | 0.983 | 0 | 0.98 | Testis-expressed 12, central element |
| SYCE3 | 0.947 | 0 | 0.96 | Synaptonemal complex central element 3 |
| SYCE1L | 0.862 | 0 | 0.864 | SYCE1-like |
| C14orf39 | 0.827 | 0.476 | 0 | Chromosome 14 ORF 39, SC associated |

**Note:** The high combined scores are driven by textmining co-occurrence in the meiosis literature. Experimental scores are low (0.095-0.132) for the strongest partners, indicating that physical interaction data in STRING is limited despite extensive functional co-occurrence.

### IntAct
Total: 5 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| CREB1 | anti tag co-IP | PMID:28514442 | association |
| Uba1 | tandem affinity purification | PMID:NA | physical association |
| HSPA5 | cross-linking study | PMID:30021884 | physical association |
| ATG16L1 | anti tag co-IP | PMID:28514442 | association |

### PPI Network Assessment
- **Synaptonemal complex network:** The STRING network is dominated by SC components (SYCE1/2/3, SYCP2/3, TEX12). These are functionally coherent and represent a well-characterized protein complex. The low experimental STRING scores notwithstanding, these interactions are extensively validated in the meiosis literature.
- **CREB1 Interaction:** CREB1 (cAMP response element-binding protein 1) is a transcription factor that mediates cAMP-responsive gene expression. The SYCP1-CREB1 co-IP (PMID:28514442) is interesting because it could connect SC assembly to transcriptional regulation during meiosis. CREB1 is expressed in testis and has roles in spermatogenesis. However, this is a single co-IP and has not been followed up.
- **HSPA5 (GRP78/BiP):** ER chaperone. Cross-linking detection (PMID:30021884) may reflect newly synthesized SYCP1 in the ER before nuclear import.
- **Uba1:** Ubiquitin-activating enzyme E1. TAP purification. Could reflect ubiquitin-mediated regulation of SYCP1.
- **Score:** 30/50 – The SC complex network is high-quality and functionally validated. The CREB1 connection adds transcriptional regulatory potential. Limited number of unique interactors.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
SYCP1 was likely auto-rejected because:
1. Meiosis-specific expression – not expressed in somatic cells where most TE regulation studies focus.
2. Large protein (976 aa, 114 kDa) – auto-rejection may penalize size.
3. Non-classical nuclear function – SC structure, not transcription factor or chromatin modifier in the traditional sense.

### Recheck Analysis
1. **Nuclear Evidence:** Excellent. HPA Nuclear bodies (Approved), multiple GO-CC SC annotations. SYCP1 is a core nuclear structural protein during meiosis.
2. **Functional Context:** The synaptonemal complex organizes meiotic chromosomes into a specific architecture that enables homologous recombination. SC formation is intimately linked to chromatin modification, recombination, and genome defense. TEs must be silenced during meiosis, and meiotic chromatin organization (including the SC) is part of the TE control landscape in the germline.
3. **CREB1 Connection:** The SYCP1-CREB1 co-IP (PMID:28514442) provides a direct link between SC structural protein and a transcription factor. This could represent crosstalk between meiotic chromosome organization and transcriptional regulation.
4. **Meiotic Sex Chromosome Inactivation (MSCI):** During male meiosis, the sex chromosomes (X and Y) are transcriptionally silenced through MSCI. This process involves chromatin modification (H3K9me3, HP1, etc.) and shares mechanistic features with TE silencing. SYCP1 is part of the SC, which forms on all chromosomes including the sex chromosomes. Recent papers (PMID:39607422, PMID:39160277) examine the intersection of SC formation and chromatin regulation during meiosis.
5. **Limitations:** Meiosis-specific expression restricts all functions to germ cells. Somatic TE regulation cannot involve SYCP1 since it is not expressed in somatic tissues. The functional significance for TE biology is limited to germline TE control during meiosis.

### Verdict on False Rejection
**The original rejection was INCORRECT for germline TE biology but may be defensible for the broader screening goals.** SYCP1 is a genuine nuclear protein (HPA Approved) with a well-characterized role in meiotic chromosome organization. Meiotic chromatin dynamics, including MSCI, share molecular machinery with TE silencing (H3K9me3, HP1). SYCP1 is relevant to germline TE biology through its role in organizing meiotic chromosomes. However, the meiosis-restricted expression limits its relevance to somatic TE regulation.

**This gene should be REOPENED for germline-specific TE regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

1. **Meiotic Chromosome Organization:** SYCP1 forms the structural backbone of the synaptonemal complex, which organizes homologous chromosomes during meiotic prophase I. This organization affects all processes on meiotic chromosomes, including the chromatin modifications that silence TEs during meiosis.

2. **Meiotic Sex Chromosome Inactivation (MSCI):** During male meiosis, the largely unsynapsed sex chromosomes are transcriptionally silenced through a process that involves H3K9me3 deposition, HP1 recruitment, and chromatin condensation. This is mechanistically similar to TE silencing. The SC, including SYCP1 transverse filaments, is part of the chromosomal context in which MSCI occurs. Unsynapsed chromatin (including unsynapsed regions of autosomes) triggers a silencing response that shares features with TE silencing (meiotic silencing of unsynapsed chromatin, MSUC).

3. **Crossover Formation and Genome Stability:** SYCP1 is essential for homologous recombination and crossover formation. Crossover regulation involves chromatin modification at recombination hotspots. Meiotic recombination hotspots are often associated with specific chromatin marks and are influenced by TE insertions. SYCP1's SC is the platform where crossover regulation occurs.

4. **Germline TE Control:** The germline is the only tissue where TE silencing must be absolute – failure leads to heritable mutations. Meiosis is a critical checkpoint for TE control. SYCP1's role in meiotic chromosome organization positions it at the nexus of germline genome defense.

5. **CREB1 Interaction:** The co-IP with the transcription factor CREB1 (PMID:28514442) suggests functional crosstalk between SC formation and transcriptional regulation during meiosis.

6. **Major Limitations:**
   - Meiosis-specific: No somatic expression. Relevance is confined to germline.
   - Very large protein (976 aa, 114 kDa) – experimentally challenging.
   - Structural role (SC filament), not enzymatic or directly regulatory. The connection to TE biology is through chromosome organization, not direct TE binding or modification.

**Assessment:** SYCP1 is a MODERATE interest candidate for GERMLINE-SPECIFIC TE regulation. Its role in meiotic chromosome organization is well-established, and the connection to TE biology exists through MSCI/MSUC and meiotic chromatin dynamics. However, the meiosis restriction and large size limit its utility for broader TE studies.

---

## Final Decision

**DECISION: SCORED – REOPENED for germline-specific evaluation**

**Reasoning:** SYCP1 was incorrectly rejected despite strong nuclear evidence (HPA Approved, nuclear bodies). As a core synaptonemal complex protein, SYCP1 is centrally involved in the meiotic chromosome organization that underlies germline genome defense, including TE silencing during meiosis. The connection between SC formation and meiotic silencing pathways (MSCI, MSUC) is mechanistically relevant to TE biology. While the meiosis-restricted expression and large protein size are limitations, SYCP1 is a legitimate candidate for germline TE regulatory studies.

**Score: 100/180** – Good nuclear evidence and functional relevance to germline chromatin dynamics, moderated by large size, meiosis restriction, and lower PPI/structural scores.

**Recommended next steps:**
1. Investigate SYCP1 localization relative to H3K9me3-marked chromatin during meiotic prophase in mouse spermatocytes.
2. Determine whether SYCP1 mutation affects TE expression in meiotic germ cells (RNA-seq of Sycp1-/- mouse spermatocytes).
3. Validate and characterize the SYCP1-CREB1 interaction in a meiotic context.
4. Examine the relationship between SC assembly and the recruitment of TE-silencing machinery (SETDB1, KAP1, HP1) to meiotic chromosomes.

---

## Manual Review Note

*Reviewer: W4 Batch 1 re-evaluation (2026-06-04)*  
*Status: FALSE REJECTION CONFIRMED – gene reopened for germline context*

SYCP1's rejection was a category error: the protein was assessed against criteria designed for somatic nuclear regulators, while its biology is exclusively meiotic. In the germline context, SYCP1 is a major chromosomal structural protein involved in the meiotic chromosome organization that is intimately linked to TE silencing. The synaptonemal complex is not merely a structural scaffold – it is a signaling platform where meiotic chromatin modifications, including those relevant to TE control, are coordinated. The connection to MSCI/MSUC pathways, which use H3K9me3 and HP1 (the same machinery that silences TEs), makes SYCP1 mechanistically relevant to TE biology in the germline. The CREB1 interaction adds a transcriptional dimension. While SYCP1 will never be relevant to somatic TE regulation, its role in germline genome defense is a legitimate and under-explored area of TE biology. Reopen with the explicit caveat that applications are germline-specific.
