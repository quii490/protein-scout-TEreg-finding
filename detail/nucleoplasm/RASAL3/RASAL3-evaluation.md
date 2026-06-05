---
type: protein-evaluation
gene: "RASAL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RASAL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RASAL3 |
| 蛋白名称 | RAS protein activator like-3 |
| 蛋白大小 | 1011 aa / 111.9 kDa |
| UniProt ID | Q86YV0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cytoplasm; Cytoplasm, cell cortex |
| 蛋白大小 | 8/10 | ×1 | 8 | 1011 aa / 111.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR039360, IPR023152, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Cytoplasm; Cytoplasm, cell cortex | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytoplasmic side of membrane (GO:0098562)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CCDC88B interacts with RASAL3 and ARHGEF2 and regulates dendritic cell function in neuroinflammation and colitis.. *Communications biology*. PMID: 38200184
2. Ras-mediated homeostatic control of front-back signaling dictates cell polarity.. *bioRxiv : the preprint server for biology*. PMID: 37693515
3. RASAL3 predicts overall survival and CD8+ T lymphocyte infiltration in lung adenocarcinoma.. *Journal of cellular and molecular medicine*. PMID: 36420686
4. RASAL3, a novel hematopoietic RasGAP protein, regulates the number and functions of NKT cells.. *European journal of immunology*. PMID: 25652366
5. The Ras GTPase-activating protein Rasal3 supports survival of naive T cells.. *PloS one*. PMID: 25793935

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 27.8% |
| 置信残基 (pLDDT 70-90) 占比 | 28.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 36.6% |
| 有序区域 (pLDDT>70) 占比 | 56.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 56.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR039360, IPR023152, IPR001936; Pfam: PF25321, PF00616 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SASH3 | 0.839 | 0.000 | — |
| TBC1D10C | 0.809 | 0.000 | — |
| RRAS | 0.748 | 0.099 | — |
| NRAS | 0.741 | 0.099 | — |
| HRAS | 0.713 | 0.099 | — |
| KRAS | 0.701 | 0.099 | — |
| RRAS2 | 0.696 | 0.099 | — |
| MRAS | 0.692 | 0.099 | — |
| HCST | 0.631 | 0.000 | — |
| RASA3 | 0.615 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000341905.5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Lat | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-25620|pubmed:24584089 |
| Pag1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:26512138|imex:IM-25616 |
| RABGEF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HNRNPK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DEF6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 无 | pLDDT=66.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cell cortex / Nucleoplasm, Plasma membrane | 一致 |
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
1. RASAL3 — RAS protein activator like-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1011 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YV0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105122-RASAL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RASAL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YV0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000105122-RASAL3/subcellular

![](https://images.proteinatlas.org/43417/1848_C10_10_cr5abb8f979dedd_red_green.jpg)
![](https://images.proteinatlas.org/43417/1848_C10_19_cr5abb8f979ef8a_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86YV0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
