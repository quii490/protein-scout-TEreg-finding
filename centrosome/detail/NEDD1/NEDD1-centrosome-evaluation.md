---
type: centrosome-protein-evaluation
gene: "NEDD1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# NEDD1 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q8NHV4
- **Protein name:** Neural precursor cell expressed developmentally down-regulated protein 1 (NEDD1)
- **Synonyms:** GCP-WD, TUBGCP7
- **Length:** 660 aa
- **Main atlas overlap:** Yes (status: scored, category: nucleolus)
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000139350-NEDD1
- **HPA reliability:** Approved
- **HPA location text:** Centrosome
- **IF image status:** Available — centrosome puncta

NEDD1 is a WD-repeat protein that targets γ-tubulin ring complex (γ-TuRC) to centrosomes and spindle microtubules. HPA IF shows clear centrosome localization.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, spindle, spindle pole
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0000922 (spindle pole) — IDA
  - GO:0005874 (microtubule) — IDA
- **Notes:** NEDD1 is the primary adaptor for γ-TuRC (γ-tubulin ring complex) recruitment to centrosomes. Essential for microtubule nucleation at centrosomes.

## 4. PubMed Evidence

- **Total PubMed:** 79 papers
- **Strict query (centrosome/centriole):** 49 papers
- **Broad query:** 72 papers
- **Key papers:**
  - Haren L et al. (2006) — NEDD1-dependent recruitment of γ-tubulin to centrosomes; PMID: 16814769
  - Luders J et al. (2006) — NEDD1/GCP-WD mediates γ-TuRC attachment to mitotic spindle; PMID: 16371599
  - Zhang X et al. (2009) — NEDD1 regulation by CDK1 and PLK1; PMID: 19376971
- **Alias contamination note:** Also known as GCP-WD, TUBGCP7. No significant contamination.
- **Assessment:** Well-characterized, moderate volume (79 papers). Highly centrosome-specific (62%). Excellent balance.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Good overall confidence (660 aa)
- **PAE:** Available — WD40 β-propeller well-packed; N-terminal coiled-coil moderate
- **PDB:** Limited (fragments)
- **InterPro / Pfam / SMART:**
  - IPR001680: WD40 repeat (Pfam: PF00400)
  - IPR015943: WD40/YVTN repeat-like domain
  - N-terminal coiled-coil region (predicted)
- **Domain notes:** N-terminal coiled-coil mediates NEDD1 oligomerization and γ-TuRC binding. C-terminal WD40 β-propeller (~7 blades predicted). Multi-site phosphorylation by CDK1, PLK1, Nek9 regulates centrosome targeting.

## 6. PPI / humanPPI

- **STRING:** Good centrosome/MT interaction network
- **IntAct:** Curated interactions available
- **BioGRID:** Physical interactions
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - γ-Tubulin (TUBG1, TUBG2) — direct γ-TuRC component binding
  - PLK1 (mitotic kinase, phosphorylation)
  - CDK1 (cell cycle kinase, phosphorylation)
  - CEP192 (upstream scaffold)
  - Augmin complex (HAUS proteins, spindle MT nucleation)

## 7. TE-Regulator Relevance

- **Evidence:**
  - NEDD1 links centrosome microtubule nucleation to spindle assembly — critical for chromosome segregation fidelity
  - NEDD1 phosphorylation by CDK1 couples centrosome function to cell cycle progression
  - γ-TuRC (NEDD1's complex) is also involved in DNA damage-induced microtubule reorganization
  - Recent evidence: centrosome-nucleated microtubules contribute to nuclear envelope rupture repair — relevant to genome stability
  - NEDD1 is a target of the E3 ligase MIB1 — proteasomal regulation links to protein homeostasis pathways relevant for TE-derived protein surveillance
- **Strength:** Moderate. The microtubule nucleation → chromosome segregation → genome stability chain is well-defined but TE connection is indirect.
- **Caveats:** Name "NEDD1" originates from neural development context — not centrosome literature. Gene symbol confusion possible.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 19/20 | HPA + UniProt + GO-CC + functional literature. γ-TuRC adaptor role well-established. |
| TE relevance | 6/20 | Genome stability via chromosome segregation; DNA damage MT reorganization. Indirect. |
| PubMed/literature | 10/20 | 79 papers. Well-characterized. 62% centrosome-specific. Good size for a research target. |
| PPI/network | 16/20 | γ-TuRC component; PLK1/CDK1 substrate; CEP192 downstream. MT nucleation hub. |
| Structure/domain | 7/10 | WD40 β-propeller + coiled-coil. Good pLDDT. Limited PDB. |
| Novelty/specificity | 7/10 | Moderately studied; not over-studied. Centrosome-specific. Moderate size (660 aa) good for experiments. |

- **Raw score:** (19×4) + (6×5) + (10×4) + (16×3) + (7×2) + (7×2) = 76 + 30 + 40 + 48 + 14 + 14 = 222
- **Final centrosome score:** 222 / 3.6 = **62/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** NEDD1 is a well-characterized centrosome protein with clear functional role (γ-TuRC adaptor). Moderate publication volume, good centrosome specificity, and tractable size for experiments. The γ-TuRC connection provides a unique angle: microtubule nucleation at centrosomes as a potential TE-relevant mechanism.

## 10. Manual Review Note

- Main atlas status: scored (nucleolus) — NEDD1 may have nucleolar localization in addition to centrosome
- 660 aa is experimentally tractable for cloning and biochemical characterization
- WD40 domain could be used for structural studies or as a drug target
- Consider screening NEDD1 interactors for uncharacterized centrosome-TE connections
