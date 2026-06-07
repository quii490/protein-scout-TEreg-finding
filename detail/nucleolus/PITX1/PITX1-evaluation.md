---
type: protein-evaluation
gene: "PITX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PITX1 — REJECTED (研究热度过高 (PubMed strict=295，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PITX1 / BFT, PTX1 |
| 蛋白名称 | Pituitary homeobox 1 |
| 蛋白大小 | 314 aa / 34.1 kDa |
| UniProt ID | P78337 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 34.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=295 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR016233, IPR009057, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 295 |
| PubMed broad count | 536 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BFT, PTX1 |

**关键文献**:
1. PITX1 plays essential functions in cancer.. *Frontiers in oncology*. PMID: 37841446
2. The single-cell transcriptomic atlas and RORA-mediated 3D epigenomic remodeling in driving corneal epithelial differentiation.. *Nature communications*. PMID: 38177186
3. Human and bacterial genetic variation shape oral microbiomes and health.. *Nature*. PMID: 41606319
4. Evolution of homeobox genes.. *Wiley interdisciplinary reviews. Developmental biology*. PMID: 23799629
5. Rewiring of the promoter-enhancer interactome and regulatory landscape in glioblastoma orchestrates gene expression underlying neurogliomal synaptic communication.. *Nature communications*. PMID: 37833281

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.1 |
| 高置信度残基 (pLDDT>90) 占比 | 17.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 43.0% |
| 低置信 (pLDDT<50) 占比 | 33.8% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.1），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR016233, IPR009057, IPR003654; Pfam: PF00046, PF03826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBX4 | 0.923 | 0.054 | — |
| TBX19 | 0.885 | 0.106 | — |
| EGR1 | 0.856 | 0.329 | — |
| POU1F1 | 0.845 | 0.292 | — |
| TBX5 | 0.815 | 0.054 | — |
| NR5A1 | 0.776 | 0.301 | — |
| FSHB | 0.727 | 0.000 | — |
| LHX3 | 0.676 | 0.000 | — |
| MIPOL1 | 0.652 | 0.000 | — |
| LHX4 | 0.650 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DVL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RHOXF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT34 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRR20D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLEKHB2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| C10orf55 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZBTB32 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MYOZ3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.1 + PDB: 无 | pLDDT=61.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PITX1 — Pituitary homeobox 1，研究基础较多，新颖性有限。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 295 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 295 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78337
- Protein Atlas: https://www.proteinatlas.org/ENSG00000069011-PITX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PITX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78337
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000069011-PITX1/subcellular

![](https://images.proteinatlas.org/8743/110_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8743/110_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8743/111_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8743/111_G6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78337-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78337 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR016233;IPR009057;IPR003654; |
| Pfam | PF00046;PF03826; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000069011-PITX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IPO13 | Intact, Biogrid | true |
| MAGED1 | Intact, Biogrid | true |
| RBPMS | Intact, Biogrid | true |
| SIRT1 | Biogrid, Bioplex | true |
| TRIM23 | Intact, Biogrid | true |
| AKAP8L | Intact | false |
| ARID5A | Intact | false |
| BPIFA1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
