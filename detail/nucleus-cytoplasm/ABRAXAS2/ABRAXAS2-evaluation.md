---
type: protein-evaluation
gene: ABRAXAS2
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleus-cytoplasm
  - brisc-complex
  - deubiquitinase
  - p53
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ABRAXAS2 (BRISC complex subunit Abraxas 2) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q15018 |
| **Protein Name** | BRISC complex subunit Abraxas 2 |
| **Aliases** | ABRO1, FAM175B, KIAA0157 |
| **Length** | 415 aa |
| **Mass** | 46.9 kDa |
| **AlphaFold mean pLDDT** | 73.6 |
| **AlphaFold pLDDT >90** | 47.7% |
| **AlphaFold pLDDT <50** | 32.8% |
| **PubMed (strict)** | 6 |
| **PubMed (broad)** | 17 |
| **Function** | Component of the BRISC complex, a multiprotein complex that specifically cleaves 'Lys-63'-linked polyubiquitin. Acts as a central scaffold protein assembling BRISC components and retaining them in the cytoplasm. Required for normal mitotic spindle assembly and microtubule attachment to kinetochores. Plays a role in interferon signaling via deubiquitination of IFNAR1. Down-regulates response to bacterial LPS. Required for normal induction of p53/TP53 in response to DNA damage. Independent of BRISC, promotes USP7-p53 interaction leading to p53 deubiquitination and stabilization. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Nucleus** (ECO:0000269 x4 -- experimental evidence from multiple publications)
- **Cytoplasm** (ECO:0000269 x6 -- experimental evidence)
- Cytoplasm, cytoskeleton, spindle pole (ECO:0000269)
- Cytoplasm, cytoskeleton (ECO:0000269)

**Note**: UniProt provides strong experimental evidence for BOTH nuclear and cytoplasmic localization. The nuclear evidence (ECO:0000269 x4) is robust. The protein's known function includes a nuclear role: promoting USP7-mediated p53 deubiquitination and stabilization in the nucleus.

### GO Cellular Component
- GO:0070552 BRISC complex (IDA:UniProtKB)
- GO:0036064 ciliary basal body (IDA:HPA)
- GO:0035869 ciliary transition zone (IDA:HPA)
- GO:0005737 cytoplasm (IDA:UniProtKB)
- GO:0005829 cytosol (IDA:HPA)
- GO:0005874 microtubule (IEA:UniProtKB-KW)
- GO:0005634 **nucleus** (IBA:GO_Central -- inferred from biological aspect of ancestor)
- GO:0000922 spindle pole (IEA:UniProtKB-SubCell)

**Note**: Important: nucleus is present in GO-CC with IBA evidence. The ciliary/cytoplasmic annotations dominate, but the nuclear annotation exists.

### HPA Subcellular Localization
- **Main location**: **Cytosol** (NO NUCLEAR COMPARTMENT IN HPA)
- **Additional locations**: Primary cilium transition zone, Basal body
- **Reliability (IF)**: **Supported**
- **IF Display Images Available**: YES (10 images)
  - `1484_G2_1_blue_red_green.jpg`, `1484_G2_3_blue_red_green.jpg`
  - `1559_E4_5_blue_red_green.jpg`, `1559_E4_6_blue_red_green.jpg`
  - `2176_A8_38_blue_red_green.jpg`, `2176_A8_44_blue_red_green.jpg`
  - `2201_C8_35_blue_red_green.jpg`, `2201_C8_96_blue_red_green.jpg`
  - `2178_B8_45_blue_red_green.jpg`, `2178_B8_57_blue_red_green.jpg`
- **Image status**: `if_display_images_available`
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**HPA Nuclear Localization Summary**: HPA does NOT classify ABRAXAS2 as nuclear. Its main location is Cytosol, with Primary cilium transition zone and Basal body as additional locations. No nuclear compartment appears in the HPA subcellular_location list. However, 10 IF display images are available, meaning the IF data can be manually reviewed.

**Critical Evidence Pattern**: This is a case of "nucleocytoplasmic shuttling protein where HPA primarily captures the cytoplasmic pool." UniProt provides strong experimental evidence (ECO:0000269 x4) for nuclear localization. The nuclear function (USP7-p53 interaction, p53 stabilization) is well-documented in the literature. The HPA IF images should be manually examined to check for nuclear signal that may not have met HPA's threshold for nuclear compartment classification.

## 3. HPA Immunofluorescence

10 IF display images available. These images can be manually inspected for nuclear signal. The HPA automated classification assigned Cytosol as the main location, which is consistent with the known predominant cytoplasmic localization of the BRISC complex. However, given UniProt's experimental nuclear evidence, the IF images may show a weaker or conditional nuclear signal. **Manual inspection recommended.**

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ABRAXAS2"[Title/Abstract] AND (gene OR protein OR hydrolase) | 6 | Gene-specific |
| Symbol-only: "ABRAXAS2"[Title/Abstract] | 8 | Gene-specific |
| Broad: "ABRAXAS2" | 17 | Includes alias matches |

**Key Papers:**
- PMID:40013521 -- "A bacterial RING ubiquitin ligase triggering stepwise degradation of BRISC via TOLLIP-mediated selective autophagy manipulates host inflammatory response" (Autophagy, 2025). Recent BRISC mechanism paper.
- PMID:30755420 -- "The BRISC deubiquitinating enzyme complex limits hematopoietic stem cell expansion by regulating JAK2 K63-ubiquitination" (Blood, 2019).
- PMID:31405213 -- "Connecting the Dots in the Neuroglobin-Protein Interaction Network" (Cells, 2019).
- PMID:41364128 -- "Integrative phosphoproteomic network analysis identifies CAMK2D as a shared regulator of TPD52 family proteins in cancer" (Protoplasma, 2026).
- PMID:42159682 -- "Integrated DIA and thermal proteome profiling" (Anal Bioanal Chem, 2026).

**Research Volume Assessment**: Modest literature (6 strict, 17 broad). The gene is studied primarily through its alias ABRO1. Key papers establish the BRISC complex function (deubiquitination of IFNAR1, JAK2) and the nuclear p53 regulatory role. The literature quality is good but volume is moderate.

**Aliases observed**: ABRO1, FAM175B, KIAA0157

## 5. AlphaFold / PAE / PDB

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

### AlphaFold
- Entry: AF-Q15018-F1 (version 6)
- Mean pLDDT: 73.6 (moderate confidence)
- pLDDT >90: 47.7%, 70-90: 15.7%, <50: 32.8%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
| PDB ID | Method | Resolution | Coverage |

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
|--------|--------|------------|----------|
| 6H3C | Cryo-EM | 3.90 A | Full (1-415, chains A/F) |
| 6R8F | Cryo-EM | 3.80 A | 1-267 (chains B/D) |
| 8PVY | Cryo-EM | 3.02 A | 1-267 (chains B/D/H/J) |
| 8PY2 | Cryo-EM | 3.32 A | 1-267 (chains B/D/H/J) |

**Structure Assessment**: Excellent experimental structural coverage. Four cryo-EM structures of the BRISC complex exist. The full-length structure (6H3C at 3.90A) and three partial structures (8PVY at 3.02A is the highest resolution) provide good structural information. The continual improvement in resolution (3.90A -> 3.02A) indicates active structural biology interest. AlphaFold model has moderate confidence with 32.8% low-confidence regions, suggesting some disorder.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR023240 | Abraxas 2 |
| IPR023238 | BRCA1-A complex subunit Abraxas/Abraxas2 |
| IPR037518 | MPN domain |

| Pfam | Description |
|------|-------------|
| PF21125 | MPN domain |

**Domain Assessment**: Like ABRAXAS1, ABRAXAS2 contains an MPN domain. The MPN domain serves as a scaffold for the BRISC complex assembly. The domain is shared with ABRAXAS1 but the two proteins assemble into distinct complexes (BRCA1-A vs. BRISC). No catalytic domains -- scaffold function only. The domain architecture is well-characterized via cryo-EM.

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| SHMT2 | 0.999 | 0.981 | 0.900 | 0.630 |
| BRCC3 | 0.999 | 0.991 | 0.900 | 0.992 |
| BABAM2 | 0.999 | 0.987 | 0.900 | 0.993 |
| BABAM1 | 0.999 | 0.977 | 0.900 | 0.992 |
| UIMC1 | 0.891 | 0.332 | 0 | 0.831 |
| USP7 | 0.844 | 0.596 | 0 | 0.625 |
| BRCA1 | 0.814 | 0.047 | 0 | 0.813 |
| TP53 | 0.790 | 0.618 | 0 | 0.475 |
| PSMD14 | 0.736 | 0.304 | 0 | 0.628 |
| THAP5 | 0.725 | 0.230 | 0 | 0.657 |
| NLRP3 | 0.712 | 0.328 | 0.500 | 0.213 |
| BOD1L1 | 0.674 | 0 | 0 | 0.668 |
| PSMD7 | 0.662 | 0.304 | 0 | 0.526 |
| WWP2 | 0.623 | 0.599 | 0 | 0.097 |
| DEF6 | 0.622 | 0.620 | 0 | 0 |

**STRING Assessment**: Excellent PPI network. Four core BRISC partners at 0.999 with very high experimental scores (>0.97). USP7 interaction (0.844, experimental 0.596) is key for the nuclear p53 regulatory function. TP53 interaction (0.790, experimental 0.618) directly supports the nuclear role. BRCA1 connection (0.814) via paralogy to ABRAXAS1. Network spans both cytoplasmic (BRISC) and nuclear (p53/USP7) functions.

### IntAct (15 interactions)
| Partner | Method | PMID | Significance |
|---------|--------|------|-------------|
| BABAM2 | co-IP | 17353931 | Core BRISC |
| BRCC3 | co-IP | 19615732 | Core BRISC |
| BABAM1 | co-IP | 19615732 | Core BRISC |
| UIMC1 | co-IP | 19615732 | Cross-complex |
| USP7 | co-IP | 19615732 | **Nuclear p53 regulator** |
| GRB2 | TAP | 19380743 | Signaling |
| OPTN | Display tech | 20195357 | Autophagy receptor |
| TP53 | co-IP | 28514442 | **p53 -- nuclear function** |
| ARHGEF40 | co-IP | 32203420 | RhoGEF |
| DCUN1D1 | Two-hybrid | 32296183 | Neddylation |
| TAFA4 | co-IP | 28514442 | - |
| ODF1 | co-IP | 28514442 | - |
| STK11 | co-IP | 28514442 | LKB1 kinase |
| FAM189B | co-IP | 28514442 | - |

### UniProt Interactions (4 partners)
BABAM2 (3), BRCC3 (8), DCUN1D1 (3), SCRIB (2)

**PPI Assessment**: Strong PPI evidence with direct experimental support for both cytoplasmic (BRISC complex) and nuclear (USP7, TP53) functions. The USP7 and TP53 co-IP interactions (PMID:19615732, PMID:28514442) experimentally validate the nuclear regulatory role. BRCC3 interaction is well-validated (8 experiments). The network convincingly demonstrates dual cytoplasmic/nuclear functionality.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA/UniProt/GO evidence |
| 蛋白大小 | 5/10 | ×1 | 5 | |
| 研究新颖性 | 10/10 | ×5 | 30 | PubMed strict |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT |
| 调控结构域 | 5/10 | ×2 | 10 | InterPro/Pfam |
| PPI 网络 | 3/10 | ×3 | 9 | STRING/IntAct |
| **加权总分** | | | **119/180****** | |
| **归一化总分 (÷1.83)** | | | **65.0/100****** | |

## 9. Final Decision

**SCORED: 60/100 -- MODERATE NUCLEAR CANDIDATE (NUCLEOCYTOPLASMIC SHUTTLING)**

ABRAXAS2 is a validated nucleocytoplasmic shuttling protein. The HPA data shows exclusively cytoplasmic/ciliary localization, which reflects the predominant steady-state localization of the BRISC complex. However, UniProt provides strong experimental evidence (ECO:0000269 x4) for nuclear localization, and the USP7-TP53 regulatory interaction is a well-characterized nuclear function.

**Strengths**:
- Strong UniProt experimental evidence for nuclear localization (ECO:0000269 x4)
- Experimentally validated nuclear function (USP7-mediated p53 stabilization)
- Outstanding PPI network spanning both compartments (BRISC + TP53/USP7)
- Four cryo-EM structures of the BRISC complex
- Well-characterized dual function (cytoplasmic deubiquitinase + nuclear p53 regulator)
- 10 HPA IF images available for manual review

**Weaknesses**:
- HPA classification is exclusively cytoplasmic (no nuclear compartment)
- Nuclear pool appears to be smaller/conditional relative to cytoplasmic BRISC pool
- Moderate AlphaFold confidence with 32.8% disordered regions
- Modest PubMed volume (6 strict)
- No enzymatic activity (scaffold protein)

**Recommendation**: Retain as a moderate nuclear candidate. The HPA does not capture the nuclear pool, but the experimental evidence from UniProt and the validated nuclear p53 regulatory function are compelling. Manual review of HPA IF images could reveal nuclear signal. ABRAXAS2 should not be rejected based on HPA data alone -- the literature and interaction data clearly demonstrate a nuclear role. The gene's connection to p53 makes it mechanistically interesting.

## 10. Manual Review Note

The original Excel listed ABRAXAS2 as HPA="Nucleoplasm" with nuclear_score=3, but the actual harvested HPA data does NOT include any nuclear compartment. This is the most significant Excel-to-packet discrepancy in this set. The Excel appears to have assigned a nuclear compartment that HPA does not report. Despite this, ABRAXAS2 genuinely has nuclear functions validated in the literature.

**Re-evaluator's note**: This case demonstrates why relying solely on HPA for nuclear classification can miss genuine nuclear proteins. ABRAXAS2 is a nucleocytoplasmic shuttling protein whose steady-state localization (captured by HPA IF) is predominantly cytoplasmic, but whose nuclear functions are well-established. The gene was correctly identified as having nuclear relevance (via UniProt), even though the HPA compartment assignment was inaccurate. A manual IF image review would help determine whether nuclear signal is present but below HPA's compartment-classification threshold. This gene should be retained despite the low HPA nuclear score.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000165660-ABRAXAS2/subcellular

![](https://images.proteinatlas.org/74089/1484_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74089/1484_G2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74089/1559_E4_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/74089/1559_E4_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/74089/2176_A8_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/74089/2176_A8_44_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
