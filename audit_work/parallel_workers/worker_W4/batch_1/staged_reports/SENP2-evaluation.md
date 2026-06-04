---
type: protein-evaluation
gene: "SENP2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, batch-recovery]
status: rejected
rejection_reason: "PubMed strict count 137 > 100 (well-studied protein)"
---

## SENP2 -- Re-evaluation Report (REJECTED: PubMed Count >100)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | SENP2 / KIAA1331 |
| Protein Name | Sentrin-specific protease 2 (SUMO-specific protease 2) |
| Protein Size | 589 aa, 67.9 kDa |
| UniProt ID | Q9HC62 (SENP2_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Data Source | Full harvest packet available |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 8/10 | x4 | **32** | Nuclear pore complex, nuclear membrane, nucleoplasm; strong multi-DB consensus |
| Protein Size | 8/10 | x1 | **8** | 589 aa, slightly large but tractable |
| Research Novelty | 0/10 | x5 | **0** | **PubMed strict=137 (>100 -> AUTO REJECT)** |
| 3D Structure | 10/10 | x3 | **30** | 8 experimental PDB entries (X-ray, 2.15-3.20 A); AlphaFold available |
| Regulatory Domains | 8/10 | x2 | **16** | Ulp1 protease domain (PF02902); SUMO deconjugation activity |
| PPI Network | 8/10 | x3 | **24** | Strong SUMO pathway network; SUMO1-3, RANGAP1, NUP153, nuclear pore partners |
| Cross-Validation Bonus | -- | -- | **+2.0** | Nuclear localization consensus (+1.0); PDB + domain consistency (+1.0) |
| **Raw Total** | | | **120.0/180** | (Scored for completeness despite auto-rejection) |
| **Normalized Total** | | | **66.7/100** | |

**FINAL DECISION: REJECTED. PubMed strict count 137 > 100 threshold. SENP2 is a well-studied SUMO protease with extensive literature. Auto-rejection applies regardless of other scoring dimensions per the "PubMed>100→REJECTED" rule.**

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Nucleus, nuclear pore complex | Experimental (ECO:0000269) |
| UniProt (Swiss-Prot) | Nucleus membrane | Experimental (ECO:0000269) |
| UniProt (Swiss-Prot) | Cytoplasm | Experimental (ECO:0000269) |
| GO-CC | Nuclear pore (IDA), nucleoplasm (TAS), nuclear membrane (IEA), nucleus (IBA), PML body (IEA), cytosol (IDA) | Multiple high-evidence terms |
| HPA IF | Cytosol | Reliability: Supported |

**Manual Review Assessment**: SENP2 has robust nuclear localization evidence. UniProt confirms nuclear pore complex and nuclear membrane localization with experimental evidence (ECO:0000269). GO-CC annotates nuclear pore (IDA, direct assay), nucleoplasm (TAS, traceable author statement), nucleus (IBA, inferred from biological aspect of ancestor), and PML body (IEA). The HPA IF data shows cytosol localization with "Supported" reliability, but this likely reflects the dynamic nucleocytoplasmic shuttling known for SUMO proteases. The N-terminal domain mediates nuclear envelope localization, while the C-terminal catalytic domain contains the active site. Overall nuclear evidence is strong and multi-source. Score 8/10 reflects strong nuclear evidence with the caveat of dynamic shuttling.

### 4. Protein Size Assessment

SENP2 is 589 amino acids (67.9 kDa), somewhat large but still within a tractable range for biochemical studies. The catalytic domain alone (residues 364-589, ~226 aa) can be expressed independently and has been crystallized. Size score: 8/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | **137 articles** |
| PubMed broad count | 249 articles |
| Novelty category | **>100 -> AUTO REJECT** |

SENP2 has been extensively studied since its discovery in 2000. Research covers its role in SUMO processing and deconjugation, nuclear pore association, Wnt pathway modulation (via CTNNB1 desumoylation), adipogenesis (CEBPB stabilization), cGAS-STING pathway regulation, and myocardial ischemia-reperfusion injury. With 137+ PubMed articles and 8 experimental PDB structures, SENP2 is a mature, well-characterized target with limited discovery potential. Auto-rejection for PubMed >100.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available (AF-Q9HC62-F1, v6) |
| PDB Entries | 8 experimental structures (X-ray) |
| Mean pLDDT | 62.1 |
| pct pLDDT >90 | 37.4% |
| pct pLDDT <50 | 50.9% |

SENP2 has exceptional structural coverage with 8 experimental PDB entries at resolutions ranging from 2.15 A to 3.20 A. These all cover the C-terminal catalytic domain (residues ~364-589). The AlphaFold prediction shows a moderate mean pLDDT (62.1), with 50.9% of residues below pLDDT 50, likely reflecting the N-terminal disordered region involved in nuclear envelope targeting. The crystallized catalytic domain is well-characterized. Score 10/10 reflects the abundance of experimental structural data.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR038765 | Papain-like cysteine peptidase superfamily |
| InterPro | IPR003653 | Ulp1 protease family, C-terminal catalytic domain |
| Pfam | PF02902 | Ulp1 protease family (C-terminal catalytic domain) |

SENP2 contains a C-terminal Ulp1 protease domain (PF02902) responsible for SUMO processing and deconjugation. The N-terminal region (~1-363) mediates subcellular localization to the nuclear pore complex and nuclear envelope but is predicted to be largely disordered (consistent with low AlphaFold pLDDT). The catalytic domain is a cysteine protease with a conserved catalytic triad. The domain architecture directly supports nuclear function through the N-terminal targeting domain and enzymatic function through the C-terminal protease domain. Score 8/10.

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | Top partners: SUMO1 (0.997, exp 0.983), SUMO2 (0.995, exp 0.985), RANGAP1 (0.989), NUP153 (0.981), SUMO3 (0.981) |
| IntAct | 15 interactors: CDK5RAP2, SUMO1 (X-ray crystallography), IKBKG, SMAD2, CANX, CCT6A, PB2 (viral) |
| UniProt Interactions | 20 interactors: SUMO1, SUMO2, SUMO3 (multiple experiments), KASH5 (6 experiments) |

SENP2 has a rich and well-characterized PPI network centered on the SUMO pathway. The strongest interactions are with SUMO1-3 (combined scores >0.98, experimental >0.9), consistent with its enzymatic function. Nuclear pore partners (NUP153, NUP133) and nuclear transport factors (KPNB1, IPO5, RANBP6) support its nuclear envelope localization. The DVL family interactions (0.91) link SENP2 to Wnt signaling. STRING network is dense and biologically coherent. Score 8/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + GO-CC + STRING | Nuclear pore/membrane/nucleoplasm | Multi-DB consensus |
| Structure | AlphaFold + 8 PDB entries | Well-characterized catalytic domain | Consistent |
| PPI | STRING + IntAct + UniProt | SUMO pathway network | Dense and coherent |

**Cross-Validation Bonus Details**:
- Multi-database nuclear localization consensus (UniProt experimental + GO-CC IDA): +1.0
- PDB structural data cross-validated with domain architecture: +1.0
- STRING + IntAct PPI cross-validation: +0 (already accounted in PPI scoring)
- **Total Cross-Validation Bonus**: +2.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED (AUTO-REJECTED: PubMed >100)

**Primary Rejection Reason**: PubMed strict count of 137 exceeds the 100-article threshold. SENP2 is a mature research target with extensive literature spanning SUMO biology, nuclear transport, Wnt signaling, adipogenesis, cGAS-STING immunity, and ischemia-reperfusion injury. Despite excellent nuclear localization credentials (score 8/10), high-quality structural data (8 PDB entries), and a well-characterized PPI network, SENP2 cannot pass the novelty filter. The protein is too well-studied to offer significant discovery potential for a TE-regulation focused project.

### 11. Decision

**FINAL DECISION: REJECTED.** PubMed strict count 137 > 100 threshold. The auto-rejection rule "PubMed>100→REJECTED" applies regardless of other scoring dimensions. SENP2 would otherwise score 120/180 (66.7/100) with strong nuclear localization, excellent structural data, and a rich PPI network. The rejection is based solely on excessive prior research (low novelty), which is considered disqualifying for a discovery-oriented TE-regulation screen. No appeal pathway: this rejection is final and irreversible.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9HC62
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HC62
- STRING: https://string-db.org/network/9606.ENSP00000330929
- HPA: https://www.proteinatlas.org/ENSG00000163904-SENP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SENP2%22
- Harvest Packet: SENP2.json (full data available)
