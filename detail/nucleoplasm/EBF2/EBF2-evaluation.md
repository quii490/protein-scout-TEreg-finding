---
type: protein-evaluation
gene: "EBF2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EBF2 — REJECTED (研究热度过高 (PubMed strict=113，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EBF2 / COE2 |
| 蛋白名称 | Transcription factor COE2 |
| 蛋白大小 | 575 aa / 62.6 kDa |
| UniProt ID | Q9HAK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 575 aa / 62.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=113 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032200, IPR038173, IPR032201, IPR038006, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
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
| PubMed strict count | 113 |
| PubMed broad count | 190 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COE2 |

**关键文献**:
1. SOX4 facilitates brown fat development and maintenance through EBF2-mediated thermogenic gene program in mice.. *Cell death and differentiation*. PMID: 39402212
2. EBF2 Links KMT2D-Mediated H3K4me1 to Suppress Pancreatic Cancer Progression via Upregulating KLLN.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38015024
3. Control of murine brown adipocyte development by GATA6.. *Developmental cell*. PMID: 37647897
4. Thyroid hormones are required for thermogenesis of beige adipocytes induced by Zfp423 inactivation.. *Cell reports*. PMID: 39580797
5. Seedlings Transduce the Depth and Mechanical Pressure of Covering Soil Using COP1 and Ethylene to Regulate EBF1/EBF2 for Soil Emergence.. *Current biology : CB*. PMID: 26748855

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 45.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 35.1% |
| 有序区域 (pLDDT>70) 占比 | 59.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.2，有序区 59.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032200, IPR038173, IPR032201, IPR038006, IPR013783; Pfam: PF16422, PF16423, PF01833 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF423 | 0.891 | 0.309 | — |
| TMTC1 | 0.847 | 0.000 | — |
| PRDM16 | 0.791 | 0.095 | — |
| PPARG | 0.790 | 0.000 | — |
| ID1 | 0.694 | 0.000 | — |
| EBF3 | 0.691 | 0.460 | — |
| UCP1 | 0.650 | 0.000 | — |
| EHMT1 | 0.633 | 0.000 | — |
| SIX1 | 0.617 | 0.000 | — |
| HNRNPU | 0.597 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 无 | pLDDT=72.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EBF2 — Transcription factor COE2，研究基础较多，新颖性有限。
2. 蛋白大小575 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 113 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 113 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000221818-EBF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EBF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000221818-EBF2/subcellular

![](https://images.proteinatlas.org/3954/1876_G1_11_cr5ba363e41eac9_red_green.jpg)
![](https://images.proteinatlas.org/3954/1876_G1_27_cr5ba363c362660_red_green.jpg)
![](https://images.proteinatlas.org/3954/1901_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/3954/1901_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/3954/1909_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/3954/1909_B1_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HAK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
