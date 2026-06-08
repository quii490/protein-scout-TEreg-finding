---
type: centrosome-protein-evaluation
gene: "PLK4"
module: centrosome
status: centrosome_eliminated
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# PLK4 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** O00444
- **Protein name:** Serine/threonine-protein kinase PLK4 (Polo-like kinase 4)
- **Synonyms:** SAK, STK18
- **Length:** 970 aa
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000142731-PLK4
- **HPA reliability:** Supported (IF)
- **HPA location text:** Centrosome, cytosol
- **IF image:** Available

![[PLK4_IF_1.jpg]]

PLK4 is the master regulator of centriole biogenesis. HPA IF shows characteristic 1-2 puncta per cell in G1.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, centriole, deuterosome
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0036064 (ciliary basal body) — IDA
- **Notes:** Essential for centriole duplication. One of the most specific centrosome proteins.

## 4. PubMed Evidence

- **Total PubMed:** 591 papers ⚠️ **EXCEEDS THRESHOLD (>100)**
- **Strict query (centrosome/centriole):** 383 papers
- **Broad query:** 488 papers
- **Key papers:**
  - Bettencourt-Dias M et al. (2005) — PLK4 master regulator; PMID: 16244668
  - Habedanck R et al. (2005) — PLK4 controls centriole duplication; PMID: 16244669
  - Holland AJ et al. (2010) — PLK4 autophosphorylation; PMID: 20852615
- **Alias contamination note:** Also SAK, STK18. All confirmed.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** High for kinase domain
- **PAE:** Available
- **PDB:** 4Y7J (kinase), 4N9J (PB3 polo-box)
- **InterPro:** IPR000719 Protein kinase, IPR000959 POLO box, IPR033703 PLK4 polo box
- **Domain notes:** N-term kinase + 3 polo-box domains (PB1-PB3). Cryptic polo-box unique to PLK4.

## 6. PPI / humanPPI

- **STRING:** Rich centrosome network
- **IntAct:** Multiple curated interactions
- **Key centrosome interactors:** CEP152, CEP192, STIL, CEP85, TUBG1

## 7. TE-Regulator Relevance

- PLK4 overexpression → centriole amplification → genome instability
- PLK4 interacts with p53 pathway
- Target of HPV E7 oncoprotein — pathogen-TE parallel
- **Strength:** Moderate. Indirect through genome integrity.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 20/20 | Master centriole kinase. Extensive functional validation. |
| TE relevance | 7/20 | Centrosome amplification → genome instability. Indirect. |
| PubMed/literature | 8/20 | 591 papers. Centrosome-rich (65%) but over-studied. |
| PPI/network | 18/20 | CEP152-STIL-CEP192 hub; γ-tubulin connection. |
| Structure/domain | 9/10 | PDB available; unique cryptic polo-box; kinase well-structured. |
| Novelty/specificity | 3/10 | Well-studied centriole field. High specificity but low novelty. |

- **Final centrosome score:** 65/100 (academic score only — overridden by PubMed elimination)

## 9. Final Decision

**CENTROSOME_ELIMINATED**

**Reason:** PubMed total = 591 (>100 threshold). PLK4 is the master centriole kinase with excellent biology, but 591 publications put it in the over-studied category for TEreg discovery.

## 10. Manual Review Note

- Eliminated per PubMed > 100 rule
- PLK4 inhibitor centrinone may be useful as a tool compound for centrosome-depletion experiments
