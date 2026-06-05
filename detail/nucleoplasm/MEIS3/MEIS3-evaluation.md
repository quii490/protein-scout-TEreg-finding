---
type: protein-evaluation
gene: "MEIS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEIS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEIS3 / MRG2 |
| 蛋白名称 | Homeobox protein Meis3 |
| 蛋白大小 | 375 aa / 41.1 kDa |
| UniProt ID | Q99687 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 375 aa / 41.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR008422, IPR032453, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 56 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MRG2 |

**关键文献**:
1. Disruption of GPSM1/CSF1 signaling reprograms tumor-associated macrophages to overcome anti-PD-1 resistance in colorectal cancer.. *Journal for immunotherapy of cancer*. PMID: 40010765
2. PTK7 modulates Wnt signaling activity via LRP6.. *Development (Cambridge, England)*. PMID: 24353057
3. The Meis3 protein and retinoid signaling interact to pattern the Xenopus hindbrain.. *Developmental biology*. PMID: 15196951
4. High MEIS3 Expression Indicates a Poor Prognosis for Patients with Stage II/III Colorectal Cancer.. *Frontiers in bioscience (Landmark edition)*. PMID: 38179750
5. Integrative multi-omics identifies MEIS3 as a diagnostic biomarker and immune modulator in hypertrophic cardiomyopathy.. *Frontiers in immunology*. PMID: 41200169

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 19.7% |
| 低置信 (pLDDT<50) 占比 | 38.1% |
| 有序区域 (pLDDT>70) 占比 | 42.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 42.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR008422, IPR032453, IPR050224; Pfam: PF05920, PF16493 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PBX4 | 0.904 | 0.483 | — |
| PBX2 | 0.726 | 0.261 | — |
| PBX3 | 0.688 | 0.261 | — |
| PBX1 | 0.634 | 0.261 | — |
| MEIS2 | 0.527 | 0.457 | — |
| MYBBP1A | 0.499 | 0.076 | — |
| HOXB1 | 0.459 | 0.094 | — |
| ZNF676 | 0.457 | 0.066 | — |
| FOXD3 | 0.454 | 0.045 | — |
| HHEX | 0.438 | 0.301 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hoxa13 | psi-mi:"MI:0018"(two hybrid) | pubmed:15617687|imex:IM-19599 |
| TRAF3IP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| TSGA10IP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATXN1L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM110B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRPF31 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM161B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TCL1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LENG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCDC116 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MEIS3 — Homeobox protein Meis3，非常新颖，仅有少数基础研究。
2. 蛋白大小375 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99687
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105419-MEIS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEIS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99687
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEIS3/IF_images/U-251_MG_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MEIS3/IF_images/U-2_OS_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000105419-MEIS3/subcellular

![](https://images.proteinatlas.org/46699/766_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/46699/766_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/46699/778_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/46699/778_H1_4_red_green.jpg)
![](https://images.proteinatlas.org/46699/990_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/46699/990_B9_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99687-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
