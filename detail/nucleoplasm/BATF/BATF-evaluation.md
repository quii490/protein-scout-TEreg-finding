---
type: protein-evaluation
gene: "BATF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BATF — REJECTED (研究热度过高 (PubMed strict=250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BATF |
| 蛋白名称 | Basic leucine zipper transcriptional factor ATF-like |
| 蛋白大小 | 125 aa / 14.1 kDa |
| UniProt ID | Q16520 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 125 aa / 14.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=250 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 250 |
| PubMed broad count | 469 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer.. *Nature*. PMID: 37968405
2. Blockade of LAG-3 and PD-1 leads to co-expression of cytotoxic and exhaustion gene modules in CD8(+) T cells to promote antitumor immunity.. *Cell*. PMID: 39121849
3. The role of transcription factors in shaping regulatory T cell identity.. *Nature reviews. Immunology*. PMID: 37336954
4. BATF and IRF4 cooperate to counter exhaustion in tumor-infiltrating CAR T cells.. *Nature immunology*. PMID: 34282330
5. Modular pooled discovery of synthetic knockin sequences to program durable cell therapies.. *Cell*. PMID: 37714135

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 52.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 39.2% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 59.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.7，有序区 59.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUNB | 0.997 | 0.937 | — |
| JUN | 0.997 | 0.609 | — |
| IRF4 | 0.995 | 0.392 | — |
| BATF3 | 0.945 | 0.311 | — |
| JUND | 0.933 | 0.417 | — |
| BATF2 | 0.921 | 0.000 | — |
| FOS | 0.915 | 0.000 | — |
| RORC | 0.887 | 0.069 | — |
| STAT3 | 0.882 | 0.124 | — |
| BCL6 | 0.850 | 0.066 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNAPC5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DDIT3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EBI-6398437 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23021777|imex:IM-18126 |
| EBI-6398451 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23021777|imex:IM-18126 |
| EBI-4422030 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23021777|imex:IM-18126 |
| EBI-4566324 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23021777|imex:IM-18126 |
| Irf4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23021777|imex:IM-18126 |
| ENSMUSP00000040706.6 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23021777|imex:IM-18126 |
| EBI-6398447 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23021777|imex:IM-18126 |
| JUNB | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:29997244|imex:IM-26441| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 无 | pLDDT=80.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BATF — Basic leucine zipper transcriptional factor ATF-like，研究基础较多，新颖性有限。
2. 蛋白大小125 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 250 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 250 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16520
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156127-BATF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BATF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16520
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000156127-BATF/subcellular

![](https://images.proteinatlas.org/59588/1070_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/59588/1070_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/59588/1076_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/59588/1076_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/59588/1391_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/59588/1391_C7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16520-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16520 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 26..89; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR000837;IPR004827;IPR046347; |
| Pfam | PF00170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156127-BATF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDIT3 | Intact, Biogrid | true |
| JUNB | Intact, Biogrid | true |
| ATF4 | Intact | false |
| CEBPA | Intact | false |
| CEBPG | Intact | false |
| COX8A | Intact | false |
| FGFR3 | Intact | false |
| GARS1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
