---
type: protein-evaluation
gene: "TACC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TACC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TACC1 / KIAA1103 |
| 蛋白名称 | Transforming acidic coiled-coil-containing protein 1 |
| 蛋白大小 | 805 aa / 87.8 kDa |
| UniProt ID | O75410 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 8/10 | ×1 | 8 | 805 aa / 87.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039915, IPR007707; Pfam: PF05010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Midbody; Mem... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- midbody (GO:0030496)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 109 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1103 |

**关键文献**:
1. A landscape of driver mutations in melanoma.. *Cell*. PMID: 22817889
2. Transforming fusions of FGFR and TACC genes in human glioblastoma.. *Science (New York, N.Y.)*. PMID: 22837387
3. Temporal and spatial expression of TACC1 in the mouse and human.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 16496324
4. Uterine Sarcoma With FGFR1-TACC1 Gene Fusion: A Case Report and Review of the Literature.. *International journal of gynecological pathology : official journal of the International Society of Gynecological Pathologists*. PMID: 36302190
5. Analysis of the toxicity and mechanisms of osteoporosis caused by cigarette toxicants using network toxicology and molecular docking techniques.. *The Science of the total environment*. PMID: 40925315

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 24.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 64.1% |
| 有序区域 (pLDDT>70) 占比 | 27.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 27.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039915, IPR007707; Pfam: PF05010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CKAP5 | 0.985 | 0.705 | — |
| LSM7 | 0.873 | 0.474 | — |
| FGFR1 | 0.873 | 0.084 | — |
| YEATS4 | 0.846 | 0.328 | — |
| CEP120 | 0.838 | 0.098 | — |
| TACC2 | 0.836 | 0.776 | — |
| AURKA | 0.833 | 0.655 | — |
| FGFR3 | 0.807 | 0.048 | — |
| SPICE1 | 0.786 | 0.000 | — |
| TDRD7 | 0.745 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AURKB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15064709 |
| TDRD7 | psi-mi:"MI:0018"(two hybrid) | pubmed:14603251 |
| CKAP5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14603251 |
| LSM7 | psi-mi:"MI:0018"(two hybrid) | pubmed:14603251 |
| SNRPG | psi-mi:"MI:0096"(pull down) | pubmed:14603251 |
| AURKA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14603251 |
| YEATS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:11903063 |
| ENSP00000321703.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| HTT | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-17394|pubmed:23275563 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 无 | pLDDT=56.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, micro / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TACC1 — Transforming acidic coiled-coil-containing protein 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小805 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75410
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147526-TACC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TACC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75410
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000147526-TACC1/subcellular

![](https://images.proteinatlas.org/56841/1877_G2_14_cr5b741bdf6a1e2_blue_red_green.jpg)
![](https://images.proteinatlas.org/56841/1877_G2_16_cr5b741bdf6a818_blue_red_green.jpg)
![](https://images.proteinatlas.org/56841/912_B6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/56841/912_B6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75410-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75410 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 215..297; /note="SPAZ 1"; DOMAIN 359..507; /note="SPAZ 2" |
| InterPro | IPR039915;IPR007707; |
| Pfam | PF05010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147526-TACC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTRC | Intact, Biogrid | true |
| CKAP5 | Intact, Biogrid | true |
| STX5 | Intact, Biogrid | true |
| TDRD7 | Intact, Biogrid | true |
| YEATS4 | Intact, Biogrid | true |
| ALK | Biogrid | false |
| AURKA | Biogrid | false |
| AURKB | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
