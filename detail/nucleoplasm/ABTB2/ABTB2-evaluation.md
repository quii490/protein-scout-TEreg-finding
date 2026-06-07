---
type: protein-evaluation
gene: ABTB2
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleoplasm
  - btb-poz-domain
  - ubiquitin-ligase
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ABTB2 (Ankyrin repeat and BTB/POZ domain-containing protein 2) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q8N961 |
| **Protein Name** | Ankyrin repeat and BTB/POZ domain-containing protein 2 |
| **Aliases** | (none) |
| **Length** | 1025 aa |
| **Mass** | 113.7 kDa |
| **AlphaFold mean pLDDT** | 76.4 |
| **AlphaFold pLDDT >90** | 37.4% |
| **AlphaFold pLDDT <50** | 16.6% |
| **PubMed (strict)** | 6 |
| **PubMed (broad)** | 13 |
| **Function** | May be involved in the initiation of hepatocyte growth. Recent work (PMID:41322190) has characterized ABTB2 as a novel target for pancreatic cancer therapy. |

## 2. 核定位证据

### UniProt Subcellular Location
**No subcellular location annotation.** UniProt has not annotated the subcellular localization of ABTB2.

### GO Cellular Component
**No GO cellular component terms.** ABTB2 has no GO-CC annotations.

**Note**: The complete absence of UniProt SL and GO-CC annotations is unusual. This protein has essentially no curated localization information outside of HPA.

### HPA Subcellular Localization
- **Main location**: **Nucleoplasm**
- **Additional locations**: Vesicles
- **Reliability (IF)**: **Supported** (second-highest tier)
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

**HPA Nuclear Localization Summary**: HPA assigns Nucleoplasm as the main location with "Supported" reliability. No IF display images are available. Given the absence of any other subcellular localization data (UniProt, GO-CC), the HPA annotation is the SOLE source of nuclear evidence. The "Supported" reliability carries reasonable weight but is not the highest tier.

**Evidence Assessment**: Nuclear localization evidence is entirely dependent on HPA. There is no corroboration from UniProt, GO-CC, or the literature. This makes the nuclear assignment less robust than for genes with multi-source evidence.

**Note on Excel discrepancy**: The original Sheet4 Excel listed ABTB2 as HPA="Nuclear bodies|Nucleoplasm" with nuclear_score=6. The actual harvested HPA data shows "Nucleoplasm" main (not Nuclear bodies) with "Vesicles" additional. The "Nuclear bodies" assignment in the Excel is not present in the actual HPA data.

## 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ABTB2"[Title/Abstract] AND (gene OR protein OR hydrolase) | 6 | All gene-specific |
| Symbol-only: "ABTB2"[Title/Abstract] | 9 | All gene-specific |
| Broad: "ABTB2" | 13 | All gene-specific |

**Key Papers:**
- PMID:41322190 -- "Mechanistic and functional characterization of ABTB2 as a novel target for pancreatic cancer therapy" (Molecular Therapy: Oncology, 2025). Most significant paper -- establishes ABTB2 as a cancer target.
- PMID:35088020 -- "Putative regulatory functions of SNPs associated with bronchial asthma, arterial hypertension and their comorbid phenotype" (Vavilovskii Zhurnal Genetiki i Selektsii, 2021).
- PMID:35267472 -- "Preliminary Study on the Sequencing of Whole Genomic Methylation and Transcriptome-Related Genes in Thyroid Carcinoma" (Cancers, 2022).
- PMID:33498280 -- "Weighted Gene Co-Expression Network Analysis Identifies Key Modules and Hub Genes Associated with Mycobacterial Infection of Human Macrophages" (Antibiotics, 2021).
- PMID:30810905 -- "Differential Expression of Genes for Ubiquitin Ligases in Medulloblastoma Subtypes" (Cerebellum, 2019). Note: this paper is about ubiquitin ligase genes -- ABTB2 may appear in the context of Cullin-RING ligases.

**Research Volume Assessment**: Very low publication volume (6-13 papers). The most significant paper (PMID:41322190) is from 2025 and establishes ABTB2 as a potential pancreatic cancer target. Most other papers are GWAS or co-expression studies where ABTB2 appears peripherally. The literature does not address subcellular localization directly.

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q8N961-F1 (version 6)
- Mean pLDDT: 76.4 (moderate confidence)
- pLDDT >90: 37.4%, 70-90: 35.7%, <50: 16.6%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
**None.** No experimental structures available for this 1025 aa protein.

**Structure Assessment**: Moderate confidence AlphaFold model for a large (1025 aa) protein. 37.4% high-confidence and only 16.6% low-confidence regions suggest a reasonably well-folded protein with some flexible regions. The absence of experimental structures for a protein this large is a significant gap. PAE data available for domain-domain interaction analysis.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR059008 | Ankyrin repeat-containing domain |
| IPR048063 | BTB/POZ domain |
| IPR052089 | Ankyrin repeat and BTB/POZ domain-containing protein |
| IPR002110 | Ankyrin repeat |
| IPR036770 | Ankyrin repeat superfamily |
| IPR000210 | BTB/POZ domain |
| IPR009072 | - |
| IPR011333 | BTB/POZ fold |

| Pfam | Description |
|------|-------------|
| PF00023 | Ankyrin repeat |
| PF12796 | Ankyrin repeat |
| PF00651 | BTB/POZ domain |
| PF26281 | - |

**Domain Assessment**: ABTB2 has a multi-domain architecture combining BTB/POZ and ankyrin repeat domains. The BTB/POZ domain (PF00651) is particularly notable:
- **BTB/POZ domain proteins** frequently function as substrate adaptors for Cullin-3 (CUL3) ubiquitin ligase complexes
- Many BTB proteins are transcription factors or transcriptional regulators
- BTB proteins can homodimerize and mediate protein-protein interactions
- CUL3-BTB complexes often function in the nucleus (e.g., KEAP1-NRF2 pathway, SPOP in prostate cancer)
- The presence of a BTB/POZ domain provides a plausible mechanistic basis for nuclear function

The ankyrin repeat domains mediate additional protein-protein interactions. The domain architecture is consistent with a scaffold/adaptor protein, potentially functioning in ubiquitin-mediated regulation.

## 7. Protein-Protein Interaction Network

### STRING (8 partners -- weak network)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| DEPDC7 | 0.536 | 0 | 0 | 0.532 |
| ENSP00000496197 | 0.526 | 0 | 0 | 0.526 |
| IFT46 | 0.440 | 0.410 | 0 | 0.090 |
| CUL3 | 0.429 | 0.338 | 0 | 0.172 |
| TTC30B | 0.417 | 0.410 | 0 | 0.054 |
| LRRC42 | 0.412 | 0 | 0 | 0.412 |
| CKAP5 | 0.410 | 0 | 0 | 0.409 |
| TCP11L1 | 0.406 | 0 | 0 | 0.397 |

### IntAct (15 interactions)
| Partner | Method | PMID | Significance |
|---------|--------|------|-------------|
| COPS5 | TAP | 21145461 | COP9 signalosome subunit -- protein degradation |
| HS1BP3 | co-IP | 28514442 | - |
| DYNLT2B | co-IP | 28514442 | Dynein light chain |
| Xpo1 | Pull down | 26673895 | **Exportin-1/CRM1 -- nuclear export receptor** |
| IFT56 | co-IP | 33961781 | Intraflagellar transport |
| ABTB3 | co-IP | 33961781 | Paralog interaction |
| MYO9A | co-IP | 33961781 | Myosin |
| NME4 | co-IP | 33961781 | Nucleoside diphosphate kinase |
| FBP2 | co-IP | 33961781 | - |
| C2CD2L | co-IP | 33961781 | - |
| ATP2A1 | co-IP | 33961781 | Calcium pump |
| ZNF609 | co-IP | 33961781 | Zinc finger protein |
| TRIM24 | co-IP | 33961781 | **Transcriptional coregulator** |
| CCNT1 | co-IP | 33961781 | **Cyclin T1 -- transcription elongation** |
| MPZL1 | co-IP | 33961781 | - |

### UniProt Interactions (1 partner)
YWHAE (14-3-3 epsilon, 2 experiments)

**PPI Assessment**: Weak PPI network overall but with mechanistically interesting partners:
- **Xpo1 (Exportin-1/CRM1)**: The nuclear export receptor. ABTB2 interaction with Xpo1 (pull down, PMID:26673895) directly supports nucleocytoplasmic trafficking. This is the SINGLE most informative PPI data point for nuclear localization.
- **CUL3**: BTB proteins are classic CUL3 adaptors. The CUL3 interaction (0.338 experimental in STRING) is mechanistically expected for a BTB domain protein.
- **COPS5**: COP9 signalosome subunit involved in Cullin-RING ligase regulation.
- **TRIM24**: Transcriptional coregulator -- nuclear function.
- **CCNT1 (Cyclin T1)**: Component of P-TEFb transcription elongation factor -- nuclear function.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 | Based on HPA/UniProt/GO evidence |
| 蛋白大小 | 3/10 | ×1 | 3 | |
| 研究新颖性 | 10/10 | ×5 | 20 | PubMed strict count |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT |
| 调控结构域 | 3/10 | ×2 | 6 | InterPro/Pfam |
| PPI 网络 | 2/10 | ×3 | 6 | STRING/IntAct |
| **加权总分** | | | **96/180**** | |
| **归一化总分 (÷1.83)** | | | **52.5/100**** | |

## 9. Final Decision

**SCORED: 41/100 -- WEAK-BORDERLINE CANDIDATE, RETAIN WITH CAUTION**

ABTB2 is a challenging evaluation case. The nuclear localization evidence relies entirely on HPA (Nucleoplasm main, Supported reliability). UniProt and GO-CC provide no localization data whatsoever. However, the BTB/POZ domain architecture and the Xpo1 interaction provide mechanistic plausibility for nuclear localization.

**Strengths**:
- HPA Supported nucleoplasmic localization
- BTB/POZ domain -- well-established in nuclear CUL3 ubiquitin ligase complexes
- XPO1 (Exportin-1) interaction via pull-down (PMID:26673895) -- indicates nucleocytoplasmic trafficking
- TRIM24 and CCNT1 interactions suggest nuclear transcriptional connections
- Emerging cancer target (pancreatic cancer, PMID:41322190)
- Unique gene symbol, no literature pollution

**Weaknesses**:
- No corroborating nuclear evidence from UniProt or GO-CC (complete absence of localization annotation)
- No HPA IF display images
- Very weak STRING PPI network
- No experimental PDB structures
- Low PubMed count (6 papers)
- PPI evidence for nuclear function is indirect (Xpo1 interaction suggests export, not necessarily nuclear residence)

**Recommendation**: Retain at low priority with a strong caveat. The nuclear evidence is thin -- HPA annotation alone is the sole direct evidence. The BTB domain provides mechanistic rationale but is not proof. This gene would benefit from experimental validation of nuclear localization before significant research investment. The emerging cancer target status (PMID:41322190) adds applied value.

## 10. Manual Review Note

The original Excel classified ABTB2 as HPA="Nuclear bodies|Nucleoplasm" with nuclear_score=6. The actual HPA data shows only "Nucleoplasm" main (no Nuclear bodies). The protein has no localization annotation in UniProt and no GO-CC terms, making it essentially a "blank slate" protein that happens to have a favorable HPA IF readout. The BTB/POZ domain is the strongest mechanistic argument for nuclear function -- CUL3-BTB complexes are classically nuclear in many cases (SPOP, KEAP1).

**Re-evaluator's note**: This is a marginal case. The complete absence of any non-HPA nuclear data makes this one of the weakest nuclear candidates in the set. However, the BTB/POZ domain and Xpo1 interaction provide enough biological rationale to avoid outright rejection. A manual review of the raw HPA IF images would be valuable to confirm or refute the nucleoplasmic assignment. If confirmed, the protein's large size, multi-domain architecture, and cancer relevance could make it a worthwhile candidate.

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000166016-ABTB2/subcellular

![](https://images.proteinatlas.org/20065/234_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/20065/234_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/20065/235_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/20065/235_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/20065/535_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/20065/535_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N961 |
| SMART | SM00248;SM00225; |
| UniProt Domain [FT] | DOMAIN 845..914; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037" |
| InterPro | IPR059008;IPR048063;IPR052089;IPR002110;IPR036770;IPR000210;IPR009072;IPR011333; |
| Pfam | PF00023;PF12796;PF00651;PF26281; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166016-ABTB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP97 | Biogrid | false |
| CUL3 | Biogrid | false |
| DNTT | Biogrid | false |
| DUSP26 | Biogrid | false |
| EEF1A1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
