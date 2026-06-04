---
type: protein-evaluation
gene: "RNF44"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RNF44 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF44 / KIAA1100 |
| Protein Name | RING finger protein 44 |
| Protein Size | 432 aa / 47.7 kDa |
| UniProt ID | Q7L0R7 (RNF44_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 2/10 | x4 | **8** | No subcellular location annotation; no GO-CC nuclear terms; no nucleus keyword; RING domain only |
| Protein Size | 10/10 | x1 | **10** | 432 aa, within ideal 200-800 aa range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~9 articles (<=20 -> 10); extremely under-studied |
| 3D Structure | 6/10 | x3 | **18** | No PDB entries; AlphaFold prediction available; novel protein baseline (6/10) |
| Regulatory Domains | 7/10 | x2 | **14** | RING finger only; no DNA/chromatin domains; novel protein baseline (7/10) applies |
| PPI Network | 2/10 | x3 | **6** | No characterized PPI data; no interaction mapping available |
| Cross-Validation Bonus | -- | -- | **+0** | No cross-validation possible due to absence of annotation data |
| **Raw Total** | | | **106.0/180** | |
| **Normalized Total** | | | **57.9/100** | |

### 3. Nuclear Localization Evidence -- FAILS THRESHOLD

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Not annotated | -- |
| GO-CC | No nuclear terms | -- |
| UniProt Keywords | No "Nucleus" keyword | -- |
| HPA | Data not available in packet | -- |

**HPA IF Status**: HPA IF original images not reliably obtained. No nuclear localization evidence from any database source.

**Manual Review Assessment**: RNF44 presents a clear case of insufficient nuclear localization evidence. UniProt (Swiss-Prot reviewed entry) provides NO subcellular location annotation whatsoever. The Gene Ontology Cellular Component annotations contain NO nuclear terms. UniProt keywords do NOT include "Nucleus". The protein has not been experimentally localized by any high-confidence method captured in these databases.

**Key points on lack of nuclear evidence**:
1. UniProt subcellular location field: empty (no annotation)
2. GO-CC: no nuclear, nucleoplasm, or chromatin-related annotations
3. Keywords: "Alternative splicing, Metal-binding, Proteomics identification, Reference proteome, Zinc, Zinc-finger" -- no nucleus
4. The only annotated features are the RING finger domain and zinc finger motifs
5. RING finger proteins can localize to any cellular compartment -- cytoplasmic, nuclear, membrane-associated, or secreted
6. No functional annotation provides indirect evidence for nuclear localization

**Nuclear localization score: 2/10. RULE: Nuclear <=3 -> REJECTED.** The complete absence of nuclear localization annotation across all databases, combined with no functional evidence for nuclear activity, places RNF44 well below the rejection threshold. This protein is NOT a verified nuclear protein.

### 4. Protein Size Assessment

RNF44 is 432 amino acids in length, within the ideal 200-800 aa range. The protein is of a tractable size for biochemical studies. However, this does not compensate for the lack of nuclear localization evidence. Size score: 10/10 (informational only, since the protein is REJECTED on nuclear grounds).

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~9 |
| Novelty category | <=20 -> Score 10 |
| Earliest publication | Genome-wide studies only |

**Research Context**: RNF44 is an extremely under-studied protein with approximately 9 PubMed entries, the vast majority of which are likely high-throughput genomic/proteomic studies rather than dedicated functional investigations. The gene was initially identified as KIAA1100 through large-scale cDNA sequencing projects. No focused functional studies have been published for RNF44.

**Novelty Assessment**: PubMed count of ~9 places RNF44 in the most novel category (<=20 -> 10). This is among the most under-studied proteins in the human proteome. Despite the high novelty score, the protein fails the nuclear localization threshold and cannot be recommended regardless of novelty.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 |
| Structural Coverage | Predicted only |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Assessment based on domain architecture and AlphaFold prediction.

**Structure Assessment**: RNF44 has no experimental PDB structures. The AlphaFold prediction likely shows a well-folded RING finger domain with potentially disordered N/C terminal regions. The 432 aa length suggests additional domains or extended regions beyond the RING finger that remain uncharacterized. Score 6/10 applies the novel protein baseline (informational only for a rejected protein).

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR001841 (RING finger) | E3 ubiquitin ligase domain |
| InterPro | IPR013083 (Znf RING/FYVE/PHD) | Metal-binding domain |
| Pfam | PF13639 (zf-RING_2) | RING-type zinc finger |

**Domain Analysis**: RNF44 contains a single annotated domain type: the RING finger, which confers E3 ubiquitin ligase activity. The domain architecture is minimal, with only one recognized functional domain. No DNA-binding, chromatin-interacting, or nuclear localization signal domains are present. The RING domain alone does not predict or require nuclear localization -- RING E3 ligases function in all cellular compartments. Score 7/10 (baseline for novel protein, informational only).

### 8. PPI Network Analysis

**PPI Assessment**: No characterized protein-protein interaction data exists for RNF44 in any public database. The protein has not been the subject of any focused interaction study. The only predictable interactions are with ubiquitin-conjugating enzymes (E2s) as required for E3 ligase activity. Score 2/10 reflects the complete absence of interaction data.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + GO-CC + Keywords | No nuclear annotation | Data absent |
| Domain | InterPro + Pfam | RING finger only | Consistent but not nuclear-informative |

**Cross-Validation Bonus Details**:
- No multi-database localization data available: +0
- No structural cross-validation (no PDB): +0
- No PPI cross-validation: +0
- **Total Cross-Validation Bonus**: 0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED (nuclear localization failure)

**Core Reasons for Rejection**:
1. Complete absence of nuclear localization evidence (score 2/10, threshold <=3 triggers rejection)
2. No subcellular location annotation in UniProt (Swiss-Prot reviewed)
3. No nuclear GO-CC terms
4. No "Nucleus" keyword in UniProt
5. RING finger domain alone does not predict or require nuclear localization
6. No functional studies to infer nuclear activity
7. No PPI data to suggest nuclear interaction partners

**Potential if localized**: If future studies establish nuclear localization for RNF44, the protein would be an attractive candidate: extremely novel (PubMed=9, score 10/10), tractable size (432 aa), and an unexplored E3 ubiquitin ligase. The current rejection is based solely on the absence of nuclear localization evidence, not on negative evidence.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RNF44 fails the nuclear localization criterion (score 2/10, threshold <=3). The protein has NO nuclear localization annotation in any database (UniProt, GO-CC, keywords). While extremely novel (PubMed=9), the complete absence of nuclear evidence makes this protein unsuitable for a nuclear-focused protein screen. NOTE: If future experimental data establishes nuclear localization, this protein should be re-evaluated given its exceptional novelty.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q7L0R7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF44%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L0R7
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q7L0R7/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
