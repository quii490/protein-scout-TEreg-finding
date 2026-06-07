---
type: protein-evaluation
gene: "BTG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BTG2 — REJECTED (研究热度过高 (PubMed strict=526，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTG2 / PC3 |
| 蛋白名称 | Protein BTG2 |
| 蛋白大小 | 158 aa / 17.4 kDa |
| UniProt ID | P78543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 158 aa / 17.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=526 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.3; PDB: 3DJU, 3E9V |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002087, IPR033332, IPR036054; Pfam: PF07742 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 526 |
| PubMed broad count | 679 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PC3 |

**关键文献**:
1. Predicting the molecular mechanism of ginger targeting PRMT1/BTG2 axis to inhibit gastric cancer based on WGCNA and machine algorithms.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 40446574
2. Btg2 Promotes Focal Segmental Glomerulosclerosis via Smad3-Dependent Podocyte-Mesenchymal Transition.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37749872
3. Simplified algorithm for genetic subtyping in diffuse large B-cell lymphoma.. *Signal transduction and targeted therapy*. PMID: 37032379
4. Linggui Zhugan decoction ameliorating mitochondrial damage of doxorubicin-induced cardiotoxicity by modulating the AMPK-FOXO3a pathway targeting BTG2.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 39986226
5. Emerging role of anti-proliferative protein BTG1 and BTG2.. *BMB reports*. PMID: 35880434

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 72.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 76.6% |
| 可用 PDB 条目 | 3DJU, 3E9V |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3DJU, 3E9V）+ AlphaFold高质量预测（pLDDT=85.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002087, IPR033332, IPR036054; Pfam: PF07742 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRMT1 | 0.992 | 0.628 | — |
| CNOT7 | 0.963 | 0.784 | — |
| HOXB9 | 0.913 | 0.236 | — |
| TP53 | 0.888 | 0.000 | — |
| CNOT8 | 0.881 | 0.598 | — |
| CNOT6L | 0.840 | 0.312 | — |
| NR4A1 | 0.775 | 0.000 | — |
| DUSP1 | 0.739 | 0.000 | — |
| GADD45A | 0.714 | 0.000 | — |
| FOS | 0.696 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 3DJU, 3E9V | pLDDT=85.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BTG2 — Protein BTG2，研究基础较多，新颖性有限。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 526 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 526 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159388-BTG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000159388-BTG2/subcellular

![](https://images.proteinatlas.org/2355/77_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2355/77_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2355/78_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2355/78_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/2355/92_F3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/2355/92_F3_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78543 |
| SMART | SM00099; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002087;IPR033332;IPR036054; |
| Pfam | PF07742; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159388-BTG2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CNOT7 | Intact, Biogrid | true |
| CNOT8 | Intact, Biogrid | true |
| AR | Intact | false |
| HOXB9 | Biogrid | false |
| PRMT1 | Biogrid | false |
| SKP2 | Biogrid | false |
| TRIM6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
