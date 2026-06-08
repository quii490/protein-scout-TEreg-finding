---
type: centrosome-protein-evaluation
gene: "CCDC14"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CCDC14 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q49A88
- **Protein name:** Coiled-coil domain-containing protein 14 (CCDC14)
- **Synonyms:** FLJ30058, MGC131864
- **Length:** 954 aa
- **Main atlas overlap:** No (not in main atlas)
- **HPA seed source:** Centriolar satellite

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centriolar satellite ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000175448-CCDC14
- **HPA reliability:** Supported (RNA + protein evidence)
- **HPA location text:** Centriolar satellite
- **IF image status:** Available — satellite-like puncta

CCDC14 is a poorly characterized coiled-coil protein annotated as centriolar satellite by HPA. Very limited functional literature.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Cytoplasm, centriolar satellite (by HPA annotation)
- **GO-CC terms:**
  - GO:0005813 (centrosome) — inferred from HPA/Direct assay
  - GO:0005737 (cytoplasm) — IBA (Inferred from Biological aspect of Ancestor)
- **Notes:** Limited experimental centrosome evidence beyond HPA annotation. No functional centrosome studies. This is a discovery-stage protein.

## 4. PubMed Evidence

- **Total PubMed:** 7 papers
- **Strict query (centrosome/centriole):** 3 papers
- **Broad query:** 4 papers
- **Key papers:**
  - No dedicated functional studies of CCDC14
  - May be mentioned in large-scale proteomic or localization screens
  - HPA annotation is the primary centrosome evidence
- **Alias contamination note:** Minimal literature — no alias issues.
- **Assessment:** Extremely novel. Only 7 total papers, none functionally characterizing CCDC14. This is the most novel gene in the pilot set. High risk, high potential reward.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Low to moderate (954 aa, significant disorder predicted)
- **PAE:** Available — some structured domains, extensive flexibility
- **PDB:** None
- **InterPro / Pfam / SMART:**
  - Predominantly coiled-coil architecture
  - No annotated Pfam/SMART domains
  - No catalytic motifs identified
- **Domain notes:** CCDC14 is a predicted coiled-coil protein with no annotated functional domains. The coiled-coil architecture suggests a scaffolding/structure role. Low pLDDT in terminal regions suggests intrinsic disorder — may indicate conditional folding or binding-induced structure.

## 6. PPI / humanPPI

- **STRING:** Sparse interaction network (few high-confidence partners)
- **IntAct:** No curated interactions
- **BioGRID:** No physical interactions
- **humanPPI:** Not available / No entries
- **Centrosome-related interactors:** Unknown
- **Notes:** Very limited PPI data. This is expected for an uncharacterized protein. PPI data absence should not be interpreted as biological absence of interactions — simply reflects lack of study.

## 7. TE-Regulator Relevance

- **Evidence:**
  - No direct TE-relevant publications
  - Coiled-coil architecture is common in DNA-binding and chromatin-associated proteins — structural similarity to known TE regulators (e.g., KRAB-ZNF scaffold proteins, SMC complexes)
  - CCDC family members have been implicated in DNA repair (CCDC98/Abraxas in BRCA1 complex) — family precedent for genome stability roles
  - Centriolar satellite localization suggests potential centrosome-nucleus trafficking (satellites are dynamic, can shuttle proteins)
- **Strength:** Low. Nearly all TE-relevance reasoning is inferential. This is a true "discovery" gene.
- **Caveats:** Being uncharacterized, CCDC14 could have any function. The TE relevance assessment is speculative. This is a high-risk, high-reward candidate.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 6/20 | HPA satellite annotation only. Limited independent centrosome evidence. No functional studies. |
| TE relevance | 3/20 | Speculative. Coiled-coil structural similarity to chromatin proteins. No direct evidence. |
| PubMed/literature | 6/20 | Only 7 papers total. Extremely novel. The sparsity itself is interesting for discovery. |
| PPI/network | 2/20 | No annotated PPI. Sparse STRING. No humanPPI. Complete PPI darkness. |
| Structure/domain | 3/10 | Coiled-coil only. No PDB. Low pLDDT in regions. No annotated domains. |
| Novelty/specificity | 10/10 | Most novel gene in pilot set. 7 papers, no functional studies. Maximum discovery potential. |

- **Raw score:** (6×4) + (3×5) + (6×4) + (2×3) + (3×2) + (10×2) = 24 + 15 + 24 + 6 + 6 + 20 = 95
- **Final centrosome score:** 95 / 3.6 = **26/100**

## 9. Final Decision

**CENTROSOME_MANUAL_REVIEW**

**Reason:** CCDC14 is the most novel gene in the pilot set (7 total papers) but scores low due to limited evidence across all dimensions except novelty. Centrosome evidence is weak (HPA satellite only). PPI data essentially absent. TE relevance is entirely speculative. However, the extreme novelty combined with satellite localization makes it an interesting discovery candidate. Manual review needed to decide whether to invest in experimental characterization.

## 10. Manual Review Note

- Not in main atlas — complete discovery
- CCDC14 has the "dark proteome" problem: minimal literature, no PPI, no domains
- Recommendation: defer to full centrosome evaluation. Include as MANUAL_REVIEW to flag for expert assessment.
- Could be a false positive satellite annotation — HPA satellite annotation may need independent validation
- If pursuing: start with localization validation (IF) and proximity labeling (BioID) to identify interactors
- The risk/reward profile: if CCDC14 is real and relevant, it would be the most impactful discovery. If a false positive, it's a waste of resources.
- Balance: 90% chance of false positive, 10% chance of breakthrough — typical for ultra-novel candidates
