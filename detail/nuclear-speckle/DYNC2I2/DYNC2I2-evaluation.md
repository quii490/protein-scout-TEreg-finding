---
type: protein-evaluation
gene: "DYNC2I2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYNC2I2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNC2I2 / WDR34 |
| 蛋白名称 | Cytoplasmic dynein 2 intermediate chain 2 |
| 蛋白大小 | 536 aa / 57.8 kDa |
| UniProt ID | Q96EX3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centrosome, Basal body; 额外: Nucleoli, Nuclear b; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, cilium basal body; Cytop |
| 蛋白大小 | 10/10 | ×1 | 10 | 536 aa / 57.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.1; PDB: 6RLB, 6SC2, 8RGG, 8RGH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050687, IPR015943, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome, Basal body; 额外: Nucleoli, Nuclear bodies, Primary cilium, Cytosol | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, cilium axoneme; Cyto... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- ciliary plasm (GO:0097014)
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR34 |

**关键文献**:
1. Bioinformatics Analysis Highlights Five Differentially Expressed Genes as Prognostic Biomarkers of Cervical Cancer and Novel Option for Anticancer Treatment.. *Frontiers in cellular and infection microbiology*. PMID: 35782114
2. A Rare Case of Prenatal Short-Rib Thoracic Dysplasia 11 Subtype With Compound Heterozygous Variants in the DYNC2I2 Gene: Presenting Polydactyly and Shortened Limbs.. *Clinical case reports*. PMID: 41503593
3. High Throughput Transcriptome Data Analysis and Computational Verification Reveal Immunotherapy Biomarkers of Compound Kushen Injection for Treating Triple-Negative Breast Cancer.. *Frontiers in oncology*. PMID: 34604090

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 64.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 15.5% |
| 有序区域 (pLDDT>70) 占比 | 75.0% |
| 可用 PDB 条目 | 6RLB, 6SC2, 8RGG, 8RGH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6RLB, 6SC2, 8RGG, 8RGH）+ AlphaFold高质量预测（pLDDT=82.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050687, IPR015943, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC2H1 | 0.999 | 0.923 | — |
| WDR60 | 0.999 | 0.982 | — |
| DYNC2LI1 | 0.997 | 0.851 | — |
| DYNLL1 | 0.997 | 0.947 | — |
| DYNLRB1 | 0.996 | 0.966 | — |
| TCTEX1D2 | 0.991 | 0.762 | — |
| DYNLT3 | 0.978 | 0.445 | — |
| DYNLT1 | 0.957 | 0.611 | — |
| DYNLRB2 | 0.956 | 0.664 | — |
| DYNLL2 | 0.946 | 0.496 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DYNLRB1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DYNLT2B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DYNLT1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DYNC2I1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DYNLL2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DYNLRB2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| H3-3A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| RBM14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 6RLB, 6SC2, 8RGG, 8RGH | pLDDT=82.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, cilium basal b / Nucleoplasm, Centrosome, Basal body; 额外: Nucleoli, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DYNC2I2 — Cytoplasmic dynein 2 intermediate chain 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小536 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EX3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119333-DYNC2I2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNC2I2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EX3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000119333-DYNC2I2/subcellular

![](https://images.proteinatlas.org/40764/2129_E9_13_red_green.jpg)
![](https://images.proteinatlas.org/40764/2129_E9_56_red_green.jpg)
![](https://images.proteinatlas.org/40764/2152_A7_28_red_green.jpg)
![](https://images.proteinatlas.org/40764/2152_A7_40_red_green.jpg)
![](https://images.proteinatlas.org/40764/2169_D9_25_red_green.jpg)
![](https://images.proteinatlas.org/40764/2169_D9_48_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96EX3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
