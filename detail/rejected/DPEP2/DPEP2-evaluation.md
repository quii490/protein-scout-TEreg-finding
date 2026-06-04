---
type: protein-evaluation
gene: "DPEP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DPEP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPEP2 |
| 蛋白名称 | Dipeptidase 2 |
| 蛋白大小 | 486 aa / 53.4 kDa |
| UniProt ID | Q9H4A9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 486 aa / 53.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.7; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000180, IPR032466, IPR008257; Pfam: PF01244 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- side of membrane (GO:0098552)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 28 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Dipeptidase‑2 is a prognostic marker in lung adenocarcinoma that is correlated with its sensitivity to cisplatin.. *Oncology reports*. PMID: 37449493
2. The Trim32-DPEP2 axis is an inflammatory switch in macrophages during intestinal inflammation.. *Cell death and differentiation*. PMID: 40021897
3. Exploring the Potential Regulatory Mechanisms of Mitophagy in Ischemic Cardiomyopathy.. *International journal of general medicine*. PMID: 40492232
4. Generation of novel lipid metabolism-based signatures to predict prognosis and immunotherapy response for colorectal adenocarcinoma.. *Scientific reports*. PMID: 39060344
5. Integrating SWATH-MS proteomics and transcriptome analysis to preliminarily identify three DEGs as biomarkers for proliferative diabetic retinopathy.. *Proteomics. Clinical applications*. PMID: 34528762

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 69.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 22.0% |
| 有序区域 (pLDDT>70) 占比 | 73.8% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.7，有序区 73.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000180, IPR032466, IPR008257; Pfam: PF01244 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPEP3 | 0.702 | 0.361 | — |
| CNDP2 | 0.579 | 0.000 | — |
| DPEP1 | 0.555 | 0.000 | — |
| TRIML1 | 0.499 | 0.000 | — |
| BEND5 | 0.479 | 0.000 | — |
| ANPEP | 0.477 | 0.000 | — |
| HYAL2 | 0.456 | 0.454 | — |
| CHPF2 | 0.454 | 0.454 | — |
| TAZ | 0.443 | 0.429 | — |
| GALNS | 0.441 | 0.420 | — |

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
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 无 | pLDDT=82.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DPEP2 — Dipeptidase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4A9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167261-DPEP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPEP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4A9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:55
