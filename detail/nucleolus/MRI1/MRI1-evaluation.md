---
type: protein-evaluation
gene: "MRI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MRI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MRI1 / MRDI |
| 蛋白名称 | Methylthioribose-1-phosphate isomerase |
| 蛋白大小 | 369 aa / 39.1 kDa |
| UniProt ID | Q9BV20 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli fibrillar center; UniProt: Nucleus; Cytoplasm; Cell projection |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 369 aa / 39.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=94.8; PDB: 4LDQ, 4LDR |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000649, IPR005251, IPR042529, IPR011559, IPR027 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus; Cytoplasm; Cell projection | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cell projection (GO:0042995)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 109 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MRDI |

**关键文献**:
1. Identification of prognostic RNA editing profiles for clear cell renal carcinoma.. *Frontiers in medicine*. PMID: 39091293
2. NOTCH2, ATIC, MRI1, SLC6A13, ATP13A2 Genetic Variations are Associated with Ventricular Septal Defect in the Chinese Tibetan Population Through Whole-Exome Sequencing.. *Pharmacogenomics and personalized medicine*. PMID: 37138656
3. Identification of Six Pathogenic Genes for Tibetan Familial Ventricular Septal Defect by Whole Exome Sequencing.. *The Journal of surgical research*. PMID: 38215673
4. Mutagenesis, breeding, and characterization of sake yeast strains with low production of dimethyl trisulfide precursor.. *Journal of bioscience and bioengineering*. PMID: 32800812
5. Parsing Autism Heterogeneity: Transcriptomic Subgrouping of Imaging-Derived Phenotypes in Autism.. *Biological psychiatry. Cognitive neuroscience and neuroimaging*. PMID: 40651720

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 93.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 4LDQ, 4LDR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4LDQ, 4LDR）+ AlphaFold高质量预测（pLDDT=94.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000649, IPR005251, IPR042529, IPR011559, IPR027363; Pfam: PF01008 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APIP | 0.992 | 0.000 | — |
| MTAP | 0.991 | 0.000 | — |
| ENOPH1 | 0.975 | 0.000 | — |
| ADI1 | 0.909 | 0.229 | — |
| CYREN | 0.890 | 0.000 | — |
| PNP | 0.881 | 0.000 | — |
| ACAD10 | 0.842 | 0.000 | — |
| ACAD11 | 0.822 | 0.000 | — |
| ADD3 | 0.796 | 0.000 | — |
| ADD2 | 0.796 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000040663.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| D6W4B7 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| EBI-21246012 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-26346|pubmed:23695164| |
| SVF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| KTR3 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 4LDQ, 4LDR | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell projection / Nucleoplasm, Cytosol; 额外: Nucleoli fibrillar cente | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. MRI1 — Methylthioribose-1-phosphate isomerase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小369 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BV20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000037757-MRI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MRI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BV20
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:58:57

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000037757-MRI1/subcellular

![](https://images.proteinatlas.org/42744/474_F6_5_red_green.jpg)
![](https://images.proteinatlas.org/42744/474_F6_6_red_green.jpg)
![](https://images.proteinatlas.org/42744/480_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/42744/480_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/42744/510_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/42744/510_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BV20-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
