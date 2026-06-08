---
type: centrosome-protein-evaluation
gene: "CEP192"
module: centrosome
status: centrosome_eliminated
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# CEP192 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q8TEP8
- **Protein name:** Centrosomal protein of 192 kDa (CEP192)
- **Synonyms:** KIAA1569, PPP1R62
- **Length:** 2,537 aa
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000101639-CEP192
- **HPA reliability:** Uncertain (IF)
- **HPA location text:** Centrosome, basal body, cytosol
- **IF image:** Available

![[CEP192_IF_1.jpg]]

CEP192 is a large scaffolding protein essential for centrosome maturation and mitotic spindle assembly.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, spindle pole
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0000922 (spindle pole) — IDA
  - GO:0043005 (pericentriolar material) — inferred
- **Notes:** Scaffold for PLK1 and AURKA recruitment during centrosome maturation.

## 4. PubMed Evidence

- **Total PubMed:** 101 papers ⚠️ **EXCEEDS THRESHOLD (>100)**
- **Strict query (centrosome/centriole):** 86 papers
- **Broad query:** 90 papers
- **Key papers:**
  - Gomez-Ferreria MA et al. (2007) — CEP192 discovery; PMID: 17980596
  - Zhu F et al. (2008) — CEP192 in mitotic centrosome assembly; PMID: 18207742
  - Joukov V et al. (2014) — CEP192-AURKA-PLK1 cascade; PMID: 25090921
- **Assessment:** 101 papers, barely over threshold. Highly centrosome-specific (85%).

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate (2,537 aa, disordered regions)
- **PAE:** Available
- **PDB:** Limited (fragments)
- **InterPro:** Multiple coiled-coil regions; no catalytic domains
- **Domain notes:** Large scaffolding protein. AURKA/PLK1 phosphorylation sites.

## 6. PPI / humanPPI

- **STRING:** Strong centrosome network
- **IntAct:** Curated interactions
- **Key centrosome interactors:** AURKA, PLK1, PLK4, CEP152, NEDD1, PCNT

## 7. TE-Regulator Relevance

- Spindle defects → chromosome missegregation → genome instability
- AURKA/PLK1 scaffold — kinases regulating chromatin modification
- CEP192 depletion → p53 activation → DDR pathway
- **Strength:** Moderate indirect through genome integrity.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 20/20 | Core PCM scaffold. HPA + UniProt + GO-CC. |
| TE relevance | 6/20 | Genome instability via spindle defects. Indirect. |
| PubMed/literature | 10/20 | 101 papers. Good characterization but barely over threshold. |
| PPI/network | 18/20 | Central scaffold for AURKA/PLK1/PLK4 hierarchy. |
| Structure/domain | 5/10 | Large coiled-coil; limited PDB; moderate pLDDT. |
| Novelty/specificity | 6/10 | Moderately studied; centrosome-specific. |

- **Final centrosome score:** 65/100 (academic score only — overridden by PubMed elimination)

## 9. Final Decision

**CENTROSOME_ELIMINATED**

**Reason:** PubMed total = 101 (barely over the 100 threshold). CEP192 is a borderline case — excellent centrosome biology but technically over the elimination cutoff.

## 10. Manual Review Note

- Eliminated per PubMed > 100 rule. Borderline (101 papers).
- If threshold is relaxed to 150, CEP192 would be re-instated as CANDIDATE
- Large size (2,537 aa) makes experimental work challenging regardless
