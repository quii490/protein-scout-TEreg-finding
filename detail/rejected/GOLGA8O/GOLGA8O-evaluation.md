---
type: protein-evaluation
gene: "GOLGA8O"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLGA8O — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA8O |
| 蛋白名称 | Golgin subfamily A member 8O |
| 蛋白大小 | 632 aa / 71.5 kDa |
| UniProt ID | A6NCC3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 632 aa / 71.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024858, IPR043937, IPR043976; Pfam: PF19046, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- Golgi cis cisterna (GO:0000137)
- Golgi cisterna membrane (GO:0032580)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.2 |
| 高置信度残基 (pLDDT>90) 占比 | 36.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 34.2% |
| 有序区域 (pLDDT>70) 占比 | 56.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.2），有序残基占 56.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024858, IPR043937, IPR043976; Pfam: PF19046, PF15070 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GTF3C6 | 0.542 | 0.000 | — |
| GOLGB1 | 0.489 | 0.420 | — |
| STX5 | 0.482 | 0.420 | — |
| GTF3C5 | 0.474 | 0.000 | — |
| GOSR1 | 0.459 | 0.420 | — |
| GOLGA6L1 | 0.427 | 0.099 | — |
| TRMT5 | 0.425 | 0.051 | — |
| GPR89A | 0.418 | 0.000 | — |
| CCDC82 | 0.404 | 0.000 | — |
| MBD3L5 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000423159.2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-21138|pubmed:21911577 |
| EBI-8869561 | psi-mi:"MI:0018"(two hybrid) | imex:IM-21138|pubmed:21911577 |
| EBI-8869494 | psi-mi:"MI:0018"(two hybrid) | imex:IM-21138|pubmed:21911577 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 3
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.2 + PDB: 无 | pLDDT=69.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 10 + 3 interactions | 数据充分 |

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
1. GOLGA8O — Golgin subfamily A member 8O，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小632 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NCC3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000206127-GOLGA8O/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA8O
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NCC3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
