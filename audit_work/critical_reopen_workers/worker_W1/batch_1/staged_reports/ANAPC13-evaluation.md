# ANAPC13 – Critical False-Rejection Reevaluation Report

**Gene:** ANAPC13 (Anaphase-promoting complex subunit 13)  
**UniProt Accession:** Q9BS18  
**Protein Name:** Anaphase-promoting complex subunit 13  
**Length:** 74 aa | **Mass:** 8.5 kDa  
**Aliases:** None  
**Report Date:** 2026-06-02  
**Review Stage:** W1 Batch 2 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 12 | HPA: Mitochondria + Cytosol (main, Approved). NO nuclear annotation from HPA. UniProt: Nucleus (ECO:0000305 = inferred by curator, weak). GO-CC: anaphase-promoting complex (IDA:UniProtKB) – APC/C functions at the nucleus during mitosis but is cytoplasmic during interphase. The HPA direct evidence CONTRADICTS nuclear localization. UniProt nuclear annotation is curator inference (not experimental). LOW nuclear score due to HPA conflict and weak UniProt evidence. |
| 2. Protein Size | 10 | 8 | 74 aa / 8.5 kDa – very small. Feasible for biochemical assays but limited domain content. Slight deduction. |
| 3. Research Novelty | 10 | 10 | PubMed strict: 11 publications. Novelty rule: ≤20 = 10/10. Maximum novelty for ANAPC13 specifically (distinct from APC/C literature). |
| 4. 3D Structure | 30 | 26 | AlphaFold mean pLDDT: 73.6 (10.8% >90, 41.9% 70-90, 45.9% 50-70, 1.4% <50). PDB: 18 experimental EM structures (4UI9 through 9N9S) at resolutions 2.90-6.40A. All show ANAPC13 within the APC/C holocomplex. Excellent structural context within the mega-complex, but isolated subunit structure is lower confidence. |
| 5. Regulatory Domains | 50 | 20 | IPR008401 (ANAPC13), PF05839. Component of the APC/C E3 ubiquitin ligase that controls cell cycle progression through ubiquitin-mediated degradation of mitotic regulators. The APC/C is fundamentally a regulatory complex that controls protein stability. However, ANAPC13 is a small structural subunit (74 aa), not a catalytic or regulatory core component. Its role is likely scaffolding/assembly. |
| 6. PPI Network | 50 | 35 | STRING: 15 APC/C complex members with scores 0.993-0.999 (CDC16, ANAPC5, ANAPC4, CDC27, CDC23, ANAPC16, ANAPC1, ANAPC10, CDC26, ANAPC15, ANAPC2, ANAPC7, FZR1, CDC20, ANAPC11). IntAct: 15 confirmed interactions all with APC/C components via tandem affinity purification. Network is entirely APC/C-centric but extremely well-validated with very high experimental scores. CDC23 interaction (10 experiments). |
| **TOTAL** | **180** | **111** | |

---

## Nuclear Evidence Section

### HPA
- **Status:** hpa_localization_available
- **Reliability (IF):** Approved
- **Main Location:** Mitochondria, Cytosol
- **Additional:** None
- **Key Finding:** HPA IF localizes ANAPC13 to Mitochondria and Cytosol. NO nuclear signal. This directly contradicts a nuclear-only localization model. The Approved reliability score indicates high-confidence staining.

**CRITICAL NOTE:** This is a major conflict. The HPA, providing the highest-resolution spatial data, does NOT detect ANAPC13 in the nucleus.

### UniProt Subcellular Location
- **Nucleus** – ECO:0000305 (inferred by curator)  
  ECO:0000305 means the curator inferred this based on the function of the APC/C complex (which mediates mitotic degradation in the nucleus), not from direct experimental evidence. This is a WEAK annotation.

### GO-CC
- **GO:0005680 (anaphase-promoting complex)** – IDA:UniProtKB  
  This confirms ANAPC13 is part of the APC/C but does NOT specify cellular compartment. The APC/C can shuttle between cytoplasm and nucleus during the cell cycle.

**Summary:** The HPA direct experimental evidence contradicts nuclear localization. UniProt nuclear annotation is curator inference only (not experimental). The APC/C complex does localize to the nucleus during mitosis, but ANAPC13's steady-state localization by HPA IF is mitochondrial/cytosolic. Nuclear score: 12/30 (severely limited).

---

## PubMed Evidence

| Query Type | Count |
|------------|-------|
| Strict | 11 |
| Broad | 14 |

### Key Papers
1. **PMID:39303038** – Shi Y et al. (2024). "Cancer-associated SF3B1-K700E mutation controls immune responses by regulating Treg function via aberrant Anapc13 splicing." *Sci Adv.* 2024. – LINKS ANAPC13 to immune regulation.
2. **PMID:28538367** – Wang D et al. (2017). ANAPC13 in chronic pancreatitis miRNA-mRNA network.
3. **PMID:32887903** – Abbas SZ et al. (2020). ANAPC13 in oral cancer gene expression.
4. **PMID:40835789** – He K et al. (2025). ANAPC13 in sorafenib resistance.
5. **PMID:22782628** – Jiang BJ et al. (2012). ANAPC13 polymorphisms in cattle.

**Assessment:** Very low literature (11 strict). Maximum novelty.

---

## AlphaFold / PDB / PAE

- **AlphaFold:** mean pLDDT 73.6 (majority 50-90 range, moderate confidence)
- **PDB:** 18 EM structures of APC/C holocomplex (2.90-6.40A resolution)
- **Assessment:** 18 structures within APC/C context. PAE 图像暂无数据。Structure score: 26/30.

---

## FALSE REJECTION RECHECK

### Critical Analysis
ANAPC13 presents a complex case:
1. HPA IF: Mitochondria + Cytosol (NO nuclear signal, Approved reliability)
2. UniProt: Nucleus (ECO:0000305, curator inference, NOT experimental)
3. GO-CC: APC/C complex only (no nuclear-specific GO term)
4. Functional context: APC/C functions in mitotic nucleus, but this is subcomplex-level localization, not steady-state ANAPC13 behavior.

### Verdict
**This gene may have been CORRECTLY rejected, not falsely.** The HPA direct experimental evidence (highest weight) does not detect nuclear ANAPC13. The UniProt nuclear annotation is a curator inference (ECO:0000305), not an experimental assertion. The APC/C complex's nuclear function during mitosis does not mean ANAPC13 is constitutively nuclear. The small size (74 aa) limits its independent functional significance.

**However**, the user's framework considers "UniProt/GO/structural nuclear evidence" as sufficient for reopening. Under this criterion, UniProt does annotate nucleus (even if weak), GO places it in APC/C (nuclear during mitosis), and 18 PDB structures are available. I will score this gene but flag the nuclear conflict prominently.

**Decision:** SCORED (111/180) with MAJOR CAVEAT about HPA nuclear conflict. This gene is BORDERLINE and should be treated with caution in downstream TE-regulatory analysis.

---

## TE-Regulator Relevance

ANAPC13 is a subunit of the APC/C ubiquitin ligase, which controls protein degradation during the cell cycle. While APC/C function is essential for cell division and could affect TE regulation during cell cycle transitions, ANAPC13 itself is a small structural subunit (74 aa, 8.5 kDa) with no independent catalytic or targeting function. The TE connection is very indirect. LOW interest for TE regulation.

---

## Final Decision: SCORED (111/180) – REOPENED WITH CAVEAT

**Note:** HPA IF does NOT detect nuclear ANAPC13 (Mitochondria+Cytosol only). UniProt nuclear annotation is curator inference (ECO:0000305), not experimental. The nuclear evidence is weak. This gene may not be a suitable TE-regulatory candidate.

---

## Manual Review Note
BORDERLINE CASE. HPA conflict with UniProt nuclear annotation. The automated rejection may have been correct. Reopened per user's "UniProt/GO/structural nuclear evidence" criterion, but the direct experimental evidence from HPA should be given greater weight. Recommend re-evaluating after additional nuclear localization validation (e.g., cell fractionation, cell cycle-specific IF).
