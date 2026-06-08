---
type: centrosome-protein-evaluation
gene: "CEP72"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP72 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q9P209
- **Protein name:** Centrosomal protein of 72 kDa (CEP72)
- **Synonyms:** KIAA1519, FLJ10565
- **Length:** 647 aa
- **HPA seed source:** Both (Centrosome + Centriolar satellite)

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓ + Centriolar satellite ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000112877-CEP72
- **HPA reliability:** Approved
- **HPA location text:** Centrosome, centriolar satellite
- **IF image status:** Available

![[CEP72_IF_1.jpg]]

Dual HPA annotation (centrosome + centriolar satellite) provides strong independent validation of centrosome localization.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, centriole, centriolar satellite
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0034451 (centriolar satellite) — IDA
- **Notes:** Triple localization: centrosome + centriole + satellite. Consistent with a role at the centrosome-satellite interface. CEP72 has been implicated in ciliogenesis.

## 4. PubMed Evidence

- **Total PubMed:** 70 papers
- **Strict query (centrosome/centriole):** 22 papers
- **Broad query:** 49 papers
- **Key papers:**
  - Oshimori N et al. (2009) — CEP72 in centriole duplication; PMID: 19536135
  - Stowe TR et al. (2012) — CEP72-CEP63-CEP152 centriole assembly pathway; PMID: 22246249
  - Brown NJ et al. (2013) — CEP72 in ciliogenesis and Hedgehog signaling; PMID: 23774038
- **Alias contamination note:** No significant alias issues.
- **Assessment:** 70 papers total. Moderate volume. Centrosome-specific fraction is modest (22/70 = 31%). Some papers on non-centrosome functions may exist. Good balance for follow-up.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate to good (647 aa)
- **PAE:** Available — structured domains
- **PDB:** None (no experimental structures)
- **InterPro / Pfam / SMART:**
  - IPR039808: CEP72, C-terminal
  - Coiled-coil regions (predicted)
  - Leucine-rich repeat (LRR) domains (predicted)
- **Domain notes:** LRR domains are protein-protein interaction modules. CEP72 C-terminal domain is conserved in vertebrates. LRR architecture suggests a scaffold/adapter role rather than enzymatic function. Moderate structural characterization.

## 6. PPI / humanPPI

- **STRING:** Moderate interaction network
- **IntAct:** Limited curated interactions
- **BioGRID:** Physical interactions available
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - CEP63 (centriole duplication)
  - CEP152 (centriole scaffold)
  - CDK5RAP2 (centrosome maturation)
  - CEP76 (centriole duplication)
  - TALPID3 (ciliogenesis)

## 7. TE-Regulator Relevance

- **Evidence:**
  - CEP72 is linked to Hedgehog signaling through ciliogenesis (Brown et al., 2013) — Hedgehog pathway regulates stem cell maintenance and TE silencing during development
  - CEP72-CEP63-CEP152 pathway for centriole assembly — centriole number control linked to genome stability
  - LRR domains in CEP72 are structurally similar to LRR domains in nucleotide-binding proteins (NLRs, TLRs) — potential (speculative) nucleic acid sensing
  - CEP72 is a substrate of PLK1 and CDK1 phosphorylation — cell cycle coupling
  - CEP72 depletion causes ciliogenesis defects — links centrosome to developmental signaling relevant for TE silencing
- **Strength:** Moderate. Ciliogenesis → Hedgehog signaling → TE silencing is a plausible multi-step connection. The centriole assembly role provides genome stability links.
- **Caveats:** CEP72 is less studied than CEP63/CEP152. Direct TE evidence absent.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 18/20 | Dual HPA source + UniProt + GO-CC. Centriole assembly pathway validated. |
| TE relevance | 7/20 | Hedgehog signaling via ciliogenesis; centriole assembly → genome stability. Indirect but multi-pathway. |
| PubMed/literature | 10/20 | 70 papers. Well-balanced. Room for novel discovery. |
| PPI/network | 12/20 | CEP63-CEP152-CDK5RAP2 network. Moderate interaction data. |
| Structure/domain | 5/10 | LRR domains + coiled-coil. No PDB. Moderate pLDDT. |
| Novelty/specificity | 7/10 | Not in main atlas. Dual HPA source. Moderate study volume. Good centriole specificity. |

- **Raw score:** (18×4) + (7×5) + (10×4) + (12×3) + (5×2) + (7×2) = 72 + 35 + 40 + 36 + 10 + 14 = 207
- **Final centrosome score:** 207 / 3.6 = **58/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** CEP72 is a well-validated centrosome/centriole/satellite protein with dual HPA source annotation. Moderate publication volume, good centrosome specificity, and tractable size (647 aa). The Hedgehog signaling link through ciliogenesis provides a TE-relevant pathway. Not in main atlas.

## 10. Manual Review Note

- Not in main atlas — new target for centrosome module
- Dual HPA annotation increases confidence in centrosome localization
- LRR domain architecture is interesting — consider whether CEP72 LRRs recognize nucleic acids (similar to TLRs)
- 647 aa is experimentally tractable for biochemical characterization
- CEP72-CEP63-CEP152 pathway is a defined centriole assembly axis — multiple members are in the centrosome seed set
