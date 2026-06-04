---
type: protein-evaluation
gene: "N4BP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## N4BP3 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | N4BP3 |
| 蛋白名称 | N4BP3 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | N4BP3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

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
| PubMed strict count | 14 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. N4BP3 promotes breast cancer metastasis via NEDD4-mediated E-cadherin ubiquitination and degradation.. *Cancer Lett*. PMID: 36162713
2. N4BP3 Activates TLR4-NF-κB Pathway in Inflammatory Bowel Disease by Promoting K48-Linked IκBα Ubiquitination.. *J Inflamm Res*. PMID: 40487287
3. The Nedd4 binding protein 3 is required for anterior neural development in Xenopus laevis.. *Dev Biol*. PMID: 28104388
4. N4BP3 facilitates NOD2-MAPK/NF-κB pathway in inflammatory bowel disease through mediating K63-linked RIPK2 ubiquitination.. *Cell Death Discov*. PMID: 39420190
5. Whole transcriptome landscape in HAPE under the stress of environment at high altitudes: new insights into the mechanisms of hypobaric hypoxia tolerance.. *Front Immunol*. PMID: 39328420

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 32.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 17.8% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 37.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 37.3%。

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
| uniprotkb:Q8CG73 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q9Y2K6 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q04917 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:P31946-2 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:P61981 | psi-mi:"MI:0007" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:O15049 | psi-mi:"MI:0030" | - |
| uniprotkb:P03372 | psi-mi:"MI:0676" | psi-mi:"MI:1060"(spoke expansi |
| uniprotkb:Q9H4P4 | psi-mi:"MI:0397" | - |
| uniprotkb:O00560 | psi-mi:"MI:0397" | - |
| uniprotkb:Q8IYE0 | psi-mi:"MI:0397" | - |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 30
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 无 | pLDDT=64.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 9 + 30 interactions | 数据充分 |

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
1. N4BP3 — N4BP3 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/N4BP3
- Protein Atlas: https://www.proteinatlas.org/search/N4BP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=N4BP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/N4BP3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
