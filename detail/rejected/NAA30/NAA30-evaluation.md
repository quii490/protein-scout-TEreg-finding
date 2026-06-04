---
type: protein-evaluation
gene: "NAA30"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NAA30 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAA30 |
| 蛋白名称 | NAA30 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | NAA30 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Quantitative proteomics combined independent PRM analysis reveals the mitochondrial and synaptic mechanism underlying norisoboldine's antidepressant effects.. *Transl Psychiatry*. PMID: 39358323
2. Human NAA30 can rescue yeast mak3∆ mutant growth phenotypes.. *Biosci Rep*. PMID: 33600573
3. Knockdown of NAT12/NAA30 reduces tumorigenic features of glioblastoma-initiating cells.. *Mol Cancer*. PMID: 26292663
4. Molecular role of NAA38 in thermostability and catalytic activity of the human NatC N-terminal acetyltransferase.. *Structure*. PMID: 36638802
5. Expanded in vivo substrate profile of the yeast N-terminal acetyltransferase NatC.. *J Biol Chem*. PMID: 36567016

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 39.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 44.8% |
| 有序区域 (pLDDT>70) 占比 | 43.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 43.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q03503 | psi-mi:"MI:0676" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:P53743 | psi-mi:"MI:0397" | - |
| uniprotkb:Q02197 | psi-mi:"MI:0018" | - |
| uniprotkb:P10592 | psi-mi:"MI:0676" | - |
| uniprotkb:O95400 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q6P5F9 | psi-mi:"MI:0096" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:P30822 | psi-mi:"MI:0096" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q9BU76 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q9BRA0 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:P20290 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 无 | pLDDT=63.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

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
1. NAA30 — NAA30 (UniProt未获取)，非常新颖，仅有少数基础研究。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/NAA30
- Protein Atlas: https://www.proteinatlas.org/search/NAA30
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAA30
- AlphaFold: https://alphafold.ebi.ac.uk/entry/NAA30
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
