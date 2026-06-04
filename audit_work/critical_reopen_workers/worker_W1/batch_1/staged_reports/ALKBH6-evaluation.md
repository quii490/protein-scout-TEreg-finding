# ALKBH6 – Critical False-Rejection Reevaluation Report

**Gene:** ALKBH6 (Probable RNA/DNA demethylase ALKBH6)  
**UniProt Accession:** Q3KRA9  
**Protein Name:** Probable RNA/DNA demethylase ALKBH6  
**Length:** 238 aa | **Mass:** 26.5 kDa  
**Aliases:** ABH6  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 2 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 24 | HPA: Nucleoplasm (main, Approved), Focal adhesion sites (additional). UniProt: Cytoplasm + Nucleus (both ECO:0000269, experimental). GO-CC: nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB), focal adhesion (IDA:HPA). Strong dual localization evidence. Nucleoplasm is HPA primary annotation with Approved reliability. Minor deduction for dual localization and focal adhesion annotation suggesting non-nuclear functions. |
| 2. Protein Size | 10 | 10 | 238 aa / 26.5 kDa – moderate, tractable. Full marks. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 7 publications. Novelty rule: ≤20 = 10/10. ALKBH6 is very poorly studied. Maximum novelty. |
| 4. 3D Structure | 30 | 28 | AlphaFold mean pLDDT: 91.1 (77.3% >90, only 1.7% <50). PDB: 7VJS (X-ray, 1.79A), 7VJV (X-ray, 1.75A) – two high-resolution experimental structures with full-length coverage (chains A=1-238). Excellent structural data. Minor deduction for lack of substrate-complex structures. |
| 5. Regulatory Domains | 50 | 30 | IPR027450 (AlkB-like dioxygenase), IPR032862 (ALKBH6-specific), IPR005123 (2OG-Fe(II) oxygenase). PF13532. ALKBH6 binds nucleic acids (ssDNA/ssRNA preference) and may function in nucleic acid damage repair or epigenetic demethylation. The demethylase activity could affect DNA/RNA modifications relevant to TE regulation. STRING interaction with MED29 (Mediator complex, experimental 0.84) suggests connection to transcriptional machinery. RUNX1 (transcription factor) interaction also noted. Moderate regulatory domain score. |
| 6. PPI Network | 50 | 18 | STRING: MED29 (0.892, experimental 0.84), AlkB family members (textmining). IntAct: RUNX1 (two-hybrid, PMID:35914814). Very small network. MED29 is a Mediator complex component linking to transcription. But no UniProt interactions (empty list) and only 2 IntAct interactors. Very poorly characterized interaction network. |
| **TOTAL** | **180** | **120** | |

---

## Nuclear Evidence Section

### HPA
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Nucleoplasm
- **Additional:** Focal adhesion sites
- **Key Finding:** Primary HPA annotation is Nucleoplasm with Approved reliability. This is among the strongest HPA evidence available.

### UniProt Subcellular Location
- **Cytoplasm** – ECO:0000269 (experimental, PMID:35120926)
- **Nucleus** – ECO:0000269 (experimental, PMID:35120926)
- Both are experimental assertions from the same publication characterizing ALKBH6's nucleic acid binding.

### GO-CC
- **GO:0005654 (nucleoplasm)** – IDA:HPA
- **GO:0005634 (nucleus)** – IDA:UniProtKB
- **GO:0005737 (cytoplasm)** – IDA:UniProtKB
- **GO:0005925 (focal adhesion)** – IDA:HPA

**Summary:** Strong nuclear evidence (HPA Approved + UniProt experimental + GO IDA), though dual localization to cytoplasm and focal adhesions is also documented. Nuclear score: 24/30.

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict | 7 |
| Broad | 11 |

### Key Papers
1. **PMID:35120926** – Ma L, Lu H, Tian Z et al. (2022). "Structural insights into the interactions and epigenetic functions of human nucleic acid repair protein ALKBH6." *J Biol Chem.* 2022 Mar. – FOUNDATIONAL: Characterizes nucleic acid binding preferences and structural basis.
2. **PMID:35657140** – Fang KY et al. (2022). ALKBH6 identified in COVID-19 bioinformatics screen.
3. **PMID:41303572** – Yuan L et al. (2025). ALKBH6 in nacre color diversity.
4. **PMID:41591843** – Bai X et al. (2026). ZMYMD11 tumor suppressor structural study mentioning ALKBH6.
5. **PMID:42187748** – Guo W et al. (2026). m6A regulators including ALKBH6 in nematode.

**Assessment:** Extremely low literature (7 strict). Maximum novelty. No TE-specific publications.

---

## AlphaFold / PDB / PAE

- **AlphaFold:** mean pLDDT 91.1 (77.3% >90)
- **PDB:** 7VJS (1.79A), 7VJV (1.75A) – both full-length X-ray structures
- **Assessment:** Exceptional structural coverage. PAE 图像暂无数据。Structure score: 28/30.

---

## PPI Network

Very sparse. STRING shows MED29 (Mediator complex subunit, experimental 0.84) and AlkB family members (textmining). IntAct has RUNX1 (two-hybrid) and one CLASH interaction. Only 2 total experimental interactors. MED29 connects ALKBH6 to transcriptional Mediator complex, potentially relevant for gene regulation.

---

## FALSE REJECTION RECHECK

**Verdict: FALSE REJECTION.** ALKBH6 has HPA Approved Nucleoplasm + UniProt experimental nuclear evidence + 2 high-resolution PDB structures. The nuclear evidence is robust. The false rejection likely resulted from the very sparse PPI network (zero UniProt interactions) and the focal adhesion annotation reducing automated nuclear confidence. **SCORED – REOPENED.**

---

## TE-Regulator Relevance

ALKBH6 is a nucleic acid demethylase with MED29/RUNX1 connections to transcription. While no TE-specific evidence exists, its epigenetic demethylation function (analogous to ALKBH5/m6A) could affect TE-derived RNA modifications. Very high novelty (7 PubMed). MODERATE interest candidate.

---

## Final Decision: SCORED (120/180) – REOPENED

---

## Manual Review Note
FALSE REJECTION CONFIRMED. ALKBH6 has strong nuclear evidence and exceptional structural data. Primary limitation is the very sparse PPI network. Reopened due to robust nuclear localization and very high novelty.

---

## Extended Verification Notes

The above scoring and analysis were generated through systematic re-evaluation of all harvested data sources for ALKBH6. The gene was assessed under the critical false-rejection audit protocol defined for Worker W1. Key evidence sources consulted include: UniProt (Q3KRA9) for protein sequence, function, subcellular localization, GO annotations, PDB structures, and interactions; Human Protein Atlas for immunofluorescence-based subcellular localization; PubMed for literature metrics and key publications; AlphaFold for predicted protein structure confidence metrics; STRING for functional protein association networks; and IntAct for experimentally validated molecular interactions.

The scoring follows the predefined six-dimension framework (/180 total): Nuclear Localization (30), Protein Size (10), Research Novelty (10 based on PubMed strict count), 3D Structure (30), Regulatory Domains (50), and PPI Network (50). Where HPA IF images were not reliably obtainable for direct review, nuclear localization was assessed based on HPA database annotations (localization categories and reliability scores) combined with UniProt subcellular location evidence (evidence codes) and GO Cellular Component annotations (evidence types). PAE images were not locally generated or reliably fetched for this cycle; structural judgments are based on AlphaFold pLDDT statistics and available experimental PDB structures.

ALKBH6 represents a promising candidate for further TE-regulatory investigation due to its nucleic acid demethylase activity (which could affect epigenetic modifications on TE-derived DNA/RNA), nuclear localization (HPA Approved Nucleoplasm), and very high structural confidence (mean pLDDT 91.1, two high-resolution experimental structures). The primary limitation is the very sparse characterized PPI network, which should be addressed through targeted interaction studies before committing significant experimental resources to TE-specific investigations.
