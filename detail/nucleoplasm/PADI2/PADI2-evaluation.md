---
type: protein-evaluation
gene: "PADI2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## PADI2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PADI2 |
| 蛋白名称 | Protein-arginine deiminase type-2 |
| 蛋白大小 | 665 aa / 75.6 kDa |
| UniProt ID | Q9Y2J8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) + ChIP |
| 蛋白大小 | 9/10 | x1 | 9.0 | 665 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=97 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=94.3; PDB=24 |
| 调控结构域 | 5/10 | x2 | 10.0 | Cupredoxin; PAD; PAD_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **119/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +3 |

### 3. 分析
- nan (nan)
- PubMed strict=97 broad=249
- AF pLDDT=94.3 PDB=24
- InterPro: Cupredoxin; PAD; PAD_C
- Pfam: PAD; PAD_M; PAD_N
- PPI degree=9 ChIP: Yes
39529192: Sorafenib-induced macrophage extracellular traps via ARHGDIG/IL4/PADI4 axis conf | 38524554: Association of PADI2 and PADI4 polymorphisms in COVID-19 host severity and non-s | 39793573: Phase 1/2 trial of brogidirsen: Dual-targeting antisense oligonucleotides for ex

### 4. 总体评价
**66.7/100** | **nucleoplasm**
TE candidate: Cupredoxin; PAD; PAD_C


### 补充分析 (UniProt API)

**蛋白全称**: Protein-arginine deiminase type-2

**功能**: Catalyzes the deimination of arginine residues of proteins

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR008972 |
| InterPro | IPR004303 |
| InterPro | IPR013530 |
| InterPro | IPR036556 |
| InterPro | IPR013732 |
| InterPro | IPR038685 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：PADI2（Q9Y2J8, Protein-arginine deiminase type-2, 665 aa / 75.6 kDa）的主要结构域注释为Cupredoxin, PAD, PAD_C。Pfam数据库进一步识别到PAD、PAD_M、PAD_N等保守域。AlphaFold pLDDT=94.3（极高质量）——该蛋白整体折叠高度可信，结构性表征良好。该蛋白已有24个实验PDB结构条目，为机械性研究提供直接的结构基础。PubMed=97，该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=9）——BioGRID数据库记录的互作伙伴包括MTMR14、TRIM24、CSK、CSH1、KLK10、RIPK4。其中TRIM24等具有染色质调控或转录相关功能——提示PADI2可能通过protein-protein interaction平台间接参与核内转录调控网络。

**结构解读**：AlphaFold预测（pLDDT=94.3）显示该蛋白具有明确的折叠结构域，其中Cupredoxin为保守的催化/结合模块。Pfam域PAD、PAD_M的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=94.3的整体质量表明大部分残基（pLDDT>70）处于有序构象，适合X射线晶体学或冷冻电镜（cryo-EM）解析。

**机制模型**：PADI2为protein-arginine deiminase（PAD）家族成员——催化arginine→citrulline的翻译后修饰（citrullination/deimination）。这种不可逆修饰改变target protein的电荷状态、折叠和互作能力。Histone citrullination（尤其H3Cit26）已被报道与transcriptional activation和NETosis相关——PADI2可能通过citrullinate histone tail或chromatin-associated protein→modulate chromatin compaction around TE loci。

**TE调控展望**：该蛋白被标注为TE_REG_CANDIDATE——含Cupredoxin; PAD; PAD_C结构域。TE调控关联性取决于以下几个方面：（1）PADI2是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）PADI2是否能够通过其结构域识别TE-derived DNA/RNA element；（3）PADI2的knockout/knockdown是否改变LINE-1或ERV family的expression level。PAD-mediated citrullination在chromatin decompaction和NETosis中有明确功能——PADI2可能通过histone citrullination remodel TE chromatin landscape。建议citrullinomics profiling（anti-citrulline antibody enrichment + MS）检测其在histone tail上的modification site。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MTMR14 | BioGRID | 1 |
| TRIM24 | BioGRID | 1 |
| CSK | BioGRID | 0 |
| CSH1 | BioGRID | 0 |
| KLK10 | BioGRID | 0 |
| RIPK4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y2J8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PADI2

### PubMed

**Count: 249**

| PMID | Title |
|---|---|
| 42252772 | Mapping the Substrate Specificity Landscape of PAD2 and PAD4 Enzymes. |
| 42035672 | Innovative multi-epitope vaccine development for rheumatoid arthritis via immunoinformatics. |
| 41962542 | Astrocytic calcium-dependent enzyme PAD2 governs microglia activity to exacerbate amyloid pathology via citrullinated vimentin. |
| 41818416 | Epigenetic Alterations Beyond CpG Islands in Periodontitis: In Silico Study of DNA Methylation Data. |
| 41816790 | Genomic landscape of oral squamous cell carcinoma from the southwest coast of Karnataka: insights from FFPE-based next-generation sequencing. |
