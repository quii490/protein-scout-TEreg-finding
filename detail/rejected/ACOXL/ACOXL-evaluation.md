---
type: protein-evaluation
gene: ACOXL
date: 2026-06-02
tags:
  - protein-evaluation
  - nucleus-cytoplasm
  - nucleolus
  - acyl-coa-oxidase
  - peroxisome
  - cancer-marker
  - re-evaluate
  - pilot-gene
status: rejected
nuclear_score: 6
---

# ACOXL (Acyl-coenzyme A oxidase-like protein) -- Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9NUZ1 |
| **Protein Name** | Acyl-coenzyme A oxidase-like protein |
| **Aliases** | (none) |
| **Length** | 547 aa |
| **Mass** | 61.8 kDa |
| **AlphaFold mean pLDDT** | 92.1 |
| **AlphaFold pLDDT >90** | 80.1% |
| **AlphaFold pLDDT <50** | 1.5% |
| **PubMed (strict)** | 18 |
| **PubMed (broad)** | 35 |
| **Function** | No functional annotation in UniProt. By homology, predicted to function as an acyl-CoA oxidase involved in fatty acid beta-oxidation in peroxisomes. Identified as a putative diagnostic marker in prostate cancer (PMID:26237329). |

## 2. 核定位证据

### UniProt Subcellular Location
**No subcellular location annotation.** UniProt has not annotated ACOXL's subcellular localization.

### GO Cellular Component
- GO:0005782 **peroxisomal matrix** (TAS:Reactome -- traceable author statement)
- GO:0005777 **peroxisome** (IBA:GO_Central)

**Note**: Both GO-CC terms point to peroxisomal localization. This is consistent with ACOXL's homology to acyl-CoA oxidases, which are peroxisomal enzymes. No nuclear GO terms.

### HPA Subcellular Localization
- **Main location**: **Cytosol**
- **Additional locations**: **Nucleoli**
- **Reliability (IF)**: **Supported** (second-highest tier)
- **IF Display Images Available**: YES (12 images)
  - `407_B2_1_blue_red_green.jpg`, `407_B2_2_blue_red_green.jpg`
  - `1392_G3_1_blue_red_green.jpg`, `1392_G3_2_blue_red_green.jpg`
  - `410_B2_1_blue_red_green.jpg`, `410_B2_2_blue_red_green.jpg`
  - `862_F3_1_blue_red_green.jpg`, `862_F3_2_blue_red_green.jpg`
  - `1423_E12_2_blue_red_green.jpg`, `1423_E12_3_blue_red_green.jpg`
  - `859_F3_1_blue_red_green.jpg`, `859_F3_2_blue_red_green.jpg`
- **Image status**: `if_display_images_available`

**HPA Nuclear Localization Summary**: HPA classifies ACOXL with Cytosol as the main location and Nucleoli as an additional location. This is NOT a primarily nuclear protein by HPA classification -- the main compartment is cytoplasmic. Nucleoli are listed as an additional (minor) location. 12 IF display images are available for manual review, which is an unusually large number and provides good opportunities to assess the nucleolar signal.

**Nuclear Evidence Assessment**: The only nuclear evidence is the HPA nucleoli additional classification. UniProt has no SL annotation, and GO-CC points exclusively to peroxisomes. The nucleolar annotation is weak evidence for nuclear localization -- it is an additional (not main) location that may represent a minor pool or conditional localization.

**Note on Excel discrepancy**: The original Sheet4 Excel listed ACOXL as HPA="Nucleoplasm" with nuclear_score=6. The actual harvested HPA data does NOT include Nucleoplasm anywhere in the subcellular_location list. The main location is Cytosol, and the only nuclear compartment is Nucleoli (additional). This is a compound discrepancy: (1) Nucleoplasm vs. Nucleoli -- wrong compartment, and (2) the Excel implied this was a primary nuclear location when it is only an additional location.

## 3. HPA Immunofluorescence

12 IF display images available -- the most of any gene in this set. This provides excellent material for manual review. The images span multiple cell lines and antibodies, giving multiple independent views of the localization. The nucleolar classification as an additional (not main) location suggests the nucleolar signal is weaker or more variable than the cytosolic signal. **Manual inspection of these images is strongly recommended to assess nucleolar signal quality and consistency.**

The large number of images (12 IF display images) is unusually generous for HPA and suggests the antibody staining was strong and reproducible, even if the nucleolar classification was not the primary one.

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "ACOXL"[Title/Abstract] AND (gene OR protein OR hydrolase) | 18 | All gene-specific |
| Symbol-only: "ACOXL"[Title/Abstract] | 35 | Gene-specific |
| Broad: "ACOXL" | 35 | All gene-specific |

**Key Papers:**
- PMID:26237329 -- "Analysis of the Human Prostate-Specific Proteome Defined by Transcriptomics and Antibody-Based Profiling Identifies TMEM79 and ACOXL as Two Putative, Diagnostic Markers in Prostate Cancer" (PLoS ONE, 2015). **Key paper**. Identifies ACOXL as a prostate cancer diagnostic marker using HPA data. This is an HPA-derived study.
- PMID:33841008 -- "Anti-tumor activities of Panax quinquefolius saponins and potential biomarkers in prostate cancer" (J Ginseng Res, 2021).
- PMID:38367693 -- "Histone H3K36me3 mediates the genomic instability of Benzo[a]pyrene in human bronchial epithelial cells" (Environ Pollut, 2024).
- PMID:36631795 -- "Proteomics investigation of human sera for determination of postoperative indicators of pulmonary cystic echinococcosis" (J Cardiothorac Surg, 2023).
- PMID:39930543 -- "Multi-omics analysis in primary T cells elucidates mechanisms behind disease-associated genetic loci" (Genome Biol, 2025).

**Research Volume Assessment**: Moderate literature (18 strict, 35 broad). The most relevant paper (PMID:26237329) is directly relevant to this project -- it used HPA data to identify ACOXL as a prostate cancer marker. This paper validates the HPA antibody and localization data being used. The literature spans cancer biomarker studies, GWAS, and proteomics. No paper addresses the nucleolar localization or nuclear function of ACOXL.

## 5. AlphaFold / PAE / PDB

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

### AlphaFold
- Entry: AF-Q9NUZ1-F1 (version 6)
- Mean pLDDT: 92.1 (EXCELLENT confidence)
- pLDDT >90: 80.1%, 70-90: 14.3%, <50: 1.5%
- PAE: Available (JSON file exists at EBI)

### Experimental PDB Structures

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
**None.** No experimental structures available.

**Structure Assessment**: Exceptionally high-confidence AlphaFold model. Mean pLDDT of 92.1 with 80.1% of residues >90 pLDDT is among the best in this set. Only 1.5% low-confidence residues. This suggests ACOXL is a well-folded, globular protein with high structural predictability. The model quality rivals many experimental structures. PAE data available for domain interaction analysis. The absence of experimental PDB structures is mitigated by the very high AlphaFold confidence.

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR055060 | Acyl-coenzyme A oxidase-like |
| IPR006091 | Acyl-CoA oxidase/dehydrogenase, central domain |
| IPR046373 | Acyl-CoA oxidase/dehydrogenase, middle domain superfamily |
| IPR012258 | Acyl-CoA oxidase |
| IPR002655 | Acyl-CoA oxidase, C-terminal domain |
| IPR036250 | Acyl-CoA dehydrogenase/oxidase-like |
| IPR009100 | Acyl-CoA dehydrogenase/oxidase, N-terminal domain superfamily |

| Pfam | Description |
|------|-------------|
| PF01756 | Acyl-CoA oxidase |
| PF22924 | Acyl-CoA oxidase, FAD-binding domain |
| PF02770 | Acyl-CoA dehydrogenase, middle domain |

**Domain Assessment**: ACOXL has a canonical acyl-CoA oxidase domain architecture: N-terminal FAD-binding domain (PF22924), central acyl-CoA dehydrogenase domain (PF02770), and C-terminal acyl-CoA oxidase domain (PF01756). This is the classic domain organization of peroxisomal fatty acid beta-oxidation enzymes. The domains are exclusively metabolic (fatty acid oxidation), with no known DNA-binding domains, no chromatin-interacting domains, and no transcriptional regulatory domains. The domain architecture provides no mechanistic rationale for nucleolar localization.

## 7. Protein-Protein Interaction Network

### STRING (Top 15 -- fatty acid metabolism network)
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
| ECI2 | 0.851 | 0.091 | 0.438 | 0.166 |
| HSDL2 | 0.821 | 0.071 | 0.643 | 0.356 |
| ACOX2 | 0.785 | 0 | 0.700 | 0.170 |
| ETFA | 0.751 | 0.445 | 0.233 | 0.166 |
| ETFB | 0.738 | 0.436 | 0.233 | 0.166 |
| SCP2 | 0.637 | 0.094 | 0.216 | 0.353 |
| HADH | 0.608 | 0.071 | 0.265 | 0.158 |
| CRYL1 | 0.599 | 0.071 | 0.265 | 0.138 |
| ECHS1 | 0.585 | 0.091 | 0.185 | 0.295 |
| HSD17B4 | 0.569 | 0.065 | 0.216 | 0.303 |
| FASN | 0.561 | 0 | 0.312 | 0.378 |
| EHHADH | 0.555 | 0.091 | 0.188 | 0.242 |
| ECI1 | 0.554 | 0.091 | 0.188 | 0.241 |
| HADHB | 0.554 | 0.051 | 0.216 | 0.208 |
| ACAA2 | 0.551 | 0.051 | 0.216 | 0.203 |

### IntAct (1 interaction only)
| Partner | Method | PMID | Significance |
|---------|--------|------|-------------|
| CUL1 | TAP | 21145461 | Cullin-1 scaffold -- ubiquitin ligase complex |

### UniProt Interactions
**None.** No UniProt binary interactions recorded.

**PPI Assessment**: The PPI network is exclusively metabolic. STRING places ACOXL in a fatty acid beta-oxidation network with peroxisomal and mitochondrial enzymes (ECI2, ACOX2, HADH, ECHS1, etc.). Most scores are database-derived or textmining-based. The single IntAct interaction (CUL1, TAP-MS, PMID:21145461) is from a high-throughput study mapping Cullin-RING ligase interactions. No nuclear interaction partners. The PPI data firmly places ACOXL in peroxisomal metabolism, not nuclear processes.

## 7. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA/UniProt/GO evidence |
| 蛋白大小 | 3/10 | ×1 | 3 | |
| 研究新颖性 | 10/10 | ×5 | 15 | PubMed strict |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT |
| 调控结构域 | 3/10 | ×2 | 6 | InterPro/Pfam |
| PPI 网络 | 2/10 | ×3 | 6 | STRING/IntAct |
| **加权总分** | | | **89/180******** | |
| **归一化总分 (÷1.83)** | | | **48.6/100******** | |

## 9. Final Decision

**SCORED: 34/100 -- WEAK NUCLEAR CANDIDATE, LOWEST CONFIDENCE (TIED)**

ACOXL is tied with ABTB3 for the lowest score in this re-evaluation set. The nuclear evidence is minimal: HPA lists Nucleoli as an additional (not main) location, and no other source (UniProt, GO-CC, literature, PPI) supports any nuclear localization. The protein's domain architecture, PPI network, and GO annotations all point to a peroxisomal metabolic enzyme.

**Strengths**:
- 12 HPA IF display images available -- good material for manual review
- Exceptional AlphaFold model (mean pLDDT 92.1)
- Moderate PubMed literature (18-35 papers)
- Identified as prostate cancer diagnostic marker (PMID:26237329) -- applied relevance
- HPA Supported reliability for the annotation

**Weaknesses**:
- Nucleolar annotation is ADDITIONAL, not main -- HPA's primary read is cytoplasmic
- No corroborating nuclear evidence from any other source
- Domain architecture is exclusively metabolic (fatty acid oxidation)
- PPI network is exclusively metabolic/peroxisomal
- GO-CC: peroxisome only
- No functional rationale for nucleolar localization
- No PDB structures

**PAE 状态**: PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
- Cancer marker status is from HPA data, creating potential circularity if HPA data quality is uncertain

**Recommendation**: This is the weakest nuclear candidate in the set and the closest to a legitimate rejection. The nucleolar annotation is a minor additional location that may represent background or cross-reactivity rather than genuine nucleolar enrichment. The 12 IF images should be manually examined -- if the nucleolar signal is weak or inconsistent, this gene should be rejected. If the signal is clear, it could represent a genuinely surprising dual localization (peroxisomal enzyme with nucleolar pool) that would be novel and interesting.

## 10. Manual Review Note

ACOXL is fundamentally a peroxisomal enzyme. The HPA nucleoli additional annotation is the ONLY piece of nuclear evidence. The prostate cancer marker paper (PMID:26237329) comes from the same HPA data, creating a circularity issue -- the only "validation" of the HPA data is from HPA-derived studies. The gene was likely included in the original Excel because of the keyword "Nucleoplasm" assignment, but the actual data shows "Nucleoli" and only as an additional location.

**Re-evaluator's note**: If the project is screening for genuinely nuclear proteins, ACOXL is probably a false positive. The evidence for nuclear localization is a single HPA "additional" annotation that contradicts every other piece of data (GO peroxisome, PPI metabolic, domain architecture). However, the 12 IF images provide an excellent opportunity for definitive adjudication -- if manual review shows clear nucleolar signal, this could represent an interesting case of metabolic enzyme moonlighting in the nucleolus. If the signal is absent or represents nucleolar-adjacent cytoplasmic staining, the gene should be rejected. **Manual IF review required before final decision.**

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000153093-ACOXL/subcellular

![](https://images.proteinatlas.org/35392/1392_G3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35392/1392_G3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35392/407_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35392/407_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35392/410_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35392/410_B2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
