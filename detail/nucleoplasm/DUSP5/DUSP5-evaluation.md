---
type: protein-evaluation
gene: "DUSP5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUSP5 — REJECTED (研究热度过高 (PubMed strict=200，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP5 / VH3 |
| 蛋白名称 | Dual specificity protein phosphatase 5 |
| 蛋白大小 | 384 aa / 42.0 kDa |
| UniProt ID | Q16690 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 384 aa / 42.0 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=200 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.6; PDB: 2G6Z |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 200 |
| PubMed broad count | 299 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: VH3 |

**关键文献**:
1. Human umbilical cord-derived mesenchymal stem cells not only ameliorate blood glucose but also protect vascular endothelium from diabetic damage through a paracrine mechanism mediated by MAPK/ERK signaling.. *Stem cell research & therapy*. PMID: 35715841
2. DUSP5 deficiency suppresses the progression of acute kidney injury by enhancing autophagy through AMPK/ULK1 pathway.. *Translational research : the journal of laboratory and clinical medicine*. PMID: 39218057
3. DUSP5 regulated by YTHDF1-mediated m6A modification promotes epithelial-mesenchymal transition and EGFR-TKI resistance via the TGF-β/Smad signaling pathway in lung adenocarcinoma.. *Cancer cell international*. PMID: 38872157
4. MAP4K Family Kinases and DUSP Family Phosphatases in T-Cell Signaling and Systemic Lupus Erythematosus.. *Cells*. PMID: 31766293
5. Developing the new diagnostic model by integrating bioinformatics and machine learning for osteoarthritis.. *Journal of orthopaedic surgery and research*. PMID: 39695788

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 49.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 22.1% |
| 有序区域 (pLDDT>70) 占比 | 74.2% |
| 可用 PDB 条目 | 2G6Z |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=77.6，有序区 74.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036873; Pfam: PF00782, PF00581 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.969 | 0.189 | — |
| MAPK9 | 0.959 | 0.189 | — |
| MAPK3 | 0.942 | 0.441 | — |
| ITIH4 | 0.899 | 0.092 | — |
| DUSP11 | 0.896 | 0.048 | — |
| MAPK1 | 0.888 | 0.441 | — |
| SNRK | 0.839 | 0.000 | — |
| MAPK14 | 0.813 | 0.243 | — |
| MAPK12 | 0.804 | 0.243 | — |
| MAPK13 | 0.799 | 0.243 | — |

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
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 2G6Z | pLDDT=77.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
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
1. DUSP5 — Dual specificity protein phosphatase 5，有一定研究基础，但仍存在niche空间。
2. 蛋白大小384 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 200 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 200 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16690
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138166-DUSP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16690
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:21:21

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16690-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16690 |
| SMART | SM00195;SM00404;SM00450; |
| UniProt Domain [FT] | DOMAIN 19..141; /note="Rhodanese"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00173"; DOMAIN 178..319; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR000340;IPR008343;IPR029021;IPR001763;IPR036873;IPR016130;IPR003595;IPR000387;IPR020422; |
| Pfam | PF00782;PF00581; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138166-DUSP5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FTL | Bioplex | false |
| IPO7 | Biogrid | false |
| LZTS2 | Biogrid | false |
| MAPK1 | Intact | false |
| RPS15 | Biogrid | false |
| ZNRD2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
