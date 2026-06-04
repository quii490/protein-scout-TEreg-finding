---
type: protein-evaluation
gene: "CLPB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLPB2 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLPB2 |
| 蛋白名称 | CLPB2 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | CLPB2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 5/10 | x1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | 获取失败 |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Bacterial rotary export ATPases are allosterically regulated by the nucleotide second messenger cyclic-di-GMP.. *J Biol Chem*. PMID: 26265469
2. Structural mapping of the ClpB ATPases of Plasmodium falciparum: Targeting protein folding and secretion for antimalarial drug design.. *Protein Sci*. PMID: 26130467
3. Crystal structure and solution characterization of the thioredoxin-2 from Plasmodium falciparum, a constituent of an essential parasitic protein export complex.. *Biochem Biophys Res Commun*. PMID: 25475729
4. The Arabidopsis ClpB/Hsp100 family of proteins: chaperones for stress and chloroplast development.. *Plant J*. PMID: 17144892
5. In vivo induced clpB1 gene of Vibrio cholerae is involved in different stress responses and affects in vivo cholera toxin production.. *Biochem Biophys Res Commun*. PMID: 15883026

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

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
| uniprotkb:P74361 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:A0A2U2GXJ3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P72833 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 8
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 0 + 8 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLPB2 -- CLPB2 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/CLPB2
- Protein Atlas: https://www.proteinatlas.org/search/CLPB2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLPB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CLPB2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
