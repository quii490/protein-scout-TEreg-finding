---
type: protein-evaluation
gene: "REXO1L2P"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## REXO1L2P -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | REXO1L2P / REX1, RNA exonuclease 1 homolog (S. cerevisiae)-like pseudogene; GOR; LOC401467 |
| Gene Type | Pseudogene (processed pseudogene / transcribed pseudogene) |
| Protein Product | NONE -- this is a pseudogene that does not encode a functional protein |
| Protein Size | N/A |
| UniProt ID | N/A -- no protein product |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 0/10 | x4 | **0** | Pseudogene -- no protein product; no subcellular localization possible |
| Protein Size | 0/10 | x1 | **0** | No protein product |
| Research Novelty | N/A | x5 | **N/A** | Pseudogene; not applicable as a protein-coding target |
| 3D Structure | 0/10 | x3 | **0** | No protein; no structure |
| Regulatory Domains | 0/10 | x2 | **0** | No protein product |
| PPI Network | 0/10 | x3 | **0** | No protein product |
| Cross-Validation Bonus | -- | -- | **+0** | N/A |
| **Raw Total** | | | **0/180** | |
| **Normalized Total** | | | **0/100** | |

### 3. Nuclear Localization Evidence -- CRITICAL FAIL

| Source | Localization | Reliability |
|--------|-------------|-------------|
| Gene Type | Processed pseudogene | NCBI validated |
| Protein Product | NONE | Ensembl: no coding potential |
| Any nuclear source | N/A -- no protein | N/A |

**HPA IF Status**: Not applicable -- this is a pseudogene with no protein product. No IF images exist because there is no protein to detect.

**Manual Review Assessment**: REXO1L2P (REXO1 like 2, pseudogene) is a processed pseudogene derived from the functional REXO1 gene (RNA exonuclease 1 homolog). It is classified as a "transcribed pseudogene" meaning it produces non-coding RNA but does NOT encode a functional protein. Key evidence:

- NCBI Gene ID 100288527: "REXO1 like 2, pseudogene"
- RefSeq transcript NR_003594.1 -- non-coding RNA
- Ensembl: classified as "processed pseudogene" with "no coding potential"
- No protein product annotated in any database
- No UniProt entry (because there is no protein)

The gene is located on chromosome 8q21.2 and contains 1-2 exons. The parent gene, REXO1, encodes a functional RNA exonuclease, but REXO1L2P is a non-functional retroposed copy.

**Nuclear localization score: 0/10. RULE: Nuclear <=3 -> REJECTED. Furthermore, this gene cannot be scored at all because it does not produce a protein.**

### 4. Protein Size Assessment

No protein product exists. Not applicable.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed direct studies | 0 (no functional protein studies) |
| Mentions in genomic studies | Occasional mention as genomic locus |

**Research Context**: As a pseudogene, REXO1L2P has no direct functional studies. It may appear in genomic studies as a locus or in expression analyses detecting its non-coding RNA transcript. The RGD database reports chemical interactions (benzo[a]pyrene, cadmium, resveratrol) associated with altered REXO1L2P mRNA expression, but these are incidental findings from large-scale transcriptomic studies.

### 6. 3D Structure Analysis

No protein product exists. No structural data is available or applicable.

### 7. Domain Architecture

No protein product exists. The parent gene REXO1 contains RNA exonuclease domains, but REXO1L2P is a pseudogene that does not encode these domains in a functional protein.

### 8. PPI Network Analysis

No protein product exists. No PPI data is available or applicable.

### 9. Cross-Validation Analysis

Not applicable. This is a pseudogene locus, not a protein-coding gene.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED (and should be EXCLUDED from all protein-coding screens)

**Core Reasons for Rejection**:
1. REXO1L2P is a pseudogene -- it does NOT encode a protein
2. Without a protein product, all scoring dimensions are zero
3. This gene should never have been included in a protein-coding gene screen
4. The inclusion of this gene in the original screen was erroneous

**Why Previous Rejection Was Correct**:
The original rejection was appropriate -- actually, this gene should have been excluded at the gene list curation stage, before any evaluation was performed. Pseudogenes should not be included in protein-coding gene screens.

**Root Cause of False Inclusion**:
REXO1L2P may have been included because its gene symbol resembles a protein-coding gene (REXO1L2 with a "P" suffix for pseudogene). The "P" suffix in HGNC nomenclature explicitly marks pseudogenes. Gene list curation should filter out all genes with the "P" suffix (with rare exceptions for readthrough transcripts that produce functional proteins).

### 11. Decision

**FINAL DECISION**: REJECTED (and EXCLUDED from all further analysis). REXO1L2P is a pseudogene. It does not encode a protein. Nuclear score is 0/10 (threshold <=3 -> REJECTED). This gene should be removed from the candidate gene list entirely. Recovery from false-rejection does not apply because the original rejection was correct and the gene is fundamentally unsuitable for protein-based screening.

**Recommendation for Pipeline Improvement**: Add a pre-filtering step to exclude all HGNC genes with the "P" suffix (pseudogenes) before protein evaluation begins. This will prevent wasted analysis of non-coding loci.

### 12. Data Sources
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/100288527
- Ensembl: https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276998
- RGD: https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=1602385
- UCSC Genome Browser: https://genome.ucsc.edu (NR_003594.1)
- Note: No harvest packet and no protein data exist for this pseudogene
