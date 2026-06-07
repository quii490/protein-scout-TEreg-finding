---
type: protein-evaluation
gene: ACBD4
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleoplasm
  - acyl-coa-binding
  - peroxisome
  - lipid-metabolism
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ACBD4 (Acyl-CoA-binding domain-containing protein 4) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q8NC06 |
| **Protein Name** | Acyl-CoA-binding domain-containing protein 4 |
| **Aliases** | (none) |
| **Length** | 268 aa |
| **Mass** | 30.3 kDa |
| **AlphaFold mean pLDDT** | 64.4 |
| **AlphaFold pLDDT >90** | 23.1% |
| **AlphaFold pLDDT <50** | 38.4% |
| **PubMed (strict)** | 15 |
| **PubMed (broad)** | 15 |
| **Function** | Binds medium- and long-chain acyl-CoA esters and may function as an intracellular carrier of acyl-CoA esters. Key role in peroxisome-ER contact sites and lipid metabolism. |

## 2. 核定位证据

### UniProt Subcellular Location
**No subcellular location annotation.** UniProt has not annotated ACBD4's subcellular localization.

### GO Cellular Component
- GO:0005737 **cytoplasm** (IBA:GO_Central)

**Note**: Only one GO-CC term, and it is cytoplasmic. The annotation is inferred from biological aspect of ancestor (IBA), not direct experimental evidence.

### HPA Subcellular Localization
- **Main location**: **Nucleoplasm**, Vesicles (dual main)
- **Additional locations**: (none)
- **Reliability (IF)**: **Approved** (highest tier)
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

**HPA Nuclear Localization Summary**: HPA classifies ACBD4 with dual main localization at Nucleoplasm and Vesicles, with "Approved" reliability -- the highest HPA confidence tier. No IF display images are available despite the Approved classification. The nucleoplasmic classification is surprising for a protein whose known function is in peroxisome-ER contact sites and acyl-CoA binding.

**Evidence Conflict**: The HPA Nucleoplasm classification (Approved) is in direct tension with the known peroxisomal/ER function of ACBD4. The literature (PMID:37414147, PMID:36952197) establishes ACBD4 as a peroxisome-ER contact site protein. A nucleoplasmic pool is unexpected and could represent either (a) a genuine dual localization, (b) an HPA IF artifact, or (c) detection of nascent protein in the nucleus before trafficking to peroxisomes/ER.

## 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ACBD4"[Title/Abstract] AND (gene OR protein OR hydrolase) | 15 | All gene-specific |
| Symbol-only: "ACBD4"[Title/Abstract] | 15 | All gene-specific |
| Broad: "ACBD4" | 15 | All gene-specific |

**Key Papers:**
- PMID:37414147 -- "Differential roles for ACBD4 and ACBD5 in peroxisome-ER interactions and lipid metabolism" (J Biol Chem, 2023). The key functional paper. Establishes ACBD4 role at peroxisome-ER contact sites.
- PMID:36952197 -- "Assessing Peroxisomal Protein Interaction by Immunoprecipitation" (Methods Mol Biol, 2023). Methodological paper featuring ACBD4.
- PMID:39394562 -- "Genetic architectures of the human hippocampus and those involved in neuropsychiatric traits" (BMC Medicine, 2024). GWAS -- ACBD4 appears as a locus.
- PMID:40570459 -- "Multi-omics analysis provides new insights into molecular mechanisms for waterfowl fatty liver formation" (Poultry Science, 2025).
- PMID:40873809 -- "Acyl-coA binding protein AcbdA regulates peroxisome hitchhiking on early endosomes" (bioRxiv, 2025).

**Research Volume Assessment**: Moderate but focused literature (15 papers). Research centers on peroxisome biology and lipid metabolism. The JBC paper (PMID:37414147) is the definitive functional characterization. No paper specifically addresses nuclear localization or nuclear function. Gene symbol is unique.

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-Q8NC06-F1 (version 6)
- Mean pLDDT: 64.4 (LOW confidence)
- pLDDT >90: 23.1%, 70-90: 23.9%, <50: 38.4%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
| PDB ID | Method | Resolution | Coverage |
|--------|--------|------------|----------|
| 2WH5 | X-ray | 2.60 A | 7-110 (ACB domain, chains A-F) |

**Structure Assessment**: One X-ray crystal structure at good resolution (2.60A) covering the N-terminal acyl-CoA-binding (ACB) domain (residues 7-110). This represents approximately 40% of the protein. The C-terminal half (residues 111-268) has no experimental structure. The AlphaFold model has low confidence (mean pLDDT 64.4, 38.4% <50), suggesting the C-terminal region may be largely disordered. The ACB domain is well-characterized structurally -- it forms a four-helix bundle that binds acyl-CoA.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR022408 | Acyl-CoA-binding protein, conserved site |
| IPR000582 | Acyl-CoA-binding protein (ACBP) |
| IPR035984 | Acyl-CoA-binding protein superfamily |
| IPR014352 | FERM/acyl-CoA-binding protein superfamily |

| Pfam | Description |
|------|-------------|
| PF00887 | Acyl-CoA-binding protein (ACBP) |

**Domain Assessment**: ACBD4 contains a single characterized domain: the acyl-CoA-binding protein (ACBP) domain. This is a well-studied lipid-binding domain found in proteins involved in fatty acid metabolism, intracellular lipid transport, and membrane contact site formation. The domain binds medium- and long-chain acyl-CoA esters with high affinity. No DNA-binding domains, no nuclear localization signals, no transcriptional regulatory domains. The domain architecture provides no obvious mechanistic rationale for nuclear localization.

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| VAPB | 0.980 | 0.545 | 0 | 0.958 |
| VAPA | 0.908 | 0.329 | 0 | 0.869 |
| GCDH | 0.574 | 0 | 0.165 | 0.304 |
| ACOX1 | 0.542 | 0 | 0.165 | 0.281 |
| ACAA1 | 0.531 | 0 | 0.185 | 0.178 |
| ACAA2 | 0.506 | 0 | 0.185 | 0.152 |
| ACOX3 | 0.495 | 0 | 0.165 | 0.201 |
| ACADS | 0.492 | 0 | 0.165 | 0.163 |
| ACOX2 | 0.490 | 0 | 0.165 | 0.201 |
| ACADVL | 0.488 | 0 | 0.165 | 0.191 |
| ACADM | 0.476 | 0 | 0.165 | 0.178 |
| HADHB | 0.474 | 0 | 0.185 | 0.097 |
| ACADL | 0.468 | 0 | 0.165 | 0.166 |
| DCAKD | 0.466 | 0 | 0 | 0.448 |
| ACAT2 | 0.464 | 0 | 0.185 | 0.081 |

### IntAct (15 interactions)
| Partner | Method | PMID | Significance |
|---------|--------|------|-------------|
| TEKT4 | Two-hybrid array | 32296183 | - |
| VAPB | co-IP | 28514442 | **ER contact site protein** |
| VAPA | co-IP | 26496610 | **ER contact site protein** |
| KIF9 | Validated two-hybrid | 26871637 | Kinesin motor |
| CRX | Validated two-hybrid | 26871637 | Transcription factor |
| REL | Validated two-hybrid | 26871637 | Transcription factor |
| MEOX2 | Validated two-hybrid | 26871637 | Transcription factor |
| MEOX1 | Two-hybrid | 26871637 | Transcription factor |
| TRIM63 | Two-hybrid | 31391242 | E3 ubiquitin ligase |
| TRIM55 | Two-hybrid | 31391242 | E3 ubiquitin ligase |
| SPRED1 | Two-hybrid array | 32814053 | Signaling |
| GIPC1 | Two-hybrid array | 32814053 | Signaling |
| KLK6 | Two-hybrid array | 32814053 | Protease |
| FGFR3 | Two-hybrid array | 32814053 | Receptor kinase |
| GSN | Two-hybrid array | 32814053 | Actin-binding |

### UniProt Interactions (9 entries, isoform-specific)
ATN1, CRYAA, DMWD, FGFR3, GIPC1, GSN, KLK6, SPRED1, TEKT4 (all 3 experiments each, via Q8NC06-3 isoform)

**PPI Assessment**: The PPI network reveals a dichotomy. The strongest experimental interactions (VAPB co-IP, VAPA co-IP) are with ER membrane contact site proteins -- consistent with the peroxisome-ER function. However, several validated two-hybrid interactions with transcription factors (CRX, REL, MEOX2, MEOX1, all PMID:26871637) are noteworthy. These transcription factor interactions could suggest a nuclear connection, possibly involving transcriptional regulation of lipid metabolism genes. However, all are from two-hybrid screens and none have been validated by co-IP.

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

ACBD4 exemplifies the tension between HPA data and known protein function. The HPA Approved nucleoplasmic classification is the highest-confidence tier, but the protein's well-characterized function is in peroxisome-ER contact sites and lipid metabolism -- not nuclear processes. The PPI network (VAPB/VAPA interactions) confirms the ER/peroxisomal role.

**Strengths**:
- HPA Approved nucleoplasmic localization (highest confidence tier)
- Well-characterized functional domain (ACBP, X-ray structure at 2.60A)
- Moderate PubMed literature (15 papers) with clear functional characterization
- VAPB/VAPA interactions are experimentally validated (co-IP)
- Transcription factor interactions (CRX, REL, MEOX1/2) provide a possible nuclear connection

**Weaknesses**:
- Known biological function is peroxisomal/ER, not nuclear
- No corroborating nuclear evidence from UniProt or GO-CC
- Single ACBP domain with no nuclear function rationale; no NLS
- Low AlphaFold confidence (38.4% disordered)
- No HPA IF display images available for independent verification
- TF interactions are from two-hybrid screens only (no validation)

**Recommendation**: Retain as a low-priority candidate, but with the strong caveat that the nuclear localization may not reflect the primary biological function. ACBD4 could represent a protein with a minor nuclear pool or a moonlighting function, but the existing literature does not support a nuclear role. If the project focuses on proteins with well-established nuclear functions, ACBD4 should be deprioritized. If the project aims to discover unexpected nuclear proteins, the Approved HPA classification and TF interactions warrant investigation.

## 10. Manual Review Note

The HPA Approved reliability carries significant weight, but the biological context strongly argues against a primary nuclear function. ACBD4 is a peroxisome-ER contact site protein with a well-characterized lipid-binding domain. The nucleoplasmic annotation may reflect detection of the acyl-CoA binding domain in the nucleus (possibly binding nuclear acyl-CoA pools) or could be an HPA artifact despite the Approved classification.

**Re-evaluator's note**: This is a case where HPA evidence for nuclear localization is formally strong (Approved tier) but conflicts with biological knowledge. The protein is not described as nuclear in any functional study. The decision to retain or reject depends on the project's tolerance for unexpected localizations. For a conservative nuclear protein screen, rejection would be defensible. For a discovery-oriented screen, this protein is worth keeping for the unexpected HPA finding and the potential lipid-nucleus connection. Manual review of HPA IF raw data is essential before any downstream investment.

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000181513-ACBD4/subcellular

![](https://images.proteinatlas.org/51772/1101_D2_5_red_green.jpg)
![](https://images.proteinatlas.org/51772/1101_D2_6_red_green.jpg)
![](https://images.proteinatlas.org/51772/1128_A9_4_red_green.jpg)
![](https://images.proteinatlas.org/51772/1128_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/51772/1276_D6_4_red_green.jpg)
![](https://images.proteinatlas.org/51772/1276_D6_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NC06 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 12..101; /note="ACB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00573" |
| InterPro | IPR022408;IPR000582;IPR035984;IPR014352; |
| Pfam | PF00887; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181513-ACBD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| VAPA | Biogrid, Opencell | true |
| VAPB | Biogrid, Opencell | true |
| LPCAT1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
