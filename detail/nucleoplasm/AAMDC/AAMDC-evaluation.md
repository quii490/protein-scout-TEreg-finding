---
type: protein-evaluation
gene: AAMDC
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleoplasm
  - small-protein
  - oncogene
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# AAMDC (Mth938 domain-containing protein) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9H7C9 |
| **Protein Name** | Mth938 domain-containing protein |
| **Aliases** | C11orf67 |
| **Length** | 122 aa |
| **Mass** | 13.3 kDa |
| **AlphaFold mean pLDDT** | 97.7 |
| **AlphaFold pLDDT >90** | 99.2% |
| **AlphaFold pLDDT <50** | 0.0% |
| **PubMed (strict)** | 5 |
| **PubMed (broad)** | 6 |
| **Function** | May play a role in preadipocyte differentiation and adipogenesis. Has been characterized as an oncogene in estrogen receptor-positive breast cancer (PMID:33772001), linking PI3K-AKT-mTOR signaling with metabolic reprogramming. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Cytoplasm** (ECO:0000250 -- by similarity, not experimental)

**Note**: UniProt annotates AAMDC as cytoplasmic only, based on sequence similarity. There is NO UniProt nuclear annotation.

### GO Cellular Component
- GO:0005737 **cytoplasm** (ISS:UniProtKB -- inferred from sequence similarity)

**Note**: Only one GO-CC term, and it is cytoplasmic. No nuclear GO terms.

### HPA Subcellular Localization
- **Main location**: **Nucleoplasm**
- **Additional locations**: Cytosol
- **Reliability (IF)**: **Approved** (highest tier)
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**Critical Evidence Conflict**: There is a direct contradiction between HPA (Nucleoplasm main, Approved) and UniProt/GO (cytoplasm only, by similarity). UniProt annotation is computational (by similarity), while HPA annotation is based on experimental IF data. The HPA Approved reliability suggests strong experimental support for nucleoplasmic localization despite the lack of published IF display images.

## 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "AAMDC"[Title/Abstract] AND (gene OR protein OR hydrolase) | 5 | All gene-specific |
| Symbol-only: "AAMDC"[Title/Abstract] | 6 | All gene-specific |
| Broad: "AAMDC" | 6 | All gene-specific |

**Key Papers:**
- PMID:33772001 -- "The oncogene AAMDC links PI3K-AKT-mTOR signaling with metabolic reprograming in estrogen receptor-positive breast cancer" (Nature Communications, 2021). This is a high-impact paper establishing AAMDC as an oncogene.
- PMID:31116411 -- "Adipogenesis associated Mth938 domain containing (AAMDC) protein expression is regulated by alternative polyadenylation and microRNAs" (FEBS Letters, 2019).
- PMID:36167494 -- "Genome-wide association analyses of common infections in a large practice-based biobank" (BMC Genomics, 2022).
- PMID:30155244 -- "Fat deposition deficiency is critical for the high mortality of pre-weanling newborn piglets" (J Animal Sci Biotechnol, 2018).
- PMID:39935538 -- "Transcriptional profiles analysis of effects of Toxoplasma gondii rhoptry protein 16 on THP-1 macrophages" (Front Cell Infect Microbiol, 2024).

**Research Volume Assessment**: Very low publication volume (6 papers total). However, the one high-impact paper in Nature Communications (PMID:33772001) establishes AAMDC as a bona fide oncogene with mechanistic characterization. This single paper carries substantial weight. The gene symbol is unique (no acronym conflicts).

**Aliases observed**: C11orf67

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q9H7C9-F1 (version 6)
- Mean pLDDT: 97.7 (EXCEPTIONALLY HIGH)
- pLDDT >90: 99.2%, 70-90: 0.8%, <50: 0.0%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
| PDB ID | Method | Resolution | Coverage |
|--------|--------|------------|----------|
| 2AB1 | X-ray | 2.59 A | Full (2-122, chains A/B) |
| 2Q4Q | X-ray | 2.59 A | Full (2-122, chains A/B) |

**Structure Assessment**: Excellent structural coverage. Two independent X-ray crystal structures at 2.59A resolution covering the full protein. AlphaFold model has exceptionally high confidence (mean pLDDT 97.7, 99.2% >90). This is one of the best structurally characterized proteins in the set. The small size (122 aa) makes it highly amenable to structural biology approaches.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR034096 | Mth938 domain |
| IPR036748 | Mth938 domain superfamily |
| IPR007523 | Domain of unknown function DUF541 |

| Pfam | Description |
|------|-------------|
| PF04430 | DUF541 (Mth938 domain) |

**Domain Assessment**: AAMDC contains the Mth938 domain (DUF541), which is a domain of unknown function. The domain is structurally well-characterized (two X-ray structures) but its molecular function remains uncharacterized. The oncogenic function described in PMID:33772001 is not explained by known domain functions, suggesting novel biology.

## 7. Protein-Protein Interaction Network

### STRING
**STRING query failed** (URLError: EOF occurred in violation of protocol). No STRING data available.

### IntAct (12 interactions)
| Partner | Method | PMID | Type |
|---------|--------|------|------|
| OCRL | co-IP | 32203420 | Association |
| Arhgap30 | co-IP | 32203420 | Association |
| VPS9D1 | Two-hybrid array | 32296183 | Physical association |
| Rab7a | co-IP | 26496610 | Association |
| ACY3 | Two-hybrid array | 25416956 | Physical association |
| GORASP2 | Two-hybrid array | 25416956 | Physical association |
| TRIM54 | Two-hybrid prey pooling | 31391242 | Physical association |
| HTT | Two-hybrid array | 32814053 | Physical association |
| GDAP1 | Two-hybrid array | 32814053 | Physical association |
| ATXN3 | Two-hybrid pooling | 32814053 | Physical association |
| APP | Two-hybrid array | 32814053 | Physical association |
| DNM2 | Two-hybrid pooling | 32814053 | Physical association |

### UniProt Interactions (8 partners)
ACY3, APP, ATXN3, DNM2, GDAP1, GORASP2, HTT, VPS9D1 (all with 3 experiments)

**PPI Assessment**: Moderate PPI evidence from IntAct (12 interactions, mostly from two-hybrid screens). Notable interactions with HTT (huntingtin, PMID:32814053), APP (amyloid precursor protein), and ATXN3 (ataxin-3). These are disease-relevant partners. STRING data is unavailable due to a server error. Overall PPI evidence is moderate but includes some interesting disease-relevant interactions.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20 | Based on HPA/UniProt/GO evidence |
| 蛋白大小 | 4/10 | ×1 | 4 | |
| 研究新颖性 | 10/10 | ×5 | 25 | PubMed strict count |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT |
| 调控结构域 | 4/10 | ×2 | 8 | InterPro/Pfam |
| PPI 网络 | 3/10 | ×3 | 9 | STRING/IntAct |
| **加权总分** | | | **109/180**** | |
| **归一化总分 (÷1.83)** | | | **59.6/100**** | |

## 9. Final Decision

**SCORED: 51/100 -- BORDERLINE CANDIDATE, CONDITIONALLY RETAINED**

AAMDC presents a challenging evaluation case. The HPA data (Approved reliability, Nucleoplasm main) strongly supports nuclear localization, but this is contradicted by UniProt and GO annotations. The protein is very small (122 aa) with limited functional characterization.

**Strengths**:
- HPA Approved reliability for nucleoplasmic localization
- Exceptional AlphaFold model (mean pLDDT 97.7)
- Two high-quality X-ray crystal structures (2.59A)
- Established oncogene role in breast cancer (Nature Communications, 2021)
- Unique gene symbol -- no literature pollution

**Weaknesses**:
- Direct contradiction between HPA (nuclear) and UniProt (cytoplasmic)
- No nuclear GO-CC terms
- Very small protein (122 aa) with single domain of unknown function
- Low PubMed count (5-6 papers)
- No HPA IF display images available
- STRING data unavailable
- Most IntAct interactions from high-throughput two-hybrid screens, not targeted studies

**Recommendation**: Retain as borderline candidate. The HPA Approved nuclear classification deserves weight, and the oncogene role is intriguing. However, the conflict with UniProt annotation and the general lack of nuclear context in other databases warrant caution. This protein would benefit from a manual verification of the HPA IF raw images to confirm the nuclear signal.

## 10. Manual Review Note

The original Excel assigned AAMDC with HPA="Nuclear speckles|Nucleoplasm" and nuclear_score=6. The actual harvested HPA data shows only "Nucleoplasm" main (no nuclear speckles). The HPA reliability is "Approved" -- the highest tier. The critical issue is the HPA/UniProt contradiction. A reviewer should manually examine whether the HPA IF signal genuinely supports nuclear localization or whether the Approved annotation might be an artifact for such a small protein. If the nuclear localization is confirmed, the score could be revised upward.

**Re-evaluator's note**: The original template rejection was likely due to the UniProt annotation showing cytoplasm only. However, the HPA Approved nuclear classification cannot be dismissed. This gene needs a manual IF image review to resolve the conflict. It should not have been template-rejected without examining the evidence.

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000087884-AAMDC/subcellular

![](https://images.proteinatlas.org/37918/404_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37918/404_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/37918/407_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37918/407_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/37918/410_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37918/410_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
