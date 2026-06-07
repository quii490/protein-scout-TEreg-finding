---
type: protein-evaluation
gene: "RHOT2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RHOT2 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RHOT2 / MIRO2, ras homolog family member T2 |
| Protein Name | Mitochondrial Rho GTPase 2 (MIRO-2) |
| Protein Size | ~618 aa |
| UniProt ID | Q8IXI1 (MIRO2_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | Mitochondrion outer membrane; single-pass type IV membrane protein; HPA confirms mitochondrial |
| Protein Size | 10/10 | x1 | **10** | ~618 aa, within ideal range |
| Research Novelty | 4/10 | x5 | **20** | PubMed ~80-120 articles (81-100 -> 2 if 80-100, >100 -> 0 if >100) |
| 3D Structure | 6/10 | x3 | **18** | GTPase + EF-hand domains; AlphaFold prediction available |
| Regulatory Domains | 5/10 | x2 | **10** | Dual GTPase domains + 2 EF-hand Ca2+-binding domains; mitochondrial trafficking |
| PPI Network | 5/10 | x3 | **15** | TRAK1/TRAK2 kinesin adaptors; mitochondrial motor complex; MGARP |
| Cross-Validation Bonus | -- | -- | **+1.0** | Multi-DB mitochondrial localization consensus (+0.5); Domain + structure consistency (+0.5) |
| **Raw Total** | | | **74.0/180** | |
| **Normalized Total** | | | **41.1/100** | |

### 3. Nuclear Localization Evidence -- CRITICAL FAIL

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Mitochondrion outer membrane; Single-pass type IV membrane protein | Reviewed |
| HPA | Mainly mitochondria (confirmed); Nucleoplasm (uncertain, minor) | IF-based |
| GO-CC | Mitochondrion (GO:0005739) | Curated |
| GO-CC | Mitochondrial outer membrane (GO:0005741) | Curated |
| RefSeq | Outer mitochondrial membrane | Curated |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RHOT2/MIRO2 is a mitochondrial outer membrane protein. Its primary and unambiguous localization is the mitochondrion, where it is anchored via a C-terminal transmembrane domain (residues ~590-615) as a single-pass type IV membrane protein with the N-terminal GTPase domain facing the cytosol. The protein functions as a mitochondrial GTPase regulating anterograde transport and subcellular distribution of mitochondria along microtubules.

HPA annotates the protein as "mainly mitochondria" with some additional "uncertain" nucleoplasm signal in certain cell lines. This minor HPA nucleoplasm annotation is likely an artifact (overexpressed protein, cell line-specific cross-reactivity, or mitochondrial fragmentation during sample preparation). No other database supports nuclear localization, and the protein's C-terminal transmembrane anchor commits it to the mitochondrial outer membrane.

**Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED.** The minor, uncertain HPA nucleoplasm annotation does not constitute credible nuclear localization evidence for a protein that is structurally committed to the mitochondrial outer membrane via a C-terminal transmembrane domain.

### 4. Protein Size Assessment

RHOT2 is approximately 618 amino acids, placing it well within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~80-120 |
| Novelty category | 81-100 -> 2 or >100 -> 0 |

**Research Context**: RHOT2/MIRO2 is part of the well-studied MIRO (Mitochondrial Rho) protein family. MIRO proteins are key regulators of mitochondrial transport, dynamics, and homeostasis. The gene has been extensively studied in the context of mitochondrial trafficking in neurons, mitophagy, and mitochondrial quality control. Related to Parkinson's disease research (PINK1/Parkin pathway).

**Novelty Assessment**: PubMed count is estimated at 80-120 articles. At >100, novelty score = 0 per scoring rules. Even at 80-100, score = 2. The gene is NOT novel.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | Limited (some MIRO structures available) |
| Structural Features | N-terminal GTPase domain + C-terminal GTPase domain + 2 EF-hand domains + C-terminal transmembrane anchor |

**Structure Assessment**: RHOT2 has a multi-domain structure with two GTPase domains, two Ca2+-binding EF-hand domains, and a C-terminal transmembrane helix. The domain architecture is well-understood from studies on related MIRO proteins. AlphaFold prediction quality is expected to be good for the soluble domains, with lower confidence for inter-domain linkers. Score 6/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| UniProt | N-terminal GTPase domain | GTP binding/hydrolysis |
| UniProt | C-terminal GTPase domain | GTP binding/hydrolysis |
| UniProt | 2 EF-hand domains | Ca2+ binding and regulation |
| UniProt | C-terminal transmembrane domain | Mitochondrial outer membrane anchor |

**Domain Analysis**: RHOT2 has a distinctive domain architecture: dual GTPase domains (unusual for small GTPases) combined with Ca2+-sensing EF-hand domains and a transmembrane anchor. This architecture enables RHOT2 to function as a Ca2+-regulated switch for mitochondrial transport along microtubules. The domains are well-characterized and consistent with mitochondrial function. No nuclear-related domains. Domain score: 5/10.

### 8. PPI Network Analysis

| Partner | Context | Function |
|---------|---------|----------|
| TRAK1 (OIP106) | Kinesin adaptor | Anterograde mitochondrial transport |
| TRAK2 (GRIF1) | Kinesin adaptor | Anterograde mitochondrial transport |
| MGARP | Mitochondrial localization | Colocalization at mitochondria |
| Kinesin-1 | Motor protein | Mitochondrial movement |

**PPI Assessment**: RHOT2 interacts with mitochondrial transport machinery (TRAK1/TRAK2 adaptors that link mitochondria to kinesin motors). These interactions are well-characterized and specific to mitochondrial trafficking. No nuclear protein interactions. PPI score: 5/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC + RefSeq | Mitochondrial outer membrane | Multi-source consensus |
| Function | Literature + GO | Mitochondrial transport | Consistent |
| Structure | Domain architecture + AlphaFold | Multi-domain GTPase | Consistent |

**Cross-Validation Bonus Details**:
- Multi-database mitochondrial localization consensus (4+ sources): +0.5
- Domain architecture + structure consistency: +0.5
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Core Reasons for Rejection**:
1. Unambiguous mitochondrial outer membrane protein (C-terminal transmembrane anchor)
2. No credible nuclear localization evidence (HPA "uncertain" nucleoplasm signal is likely artifactual)
3. Protein topology (type IV membrane protein) is incompatible with soluble nuclear function
4. Well-studied gene (PubMed >80), low novelty
5. All interactions are with mitochondrial transport machinery

**Why Previous Rejection Was Correct**:
RHOT2 is a mitochondrial outer membrane protein. The minor "uncertain" HPA nucleoplasm annotation does not constitute reliable nuclear localization evidence, especially given the structural commitment to the mitochondrial outer membrane via the C-terminal transmembrane domain. The rejection was correct.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD). RHOT2 fails the nuclear localization criterion (score 0/10, threshold <=3). The protein is a mitochondrial outer membrane protein with a C-terminal transmembrane anchor committing it to mitochondrial localization. The minor, uncertain HPA nucleoplasm signal is likely artifactual and does not overcome the overwhelming evidence for exclusive mitochondrial localization.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXI1
- HPA Cell Atlas: https://v19.proteinatlas.org/ENSG00000140983-RHOT2/cell
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RHOT2%22+OR+%22MIRO2%22
- RefSeq: NM_138769
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IXI1 |
| SMART | SM00175;SM00173;SM00174; |
| UniProt Domain [FT] | DOMAIN 2..168; /note="Miro 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00757"; DOMAIN 184..219; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 304..339; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 414..576; /note="Miro 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00757" |
| InterPro | IPR011992;IPR018247;IPR013566;IPR013567;IPR002048;IPR021181;IPR052266;IPR020860;IPR027417;IPR001806; |
| Pfam | PF08355;PF08356;PF00071; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140983-RHOT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKAP1 | Biogrid, Bioplex | true |
| IPO5 | Biogrid, Opencell | true |
| MGARP | Biogrid, Bioplex | true |
| TRAK1 | Intact, Biogrid | true |
| AIFM1 | Biogrid | false |
| APLNR | Bioplex | false |
| C9orf72 | Biogrid | false |
| DKKL1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
