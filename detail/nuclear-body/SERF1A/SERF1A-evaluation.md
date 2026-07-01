---
type: protein-evaluation
gene: SERF1A
date: 2026-06-28
tags: [TE-regulation, nuclear-body, IDP, amyloid-modifier, tier-1]
status: shortlisted
---

# SERF1A Protein Evaluation for TE Regulation Research

## 1. Basic Information (基本信息)

| 属性 Attribute | 值 Value |
|---|---|
| **Gene Symbol** | SERF1A (small EDRK-rich factor 1A) |
| **Synonyms** | FAM2A, SERF1, SMAM1, 4F5, h4F5 |
| **UniProt Accession** | [O75920](https://www.uniprot.org/uniprotkb/O75920) (SERF1_HUMAN, Swiss-Prot reviewed) |
| **Protein Name** | Small EDRK-rich factor 1 |
| **Length** | 110 aa (canonical isoform); isoform 2: ~68 aa |
| **Molecular Weight** | ~12.3 kDa |
| **Chromosome Location** | 5q13.3 |
| **HPA Subcellular** | **Nuclear bodies** (Uncertain reliability, single antibody HPA075271) |
| **UniProt Subcellular** | Cytoplasm (cytosol), Nucleus (IMP evidence) |
| **HPA Nuclear** | Yes (nuclear bodies) |
| **Classification** | nuclear-body |
| **Excel Tier** | 1 |
| **Excel PPI Count** | 27 |
| **Excel Hotness** | 25 |
| **AlphaFold pLDDT** | 62.66 (isoform 1, low confidence); 80.31 (isoform 2) |
| **Disorder** | 55.5% disordered (residues 1–61) -- likely IDP |
| **PubMed Count** | 18 |
| **Key Domains** | SERF family (IPR007513 / Pfam PF04419), N-terminal disordered region, SNCA-binding motif (aa 11–17) |

## 2. Scoring Overview (评分概览)

| 维度 Dimension | 得分 Score | 权重 Weight | 加权后 Weighted | 关键证据摘要 Key Evidence |
|---|---|---|---|---|
| **核定位** (Nuclear Localization) | 8/10 | ×4 | 32 | Both UniProt (IMP) and HPA support nuclear localization; HPA specifically shows "Nuclear bodies"; UniProt also lists cytosol |
| **大小** (Size) | 10/10 | ×1 | 10 | 110 aa, extremely small protein -- ideal for delivery, facile manipulation |
| **新颖性** (Novelty) | 9/10 | ×5 | 45 | Literally zero publications on TE regulation; totally uncharted territory for transposon biology; 18 PubMed total, all amyloid/neurodegeneration |
| **结构** (Structure) | 5/10 | ×3 | 15 | Mostly disordered (55.5% IDR); AlphaFold pLDDT 62.66 (low confidence); NMR structures exist (PDB 9M27, 9M2D) for N-terminal half only; no defined globular fold |
| **调控结构域** (Regulatory Domains) | 3/10 | ×2 | 6 | No chromatin-binding, DNA-binding, or histone-modifying domains; SERF domain is amyloid-modifying, not gene-regulatory; SNCA-binding motif is neurodegeneration-relevant |
| **PPI 网络** (PPI Network) | 5/10 | ×3 | 15 | 27 interactors (Excel count); BioGRID shows 21 unique physical interactors including SMC2/SMC4 (chromatin structural proteins!), GAPDH, APP, LRRK2; limited direct nuclear PPI |

| 加权总分 Weighted Total | **123/180** |
|---|---|
| 归一化总分 Normalized Score (÷1.83) | **67.2/100** |

**Scoring Notes:**
- Nuclear localization is validated but the signal is not strong (HPA: uncertain reliability, antibody cross-reactivity warning).
- Novelty is the standout dimension -- SERF1A is in a completely different field (amyloid biology/neurodegeneration), which means TE regulation represents a genuine paradigm shift if validated.
- Structural score is modest because the protein is largely disordered, lacking well-defined domains typical of transcriptional regulators.
- The PPI network includes SMC2 and SMC4 (condensin complex), which are chromatin structural proteins -- this is a potentially relevant connection for TE regulation via chromatin architecture.

## 3. Detailed Analysis (详细分析)

### 3.1 Nuclear Localization Evidence (核定位证据)

| Evidence Type | Finding | Reliability |
|---|---|---|
| **UniProt (GO)** | Nucleus (GO:0005634) -- IMP, PMID:31034892 | **High** -- experimental |
| **HPA IF** | Nuclear bodies (AF22, HEK293 cells); no staining in U2OS | **Uncertain** -- single antibody (HPA075271), cross-reactivity warning |
| **HPA Prediction** | Membrane, Intracellular (bioinformatic prediction) | Low |
| **Note** | HPA explicitly cautions: "Based on antibodies targeting proteins from multiple genes." This means the nuclear bodies signal may not be SERF1A-specific. | -- |

**HPA IF Images:**

AF22 cell line (Nuclear bodies staining):
![SERF1A HPA AF22](https://images.proteinatlas.org/75271/1595_E4_1_blue_red_green.jpg)

HEK293 cell line (Nuclear bodies staining):
![SERF1A HPA HEK293](https://images.proteinatlas.org/75271/1569_A4_1_blue_red_green.jpg)

**Assessment:** SERF1A is reported in both the nucleus and cytoplasm by UniProt experimental annotation. The HPA nuclear bodies localization is uncertain-grade. Given the very small size (12.3 kDa), SERF1A can passively diffuse through nuclear pores, so nuclear presence is physically plausible. However, the nuclear bodies annotation should be treated with caution given the antibody specificity concern.

### 3.2 Structural Analysis (结构分析)

SERF1A is a prototypical intrinsically disordered protein (IDP):

| Structural Feature | Residues | Notes |
|---|---|---|
| **Disordered region** | 1–61 | Predicted by MobiDB-lite and SAM |
| **Low complexity region** | 34–50 | Typical of IDPs |
| **Basic/acidic bias** | 1–30 | Highly charged N-terminus, characteristic of disordered proteins |
| **SNCA-binding motif** | 11–17 (RQKNKK) | The only functionally characterized motif |
| **C-terminal half** | ~62–110 | May have partial structure; no domain annotation |

**AlphaFold Prediction Quality:**
- Isoform 1 (110 aa): pLDDT = 62.66, with 24.5% residues in "very low" confidence (<50)
- Isoform 2 (68 aa): pLDDT = 80.31, with 27.4% residues in "very high" confidence (>90)
- PAE image: [AF-O75920-F1 PAE](https://alphafold.ebi.ac.uk/files/AF-O75920-F1-predicted_aligned_error_v6.png)
- The low pLDDT score for isoform 1 is expected for an IDP -- AlphaFold does not model disorder well.

**NMR Structures:** Two NMR ensembles exist for the N-terminal region (residues 1-62): PDB 9M27 and 9M2D. These confirm intrinsic disorder.

**Implications for TE Regulation:**
- IDPs often function through "fuzzy" interactions and can serve as hubs in protein interaction networks
- The lack of a DNA-binding domain is a limitation for direct TE silencing
- However, IDPs can form condensates via phase separation (PMID 38272228 shows SERF1A promotes alpha-synuclein aggregation through liquid-liquid phase separation) -- LLPS is directly relevant to heterochromatin formation and TE silencing

### 3.3 Domain Architecture (结构域分析)

| Database | Identifier | Name | Description |
|---|---|---|---|
| **Pfam** | PF04419 | SERF-like_N | SERF family, N-terminal |
| **InterPro** | IPR007513 | SERF-like_N | Small EDRK-rich factor-like, N-terminal |
| **InterPro** | IPR040211 | SERF1/2-like | SERF1 and SERF2 subfamily |
| **PANTHER** | PTHR13596:SF1 | SMALL EDRK-RICH FACTOR 1 | Species-specific subfamily |

**Assessment:** No DNA-binding domains, no chromatin reader/writer domains, no histone modification domains. The SERF domain is exclusively associated with amyloid modification. This is the major weakness for TE regulation candidacy -- SERF1A lacks any recognizable regulatory domain architecture.

### 3.4 PPI Network Analysis (蛋白互作网络分析)

**Total BioGRID physical interactors:** 21 unique

**Key interactors sorted by functional relevance:**

| Interactor | Function | Relevance to TE Regulation |
|---|---|---|
| **SMC4** | Condensin complex subunit, chromosome condensation | **HIGH** -- Condensins shape 3D genome architecture; direct chromatin structural protein |
| **SMC2** | Condensin complex subunit, chromosome condensation | **HIGH** -- Partner of SMC4; chromosome architecture |
| **APP** | Amyloid precursor protein; also has nuclear functions | **MODERATE** -- APP intracellular domain (AICD) is a transcriptional regulator |
| **GAPDH** | Glycolytic enzyme; also functions in transcriptional regulation | **MODERATE** -- GAPDH binds DNA and regulates transcription |
| **MED4** | Mediator complex subunit | **MODERATE** -- Mediator links transcription factors to RNA Pol II; core transcriptional machinery |
| **APEX1** | AP endonuclease 1; redox regulator of transcription factors | **MODERATE** -- Transcriptional co-regulator |
| **ZRANB1** | Zinc finger RANBP2-type containing 1; deubiquitinase | **LOW** |
| **LRRK2** | Leucine-rich repeat kinase 2 | **LOW** -- Parkinson's disease; not TE-related |
| **PIK3R3** | PI3K regulatory subunit | **LOW** |
| Others (AQP6, CERS4, etc.) | Membrane/vesicle proteins from Luck et al. 2020 high-throughput screen | **LOW** |

**Nuclear PPI:** SERF1A has 16+ entries in `nuclear_ppi_human.tsv`, but most come from the STRING database (inferred associations). BioGRID shows few direct nuclear interactions.

**Assessment:** The SMC2/SMC4 interaction is the most intriguing for TE biology. Condensins are essential for mitotic chromosome architecture and also contribute to interphase chromatin organization. If SERF1A influences condensin loading or activity at TE loci, this could provide a mechanism for TE regulation. However, the condensin interaction is from a single high-throughput study (Huttlin et al. 2021) and requires independent validation.

### 3.5 Functional Annotation (功能注释)

| GO Category | Term | Evidence |
|---|---|---|
| **Biological Process** | Amyloid fibril formation (GO:1990000) | IMP |
| **Biological Process** | Protein destabilization (GO:0031648) | IMP |
| **Biological Process** | Nervous system development (GO:0007399) | TAS |
| **Cellular Component** | Nucleus (GO:0005634) | IMP |
| **Cellular Component** | Cytosol (GO:0005829) | IMP |
| **Cellular Component** | Protein-containing complex (GO:0032991) | IMP |

**No GO molecular function assigned.** This is typical for an IDP without enzymatic activity.

### 3.6 Literature Landscape (文献全景)

**PubMed total:** 18 publications

**Top 5 papers by relevance:**

| PMID | Year | Title | Journal | Relevance |
|---|---|---|---|---|
| 31034892 | 2019 | Increased Aggregation Tendency of Alpha-Synuclein in a Fully Disordered Protein Complex | J Mol Biol | Core -- structural basis of SERF1a pro-amyloid activity |
| 22854022 | 2012 | SERF protein is a direct modifier of amyloid fiber assembly | Cell Rep | Core -- SERF1a distinguishes amyloid vs non-amyloid aggregation |
| 20723760 | 2010 | Identification of MOAG-4/SERF as a regulator of age-related proteotoxicity | Cell | Core -- discovery of SERF as conserved aggregation modifier |
| 38272228 | 2024 | The disordered protein SERF promotes alpha-Synuclein aggregation through liquid-liquid phase separation | J Biol Chem | Important -- LLPS mechanism, condensate biology relevant to nuclear organization |
| 39120045 | 2024 | Binding structures of SERF1a with NT17-polyQ peptides of huntingtin exon 1 | IUCrJ | Structural -- huntingtin interaction |

**Key insight from PMID 38272228:** SERF1A undergoes liquid-liquid phase separation. This is mechanistically interesting because nuclear bodies (where SERF1A localizes per HPA) are phase-separated condensates. LLPS is also central to heterochromatin formation (HP1 proteins phase-separate), suggesting a possible parallel mechanism for TE regulation.

**Literature gap:** Zero publications connecting SERF1A to transposable elements, chromatin regulation, or genome defense. The entire literature is focused on neurodegeneration (Alzheimer's, Parkinson's, polyglutamine diseases) and spinal muscular atrophy.

### 3.7 Expression and Tissue Distribution (表达与组织分布)

- **Predominantly expressed** in heart, brain, and skeletal muscle
- Both isoforms expressed throughout the central nervous system, including spinal cord
- Expression is not testis-specific (testis is a key site of TE regulation via piRNA pathway)
- Brain expression is notable because LINE-1 retrotransposition is observed in neural cells

## 4. Overall Assessment (总体评估)

### Strengths for TE Regulation Research

1. **Unique angle (novelty):** SERF1A is completely unexplored in TE biology. Its known function -- amyloid protein aggregation modification -- has no obvious connection to transposon control, making any TE regulation finding a genuine paradigm shift rather than incremental work.
2. **Nuclear localization is plausible:** Experimental evidence (UniProt IMP) places SERF1A in the nucleus. If validated, the nuclear bodies localization is intriguing because several TE silencing factors localize to nuclear bodies (e.g., PML bodies).
3. **Phase separation competence:** PMID 38272228 demonstrates SERF1A undergoes LLPS. Since heterochromatin formation and nuclear body assembly both involve phase separation, there is a mechanistic conceptual bridge -- even if the substrates are totally different (amyloid proteins vs. chromatin).
4. **Condensin interaction (SMC2/SMC4):** If real, this provides a direct chromatin architectural connection. Condensin loading/unloading affects chromatin compaction, which directly impacts TE accessibility.
5. **Very small size:** 110 aa / 12.3 kDa makes SERF1A experimentally tractable -- easy to clone, express, purify, tag, and deliver.

### Weaknesses for TE Regulation Research

1. **No DNA/chromatin regulatory domains:** SERF1A lacks any recognizable DNA-binding domain, histone modification domain, chromatin reader domain, or transcription factor domain. This makes a direct TE silencing mechanism hard to envision.
2. **Primary function is cytoplasmic:** The dominant biological function of SERF1A is cytoplasmic -- promoting amyloid protein aggregation. Nuclear localization may be secondary or even incidental (passive diffusion for a 12.3 kDa protein).
3. **No TE-related literature:** Zero papers. SERF1A is exclusively studied in neurodegeneration contexts. There is no existing evidence base to build on.
4. **HPA nuclear bodies data is uncertain:** The single antibody (HPA075271) has a multi-gene cross-reactivity warning. Nuclear localization needs independent validation.
5. **Cellular function is pro-aggregation:** SERF1A destabilizes proteins and promotes their aggregation. If it has a nuclear function, it might promote aggregation of nuclear proteins -- which could be toxic rather than regulatory.
6. **No expression in germline/testis:** TE regulation is most critical in the germline. SERF1A is primarily expressed in brain, heart, and muscle.

### Verdict

SERF1A is a **bold, unconventional candidate** for TE regulation. The case rests on two speculative mechanistic hypotheses:
- **The LLPS/condensate hypothesis:** SERF1A phase-separates and its condensate properties could be co-opted for heterochromatin or nuclear body assembly at TE loci.
- **The SMC2/SMC4 hypothesis:** SERF1A interacts with condensins and influences chromosome architecture, indirectly affecting TE accessibility.

These are plausible but entirely untested. The protein's entire annotation points toward neurodegeneration/amyloid biology, making this a high-risk/high-reward pick. If you are looking for a protein with an established chromatin regulatory mechanism, SERF1A is not the right choice. If you are screening for unexpected TE regulators and want to open a completely new direction, SERF1A is an intellectually exciting (albeit risky) candidate.

**Recommendation:** Keep shortlisted but assign lower priority than proteins with established chromatin/nuclear regulatory domains. SERF1A would be a "breakthrough or bust" project.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR007513;IPR040211; |
| Pfam | PF04419; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SMN1 | STRING | 843 |
| SMN2 | STRING | 843 |
| GPKOW | STRING | 724 |
| C1S | STRING | 720 |
| APP | BioGRID | 1 |
| MED4 | BioGRID | 1 |
| LRRK2 | BioGRID | 1 |
| APEX1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

## 5. Data Sources (数据来源)

| Source | Access URL / Identifier | Data Retrieved |
|---|---|---|
| **UniProt** | https://rest.uniprot.org/uniprotkb/O75920 | Full annotation, domains, GO terms, subcellular location |
| **AlphaFold DB** | https://alphafold.ebi.ac.uk/api/prediction/O75920 | pLDDT (62.66/80.31), PAE image, structure metadata |
| **HPA** | https://www.proteinatlas.org/ENSG00000172058-SERF1A/subcellular | IF images, nuclear bodies localization, HPA075271 antibody |
| **PubMed** | esearch/esummary NCBI E-utilities | 18 publications, top 5 papers |
| **BioGRID (local)** | `/protein_data/data-finding/ppi_data/biogrid_human_ppi.tab3.txt` | 21 unique physical interactors |
| **STRING (local)** | `/protein_data/data-finding/ppi_data/string_human_ppi.tsv.gz` | Inferred associations (viewed in `nuclear_ppi_human.tsv`) |
| **Nuclear PPI (local)** | `/protein_data/data-finding/ppi_data/nuclear_ppi_human.tsv` | 16+ entries including SMC2, SMC4, GAPDH |
| **InterPro** | https://www.ebi.ac.uk/interpro/ | IPR007513 (SERF-like_N), IPR040211 (SERF1/2-like) |
| **PDB** | https://www.rcsb.org/ | 9M27, 9M2D (NMR structures, residues 1-62) |
| **NCBI Gene** | GeneID: 8293 | Gene info, chromosomal location |

## 6. Supplementary Notes (补充说明)

1. **SERF1A vs SERF1B:** SERF1A and SERF1B are nearly identical paralogs. The exon count given by HPA (8 transcripts) includes both genes. Most functional studies likely cannot distinguish which paralog is being measured.

2. **SMA connection:** SERF1A was originally identified as a "candidate modifier gene for spinal muscular atrophy" (Scharf et al., 1998, Nat Genet). SMA is caused by SMN1 deletion; SMN1 has genomic proximity to SERF1A at 5q13.3. The SMA modifier role may be due to genomic location rather than protein function.

3. **LLPS and TE biology:** The 2024 paper (PMID 38272228) showing SERF1A drives aggregation via liquid-liquid phase separation is the most TE-relevant finding indirectly. Nuclear condensates (nucleoli, Cajal bodies, PML bodies, heterochromatin foci) are all phase-separated compartments. If SERF1A can nucleate condensates in the nucleus, it could influence chromatin organization. This is speculative but mechanistically grounded.

4. **Alternative isoform:** The short isoform (residues 39-110 replaced with "RDSEIMQEKQKAANEKKSMQTREK") is 68 aa and has a much higher AlphaFold pLDDT (80.31). Its specific function is uncharacterized.

5. **Antibody situation:** Only one commercial HPA antibody (HPA075271) exists. Independent validation of subcellular localization (e.g., by expressing tagged SERF1A) would be essential before pursuing TE regulation experiments.

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/SERF1A_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.48 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 72.7% |
| 建模残基数 | 110 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

