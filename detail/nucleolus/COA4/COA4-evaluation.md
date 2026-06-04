---
type: protein-evaluation
gene: "COA4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COA4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COA4 / CHCHD8, E2IG2 |
| 蛋白名称 | Cytochrome c oxidase assembly factor 4 homolog, mitochondrial |
| 蛋白大小 | 87 aa / 10.1 kDa |
| UniProt ID | Q9NYJ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Nucleoli fibrillar center; 额外: Mitochondria; UniProt: Mitochondrion |
| 蛋白大小 | 5/10 | x1 | 5 | 87 aa / 10.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.5; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR010625, IPR039870; Pfam: PF06747 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center; 额外: Mitochondria | Approved |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mitochondrial intermembrane space (GO:0005758)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.5 |
| 高置信度残基 (pLDDT>90) 占比 | 70.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.9% |
| 中等置信 (pLDDT 50-70) 占比 | 23.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 77.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=87.5，有序区 77.0%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010625, IPR039870; Pfam: PF06747 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COA6 | 0.843 | 0.000 | — |
| CHCHD4 | 0.803 | 0.000 | — |
| COX17 | 0.802 | 0.162 | — |
| CMC4 | 0.797 | 0.071 | — |
| CMC2 | 0.776 | 0.000 | — |
| MRPL17 | 0.757 | 0.000 | — |
| COX19 | 0.753 | 0.000 | — |
| CHCHD7 | 0.694 | 0.000 | — |
| BCS1L | 0.677 | 0.000 | — |
| COA7 | 0.648 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=87.5 + PDB: 无 | pLDDT=87.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion / Nucleoplasm, Nucleoli fibrillar center; 额外: Mitoch | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. COA4 -- Cytochrome c oxidase assembly factor 4 homolog, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小87 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYJ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181924-COA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYJ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
