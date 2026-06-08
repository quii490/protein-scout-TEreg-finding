---
type: centrosome-protein-evaluation
gene: "CETN2"
module: centrosome
status: centrosome_eliminated
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# CETN2 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** P41208
- **Protein name:** Centrin-2 (CETN2)
- **Synonyms:** CALT, CEN2
- **Length:** 172 aa
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000147400-CETN2
- **HPA reliability:** Supported (IF)
- **HPA location text:** Nucleoplasm, flagellar centriole, centrosome
- **IF image:** Available

![[CETN2_IF_1.jpg]]

CETN2 is a core centriole component and calcium-binding protein. HPA IF shows centrosome puncta.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, centriole, cilium basal body, nucleus
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA, TAS
  - GO:0036064 (ciliary basal body) — IDA
  - GO:0035869 (ciliary transition zone) — IDA
  - GO:0005634 (nucleus) — IDA (NER)
- **Notes:** Dual role: centrosome (structural centriole) + nucleus (NER/DNA repair). This dual function is notable for TE biology.

## 4. PubMed Evidence

- **Total PubMed:** 111 papers ⚠️ **EXCEEDS THRESHOLD (>100)**
- **Strict query (centrosome/centriole):** 55 papers
- **Broad query:** 92 papers
- **Key papers:**
  - Salisbury JL et al. (2002) — Centrin-2 and centriole duplication; PMID: 11864938
  - Araki M et al. (2001) — CETN2 in NER; interacts with XPC; PMID: 11278958
  - Nishi R et al. (2005) — CETN2 enhances XPC damage recognition; PMID: 15964821
- **Assessment:** 111 papers. Unique dual role in centrosome + NER DNA repair. NER function highly relevant for TE biology.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Very high (172 aa, compact, well-folded)
- **PAE:** Available
- **PDB:** 2A4J (CETN2+XPC), 2GGM (CETN2+Sfi1)
- **InterPro:** IPR002048 EF-hand; 4 EF-hand motifs
- **Domain notes:** Calcium-induced conformational change. Two binding modes: XPC (NER) vs. Sfi1 (centrosome).

## 6. PPI / humanPPI

- **STRING:** Good network
- **IntAct:** Curated
- **Centrosome interactors:** Sfi1, POC5, hPOC1
- **NER interactors:** XPC, RAD23B, HR23B

## 7. TE-Regulator Relevance

- Core component of Nucleotide Excision Repair (NER) — directly involved in DNA damage recognition with XPC
- NER repairs UV/bulky DNA lesions — same pathways activated by TE integration intermediates
- CETN2's dual role (centrosome + NER) uniquely connects centrosome biology to DNA repair
- **Strength:** Highest TE relevance in pilot set due to direct NER/DNA repair function

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 19/20 | Core centriole protein. HPA + UniProt + GO-CC + PDB. |
| TE relevance | 16/20 | Direct NER/DNA repair. XPC co-factor. Strongest TE link. |
| PubMed/literature | 10/20 | 111 papers. Well-balanced but barely over threshold. |
| PPI/network | 14/20 | Bipartite: centrosome + NER (XPC, RAD23B). |
| Structure/domain | 10/10 | High-res PDB; compact EF-hand; well-characterized. |
| Novelty/specificity | 7/10 | Dual role underappreciated. Small size (172 aa). |

- **Final centrosome score:** 76/100 (academic score only — overridden by PubMed elimination)

## 9. Final Decision

**CENTROSOME_ELIMINATED**

**Reason:** PubMed total = 111 (barely over the 100 threshold). CETN2 is the most TE-relevant centrosome protein in the pilot (direct NER function), but is eliminated by the PubMed > 100 rule. This is a borderline case — the NER literature inflates the count relative to centrosome-specific papers (55).

## 10. Manual Review Note

- Eliminated per PubMed > 100 rule. Borderline case at 111 papers.
- NER literature (XPC co-factor studies) accounts for ~50% of publications — functionally distinct from centrosome biology
- If threshold considers only centrosome-specific papers (55), CETN2 would be a top CANDIDATE
- Recommended: flag for potential re-evaluation if PubMed threshold is refined to exclude non-centrosome literature
