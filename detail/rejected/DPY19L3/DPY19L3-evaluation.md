---
type: protein-evaluation
gene: "DPY19L3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DPY19L3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPY19L3 |
| 蛋白名称 | Protein C-mannosyl-transferase DPY19L3 |
| 蛋白大小 | 716 aa / 83.2 kDa |
| UniProt ID | Q6ZPD9 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPY19L3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPY19L3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules; UniProt: Endoplasmic reticulum membrane; Endoplasmic reticulum membra |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 716 aa / 83.2 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.7; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018732, IPR047465; Pfam: PF10034 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules | Approved |
| UniProt | Endoplasmic reticulum membrane; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 13 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The C-Mannosylome of Human Induced Pluripotent Stem Cells Implies a Role for ADAMTS16 C-Mannosylation in Eye Development.. *Molecular & cellular proteomics : MCP*. PMID: 33975020
2. Topological analysis of DPY19L3, a human C-mannosyltransferase.. *The FEBS journal*. PMID: 29405629
3. Identification of DPY19L3 as the C-mannosyltransferase of R-spondin1 in human cells.. *Molecular biology of the cell*. PMID: 26764097
4. Involvement of DPY19L3 in Myogenic Differentiation of C2C12 Myoblasts.. *Molecules (Basel, Switzerland)*. PMID: 34577156
5. Dpy-19 like 3-mediated C-mannosylation and expression levels of RPE-spondin in human tumor cell lines.. *Oncology letters*. PMID: 28781692

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 73.3% |
| 置信残基 (pLDDT 70-90) 占比 | 18.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 91.9% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.7，有序区 91.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018732, IPR047465; Pfam: PF10034 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSR3 | 0.615 | 0.000 | — |
| CCDC126 | 0.583 | 0.000 | — |
| TSR1 | 0.580 | 0.000 | — |
| TSR2 | 0.576 | 0.000 | — |
| PRPSAP1 | 0.561 | 0.000 | — |
| UNC5A | 0.530 | 0.091 | — |
| PPP1R3G | 0.516 | 0.000 | — |
| RSPO3 | 0.514 | 0.454 | — |
| CHST10 | 0.512 | 0.066 | — |
| NLRP13 | 0.506 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 无 | pLDDT=88.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Endoplasmic reticu / Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DPY19L3 — Protein C-mannosyl-transferase DPY19L3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小716 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZPD9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178904-DPY19L3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPY19L3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZPD9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:19:26




