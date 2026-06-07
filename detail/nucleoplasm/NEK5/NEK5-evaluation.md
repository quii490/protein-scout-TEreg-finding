---
type: protein-evaluation
gene: "NEK5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEK5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEK5 |
| 蛋白名称 | Serine/threonine-protein kinase Nek5 |
| 蛋白大小 | 708 aa / 81.4 kDa |
| UniProt ID | Q6P3R8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cell projection, cilium; Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | ×1 | 10 | 708 aa / 81.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR051131, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cell projection, cilium; Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cilium (GO:0005929)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Structurally divergent and recurrently mutated regions of primate genomes.. *Cell*. PMID: 38428424
2. Development and validation of a kinase-related gene signature as a novel diagnostic and prognostic model for prostate cancer.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 39965532
3. Nek5 interacts with mitochondrial proteins and interferes negatively in mitochondrial mediated cell death and respiration.. *Cellular signalling*. PMID: 25725288
4. NEK5 regulates cell cycle progression during mouse oocyte maturation and preimplantation embryonic development.. *Molecular reproduction and development*. PMID: 31304658
5. Nek5 promotes centrosome integrity in interphase and loss of centrosome cohesion in mitosis.. *The Journal of cell biology*. PMID: 25963817

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.2 |
| 高置信度残基 (pLDDT>90) 占比 | 26.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 51.0% |
| 有序区域 (pLDDT>70) 占比 | 38.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.2），有序残基占 38.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR051131, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRGUK | 0.554 | 0.000 | — |
| COX11 | 0.507 | 0.000 | — |
| UBXN10 | 0.500 | 0.000 | — |
| BCLAF1 | 0.500 | 0.000 | — |
| LRRC18 | 0.480 | 0.000 | — |
| NEK2 | 0.429 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAM1 | psi-mi:"MI:0089"(protein array) | pubmed:17360592 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| NEK1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| FTL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 5
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.2 + PDB: 无 | pLDDT=59.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cell projection, cilium,  / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 6 + 5 interactions | 数据充分 |

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
1. NEK5 — Serine/threonine-protein kinase Nek5，非常新颖，仅有少数基础研究。
2. 蛋白大小708 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P3R8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197168-NEK5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEK5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P3R8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000197168-NEK5/subcellular

![](https://images.proteinatlas.org/37016/2101_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/37016/2101_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/37016/606_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/37016/606_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/37016/608_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/37016/608_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P3R8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P3R8 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 4..259; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR051131;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197168-NEK5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FTL | Bioplex | false |
| NEK1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
