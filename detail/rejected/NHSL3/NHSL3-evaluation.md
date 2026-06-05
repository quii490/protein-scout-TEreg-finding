---
type: protein-evaluation
gene: "NHSL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation, recovery, re-evaluation]
status: rejected
---

## NHSL3 -- REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NHSL3 / KIAA1522 |
| 蛋白名称 | NHS-like protein 3 |
| 蛋白大小 | 1035 aa / 107.1 kDa |
| UniProt ID | Q9P206 |
| 数据采集时间 | 2026-06-03 23:45:23 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | x1 | 8 | 1035 aa / 107.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (<= 20 -> 10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=48.8; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR024845; Pfam: PF15273 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1522 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.8 |
| 高置信度残基 (pLDDT>90) 占比 | 1.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 68.9% |
| 有序区域 (pLDDT>70) 占比 | 9.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.8），有序残基占 9.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024845; Pfam: PF15273 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCK1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SFRP1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| ABI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| NCK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BAIAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLMAP | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:24255178|imex:IM-21541 |
| Ddb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.8 + PDB: 无 | pLDDT=48.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: (REJECTED) (REJECTED)

**核心优势**:
1. NHSL3 -- NHS-like protein 3，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小1035 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P206
- Protein Atlas: https://www.proteinatlas.org/search/NHSL3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NHSL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P206
- STRING: https://string-db.org/network/9606.NHSL3
- Packet data timestamp: 2026-06-03 23:45:23

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P206-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
