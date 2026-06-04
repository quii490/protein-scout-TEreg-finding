---
type: protein-evaluation
gene: "RXRA"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RXRA -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RXRA / NR2B1, RXR-alpha |
| Protein Name | Retinoic Acid Receptor RXR-alpha (Retinoid X Receptor Alpha) |
| Protein Size | 462 aa / ~51 kDa |
| UniProt ID | P19793 (RXRA_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | Previously unscored; flagged for re-evaluation |
| Re-evaluation Reason | Complete re-evaluation per batch recovery protocol |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 10/10 | x4 | **40** | Classic nuclear receptor; predominantly nuclear; extensively documented |
| Protein Size | 10/10 | x1 | **10** | 462 aa, within ideal range |
| Research Novelty | REJECTED | x5 | **--** | PubMed >5,000-10,000+ articles; >100 threshold exceeded |
| 3D Structure | 10/10 | x3 | **30** | 25+ experimental PDB entries including ligand-bound and DNA-bound structures |
| Regulatory Domains | 10/10 | x2 | **20** | Nuclear receptor superfamily; DBD + LBD + AF-1/AF-2; heterodimerization |
| PPI Network | 10/10 | x3 | **30** | Extensive heterodimerization partners (RARs, VDR, TR, PPARs, LXRs, FXR) |
| Cross-Validation Bonus | -- | -- | **+3.0** | Multi-DB nuclear localization (+0.5); PDB + AlphaFold (+0.5); STRING + IntAct (+0.5); Domain multi-DB (+0.5); Broad pathway integration (+1.0) |
| **Normalized Total** | | | **N/A** | REJECTED for PubMed >100 |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus | Reviewed, experimental |
| GO-CC | Nucleus (GO:0005634) | Multiple evidence codes |
| GO-CC | Nucleoplasm | IDA, TAS |
| GeneCards | Nucleus | Tier1, high confidence |
| PhosphoSitePlus | Nucleus | Experimental |
| HPA | Nuclear | Approved |

**HPA IF Status**: HPA IF data available; nuclear localization confirmed.

**Manual Review Assessment**: RXRA is the prototypical nuclear receptor. It functions as a ligand-dependent transcription factor that heterodimerizes with multiple other nuclear receptors (RARs, VDR, TR, PPARs, LXRs, FXR, etc.) to regulate gene expression. Its nuclear localization is unequivocal and extensively documented across decades of research and thousands of publications. As a member of the nuclear receptor superfamily, it contains a DNA-binding domain (DBD) with zinc finger motifs that directly mediate sequence-specific DNA binding in the nucleus. Nuclear localization score: 10/10. However, this score is superseded by the PubMed rejection criterion.

### 4. Protein Size Assessment

RXRA is 462 amino acids, well within the ideal range. Multiple crystal structures of various domains and full-length constructs are available. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed total articles | >5,000 (est. 5,000-10,000+) |
| Novelty category | >100 -> REJECTED |

**REJECTION TRIGGER**: PubMed count exceeds 100 threshold by a massive margin. RXRA is one of the most extensively studied transcription factors in biology. As the obligate heterodimerization partner for numerous nuclear receptors, it has been studied in virtually every biological context: development, metabolism, cancer, immunology, neuroscience, circadian rhythm, and more. Key research areas include:

- Retinoid signaling and vitamin A biology
- Cancer (RXRA as tumor suppressor and oncogene)
- Metabolic syndrome and diabetes (PPAR-RXR heterodimers)
- Circadian rhythm regulation
- Drug target for bexarotene and other rexinoids
- Structural biology (RXR-ligand interactions, DNA recognition)
- Embryonic development and organogenesis

RXRA is the subject of hundreds of reviews, dozens of clinical trials, and is a well-established drug target. There is no meaningful novelty premium for a protein of this research intensity.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| PDB Entries | 25+ experimental structures |
| Structural Coverage | DBD (zinc fingers), LBD (ligand-binding domain), full-length with DNA |
| Methods | X-ray crystallography, NMR, Cryo-EM |
| Key Structures | RXR-LXR heterodimer on DNA, RXR-RAR heterodimer, RXR-PPAR, RXR with agonists/antagonists |

RXRA has extensive experimental structural characterization. The DNA-binding domain (zinc finger modules), ligand-binding domain (with multiple ligands including 9-cis-retinoic acid, bexarotene, and synthetic rexinoids), and heterodimer interfaces have all been structurally resolved at high resolution. Score 10/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | Nuclear hormone receptor, ligand-binding domain | IPR000536 |
| InterPro | Nuclear hormone receptor, DNA-binding domain | IPR001628 |
| InterPro | Zinc finger, nuclear hormone receptor-type | IPR001723 |
| Pfam | Ligand-binding domain of nuclear hormone receptor | PF00104 |
| Pfam | Zinc finger, C4 type | PF00105 |
| PROSITE | Nuclear receptors signatures | Multiple |

RXRA contains the canonical nuclear receptor domain architecture: N-terminal AF-1 (activation function 1) domain, central DNA-binding domain (DBD) with two C4-type zinc fingers, hinge region, C-terminal ligand-binding domain (LBD) containing AF-2 (activation function 2), and heterodimerization interface. This is the archetypal regulatory domain architecture of the nuclear receptor superfamily. Score 10/10.

### 8. PPI Network Analysis

RXRA is the central hub of the nuclear receptor interactome. It forms obligate heterodimers with:
- RAR-alpha/beta/gamma (retinoic acid receptors)
- VDR (vitamin D receptor)
- TR-alpha/beta (thyroid hormone receptors)
- PPAR-alpha/delta/gamma (peroxisome proliferator-activated receptors)
- LXR-alpha/beta (liver X receptors)
- FXR (farnesoid X receptor)
- PXR (pregnane X receptor)
- CAR (constitutive androstane receptor)
- NURR1 (nuclear receptor related 1)

Additionally, it interacts with corepressors (N-CoR, SMRT), coactivators (SRC-1, p300/CBP), and components of the basal transcription machinery. The PPI network is one of the most extensively characterized in biology. Score 10/10.

### 9. Cross-Validation Analysis

All dimensions of RXRA biology are cross-validated across dozens of databases, thousands of publications, and multiple experimental approaches. The cross-validation bonus would be maximal for any gene: multi-DB nuclear localization (+0.5), PDB + AlphaFold structural validation (+0.5), STRING + IntAct PPI cross-validation (+0.5), multi-DB domain annotation (+0.5), and broad pathway integration across multiple nuclear receptor signaling pathways (+1.0). Total bonus: +3.0 (maximum). These scores are academic since the gene is rejected for PubMed count.

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (REJECTED for PubMed >100)

**Core Strengths**:
1. Quintessential nuclear protein with decades of experimental validation
2. Outstanding structural characterization (25+ PDB entries)
3. Canonical regulatory domain architecture (nuclear receptor superfamily)
4. Hub of the nuclear receptor interactome
5. Well-established drug target

**Fatal Weakness for Our Screening Purpose**:
1. PubMed count >5,000 vastly exceeds the 100-article rejection threshold
2. One of the most extensively studied proteins in biology
3. No novelty premium whatsoever
4. Established drug target -- competitive research landscape
5. Extensive prior art in every conceivable biological context

### 11. Decision

**FINAL DECISION**: REJECTED. PubMed count >100 (estimated >5,000 articles). RXRA is a classic nuclear receptor and one of the most intensely studied transcription factors in biology. While it would score maximum points on nuclear localization, structure, domains, and PPI, the complete absence of research novelty is disqualifying for our screening objectives. As an established drug target with thousands of publications, RXRA offers no opportunity for novel discovery in the context of TE-regulated nuclear protein screening. The gene fails the PubMed >100 rejection criterion.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P19793
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RXRA
- PDB: https://www.rcsb.org/search?q=RXRA
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=RXRA
- Note: Harvest packet not available; RXRA is extremely well-characterized; data compiled from public databases
