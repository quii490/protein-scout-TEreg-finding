---
type: protein-evaluation
gene: "ANXA2R"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ANXA2R — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANXA2R / AX2R, C5orf39 |
| 蛋白名称 | Annexin-2 receptor |
| 蛋白大小 | 193 aa / 21.7 kDa |
| UniProt ID | Q3ZCQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 193 aa / 21.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031449; Pfam: PF15721 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AX2R, C5orf39 |

**关键文献**:
1. Investigating the role of cathepsins in breast cancer progression: a Mendelian randomization study.. *Frontiers in oncology*. PMID: 39944834
2. Multiomics Data Reveal the Important Role of ANXA2R in T Cell-mediated Rejection After Renal Transplantation.. *Transplantation*. PMID: 37677931
3. Oxidative stress-induced hypermethylation and low expression of ANXA2R: Novel insights into the dysfunction of melanocytes in vitiligo.. *Journal of dermatological science*. PMID: 38806323
4. ZNNT1 long noncoding RNA induces autophagy to inhibit tumorigenesis of uveal melanoma by regulating key autophagy gene expression.. *Autophagy*. PMID: 31462126
5. Potential prognostic and therapeutic value of ANXA8 in renal cell carcinoma: based on the comprehensive analysis of annexins family.. *BMC cancer*. PMID: 37464398

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 49.7% |
| 低置信 (pLDDT<50) 占比 | 37.8% |
| 有序区域 (pLDDT>70) 占比 | 12.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 12.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031449; Pfam: PF15721 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANXA2 | 0.997 | 0.000 | — |
| S100A10 | 0.733 | 0.000 | — |
| CXCL12 | 0.527 | 0.000 | — |
| PLAT | 0.520 | 0.000 | — |
| AXL | 0.485 | 0.000 | — |
| CXCR4 | 0.459 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CNOT1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CNOT3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CNOT9 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CNOT6L | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| TNKS1BP1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CNOT7 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 6
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 无 | pLDDT=55.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 6 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ANXA2R — Annexin-2 receptor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小193 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3ZCQ2
- Protein Atlas: https://www.proteinatlas.org/search/ANXA2R
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANXA2R
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3ZCQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ANXA2R/ANXA2R-PAE.png]]
