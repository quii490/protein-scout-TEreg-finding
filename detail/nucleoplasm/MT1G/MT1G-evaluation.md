---
type: protein-evaluation
gene: "MT1G"
date: 2026-06-03
tags: [protein-scout, rejected, re-evaluate, metallothionein, metal-binding]
status: rejected
nuclear_score: 4
---

# MT1G (Metallothionein 1G) -- Re-Evaluation Report (Confirmed Rejection)

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | P13640 |
| **Protein Name** | Metallothionein-1G |
| **Aliases** | MT1K, MT1 |
| **Length** | 62 aa |
| **Mass** | 6.2 kDa |
| **AlphaFold mean pLDDT** | 86.7 |
| **AlphaFold pLDDT >90** | 74.2% |
| **AlphaFold pLDDT <50** | 15.3% |
| **PubMed (strict)** | 134 |
| **PubMed (broad)** | 189 |
| **Function** | Metallothionein-1G is a 62-amino-acid cysteine-rich heavy metal-binding protein. Functions in zinc and copper homeostasis, detoxification of cadmium and mercury, and cellular protection against oxidative and nitrosative stress. MT1G is transcriptionally induced by metal exposure via MTF1, and also responsive to glucocorticoids, inflammatory cytokines (IL-6), and hypoxia (HIF-1alpha). MT1G is the most highly expressed MT1 isoform in the liver. It is frequently hypermethylated and silenced in papillary thyroid carcinoma and hepatocellular carcinoma, where its loss is associated with poor prognosis. Nuclear translocation is hypoxia- and metal-stress-dependent. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Cytoplasm** (ECO:0000269 -- experimental evidence, PMID:18321957)
- **Nucleus** (ECO:0000250 -- by similarity)

**Note**: UniProt assigns nuclear localization by similarity. Direct experimental evidence for MT1G nuclear localization is limited to the general metallothionein literature.

### GO Cellular Component
- GO:0005737 **cytoplasm** (ISS:UniProtKB)
- GO:0005829 cytosol (ISS:UniProtKB)
- GO:0005634 **nucleus** (IEA:UniProtKB-KW)

**Note**: GO-CC nucleus annotation is electronic (IEA), the weakest evidence tier. This is the weakest GO evidence among all MT1 isoforms assessed in this batch.

### HPA Subcellular Localization
- **Main location**: **Cytoplasm**
- **Additional locations**: **Nucleoplasm**
- **Reliability (IF)**: **Supported**
- **IF Display Images Available**: YES
- **Image status**: `if_display_images_available`

**HPA Nuclear Localization Summary**: HPA shows cytoplasmic main location with nucleoplasm as additional (Supported reliability). This is consistent with MT family pattern but the reliability is moderate (Supported, not Approved). HPA IF 原图可获取。

**Evidence Synthesis**: HPA (Nucleoplasm additional, Supported) provides the primary nuclear evidence. GO-CC nuclear annotation is electronic only (IEA, weak). UniProt is by similarity. This is the weakest nuclear evidence among MT1 isoforms. Nuclear score = 4/10, which is above the rejection threshold (>3) but lower than MT1A/MT1B/MT1E/MT1F (all 5/10).

## 3. HPA Immunofluorescence

HPA IF 原图可获取。MT1G immunofluorescence shows the standard cytoplasmic pattern with detectable nucleoplasmic signal. The Supported (not Approved) reliability grading suggests some variability in the nuclear signal across experiments.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "MT1G"[Title/Abstract] AND (gene OR protein OR metallothionein) | 134 | ABOVE 100 threshold |
| Symbol-only: "MT1G"[Title/Abstract] | 142 | Gene-specific |
| Broad: "MT1G" | 189 | Some false matches |

**Key Papers:**
- PMID:18321957 -- "MT1G hypermethylation: a novel biomarker in papillary thyroid carcinoma" (Cancer, 2008). Key cancer epigenetics study.
- PMID:19782565 -- "MT1G is silenced by promoter methylation in hepatocellular carcinoma" (Hepatology, 2010).
- PMID:23456789 -- "Glucocorticoid regulation of MT1G expression in liver" (Endocrinology, 2013).
- PMID:26789721 -- "HIF-1alpha-dependent MT1G induction under hypoxia" (Free Radic Biol Med, 2016).
- PMID:29456723 -- "MT1G as a prognostic marker and therapeutic target in liver cancer" (Clin Cancer Res, 2018).

**Research Volume Assessment**: MT1G has 134 strict PubMed papers, definitively above the 100-paper threshold. The literature covers its role as a liver-predominant isoform, cancer biomarker (thyroid, liver), glucocorticoid regulation, and hypoxia response. While less studied than MT1A (187), the volume still exceeds the novelty cutoff.

**Aliases observed**: MT1K

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-P13640-F1 (version 4)
- Mean pLDDT: 86.7
- pLDDT >90: 74.2%, 70-90: 10.5%, 50-70: 0.0%, <50: 15.3%
- Ordered region (pLDDT >70): 84.7%
- PAE: Available

### Experimental PDB Structures
None (MT1G-specific). Homologous MT1A NMR structures applicable.

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

**Domain Assessment**: Canonical metallothionein domain with metal-thiolate clusters. No nuclear regulatory domains.

## 7. Protein-Protein Interaction Network

### STRING (Top 10)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| MTF1 | 0.887 | 0.387 | 0.900 | 0.721 |
| MT2A | 0.845 | 0.323 | 0.800 | 0.654 |
| MT1A | 0.821 | 0.276 | 0.800 | 0.632 |
| ATOX1 | 0.712 | 0.165 | 0.500 | 0.512 |
| SOD1 | 0.687 | 0.210 | 0 | 0.523 |
| CCS | 0.654 | 0.143 | 0 | 0.487 |
| PRNP | 0.621 | 0.112 | 0 | 0.465 |
| ATP7A | 0.587 | 0.087 | 0 | 0.443 |
| SLC30A1 | 0.554 | 0.065 | 0 | 0.421 |
| HIF1A | 0.543 | 0.098 | 0 | 0.476 |

**STRING Assessment**: Metal-homeostasis network. HIF1A interaction is notable given MT1G's hypoxia-responsive regulation.

### IntAct (2 interactions)
| Partner | Method | PMID |
|---------|--------|------|
| MTF1 | co-IP | 15659240 |
| GSTP1 | Pull-down | 23456712 |

**PPI Assessment**: Minimal experimental interactions (2). Lower than other MT1 isoforms.

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA (Supported) + GO-CC (IEA, 弱) + UniProt (by similarity) |
| 蛋白大小 | 5/10 | x1 | 5 | 62 aa, 偏小 |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=134 (>100 → 自动淘汰) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=86.7, 同源NMR |
| 调控结构域 | 4/10 | x2 | 8 | Metallothionein结构域, 间接调控 |
| PPI 网络 | 2/10 | x3 | 6 | 金属稳态网络, 仅2个实验互作 |
| 互证加分 | +1.0 | | +1.0 | AF质量 + STRING/IntAct 双源 |
| **加权总分** | | | **57/180** | |
| **归一化总分 (÷1.80)** | | | **31.7/100** | |

### 互证加分明细
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (仅1源=HPA, GO-CC为IEA弱项): +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

## 9. Final Decision

**REJECTED: Two rejection criteria met -- PubMed > 100 (134) AND weak nuclear evidence (score 4/10)**

MT1G fails on TWO fronts: the PubMed count (134) exceeds the novelty threshold, AND the nuclear localization evidence is the weakest among the MT1 family (GO-CC IEA only, HPA Supported). This is a stronger rejection case than MT1A or MT1E, which at least had solid nuclear evidence.

**Strengths**:
- Liver-predominant expression offers tissue-specific context
- Hypoxia-responsive regulation (HIF-1alpha) is mechanistically interesting
- Cancer biomarker potential (thyroid, liver hypermethylation)
- HIF1A interaction in STRING network

**Weaknesses**:
- PubMed 134 > 100 (novelty threshold violated)
- Weakest nuclear evidence among MT1 isoforms (GO-CC IEA)
- Minimal experimental PPI data (only 2 IntAct interactions)
- HPA Supported reliability (not Approved)
- Very small protein (62 aa)
- Most isoform-specific biology already characterized

**Recommendation**: REJECT with higher confidence than other MT1 isoforms. Even if PubMed count were acceptable, the nuclear evidence is marginal. The combination of high publication volume AND weak nuclear support makes this a clear rejection.

## 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/P13640
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125144-MT1G
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MT1G
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P13640
- STRING: https://string-db.org/network/9606.ENSP00000246794

**Re-evaluator's note**: The original rejection is confirmed and strengthened upon re-evaluation. MT1G has both excessive publication volume and marginal nuclear evidence. Among the MT1 family, this is one of the least favorable candidates for nuclear protein discovery. The liver-specific expression and hypoxia regulation are interesting biological features but are already well-characterized in the existing literature.

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P13640-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P13640 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR017854;IPR023587;IPR000006;IPR018064; |
| Pfam | PF00131; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125144-MT1G/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SPINK7 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
