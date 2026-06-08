---
type: centrosome-protein-evaluation
gene: "AURKA"
module: centrosome
status: centrosome_eliminated
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# AURKA — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** O14965
- **Protein name:** Aurora kinase A (AURKA)
- **Synonyms:** AIK, ARK1, AURA, BTAK, STK15, STK6
- **Length:** 403 aa
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000087586-AURKA
- **HPA reliability:** Supported (IF)
- **HPA location text:** Centrosome, mitotic spindle, basal body
- **IF image:** Available (see below)

![[AURKA_IF_1.jpg]]

AURKA is one of the most well-documented centrosome proteins. It localizes to centrosomes and spindle poles during mitosis. HPA IF images consistently show punctate perinuclear staining characteristic of centrosome localization.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, spindle pole, spindle microtubule, cilium basal body
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0036064 (ciliary basal body) — IDA
  - GO:0000922 (spindle pole) — IDA
- **Notes:** Highly confident centrosome localization. AURKA is the prototypical centrosome kinase.

## 4. PubMed Evidence

- **Total PubMed:** 3,081 papers ⚠️ **EXCEEDS THRESHOLD (>100)**
- **Strict query (centrosome/centriole):** 384 papers
- **Broad query (centrosome/cilia/cell cycle/DNA damage):** 1,665 papers
- **Key papers:**
  - Glover DM et al. (1995) — Discovery of aurora kinase family; PMID: 7606778
  - Bischoff JR et al. (1998) — Human AURKA cloning and centrosome localization; PMID: 9467949
  - Nikonova AS et al. (2013) — AURKA in ciliary resorption; PMID: 23169530
- **Alias contamination note:** Many synonyms (STK6, STK15, BTAK, ARK1). All verified.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** High (kinase domain well-folded)
- **PAE:** Available
- **PDB:** 100+ structures (1MQ4, 3E5A, 5LX9)
- **InterPro:** IPR000719 Protein kinase, IPR008271 Ser/Thr kinase, IPR030616 Aurora kinase
- **Domain notes:** N-terminal regulatory (~130 aa) + C-terminal kinase domain

## 6. PPI / humanPPI

- **STRING:** Rich network (TPX2, BORA, CEP192, PLK1, INCENP, NEDD1)
- **IntAct:** 100+ interactions
- **BioGRID:** Extensive
- **Key centrosome interactors:** TPX2, CEP192, NEDD1, PLK1, BORA

## 7. TE-Regulator Relevance

- H3S10 phosphorylation (chromatin mark)
- Ciliary dynamics regulation
- Centrosome amplification → genome instability → TE activation
- BRCA1 interaction in DDR pathways
- **Strength:** Indirect, multi-step inference

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 20/20 | Gold-standard centrosome kinase. HPA + UniProt + GO-CC. |
| TE relevance | 8/20 | H3S10 phosphorylation; genome instability. Indirect. |
| PubMed/literature | 5/20 | 3,081 papers total. Over-studied. |
| PPI/network | 20/20 | Extensive PPI; multiple centrosome partners. |
| Structure/domain | 10/10 | 100+ PDB structures; drug targets available. |
| Novelty/specificity | 2/10 | Very highly studied. Not novel. |

- **Final centrosome score:** 65/100 (academic score only — overridden by PubMed elimination)

## 9. Final Decision

**CENTROSOME_ELIMINATED**

**Reason:** PubMed total = 3,081 (>100 threshold). AURKA is the most-studied centrosome protein. Despite impeccable centrosome biology, it is eliminated from centrosome discovery list due to over-study.

## 10. Manual Review Note

- Eliminated per PubMed > 100 rule (same as main atlas)
- Could serve as a centrosome reference/positive control for method validation, but not as a discovery target
- AURKA inhibitors (alisertib, etc.) may be useful as chemical tools for centrosome biology experiments
