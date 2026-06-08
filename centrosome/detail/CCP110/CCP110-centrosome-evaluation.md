---
type: centrosome-protein-evaluation
gene: "CCP110"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CCP110 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** O75939
- **Protein name:** Centriolar coiled-coil protein of 110 kDa (CCP110)
- **Synonyms:** CP110, CEP110, KIAA0419
- **Length:** 1,012 aa
- **Main atlas overlap:** Yes (status: rejected, category: rejected)
- **HPA seed source:** Centriolar satellite

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centriolar satellite ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000103540-CCP110
- **HPA reliability:** Approved
- **HPA location text:** Centriolar satellite, centriole
- **IF image status:** Available — centrosome/satellite puncta

CCP110 (CP110) caps the distal end of centrioles and regulates centriole length. HPA IF shows centrosome puncta. It also localizes to centriolar satellites.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centriole, centriolar satellite, centrosome, cilium
- **GO-CC terms:**
  - GO:0005814 (centriole) — IDA
  - GO:0005813 (centrosome) — IDA
  - GO:0034451 (centriolar satellite) — IDA
  - GO:0036064 (ciliary basal body) — IDA
  - GO:0097542 (ciliary tip) — IDA
- **Notes:** CCP110 is a centriole distal-end cap protein. Critical suppressor of ciliogenesis. Removed from centrioles during ciliogenesis, allowing axoneme extension.

## 4. PubMed Evidence

- **Total PubMed:** 77 papers
- **Strict query (centrosome/centriole):** 61 papers
- **Broad query:** 71 papers
- **Key papers:**
  - Chen Z et al. (2002) — CP110 as centriole distal-end cap; PMID: 11978807
  - Spektor A et al. (2007) — CP110 suppresses ciliogenesis; PMID: 17646409
  - Tsang WY et al. (2008) — CP110-CEP97 complex in centriole length control; PMID: 18694559
  - Yadav SP et al. (2016) — CP110-CEP290 interaction in ciliogenesis; PMID: 27527997
- **Alias contamination note:** CP110 and CCP110 are the same gene. Also CEP110. Minimal contamination.
- **Assessment:** 77 papers total. Highly centrosome-specific (79%). Excellent target volume — well-characterized but not over-studied.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate (1,012 aa)
- **PAE:** Available — N-terminal coiled-coil domains; C-terminal cyclin-like domain
- **PDB:** Limited
- **InterPro / Pfam / SMART:**
  - Coiled-coil regions (N-terminal)
  - IPR046963: CCP110, C-terminal cyclin-like domain
  - Multiple CDK phosphorylation sites
- **Domain notes:** N-terminal region mediates centriole capping and CEP97 binding. C-terminal cyclin-like domain is atypical — not a true cyclin but structurally similar. CDK/PLK phosphorylation regulates ciliogenesis function.

## 6. PPI / humanPPI

- **STRING:** Good centriole interaction network
- **IntAct:** Curated interactions
- **BioGRID:** Physical interactions
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - CEP97 (stoichiometric partner, centriole cap complex)
  - CEP290 (ciliopathy protein, ciliogenesis)
  - CEP104 (centriole elongation)
  - KIF24 (kinesin, centriole disassembly)
  - CEP76 (centriole duplication)
  - TALPID3 (ciliogenesis)

## 7. TE-Regulator Relevance

- **Evidence:**
  - CCP110 caps centrioles and prevents ciliogenesis — directly controls the centrosome-to-cilium transition
  - Ciliogenesis is coupled to cell cycle exit and differentiation programs — pathways that regulate TE silencing during development
  - CCP110 removal from centrioles is driven by TTBK2/MARK4 phosphorylation — kinases linked to chromatin regulation
  - CCP110 interacts with CEP290, a protein also involved in DNA damage response and transcription regulation
  - Centriole length control by CCP110 may affect the centriole's role in DNA damage signaling
  - CCP110 is a CDK2 substrate — couples centriole biology to cell cycle, linking to cell cycle-dependent TE regulation
- **Strength:** Moderate. The ciliogenesis connection ties to developmental TE silencing. Centriole-DNA damage connection is less explored.
- **Caveats:** CCP110 is primarily a structural centriole cap. Its TE relevance is through cell cycle/ciliogenesis pathways rather than direct TE biology.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 19/20 | Core centriole cap protein. HPA + UniProt + GO-CC. Ciliogenesis gatekeeper. |
| TE relevance | 7/20 | Ciliogenesis ↔ differentiation ↔ TE silencing. CDK2 link to cell cycle TE regulation. |
| PubMed/literature | 10/20 | 77 papers. Ideal volume — characterized without over-study. 79% centrosome-specific. |
| PPI/network | 15/20 | CEP97 complex; CEP290; KIF24; centriole disassembly pathway. Distinct centriole cap network. |
| Structure/domain | 6/10 | Coiled-coil + cyclin-like domain. Moderate pLDDT. Limited PDB. |
| Novelty/specificity | 7/10 | Centriole-specific. Not in nuclear- or chromatin-focused literature. Rejected in main atlas but centrosome-relevant. |

- **Raw score:** (19×4) + (7×5) + (10×4) + (15×3) + (6×2) + (7×2) = 76 + 35 + 40 + 45 + 12 + 14 = 222
- **Final centrosome score:** 222 / 3.6 = **62/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** CCP110 is a well-characterized centriole cap protein with moderate publication volume and high centrosome specificity. Not a candidate in the main atlas (primarily due to predominantly cytoplasmic/centrosome localization outside the main atlas scope). The ciliogenesis/cell cycle connection provides a pathway to TE-relevant biology.

## 10. Manual Review Note

- Main atlas status: not a candidate — likely due to predominantly cytoplasmic/centrosome localization. Centrosome module evaluates independently.
- CCP110-CEP97 complex is a key regulatory node for ciliogenesis — tool compounds targeting this complex may be useful
- Consider: does CCP110 removal during ciliogenesis trigger DNA damage signaling relevant to TE activation?
