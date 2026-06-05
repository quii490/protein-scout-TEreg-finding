---
type: protein-evaluation
gene: "PYGO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PYGO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PYGO1 |
| 蛋白名称 | Pygopus homolog 1 |
| 蛋白大小 | 419 aa / 45.1 kDa |
| UniProt ID | Q9Y3Y4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 45.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 2VP7, 2VPB, 2VPD, 2VPE, 2VPG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052475, IPR019786, IPR011011, IPR001965, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Pygo1 and Pygo2 roles in Wnt signaling in mammalian kidney development.. *BMC biology*. PMID: 17425782
2. Identification of novel genes associated with exercise and calorie restriction effects in skeletal muscle.. *Aging*. PMID: 37310402
3. KMT2A-rearranged sarcoma with unusual fusion gene CBX6::KMT2A::PYGO1.. *Virchows Archiv : an international journal of pathology*. PMID: 37713130
4. Expression of Wnt signaling proteins in rare congenital bladder disorders.. *Journal of pediatric urology*. PMID: 39500676
5. Overexpression of PYGO1 promotes early cardiac lineage development in human umbilical cord mesenchymal stromal/stem cells by activating the Wnt/β-catenin pathway.. *Human cell*. PMID: 36085540

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 14.1% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 24.8% |
| 低置信 (pLDDT<50) 占比 | 58.7% |
| 有序区域 (pLDDT>70) 占比 | 16.5% |
| 可用 PDB 条目 | 2VP7, 2VPB, 2VPD, 2VPE, 2VPG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 16.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052475, IPR019786, IPR011011, IPR001965, IPR019787; Pfam: PF00628 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCL9 | 0.999 | 0.977 | — |
| H3-4 | 0.981 | 0.908 | — |
| H3-3B | 0.981 | 0.908 | — |
| H3C12 | 0.981 | 0.908 | — |
| H3C13 | 0.981 | 0.908 | — |
| H3-2 | 0.965 | 0.908 | — |
| H3-5 | 0.965 | 0.908 | — |
| CTNNB1 | 0.949 | 0.331 | — |
| BCL9L | 0.920 | 0.278 | — |
| H3C2 | 0.910 | 0.908 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LENG8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| SPTBN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| BCL9 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:18498752|imex:IM-17354 |
| lgs | psi-mi:"MI:0096"(pull down) | pubmed:18498752|imex:IM-17354 |
| Rab9b | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |
| DLST | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| B2M | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| CALR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| TP53BP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| NEK7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 2VP7, 2VPB, 2VPD, 2VPE, 2VPG | pLDDT=55.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PYGO1 — Pygopus homolog 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3Y4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171016-PYGO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PYGO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3Y4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000171016-PYGO1/subcellular

![](https://images.proteinatlas.org/42248/475_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/42248/475_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/42248/477_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/42248/477_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/42248/479_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/42248/479_B10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3Y4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
