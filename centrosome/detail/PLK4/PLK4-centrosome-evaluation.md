---
type: centrosome-protein-evaluation
gene: "PLK4"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# PLK4 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** O00444
- **Protein name:** Serine/threonine-protein kinase PLK4 (Polo-like kinase 4)
- **Synonyms:** SAK, STK18
- **Length:** 970 aa
- **Main atlas overlap:** Yes (status: scored, category: nucleoplasm)
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000142731-PLK4
- **HPA reliability:** Approved
- **HPA location text:** Centrosome, centriole
- **IF image status:** Available — punctate centrosome staining

PLK4 is the master regulator of centriole biogenesis. HPA IF shows characteristic 1-2 puncta per cell in G1, duplicating to 2-4 in G2/M. This is diagnostic of centriole localization.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, centriole, deuterosome
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0036064 (ciliary basal body) — IDA
- **Notes:** PLK4 is the kinase that initiates procentriole assembly. Essential for centriole duplication. One of the most specific centrosome proteins.

## 4. PubMed Evidence

- **Total PubMed:** 591 papers
- **Strict query (centrosome/centriole):** 383 papers
- **Broad query:** 488 papers
- **Key papers:**
  - Bettencourt-Dias M et al. (2005) — PLK4 as master regulator of centriole biogenesis; PMID: 16244668
  - Habedanck R et al. (2005) — PLK4 controls centriole duplication; PMID: 16244669
  - Kleylein-Sohn J et al. (2007) — PLK4-induced centriole biogenesis in human cells; PMID: 17785410
  - Holland AJ et al. (2010) — PLK4 autophosphorylation and centriole number control; PMID: 20852615
- **Alias contamination note:** Also known as SAK (Snk/Plk-akin kinase), STK18. All confirmed as PLK4.
- **Assessment:** Moderately well-studied (591 papers) but highly centrosome-focused (65% centrosome-specific). Some papers may be aliased from Drosophila Sak studies.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** High confidence for kinase domain; N-terminal region lower confidence
- **PAE:** Available — kinase domain compact; PB1-PB3 polo-box domains have moderate inter-domain confidence
- **PDB:** Available. Key structures:
  - 4Y7J (kinase domain)
  - 4N9J (PB3 polo-box domain)
- **InterPro / Pfam / SMART:**
  - IPR000719: Protein kinase domain (Pfam: PF00069)
  - IPR000959: POLO box domain (Pfam: PF00659)
  - IPR033703: PLK4, POLO box 1-2 (cryptic polo boxes)
- **Domain notes:** Unique architecture: N-terminal kinase domain + 3 polo-box domains (PB1-PB3). PB1-PB2 form a cryptic polo-box that mediates centriole targeting. Cryptic polo-box is unique to PLK4.

## 6. PPI / humanPPI

- **STRING:** Rich centrosome interaction network
- **IntAct:** Multiple curated interactions
- **BioGRID:** Extensive physical interactions
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - CEP152 (centriole receptor/scaffold)
  - CEP192 (centrosome scaffold)
  - STIL (centriole assembly protein)
  - CEP85 (centriole assembly)
  - TUBG1 (γ-tubulin, centriole component)

## 7. TE-Regulator Relevance

- **Evidence:**
  - PLK4 overexpression → centriole amplification → centrosome amplification → genome instability — a known cancer mechanism
  - Centrosome amplification can drive TE activation via DNA damage response (DDR) signaling
  - PLK4 interacts with p53 pathway (p53 restricts centriole overduplication)
  - PLK4 loss induces p53-dependent cell cycle arrest → potential TE activation context
  - PLK4 is a target of viral oncoproteins (HPV E7) — hints at pathogen-TE parallel mechanisms
- **Strength:** Moderate. The centrosome amplification → genome instability → TE activation chain is biologically plausible but multi-step.
- **Caveats:** No direct evidence of PLK4-TE interaction. The connection is via genome integrity pathways.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 20/20 | Master centriole kinase. HPA + UniProt + GO-CC + extensive functional literature. |
| TE relevance | 7/20 | Centrosome amplification → genome instability → potential TE activation. Plausible chain but no direct evidence. |
| PubMed/literature | 8/20 | 591 papers total. Centrosome-rich but high volume limits novelty. |
| PPI/network | 18/20 | Well-characterized PPI with CEP152, STIL, CEP192; γ-tubulin connection to MT cytoskeleton. |
| Structure/domain | 9/10 | PDB available; unique cryptic polo-box; kinase domain well-structured. N-term flexibility minor. |
| Novelty/specificity | 3/10 | Well-studied (centriole field). Very centrosome-specific but not novel. |

- **Raw score:** (20×4) + (7×5) + (8×4) + (18×3) + (9×2) + (3×2) = 80 + 35 + 32 + 54 + 18 + 6 = 225
- **Final centrosome score:** 225 / 3.6 = **63/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** PLK4 is the master regulator of centriole biogenesis with impeccable centrosome evidence. Despite moderate publication volume, it qualifies as CANDIDATE because: (1) its centrality to centrosome biology makes it a key reference point for the module; (2) the centrosome amplification → TE activation connection is mechanistically interesting; (3) PLK4 inhibitors exist as chemical tools. However, novelty is limited.

## 10. Manual Review Note

- Main atlas status: scored (nucleoplasm)
- PLK4 is auto-rejected in main atlas due to PubMed > 100 but centrosome module uses different criteria
- Worth including as a "module anchor" — provides context for interpreting less-studied centrosome proteins
- Consider: PLK4 inhibitor centrinone as a tool compound for centrosome-TE experiments
