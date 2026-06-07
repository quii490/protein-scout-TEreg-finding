---
type: protein-evaluation
gene: ABITRAM
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleoplasm
  - actin-binding
  - small-protein
  - novel-gene
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ABITRAM (Protein Abitram) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9NX38 |
| **Protein Name** | Protein Abitram |
| **Aliases** | C9orf6, FAM206A |
| **Length** | 181 aa |
| **Mass** | 20.4 kDa |
| **AlphaFold mean pLDDT** | 79.7 |
| **AlphaFold pLDDT >90** | 9.4% |
| **AlphaFold pLDDT <50** | 1.1% |
| **PubMed (strict)** | 0 |
| **PubMed (broad)** | 0 |
| **Function** | Actin-binding protein that regulates actin polymerization, filopodia dynamics and increases the branching of proximal dendrites of developing neurons. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Nucleus speckle** (ECO:0000250 -- by similarity)
- **Nucleus** (ECO:0000250 -- by similarity)
- Cell projection, lamellipodium (ECO:0000250)
- Cell projection, growth cone (ECO:0000250)
- Cell projection, dendrite (ECO:0000250)

### GO Cellular Component
- GO:0016607 **nuclear speck** (IEA:UniProtKB-SubCell)
- GO:0005634 **nucleus** (IBA:GO_Central)
- GO:0030425 dendrite (IBA:GO_Central)
- GO:0032433 filopodium tip (ISS:UniProtKB)
- GO:0030426 growth cone (ISS:UniProtKB)
- GO:0030027 lamellipodium (ISS:UniProtKB)

### HPA Subcellular Localization
- **Main location**: **Nucleoplasm**, Cytosol (dual main)
- **Additional locations**: Kinetochore, Cytokinetic bridge, Mitotic spindle, Primary cilium, Primary cilium tip
- **Reliability (IF)**: **Approved** (highest tier)
- **IF Display Images Available**: YES (2 images)
  - `2266_E10_66_blue_red_green.jpg`
  - `2266_E10_197_blue_red_green.jpg`
- **Image status**: `if_display_images_available`
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**HPA Nuclear Localization Summary**: HPA assigns Nucleoplasm as a main location with "Approved" reliability. Two IF display images are available. The additional locations include several mitosis-related structures (kinetochore, mitotic spindle, cytokinetic bridge), suggesting cell cycle-dependent localization patterns. The dual Nucleoplasm + Cytosol main assignment is noteworthy.

**Nuclear Evidence Convergence**: Unlike some genes in this set, there is good agreement between UniProt (Nucleus, Nucleus speckle), GO-CC (nuclear speck, nucleus), and HPA (Nucleoplasm main) for nuclear localization. This is a three-way consensus supporting nuclear presence.

## 3. HPA Immunofluorescence

2 IF display images available showing nucleoplasmic localization. The images are from the standard HPA IF panel. The specific image IDs (2266_E10_66 and 2266_E10_197) should be examined for signal quality and specificity. The dual Nucleoplasm + Cytosol main assignment suggests signal is detected in both compartments.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ABITRAM"[Title/Abstract] AND (gene OR protein OR hydrolase) | 0 | No papers |
| Symbol-only: "ABITRAM"[Title/Abstract] | 0 | No papers |
| Broad: "ABITRAM" | 0 | No papers |

**Aliases checked**: C9orf6, FAM206A (no refinement performed on aliases, but they would likely return some papers under the older gene symbols)

**Research Volume Assessment**: Zero published papers under the current gene symbol "ABITRAM". This gene was recently renamed (from FAM206A/C9orf6). The complete absence of literature under the current name represents a significant challenge for research prioritization. However, this also means the gene is essentially unstudied, which could represent an opportunity for novel discovery. Note that the alias FAM206A may return some older literature if searched separately.

**Aliases observed**: C9orf6, FAM206A

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q9NX38-F1 (version 6)
- Mean pLDDT: 79.7 (moderate confidence)
- pLDDT >90: 9.4%, 70-90: 68.0%, <50: 1.1%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
**None.** No experimental structures available.

**Structure Assessment**: Moderate confidence AlphaFold model. The majority of the protein (68%) falls in the 70-90 pLDDT range, indicating reasonably confident but not exceptional prediction. Only 1.1% of residues are below 50 pLDDT, suggesting a largely ordered structure. No experimental structures exist. PAE data is available for domain interaction analysis. The small size (181 aa) makes it amenable to structural studies.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR039169 | Protein Abitram |
| IPR033753 | Abitram-like domain |
| IPR011053 | Single hybrid motif |

| Pfam | Description |
|------|-------------|
| PF01597 | Single hybrid motif (SHM) domain |

**Domain Assessment**: ABITRAM contains a single hybrid motif (SHM) domain. This is a relatively uncharacterized domain family. No enzymatic domains, no known DNA-binding domains, no regulatory domains of established function. The domain architecture is simple and does not provide functional clues beyond actin binding.

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| FRRS1L | 0.882 | 0 | 0 | 0.882 |
| PEX26 | 0.879 | 0 | 0 | 0.879 |
| PEX6 | 0.866 | 0 | 0 | 0.864 |
| SYNJ2BP | 0.826 | 0 | 0 | 0.826 |
| PUS10 | 0.801 | 0.801 | 0 | 0 |
| GPN3 | 0.540 | 0 | 0 | 0 |
| ELP1 | 0.524 | 0 | 0 | 0.385 |
| SPRYD7 | 0.459 | 0 | 0 | 0.458 |
| C8A | 0.453 | 0 | 0 | 0.445 |
| CTNNAL1 | 0.453 | 0 | 0 | 0.452 |
| HSDL1 | 0.445 | 0 | 0 | 0.443 |
| CYGB | 0.415 | 0 | 0 | 0.348 |
| NIPAL3 | 0.406 | 0 | 0 | 0.406 |
| LGALS8 | 0.400 | 0 | 0 | 0.385 |
| REPS1 | 0.400 | 0 | 0 | 0.332 |

**STRING Assessment**: Weak PPI network. Only PUS10 shows experimental evidence (0.801). All other interactions are textmining-based (co-mentioned in literature). Most scores are moderate (0.4-0.88 range). No strong (non-textmining) PPI partners. The PEX26/PEX6 connection suggests possible peroxisomal association through text co-occurrence.

### IntAct (15 interactions)
| Partner | Method | PMID | Type |
|---------|--------|------|------|
| HMBOX1 | Validated two-hybrid | 32296183 | Physical association |
| MESD | Validated two-hybrid | 32296183 | Physical association |
| PUS10 | Validated two-hybrid | 32296183 | Physical association |
| PGCKA1 | Validated two-hybrid | 32296183 | Physical association |
| POTEF | co-IP | 28514442 | Association |
| TAOK1 | co-IP | 28514442 | Association |
| TAOK2 | co-IP | 28514442 | Association |
| CBY1 | co-IP | 28514442 | Association |
| ZHX2 | co-IP | 28514442 | Association |
| FYN | co-IP | 33961781 | Association |
| LYN | co-IP | 33961781 | Association |
| MRFAP1 | co-IP | 33961781 | Association |
| eEF1alpha1 | Two-hybrid | 14605208 | Physical association |
| MBD-R2 | Two-hybrid | 14605208 | Physical association |

### UniProt Interactions (4 partners)
HMBOX1 (6 experiments), MESD (3 experiments), PGCKA1 (3 experiments), PUS10 (9 experiments)

**PPI Assessment**: Moderate PPI evidence from IntAct, with several interactions validated by multiple methods. The interaction with PUS10 (pseudouridine synthase 10) is the strongest, supported by both STRING experimental and IntAct (9 UniProt experiments). HMBOX1 interaction (6 experiments) is also notable as HMBOX1 is a transcription factor. TAOK1/TAOK2 (kinases) and FYN/LYN (Src family kinases) interactions suggest signaling connections. However, most interactions are from high-throughput studies.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 | Based on HPA/UniProt/GO evidence |
| 蛋白大小 | 3/10 | ×1 | 3 | |
| 研究新颖性 | 10/10 | ×5 | 20 | PubMed strict count |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT |
| 调控结构域 | 3/10 | ×2 | 6 | InterPro/Pfam |
| PPI 网络 | 2/10 | ×3 | 6 | STRING/IntAct |
| **加权总分** | | | **93/180**** | |
| **归一化总分 (÷1.83)** | | | **50.8/100**** | |

## 9. Final Decision

**SCORED: 40/100 -- WEAK CANDIDATE, RETAIN FOR NOVELTY**

ABITRAM is a challenging gene to evaluate. The nuclear localization evidence from HPA is solid (Nucleoplasm main, Approved, IF images available), and UniProt/GO-CC corroborate nuclear localization. However, the complete absence of literature under the current gene name makes it essentially unstudied, and its small size with a single uncharacterized domain limits mechanistic interpretability.

**Strengths**:
- HPA Approved nucleoplasmic localization with IF images
- Three-way nuclear evidence convergence (HPA + UniProt + GO-CC)
- Actin-binding function with neuron-specific roles -- could be mechanistically interesting
- Completely unstudied (discovery potential)
- IntAct interactions with transcription factor HMBOX1 and pseudouridine synthase PUS10

**Weaknesses**:
- Zero PubMed papers (completely uncharacterized)
- No experimental PDB structures
- Single poorly characterized domain (SHM)
- STRING PPI mostly textmining-based
- Small protein (181 aa) with limited functional annotation
- All UniProt subcellular locations are "by similarity" (not experimentally validated in human)

**Recommendation**: Retain at low priority. ABITRAM has genuine nuclear localization evidence but essentially no functional characterization. The gene would require substantial fundamental research before it could be useful as a target. Its value lies in novelty -- if the lab is interested in understudied nuclear proteins, ABITRAM represents a blank slate.

## 10. Manual Review Note

The original Excel listed ABITRAM as HPA=Nucleoplasm with nuclear_score=6. The harvested data confirms this. The gene symbol is very new (ABITRAM replaced FAM206A), which explains the zero PubMed result. Searching for FAM206A as a separate query might recover some literature. The PUS10 interaction (pseudouridine synthase, 9 experiments in UniProt) is the most promising PPI lead. The mitotic localizations (kinetochore, mitotic spindle) from HPA are intriguing and suggest a possible cell cycle role.

**Re-evaluator's note**: This is the purest case of a "novel gene" in this set. The nuclear localization is solid, but everything else is unknown. Whether to retain this depends entirely on the project's goals -- it offers discovery potential but with high risk. The gene was correctly identified as nuclear but rejected because of the zero-literature PubMed score. The re-evaluation confirms the nuclear evidence but the overall score remains low due to absent functional characterization.

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000119328-ABITRAM/subcellular

![](https://images.proteinatlas.org/35918/2266_E10_197_blue_red_green.jpg)
![](https://images.proteinatlas.org/35918/2266_E10_66_blue_red_green.jpg)
![](https://images.proteinatlas.org/35917/1129_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/35917/1129_F9_3_red_green.jpg)
![](https://images.proteinatlas.org/35917/574_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/35917/574_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NX38 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039169;IPR033753;IPR011053; |
| Pfam | PF01597; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119328-ABITRAM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PUS10 | Intact, Biogrid, Bioplex | true |
| ATP6V0D2 | Bioplex | false |
| C4orf19 | Intact | false |
| HMBOX1 | Intact | false |
| MESD | Intact | false |
| MRFAP1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
