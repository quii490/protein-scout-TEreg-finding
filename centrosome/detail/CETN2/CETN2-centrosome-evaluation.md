---
type: centrosome-protein-evaluation
gene: "CETN2"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CETN2 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** P41208
- **Protein name:** Centrin-2 (CETN2)
- **Synonyms:** CALT, CEN2
- **Length:** 172 aa
- **Main atlas overlap:** Yes (status: scored, category: nuclear-envelope)
- **HPA seed source:** Centrosome

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centrosome ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000147400-CETN2
- **HPA reliability:** Approved
- **HPA location text:** Centrosome, centriole
- **IF image status:** Available — punctate centrosome staining

CETN2 is a core centriole component and a member of the centrin family of calcium-binding proteins. HPA IF shows characteristic centrosome puncta.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centrosome, centriole, cilium basal body, nucleus
- **GO-CC terms:**
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA, TAS
  - GO:0036064 (ciliary basal body) — IDA
  - GO:0035869 (ciliary transition zone) — IDA
  - GO:0005634 (nucleus) — IDA (nucleotide excision repair)
- **Notes:** CETN2 has dual localization: centrosome (structural centriole component) and nucleus (NER/DNA repair). This dual role is notable for TE biology.

## 4. PubMed Evidence

- **Total PubMed:** 111 papers
- **Strict query (centrosome/centriole):** 55 papers
- **Broad query:** 92 papers
- **Key papers:**
  - Salisbury JL et al. (2002) — Centrin-2 and centriole duplication; PMID: 11864938
  - Araki M et al. (2001) — Centrin-2 in NER; interacts with XPC; PMID: 11278958
  - Nishi R et al. (2005) — CETN2 enhances XPC damage recognition in NER; PMID: 15964821
  - Yang CH et al. (2006) — Dual role: centriole and DNA repair; PMID: 16713576
- **Alias contamination note:** Also known as CALT (caltractin). Minimal contamination.
- **Assessment:** 111 papers total. Unique dual role in centrosome + DNA repair. NER function (40+ papers) separate from centrosome literature. This dual function is highly relevant for TE biology.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Very high (172 aa, small protein, well-folded)
- **PAE:** Available — compact EF-hand domain, excellent confidence
- **PDB:** Available. Key structures:
  - 2A4J (CETN2 + XPC peptide, NER complex)
  - 2GGM (CETN2 + Sfi1 peptide, centrosome)
  - Multiple EF-hand conformations (Ca²⁺-bound vs. apo)
- **InterPro / Pfam / SMART:**
  - IPR002048: EF-hand domain (Pfam: PF13499)
  - IPR011992: EF-hand domain pair
  - 4 EF-hand motifs
- **Domain notes:** Small (172 aa), compact EF-hand protein. Calcium binding induces conformational change. Two distinct binding modes: XPC peptide (NER) vs. Sfi1 peptide (centrosome). Well-characterized structurally.

## 6. PPI / humanPPI

- **STRING:** Good interaction network
- **IntAct:** Curated interactions
- **BioGRID:** Physical interactions
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - Sfi1 (centrin-binding scaffold, centriole)
  - POC5 (centriole protein)
  - hPOC1 (centriole)
- **NER-related interactors:**
  - XPC (DNA damage recognition, NER)
  - RAD23B (NER co-factor)
  - HR23B (NER)

## 7. TE-Regulator Relevance

- **Evidence:**
  - CETN2 is a core component of Nucleotide Excision Repair (NER) — directly involved in DNA damage recognition with XPC
  - NER repairs UV-induced and bulky DNA lesions — same repair pathways activated by TE integration intermediates
  - CETN2 enhances XPC binding to damaged DNA — may recognize TE-induced DNA structures
  - CETN2's dual role (centrosome + NER) is unique: it physically connects centrosome biology to DNA repair
  - TE integration and excision can generate DNA intermediates recognized by NER machinery
  - Recent evidence: centriolar CETN2 pool may regulate ciliary signaling relevant to developmental TE silencing
- **Strength:** High. CETN2's NER function provides a direct molecular link between a "centrosome protein" and DNA repair/TE biology. This is one of the strongest TE-relevance connections in the centrosome seed list.
- **Caveats:** The NER connection is well-established but the specific TE-related DNA damage context needs experimental validation.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 19/20 | Core centriole protein. HPA + UniProt + GO-CC + PDB. Well-validated. |
| TE relevance | 16/20 | Direct NER/DNA repair role. XPC co-factor. Dual centrosome-DNA repair protein. Strongest TE link in pilot set. |
| PubMed/literature | 10/20 | 111 papers; well-balanced between centrosome and NER literature. |
| PPI/network | 14/20 | Bipartite network: centrosome (Sfi1, POC5) + NER (XPC, RAD23B). Unique dual interactome. |
| Structure/domain | 10/10 | High-res PDB available; EF-hand conformations characterized; compact, well-folded. |
| Novelty/specificity | 7/10 | Dual role is underappreciated. Centrosome + NER combination is unique. Small size (172 aa) ideal for biochemistry. |

- **Raw score:** (19×4) + (16×5) + (10×4) + (14×3) + (10×2) + (7×2) = 76 + 80 + 40 + 42 + 20 + 14 = 272
- **Final centrosome score:** 272 / 3.6 = **76/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** CETN2 stands out from the pilot set due to its unique dual role: core centriole protein + NER DNA repair co-factor. The NER function provides a direct molecular bridge between centrosome biology and DNA repair — highly relevant for TE biology. Well-characterized structurally, moderate publication volume, small protein size ideal for experiments. Highest TE relevance score in the pilot set.

## 10. Manual Review Note

- Main atlas status: scored (nuclear-envelope) — also has nuclear localization consistent with NER function
- Strongest candidate for experimental follow-up in the pilot set
- CETN2's NER function with XPC could be tested for TE DNA intermediate recognition
- Small size (172 aa) makes it ideal for recombinant expression and in vitro reconstitution
- Consider: does centriolar CETN2 recognize DNA damage at the centrosome? Open question.
