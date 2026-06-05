---
type: protein-evaluation
gene: "CNNM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNNM1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNNM1 |
| 蛋白名称 | Metal transporter |
| 蛋白大小 | 972 aa / 106.4 kDa |
| UniProt ID | A0A8Q3SIV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Plasma membrane, Cytosol; UniProt: Cell membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 972 aa / 106.4 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cell membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 27 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The cytoplasmic domains of the CNNM family of transmembrane proteins modulate the ion channel-kinase TRPM7.. *J Biol Chem*. PMID: 40962059
2. Differential regulation of magnesium transporters Slc41, Cnnm and Trpm6-7 in the kidney of salmonids may represent evolutionary adaptations to high salinity environments.. *BMC Genomics*. PMID: 39614204
3. Intestinal Mg(2+) accumulation induced by cnnm mutations decreases the body size by suppressing TORC2 signaling in Caenorhabditis elegans.. *Dev Biol*. PMID: 38373693
4. Insight on the hub gene associated signatures and potential therapeutic agents in epilepsy and glioma.. *Brain Res Bull*. PMID: 37192718
5. The Benefits of Nanosized Magnesium Oxide in Fish Megalobrama amblycephala: Evidence in Growth Performance, Redox Defense, Glucose Metabolism, and Magnesium Homeostasis.. *Antioxidants (Basel)*. PMID: 37507890

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 19.3% |
| 置信残基 (pLDDT 70-90) 占比 | 29.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 35.7% |
| 有序区域 (pLDDT>70) 占比 | 49.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 49.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBSL | 0.000 | 0.000 | — |
| CBS | 0.000 | 0.000 | — |
| PTP4A2 | 0.000 | 0.000 | — |
| PTP4A1 | 0.000 | 0.000 | — |
| COX11 | 0.000 | 0.000 | — |
| TRPM6 | 0.000 | 0.000 | — |
| GMPS | 0.000 | 0.000 | — |
| SLC41A1 | 0.000 | 0.000 | — |
| HPSE2 | 0.000 | 0.000 | — |
| ATIC | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9NRU3-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q12974 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NRU3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 无 | pLDDT=62.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CNNM1 -- Metal transporter，非常新颖，仅有少数基础研究。
2. 蛋白大小972 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A8Q3SIV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119946-CNNM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNNM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A8Q3SIV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0A8Q3SIV9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
