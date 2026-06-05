---
type: protein-evaluation
gene: "CSAD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSAD — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSAD / CSD |
| 蛋白名称 | Cysteine sulfinic acid decarboxylase |
| 蛋白大小 | 493 aa / 55.0 kDa |
| UniProt ID | Q9Y600 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum, Vesicles, Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 493 aa / 55.0 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=96.5; PDB: 2JIS |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR002129, IPR015424, IPR015421; Pfam: PF00282 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Vesicles, Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 183 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CSD |

**关键文献**:
1. Taurine Alleviates Experimental Colitis by Enhancing Intestinal Barrier Function and Inhibiting Inflammatory Response through TLR4/NF-κB Signaling.. *Journal of agricultural and food chemistry*. PMID: 38761152
2. Mammalian CSAD and GADL1 have distinct biochemical properties and patterns of brain expression.. *Neurochemistry international*. PMID: 26327310
3. CSAD inhibits excessive inflammation during viral infections through the NF-κB signaling pathway.. *Journal of virology*. PMID: 40952115
4. HNF4α Regulates CSAD to Couple Hepatic Taurine Production to Bile Acid Synthesis in Mice.. *Gene expression*. PMID: 29871716
5. Dermatofibrosarcoma Protuberans (DFSP): Diagnostics and Molecular Pathology.. *Current treatment options in oncology*. PMID: 41032154

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.5 |
| 高置信度残基 (pLDDT>90) 占比 | 96.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 98.1% |
| 可用 PDB 条目 | 2JIS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度（pLDDT=96.5，有序区 98.1%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002129, IPR015424, IPR015421; Pfam: PF00282 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDO1 | 0.984 | 0.000 | — |
| ADO | 0.969 | 0.000 | — |
| AGXT2 | 0.948 | 0.092 | — |
| BAAT | 0.929 | 0.000 | — |
| GAD2 | 0.914 | 0.071 | — |
| GGT7 | 0.908 | 0.000 | — |
| GGT5 | 0.908 | 0.000 | — |
| GGT6 | 0.907 | 0.000 | — |
| GGT1 | 0.907 | 0.000 | — |
| GAD1 | 0.904 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=96.5 + PDB: 2JIS | pLDDT=96.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Endoplasmic reticulum, Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CSAD -- Cysteine sulfinic acid decarboxylase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小493 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y600
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139631-CSAD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSAD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y600
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y600-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
