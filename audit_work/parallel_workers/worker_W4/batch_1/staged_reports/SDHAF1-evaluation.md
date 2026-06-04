---
type: protein-evaluation
gene: "SDHAF1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "Nuclear localization score ≤3 (mitochondrial assembly factor)"
---

## SDHAF1 -- Re-evaluation Report (REJECTED: Mitochondrial Protein, No Nuclear Function)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SDHAF1 / LYRM8, Succinate dehydrogenase assembly factor 1 |
| Protein Name | Succinate dehydrogenase assembly factor 1, mitochondrial (LYR motif-containing protein 8) |
| Protein Size | ~115 aa |
| UniProt ID | A6NFY7 (SDHF1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Web database queries (no harvest packet available) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | Mitochondrion matrix exclusively; no nuclear annotation |
| Protein Size | 10/10 | x1 | **10** | ~115 aa, small and tractable |
| Research Novelty | 8/10 | x5 | **40** | Estimated ~20-30 PubMed articles |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold predicted; LYR motif; no experimental PDB |
| Regulatory Domains | 2/10 | x2 | **4** | LYR motif (Fe-S cluster assembly); no regulatory domains |
| PPI Network | 4/10 | x3 | **12** | SDH complex partners; Fe-S cluster transfer machinery |
| Cross-Validation Bonus | -- | -- | **+0** | Consistent mitochondrial annotation; no nuclear evidence |
| **Raw Total** | | | **82.0/180** | |
| **Normalized Total** | | | **45.6/100** | |

**FINAL DECISION: REJECTED. Nuclear localization score 1/10 (threshold: ≤3). SDHAF1 is a mitochondrial matrix protein with no nuclear function or localization.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Mitochondrion matrix | Probable |
| GO-CC | Mitochondrion (GO:0005739) | Database annotation |
| GO-CC | Mitochondrial matrix (GO:0005759) | Database annotation |
| PhosphoSitePlus | Mitochondrion | Curated |
| MitoTox | Mitochondrion | Database |

**Manual Review Assessment**: SDHAF1 is exclusively a mitochondrial protein. It functions in the assembly of succinate dehydrogenase (SDH, Complex II of the mitochondrial electron transport chain). Specifically, it promotes maturation of the iron-sulfur protein subunit SDHB by protecting it from oxidants and contributing to Fe-S cluster incorporation. This function occurs entirely within the mitochondrial matrix. The LYR motif (Leu-Tyr-Arg) is a signature of mitochondrial Fe-S cluster assembly factors. No database or experimental study annotates nuclear localization. Any nuclear detection would represent mislocalization artifact. Nuclear localization score 1/10 reflects unequivocal mitochondrial localization with zero nuclear evidence.

### 4. Protein Size Assessment

SDHAF1 is approximately 115 amino acids, a small protein amenable to structural and biochemical studies. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed estimated count | ~20-30 articles |
| Novelty category | 21-40 -> Score 8 |

SDHAF1 was identified in the context of mitochondrial complex II assembly. Research focuses on its role in Fe-S cluster incorporation into SDHB and its link to mitochondrial disease (SDH-deficient paraganglioma/pheochromocytoma). Research activity is limited to mitochondrial biology. Score 8/10.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 0 (no experimental structures) |
| Domain | LYR motif (Fe-S cluster assembly factor family) |

Standard AlphaFold prediction available. The small size (~115 aa) and LYR motif suggest a simple fold. No experimental structural data. Score 4/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| Pfam | LYR motif | Mitochondrial Fe-S cluster assembly factor family |
| InterPro | Complex1_LYR-like | LYR family involved in respiratory chain assembly |

SDHAF1 contains the LYR motif (named after a conserved Leu-Tyr-Arg tripeptide), characteristic of mitochondrial respiratory chain assembly factors. The motif is functionally specialized for Fe-S cluster protein maturation. No regulatory domains (no kinase, phosphatase, DNA-binding, or chromatin domains). Score 2/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| Known Partners | SDHB (substrate), HSC20/HSPA9/ISCU (Fe-S transfer complex) |
| STRING | Respiratory chain assembly network expected |

Limited PPI data centered on SDH complex assembly partners. No nuclear or regulatory interactions. Score 4/10.

### 9. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED)

**Primary Rejection Reason**: SDHAF1 is a mitochondrial matrix protein dedicated to respiratory chain complex II assembly. It has no nuclear localization, no DNA-binding domains, no transcriptional regulatory function, and no connection to chromatin biology or TE regulation. The rejection is confident and irreversible.

### 10. Decision

**FINAL DECISION: REJECTED.** Nuclear localization score 1/10. SDHAF1's mitochondrial function excludes it from TE-regulation screening.

### 11. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/A6NFY7
- MitoTox: https://www.mitotox.org/targets/19922/detail/
- PhosphoSitePlus: https://www.phosphosite.org/overviewExecuteAction?id=19108034
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SDHAF1
- Note: Harvest packet not available; data compiled from web database queries
