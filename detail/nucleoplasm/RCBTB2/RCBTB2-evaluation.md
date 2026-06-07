---
type: protein-evaluation
gene: "RCBTB2"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RCBTB2 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RCBTB2 / CHC1L, RLG |
| Protein Name | RCC1 and BTB domain-containing protein 2 |
| Protein Size | 551 aa / 60.3 kDa |
| UniProt ID | O95199 |
| Evaluation Date | 2026-06-04 |
| Re-evaluation Reason | Recovery from previous false-rejection; full data re-harvest and manual review |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 4/10 | x4 | **16** | HPA: Nucleoplasm + Golgi apparatus (Approved); UniProt: Cytoplasmic vesicle, secretory vesicle, acrosome; GO-CC: acrosomal vesicle + cytoplasm |
| Protein Size | 10/10 | x1 | **10** | 551 aa, within ideal range (200-800 aa) |
| Research Novelty | 10/10 | x5 | **50** | PubMed strict count = 20 (<=20 -> 10) |
| 3D Structure | 8/10 | x3 | **24** | AlphaFold v6, mean pLDDT = 90.4, ordered region (pLDDT>70) = 93.5%; PDB = 0 |
| Regulatory Domains | 8/10 | x2 | **16** | InterPro: 6 annotated domains (IPR000210, IPR058923, IPR009091, IPR000408, IPR051625, IPR011333); Pfam: 2 domains (PF00651, PF25390); BTB + RCC1 fold |
| PPI Network | 5/10 | x3 | **15** | STRING 15 partners (top LPAR6 0.755); IntAct 15 experimental interactions (co-IP, two-hybrid, pull-down); UniProt 7 curated interactions |
| Cross-Validation Bonus | -- | -- | **+1.5** | STRING + IntAct dual-source (+0.5); Multi-DB localization consistency (+0.5); Domain + AlphaFold quality (+0.5) |
| **Raw Total** | | | **132.5/180** | |
| **Normalized Total** | | | **73.6/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| HPA (Immunofluorescence) | Nucleoplasm, Golgi apparatus | Approved |
| HPA (Main Location) | Nucleoplasm, Golgi apparatus | -- |
| UniProt (Subcellular) | Cytoplasmic vesicle, secretory vesicle, acrosome | ECO:0000250 (sequence similarity) |
| GO-CC | Acrosomal vesicle (GO:0001669), Cytoplasm (GO:0005737) | IEA + IBA |

**HPA IF Status**: HPA IF original images not reliably obtained (HPA search page lacks usable subcellular IF original images). Nuclear localization assessment based on HPA localization/reliability + UniProt + GO-CC.

**Manual Review Assessment**: RCBTB2 shows partial nuclear localization (Nucleoplasm by HPA). However, the protein also annotates to Golgi and cytoplasmic vesicles, indicating it is not exclusively nuclear. The dual localization pattern (nucleoplasm + Golgi) is consistent with proteins that may shuttle between compartments. Immunofluorescence evidence from HPA is classified as "Approved" for nucleoplasm detection. Nuclear specificity is moderate -- the protein is detected in the nucleoplasm but not exclusively nuclear (also Golgi and cytoplasmic vesicles). Score 4/10 reflects partial but not exclusive nuclear localization.

### 4. Protein Size Assessment

At 551 amino acids (60.3 kDa), RCBTB2 falls within the ideal range for biochemical characterization. Proteins in this size range are amenable to recombinant expression, purification, crystallography, and most functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query | 20 |
| PubMed symbol-only query | 22 |
| PubMed broad query | 27 |
| Aliases observed (not scored) | CHC1L, RLG |

**Key Publications**:
1. Mo R, Chi N, Du J et al. (2025). "The ubiquitin ligase RCBTB2 regulates aggrephagy and inhibits prostate cancer progression by targeting GPAA1 for degradation." *Am J Cancer Res*. PMID: 41244118
2. Singh M, Sharma P, Bhatia P et al. (2024). "Integrated analysis of transcriptome and genome variations in pediatric T cell acute lymphoblastic leukemia." *BMC Cancer*. PMID: 38459434
3. Kim JW, Moon SW, Mo HY et al. (2023). "Concurrent inactivating mutations and expression losses of RGS2, HNF1A, and CAPN12 candidate tumor suppressor genes in colon cancers." *Pathol Res Pract*. PMID: 36566600
4. Legoff L, Dali O, D'Cruz SC et al. (2019). "Ovarian dysfunction following prenatal exposure to an insecticide, chlordecone, associates with altered epigenetic features." *Epigenetics Chromatin*. PMID: 31084621
5. Zhou X, Zhao H et al. (2023). "FAIM2 is correlated with metastasis of medulloblastoma through bioinformatics analysis." *Medicine*. PMID: 37083768

**Novelty Score**: PubMed strict count = 20. Per scoring rule: <=20 -> 10. This gene is extremely understudied, with only 20 direct PubMed hits. The most relevant paper (PMID 41244118) describes RCBTB2 as a ubiquitin ligase regulating aggrephagy in prostate cancer -- a recently discovered function. The remaining literature is primarily genomic/transcriptomic association studies without functional characterization. **Extremely novel target.**

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Version | v6 |
| Mean pLDDT | 90.4 |
| pLDDT > 90 (very high confidence) | 72.6% |
| pLDDT 70-90 (confident) | 20.9% |
| pLDDT 50-70 (low confidence) | 2.2% |
| pLDDT < 50 (disordered) | 4.4% |
| Ordered region (pLDDT > 70) | 93.5% |
| Available PDB entries | 0 |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on AlphaFold pLDDT statistics.

**Structure Assessment**: The AlphaFold prediction is of very high quality (mean pLDDT = 90.4). Over 93% of residues are in ordered regions, suggesting a well-folded protein. The high confidence prediction supports the structural domain annotations (BTB domain, RCC1 repeats). No experimental PDB structures exist, confirming the novelty of this target. Score 8/10 reflects excellent predicted structure quality but lack of experimental validation.

### 7. Domain Architecture

| Source | Domain/Feature | ID |
|--------|---------------|-----|
| InterPro | BTB/POZ domain | IPR000210 |
| InterPro | RCC1/regulator of chromosome condensation | IPR058923 |
| InterPro | Regulator of chromosome condensation 1/beta-lactamase-inhibitor protein II | IPR009091 |
| InterPro | RCC1 repeat | IPR000408 |
| InterPro | RCC1 and BTB domain-containing protein | IPR051625 |
| InterPro | RCC1/BLIP-II superfamily | IPR011333 |
| Pfam | BTB/POZ domain | PF00651 |
| Pfam | Domain of unknown function | PF25390 |

**Domain Analysis**: RCBTB2 contains two major domain types: (1) an N-terminal BTB/POZ domain, which mediates protein-protein interactions and is commonly found in transcription factors and ubiquitin ligase adaptors; (2) RCC1-like repeats forming a seven-bladed beta-propeller, a fold commonly involved in chromatin binding and guanine nucleotide exchange. The combination of BTB + RCC1 domains is characteristic of the RCBTB family, which may function as ubiquitin ligase substrate adaptors. The domain architecture supports potential roles in chromatin regulation and protein degradation.

### 8. PPI Network Analysis

**STRING Predicted Interactions** (combined score > 0.4):

| Partner | Combined Score | Experimental | Database | Text Mining |
|---------|---------------|--------------|----------|-------------|
| LPAR6 | 0.755 | 0.000 | 0.000 | 0.641 |
| RCBTB1 | 0.698 | 0.637 | 0.000 | 0.064 |
| ITM2B | 0.653 | 0.000 | 0.000 | 0.628 |
| NUDCD2 | 0.607 | 0.607 | 0.000 | 0.000 |
| FNDC3A | 0.565 | 0.000 | 0.000 | 0.531 |
| UBE2E3 | 0.565 | 0.489 | 0.000 | 0.154 |
| CDADC1 | 0.555 | 0.000 | 0.000 | 0.516 |
| SETDB2 | 0.496 | 0.041 | 0.000 | 0.478 |
| CYSLTR2 | 0.492 | 0.000 | 0.000 | 0.488 |
| TSSK4 | 0.490 | 0.045 | 0.000 | 0.488 |

**IntAct Experimental Interactions**:

| Partner | Method | PMID |
|---------|--------|------|
| RCBTB1 | Anti-tag coimmunoprecipitation | 28514442 |
| COPS4 | Two-hybrid pooling | 16189514 |
| HSP90AB1 | Luminescence-based mammalian interactome mapping | 22939624 |
| FARS2 | Two-hybrid array | 32296183 |
| PTPN11 | Pull-down | 31585087 |
| FLT3 | Pull-down | 31585087 |
| ZBTB18 | Anti-tag coimmunoprecipitation | 28514442 |
| STX11 | Anti-tag coimmunoprecipitation | 28514442 |
| CCDC120 | Anti-tag coimmunoprecipitation | 28514442 |
| MRPS11 | Anti-tag coimmunoprecipitation | 28514442 |
| FECH | Anti-tag coimmunoprecipitation | 28514442 |
| ZNF558 | Anti-tag coimmunoprecipitation | 28514442 |
| HELLS | Anti-tag coimmunoprecipitation | 28514442 |
| UBE2E3 | Anti-tag coimmunoprecipitation | 28514442 |
| ENSP00000345144.3 | Two-hybrid pooling | 16189514 |

**UniProt Curated Interactions**: FARS2 (6 experiments), MORF4L1 (3), NUDCD2 (2), PLA2G6 (3), RBBP9 (3), UBE2I (3), TAE1 (3)

**PPI Assessment**: RCBTB2 has a moderately sized PPI network with 15 STRING partners and 15 IntAct experimental interactions. Notable regulatory partners include: UBE2E3 (ubiquitin-conjugating enzyme), SETDB2 (histone methyltransferase), HELLS (chromatin remodeling), and ZBTB18 (transcriptional repressor). These partners suggest involvement in ubiquitin-mediated processes and chromatin regulation. The interaction with the paralog RCBTB1 is the strongest experimentally validated interaction (STRING combined 0.698, experimental 0.637), suggesting possible functional redundancy or heterodimerization. PPI score: 5/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| 3D Structure | AlphaFold + PDB | pLDDT=90.4, 0 PDB entries | Prediction only |
| Localization | HPA + UniProt + GO-CC | Nucleoplasm + Golgi / Cytoplasmic vesicle + acrosome | Multi-source, partially consistent |
| PPI | STRING + IntAct + UniProt | 15 + 15 + 7 interactions | Dual-source validated |
| Domains | InterPro + Pfam | 6 + 2 domains | Multi-DB consistent |

**Cross-Validation Bonus Details**:
- STRING + IntAct dual-source PPI validation: +0.5
- Multi-database localization consistency (HPA + UniProt + GO-CC): +0.5
- Domain annotation + AlphaFold structural quality: +0.5
- PDB + AlphaFold structural cross-validation: +0 (no experimental PDB)
- **Total Cross-Validation Bonus**: +1.5 / max +3

### 10. Overall Assessment

**Recommendation Level**: Recommended for further study (Score: 73.6/100)

**Core Strengths**:
1. Extreme novelty: Only 20 PubMed publications, making this a highly underexplored target
2. High-quality structural prediction: AlphaFold pLDDT 90.4 with 93.5% ordered residues
3. Well-annotated domain architecture: BTB domain + RCC1 repeats suggest regulatory function
4. Moderate PPI network with chromatin/ubiquitin-related partners
5. Protein size (551 aa) is ideal for experimental characterization
6. HPA-confirmed nucleoplasm localization

**Risks / Uncertainties**:
1. Nuclear localization is partial (also Golgi + cytoplasmic vesicles), not exclusively nuclear
2. No experimental PDB structures available
3. Very limited functional literature -- most functional annotation is predicted
4. Potential functional redundancy with paralog RCBTB1
5. HPA IF original images not directly obtained; localization based on database annotations

**Next Steps**:
- [ ] Obtain HPA IF images to verify nucleoplasm localization independently
- [ ] Experimental validation of nuclear vs. cytoplasmic distribution
- [ ] Functional studies of the BTB-ubiquitin ligase activity
- [ ] Investigate potential redundancy with RCBTB1
- [ ] Structural determination via crystallography or cryo-EM

### 11. Decision

**FINAL DECISION**: NOT REJECTED. This protein was previously false-rejected. Upon complete re-evaluation with full harvest packet data, RCBTB2 meets the scoring criteria for a viable TE-regulated nuclear protein candidate. Nuclear localization is supported by HPA (Nucleoplasm, Approved), protein is extremely novel (PubMed 20), and structural prediction is high quality. Recommended for inclusion in the candidate pool.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/O95199
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136161-RCBTB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RCBTB2%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95199
- STRING: https://string-db.org/network/9606.ENSP00000266049
- Data harvested: 2026-06-04
- Re-evaluation: Manual review with full packet inspection

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95199 |
| SMART | SM00225; |
| UniProt Domain [FT] | DOMAIN 394..457; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037" |
| InterPro | IPR000210;IPR058923;IPR009091;IPR000408;IPR051625;IPR011333; |
| Pfam | PF00651;PF25390; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136161-RCBTB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN2L | Opencell | false |
| CAPRIN1 | Opencell | false |
| CLASP1 | Opencell | false |
| CLASP2 | Opencell | false |
| CUL3 | Biogrid | false |
| FARS2 | Intact | false |
| FXR1 | Opencell | false |
| HDAC2 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
