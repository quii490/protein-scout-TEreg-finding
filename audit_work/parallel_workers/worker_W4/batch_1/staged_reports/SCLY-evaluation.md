---
type: protein-evaluation
gene: "SCLY"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (cytosolic enzyme)"
---

## SCLY -- Re-evaluation Report (REJECTED: Cytosolic Enzyme, No Nuclear Localization)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SCLY / Selenocysteine lyase, mSCL |
| Protein Name | Selenocysteine lyase (EC 4.4.1.16) |
| Protein Size | ~445 aa |
| UniProt ID | Q96I15 (SCLY_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 2/10 | x4 | **8** | Cytoplasm, cytosol; no nuclear annotation in any database |
| Protein Size | 10/10 | x1 | **10** | ~445 aa, well within ideal range |
| Research Novelty | 6/10 | x5 | **30** | Estimated ~50-70 PubMed articles |
| 3D Structure | 5/10 | x3 | **15** | AlphaFold prediction available; no experimental PDB |
| Regulatory Domains | 2/10 | x2 | **4** | PLP-dependent transferase fold; no regulatory domains |
| PPI Network | 3/10 | x3 | **9** | Limited PPI data; metabolic enzyme interactome |
| Cross-Validation Bonus | -- | -- | **+0** | No multi-DB nuclear consensus; cytosolic localization consistent |
| **Raw Total** | | | **76.0/180** | |
| **Normalized Total** | | | **42.2/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 2/10 (threshold: ≤3). SCLY is a cytosolic enzyme with no credible nuclear localization evidence.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cytoplasm, cytosol | Computational (ECO:0000250) |
| PhosphoSitePlus | Cytosol, Golgi apparatus | Curated |
| InnateDB | Cytoplasm, cytosol | Curated |
| dbPTM | Cytoplasm, cytosol | Curated |
| HumanCyc (MetaCyc) | Cytosol, Golgi apparatus | Database |

**Manual Review Assessment**: SCLY is annotated exclusively as a cytoplasmic/cytosolic protein across all major databases. UniProt lists cytoplasm and cytosol as its subcellular location. PhosphoSitePlus adds Golgi apparatus but no nuclear annotation. The protein's function -- catalyzing the decomposition of L-selenocysteine to L-alanine and elemental selenium (PLP-dependent) -- is a metabolic reaction occurring in the cytosol. Some commercial antibody suppliers list both "Cytoplasm, Nucleus" but this reflects non-specific antibody detection rather than bona fide nuclear localization. No GO-CC nuclear terms are annotated. Nuclear localization score 2/10 reflects the complete absence of credible nuclear evidence from primary databases.

### 4. Protein Size Assessment

SCLY is approximately 445 amino acids, well within the ideal range for experimental characterization. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~50-70 articles |
| Novelty category | 41-80 -> Score 6 |

SCLY research focuses on selenium metabolism -- the enzyme releases selenium from selenocysteine for selenoprotein biosynthesis. The gene has been studied in the context of selenium homeostasis, redox biology, and metabolic pathways. Research activity is moderate but not extensive. Score 6/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (standard prediction) |
| PDB Entries | 0 (no experimental structures) |
| Domain Architecture | PLP-dependent transferase (fold type I) |

No experimental structural data exists. AlphaFold prediction is available but without specific pLDDT statistics from harvest data. The enzyme belongs to the PLP-dependent transferase superfamily, suggesting a well-folded catalytic domain. Score 5/10 reflects standard AlphaFold availability without experimental validation or domain-based structural confidence.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| Pfam | PLP-dependent transferase | Pyridoxal phosphate-dependent enzyme superfamily |
| InterPro | PLP-dependent enzyme | Catalytic domain for selenocysteine decomposition |

SCLY is a metabolic enzyme with a PLP-dependent catalytic domain. It lacks any known regulatory domains (no kinase, phosphatase, ubiquitin ligase, transcription factor, or chromatin-modifying domains). Its function is purely metabolic, with no direct connection to transcriptional regulation, chromatin modification, or signal transduction. Score 2/10 reflects the absence of regulatory domain architecture.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Limited data; metabolic enzyme network |
| IntAct | Limited interactions expected |
| Known Partners | Selenium metabolism partners (SEPHS2, selenoproteins) |

As a metabolic enzyme, SCLY's PPI network is expected to be sparse and functionally restricted to selenium metabolism. No high-confidence regulatory or signaling interactions are documented. Score 3/10 reflects limited PPI characterization.

### 9. Cross-Validation Analysis

No cross-validation bonus: all databases consistently annotate SCLY as cytosolic, and the lack of structural or PPI cross-validation opportunities precludes bonus points. Cross-validation bonus: +0.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED)

**Primary Rejection Reason**: SCLY is a cytosolic metabolic enzyme with no credible nuclear localization evidence. Its function in selenium metabolism is well-defined and exclusively cytoplasmic. No database or experimental study supports nuclear localization. The protein lacks regulatory domains and has no connection to transcriptional regulation or chromatin biology.

### 11. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 2/10 (threshold: ≤3 → REJECTED). SCLY is a selenium metabolism enzyme operating entirely in the cytosol. Its exclusion from the TE-regulation screen is confident and irreversible based on the absence of nuclear localization.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96I15
- PhosphoSitePlus: https://www.phosphosite.org/overviewExecuteAction?id=12757
- dbPTM: https://awi.cuhk.edu.cn/dbPTM/info.php?id=SCLY_HUMAN
- InnateDB: http://innatedb.com/getProteinCard.do?id=292857
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCLY
- Note: Harvest packet not available; data compiled from web database queries
