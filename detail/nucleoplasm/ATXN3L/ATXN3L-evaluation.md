---
type: protein-evaluation
gene: "ATXN3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATXN3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATXN3L / ATX3L, MJDL |
| 蛋白名称 | Ataxin-3-like protein |
| 蛋白大小 | 355 aa / 40.7 kDa |
| UniProt ID | Q9H3M9 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:26:38 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 355 aa / 40.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=11 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=71.2; PDB: 3O65 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: 3; Pfam: 3; IPR033865, IPR006155... |
| PPI 网络 | 6/10 | x3 | 18 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | -- | max +3 | 1.5 | PDB + AlphaFold 双源验证: +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **132.5/180** | |
| **归一化总分 (/1.83)** | | | **72.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 355 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATX3L, MJDL |

**关键文献**:
1. Gene editing for Spinocerebellar ataxia type 3 taking advantage of the human ATXN3L paralog as replacement gene.. *Gene therapy*. PMID: 40721863
2. Crystal structure of a Josephin-ubiquitin complex: evolutionary restraints on ataxin-3 deubiquitinating activity.. *The Journal of biological chemistry*. PMID: 21118805
3. Differential Expression of DUB Genes in Ovarian Cells Treated with Di-2-Ethylhexyl Phthalate.. *International journal of molecular sciences*. PMID: 32143396
4. Diagnostic implications of ubiquitination-related gene signatures in Alzheimer's disease.. *Scientific reports*. PMID: 38730027
5. Distinct X-chromosome SNVs from some sporadic AD samples.. *Scientific reports*. PMID: 26648445

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 29.0% |
| 置信残基 (pLDDT 70-90) 占比 | 34.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 63.1% |
| 可用 PDB 条目 | 3O65 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=71.2），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033865, IPR006155, IPR003903; Pfam: PF02099, PF16619, PF02809 |

**染色质调控潜力分析**: 存在 6 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITPR3 | 0.941 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HMGA1 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| MTA2 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2

**评价**: 互作网络中等：STRING 15 预测 + IntAct 2 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 3O65 | pLDDT=71.2, v6 | 预测+实验 |
| 定位 | UniProt | Nucleus | 单一来源 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 72.4/100

**核心优势**:
1. ATXN3L -- Ataxin-3-like protein，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小355 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 已有PDB实验结构：3O65。
4. 存在 6 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9H3M9
- Protein Atlas: https://www.proteinatlas.org/search/ATXN3L
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATXN3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3M9
- STRING: https://string-db.org/network/9606.ATXN3L
- Packet data timestamp: 2026-06-03 03:26:38

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3M9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
