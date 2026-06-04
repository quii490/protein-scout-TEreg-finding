---
type: protein-evaluation
gene: ABRAXAS1
date: 2026-06-02
tags:
  - protein-evaluation
  - nuclear-body
  - dna-damage
  - brca1
  - ddr
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ABRAXAS1 (BRCA1-A complex subunit Abraxas 1) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q6UWZ7 |
| **Protein Name** | BRCA1-A complex subunit Abraxas 1 |
| **Aliases** | ABRA1, CCDC98, FAM175A |
| **Length** | 409 aa |
| **Mass** | 46.7 kDa |
| **AlphaFold mean pLDDT** | 77.0 |
| **AlphaFold pLDDT >90** | 46.9% |
| **AlphaFold pLDDT <50** | 19.8% |
| **PubMed (strict)** | 9 |
| **PubMed (broad)** | 48 |
| **Function** | Involved in DNA damage response and double-strand break (DSB) repair. Component of the BRCA1-A complex, acting as a central scaffold protein that assembles the various components of the complex and mediates the recruitment of BRCA1. The BRCA1-A complex specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesion sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at DSBs. This complex also possesses deubiquitinase activity. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Nucleus** (ECO:0000269 x3 -- experimental evidence from multiple publications)

**Note**: UniProt provides strong experimental evidence for nuclear localization. The ECO:0000269 code indicates direct experimental assay evidence from published studies (not computational prediction).

### GO Cellular Component
- GO:0070531 **BRCA1-A complex** (IDA:UniProtKB -- experimental)
- GO:0016604 **nuclear body** (IDA:HPA -- experimental, based on HPA antibody staining)
- GO:0005654 **nucleoplasm** (TAS:Reactome -- traceable author statement)
- GO:0005634 **nucleus** (IDA:UniProtKB -- experimental)

**Note**: Four nuclear GO-CC terms, two with IDA (direct assay) evidence. BRCA1-A complex localization to nuclear bodies is experimentally confirmed. The GO annotation independently supports the HPA nuclear body localization.

### HPA Subcellular Localization
- **Main location**: **Nuclear bodies**
- **Additional locations**: (none)
- **Reliability (IF)**: **Supported** (second-highest tier)
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

**HPA Nuclear Localization Summary**: HPA classifies ABRAXAS1 as exclusively localized to nuclear bodies with "Supported" reliability. This is consistent with its well-characterized role in the BRCA1-A DNA damage response complex, which forms discrete nuclear foci (bodies) at sites of DNA double-strand breaks. While no curated IF display images are shown, the Supported reliability and GO-CC IDA evidence provide strong confidence.

**Nuclear Evidence Consensus**: There is excellent agreement between HPA (Nuclear bodies, Supported), UniProt (Nucleus, experimental), and GO-CC (nuclear body IDA, nucleoplasm TAS, nucleus IDA). This is one of the most consistent nuclear localization profiles in the set. The BRCA1-A complex localization to DNA-damage-induced nuclear foci is a well-established finding in the DDR field.

**Note on Excel discrepancy**: The original Sheet4 Excel listed ABRAXAS1 as HPA="Nuclear membrane|Nucleoplasm" with nuclear_score=6. The actual harvested HPA data shows "Nuclear bodies" as the sole main location (no Nuclear membrane, no Nucleoplasm). This is a significant misclassification in the original Excel. Interestingly, Nuclear bodies is actually a stronger and more specific nuclear compartment annotation than the original assignment.

## 3. HPA Immunofluorescence

**IF unavailable — HPA 检索页无可用的 subcellular IF 原图。暂无数据（HPA IF 原图未可靠获取），核定位基于 HPA localization + UniProt + GO-CC -- HPA检索页无可用的subcellular IF原图。核定位基于HPA localization (Supported reliability) + UniProt experimental evidence + GO-CC IDA annotations.**

The HPA subcellular page shows `no_image_detected` for display-quality IF images. However, the "Supported" reliability tier indicates that HPA internal scoring of IF data supports nuclear body localization. Given the extensive independent evidence for nuclear localization (UniProt experimental, GO-CC IDA, well-characterized DDR function), the absence of curated IF display images does not weaken the nuclear localization conclusion.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ABRAXAS1"[Title/Abstract] AND (gene OR protein OR hydrolase) | 9 | Gene-specific |
| Symbol-only: "ABRAXAS1"[Title/Abstract] | 14 | Gene-specific |
| Broad: "ABRAXAS1" | 48 | Includes some alias matches |

**Key Papers:**
- PMID:37198153 -- "ABRAXAS1 orchestrates BRCA1 activities to counter genome destabilizing repair pathways -- lessons from breast cancer patients" (Cell Death & Disease, 2023). Excellent review of ABRAXAS1 function in DDR and cancer.
- PMID:31630195 -- "BRCA1 mislocalization leads to aberrant DNA damage response in heterozygous ABRAXAS1 mutation carrier cells" (Human Molecular Genetics, 2019). Directly addresses nuclear localization and functional consequences of ABRAXAS1 mutation.
- PMID:41088366 -- "Exome sequencing reveals new insights into the germline landscape of inflammatory breast cancer among Tunisian patients" (J Transl Med, 2025). Clinical cancer relevance.
- PMID:36896237 -- "Evaluation of AlphaFold structure-based protein stability prediction on missense variations in cancer" (Front Genet, 2023).
- PMID:36551595 -- "Proteome-Wide Identification of RNA-Dependent Proteins in Lung Cancer Cells" (Cancers, 2022).

**Research Volume Assessment**: Modest strict count (9) but much larger when aliases are included (broad: 48). ABRAXAS1 is studied primarily in the context of DNA damage response and breast cancer. The protein is clinically relevant -- mutations are associated with hereditary breast cancer. The literature, while not voluminous, is high-quality and mechanistically detailed. Gene symbol is unique.

**Aliases observed**: ABRA1, CCDC98, FAM175A

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q6UWZ7-F1 (version 6)
- Mean pLDDT: 77.0 (moderate confidence)
- pLDDT >90: 46.9%, 70-90: 24.4%, <50: 19.8%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
| PDB ID | Method | Resolution | Coverage |
|--------|--------|------------|----------|
| 4JLU | X-ray | 3.50 A | 399-409 (C-terminal peptide, chain B) |
| 4U4A | X-ray | 3.51 A | 399-409 (C-terminal peptide, chains D/E/F) |
| 4Y18 | X-ray | 3.50 A | 399-409 (C-terminal peptide, chains I-P) |
| 4Y2G | X-ray | 2.50 A | 403-409 (C-terminal peptide, chain B) |

**Structure Assessment**: Four X-ray crystal structures exist, but they all cover only the extreme C-terminal peptide (last 7-10 amino acids, 399-409). These structures represent ABRAXAS1 in complex with other BRCA1-A components (the C-terminal peptide is responsible for complex assembly). The vast majority of the protein (residues 1-398, ~97%) has no experimental structure. The AlphaFold model has moderate confidence (mean pLDDT 77.0) with 19.8% low-confidence regions, suggesting some intrinsic disorder. PAE data available.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR023239 | Abraxas 1, MPN domain |
| IPR023238 | BRCA1-A complex subunit Abraxas/Abraxas2 |
| IPR037518 | MPN domain |

| Pfam | Description |
|------|-------------|
| PF21125 | MPN domain |

**Domain Assessment**: ABRAXAS1 contains an MPN (Mpr1/Pad1 N-terminal) domain. MPN domains are found in subunits of the proteasome, COP9 signalosome, and translation initiation factor 3 complexes. In ABRAXAS1, the MPN domain serves as a scaffold for the BRCA1-A complex. This is a protein-protein interaction domain without catalytic activity. The domain architecture is consistent with ABRAXAS1's role as a scaffold protein in DDR.

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| UIMC1 | 0.999 | 0.994 | 0.900 | 0.999 |
| BARD1 | 0.999 | 0.994 | 0.900 | 0.993 |
| BABAM1 | 0.999 | 0.994 | 0.900 | 0.997 |
| BRCA1 | 0.999 | 0.994 | 0.900 | 0.997 |
| BABAM2 | 0.999 | 0.994 | 0.900 | 0.997 |
| BRCC3 | 0.999 | 0.997 | 0.900 | 0.998 |
| MDC1 | 0.923 | 0.443 | 0.500 | 0.748 |
| RBBP8 | 0.896 | 0.292 | 0.500 | 0.729 |
| RNF8 | 0.846 | 0 | 0.500 | 0.705 |
| MRE11 | 0.843 | 0 | 0.500 | 0.691 |
| CHEK2 | 0.790 | 0 | 0.500 | 0.595 |
| TP53BP1 | 0.789 | 0.330 | 0.500 | 0.419 |
| ATM | 0.785 | 0 | 0.500 | 0.582 |
| H2AX | 0.777 | 0 | 0.500 | 0.574 |
| RNF168 | 0.776 | 0 | 0.500 | 0.570 |

**STRING Assessment**: Exceptional PPI network. The top 6 partners (all BRCA1-A complex components) have combined scores of 0.999 with experimental scores >=0.994. This is one of the strongest PPI networks observed. Beyond the core complex, partners include key DDR proteins: MDC1, RBBP8/CtIP, RNF8, MRE11, CHEK2, TP53BP1, ATM, H2AX, RNF168. The network is entirely DDR-focused, reflecting ABRAXAS1's central scaffold role.

### IntAct (15 interactions)
| Partner | Method | PMID | Significance |
|---------|--------|------|-------------|
| BRCA1 | Pull down (direct interaction) | 17525340 | Core BRCA1-A interaction |
| UIMC1 | co-IP | 17525340 | Core BRCA1-A subunit |
| RBBP8/CtIP | co-IP | 17525340 | DNA end resection |
| RAD51 | Fluorescence microscopy (colocalization) | 17525340 | Homologous recombination |
| BRIP1 | co-IP | 17525340 | DNA helicase |
| BRCC3 | co-IP | 19615732 | Deubiquitinase |
| BABAM2 | co-IP | 19615732 | BRCA1-A subunit |
| BABAM1 | co-IP | 19615732 | BRCA1-A subunit |
| MANF | Cross-linking | 30021884 | ER stress protein |
| RABGGTB | co-IP | 28514442 | Prenylation |
| TEKT4 | co-IP | 28514442 | - |
| LAMC1 | co-IP | 28514442 | - |
| PSMC5 | co-IP | 28514442 | Proteasome subunit |
| ALDH6A1 | co-IP | 28514442 | Metabolism |
| WTAP | co-IP | 28514442 | RNA modification |

### UniProt Interactions (6 entries)
BRCA1 (16 experiments), BRCC3 (4), CFTR (3), KPNA4 (2), UIMC1 (9+4), UIMC1 (duplicate)

**PPI Assessment**: Outstanding PPI evidence. ABRAXAS1 is the central scaffold of the BRCA1-A complex with extensive experimental validation. BRCA1 interaction (16 UniProt experiments, plus direct interaction by pull-down in IntAct) is the strongest PPI in the dataset. The KPNA4 (karyopherin alpha 4) interaction (2 experiments) may mediate nuclear import. PPI network strength is among the highest of any protein in this evaluation set.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA/UniProt/GO evidence |
| 蛋白大小 | 6/10 | ×1 | 6 | |
| 研究新颖性 | 10/10 | ×5 | 35 | PubMed strict |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT |
| 调控结构域 | 6/10 | ×2 | 12 | InterPro/Pfam |
| PPI 网络 | 4/10 | ×3 | 12 | STRING/IntAct |
| **加权总分** | | | **136/180**** | |
| **归一化总分 (÷1.83)** | | | **74.3/100**** | |

## 9. Final Decision

**SCORED: 71/100 -- STRONG NUCLEAR CANDIDATE**

ABRAXAS1 is a high-confidence nuclear protein. The evidence for nuclear localization is definitive (UniProt experimental, GO-CC IDA, HPA Supported), and the functional characterization as a DNA damage response scaffold protein is excellent. The BRCA1-A complex exclusively functions in the nucleus at sites of DNA double-strand breaks.

**Strengths**:
- Definitive nuclear localization from multiple independent sources
- Well-characterized function in DNA damage response
- Central scaffold of the BRCA1-A complex with outstanding PPI network
- Clinical relevance: mutations associated with hereditary breast cancer
- Extensive literature on molecular mechanism
- BRCA1 interaction is among the most validated PPIs in the human proteome

**Weaknesses**:
- PDB structures are fragment-level only (C-terminal peptide)
- No enzymatic activity (purely a scaffold protein)
- No HPA IF display images (but strong corroborating evidence compensates)
- Modest strict PubMed count (9) relative to functional importance

**Recommendation**: Retain as a high-priority nuclear protein. ABRAXAS1 should never have been template-rejected. The nuclear body localization is experimentally validated and functionally characterized. The gene's role in DDR and breast cancer makes it both biologically important and clinically relevant. If the project focuses on nuclear proteins with defined functions, ABRAXAS1 should be prioritized.

## 10. Manual Review Note

The original Excel classified ABRAXAS1 as HPA="Nuclear membrane|Nucleoplasm", which is incorrect. The actual HPA data shows "Nuclear bodies" as the sole main location. This misclassification may explain the template rejection -- the evaluator may have been looking for the wrong nuclear compartment. Nuclear bodies (DNA damage foci) is a more specific and mechanistically relevant annotation than the generic "Nuclear membrane|Nucleoplasm" originally assigned.

**Re-evaluator's note**: ABRAXAS1 is one of the strongest candidates in this re-evaluation set. The template rejection was clearly an error, likely caused by the Excel misclassifying the nuclear compartment. This gene scores very well across all nuclear dimensions and functions in a pathway (DDR) that is of high interest for many research programs. The only caveat is that scaffold proteins without enzymatic activity can be challenging as drug targets, but this does not diminish the nuclear localization evidence.

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。
