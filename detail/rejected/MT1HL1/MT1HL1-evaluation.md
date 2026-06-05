---
type: protein-evaluation
gene: "MT1HL1"
date: 2026-06-03
tags: [protein-scout, rejected, re-evaluate, pseudogene, metallothionein]
status: rejected
nuclear_score: 0
---

# MT1HL1 (Metallothionein 1H Like 1) -- Re-Evaluation Report (Confirmed Rejection)

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | P0DM35 (UniProtKB/Swiss-Prot, evidence at protein level) |
| **Protein Name** | Putative metallothionein MT1HL1 |
| **Aliases** | None |
| **Length** | 61 aa |
| **Mass** | 6.1 kDa |
| **AlphaFold mean pLDDT** | 84.2 |
| **AlphaFold pLDDT >90** | 68.7% |
| **AlphaFold pLDDT <50** | 18.5% |
| **PubMed (strict)** | 3 |
| **PubMed (broad)** | 5 |
| **Function** | MT1HL1 is a putative metallothionein-like protein with predicted metal-binding capacity based on cysteine content. The gene is annotated as a protein-coding gene by HGNC (HGNC:31968) but its expression status, functional protein production, and biological role remain largely uncharacterized. No direct functional studies exist. The protein is predicted to bind zinc, copper, and other heavy metals through cysteine thiolate coordination, following the canonical metallothionein architecture. However, evidence at the protein level is described as "evidence at protein level" in UniProt (ECO:0000256, match to InterPro signature), which is a computational prediction rather than direct experimental protein identification. |

## 2. 核定位证据

### UniProt Subcellular Location
- **No subcellular location annotated**

**Note**: UniProt does NOT provide any subcellular location annotation for MT1HL1. This is a critical absence. Even by similarity, UniProt has not assigned a location.

### GO Cellular Component
- GO:0005737 **cytoplasm** (IEA:UniProtKB-KW)
- GO:0005634 **nucleus** (IEA:UniProtKB-KW)

**Note**: GO-CC annotations are purely electronic (IEA, weakest tier). Both cytoplasm and nucleus are computationally predicted. No direct experimental evidence exists for any subcellular localization.

### HPA Subcellular Localization
- **Data NOT AVAILABLE**: MT1HL1 is not included in the Human Protein Atlas database. No IF images, no subcellular classification, no tissue expression data.

**HPA Nuclear Localization Summary**: Complete absence of HPA data. MT1HL1 has not been profiled by the Human Protein Atlas. This is a major data gap.

**Evidence Synthesis**: There is essentially NO reliable subcellular localization evidence for MT1HL1. UniProt provides no annotation. GO-CC provides only electronic predictions (IEA), which are computational and lack experimental validation. HPA does not cover this gene. Nuclear score = 0/10 -- no nuclear evidence from any source.

## 3. HPA Immunofluorescence

HPA IF 数据不存在。MT1HL1 未收录于 Human Protein Atlas 数据库。无法获取免疫荧光图像。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "MT1HL1"[Title/Abstract] AND (gene OR protein) | 3 | Essentially no dedicated literature |
| Symbol-only: "MT1HL1"[Title/Abstract] | 3 | All gene-specific but minimal |
| Broad: "MT1HL1" | 5 | Includes genome annotation papers |

**Key Papers:**
- No dedicated functional studies exist for MT1HL1. The 3 papers mentioning MT1HL1 are genome annotation studies or large-scale transcriptomic surveys where MT1HL1 appears in gene lists without functional characterization.
- PMID:25348722 -- Appears in a genome-wide survey of metallothionein gene family in primates (BMC Genomics, 2014). Annotation-level mention only.
- PMID:29875321 -- Mentioned in a comparative genomics study of metallothionein evolution (Mol Biol Evol, 2018).

**Research Volume Assessment**: MT1HL1 has negligible dedicated literature. The gene exists primarily as a genomic annotation. No functional studies, no expression validation, no disease association studies. While this would ordinarily signal extreme novelty, the absence of basic functional characterization (including subcellular localization) makes it unviable as a research target.

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-P0DM35-F1 (version 4)
- Mean pLDDT: 84.2
- pLDDT >90: 68.7%, 70-90: 12.8%, 50-70: 0.0%, <50: 18.5%
- Ordered region (pLDDT >70): 81.5%
- PAE: Available

### Experimental PDB Structures
None. No experimental structures exist for MT1HL1.

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR000006 | Metallothionein, vertebrate |
| IPR018064 | Metallothionein, vertebrate, metal binding site |
| IPR003019 | Metallothionein superfamily |

| Pfam | Description |
|------|-------------|
| PF00131 | Metallothionein |

**Domain Assessment**: MT1HL1 is annotated as containing a metallothionein domain based on sequence similarity (InterPro match). The cysteine pattern is consistent with the MT family. However, domain annotation is computational and does not confirm functional protein production.

## 7. Protein-Protein Interaction Network

### STRING
No STRING data available. MT1HL1 has insufficient experimental evidence to support a STRING interaction network.

### IntAct
No IntAct interactions. The protein has never been studied in any interaction assay.

**PPI Assessment**: Complete absence of PPI data. This is expected for a gene with uncertain protein-level expression.

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 0/10 | x4 | 0 | 无UniProt定位, 无HPA数据, GO-CC仅IEA |
| 蛋白大小 | 5/10 | x1 | 5 | 61 aa (预测), 偏小 |
| 研究新颖性 | 0/10 | x5 | 0 | 极端新颖但无功能验证基础 |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=84.2, 无实验结构 |
| 调控结构域 | 4/10 | x2 | 8 | Metallothionein结构域(预测) |
| PPI 网络 | 0/10 | x3 | 0 | 无STRING, 无IntAct, 无任何PPI数据 |
| 互证加分 | +0 | | +0 | 无可靠实验数据可用于互证 |
| **加权总分** | | | **34/180** | |
| **归一化总分 (÷1.80)** | | | **18.9/100** | |

### 互证加分明细
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

## 9. Final Decision

**REJECTED: Multiple critical data deficiencies -- no nuclear localization evidence, no experimental protein characterization, no PPI data, no HPA coverage**

MT1HL1 is NOT a viable research target at this time. The gene suffers from a near-total absence of experimental characterization. While this extreme data sparsity might be interpreted as extreme novelty, it actually reflects a gene for which basic biological validation is absent. Key deficiencies include:

1. **No subcellular localization evidence** from any source (UniProt, HPA, or GO experimental evidence)
2. **No HPA coverage** (gene not included in the Human Protein Atlas)
3. **No PPI data** (zero STRING or IntAct interactions)
4. **Protein-level evidence is computational only** (UniProt ECO:0000256, InterPro match)
5. **No functional studies** exist (3 PubMed mentions, all genome annotation)
6. **Uncertain expression status** -- it is unclear whether MT1HL1 produces a stable protein in any human tissue

**Original Rejection Reason**: The gene is insufficiently characterized to serve as a tractable research target. While the metallothionein family is well-studied, MT1HL1 itself is essentially uncharacterized. The risk of investing in a gene that may not produce a functional protein or may lack detectable expression is too high.

**Recommendation**: DO NOT RE-EVALUATE unless new experimental evidence becomes available. Specifically, wait for: (1) HPA inclusion with IF data, (2) proteomics evidence confirming protein expression in human tissues, or (3) a dedicated functional study. Prior to these milestones, MT1HL1 should remain rejected.

## 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P0DM35
- Protein Atlas: NOT COVERED
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MT1HL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0DM35
- STRING: No data available

**Re-evaluator's note**: MT1HL1 was likely included in the batch due to its metallothionein family membership and UniProt annotation as "evidence at protein level." However, this UniProt evidence code (ECO:0000256) is computational (InterPro signature match), not experimental protein identification. The gene is essentially a genomic prediction without experimental validation. Rejection is the correct outcome -- this is not a false rejection but rather a prudent exclusion of an uncharacterized gene. If MT1HL1 is confirmed as a functional protein in future studies, a re-evaluation would be warranted, but for now, the risk of non-expression is too high for an experimental target.

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0DM35-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
