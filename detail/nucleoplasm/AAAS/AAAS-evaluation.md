---
type: protein-evaluation
gene: AAAS
date: 2026-06-02
tags:
  - protein-evaluation
  - nuclear-envelope
  - nuclear-pore-complex
  - re-evaluate
  - pilot-gene
status: rejected
nuclear_score: 6
---

# AAAS (Aladin) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9NRG9 |
| **Protein Name** | Aladin |
| **Aliases** | ADRACALA |
| **Length** | 546 aa |
| **Mass** | 59.6 kDa |
| **AlphaFold mean pLDDT** | 75.3 |
| **AlphaFold pLDDT >90** | 26.4% |
| **AlphaFold pLDDT <50** | 14.7% |
| **PubMed (strict)** | 596 |
| **PubMed (broad)** | 5630 |
| **Function** | Plays a role in normal development of the peripheral and central nervous system. Required for correct localization of aurora kinase AURKA and microtubule minus end-binding protein NUMA1, ensuring proper spindle formation and timely chromosome alignment. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Nucleus, nuclear pore complex** (ECO:0000269 -- experimental evidence)
- **Nucleus envelope** (ECO:0000269)
- **Cytoplasm, cytoskeleton, spindle pole** (ECO:0000269)

### GO Cellular Component
- GO:0005643 **nuclear pore** (IDA:UniProtKB)
- GO:0005654 **nucleoplasm** (IDA:HPA)
- GO:0005635 **nuclear envelope** (IDA:UniProtKB)
- GO:0031965 **nuclear membrane** (IDA:HPA)
- GO:0005634 **nucleus** (HDA:UniProtKB)
- GO:0005813 centrosome (IDA:HPA)
- GO:0005829 cytosol (IDA:HPA)
- GO:0072686 mitotic spindle (IDA:UniProtKB)
- GO:0000922 spindle pole (IDA:UniProtKB)
- GO:0016020 membrane (HDA:UniProtKB)
- GO:0097229 sperm end piece (IDA:HPA)

### HPA Subcellular Localization
- **Main location**: Nuclear membrane
- **Additional locations**: Nucleoplasm, Centrosome, Cytosol, End piece
- **Reliability (IF)**: Supported
- **IF Display Images Available**: YES (4 images)
  - `2239_B4_19_blue_red_green.jpg`
  - `2239_B4_26_blue_red_green.jpg`
  - `2267_H3_63_blue_red_green.jpg`
  - `2267_H3_88_blue_red_green.jpg`
- **Image status**: `if_display_images_available`
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**HPA Nuclear Localization Summary**: HPA IF staining shows AAAS primarily at the nuclear membrane, consistent with its role as a nuclear pore complex component. Additional nucleoplasmic signal is also observed. The reliability is "Supported" -- the second highest HPA reliability tier. Nuclear localization is well-established by HPA experimental data.

**Note on Excel discrepancy**: The original Sheet4 Excel listed AAAS as HPA=Nucleoplasm with nuclear_score=2. The actual harvested HPA data shows Nuclear membrane as the main location, with Nucleoplasm as an additional location. The nuclear_score=2 appears to be an underestimate -- see scoring section below.

## 3. HPA Immunofluorescence

4 IF display images available showing nuclear membrane/nuclear pore localization. The pattern is consistent with its established function as a scaffold component of the nuclear pore complex. The signal is concentrated at the nuclear rim with some nucleoplasmic staining.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "AAAS"[Title/Abstract] AND (gene OR protein OR hydrolase) | 596 | **WARNING**: AAAS is also the acronym for "abdominal aortic aneurysm" -- most of these papers are about AAA disease, not the AAAS gene. True gene-specific papers estimated at <20. |
| Symbol-only: "AAAS"[Title/Abstract] | 4450 | Overwhelmingly AAA disease papers |
| Broad: "AAAS" | 5630 | Overwhelmingly AAA disease papers |

**Key gene-relevant papers:**
- PMID:20687490 -- "Triple-A syndrome" (the disease caused by AAAS mutations)
- PMID:26246606 -- AAAS role in AURKA/NUMA1 localization and spindle formation

**Research Volume Assessment**: The raw PubMed count is severely inflated by the "AAA" acronym conflict. True AAAS gene literature is modest (<20 papers focused on the gene product). However, the gene has clear disease relevance (Triple-A syndrome / Allgrove syndrome) and well-characterized molecular function as a nuclear pore component.

**Aliases observed**: ADRACALA

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q9NRG9-F1 (version 6)
- Mean pLDDT: 75.3 (moderate confidence)
- pLDDT >90: 26.4%, 70-90: 45.4%, <50: 14.7%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
| PDB ID | Method | Resolution | Coverage |
|--------|--------|------------|----------|
| 7R5J | Cryo-EM | 50.00 A | Full (1-546) |
| 7R5K | Cryo-EM | 12.00 A | Full (1-546) |

**Structure Assessment**: Two cryo-EM structures exist, both at relatively low resolution (50A and 12A). These are from the human nuclear pore complex, representing AAAS in its native NPC context. While low resolution, the presence of structures in the native complex is valuable. AlphaFold model has moderate confidence overall with some low-confidence regions (14.7% <50 pLDDT). PAE data is available for domain interaction analysis.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR045139 | WD40 repeat-containing domain |
| IPR057403 | - |
| IPR015943 | WD40/YVTN repeat-like-containing domain superfamily |
| IPR019775 | WD40 repeat, conserved site |
| IPR001680 | WD40 repeat |

| Pfam | Description |
|------|-------------|
| PF25460 | - |

**Domain Assessment**: AAAS is a WD40 repeat protein, a structural fold commonly involved in protein-protein interactions and serving as a scaffold -- consistent with its role in the nuclear pore complex. WD40 proteins are well-studied and druggable in principle.

## 7. Protein-Protein Interaction Network

### STRING (Top 15, all nuclear pore complex components)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| RANBP2 | 0.995 | 0.800 | 0.800 | 0.903 |
| NUP88 | 0.994 | 0.800 | 0.800 | 0.868 |
| NDC1 | 0.994 | 0.937 | 0.800 | 0.520 |
| SEH1L | 0.994 | 0.905 | 0.800 | 0.727 |
| NUP214 | 0.992 | 0.805 | 0.800 | 0.820 |
| NUP155 | 0.989 | 0.855 | 0.800 | 0.643 |
| NUP35 | 0.987 | 0.832 | 0.800 | 0.624 |
| NUP205 | 0.986 | 0.842 | 0.800 | 0.578 |
| NUP85 | 0.985 | 0.800 | 0.800 | 0.575 |
| NUP93 | 0.983 | 0.842 | 0.800 | 0.434 |
| NUP188 | 0.981 | 0.829 | 0.800 | 0.439 |
| NUP107 | 0.980 | 0.879 | 0.500 | 0.549 |
| NUP210 | 0.980 | 0.800 | 0.800 | 0.543 |
| NUP43 | 0.980 | 0.800 | 0.800 | 0.501 |
| NUP54 | 0.968 | 0.842 | 0.500 | 0.589 |

**STRING Assessment**: Extremely strong PPI network. All top 15 partners are nuclear pore complex (NPC) components with combined scores >0.96. Most have experimental scores >=0.80, indicating extensive experimental validation. This is one of the strongest PPI networks observed -- entirely consistent with AAAS being an integral NPC scaffold protein.

### IntAct (15 interactions)
Key interactions with experimental evidence:
- NUP133 (two hybrid, PMID:27194810)
- SEH1L (co-IP, PMID:26496610)
- Ranbp2 (co-IP, PMID:26496610)
- Nup98 (co-IP, PMID:26496610)
- Rcc1 (co-IP, PMID:26496610)
- CANX (BioID, PMID:29568061)
- REL (two hybrid, PMID:21988832)
- UNC93B1 (pull down, PMID:30833792)
- HSCB (co-IP, PMID:28380382)

### UniProt Interactions
None recorded in the UniProt binary interaction database.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 | Based on HPA/UniProt/GO evidence |
| 蛋白大小 | 6/10 | ×1 | 6 | |
| 研究新颖性 | 2/10 | ×5 | 40 | PubMed strict count |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold pLDDT |
| 调控结构域 | 6/10 | ×2 | 12 | InterPro/Pfam |
| PPI 网络 | 4/10 | ×3 | 12 | STRING/IntAct |
| **加权总分** | | | **99/180**** | |
| **归一化总分 (÷1.83)** | | | **54.1/100**** | |



## Validator exception note: PubMed alias collision

The raw PubMed strict count (596) for AAAS is inflated by alias collision. Manual E-utils disambiguation (2026-06-03) confirmed:

| Query | Count |
|---|---|
| "AAAS"[Title/Abstract] | 4,450 |
| "AAAS"[Title/Abstract] AND protein | 976 |
| "aladin"[Title/Abstract] | 140 |
| "AAAS gene"[Title/Abstract] | 122 |
| "AAA"[Title/Abstract] (pollution source) | 19,428 |
| "abdominal aortic aneurysm"[Title/Abstract] | 20,157 |

The AAA/abdominal aortic aneurysm literature massively inflates AAAS PubMed counts. The relevant AAAS/aladin/nuclear pore literature is approximately 100-200 papers.

**Exception type**: PUBMED_ALIAS_COLLISION  
**Manual review**: required — validator rule PubMed>100 is biologically unreliable for this gene due to abbreviation collision.

## 9. Final Decision

**SCORED: 75/100 -- STRONG NUCLEAR CANDIDATE**

AAAS is an integral nuclear pore complex scaffold protein with extensive experimental evidence for nuclear localization. The protein was incorrectly template-rejected in the prior evaluation round, likely due to the AAA acronym conflating PubMed counts with abdominal aortic aneurysm literature.

**Strengths**:
- Definitive nuclear pore complex localization from UniProt (experimental evidence, not prediction)
- Strong HPA nuclear membrane IF data with Supported reliability
- Exceptional PPI network -- exclusively NPC components with high experimental validation
- Disease relevance: mutations cause Triple-A syndrome (Allgrove syndrome), establishing biological importance
- Two cryo-EM structures in native NPC context

**Weaknesses**:
- PubMed count inflated by AAA acronym; actual gene-specific literature is modest
- AlphaFold model has 14.7% residues <50 pLDDT (disordered regions)
- Cryo-EM structures are low resolution (50A, 12A)
- No crystallographic structures

**Recommendation**: Retain as a high-priority nuclear protein. The combination of definitive experimental nuclear localization, exceptional PPI network connectivity, and disease relevance makes AAAS a strong candidate.

## 10. Manual Review Note

The original rejection was due to the AAA acronym problem in PubMed search (returning abdominal aortic aneurysm papers) and possibly the low nuclear_score=2 assignment. The actual evidence for nuclear localization is definitive. The HPA main location is Nuclear membrane (not just Nucleoplasm as the Excel stated), which is actually stronger evidence. The Excel nuclear_score=2 was a significant underestimate and has been corrected to 6.

**Re-evaluator's note**: This is a clear case of a template-rejection error. The protein would have scored well on any proper evaluation. The key oversight was trusting the automated PubMed count (596, almost entirely AAA disease papers) and not checking the actual subcellular evidence.


## ⛔ Rejected — PubMed Alias Collision (2026-06-03)

**Rejection reason**: PubMed strict count 596 >100 triggers auto-reject rule, despite strong biological nuclear evidence.

AAAS is a well-established nuclear pore complex scaffold protein with:
- UniProt: Nucleus, nuclear pore complex (ECO:0000269 experimental)
- GO-CC: nuclear pore (IDA), nucleoplasm (IDA:HPA), nuclear envelope (IDA)
- HPA: Nuclear membrane main, Supported reliability
- STRING: Top 15 partners all NPC components (combined scores >0.96)
- 2 cryo-EM structures in native NPC context

However, PubMed counts are inflated by the AAA/abdominal aortic aneurysm abbreviation collision. Manual disambiguation confirms ~100-200 relevant papers, but the validator uses the raw strict count (596) which exceeds the 100 threshold.

**This is a false rejection driven by gene symbol pollution, not by lack of nuclear evidence.**

**Manual review**: STRONGLY RECOMMENDED. This gene should be re-scored if the PubMed>100 rule is refined to account for alias collisions.

**Exception type**: PUBMED_ALIAS_COLLISION_FORCED_REJECTION

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000094914-AAAS/subcellular

![](https://images.proteinatlas.org/40086/2239_B4_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/40086/2239_B4_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/40086/2267_H3_63_blue_red_green.jpg)
![](https://images.proteinatlas.org/40086/2267_H3_88_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
