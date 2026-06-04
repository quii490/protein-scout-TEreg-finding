---
type: protein-evaluation
gene: "SERPINI2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (secreted extracellular protein)"
---

## SERPINI2 -- Re-evaluation Report (REJECTED: Secreted Serine Protease Inhibitor)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SERPINI2 / MEPI, PI14, Pancpin, Pancreas-specific protein TSA2004 |
| Protein Name | Serpin I2 (Myoepithelium-derived serine protease inhibitor, Pancpin, Peptidase inhibitor 14) |
| Protein Size | ~405 aa |
| UniProt ID | O75830 (SPI2_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | Secreted, extracellular; no nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | ~405 aa, within ideal range |
| Research Novelty | 6/10 | x5 | **30** | Estimated ~40-60 PubMed articles |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold predicted; serpin family fold; no experimental PDB |
| Regulatory Domains | 3/10 | x2 | **6** | Serpin domain (serine protease inhibitor); no regulatory domains |
| PPI Network | 2/10 | x3 | **6** | Limited PPI data; targets uncharacterized serine proteases |
| Cross-Validation Bonus | -- | -- | **+0** | Consistent secreted annotation; no nuclear evidence |
| **Raw Total** | | | **68.0/180** | |
| **Normalized Total** | | | **37.8/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 1/10 (threshold: ≤3). SERPINI2 is a secreted extracellular serine protease inhibitor with no nuclear localization.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Secreted (probable) | Primary annotation |
| GO-CC | Extracellular region (GO:0005576) | Database annotation |
| GO-CC | Extracellular space (GO:0005615) | Database annotation |
| GO-CC | Extracellular exosome (GO:0070062) | Database annotation |

**Manual Review Assessment**: SERPINI2 is unambiguously a secreted protein. As a member of the serpin superfamily, it functions as an extracellular serine protease inhibitor regulating coagulation, fibrinolysis, and inflammation. The protein is primarily expressed in pancreas and adipose tissues, and expression may be downregulated during pancreatic carcinogenesis. It is also known as myoepithelium-derived serine protease inhibitor (MEPI) and pancpin. No database annotates nuclear localization or nuclear function. As a secreted protein, SERPINI2 lacks any mechanism for nuclear entry and has no connection to transcriptional regulation, chromatin biology, or DNA binding. Nuclear localization score 1/10 reflects the definitive extracellular/secreted localization.

### 4. Protein Size Assessment

SERPINI2 is approximately 405 amino acids, within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~40-60 articles |
| Novelty category | 41-80 -> Score 6 |

SERPINI2 research focuses on its role as a serine protease inhibitor in the pancreas and its potential as a tumor suppressor in pancreatic cancer. The serpin family is well-characterized, but SERPINI2 itself has limited specific literature. Moderate research activity. Score 6/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no experimental structures for human SERPINI2) |
| Domain | Serpin fold (conserved among serpin family members) |

AlphaFold prediction available. The serpin fold is well-characterized across the family, and AlphaFold typically predicts it with high confidence. No experimental structures for human SERPINI2. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | Serpin domain | Serine protease inhibitor superfamily |
| Pfam | Serpin (PF00079) | Conserved protease inhibitor fold |

SERPINI2 contains a serpin domain, characteristic of extracellular serine protease inhibitors. The serpin fold undergoes a dramatic conformational change upon protease binding (the "stressed-to-relaxed" transition). While this is a biochemically interesting mechanism, it is not a regulatory domain relevant to nuclear function, transcription, or chromatin biology. Score 3/10 reflects the well-characterized but non-regulatory domain type.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Known Partners | Target serine proteases (uncharacterized) |
| STRING | Limited data expected for an extracellular inhibitor |

As a secreted protein, SERPINI2 interactions are limited to target proteases in the extracellular space. No nuclear, cytoplasmic, or signaling protein interactions. Score 2/10.

### 9. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 1/10. SERPINI2 is a secreted extracellular serine protease inhibitor with no nuclear function.

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O75830
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SERPINI2
- Note: Harvest packet not available; data compiled from web database queries
