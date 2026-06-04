---
type: protein-evaluation
gene: "MT1L"
date: 2026-06-03
tags: [protein-scout, rejected, re-evaluate, pseudogene, metallothionein]
status: rejected
nuclear_score: 0
---

# MT1L (Metallothionein 1L, Pseudogene) -- Re-Evaluation Report (Confirmed Rejection)

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Not applicable (pseudogene, no functional protein) |
| **Protein Name** | Metallothionein 1L (pseudogene) |
| **Aliases** | MT1L |
| **Length** | Not applicable |
| **Mass** | Not applicable |
| **AlphaFold** | Not applicable (no functional protein sequence) |
| **PubMed (strict)** | 4 |
| **PubMed (broad)** | 7 |
| **HGNC Status** | **Pseudogene** (HGNC:7410) |

**Critical Note**: MT1L is classified as a pseudogene by HGNC (HUGO Gene Nomenclature Committee). It is NOT a protein-coding gene. A pseudogene is defined as a genomic sequence that resembles a functional gene but has been rendered non-functional through mutations such as premature stop codons, frameshifts, or loss of regulatory elements. MT1L arose from duplication of a functional metallothionein gene but accumulated inactivating mutations.

## 2. 核定位证据

**Not applicable**: As a pseudogene, MT1L does not encode a functional protein. There is no protein product to localize. Nuclear localization assessment is meaningless for a non-coding genomic element.

### UniProt
- No entry exists for a functional MT1L protein. Some databases may list a computationally predicted sequence, but HGNC and the consensus genomic annotation classify MT1L as non-coding.

### GO Cellular Component
- No GO annotations exist for MT1L as a protein-coding gene.

### HPA
- MT1L is not covered by the Human Protein Atlas. No antibody, no IF data, no tissue expression profiling exists.

**Nuclear Score**: 0/10 (no protein product, no localization possible)

## 3. HPA Immunofluorescence

HPA does not cover MT1L. No immunofluorescence data exists or can exist for a pseudogene without a protein product.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "MT1L"[Title/Abstract] AND (gene OR pseudogene) | 4 | All mention MT1L as a pseudogene |
| Symbol-only: "MT1L"[Title/Abstract] | 5 | Pseudogene context |
| Broad: "MT1L" | 7 | Includes gene family studies |

**Key Papers:**
- The few PubMed mentions of MT1L are within the context of metallothionein gene family evolution and genomic organization studies. MT1L is discussed as a pseudogene member of the MT1 cluster on chromosome 16q13, alongside other pseudogenes (MT1J, MT1L) and functional genes (MT1A through MT1H, MT1M, MT1X).
- PMID:14647412 -- "The human metallothionein gene family: structure and expression" (Mol Biol Evol, 2004). Family-wide annotation study.
- PMID:21358720 -- "Evolution of the vertebrate metallothionein gene family" (BMC Evol Biol, 2011).

**Research Volume Assessment**: Negligible. MT1L has no dedicated functional literature because it is a pseudogene. The few mentions are in gene family evolution contexts. The gene is not a viable research target.

## 5. AlphaFold / PAE / PDB

Not applicable. AlphaFold does not provide predictions for pseudogenes as there is no functional protein sequence to model.

## 6. InterPro / Pfam Domains

Not applicable. Domain annotation tools typically do not annotate pseudogenes as functional proteins.

## 7. Protein-Protein Interaction Network

Not applicable. A pseudogene does not produce a protein and therefore cannot have protein-protein interactions.

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 0/10 | x4 | 0 | 假基因, 无蛋白产物 |
| 蛋白大小 | 0/10 | x1 | 0 | 无蛋白产物 |
| 研究新颖性 | 0/10 | x5 | 0 | 假基因, 非研究靶点 |
| 三维结构 | 0/10 | x3 | 0 | 无蛋白模型 |
| 调控结构域 | 0/10 | x2 | 0 | 无功能结构域 |
| PPI 网络 | 0/10 | x3 | 0 | 无蛋白互作 |
| 互证加分 | +0 | | +0 | 全部不适用 |
| **加权总分** | | | **0/180** | |
| **归一化总分** | | | **0/100** | |

## 9. Final Decision

**REJECTED: MT1L is a pseudogene (HGNC:7410) -- not a protein-coding gene**

MT1L should never have been included in the protein target list. This is a pseudogene as classified by HGNC, the authoritative human gene nomenclature body. Pseudogenes are non-functional genomic remnants of gene duplication events and do not produce protein products.

**Original Inclusion Error**: MT1L was likely included in the initial screen due to automated parsing of gene lists or databases that listed it as a metallothionein family member. HGNC classification as pseudogene was not filtered out. This is a data curation issue, not a scoring issue.

**Recommendation**: PERMANENTLY EXCLUDE MT1L from all future protein target evaluations. If MT1L appears in any gene list, it should be automatically removed as a pseudogene. Implement a pre-filtering step that checks HGNC status before batch evaluation to prevent pseudogenes from consuming evaluation resources.

## 10. Data Sources
- HGNC: https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7410
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MT1L
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/4497

**Re-evaluator's note**: This is the clearest rejection in the entire batch. MT1L is unequivocally a pseudogene per HGNC classification. No amount of re-evaluation can recover a gene that does not encode a protein. The original inclusion was a curation error that should be prevented in future by adding an HGNC pseudogene filter to the gene list preprocessing step. The 7 PubMed mentions are all in the context of "MT1L is a pseudogene" -- even the literature agrees. This gene should be permanently excluded from all future protein-scout evaluations.
