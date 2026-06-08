---
type: centrosome-protein-evaluation
gene: "PCM1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# PCM1 — Centrosome Module Evaluation

## 1. 基本信息

- **UniProt:** Q15154
- **Protein name:** Pericentriolar material 1 protein (PCM1)
- **Synonyms:** hPCM1, PTC4
- **Length:** 2,024 aa
- **Main atlas overlap:** No (not in main atlas)
- **HPA seed source:** Centriolar satellite

## 2. HPA Centrosome / Centriolar Satellite Evidence

- **HPA seed source:** Centriolar satellite ✓
- **HPA URL:** https://www.proteinatlas.org/ENSG00000078674-PCM1
- **HPA reliability:** Approved
- **HPA location text:** Centriolar satellite
- **IF image status:** Available — punctate cytoplasmic foci near centrosome (satellite pattern)

PCM1 is the defining marker protein of centriolar satellites — granular structures surrounding the centrosome. HPA IF shows the characteristic dispersed punctate satellite pattern. Centriolar satellites are dynamic protein granules involved in centrosome protein trafficking.

## 3. UniProt / GO-CC Centrosome Evidence

- **UniProt subcellular location:** Centriolar satellite, centrosome, cilium basal body, cytoplasm
- **GO-CC terms:**
  - GO:0034451 (centriolar satellite) — IDA
  - GO:0005813 (centrosome) — IDA
  - GO:0005814 (centriole) — IDA
  - GO:0036064 (ciliary basal body) — IDA
- **Notes:** PCM1 is the scaffold protein for centriolar satellite assembly. Required for ciliogenesis. Not a static centrosome component — satellites are dynamic trafficking intermediates.

## 4. PubMed Evidence

- **Total PubMed:** 367 papers
- **Strict query (centrosome/centriole):** 142 papers
- **Broad query:** 206 papers
- **Key papers:**
  - Kubo A et al. (1999) — Centriolar satellites: PCM1-containing granules; PMID: 10533096
  - Dammermann A & Merdes A (2002) — PCM1 and dynein-dependent centrosome protein targeting; PMID: 12163438
  - Hori A & Toda T (2017) — Centriolar satellite dynamics and ciliogenesis; PMID: 27565691
  - Villumsen BH et al. (2013) — PCM1 in DNA damage response; PMID: 23922942
- **Alias contamination note:** PCM1 also found in some cancer fusion genes (PCM1-JAK2, PCM1-RET). Distinguish from hematological malignancy literature.
- **Assessment:** 367 papers total. About 142 centrosome-specific. Satellite field moderate but active. Cancer fusion gene literature adds volume but is distinct.

## 5. AlphaFold / PAE / PDB / Domain

- **AlphaFold pLDDT:** Moderate — large protein (2,024 aa), significant disordered regions
- **PAE:** Available — structured domains separated by long linkers
- **PDB:** Limited (fragments only)
- **InterPro / Pfam / SMART:**
  - Predominantly coiled-coil architecture
  - Multiple putative protein interaction motifs
  - No catalytic domains — scaffolding protein
- **Domain notes:** PCM1 is a large coiled-coil scaffold. Contains multiple centrosome-targeting motifs. Disordered regions may mediate liquid-liquid phase separation (LLPS) — a property of many satellite proteins. No resolved PDB structure for full-length protein.

## 6. PPI / humanPPI

- **STRING:** Extensive satellite interaction network
- **IntAct:** Curated interactions
- **BioGRID:** Physical interactions
- **humanPPI:** Available
- **Centrosome-related interactors:**
  - CEP290 (satellite/centriole, ciliopathy protein)
  - BBS4 (BBSome, satellite component)
  - OFD1 (satellite, ciliopathy protein)
  - CEP131 (satellite, centriole)
  - SSX2IP (satellite protein)
  - DCTN1 (dynactin, dynein-mediated transport)
  - PLK4 (centriole kinase — recruitment via satellites?)
- **Cancer fusion partners:**
  - JAK2 (PCM1-JAK2 in leukemia — caution: distinct biology)
  - RET (PCM1-RET in thyroid cancer)

## 7. TE-Regulator Relevance

- **Evidence:**
  - PCM1 localizes to DNA damage foci upon UV/IR treatment (Villumsen et al., 2013)
  - Centriolar satellites regulate centrosomal protein trafficking — may affect cell cycle regulation of TE silencing
  - PCM1 depletion causes ciliogenesis defects → loss of Hedgehog signaling → developmental pathway relevant to TE silencing during differentiation
  - PCM1 interacts with CEP290, which also has nuclear/nucleolar localization
  - Satellite disassembly in mitosis releases PCM1 to cytoplasm — may have uncharacterized cytoplasmic DNA sensing functions
  - PCM1's DNA damage localization is independent of its centrosome role — suggests moonlighting function
- **Strength:** Moderate. The DNA damage localization is directly relevant but the TE connection is not established. Ciliogenesis link connects to developmental TE silencing pathways.
- **Caveats:** Most PCM1 literature is on satellite biology and cancer fusions. DNA damage function is less studied.

## 8. Centrosome Scoring Table

| Dimension | Score | Evidence |
|---|---:|---|
| Centrosome evidence | 18/20 | Defining satellite marker. HPA + UniProt + GO-CC. Satellite-specific biology unique. |
| TE relevance | 10/20 | DNA damage foci localization. Ciliogenesis/signaling link. Two independent TE-relevant connections. |
| PubMed/literature | 8/20 | 367 papers total. Cancer fusion literature inflates count. Centrosome component well-characterized. |
| PPI/network | 16/20 | Satellite hub. Interacts with BBSome, CEP290, OFD1, CEP131, dynein. Rich interaction network. |
| Structure/domain | 4/10 | Large coiled-coil scaffold. No PDB. Moderate pLDDT. LLPS potential interesting but unresolved. |
| Novelty/specificity | 6/10 | Active satellite field. DNA damage function is novel/under-studied aspect. Not in main atlas. |

- **Raw score:** (18×4) + (10×5) + (8×4) + (16×3) + (4×2) + (6×2) = 72 + 50 + 32 + 48 + 8 + 12 = 222
- **Final centrosome score:** 222 / 3.6 = **62/100**

## 9. Final Decision

**CENTROSOME_CANDIDATE**

**Reason:** PCM1 is the defining centriolar satellite protein with unique satellite biology. Its DNA damage foci localization provides an unexpected TE-relevant function. Not in main atlas (new protein). Moderate-high publication volume but satellite DNA damage function is under-studied. Large size (2,024 aa) is a practical concern but manageable as a scaffold.

## 10. Manual Review Note

- Not in main atlas — "discovery" for centrosome module
- PCM1 DNA damage localization should be further investigated for TE biology relevance
- Consider PCM1 as a satellite-biology anchor for the centrosome module
- PCM1-JAK2 fusion is a leukemia driver — confirms PCM1's role in cellular transformation but is a distinct mechanism from TE regulation
- 2,024 aa is large for recombinant expression; consider domain-based approaches
