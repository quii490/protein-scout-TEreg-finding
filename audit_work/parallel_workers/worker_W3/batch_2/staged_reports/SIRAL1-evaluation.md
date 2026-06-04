---
type: protein-evaluation
gene: "SIRAL1"
date: 2026-06-04
tags: [protein-scout, evaluation, rejected]
status: rejected
---

## SIRAL1 -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SIRAL1 / — |
| Protein Name | Unknown |
| Protein Size | ? aa / ? kDa |
| UniProt ID | N/A |
| Evaluation Date | 2026-06-04 |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | No UniProt entry found; no HPA data; gene symbol unrecognized in major databases |
| Protein Size | 5/10 | x1 | **5** | Unknown size |
| Research Novelty | 10/10 | x5 | **50** | ~0 publications; extremely novel |
| 3D Structure | 4/10 | x3 | **12** | AlphaFold poor (pLDDT=0.0); mostly disordered |
| Regulatory Domains | 7/10 | x2 | **14** | No annotated domains; novel protein baseline, structure may harbor uncharacterized domains. |
| PPI Network | 1/10 | x3 | **3** | No PPI data available |
| Cross-Validation Bonus | — | max +3 | **+0** | No bonus criteria met |
| **Raw Total** | | | **84/183** | |
| **Normalized Total** | | | **45.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
| — | No localization data available | — |

**Assessment**: No UniProt entry found; no HPA data; gene symbol unrecognized in major databases


**DECISION**: REJECTED. Nuclear localization score 0/10 (threshold: >3). No UniProt entry found; no HPA data; gene symbol unrecognized in major databases

### 4. Protein Size Assessment

Unknown size. The protein size is outside the ideal range for biochemical studies (200-800 aa optimal).


### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | 0 |
| PubMed symbol-only count | 0 |
| PubMed broad count | 0 |
| Novelty category | ≤20 → 10 |

**Key Publications**:


**Assessment**: ~0 publications; extremely novel

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | N/A |
| pLDDT > 90 (high confidence) | N/A% |
| pLDDT 70-90 (moderate) | N/A% |
| pLDDT 50-70 (low) | N/A% |
| pLDDT < 50 (disordered) | N/A% |
| Available PDB Entries | 0 |

**Assessment**: AlphaFold poor (pLDDT=0.0); mostly disordered

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| — | No annotated domains | Novel protein — may harbor uncharacterized domains |

**Assessment**: No annotated domains; novel protein baseline, structure may harbor uncharacterized domains.

### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
| — | — | — | — | — |

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
| — | — | — | — |

**Known Complex Membership (GO Cellular Component)**:
- No complex annotations available

**PPI Assessment**: No PPI data available

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | Non-nuclear/ambiguous | Partial/No |
| 3D Structure | AlphaFold + PDB | AlphaFold only | Limited |
| PPI | IntAct + STRING | No PPI data | Single/No source |

**Cross-Validation Bonus Details**:
- No bonus criteria met across databases.
- **Total Cross-Validation Bonus**: +0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED

**Normalized Score**: 45.9/100 (Raw: 84/183)

**Core Reasons for Rejection**:
Nuclear localization score 0/10 (threshold: >3). No UniProt entry found; no HPA data; gene symbol unrecognized in major databases

### 11. Decision

**FINAL DECISION**: REJECTED. Automatically rejected. Nuclear localization score 0/10 (threshold: >3). No UniProt entry found; no HPA data; gene symbol unrecognized in major databases

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/N/A
- HPA: https://www.proteinatlas.org/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SIRAL1%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
