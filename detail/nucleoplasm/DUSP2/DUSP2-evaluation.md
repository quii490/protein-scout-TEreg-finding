---
type: protein-evaluation
gene: "DUSP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUSP2 — REJECTED (研究热度过高 (PubMed strict=127，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP2 / PAC1 |
| 蛋白名称 | Dual specificity protein phosphatase 2 |
| 蛋白大小 | 314 aa / 34.4 kDa |
| UniProt ID | Q05923 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Nucleoplasm; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 34.4 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=127 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.4; PDB: 1M3G |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 127 |
| PubMed broad count | 274 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAC1 |

**关键文献**:
1. GABA regulates IL-1β production in macrophages.. *Cell reports*. PMID: 36476877
2. Simplified algorithm for genetic subtyping in diffuse large B-cell lymphoma.. *Signal transduction and targeted therapy*. PMID: 37032379
3. PTBP1 Regulates DNMT3B Alternative Splicing by Interacting With RALY to Enhance the Radioresistance of Prostate Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39287090
4. Protein phosphatases in systemic autoimmunity.. *Immunometabolism (Cobham, Surrey)*. PMID: 39944077
5. BATF2 activates DUSP2 gene expression and up-regulates NF-κB activity via phospho-STAT3 dephosphorylation.. *International immunology*. PMID: 29534174

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 77.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 4.5% |
| 有序区域 (pLDDT>70) 占比 | 93.0% |
| 可用 PDB 条目 | 1M3G |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.4，有序区 93.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036873; Pfam: PF00782, PF00581 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.942 | 0.189 | — |
| MAPK9 | 0.936 | 0.189 | — |
| MAPK3 | 0.908 | 0.441 | — |
| MAPK1 | 0.841 | 0.365 | — |
| MAPK14 | 0.802 | 0.308 | — |
| MAPK11 | 0.785 | 0.272 | — |
| MAPK12 | 0.768 | 0.243 | — |
| SNRK | 0.762 | 0.000 | — |
| MAPK13 | 0.759 | 0.243 | — |
| SYN2 | 0.614 | 0.610 | — |

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
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 1M3G | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DUSP2 — Dual specificity protein phosphatase 2，有一定研究基础，但仍存在niche空间。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 127 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 127 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05923
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158050-DUSP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05923
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:21:11

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000158050-DUSP2/subcellular

![](https://images.proteinatlas.org/71920/1337_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/71920/1337_C11_3_red_green.jpg)
![](https://images.proteinatlas.org/71920/1338_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/71920/1338_C11_5_red_green.jpg)
![](https://images.proteinatlas.org/71920/1422_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/71920/1422_E5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q05923-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
