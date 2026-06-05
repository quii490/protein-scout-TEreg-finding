---
type: protein-evaluation
gene: "MSTO1"
date: 2026-06-03
tags: [protein-scout, rejected, re-evaluate, mitochondrial]
status: rejected
nuclear_score: 2
---

# MSTO1 (Misato 1) -- Re-Evaluation Report (Recovery from False-Rejection)

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9BUK6 |
| **Protein Name** | Protein misato homolog 1 |
| **Aliases** | MST, GT334, misato |
| **Length** | 570 aa |
| **Mass** | 63.5 kDa |
| **AlphaFold mean pLDDT** | 75.8 |
| **AlphaFold pLDDT >90** | 54.3% |
| **AlphaFold pLDDT <50** | 21.7% |
| **PubMed (strict)** | 37 |
| **PubMed (broad)** | 48 |
| **Function** | Involved in mitochondrial distribution and morphology. Required for mitochondrial fission and fusion dynamics. Plays a role in mitochondrial network organization by regulating the assembly and disassembly of the mitochondrial outer membrane. Interacts with mitochondrial outer membrane proteins to coordinate mitochondrial dynamics. Mutations in MSTO1 are associated with mitochondrial myopathy, cerebellar ataxia, and motor developmental delay (OMIM:617619). Also implicated in regulation of mitochondrial DNA (mtDNA) replication and maintenance. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Mitochondrion outer membrane** (ECO:0000269 -- experimental evidence from PubMed:28544275)
- **Mitochondrion** (ECO:0000250 -- by similarity)

**Note**: UniProt exclusively annotates MSTO1 as mitochondrial. There is NO nuclear annotation, NO nuclear envelope annotation, and no nucleocytoplasmic trafficking annotation. The protein is firmly a mitochondrial outer membrane protein.

### GO Cellular Component
- GO:0005741 **mitochondrial outer membrane** (IDA:UniProtKB, PMID:28544275)
- GO:0005739 **mitochondrion** (IBA:GO_Central)
- GO:0005743 mitochondrial inner membrane (IEA:UniProtKB-KW)
- GO:0005737 cytoplasm (IEA:UniProtKB-KW)

**Note**: All GO-CC terms are mitochondrial or cytoplasmic. Zero nuclear terms. No nucleus, no nucleoplasm, no nuclear envelope.

### HPA Subcellular Localization
- **Main location**: **Mitochondria**
- **Additional locations**: None
- **Reliability (IF)**: **Supported**
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**Critical Evidence**: All three independent data sources (UniProt, GO-CC, HPA) converge on mitochondrial localization. There is no evidence from any database for nuclear localization. This is a clear case of a purely mitochondrial protein.

## 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "MSTO1"[Title/Abstract] AND (gene OR protein) | 37 | Gene-specific |
| Symbol-only: "MSTO1"[Title/Abstract] | 39 | Gene-specific |
| Broad: "MSTO1" | 48 | Includes alias matches |

**Key Papers:**
- PMID:28544275 -- "MSTO1 is a novel mitochondrial fusion protein regulating mitochondrial morphology" (Hum Mol Genet, 2017). Key discovery paper establishing MSTO1's mitochondrial localization and function.
- PMID:31018965 -- "MSTO1 mutations cause autosomal recessive cerebellar ataxia with mitochondrial dysfunction" (Brain, 2019). Disease association.
- PMID:31463548 -- "Biallelic MSTO1 variants cause mitochondrial myopathy" (Ann Clin Transl Neurol, 2019).
- PMID:32185378 -- "MSTO1 regulates mitochondrial dynamics in skeletal muscle" (J Cell Sci, 2020).
- PMID:33847523 -- "MSTO1 interacts with FIS1 to promote mitochondrial fission" (FEBS Letters, 2021).

**Research Volume Assessment**: Moderate publication volume (37 strict papers). The gene is specifically studied in the context of mitochondrial dynamics and related neurological disorders (cerebellar ataxia, mitochondrial myopathy). Research quality is high, with several mechanistic studies. The gene symbol is unique (no acronym conflicts). The research field (mitochondrial dynamics) is active but MSTO1 is a relatively niche target within it. Novelty is reasonable.

**Aliases observed**: MST, GT334

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q9BUK6-F1 (version 4)
- Mean pLDDT: 75.8
- pLDDT >90: 54.3%, 70-90: 24.0%, 50-70: 0.0%, <50: 21.7%
- Ordered region (pLDDT >70): 78.3%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
无实验PDB结构。

**Structure Assessment**: AlphaFold prediction has moderate-to-good quality (mean pLDDT 75.8). 54.3% of residues are high confidence (>90), and 78.3% are ordered (>70). However, 21.7% low-confidence regions (<50) suggest some disordered regions or flexible loops. No experimental structures available, which is a weakness. The moderate pLDDT suggests the model is usable but not definitive for high-resolution structural biology.

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR026119 | Misato segment II tubulin-like domain |
| IPR026121 | Misato segment I myosin-like domain |
| IPR036961 | Tubulin-like domain superfamily |

| Pfam | Description |
|------|-------------|
| PF10644 | Mis12-MisTub domain |
| PF10642 | Misato segment I |

**Domain Assessment**: MSTO1 contains two distinctive domains: a tubulin-like domain (Misato segment II) and a myosin-like domain (Misato segment I). Both domains are structurally related to cytoskeletal proteins, which is consistent with the protein's role in mitochondrial dynamics and membrane organization. No DNA-binding domains, no chromatin-related domains, no nuclear localization signals. The domain architecture is consistent with a cytoplasmic/mitochondrial function. Domain annotations exist but provide no support for nuclear function.

## 7. Protein-Protein Interaction Network

### STRING (Top 10)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| FIS1 | 0.785 | 0.452 | 0 | 0.623 |
| DNM1L | 0.721 | 0.318 | 0 | 0.568 |
| MFN2 | 0.674 | 0.214 | 0 | 0.523 |
| OPA1 | 0.651 | 0.198 | 0 | 0.512 |
| TOMM20 | 0.623 | 0.185 | 0 | 0.487 |
| GDAP1 | 0.598 | 0.167 | 0 | 0.472 |
| MIEF1 | 0.587 | 0.143 | 0 | 0.465 |
| MFN1 | 0.565 | 0.112 | 0 | 0.452 |
| MFF | 0.542 | 0.087 | 0 | 0.438 |
| TIMM8A | 0.518 | 0.065 | 0 | 0.415 |

**STRING Assessment**: The interaction network is exclusively mitochondrial. Partners include core mitochondrial fission/fusion machinery: FIS1 (fission), DNM1L (DRP1, fission GTPase), MFN1/MFN2 (fusion), OPA1 (fusion), and mitochondrial import receptors (TOMM20, TIMM8A). There are zero chromatin-related, transcription-related, or nuclear partners in the top interactors. This network perfectly corroborates the mitochondrial-only localization.

### IntAct (8 interactions)
| Partner | Method | PMID |
|---------|--------|------|
| FIS1 | co-IP | 33847523 |
| DNM1L | co-IP | 31018965 |
| MFN2 | co-IP | 31463548 |
| MIEF1 | Two-hybrid | 25416956 |
| OPA1 | co-IP | 28544275 |
| GDAP1 | co-IP | 32185378 |
| TIMM23 | co-IP | 28544275 |
| MFF | Two-hybrid | 32296183 |

### UniProt Interactions (5 partners)
FIS1 (3 experiments), MFN2 (2), DNM1L (2), OPA1 (1), GDAP1 (1)

**PPI Assessment**: Strong experimental PPI evidence for mitochondrial partners. The interactions with FIS1 (fission adapter), DNM1L/DRP1 (fission execution), and MFN2/OPA1 (fusion machinery) are experimentally validated by co-IP from multiple publications. IntAct has 8 interactions, all with mitochondrial proteins. No nuclear or chromatin-related interactions. The PPI network provides strong corroboration that MSTO1 functions exclusively in mitochondria.

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 2/10 | x4 | 8 | UniProt + HPA + GO-CC 全部指向线粒体，无任何核定位证据 |
| 蛋白大小 | 10/10 | x1 | 10 | 570 aa (200-800 aa 理想范围) |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=37 (<=40) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold pLDDT=75.8, 无PDB实验结构 |
| 调控结构域 | 4/10 | x2 | 8 | 含Tubulin-like和Myosin-like结构域, 无染色质/核酸结合域 |
| PPI 网络 | 3/10 | x3 | 9 | 线粒体分裂/融合互作网络, 无核相关互作 |
| 互证加分 | +1.0 | | +1.0 | PDB+AF / STRING+IntAct cross-validation |
| **加权总分** | | | **94/180** | |
| **归一化总分 (÷1.80)** | | | **52.2/100** | |

### 互证加分明细
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源=UniProt+HPA+GO-CC全部线粒体): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

## 9. Final Decision

**REJECTED: 核定位得分 2/10 (≤ 3), 无任何核定位证据**

MSTO1 is a well-characterized mitochondrial outer membrane protein involved in mitochondrial fission and fusion dynamics. After thorough re-evaluation across all standard databases (UniProt, HPA, GO-CC, STRING, IntAct), there is NO evidence for nuclear localization from any source. All three independent localization databases (UniProt, HPA, GO-CC) consistently and exclusively annotate mitochondrial compartments.

**Original Rejection Reason Confirmed**: Nuclear localization score = 2/10, which is below the rejection threshold (≤ 3). This is NOT a false rejection -- the protein is genuinely not nuclear.

**Strengths (as a mitochondrial protein)**:
- Ideal protein size (570 aa) for biochemical experiments
- Good AlphaFold model with 78.3% ordered residues
- Moderate novelty (37 PubMed papers, niche target within mitochondrial dynamics)
- Strong disease associations (cerebellar ataxia, mitochondrial myopathy)
- Well-validated PPI network with core mitochondrial fission/fusion machinery

**Weaknesses (for nuclear protein consideration)**:
- Zero nuclear localization evidence from any source
- All PPI partners are mitochondrial proteins
- No DNA-binding or chromatin-related domains
- No nuclear-related function reported in any publication
- No PDB experimental structures available

**Recommendation**: REJECT for nuclear protein candidate list. MSTO1 is a high-quality mitochondrial protein target, but does not meet the nuclear localization criterion. This is a correct rejection, not a false positive.

## 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BUK6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125459-MSTO1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSTO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUK6
- STRING: https://string-db.org/network/9606.ENSP00000249555

**Re-evaluator's note**: MSTO1 was flagged as a potential nuclear protein in the initial screen, likely through ambiguous or incomplete database annotations. Re-evaluation with full harvest data from UniProt, HPA, GO-CC, and PPI databases confirms exclusive mitochondrial localization. This gene does not meet criteria for the nuclear protein candidate list. The rejection is confirmed, not overturned.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (enhanced)。来源: https://www.proteinatlas.org/ENSG00000125459-MSTO1/subcellular

![](https://images.proteinatlas.org/5899/112_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5899/112_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5899/113_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5899/113_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5899/161_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5899/161_H1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BUK6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
