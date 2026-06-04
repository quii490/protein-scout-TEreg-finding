---
type: protein-evaluation
gene: "CBWD3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBWD3 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBWD3 / ZNG1C |
| 蛋白名称 | Zinc-regulated GTPase metalloprotein activator 1C |
| 蛋白大小 | 395 aa / 44.0 kDa |
| UniProt ID | Q5JTY5 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBWD3/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 3/10 | ×4 | 12 | HPA: Plasma membrane; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 395 aa / 44.0 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.4; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 17 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Identification and Validation of Alkaliptosis Resistance-Associated Genes in Prostate Cancer Via Transcriptome Sequencing and Prediction of Biochemical Recurrence.. *Mol Biotechnol*. PMID: 39760809

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 35.2% |
| 置信残基 (pLDDT 70-90) 占比 | 33.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBWD3/CBWD3-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=75.4，有序区 68.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKRD20A3 | 0.000 | 0.000 | — |
| SETD2 | 0.000 | 0.000 | — |
| FAM72C | 0.000 | 0.000 | — |
| MRPL33 | 0.000 | 0.000 | — |
| ANKRD20A2 | 0.000 | 0.000 | — |
| ANKRD20A4 | 0.000 | 0.000 | — |
| FAM72B | 0.000 | 0.000 | — |
| RIMKLA | 0.000 | 0.000 | — |
| TRIM49C | 0.000 | 0.000 | — |
| HSPB3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q5JTY5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q96E35 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 17，IntAct interactions: 30
- 调控相关比例: 0 / 17 = 0%

**评价**: STRING 17 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 无 | pLDDT=75.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 17 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CBWD3 — Zinc-regulated GTPase metalloprotein activator 1C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小395 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTY5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196873-CBWD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBWD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTY5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CBWD3/CBWD3-PAE.png]]




