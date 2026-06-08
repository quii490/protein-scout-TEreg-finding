---
type: centrosome-protein-evaluation
gene: "PCM1"
module: centrosome
status: centrosome_eliminated
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# PCM1 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q15154
- **Protein name:** Pericentriolar material 1 protein (PCM1)
- **Synonyms:** hPCM1, PTC4
- **Length:** 2,024 aa
- **HPA seed source:** Centriolar satellite

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centriolar satellite ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000078674-PCM1
- **HPA reliability:** Supported (IF)
- **HPA location text:** Microtubules, primary cilium, centriolar satellite, basal body
- **IF image:** Available

![[PCM1_IF_1.jpg]]

PCM1 is the defining marker protein of centriolar satellites — dynamic protein granules surrounding the centrosome.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centriolar satellite, centrosome, cilium basal body
- **GO-CC terms:**
  - GO:0034451 (centriolar satellite) — IDA
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0036064 (ciliary basal body) — IDA
- **Notes:** Scaffold for centriolar satellite assembly. Required for ciliogenesis.

## 4. PubMed Evidence

- **Total PubMed:** 367 papers ⚠️ **EXCEEDS THRESHOLD (>100)**
- **Strict query (centrosome/centriole):** 142 papers
- **Broad query:** 206 papers
- **Key papers:**
  - Kubo A et al. (1999) — PCM1 centriolar satellites; PMID: 10533096
  - Dammermann A & Merdes A (2002) — PCM1 dynein-dependent targeting; PMID: 12163438
  - Villumsen BH et al. (2013) — PCM1 in DNA damage response; PMID: 23922942
- **Alias contamination note:** PCM1-JAK2 and PCM1-RET cancer fusions inflate PubMed count — distinct biology from centrosome function.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate (2,024 aa, significant disorder)
- **PAE:** Available
- **PDB:** Limited (fragments)
- **InterPro:** Predominantly coiled-coil; no catalytic domains
- **Domain notes:** Large coiled-coil scaffold. LLPS potential. No resolved full-length structure.

## 6. PPI / humanPPI

- **STRING:** Extensive satellite network
- **Centrosome interactors:** CEP290, BBS4, OFD1, CEP131, SSX2IP, DCTN1, PLK4
- **Cancer fusion partners:** JAK2, RET (distinct biology)

## 7. TE-Regulator Relevance

- PCM1 localizes to DNA damage foci upon UV/IR (Villumsen et al., 2013)
- Ciliogenesis defects → loss of Hedgehog signaling → relevant to developmental TE silencing
- Satellite disassembly in mitosis — potential uncharacterized DNA sensing functions
- **Strength:** Moderate. DNA damage localization directly relevant.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 18/20 | Defining satellite marker. HPA + UniProt + GO-CC. |
| TE relevance | 10/20 | DNA damage foci; ciliogenesis/signaling. |
| PubMed/literature | 8/20 | 367 papers. Cancer fusion literature inflates count. |
| PPI/network | 16/20 | Satellite hub. BBSome-CEP290-OFD1 network. |
| Structure/domain | 4/10 | Large coiled-coil; no PDB; LLPS potential. |
| Novelty/specificity | 6/10 | DNA damage function under-studied. |

- **Final centrosome score:** 62/100 (academic score only — overridden by PubMed elimination)

## 9. Final Decision

**CENTROSOME_ELIMINATED**

**Reason:** PubMed total = 367 (>100 threshold). PCM1 cancer fusion literature (JAK2, RET) inflates count. Core satellite biology is well-characterized but over-studied for TEreg discovery.

## 10. Manual Review Note

- Eliminated per PubMed > 100 rule
- Cancer fusion literature (JAK2/RET) accounts for ~40% of publications — distinct from centrosome biology
- DNA damage foci localization (2013) is an under-explored function worth noting
