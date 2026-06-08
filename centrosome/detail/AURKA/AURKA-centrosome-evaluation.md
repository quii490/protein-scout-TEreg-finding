---
type: centrosome-protein-evaluation
gene: "AURKA"
module: centrosome
status: centrosome_low_priority
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# AURKA — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** O14965
- **Protein name:** Aurora kinase A (AURKA)
- **Synonyms:** AIK, ARK1, AURA, BTAK, STK15, STK6
- **Length:** 403 aa
- **Main atlas overlap:** Yes (status: rejected, category: rejected — PubMed > 100)
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000087586-AURKA
- **HPA reliability:** Approved (HPA + UniProt)
- **HPA location text:** Centrosome
- **IF image status:** Available (HPA IF images show centrosome localization during mitosis)

AURKA is one of the most well-documented centrosome proteins. It localizes to centrosomes and spindle poles during mitosis. HPA IF images consistently show punctate perinuclear staining characteristic of centrosome localization.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, spindle pole, spindle microtubule, cilium basal body
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0036064 (ciliary basal body) — IDA
  - GO:0000922 (spindle pole) — IDA
- **Notes:** Highly confident centrosome localization. AURKA is the prototypical centrosome kinase, recruited to centrosomes in G2/M.

## 4. PubMed Evidence

- **Total PubMed:** 3,081 papers
- **Strict query (centrosome/centriole):** 384 papers
- **Broad query (centrosome/cilia/cell cycle/DNA damage):** 1,665 papers
- **Key papers:**
  - Glover DM et al. (1995) — Discovery of aurora kinase family in Drosophila; PMID: 7606778
  - Bischoff JR et al. (1998) — Human AURKA cloning and centrosome localization; PMID: 9467949
  - Nikonova AS et al. (2013) — AURKA in ciliary resorption and cell cycle; PMID: 23169530
- **Alias contamination note:** AURKA has many synonyms (STK6, STK15, BTAK, ARK1). All verified as same gene product.
- **Assessment:** Extremely well-studied. Very high PubMed count (>3,000). This limits novelty for TEreg discovery.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** High overall confidence (canonical isoform well-folded)
- **PAE:** Available — kinase domain well-packed; N-terminal regulatory domain has some flexibility
- **PDB:** Extensive coverage (100+ structures). Key structures:
  - 1MQ4 (kinase domain + ATP)
  - 3E5A (kinase domain + TPX2 peptide)
  - 5LX9 (kinase domain + inhibitor)
- **InterPro / Pfam / SMART:**
  - IPR000719: Protein kinase domain (Pfam: PF00069)
  - IPR008271: Serine/threonine-protein kinase, active site
  - IPR030616: Aurora kinase
- **Domain notes:** Two-domain architecture: N-terminal regulatory domain (~130 aa) + C-terminal serine/threonine kinase domain. The N-terminal domain mediates centrosome targeting via AURKA-A (AURKA activation domain). High structural coverage; multiple inhibitor-bound structures available.

## 6. PPI / humanPPI

- **STRING:** Rich interaction network (well-established interactors including TPX2, BORA, CEP192, PLK1, INCENP, NEDD1)
- **IntAct:** 100+ binary interactions curated
- **BioGRID:** Extensive genetic and physical interaction data
- **humanPPI:** Available — multiple centrosome/kinase partners
- **Centrosome-related interactors:**
  - TPX2 (activator, centrosome/spindle)
  - CEP192 (centrosome scaffold)
  - NEDD1 (γ-TuRC targeting)
  - PLK1 (mitotic kinase, centrosome maturation partner)
  - BORA (AURKA activator)

## 7. TE-Regulator Relevance

- **Evidence:**
  - AURKA phosphorylates histone H3 at Ser10 during mitosis — direct chromatin modification
  - AURKA regulates ciliary dynamics (ciliogenesis/ciliary resorption), linking centrosome to signaling
  - AURKA overexpression causes centrosome amplification → aneuploidy → genome instability
  - AURKA interacts with BRCA1 in DNA damage response (DDR) pathways
  - AURKA regulates PLK1 → cell cycle checkpoints relevant to TE-induced DNA damage response
- **Strength:** Moderate indirect connection. AURKA's chromatin link is strong (H3S10ph), but its direct TE biology relevance is not established. Genome instability connection is well-documented but indirect for TE regulation specifically.
- **Caveats:** The TE relevance chain requires: centrosome amplification → genome instability → TE activation. This is a two-step inference.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 20/20 | HPA seed + UniProt + GO-CC + extensive literature. Gold-standard centrosome protein. |
| TE relevance | 8/20 | H3S10 phosphorylation (chromatin mark); genome instability link. Indirect but plausible. |
| PubMed/literature | 5/20 | 3,081 papers total. Extremely well-studied. Centrosome literature rich but novelty low. |
| PPI/network | 20/20 | Extensive PPI network; multiple centrosome-kinase partners; high-confidence interactors. |
| Structure/domain | 10/10 | 100+ PDB structures; high pLDDT; well-characterized kinase domain; drug targets available. |
| Novelty/specificity | 2/10 | Very highly studied. Not novel. Centrosome specificity high during mitosis but also spindle/cilia. |

- **Raw score:** (20×4) + (8×5) + (5×4) + (20×3) + (10×2) + (2×2) = 80 + 40 + 20 + 60 + 20 + 4 = 224
- **Final centrosome score:** 224 / 3.6 = **62/100**

## 9. Final Decision

**CENTROSOME_LOW_PRIORITY**

**Reason:** AURKA is the canonical centrosome kinase with the best-possible centrosome evidence. However, it has extremely high publication volume (3,081 papers), severely limiting novelty. The TE relevance connection is indirect (via chromatin phosphorylation and genome instability). While it could serve as a positive control for centrosome methods, it is not a high-priority TEreg candidate due to over-study and indirect TE biology.

## 10. Manual Review Note

- Main atlas status: rejected (PubMed > 100)
- Centrosome module uses independent scoring — AURKA's exclusion from the main atlas candidate list was due to high publication volume (>100 papers), not subcellular localization
- Could be included in a "centrosome reference set" for benchmarking but not as a discovery target
- Recommended follow-up: consider AURKA inhibitors as tools for centrosome biology experiments rather than as a TEreg target
