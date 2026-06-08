---
type: centrosome-protein-evaluation
gene: "CEP192"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP192 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q8TEP8
- **Protein name:** Centrosomal protein of 192 kDa (CEP192)
- **Synonyms:** KIAA1569, PPP1R62
- **Length:** 2,537 aa
- **Main atlas overlap:** No (not in main atlas)
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000101639-CEP192
- **HPA reliability:** Approved
- **HPA location text:** Centrosome
- **IF image status:** Available — centrosomal puncta

CEP192 is a large scaffolding protein essential for centrosome maturation and mitotic spindle assembly. HPA IF shows clear centrosome localization.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, spindle pole
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0000922 (spindle pole) — IDA
  - GO:0043005 (pericentriolar material) — inferred
- **Notes:** CEP192 serves as a scaffold for PLK1 and AURKA recruitment during centrosome maturation. Strong centrosome evidence.

## 4. PubMed Evidence

- **Total PubMed:** 101 papers
- **Strict query (centrosome/centriole):** 86 papers
- **Broad query:** 90 papers
- **Key papers:**
  - Gomez-Ferreria MA et al. (2007) — CEP192 discovery and centrosome localization; PMID: 17980596
  - Zhu F et al. (2008) — CEP192 role in mitotic centrosome/spindle assembly; PMID: 18207742
  - Joukov V et al. (2014) — CEP192-AURKA-PLK1 cascade at centrosomes; PMID: 25090921
- **Alias contamination note:** Minimal alias risk. Previously KIAA1569. All verified.
- **Assessment:** Moderate publication volume (101 papers). Highly centrosome-specific (85% of papers are centrosome-related). Good balance of characterization without over-study.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate — large protein (2,537 aa) with some disordered regions
- **PAE:** Available — structured domains with flexible linker regions
- **PDB:** Limited experimental structures (fragments only)
- **InterPro / Pfam / SMART:**
  - Multiple coiled-coil regions (predicted)
  - No classical enzymatic domains — scaffolding protein
- **Domain notes:** Predominantly coiled-coil architecture. Multiple phosphorylation sites (AURKA, PLK1 substrates). N-terminal region interacts with AURKA; C-terminal region with PLK1. Large size (2,537 aa) makes it structurally challenging but functionally informative as a scaffold.

## 6. PPI / humanPPI

- **STRING:** Strong centrosome interaction network
- **IntAct:** Multiple curated interactions
- **BioGRID:** Physical interactions available
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - AURKA (centrosome kinase client)
  - PLK1 (centrosome kinase client)
  - PLK4 (centriole kinase)
  - CEP152 (centriole scaffold)
  - NEDD1 (γ-TuRC targeting factor)
  - PCNT (pericentrin, PCM scaffold)

## 7. TE-Regulator Relevance

- **Evidence:**
  - CEP192-mediated centrosome maturation regulates mitotic fidelity
  - Disruption of CEP192 → spindle defects → chromosome missegregation → genome instability
  - CEP192 interacts with AURKA and PLK1 — kinases that regulate chromatin modification (H3S10ph, H3T3ph)
  - CEP192 depletion causes p53 activation — DNA damage response pathway relevant to TE surveillance
  - As a large scaffold, CEP192 may have uncharacterized nuclear roles
- **Strength:** Moderate. The genome instability link via spindle defects is direct. TE relevance is indirect through genome integrity pathways.
- **Caveats:** No direct TE interaction evidence. Scaffolding proteins can have moonlighting functions not yet characterized.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 20/20 | HPA + UniProt + GO-CC + 86 centrosome-specific papers. Core PCM scaffold. |
| TE relevance | 6/20 | Genome instability via spindle defects. Indirect TE connection. |
| PubMed/literature | 10/20 | 101 papers, well-balanced. 85% centrosome-specific. Good characterization without over-study. |
| PPI/network | 18/20 | Scaffold for AURKA/PLK1/PLK4. Central position in the centrosome maturation hierarchy. |
| Structure/domain | 5/10 | Large coiled-coil scaffold; limited PDB; moderate pLDDT. Scaffold nature limits structural resolution. |
| Novelty/specificity | 6/10 | Moderately studied. Not in main atlas. Centrosome-specific. Good size for biochemical study (though large). |

- **Raw score:** (20×4) + (6×5) + (10×4) + (18×3) + (5×2) + (6×2) = 80 + 30 + 40 + 54 + 10 + 12 = 226
- **Final centrosome score:** 226 / 3.6 = **63/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** CEP192 is a core centrosome scaffold with strong evidence. Not in main atlas (new protein). Good publication volume (101 papers) — characterized but not over-studied. Central position in centrosome maturation kinase hierarchy makes it an excellent reference for understanding centrosome-PPI in the context of genome stability and potential TE regulation. The scaffold nature (large coiled-coil) provides many potential interaction surfaces.

## 10. Manual Review Note

- Not in main atlas — this is a "discovery" for the centrosome module
- Large protein (2,537 aa) — cloning and expression may be challenging
- Scaffold protein — may be challenging for traditional biochemical assays but excellent for proximity-labeling approaches
- Consider CEP192 as a "bait" for centrosome interactome mapping via BioID/APEX
