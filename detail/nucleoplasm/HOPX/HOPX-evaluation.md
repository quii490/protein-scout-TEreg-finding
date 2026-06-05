---
type: protein-evaluation
gene: "HOPX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HOPX — REJECTED (研究热度过高 (PubMed strict=177，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HOPX / HOD, HOP, LAGY, NECC1, OB1 |
| 蛋白名称 | Homeodomain-only protein |
| 蛋白大小 | 73 aa / 8.3 kDa |
| UniProt ID | Q9BPY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 73 aa / 8.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=177 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001356, IPR009057, IPR039162; Pfam: PF00046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 177 |
| PubMed broad count | 309 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HOD, HOP, LAGY, NECC1, OB1 |

**关键文献**:
1. β-Hydroxybutyrate suppresses colorectal cancer.. *Nature*. PMID: 35477756
2. Decoding the development of the human hippocampus.. *Nature*. PMID: 31942070
3. An ex vivo model to induce early fibrosis-like changes in human precision-cut lung slices.. *American journal of physiology. Lung cellular and molecular physiology*. PMID: 28314802
4. Gut microbiota modulate CD8(+) T cell immunity in gastric cancer through Butyrate/GPR109A/HOPX.. *Gut microbes*. PMID: 38319728
5. Type 2 alveolar cells are stem cells in adult lung.. *The Journal of clinical investigation*. PMID: 23921127

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 56.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 19.2% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 76.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.7，有序区 76.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR039162; Pfam: PF00046 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC2 | 0.973 | 0.301 | — |
| NKX2-5 | 0.756 | 0.045 | — |
| SRF | 0.755 | 0.136 | — |
| LRIG1 | 0.744 | 0.047 | — |
| NKX2-1 | 0.697 | 0.045 | — |
| LGR5 | 0.695 | 0.047 | — |
| SFTPC | 0.680 | 0.000 | — |
| SOX2 | 0.662 | 0.000 | — |
| HSP90AA1 | 0.657 | 0.625 | — |
| FAM107A | 0.644 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| INTS13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PICK1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCF12 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ZSCAN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| HOXB9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| TLX3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 无 | pLDDT=82.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. HOPX — Homeodomain-only protein，研究基础较多，新颖性有限。
2. 蛋白大小73 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 177 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 177 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BPY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171476-HOPX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HOPX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BPY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000171476-HOPX/subcellular

![](https://images.proteinatlas.org/30180/1591_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30180/1591_C2_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/30180/1878_D1_61_blue_red_green.jpg)
![](https://images.proteinatlas.org/30180/1878_D1_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/30180/2175_C1_22_blue_red_green.jpg)
![](https://images.proteinatlas.org/30180/2175_C1_37_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BPY8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
