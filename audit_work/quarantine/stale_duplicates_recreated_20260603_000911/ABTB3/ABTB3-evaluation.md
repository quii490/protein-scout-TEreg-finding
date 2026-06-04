---
type: protein-evaluation
gene: ABTB3
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleoplasm
  - btb-poz-domain
  - synaptic-protein
  - novel-gene
  - re-evaluate
  - pilot-gene
status: scored
nuclear_score: 6
---

# ABTB3 (Ankyrin repeat and BTB/POZ domain-containing protein 3) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | A6QL63 |
| **Protein Name** | Ankyrin repeat- and BTB/POZ domain-containing protein 3 |
| **Aliases** | BTBD11 |
| **Length** | 1104 aa |
| **Mass** | 120.9 kDa |
| **AlphaFold mean pLDDT** | 71.9 |
| **AlphaFold pLDDT >90** | 32.6% |
| **AlphaFold pLDDT <50** | 25.7% |
| **PubMed (strict)** | 1 |
| **PubMed (broad)** | 2 |
| **Function** | Cortical and hippocampal inhibitory interneuron-specific protein localized at glutamatergic (excitatory) synapses, where it supports cell type-specific synaptic function. Known primarily under the alias BTBD11. |

## 2. 核定位证据

### UniProt Subcellular Location
- **Membrane** (ECO:0000305 -- inferred from experimental data)

**Note**: UniProt annotates ABTB3 as a membrane protein. No nuclear annotation. The membrane annotation likely reflects the synaptic localization.

### GO Cellular Component
- GO:0098978 glutamatergic synapse (IEA:Ensembl)
- GO:0016020 membrane (IEA:UniProtKB-SubCell)

**Note**: Only two GO-CC terms, both pointing to membrane/synaptic localization. No nuclear terms.

### HPA Subcellular Localization
- **Main location**: **Nucleoplasm**
- **Additional locations**: Cytosol
- **Reliability (IF)**: **Supported** (second-highest tier)
- **IF Display Images Available**: NO (`if_image_urls` array is empty)
- **Image status**: `no_image_detected`

**HPA Nuclear Localization Summary**: HPA classifies ABTB3 as primarily nucleoplasmic with additional cytosolic localization. The reliability is "Supported." No IF display images are available. This is the SOLE source of nuclear localization evidence for this protein -- UniProt and GO-CC agree on membrane/synaptic localization.

**Evidence Conflict**: There is a direct contradiction. HPA says Nucleoplasm main + Cytosol. UniProt says Membrane. GO-CC says glutamatergic synapse + membrane. The known function (interneuron-specific synaptic protein) aligns with UniProt/GO, not with HPA. This is a significant discrepancy that warrants caution.

**Note on Excel discrepancy**: The original Sheet4 Excel listed ABTB3 as HPA="Nucleoli|Nucleoplasm" with nuclear_score=6. The actual harvested HPA data shows "Nucleoplasm" main only (no Nucleoli). The "Nucleoli" in the original Excel is not supported by the packet data.

## 3. HPA Immunofluorescence

**HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

The HPA subcellular page shows `no_image_detected` status. No curated IF display images are available, despite the presence of raw red_green images in the image_urls. The lack of curated images combined with the UniProt/HPA conflict makes the nuclear assignment uncertain.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ABTB3"[Title/Abstract] AND (gene OR protein OR hydrolase) | 1 | Single paper under ABTB3 name |
| Symbol-only: "ABTB3"[Title/Abstract] | 1 | Single paper |
| Broad: "ABTB3" | 2 | Two papers total |

**Key Papers (under ABTB3):**
- PMID:40564278 -- "Genome-Wide Association Analysis of Flavor Precursor Traits in Chengkou Mountain Chicken" (Animals, 2025). GWAS study -- ABTB3 appears as a locus, not functionally studied.

**Note on alias**: ABTB3 is also known as **BTBD11**. Searching under BTBD11 would likely recover additional literature, including the synaptic function characterization. The BTBD11 alias was not searched in this harvest.

**Research Volume Assessment**: Essentially no literature under the ABTB3 name (1-2 papers, neither functionally characterizing the protein). The alias BTBD11 is the more established name. This gene symbol change (BTBD11 to ABTB3) is recent and has fragmented the literature. The known function (interneuron-specific synaptic protein) comes from BTBD11 studies.

**Aliases observed**: BTBD11

## 5. AlphaFold / PAE / PDB

### AlphaFold
- Entry: AF-A6QL63-F1 (version 6)
- Mean pLDDT: 71.9 (moderate-low confidence)
- pLDDT >90: 32.6%, 70-90: 33.7%, <50: 25.7%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures
**None.** No experimental structures for this 1104 aa protein.

**Structure Assessment**: Moderate-low confidence AlphaFold model. A quarter of residues (25.7%) are in the low-confidence range (<50 pLDDT), suggesting significant intrinsic disorder. Only 32.6% high-confidence regions. The model suggests a largely flexible protein with some structured domains. The absence of experimental structures for an 1104 aa protein is not surprising but limits structural analysis.

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR059008 | Ankyrin repeat-containing domain |
| IPR052089 | Ankyrin repeat and BTB/POZ domain-containing protein |
| IPR002110 | Ankyrin repeat |
| IPR036770 | Ankyrin repeat superfamily |
| IPR000210 | BTB/POZ domain |
| IPR047824 | BTB/POZ domain, ABTB3-like |
| IPR009072 | - |
| IPR011333 | BTB/POZ fold |

| Pfam | Description |
|------|-------------|
| PF00023 | Ankyrin repeat |
| PF12796 | Ankyrin repeat |
| PF00651 | BTB/POZ domain |
| PF26281 | - |

**Domain Assessment**: ABTB3 has the same domain architecture as ABTB2: BTB/POZ + ankyrin repeats. The domains are nearly identical (same Pfam and InterPro entries). As with ABTB2, the BTB/POZ domain is mechanistically compatible with CUL3 adaptor function and potential nuclear roles. However, the known synaptic function (from BTBD11 literature) suggests a primarily membrane/synaptic role for this paralog.

Note that ABTB3 has an additional ABTB3-specific InterPro entry (IPR047824), distinguishing it from ABTB2 at the domain level.

## 7. Protein-Protein Interaction Network

### STRING
**STRING query failed** (HTTP Error 502: Bad Gateway). No STRING data available.

### IntAct (7 interactions)
| Partner | Method | PMID | Significance |
|---------|--------|------|-------------|
| Dlg4/PSD-95 | co-IP | 19455133 | **Postsynaptic scaffold -- synaptic function** |
| CEP83 | BioID | 26638075 | Centrosomal protein |
| Dlgap1/SAPAP | co-IP | 28671696 | **Postsynaptic scaffold -- synaptic function** |
| ABTB2 | co-IP | 33961781 | Paralog interaction |
| TIAM1 | Two-hybrid | 35914814 | Rac1 GEF |
| MAP1LC3B | Phage display (direct) | 35044719 | **Autophagy receptor LC3B** |
| MAP1LC3A | Phage display (direct) | 35044719 | **Autophagy receptor LC3A** |

### UniProt Interactions
**None.** No UniProt binary interactions recorded.

**PPI Assessment**: Sparse but mechanistically interesting. The interactions with postsynaptic scaffolds (Dlg4/PSD-95, Dlgap1/SAPAP) confirm the synaptic localization. The direct interaction with LC3 family autophagy receptors (MAP1LC3B, MAP1LC3A) is notable and suggests a role in autophagy. The ABTB2 paralog interaction (co-IP, PMID:33961781) may indicate co-regulation or complex formation. No nuclear interaction partners -- consistent with the synaptic function.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | Based on HPA/UniProt/GO evidence |
| 蛋白大小 | 3/10 | ×1 | 3 | |
| 研究新颖性 | 10/10 | ×5 | 15 | PubMed strict count |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT |
| 调控结构域 | 3/10 | ×2 | 6 | InterPro/Pfam |
| PPI 网络 | 2/10 | ×3 | 6 | STRING/IntAct |
| **加权总分** | | | **89/180**** | |
| **归一化总分 (÷1.83)** | | | **48.6/100**** | |

## 9. Final Decision

**SCORED: 34/100 -- WEAK CANDIDATE, LOW CONFIDENCE**

ABTB3 has the lowest score in this re-evaluation set. The case for nuclear localization is thin: HPA says Nucleoplasm (Supported) but is directly contradicted by UniProt (Membrane) and the known synaptic function. The protein is a characterized interneuron-specific synaptic protein under the alias BTBD11. While the BTB/POZ domain is compatible with nuclear function (CUL3 adaptor), the experimental evidence strongly points to a synaptic membrane role.

**Strengths**:
- HPA Supported nucleoplasmic localization
- BTB/POZ + ankyrin repeat architecture -- CUL3 adaptor potential
- Large protein with multi-domain organization
- Direct LC3 interaction suggests autophagy connection

**Weaknesses**:
- Direct contradiction with UniProt (Membrane) and known synaptic function
- No corroborating nuclear evidence from any source other than HPA
- STRING data unavailable (server error)
- No nuclear PPI partners -- all interactions are synaptic or cytoplasmic
- Essentially zero literature under ABTB3 name
- No IF display images
- No PDB structures
- Known function (BTBD11) is synaptic, not nuclear

**Recommendation**: This is the weakest candidate in the set and the closest to being a legitimate rejection. The HPA nuclear annotation contradicts both the UniProt annotation and the established functional characterization. However, other BTB proteins are known to have dual cytoplasmic/nuclear functions, and the protein has not been specifically studied for nuclear localization. Retain at lowest priority with a strong recommendation for validation before any functional follow-up.

## 10. Manual Review Note

The original Excel classified ABTB3 as HPA="Nucleoli|Nucleoplasm" with nuclear_score=6. The actual HPA data shows only "Nucleoplasm" (no Nucleoli). More critically, ABTB3 is a known synaptic protein (BTBD11) characterized as "cortical and hippocampal inhibitory interneuron-specific" with localization at glutamatergic synapses. The HPA nuclear annotation may reflect the antibody detecting the protein in the cell body (where the nucleus resides) rather than true nuclear enrichment.

**Re-evaluator's note**: If the project's goal is to identify genuine nuclear proteins, ABTB3 is probably a false positive from the HPA screen. The protein's established function and interaction network are exclusively synaptic/cytoplasmic. The HPA nuclear annotation, while "Supported," is the only source claiming nuclear localization and is contradicted by functional data. This gene may have been correctly rejected in the original screen, or at minimum should be deprioritized below all other candidates in this set. If retained, manual verification of the HPA IF raw images is essential to determine whether the nucleoplasmic signal is real or represents cell body/perinuclear staining.
