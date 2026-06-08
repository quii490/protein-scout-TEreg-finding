---
type: centrosome-protein-evaluation
gene: "CEP97"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP97 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q8IW35
- **Protein name:** Centrosomal protein of 97 kDa (CEP97)
- **Synonyms:** FLJ31735, MGC125823
- **Length:** 865 aa
- **Main atlas overlap:** No (not in main atlas)
- **HPA seed source:** Both (Centrosome + Centriolar satellite)

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓ + Centriolar satellite ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000182504-CEP97
- **HPA reliability:** Approved
- **HPA location text:** Centrosome, centriolar satellite
- **IF image status:** Available

Dual HPA annotation provides strong independent centrosome validation. CEP97 forms a stoichiometric complex with CCP110 (also in pilot set).

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, centriole, centriolar satellite, cilium basal body
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0034451 (centriolar satellite) — IDA
  - GO:0036064 (ciliary basal body) — IDA
- **Notes:** CEP97 is the obligate binding partner of CCP110. Together they form the centriole distal-end cap complex that suppresses ciliogenesis.

## 4. PubMed Evidence

- **Total PubMed:** 43 papers
- **Strict query (centrosome/centriole):** 36 papers
- **Broad query:** 39 papers
- **Key papers:**
  - Spektor A et al. (2007) — CEP97-CP110 complex in centriole capping and ciliogenesis; PMID: 17646409
  - Tsang WY et al. (2008) — CEP97 in centriole length control; PMID: 18694559
  - Kobayashi T et al. (2014) — CEP97 degradation in ciliogenesis regulation; PMID: 25232968
- **Alias contamination note:** No significant alias contamination. Well-defined gene.
- **Assessment:** 43 papers total. Excellent volume — characterized enough to be confident in biology but not over-studied. Very high centrosome specificity (84%).

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate (865 aa)
- **PAE:** Available — structured domains with flexibility
- **PDB:** None (no experimental structures)
- **InterPro / Pfam / SMART:**
  - IPR048484: CEP97, C-terminal domain
  - Leucine-rich repeat (LRR) domains (predicted)
  - Coiled-coil regions (predicted)
- **Domain notes:** CEP97 has an N-terminal LRR-like domain and a conserved C-terminal domain. LRR architecture is shared with CCP110 partner and may mediate protein-protein interactions in the centriole cap complex. No catalytic domains — scaffolding/adaptor function. Limited structural data.

## 6. PPI / humanPPI

- **STRING:** Good interaction network centered on CCP110 complex
- **IntAct:** Curated interactions
- **BioGRID:** Physical interactions
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - CCP110/CP110 (stoichiometric partner, centriole cap)
  - CEP290 (ciliopathy protein)
  - KIF24 (centriolar kinesin)
  - CEP76 (centriole duplication)
  - TALPID3 (ciliogenesis)
  - CUL3-RBX1 (E3 ubiquitin ligase — mediates CEP97 degradation during ciliogenesis)

## 7. TE-Regulator Relevance

- **Evidence:**
  - CEP97-CCP110 complex suppresses ciliogenesis by capping centriole distal ends — removal of this cap triggers ciliogenesis
  - CEP97 degradation (via CUL3-RBX1 E3 ligase) is required for ciliogenesis initiation — links to ubiquitin-proteasome system, relevant for TE-derived protein degradation
  - Ciliogenesis couples to cell cycle exit and differentiation — pathways that regulate developmental TE silencing
  - CEP97 is a PLK1 phosphorylation target — kinase linked to cell cycle and chromatin
  - CEP97 interacts with CEP290 — CEP290 has nuclear/nucleolar roles in addition to centrosome functions
  - The ubiquitin-mediated degradation of CEP97 provides a "switch" mechanism — similar regulatory logic to TE silencing (rapid ON/OFF)
- **Strength:** Moderate. The ciliogenesis gatekeeper function is well-defined. Ubiquitin regulation and CEP290 connection provide additional TE-relevant links.
- **Caveats:** Primarily a structural centrosome protein. TE relevance is through ciliogenesis and degradation pathways.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 19/20 | Dual HPA source + UniProt + GO-CC. Ciliogenesis gatekeeper. High-confidence centrosome protein. |
| TE relevance | 7/20 | Ciliogenesis ↔ differentiation; ubiquitin-mediated degradation switch; CEP290 connection. |
| PubMed/literature | 10/20 | 43 papers. Ideal for discovery. 84% centrosome-specific. Excellent target volume. |
| PPI/network | 15/20 | CCP110 stoichiometric complex; CUL3 ubiquitin ligase; centriole cap interactome. |
| Structure/domain | 5/10 | LRR + C-terminal domain. No PDB. Moderate pLDDT. |
| Novelty/specificity | 8/10 | Not in main atlas. Dual HPA source. 43 papers. Highest centrosome specificity in pilot. |

- **Raw score:** (19×4) + (7×5) + (10×4) + (15×3) + (5×2) + (8×2) = 76 + 35 + 40 + 45 + 10 + 16 = 222
- **Final centrosome score:** 222 / 3.6 = **62/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** CEP97 is a high-confidence centrosome protein with dual HPA source annotation. Forms a stoichiometric complex with CCP110 (also a pilot candidate). Low publication volume (43 papers) with very high centrosome specificity. The ciliogenesis gatekeeper function and ubiquitin-mediated degradation provide interesting TE-relevant biology. Not in main atlas.

## 10. Manual Review Note

- Not in main atlas — new target for centrosome module
- CEP97 + CCP110 form a defined complex — evaluating both together increases confidence
- CUL3-RBX1-mediated degradation is a druggable pathway — potential for chemical biology approaches
- Consider CEP97 as part of a "centriole cap sub-module" with CCP110, CEP290, and KIF24
- The degradation switch mechanism is conceptually similar to TE silencing — rapid ON/OFF via ubiquitination
