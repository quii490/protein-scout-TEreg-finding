---
type: protein-evaluation
gene: ABLIM3
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleoplasm
  - actin-binding
  - lim-domain
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ABLIM3 (Actin-binding LIM protein 3) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | O94929 |
| **Protein Name** | Actin-binding LIM protein 3 |
| **Aliases** | KIAA0843 |
| **Length** | 683 aa |
| **Mass** | 77.8 kDa |
| **AlphaFold mean pLDDT** | 61.1 |
| **AlphaFold pLDDT >90** | 24.5% |
| **AlphaFold pLDDT <50** | 49.2% |
| **PubMed (strict)** | 19 |
| **PubMed (broad)** | 25 |
| **Function** | May act as scaffold protein. May stimulate ABRA activity and ABRA-dependent SRF transcriptional activity. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Cytoplasm** (ECO:0000250 -- by similarity)

**Note**: UniProt annotates ABLIM3 as cytoplasmic only, based on sequence similarity to other ABLIM family members. No nuclear annotation.

### GO Cellular Component
- GO:0015629 actin cytoskeleton (IBA:GO_Central)
- GO:0005737 cytoplasm (IEA:UniProtKB-SubCell)
- GO:0098978 glutamatergic synapse (IEA:Ensembl)
- GO:0030027 lamellipodium (IDA:MGI -- mouse experimental evidence)
- GO:0001725 stress fiber (IDA:MGI -- mouse experimental evidence)

**Note**: No nuclear GO-CC terms. All annotations are cytoplasmic or membrane-associated.

### HPA Subcellular Localization
- **Main location**: **Nucleoplasm**
- **Additional locations**: Cytosol
- **Reliability (IF)**: **Uncertain** (lowest tier with data)
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

**HPA Nuclear Localization Summary**: HPA classifies ABLIM3 as primarily nucleoplasmic with additional cytosolic localization. However, the reliability is "Uncertain" -- HPA's lowest confidence tier. No IF display images are available. The nucleoplasmic classification should be treated with caution given the "Uncertain" reliability flag.

**Critical Evidence Conflict**: There is a severe contradiction between HPA (Nucleoplasm main, Uncertain reliability) and UniProt/GO (cytoplasm only). The "Uncertain" HPA reliability flag strongly suggests that the IF data is ambiguous or inconsistent. This is a weaker nuclear case than genes with Approved or Supported reliability.

**Note on Excel discrepancy**: The original Sheet4 Excel listed ABLIM3 as HPA="Nuclear bodies" with nuclear_score=6. The actual harvested HPA data shows "Nucleoplasm" (not Nuclear bodies) as the main location. This is a significant misclassification in the original Excel.

## 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ABLIM3"[Title/Abstract] AND (gene OR protein OR hydrolase) | 19 | All gene-specific |
| Symbol-only: "ABLIM3"[Title/Abstract] | 23 | All gene-specific |
| Broad: "ABLIM3" | 25 | All gene-specific |

**Key Papers:**
- PMID:37797581 -- "An inhibitory circuit-based enhancer of DYRK1A function reverses Dyrk1a-associated impairment in social recognition" (Neuron, 2023). ABLIM3 identified in neuronal circuits.
- PMID:16328021 -- "Actin binding LIM protein 3 (abLIM3)" (Int J Mol Med, 2006). Early characterization paper.
- PMID:29529016 -- "Dentate granule cell recruitment of feedforward inhibition governs engram maintenance and remote memory generalization" (Nature Medicine, 2018). ABLIM3 in memory circuits.
- PMID:35426765 -- "Airway Aging and Methylation Disruptions in HIV-associated Chronic Obstructive Pulmonary Disease" (Am J Respir Crit Care Med, 2022).
- PMID:36778241 -- DYRK1A enhancer study (bioRxiv, 2023).

**Research Volume Assessment**: Modest but focused literature (19-25 papers). Research centers on neuronal function and actin cytoskeleton regulation. The Neuron paper (PMID:37797581) is the highest-impact publication. No papers specifically address nuclear localization or nuclear function. The gene symbol is unique with no acronym conflicts.

**Aliases observed**: KIAA0843

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-O94929-F1 (version 6)
- Mean pLDDT: 61.1 (LOW confidence)
- pLDDT >90: 24.5%, 70-90: 19.8%, <50: 49.2%
- PAE: Available (JSON file exists at EBI)

**Structure Assessment**: Low confidence AlphaFold model. Nearly half (49.2%) of residues have pLDDT below 50, indicating substantial intrinsic disorder. Only 24.5% are high-confidence (>90). This suggests ABLIM3 is largely disordered or contains long flexible linkers between structured domains. PAE data is available but the low confidence limits its utility.

### Experimental PDB Structures
| PDB ID | Method | Resolution | Coverage |
|--------|--------|------------|----------|
| 1UJS | NMR | - | 609-683 (C-terminal LIM domain) |
| 2DJ7 | NMR | - | 141-207 (internal LIM domain) |

**Structure Assessment**: Two solution NMR structures exist, each covering a single LIM domain. These represent small structured regions (75 aa and 67 aa respectively) within a largely disordered 683 aa protein. The experimental structures confirm that individual LIM domains are well-folded, but the overall protein architecture is flexible/disordered.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR032402 | ABLIM-type actin-binding domain |
| IPR051618 | Actin-binding LIM protein family |
| IPR003128 | Villin headpiece domain |
| IPR036886 | Villin headpiece domain superfamily |
| IPR001781 | Zinc finger, LIM-type |

| Pfam | Description |
|------|-------------|
| PF16182 | ABLIM N-terminal domain |
| PF00412 | LIM domain (zinc finger) |
| PF02209 | Villin headpiece domain |

**Domain Assessment**: ABLIM3 has a multi-domain architecture including actin-binding domains (villin headpiece), LIM domains (zinc finger protein interaction modules), and an ABLIM-specific N-terminal domain. LIM domains are known to mediate protein-protein interactions and can function in both cytoplasmic (cytoskeletal) and nuclear (transcriptional regulation) contexts. The presence of multiple LIM domains is notable -- LIM domain proteins (e.g., LMO, LDB1, FHL families) frequently shuttle between cytoplasm and nucleus and can regulate transcription. This provides a mechanistic rationale for possible nuclear localization despite UniProt's cytoplasmic annotation.

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| ABRA | 0.957 | 0.292 | 0 | 0.942 |
| ABLIM1 | 0.935 | 0 | 0.900 | 0.370 |
| CDC42 | 0.909 | 0 | 0.900 | 0.128 |
| RAC2 | 0.908 | 0 | 0.900 | 0.119 |
| RAC3 | 0.906 | 0 | 0.900 | 0.102 |
| SRF | 0.690 | 0 | 0 | 0.690 |
| NTN1 | 0.602 | 0 | 0.500 | 0.236 |
| TRIO | 0.586 | 0 | 0.500 | 0.180 |
| DCC | 0.564 | 0 | 0.500 | 0.164 |
| AFAP1L1 | 0.546 | 0 | 0 | 0.501 |
| RAC1 | 0.531 | 0 | 0.500 | 0.102 |
| DOCK1 | 0.529 | 0 | 0.500 | 0.047 |
| SRC | 0.510 | 0 | 0.500 | 0 |
| PTK2 | 0.501 | 0 | 0.500 | 0 |
| NCK1 | 0.499 | 0 | 0.500 | 0 |

**STRING Assessment**: STRING places ABLIM3 in an actin cytoskeleton regulatory network centered on ABRA, LIM family proteins, and small GTPases (CDC42, RAC1/2/3). The SRF (serum response factor) connection via textmining (0.69) is notable -- SRF is a transcription factor, consistent with the known ABRA-dependent SRF transcriptional activity of ABLIM3. However, most interactions are database-derived or textmining-based rather than experimental.

### IntAct (15 interactions)
| Partner | Method | PMID | Type |
|---------|--------|------|------|
| GRB2 | Pull down | 12577067 | Association |
| MCM7 | co-IP | 23764002 | Association |
| Mycbp2 | co-IP | 28671696 | Association |
| IKZF3 | Two-hybrid array | 31515488 | Physical association |
| CCDC33 | Two-hybrid array | 31515488 | Physical association |
| ABI2 | Two-hybrid array | 32296183 | Physical association |
| PALMD | Two-hybrid | 32296183 | Physical association |
| HIKESHI | Two-hybrid array | 32296183 | Physical association |
| CWF19L2 | Two-hybrid array | 32296183 | Physical association |
| ZNF620 | Validated two-hybrid | 32296183 | Physical association |
| CATSPER1 | Validated two-hybrid | 32296183 | Physical association |
| SNW1 | Validated two-hybrid | 32296183 | Physical association |
| CBX8 | Validated two-hybrid | 32296183 | Physical association |
| ENSP00000425394.1 | Two-hybrid | 20711500 | Physical association |

### UniProt Interactions (13 entries)
Includes interactions with IKZF3, SSX2IP, ABI2, BANP, CATSPER1, CBX8, CWF19L2, HIKESHI, PALMD, SNW1, TFIP11, ZNF620 (via isoforms).

**PPI Assessment**: Interesting network. Several nuclear protein interactions: MCM7 (DNA replication), SNW1 (transcriptional coactivator/spliceosome), CBX8 (Polycomb group chromatin regulator), IKZF3 (transcription factor), ZNF620 (zinc finger protein). These nuclear interactions are noteworthy for a protein classified as cytoplasmic and suggest potential nuclear functions. The MCM7 co-IP (PMID:23764002) and CBX8 validated two-hybrid (PMID:32296183) are the most mechanistically interesting.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20 | Based on HPA/UniProt/GO evidence |
| 蛋白大小 | 4/10 | ×1 | 4 | |
| 研究新颖性 | 10/10 | ×5 | 20 | PubMed strict count |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT |
| 调控结构域 | 4/10 | ×2 | 8 | InterPro/Pfam |
| PPI 网络 | 2/10 | ×3 | 6 | STRING/IntAct |
| **加权总分** | | | **103/180**** | |
| **归一化总分 (÷1.83)** | | | **56.3/100**** | |

## 9. Final Decision

**SCORED: 45/100 -- BORDERLINE-WEAK CANDIDATE, CONDITIONALLY RETAINED**

ABLIM3 presents an ambiguous evaluation case. The HPA nuclear evidence is weak (Uncertain reliability, no IF display images), and UniProt/GO-CC annotations are exclusively cytoplasmic. However, several factors suggest nuclear potential worth investigating: LIM domain proteins frequently have nuclear functions, multiple PPI partners are nuclear proteins (MCM7, SNW1, CBX8), and the SRF transcriptional connection provides a plausible mechanism for nucleocytoplasmic shuttling.

**Strengths**:
- Multi-domain scaffold with LIM domains (known nuclear/cytoplasmic shuttle capability)
- PPI network includes several nuclear protein partners (MCM7, SNW1, CBX8, IKZF3)
- SRF transcriptional activity connection via ABRA -- potential nuclear signaling role
- Modest but real PubMed literature (19 papers)
- IntAct interactions with validated two-hybrid entries

**Weaknesses**:
- HPA nuclear evidence is "Uncertain" -- lowest confidence tier
- No HPA IF display images
- UniProt and GO-CC exclusively cytoplasmic
- AlphaFold model is largely disordered (49.2% <50 pLDDT)
- Only fragment-level PDB structures (individual LIM domains by NMR)
- No paper specifically investigates nuclear localization or function

**Recommendation**: Retain at low priority with a note that nuclear localization needs experimental validation. ABLIM3 is more likely a primarily cytoplasmic actin-binding protein that may shuttle to the nucleus under specific conditions (consistent with LIM domain biology). The gene should not have been rejected purely on template -- the LIM domain family is well-precedented for nuclear functions -- but the overall evidence for constitutive nuclear localization is weak.

## 10. Manual Review Note

The original Excel classified ABLIM3 as HPA="Nuclear bodies" with nuclear_score=6, but the actual harvested HPA data shows "Nucleoplasm" (not Nuclear bodies) with "Uncertain" reliability. This represents two errors in the original assessment: (1) the nuclear compartment was misclassified, and (2) the Uncertain reliability flag was not considered. The Excel's nuclear_score=6 appears inflated relative to the actual evidence quality.

**Re-evaluator's note**: This gene illustrates the importance of checking HPA reliability tiers. The "Uncertain" flag is a strong caution signal. The gene's LIM domain architecture and nuclear PPI partners provide plausible nuclear biology, but the experimental HPA evidence is not compelling. This should be considered a candidate requiring validation rather than a confirmed nuclear protein.

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000173210-ABLIM3/subcellular

![](https://images.proteinatlas.org/2472/1875_C2_16_cr5b7c0b5cdd9fd_red_green.jpg)
![](https://images.proteinatlas.org/2472/1875_C2_2_cr5b7c0b5cdd6ee_red_green.jpg)
![](https://images.proteinatlas.org/2472/1904_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/2472/1904_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/2472/1913_E14_1_red_green.jpg)
![](https://images.proteinatlas.org/2472/1913_E14_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
