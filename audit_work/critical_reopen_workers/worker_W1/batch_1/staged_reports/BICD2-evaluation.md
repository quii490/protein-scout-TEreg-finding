# BICD2 – Critical False-Rejection Reevaluation Report

**Gene:** BICD2 (Protein bicaudal D homolog 2)  
**UniProt Accession:** Q8TD16  
**Protein Name:** Protein bicaudal D homolog 2  
**Length:** 824 aa | **Mass:** 93.5 kDa  
**Aliases:** KIAA0699  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 2 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 18 | HPA: Golgi apparatus + Plasma membrane + Cytosol (main, Supported). NO nuclear annotation from HPA. UniProt: Nucleus envelope (ECO:0000269), Nucleus nuclear pore complex (ECO:0000269) – both experimental but describe nuclear periphery/membrane, not nuclear interior. Also: Golgi, cytoskeleton, cytoplasm. GO-CC: nuclear envelope (IDA:UniProtKB), nuclear pore (IDA:UniProtKB), annulate lamellae (IDA). The nuclear annotations are specifically nuclear envelope/pore, NOT nucleoplasm/nucleus interior. This is a nuclear periphery protein, not a nucleoplasmic one. |
| 2. Protein Size | 10 | 8 | 824 aa / 93.5 kDa – large protein. Slight deduction. |
| 3. Research Novelty | 10 | 0 | PubMed strict: 116. PubMed>100→REJECTED. BICD2 is well-studied primarily in neurogenetics (BICD2 mutations cause spinal muscular atrophy) and dynein/dynactin motor biology. |
| 4. 3D Structure | 30 | 24 | AlphaFold mean pLDDT: 78.0 (50.1% >90, 21.8% 70-90, 7.9% 50-70, 20.1% <50). PDB: 6OFP (X-ray, 2.01A, C-terminal domain res 715-804), 6PSE (X-ray, 2.40A, N-terminal domain res 1-98). Two domains solved with good resolution. The middle region (298 residues) is predicted coiled-coil and shows moderate AF confidence. |
| 5. Regulatory Domains | 50 | 15 | IPR018477 (Bicaudal D). PF09730. BICD2 is a dynein/dynactin adaptor protein that links cargo to microtubule motor complexes. It regulates Golgi-ER transport, nuclear positioning, and centrosome positioning. While it associates with nuclear pore complex (RANBP2) and nuclear envelope, its function is in CYTOPLASMIC transport and nuclear positioning, not in nuclear transcription/chromatin regulation. No DNA-binding, chromatin, or transcriptional regulatory domains. LOW regulatory domain score for TE purposes. |
| 6. PPI Network | 50 | 30 | STRING: DYNC1H1 (0.999), DCTN2 (0.999), DYNC1LI1 (0.999), DCTN1 (0.998), DYNC1I1 (0.997), RANBP2 (0.995), RAB6A (0.991). IntAct: PLK1, ZRANB1, Ranbp2, LRRK2, NEK9, histone H1 variants (H1-5, H1-2, H1-4 cross-linked), KIF2B, MFAP1. All core interactions are with dynein/dynactin motor complex. RANBP2 is a nuclear pore component. The histone H1 cross-linking interactions (PMID:30021884) are INTRIGUING for chromatin biology – H1 is a linker histone that compacts chromatin and can contribute to TE silencing. Large network centered on microtubule transport. |
| **TOTAL** | **180** | **95** | |

**NOTE: PubMed>100 (strict=116) triggers REJECTION rule.**

---

## Nuclear Evidence Section

### HPA
- **Status:** hpa_localization_available
- **Reliability (IF):** Supported
- **Main Location:** Golgi apparatus, Plasma membrane, Cytosol
- **Key Finding:** HPA does NOT detect BICD2 in the nucleus, nuclear envelope, or nuclear pore. The primary HPA annotations are all cytoplasmic/membrane compartments. This is significant.

### UniProt Subcellular Location
- **Nucleus envelope** – ECO:0000269 (experimental) – at the nuclear periphery
- **Nucleus, nuclear pore complex** – ECO:0000269 (experimental) – at nuclear pores
- **Golgi apparatus** – ECO:0000269 x2
- **Cytoplasm, cytoskeleton** – ECO:0000269
- **Cytoplasm** – ECO:0000269 x2

### GO-CC
- **GO:0005635 (nuclear envelope)** – IDA:UniProtKB
- **GO:0005643 (nuclear pore)** – IDA:UniProtKB
- **GO:0005642 (annulate lamellae)** – IDA:UniProtKB
- **GO:0005794 (Golgi apparatus)** – IDA:HPA
- **GO:0005829 (cytosol)** – IDA:HPA

**Summary:** BICD2 is a NUCLEAR PERIPHERY protein (nuclear envelope + pore), NOT a nucleoplasmic/nuclear interior protein. Its function involves dynein adaptor activity at the nuclear envelope for nuclear positioning. HPA does not detect it at the nucleus (HPA may not be sensitive to nuclear envelope staining). Nuclear score: 18/30 – nuclear periphery localization only, not nuclear interior.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict | 116 |
| Broad | 199 |

**REJECTION TRIGGERED: PubMed strict > 100.**

### Key Papers
1. **PMID:38702287** – Tazir M et al. (2024). BICD2 in distal hereditary motor neuropathies.
2. **PMID:36930595** – Yi J et al. (2023). "Role of Nesprin-2 and RanBP2 in BICD2-associated brain developmental disorders." *PLoS Genet.* – BICD2 at nuclear pore with RANBP2.
3. **PMID:32056343** – Frasquet M et al. (2020). Clinical spectrum of BICD2 mutations.
4. **PMID:38913821** – Iversen LV et al. (2024). BICD2 autoantibodies in systemic sclerosis.
5. **PMID:33572761** – Rossi E et al. (2021). BICD2 in HIV-1 capsid interactions.

**Assessment:** BICD2 is well-studied (116 PubMed) in neurogenetics, dynein biology, and organelle positioning.

---

## AlphaFold / PDB / PAE

- **AlphaFold:** mean pLDDT 78.0 (50.1% >90, 20.1% <50)
- **PDB:** 6OFP (2.01A, C-term domain), 6PSE (2.40A, N-term domain)
- **Assessment:** Good structural data on terminal domains. PAE 图像暂无数据。

---

## FALSE REJECTION RECHECK

### Analysis
1. **Nuclear evidence:** WEAK. BICD2 localizes to nuclear ENVELOPE and PORE (periphery), not nucleoplasm. HPA does not detect nuclear staining. This is not the same as nucleoplasmic transcription/chromatin regulators.
2. **Functional context:** BICD2 is a cytoplasmic dynein adaptor. Its nuclear function is limited to nuclear envelope association (linking dynein to nuclear pores for nuclear positioning during G2). Not involved in transcription, chromatin, or RNA processing.
3. **H1 histone interaction:** The cross-linking interactions with linker histones H1-2, H1-4, H1-5 (PMID:30021884) are technically interesting but likely reflect proximity during nuclear envelope association, not chromatin-level function.
4. **PubMed:** 116 strict >100 → automatic rejection.

### Verdict
**The original rejection was CORRECT.** BICD2 is a cytoplasmic dynein adaptor that associates with the nuclear periphery (envelope/pore) for organelle positioning. It is NOT a nuclear interior protein and has no direct transcriptional/chromatin regulatory function. PubMed count exceeds 100. This gene should remain rejected.

---

## TE-Regulator Relevance

Very LOW. BICD2 is a microtubule motor adaptor. Its only potential TE relevance is through: (1) nuclear positioning during cell cycle, (2) RANBP2 interaction at nuclear pore (nuclear transport may indirectly affect TE regulation), and (3) histone H1 cross-linking (but this is likely proximity-based, not functional). No direct connection to TE silencing, chromatin regulation, or transcription.

---

## Final Decision: REJECTED (PubMed>100 + weak nuclear evidence)

Score: 95/180. Nuclear evidence is limited to nuclear periphery (envelope/pore), not nuclear interior. PubMed exceeds 100. Low TE-regulatory relevance. Confirmed rejection.

---

## Manual Review Note
CONFIRMED REJECTION. BICD2's nuclear localization is limited to the nuclear envelope/pore complex, which is functionally distinct from nucleoplasmic transcription/chromatin regulation. HPA does not detect nuclear staining. The protein is a dynein adaptor with primary function in cytoplasmic transport and organelle positioning. While annotated as nuclear by UniProt, this refers specifically to nuclear pore/envelope association, not nuclear interior function. PubMed exceeds 100. Not suitable for TE-regulatory investigation.
