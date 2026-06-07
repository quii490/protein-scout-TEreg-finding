---
type: protein-evaluation
gene: "DUSP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUSP1 — REJECTED (研究热度过高 (PubMed strict=764，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP1 / CL100, MKP1, PTPN10, VH1 |
| 蛋白名称 | Dual specificity protein phosphatase 1 |
| 蛋白大小 | 367 aa / 39.3 kDa |
| UniProt ID | P28562 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Cytosol; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 367 aa / 39.3 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=764 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.2; PDB: 6APX, 6D65, 6D66, 6D67 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 764 |
| PubMed broad count | 1702 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CL100, MKP1, PTPN10, VH1 |

**关键文献**:
1. DUSP1 protects against ischemic acute kidney injury through stabilizing mtDNA via interaction with JNK.. *Cell death & disease*. PMID: 37935658
2. Acetylation-regulated DUSP1 deficiency contributes to renal fibrosis progression.. *Theranostics*. PMID: 40213676
3. Systems biology-based analysis exploring shared biomarkers and pathogenesis of myocardial infarction combined with osteoarthritis.. *Frontiers in immunology*. PMID: 39086489
4. The Ninj1/Dusp1 Axis Contributes to Liver Ischemia Reperfusion Injury by Regulating Macrophage Activation and Neutrophil Infiltration.. *Cellular and molecular gastroenterology and hepatology*. PMID: 36731792
5. RNA-Seq transcriptome profiling identifies CRISPLD2 as a glucocorticoid responsive gene that modulates cytokine function in airway smooth muscle cells.. *PloS one*. PMID: 24926665

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 50.7% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 20.7% |
| 有序区域 (pLDDT>70) 占比 | 72.2% |
| 可用 PDB 条目 | 6APX, 6D65, 6D66, 6D67 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6APX, 6D65, 6D66, 6D67）+ AlphaFold高质量预测（pLDDT=79.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036873; Pfam: PF00782, PF00581 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK14 | 0.998 | 0.831 | — |
| MAPK1 | 0.996 | 0.828 | — |
| MAPK3 | 0.996 | 0.830 | — |
| MAPK8 | 0.992 | 0.420 | — |
| MAPK11 | 0.973 | 0.243 | — |
| MAPK12 | 0.972 | 0.526 | — |
| MAPK9 | 0.968 | 0.421 | — |
| FOS | 0.961 | 0.130 | — |
| MAPK13 | 0.955 | 0.243 | — |
| ZFP36 | 0.934 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 6APX, 6D65, 6D66, 6D67 | pLDDT=79.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DUSP1 — Dual specificity protein phosphatase 1，有一定研究基础，但仍存在niche空间。
2. 蛋白大小367 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 764 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 764 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P28562
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120129-DUSP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P28562
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:33

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000120129-DUSP1/subcellular

![](https://images.proteinatlas.org/69577/1332_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/69577/1332_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/69577/1358_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/69577/1358_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/69577/1586_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/69577/1586_C7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P28562-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P28562 |
| SMART | SM00195;SM00404;SM00450; |
| UniProt Domain [FT] | DOMAIN 20..137; /note="Rhodanese"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00173"; DOMAIN 173..314; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR000340;IPR008343;IPR029021;IPR001763;IPR036873;IPR016130;IPR003595;IPR000387;IPR020422; |
| Pfam | PF00782;PF00581; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120129-DUSP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAPK1 | Intact, Biogrid | true |
| MAPK14 | Intact, Biogrid | true |
| MAPK3 | Intact, Biogrid | true |
| SKP2 | Intact, Biogrid | true |
| AMFR | Biogrid | false |
| MAPK8 | Biogrid | false |
| MAPK9 | Biogrid | false |
| NEURL3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
