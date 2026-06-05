---
type: protein-evaluation
gene: "CLTA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLTA — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLTA |
| 蛋白名称 | Clathrin light chain A |
| 蛋白大小 | 248 aa / 27.1 kDa |
| UniProt ID | P09496 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endosomes, Lysosomes; 额外: Golgi apparatus, Plasma membrane, ; UniProt: Cytoplasmic vesicle membrane; Membrane, coated pit; Cytoplas |
| 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 27.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=70.1; PDB: 6E5N |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000996; Pfam: PF01086 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endosomes, Lysosomes; 额外: Golgi apparatus, Plasma membrane, Mitotic spindle, Primary cilium | Supported |
| UniProt | Cytoplasmic vesicle membrane; Membrane, coated pit; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin coat (GO:0030118)
- clathrin coat of coated pit (GO:0030132)
- clathrin coat of trans-Golgi network vesicle (GO:0030130)
- clathrin complex (GO:0071439)
- clathrin vesicle coat (GO:0030125)
- clathrin-coated endocytic vesicle (GO:0045334)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 114 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification and validation of TUBB, CLTA, and FBXL5 as potential diagnostic markers of postmenopausal osteoporosis.. *Biomolecules & biomedicine*. PMID: 40791155
2. Clathrin light chain A facilitates small extracellular vesicle uptake to promote hepatocellular carcinoma progression.. *Hepatology international*. PMID: 37354358
3. Identification and functional characterization of hub genes CLTA, EDIL3, HAPLN1, and HIP1 as diagnostic biomarkers and therapeutic targets in thyroid cancer and Hashimoto's thyroiditis.. *Clinical and experimental medicine*. PMID: 40372556
4. Association of CTLA-4 gene polymorphisms and alopecia areata: a systematic review and meta-analysis.. *Biomarkers : biochemical indicators of exposure, response, and susceptibility to chemicals*. PMID: 35254172
5. Cloning of cDNAs for H1F0, TOP1, CLTA and CDK1 and the effects of cryopreservation on the expression of their mRNA transcripts in yak (Bos grunniens) oocytes.. *Cryobiology*. PMID: 24854867

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 21.8% |
| 置信残基 (pLDDT 70-90) 占比 | 36.7% |
| 中等置信 (pLDDT 50-70) 占比 | 18.5% |
| 低置信 (pLDDT<50) 占比 | 23.0% |
| 有序区域 (pLDDT>70) 占比 | 58.5% |
| 可用 PDB 条目 | 6E5N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=70.1，有序区 58.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000996; Pfam: PF01086 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLTC | 0.999 | 0.935 | — |
| CLTCL1 | 0.999 | 0.901 | — |
| CLTB | 0.985 | 0.634 | — |
| AP2A1 | 0.983 | 0.268 | — |
| MYO6 | 0.974 | 0.946 | — |
| AP2B1 | 0.965 | 0.419 | — |
| AP2S1 | 0.961 | 0.186 | — |
| AP2M1 | 0.958 | 0.183 | — |
| AP2A2 | 0.946 | 0.244 | — |
| AP1S1 | 0.932 | 0.246 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| RGS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CTNNB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 6E5N | pLDDT=70.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle membrane; Membrane, coated pit / Endosomes, Lysosomes; 额外: Golgi apparatus, Plasma  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLTA — Clathrin light chain A，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09496
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122705-CLTA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLTA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09496
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endosomes (supported)。来源: https://www.proteinatlas.org/ENSG00000122705-CLTA/subcellular

![](https://images.proteinatlas.org/2665/653_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2665/653_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2665/658_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2665/658_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2665/659_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2665/659_B7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09496-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
