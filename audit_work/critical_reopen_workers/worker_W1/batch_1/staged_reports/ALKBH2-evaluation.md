# ALKBH2 – Critical False-Rejection Reevaluation Report

**Gene:** ALKBH2 (DNA oxidative demethylase ALKBH2)  
**UniProt Accession:** Q6NS38  
**Protein Name:** DNA oxidative demethylase ALKBH2  
**Length:** 261 aa | **Mass:** 29.3 kDa  
**Aliases:** ABH2  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 30 | HPA: Nucleoplasm (main, Supported), Primary cilium + Cytosol (additional). UniProt: Nucleus (ECO:0000269 x3), Nucleolus (ECO:0000269), Nucleoplasm (ECO:0000269) – five experimental nuclear evidence codes. GO-CC: nucleolus (IDA:UniProtKB), nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB). EXTRAORDINARILY strong nuclear evidence. Multiple independent experimental demonstrations across all three annotation sources. The protein functions as a DNA repair enzyme that acts directly on DNA substrates – an inherently nuclear function. PERFECT score. |
| 2. Protein Size | 10 | 10 | 261 aa / 29.3 kDa – moderate size. Full marks. |
| 3. Research Novelty | 10 | 8 | PubMed strict: 35 publications. Novelty rule: 21-40 range = 8/10. ALKBH2 is moderately studied, with a well-characterized DNA repair function. Note: broad count is 98, close to the 100 rejection threshold, but strict (Title/Abstract with gene/protein keyword) is 35 and used for scoring. |
| 4. 3D Structure | 30 | 30 | AlphaFold mean pLDDT: 83.6 (68.6% >90). PDB: 18 experimental X-ray structures (3BTX, 3BTY, 3BTZ, 3BU0, 3BUC, 3H8O, 3H8R, 3H8X, 3RZG, 3RZH, 3RZJ, 3RZK, 3RZL, 3RZM, 3S57, 3S5A, 4MG2, 4MGT). Resolutions range from 1.60A to 3.06A. EXCEPTIONAL structural coverage – one of the most structurally characterized AlkB family members. Multiple liganded and unliganded structures, substrate complexes, and inhibitor complexes. PERFECT score. |
| 5. Regulatory Domains | 50 | 40 | IPR027450 (Alpha-ketoglutarate-dependent dioxygenase AlkB-like), IPR037151 (Alpha-ketoglutarate-dependent dioxygenase AlkB-like, C-terminal), IPR032852 (DNA oxidative demethylase ALKBH2), IPR005123 (Oxoglutarate/iron-dependent dioxygenase). PF13532 (2OG-Fe(II) oxygenase superfamily). ALKBH2 is a DNA repair enzyme that directly reverses alkylation damage on DNA bases, including N1-methyladenine, N3-methylcytosine, and etheno adducts. While not a classical transcriptional regulator, ALKBH2 directly modifies DNA bases, which can affect gene expression and chromatin structure. DNA repair at repetitive elements is critical for maintaining genome stability and preventing TE mobilization. The DNA base-modifying activity is a form of DNA-level regulation relevant to TE biology. |
| 6. PPI Network | 50 | 20 | STRING: ALKBH1 (0.986), JMJD4 (0.862), ALKBH6 (0.84), ALKBH8 (0.835), ALKBH4 (0.769). IntAct: SLX4, GOLGA2, ARL3, AARSD1, LCN15, ODAD3, SYNJ1, FTL, PIPSL, LCN1. Network dominated by AlkB family members (text-mining) and diverse co-IP partners. SLX4 is a DNA repair scaffold protein. The network reflects DNA repair and AlkB family connections rather than transcriptional or chromatin regulation. |
| **TOTAL** | **180** | **138** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Nucleoplasm
- **Additional Locations:** Primary cilium, Cytosol
- **IF Image Status:** no_image_detected (images listed but not fetchable for display in this cycle)
- **IF Image URLs:** ~40 images from multiple cell lines (A-431, U-2 OS, U-251 MG) and antibody batches
- **Key Finding:** HPA primary localization is Nucleoplasm with Supported reliability. Additional localization to primary cilium and cytosol noted but these are secondary. The main annotation is unambiguously nuclear.

**Interpretation note:** HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 The Nucleoplasm primary annotation with Supported reliability provides strong HPA-derived nuclear evidence.

### UniProt Subcellular Location
- **Nucleus** – Evidence: ECO:0000269 x3 (experimental evidence from publication, PMID:12486230) – Three independent experimental evidence codes for nuclear localization. This includes the foundational characterization paper (Duncan et al., 2002, PNAS; Aas et al., 2003, Nature) establishing ALKBH2 as a nuclear DNA repair enzyme.
- **Nucleus, nucleolus** – Evidence: ECO:0000269 (experimental) – Demonstrated nucleolar localization.
- **Nucleus, nucleoplasm** – Evidence: ECO:0000269 (experimental) – Demonstrated nucleoplasmic localization.
- **Total: FIVE experimental evidence codes** spanning three nuclear compartments. This is among the most thoroughly demonstrated nuclear localizations in the UniProt database.

### GO Cellular Component (GO-CC)
- **GO:0005730 (nucleolus)** – Evidence: IDA:UniProtKB – direct assay evidence for nucleolar localization.
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA – direct assay evidence from HPA.
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB – direct assay evidence.

### Functional Nuclear Context
- **ALKBH2 is a DNA repair enzyme** that acts on double-stranded and single-stranded DNA substrates within the nucleus. Its substrates are alkylated DNA bases (N1-methyladenine, N3-methylcytosine, etheno adducts) that it repairs by oxidative demethylation.
- **Associates with PCNA at replication forks** (PMID:19736315, PMID:26408825) – this places ALKBH2 at sites of active DNA replication in S-phase nuclei.
- **Repairs alkylated lesions in ribosomal DNA (rDNA)** – rDNA is transcribed in the nucleolus, consistent with ALKBH2's nucleolar localization.
- The DNA repair function is INHERENTLY nuclear, as DNA is a nuclear substrate.

**Summary:** ALKBH2 has arguably the STRONGEST nuclear evidence of any candidate in this batch. Five experimental (ECO:0000269) UniProt annotations, three GO IDA annotations, HPA Nucleoplasm (Supported), and an inherently nuclear function (DNA repair). Nuclear score: 30/30 (perfect).

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 35 | `"ALKBH2"[Title/Abstract] AND (gene OR protein OR hydrolase)` |
| Symbol Only (Title/Abstract) | 73 | `"ALKBH2"[Title/Abstract]` |
| Broad (All Fields) | 98 | `"ALKBH2"` |

**Alias Note:** Alias ABH2 observed but not used for scoring.

### Key Papers (with PMIDs)
1. **PMID:39923879** – Ramirez-Martin N, Buigues A, Rodriguez-Varela C et al. (2025). "Nicotinamide mononucleotide supplementation improves oocyte developmental competence in different ovarian damage conditions." *Am J Obstet Gynecol.* 2025 Aug. – ALKBH2 in oocyte quality and DNA repair.
2. **PMID:39633427** – Wada Y, Naito T, Fukushima T et al. (2024). "Evaluation of ALKBH2 and ALKBH3 gene regulation in patients with adult T-cell leukemia/lymphoma." *Virol J.* 2024 Dec 4. – ALKBH2 dysregulation in HTLV-1-associated leukemia. Note: HTLV-1 is a retrovirus that integrates into the genome – ALKBH2 regulation in this context is relevant to retroviral/TE biology.
3. **PMID:38925328** – Gutierrez R, Chan AYS, Lai SWT et al. (2024). "Lack of mismatch repair enhances resistance to methylating agents for cells deficient in oxidative demethylation." *J Biol Chem.* 2024 Aug. – ALKBH2 in DNA damage response, synthetic lethal relationships.
4. **PMID:26930515** – You C, Wang P, Nay SL et al. (2016). "Roles of Aag, Alkbh2, and Alkbh3 in the Repair of Carboxymethylated and Ethylated Thymidine Lesions." *ACS Chem Biol.* 2016 May 20. – Biochemical characterization of ALKBH2 substrate specificity.
5. **PMID:39631147** – An M, Chen C, Xiang J et al. (2024). "Systematic identification of pathogenic variants of non-small cell lung cancer in the promoters of DNA-damage repair genes." *EBioMedicine.* 2024 Dec. – ALKBH2 promoter variants in lung cancer.

### Literature Assessment
- **Total publications:** Moderate (35 strict, 98 broad). ALKBH2 is a well-characterized DNA repair enzyme.
- **Thematic focus:** DNA alkylation repair, cancer biology, alkylating chemotherapy response, DNA damage. The literature is focused on DNA repair mechanisms and cancer applications.
- **TE-relevant context:** A few indirect connections:
  - ALKBH2 repairs alkylated DNA at rDNA loci (repetitive DNA) – shows activity at repetitive elements.
  - DNA repair is essential for maintaining genome stability at repetitive elements; defects in repair can lead to TE mobilization.
  - The HTLV-1 connection (PMID:39633427) involves a retrovirus, which is evolutionarily related to endogenous retroviruses.
- **No publications directly linking ALKBH2 to TE silencing.**
- **Novelty score:** 8/10 (21-40 publications = 8). Moderate literature volume.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-Q6NS38-F1, version 6
- **Mean pLDDT:** 83.6
- **pLDDT Distribution:**
  - >90 (very high confidence): 68.6%
  - 70-90 (confident): 10.3%
  - 50-70 (low confidence): 1.1%
  - <50 (very low confidence): 19.9%
- **Assessment:** High-confidence predicted structure with a well-folded catalytic core. The 19.9% of residues <50 pLDDT likely correspond to the N-terminal region (residues 1-55), which is absent from most PDB structures (chains typically start at residue 56).

### Experimental PDB Structures
**18 structures available – exceptional structural coverage:**

| PDB ID | Method | Resolution | Chains | Notes |
|--------|--------|-----------|--------|-------|
| 3BTX | X-ray | 2.00 A | A=56-258 | Early structure |
| 3BTY | X-ray | 2.35 A | A=56-258 | |
| 3BTZ | X-ray | 3.00 A | A=57-258 | |
| 3BU0 | X-ray | 2.50 A | A=56-258 | |
| 3BUC | X-ray | 2.59 A | A=56-258 | |
| 3H8O | X-ray | 2.50 A | A=56-261 | |
| 3H8R | X-ray | 1.77 A | A=56-261 | High-resolution |
| 3H8X | X-ray | 2.50 A | A=56-261 | |
| 3RZG | X-ray | 1.62 A | A=56-261 | High-resolution |
| 3RZH | X-ray | 2.25 A | A=56-261 | |
| 3RZJ | X-ray | 2.50 A | A=56-261 | |
| 3RZK | X-ray | 2.78 A | A=56-261 | |
| 3RZL | X-ray | 2.60 A | A/D=56-261 | Dimer |
| 3RZM | X-ray | 3.06 A | A=56-260 | |
| 3S57 | X-ray | 1.60 A | A=56-258 | High-resolution |
| 3S5A | X-ray | 1.70 A | A=56-258 | High-resolution |
| 4MG2 | X-ray | 2.30 A | A=56-258 | |
| 4MGT | X-ray | 2.60 A | A=56-258 | |

### Structural Assessment
- This is one of the most extensively characterized structures among AlkB family proteins. The high-resolution structures (1.60-1.77 A) provide atomic-level detail of the catalytic mechanism.
- PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。But with 18 experimental structures, AlphaFold is secondary.
- The catalytic domain (residues 56-261) is the well-characterized 2-oxoglutarate/Fe(II)-dependent dioxygenase fold. The N-terminal region (1-55) may contain targeting or regulatory elements.
- **Score:** 30/30 – perfect. Eighteen experimental X-ray structures at resolutions down to 1.60 A, plus a high-confidence AlphaFold prediction. This is among the best structurally characterized proteins in the candidate pool.

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| ALKBH1 | 0.986 | 0 | 0.986 | AlkB homolog 1 – DNA/RNA demethylase |
| JMJD4 | 0.862 | 0 | 0.852 | JmjC domain-containing protein 4 |
| ALKBH6 | 0.84 | 0 | 0.837 | AlkB homolog 6 |
| ALKBH8 | 0.835 | 0 | 0.832 | AlkB homolog 8 – tRNA modification |
| ALKBH4 | 0.769 | 0 | 0.756 | AlkB homolog 4 |
| ALKBH7 | 0.759 | 0 | 0.751 | AlkB homolog 7 – mitochondrial |
| FTO | 0.719 | 0 | 0.719 | Fat mass and obesity-associated – RNA demethylase |
| ALKBH5 | 0.625 | 0 | 0.622 | AlkB homolog 5 – RNA m6A demethylase |
| ALKBH3 | 0.609 | 0 | 0.542 | AlkB homolog 3 – DNA/RNA repair |
| MPG | 0.604 | 0 | 0.595 | N-methylpurine DNA glycosylase |

### IntAct
Total: 15 interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| SLX4 | anti tag co-IP | PMID:19596235 | association |
| GOLGA2 | two hybrid array | PMID:32296183 | physical association |
| AARSD1 | anti tag co-IP | PMID:28514442 | association |
| LCN15 | anti tag co-IP | PMID:28514442 | association |
| ODAD3 | anti tag co-IP | PMID:28514442 | association |
| SYNJ1 | anti tag co-IP | PMID:28514442 | association |
| FTL | anti tag co-IP | PMID:33961781 | association |
| PIPSL | anti tag co-IP | PMID:33961781 | association |
| LCN1 | anti tag co-IP | PMID:33961781 | physical association |
| Kif19 | anti tag co-IP | PMID:26496610 | association |
| Sesn2 | anti tag co-IP | PMID:26496610 | association |
| Nedd1 | anti tag co-IP | PMID:26496610 | association |
| FERMT3 | anti tag co-IP | PMID:26496610 | association |

### PPI Network Assessment
- **Network character:** The STRING network is dominated by AlkB family members (text-mining associations, not experimental). The IntAct network shows diverse co-IP interactions from large-scale studies.
- **Notable interactions for TE regulation:**
  - **SLX4 (BTBD12):** A DNA repair scaffold protein that coordinates structure-specific endonucleases (XPF-ERCC1, MUS81-EME1, SLX1). SLX4 is involved in resolving DNA structures such as Holliday junctions, replication forks, and telomeres. SLX4's role in processing difficult-to-replicate genomic regions (including repetitive elements) is potentially relevant to TE stability.
  - **ALKBH1, ALKBH3, ALKBH5:** These AlkB family members have broader substrate specificity including RNA. ALKBH5 is an m6A RNA demethylase – m6A modification is known to regulate TE-derived RNAs.
- **Network quality:** Mostly text-mining and large-scale co-IP. Few functionally validated interactions.
- **Score:** 20/50 – AlkB family-centric network with limited TE-regulatory connections. SLX4 interaction is interesting for repetitive DNA processing.

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
ALKBH2 was likely auto-rejected because:
1. Broad PubMed count (98) approaches the >100 rejection threshold – the automated system may have used broad rather than strict count
2. HPA also detects cytosolic and primary cilium localization, which could have reduced the nuclear confidence score
3. Competitive exclusion: ALKBH2 may have been deprioritized relative to other AlkB family members

### Recheck Analysis
1. **HPA Evidence:** Nucleoplasm (main, Supported) – despite additional locations, the primary annotation is clearly nuclear. The Supported reliability confirms reproducibility.
2. **UniProt Evidence:** FIVE experimental (ECO:0000269) nuclear annotations across three compartments. EXCEPTIONALLY strong.
3. **GO-CC Evidence:** Three IDA-level nuclear annotations.
4. **Functional Evidence:** DNA repair enzyme acting directly on DNA. The function is inherently nuclear.
5. **PubMed Count:** Strict = 35 (well below 100), broad = 98 (below 100 but borderline). Should NOT trigger rejection.
6. **Structural Data:** 18 experimental PDB structures – exceptional.

### Verdict on False Rejection
**The original rejection was FALSE – ALKBH2 should NOT have been rejected.** The nuclear evidence is among the strongest possible: five experimental UniProt annotations, three IDA GO annotations, HPA Nucleoplasm primary localization, and an inherently nuclear DNA repair function. The PubMed count (35 strict, 98 broad) is well within acceptable range. The structural data (18 PDB structures, 1.60 A resolution) is exceptional. ALKBH2 appears to have been a victim of overly aggressive filtering, possibly due to the broad PubMed count approaching the 100 threshold or cytosolic HPA annotations reducing automated confidence.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

ALKBH2 presents a unique angle for TE regulation – through DNA repair rather than transcriptional/chromatin regulation:

1. **DNA Repair at Repetitive Elements:** ALKBH2 is known to repair alkylated DNA lesions in ribosomal DNA (rDNA), which is a repetitive genomic locus (PMID:23972994). This demonstrates activity at repetitive DNA. rDNA is one type of repetitive element; ALKBH2 could similarly act at other repeats including TEs. Alkylation damage at TEs can lead to mutations, strand breaks, and potentially TE mobilization – repair by ALKBH2 would maintain TE integrity and prevent activation.

2. **Replication Fork Association:** ALKBH2 associates with PCNA at replication forks (PMID:19736315, PMID:26408825). Replication of repetitive DNA (including TEs) is challenging and prone to fork stalling. ALKBH2's role at replication forks during S-phase could be particularly important for maintaining TE stability during DNA replication.

3. **AlkB Family Epigenetic Context:** The AlkB family includes RNA demethylases (ALKBH5 = m6A eraser, FTO = m6A/m6Am eraser). m6A modification of TE-derived RNAs is a known regulatory mechanism that affects TE transcript stability and translation. While ALKBH2 acts on DNA (not RNA), the family context suggests broader roles in nucleic acid modification relevant to TE biology.

4. **HTLV-1 Connection (PMID:39633427):** ALKBH2 is dysregulated in adult T-cell leukemia/lymphoma, which is caused by HTLV-1 retrovirus. Retroviruses integrate into the host genome and are evolutionarily related to endogenous retroviruses (ERVs). ALKBH2 regulation in a retrovirus-driven malignancy could reflect a role in managing retroviral/retrotransposon DNA.

5. **Novelty for TE field:** Despite moderate literature, no publication has examined ALKBH2 specifically in the context of TE regulation or repetitive element stability. This represents a genuine novel application of the protein's known functions.

6. **Caveats:**
   - ALKBH2 is a DNA repair enzyme with narrow substrate specificity (alkylated bases). Its role at TEs would be limited to repairing specific DNA lesions, not broad TE regulation.
   - No known interactions with chromatin modifiers, KRAB-ZNFs, or other TE silencing machinery.
   - The TE connection is hypothetical and requires direct experimental testing.

**Assessment:** ALKBH2 is a MODERATE-TO-HIGH interest candidate uniquely positioned at the DNA repair-TE stability intersection. Unlike most candidates that regulate TE expression through chromatin or transcription, ALKBH2 could contribute to TE regulation by maintaining the physical integrity of TE DNA sequences, preventing mutations and strand breaks that could activate transposition. This is a complementary and under-explored angle in TE biology.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Reasoning:** ALKBH2 was falsely rejected despite the strongest nuclear evidence in Batch 1 (five experimental UniProt annotations, three GO IDA). The protein is a nuclear DNA repair enzyme with exceptional structural characterization (18 PDB structures). The PubMed count (35 strict) is moderate and should not trigger rejection. ALKBH2 offers a unique perspective on TE regulation through DNA repair at repetitive elements, complementing the more common transcriptional/chromatin-focused candidates. The rDNA repair activity and replication fork association provide mechanistic plausibility for TE-relevant functions.

**Score: 138/180** – Very strong nuclear score (30/30), perfect structural score (30/30), good regulatory domain score for DNA-modifying activity, but limited PPI network. The score reflects ALKBH2's strengths as a highly characterized nuclear enzyme with potential novel applications to TE biology.

**Recommended next steps:**
1. Investigate whether ALKBH2 repairs alkylation damage specifically at TE loci (ChIP-seq or damage-specific sequencing approaches).
2. Test whether ALKBH2 deficiency leads to increased TE mobilization or expression (using ALKBH2 knockout cell lines and TE expression assays).
3. Examine ALKBH2 localization and activity at repetitive elements during S-phase (replication stress at repeats).
4. Explore the relationship between ALKBH2's DNA repair function and epigenetic silencing marks at TEs.

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-02)*  
*Status: FALSE REJECTION CONFIRMED – gene reopened*

ALKBH2 is one of the most structurally and functionally characterized proteins in this audit. The 18 PDB structures, five experimental nuclear localization annotations, and well-characterized DNA repair mechanism provide an exceptionally solid foundation. The false rejection likely resulted from overly conservative PubMed filtering (broad count = 98, nearly at the >100 threshold) and a failure to distinguish primary nuclear localization from secondary cytosolic/primary cilium annotations. ALKBH2 offers a novel angle on TE regulation: rather than controlling TE expression through chromatin or transcription factors, it could maintain TE genomic stability through DNA repair. This DNA repair-centric perspective on TE biology is underexplored and merits investigation. The high structural coverage (1.60 A resolution) makes ALKBH2 amenable to structure-guided functional studies and potential drug targeting. This gene is strongly recommended for inclusion in the TE-regulatory candidate pipeline.
