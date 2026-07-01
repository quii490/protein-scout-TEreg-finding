---
type: gene-evaluation
gene: DFFA
date: 2026-06-28
tags: [nucleoplasm, chromatin, apoptosis, DNA-fragmentation, caspase-pathway]
status: shortlisted
---

# DFFA - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DFFA |
| **UniProt Accession** | O00273 |
| **Protein Name** | DNA fragmentation factor subunit alpha |
| **Protein Length** | 331 aa |
| **Molecular Function** | Inhibitor of caspase-activated DNase (DFF40) |
| **Chromosome** | 1p36.22 |
| **PubMed Hits** | 179 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×4 | ×4 | 16 | Well-annotated nuclear protein |
| **GO-CC: Nucleoplasm** | ×4 | ×1 | 4 | Nucleoplasm annotation |
| **GO-CC: Chromatin** | ×4 | ×5 | 20 | Direct chromatin association |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×3 | ×2 | 6 | EWSR1 (nuclear RNA-binding), YWHAZ (14-3-3) |
| **Literature Evidence** | ×4 | ×3 | 12 | Well-studied apoptosis factor (179 pubs) |
| **Total** | | | **61** | |



| **加权总分** | | | **61.0/180** | |
| **归一化总分 (÷1.83)** | | | **33.3/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DFFA (DNA fragmentation factor subunit alpha, also known as ICAD - Inhibitor of Caspase-Activated DNase) is the regulatory subunit of the DFF complex. In non-apoptotic cells, DFFA acts as an inhibitor of DFFB (DFF40/CAD), the caspase-activated deoxyribonuclease. Upon apoptosis induction, caspase-3 cleaves DFFA, releasing active DFFB which translocates to the nucleus and fragments chromosomal DNA into nucleosomal units, a hallmark of apoptosis.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Nucleus (GO:0005634), Nucleoplasm (GO:0005654), Chromatin (GO:0000785), Cytosol (GO:0005829)
- **UniProt annotation**: "Cytoplasm" (primary)
- DFFA shuttles between cytoplasm and nucleus depending on apoptotic state
- In complex with DFFB, it gains access to chromatin where it regulates DNA fragmentation
- The chromatin and nucleoplasm GO-CC annotations demonstrate direct nuclear chromatin access

### 3.3 Domain Architecture
DFFA is a 331 aa protein with two caspase-3 cleavage sites (D117 and D224). Cleavage at both sites is required for full release of DFFB nuclease activity. The N-terminal region mediates interaction with DFFB (CIDE-N domain), while the C-terminal region contains the inhibitory domain.

### 3.4 Protein-Protein Interactions
- **DFFB (DFF40/CAD)**: Primary binding partner; DFFA is the inhibitory chaperone of DFFB
- **EWSR1 (EWS RNA-binding protein 1)**: Nuclear RNA-binding protein involved in transcription and splicing
- **NECAB2**: Neuronal calcium-binding protein
- **YWHAZ (14-3-3 zeta)**: Scaffold protein that can regulate DFFA localization
- Caspase-3: Cleaves DFFA to activate apoptosis

### 3.5 Relevance to TE Regulation
DFFA is relevant to TE regulation through multiple mechanisms:
- Chromatin fragmentation during apoptosis can release TE-derived sequences as cell-free DNA
- DFFA-regulated DNase activity may process TE-derived DNA structures
- Apoptotic DNA fragmentation machinery interfaces with chromatin organization, including TE-rich heterochromatic regions
- Caspase activation pathways that regulate DFFA are connected to DNA damage responses triggered by TE activity

## 4. Overall Assessment

**Classification: nucleoplasm** - Well-characterized nuclear protein with direct chromatin association. The cytoplasmic localization represents the inactive pre-apoptotic state; the functional nuclear localization on chromatin is the biologically relevant state for TE regulation.

**Strengths**:
- Well-studied protein (179 publications)
- Clear mechanistic function in chromatin-level DNA processing
- Direct chromatin interaction
- Caspase-dependent regulation provides a switch-like mechanism

**Weaknesses**:
- Primary function is in apoptosis, not steady-state TE regulation
- Functional nuclear localization is conditional (apoptosis-dependent)
- No HPA data for steady-state localization
- Nuclear role is destructive (DNA fragmentation) rather than regulatory

**Recommendation: Shortlist for TE regulation evaluation.** DFFA provides a link between apoptosis and chromatin-level DNA processing. TE sequences released during apoptotic DNA fragmentation could serve as innate immune stimuli. The conditional nuclear localization (apoptosis-triggered) is a valid nuclear targeting mechanism worth evaluating.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CAD | STRING | 999 |
| DFFB | STRING | 999 |
| CASP3 | STRING | 992 |
| GZMB | STRING | 966 |
| CASP7 | STRING | 716 |
| CASP6 | STRING | 709 |
| EWSR1 | BioGRID | 1 |
| YWHAZ | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000160049-DFFA

![](https://images.proteinatlas.org/19938/369_G6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/369_G6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/364_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/364_G6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/365_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/365_G6_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000160049-DFFA

![](https://images.proteinatlas.org/19938/369_G6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/369_G6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/364_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/364_G6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/365_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/365_G6_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000160049-DFFA

![](https://images.proteinatlas.org/19938/369_G6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/369_G6_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/364_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/364_G6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/365_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19938/365_G6_3_blue_red_green.jpg)

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DFFA

## 5. Data Sources

- UniProt: O00273 (accessed 2026-06-28 via REST API)
- GO-CC: nucleus (GO:0005634), nucleoplasm (GO:0005654), chromatin (GO:0000785), cytosol (GO:0005829)
- BioGRID PPI: human PPI dataset (DFFB, EWSR1, NECAB2, YWHAZ interactions)
- PubMed: 179 total hits (e.g., PMID: 10716926, 10336446, 9880528)
- HPA: unclassified_bare (no nuclear localization data)
