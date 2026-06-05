---
type: protein-evaluation
gene: "SET"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SET — REJECTED (研究热度过高 (PubMed strict=151207，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SET |
| 蛋白名称 | Protein SET |
| 蛋白大小 | 290 aa / 33.5 kDa |
| UniProt ID | Q01105 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Lipid droplets; UniProt: Cytoplasm, cytosol; Endoplasmic reticulum; Nucleus, nucleopl |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 33.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=151207 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.6; PDB: 2E50, 7MTO, 9I15 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037231, IPR002164; Pfam: PF00956 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Lipid droplets | Enhanced |
| UniProt | Cytoplasm, cytosol; Endoplasmic reticulum; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- lipid droplet (GO:0005811)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 151207 |
| PubMed broad count | 799531 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A SET domain-containing protein and HCF-1 maintain transgenerational epigenetic memory.. *Nature communications*. PMID: 41513691
2. SET protein as an epigenetics target.. *Epigenomics*. PMID: 38131159
3. Mutational scanning pinpoints distinct binding sites of key ATGL regulators in lipolysis.. *Nature communications*. PMID: 38514628
4. The SET domain protein PsKMT3 regulates histone H3K36 trimethylation and modulates effector gene expression in the soybean pathogen Phytophthora sojae.. *Molecular plant pathology*. PMID: 36748674
5. Enrichr-KG: bridging enrichment analysis across multiple libraries.. *Nucleic acids research*. PMID: 37166973

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 55.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 63.5% |
| 可用 PDB 条目 | 2E50, 7MTO, 9I15 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2E50, 7MTO, 9I15）+ AlphaFold高质量预测（pLDDT=77.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037231, IPR002164; Pfam: PF00956 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANP32A | 0.999 | 0.628 | — |
| PPP2CA | 0.928 | 0.292 | — |
| NME1 | 0.912 | 0.292 | — |
| GZMA | 0.911 | 0.510 | — |
| SRSF6 | 0.890 | 0.000 | — |
| XPO1 | 0.885 | 0.292 | — |
| NUP214 | 0.879 | 0.000 | — |
| APEX1 | 0.859 | 0.292 | — |
| SGO2 | 0.832 | 0.593 | — |
| ELAVL1 | 0.804 | 0.301 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEA | psi-mi:"MI:0018"(two hybrid) | pubmed:11148284|imex:IM-19994 |
| NSD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| RRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HORMAD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CPNE4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H1-4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 2E50, 7MTO, 9I15 | pLDDT=77.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Endoplasmic reticulum; Nucleus / Nucleoplasm; 额外: Lipid droplets | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SET — Protein SET，研究基础较多，新颖性有限。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 151207 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 151207 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01105
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119335-SET/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SET
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01105
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000119335-SET/subcellular

![](https://images.proteinatlas.org/63683/1152_C1_3_red_green.jpg)
![](https://images.proteinatlas.org/63683/1152_C1_4_red_green.jpg)
![](https://images.proteinatlas.org/63683/1156_C1_5_red_green.jpg)
![](https://images.proteinatlas.org/63683/1156_C1_6_red_green.jpg)
![](https://images.proteinatlas.org/63683/1178_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/63683/1178_E10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01105-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
